from datetime import datetime, timedelta
import os
from pdf_utils import obtener_nombre_reporte, generar_pdf_inventario
from flask import Blueprint, flash, jsonify, redirect, render_template, request, send_from_directory, url_for
from decorador import login_requerido
from modelo import Producto, Venta, DetalleVenta, db

# Blueprint for report-related routes
reporte_bp = Blueprint('reporte', __name__)

# Route to generate general inventory report
@reporte_bp.route('/reporte/inventario')
@login_requerido
def reporte_inventario():
    # Fetch active products and all sales data
    productos = Producto.query.filter_by(estado='Activo').all()
    ventas_agregadas = Venta.query.all()
    detalles_venta = DetalleVenta.query.all()

    # Generate report PDF
    nombre_archivo = obtener_nombre_reporte()
    generar_pdf_inventario(productos, ventas_agregadas, detalles_venta, path_archivo=nombre_archivo)

    # Redirect to the reports page
    nombre_en_static = nombre_archivo.replace("static/", "").lstrip("/")
    return redirect(url_for('reporte.reportes', filename=nombre_en_static))

# Route to list all PDF reports
@reporte_bp.route('/reportes')
@login_requerido
def reportes():
    reportes_dir = os.path.join("static", "reportes")
    archivos = []

    # List PDF files with their last modified date
    if os.path.exists(reportes_dir):
        for f in os.listdir(reportes_dir):
            if f.lower().endswith('.pdf'):
                ruta = os.path.join(reportes_dir, f)
                fecha_mod = datetime.fromtimestamp(os.path.getmtime(ruta)).strftime('%Y-%m-%d %H:%M:%S')
                nombre_sin_ext = os.path.splitext(f)[0]
                archivos.append({
                    'nombre': nombre_sin_ext,
                    'archivo_completo': f,
                    'fecha': fecha_mod
                })

    # Sort by most recent
    archivos.sort(key=lambda x: x['fecha'], reverse=True)
    return render_template("Facturas/reportes.html", archivos=archivos)

# Route to open a PDF report
@reporte_bp.route('/abrir_reporte/<filename>')
@login_requerido
def abrir_reporte(filename):
    if not filename.endswith('.pdf'):
        flash("❌ Formato de archivo no válido.", "errorreporte")
        return redirect(url_for('reporte.reportes'))

    carpeta = os.path.join('static', 'reportes')
    return send_from_directory(carpeta, filename)

# Route to delete a PDF report
@reporte_bp.route('/borrar_reporte/<filename>', methods=['POST'])
@login_requerido
def borrar_reporte(filename):
    if not filename.endswith('.pdf'):
        flash("❌ Formato de archivo no válido.", "errorreporte")
        return redirect(url_for('reporte.reportes'))

    ruta = os.path.join('static', 'reportes', filename)
    if os.path.exists(ruta):
        os.remove(ruta)
        flash("🗑️ Reporte eliminado exitosamente.", "reporte")
    else:
        flash("❌ Reporte no encontrado.", "errorreporte")
    return redirect(url_for('reporte.reportes'))

# Route to return all active products as JSON (for frontend filters, etc.)
@reporte_bp.route('/productos_json')
@login_requerido
def productos_json():
    productos = Producto.query.filter_by(estado='Activo').all()
    productos_data = [{
        'id': p.id,
        'nombre': p.nombre,
        'precio': p.precio,
        'cantidad_stock': p.cantidad_stock,
        'stock_minimo': p.stock_minimo,
        'imagen_url': p.imagen_url
    } for p in productos]
    return jsonify(productos_data)

# Route to generate a custom PDF report between two dates
@reporte_bp.route('/reporte-inventario', methods=['GET', 'POST'])
@login_requerido
def generar_reporte_pdf():
    if request.method == 'POST':
        # Get selected dates from form
        fecha_inicio_str = request.form.get('fecha_inicio')
        fecha_fin_str = request.form.get('fecha_fin')

        # Validate both dates
        if not fecha_inicio_str or not fecha_fin_str:
            flash("⚠️ Debes seleccionar ambas fechas de inicio y fin.", category="advertencia")
            return redirect(request.url)

        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')
            fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d')
            fecha_fin = datetime.combine(fecha_fin.date(), datetime.max.time())  # Set to end of day
        except ValueError:
            flash("❌ Formato de fecha inválido.", category="errorReporte")
            return redirect(request.url)

        # Query all products
        productos = Producto.query.all()

        # Get sales details between dates
        detalle_ventas = DetalleVenta.query.join(DetalleVenta.venta).filter(
            Venta.fecha.between(fecha_inicio, fecha_fin)
        ).all()

        if not detalle_ventas:
            flash("⚠️ No se encontraron ventas durante el período seleccionado.", "errordfecha")
            return redirect(request.url)

        # Aggregate total products sold per product
        ventas_productos_agregados_raw = db.session.query(
            DetalleVenta.id_producto,
            db.func.sum(DetalleVenta.cantidad).label('total')
        ).join(DetalleVenta.venta).filter(
            Venta.fecha.between(fecha_inicio, fecha_fin)
        ).group_by(DetalleVenta.id_producto).all()

        # Create custom objects to be passed into the PDF report
        ventas_productos_agregados = []
        for r in ventas_productos_agregados_raw:
            producto = Producto.query.get(r.id_producto)
            ventas_productos_agregados.append(
                type('ProductoAgregado', (object,), {
                    'id': r.id_producto,
                    'codigo': producto.codigo_producto if producto else "N/A",
                    'nombre': producto.nombre if producto else "Producto eliminado",
                    'total': r.total
                })
            )

        # Generate the custom report
        ruta_pdf, total = generar_pdf_inventario(
            productos,
            ventas_productos_agregados,
            detalle_ventas,
            tipo_reporte="personalizado",
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )

        flash(f"📄 Reporte generado: {os.path.basename(ruta_pdf)}", category="reporte")
        return redirect(url_for('reporte.reportes'))

    return render_template('Facturas/formularioReportes.html')
