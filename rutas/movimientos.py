from flask import Blueprint, render_template
from modelo import Producto, Movimiento
from decorador import login_requerido

# Create blueprint for product movement tracking
movimiento_bp = Blueprint('movimiento', __name__)

@movimiento_bp.route('/movimientos')
@login_requerido
def lista_movimientos():
    # Order movements from most recent to oldest
    movimientos = Movimiento.query.order_by(Movimiento.fecha.desc()).all()

    # Create a dictionary to map product ID to its name
    productos = {producto.id: producto.nombre for producto in Producto.query.all()}

    # Render the template with the list of movements and product names
    return render_template('movimientos/movimientos.html', movimientos=movimientos, productos=productos)
