from datetime import datetime
import os
from werkzeug.utils import secure_filename
from flask import Blueprint, abort, flash, redirect, render_template, send_from_directory, url_for, current_app
from decorador import login_requerido

# Create blueprint for invoice-related routes
factura_bp = Blueprint('factura', __name__)

# Route to display all available invoices
@factura_bp.route('/Facturas')
@login_requerido
def facturas():
    facturas_dir = os.path.join(current_app.root_path, "static", 'facturas')  # Absolute path to invoices folder
    archivos = []

    # Validate the folder exists and list PDF files
    if os.path.exists(facturas_dir):
        for f in os.listdir(facturas_dir):
            if f.lower().endswith('.pdf'):
                ruta = os.path.join(facturas_dir, f)
                fecha_mod = datetime.fromtimestamp(os.path.getmtime(ruta)).strftime('%Y-%m-%d %H:%M:%S')
                nombre_sin_ext = os.path.splitext(f)[0]
                archivos.append({
                    'nombre': nombre_sin_ext,
                    'archivo_completo': f,
                    'fecha': fecha_mod
                })

    # Sort files by last modified date (most recent first)
    archivos.sort(key=lambda x: x['fecha'], reverse=True)
    return render_template('Facturas/facturas.html', archivos=archivos)

# Route to open a specific invoice (PDF file)
@factura_bp.route('/factura/abrir/<filename>')
@login_requerido
def abrir_factura(filename):
    filename = secure_filename(filename)  # Sanitize the filename

    # Validate the file extension
    if not filename.lower().endswith('.pdf'):
        abort(400)

    path = os.path.join(current_app.root_path, 'static', 'facturas', filename)

    # Check if the file exists
    if not os.path.exists(path):
        abort(404)

    # Serve the file to be viewed or downloaded in the browser
    return send_from_directory(os.path.join(current_app.root_path, 'static', 'facturas'), filename)

# Route to delete an existing invoice
@factura_bp.route('/factura/borrar/<filename>', methods=['GET', 'POST'])
@login_requerido
def borrar_factura(filename):
    filename = secure_filename(filename)
    path = os.path.join(current_app.root_path, 'static', 'facturas', filename)

    # Delete the file if it exists
    if os.path.exists(path):
        try:
            os.remove(path)
            flash("✅ Factura eliminada correctamente.", "factura")
        except Exception as e:
            flash(f"❌ No se pudo eliminar la factura: {e}", "errorfactura")
    else:
        flash("❌ La factura no existe.", "errorfactura")

    return redirect(url_for('factura.facturas'))
