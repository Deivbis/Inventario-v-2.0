from datetime import datetime
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from models import Movimiento, Producto
from configs import db
from decorators import login_requerido

# Create blueprint for the purchase module
compra_bp = Blueprint('compra', __name__)

# Main route to display purchase form (product entries into inventory)
@compra_bp.route('/compra')
@login_requerido
def compra():
    # Fetch all products, ordered alphabetically by name
    productos = Producto.query.filter_by(estado='Activo').order_by(Producto.nombre).all()
    return render_template('compra/compra.html', productos=productos)

# Route to process purchase form submission (increase stock)
@compra_bp.route('/registrar_compra', methods=['GET', 'POST'])
@login_requerido
def registrar_compra():
    codigo = request.form['codigo_producto']

    # Validate entered quantity
    try:
        cantidad = int(request.form['cantidad'])
    except ValueError:
        flash('❌ La cantidad debe ser un número entero válido.', 'errorcompra')
        return redirect(url_for('rutas.compra'))

    if cantidad <= 0:
        flash('❌ La cantidad debe ser mayor que 0.', 'errorcompra')
        return redirect(url_for('compra.compra'))

    # Search for the product by its code
    producto = Producto.query.filter_by(codigo_producto=codigo, estado='Activo').first()
    if producto:
        # Increase product stock
        producto.cantidad_stock += cantidad

        # Register stock entry in movements
        movimiento = Movimiento(
            tipo='Entrada',
            id_producto=producto.id,
            cantidad=cantidad,
            motivo='Compra',
            fecha=datetime.now()
        )

        db.session.add(movimiento)
        db.session.commit()

        flash('✅ Stock del producto actualizado correctamente.', 'compra')
    else:
        flash('❌ No se puede registrar una compra para un producto inexistente.', 'errorcompra')

    return redirect(url_for('compra.compra'))

# Route to search product via AJAX request
@compra_bp.route('/buscar_producto', methods=['GET', 'POST'])
@login_requerido
def buscar_producto():
    codigo = request.json.get('codigo')
    producto = Producto.query.filter_by(codigo_producto=codigo, estado='Activo').first()
    if producto:
        # Return product data if found
        return jsonify({
            'encontrado': True,
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'categoria_id': producto.categoria_id,
            'id_proveedor': producto.id_proveedor,
            'stock_minimo': producto.stock_minimo,
            'imagen_url': producto.imagen_url,
            'cantidad_stock': producto.cantidad_stock
        })
    else:
        # Product not found
        return jsonify({'encontrado': False})
