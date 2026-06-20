from datetime import datetime
from flask import Blueprint, jsonify, redirect, render_template, request, session, url_for
from modelo import Producto, Cliente, Venta, DetalleVenta, Movimiento, db
from decorador import login_requerido
from reports.pdf_utils import generar_factura_pdf
from utils.utils import obtener_entidad_activa

ventas_bp = Blueprint('ventas', __name__)

# Ruta para mostrar la página de ventas
@ventas_bp.route('/vender', methods=['GET', 'POST'])
@login_requerido
def vender():
    productos = Producto.query.filter_by(estado='Activo').all()
    clientes = Cliente.query.filter_by(estado='Activo').all()
    return render_template('Vender/vender.html', productos=productos, clientes=clientes)

# Ruta para registrar una venta
@ventas_bp.route('/registrar_venta', methods=['GET', 'POST'])
@login_requerido
def registrar_venta():
    data = request.get_json()
    cedula = data.get('cedula')
    productos_data = data.get('productos', [])

    # Validación básica
    if not cedula or not productos_data:
        return jsonify(error="Datos incompletos."), 400

    cliente = Cliente.query.filter_by(cedula=cedula, estado='Activo').first()
    if not cliente:
        return jsonify(error="Cliente no encontrado."), 404

    try:
        nueva_venta = Venta(
            cedula_cliente=cliente.cedula,
            fecha=datetime.now(),
            total=0  # Se actualizará luego
        )
        db.session.add(nueva_venta)
        db.session.flush()  # Obtener el ID antes del commit

        total = 0
        productos_validos = 0

        for item in productos_data:
            producto_id = item.get('id_producto')
            cantidad = item.get('cantidad')

            if not producto_id or not isinstance(cantidad, int) or cantidad <= 0:
                continue

            producto = obtener_entidad_activa(Producto, producto_id, "Producto")
            if not producto:
                continue

            if producto.cantidad_stock < cantidad:
                return jsonify(error=f"Stock insuficiente para el producto '{producto.nombre}'."), 400

            subtotal = producto.precio * cantidad

            detalle = DetalleVenta(
                id_venta=nueva_venta.id,
                id_producto=producto.id,
                cantidad=cantidad,
                precio_unitario=producto.precio,
                subtotal=subtotal
            )
            db.session.add(detalle)

            # Descontar stock
            producto.cantidad_stock -= cantidad

            # Registrar movimiento
            movimiento = Movimiento(
                tipo='Salida',
                id_producto=producto.id,
                cantidad=cantidad,
                motivo='Venta',
                fecha=datetime.now()
            )
            db.session.add(movimiento)

            total += subtotal
            productos_validos += 1

        # Validar al menos un producto válido
        if productos_validos == 0:
            db.session.rollback()
            return jsonify(error="No se pudo registrar la venta. Producto inválido o stock insuficiente."), 400

        nueva_venta.total = total
        db.session.commit()

        detalles = DetalleVenta.query.filter_by(id_venta=nueva_venta.id).all()
        factura_path = generar_factura_pdf(nueva_venta, cliente, detalles)

        return jsonify(
            mensaje="✅ Venta registrada exitosamente.",
            factura_url=factura_path
        )

    except Exception as e:
        db.session.rollback()
        return jsonify(error=f"❌ Error al registrar la venta: {str(e)}"), 500
