from flask import Blueprint, flash, redirect, render_template, request
from modelo import Producto, Categoria, Proveedor, db
from decorators.auth import login_requerido, permiso_requerido
from utils.utils import obtener_entidad_activa

# Create blueprint for product management
productos_bp = Blueprint('productos', __name__)

# Main product view; supports 'gestion' (management) or 'solo_lectura' (read-only) mode
@productos_bp.route('/productos')
@productos_bp.route('/productos/<modo>')
@login_requerido
@permiso_requerido("ver_productos")
def productos(modo=None):
    productos = Producto.query.filter_by(estado='Activo').all()
    categorias = Categoria.query.all()
    proveedores = Proveedor.query.all()

    if modo not in ['gestion', 'solo_lectura']:
        modo = 'gestion'

    return render_template(
        'producto/productos.html',
        productos=productos,
        categorias=categorias,
        proveedores=proveedores,
        modo=modo
    )

# Add a new product
@productos_bp.route('/producto/agregar', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("crear_productos")
def agregar_producto():
    categorias = Categoria.query.all()
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        codigo = request.form['codigo']
        existente = Producto.query.filter_by(codigo_producto=codigo).first()

        if existente:
            flash("❌ El producto ya existe.", "aggproducto")
            return redirect('/producto/agregar')

        nombre = request.form['nombre']
        precio = request.form['precio']
        categoria_id = int(request.form['categoria'])
        cantidad_stock = request.form['cantidad_stock']
        stock_minimo = request.form['stock_minimo']
        proveedor_id = int(request.form['proveedor'])

        imagen_url = request.form.get('imagen') or None

        nuevo_producto = Producto(
            codigo_producto=codigo,
            nombre=nombre,
            precio=precio,
            categoria_id=categoria_id,
            cantidad_stock=cantidad_stock,
            stock_minimo=stock_minimo,
            id_proveedor=proveedor_id,
            imagen_url=imagen_url
        )

        db.session.add(nuevo_producto)
        db.session.commit()
        flash("✅ Producto agregado correctamente.", "producto")
        return redirect('/productos')

    return render_template('producto/agregar_producto.html', proveedores=proveedores, categorias=categorias)

# Edit an existing product
@productos_bp.route('/producto/editar/<int:id>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("editar_productos")
def editar_producto(id):
    producto = obtener_entidad_activa(Producto, id, "Producto")
    categorias = Categoria.query.all()
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        producto.codigo_producto = request.form['codigo']
        producto.nombre = request.form['nombre']
        producto.precio = request.form['precio']
        producto.categoria_id = int(request.form['categoria'])
        producto.cantidad_stock = request.form['cantidad_stock']
        producto.stock_minimo = request.form['stock_minimo']
        producto.id_proveedor = int(request.form['proveedor'])
        producto.imagen_url = request.form.get('imagen') or None

        db.session.commit()
        flash("✏️ Producto actualizado correctamente.", "producto")
        return redirect('/productos')

    return render_template(
        'producto/editar_producto.html',
        producto=producto,
        categorias=categorias,
        proveedores=proveedores
    )

# Soft-delete (deactivate) a product
@productos_bp.route('/producto/eliminar/<int:id>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("eliminar_productos")
def eliminar_producto(id):
    producto = obtener_entidad_activa(Producto, id, "Producto")
    producto.estado = 'Inactivo'
    db.session.commit()
    flash("🗑️ Producto eliminado correctamente.", "producto")
    return redirect('/productos')
