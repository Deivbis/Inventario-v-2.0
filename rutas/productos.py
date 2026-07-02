from flask import Blueprint, flash, redirect, render_template, request
from models import Producto, Categoria, Proveedor
from decorators import login_requerido, permiso_requerido
from services import obtener_entidad_activa, obtener_entidades_activas, guardar_entidad, editar_entidad, desactivar_entidad, obtener_entidad_por_campo

# Create blueprint for product management
productos_bp = Blueprint('productos', __name__)

# Main product view; supports 'gestion' (management) or 'solo_lectura' (read-only) mode
@productos_bp.route('/productos')
@productos_bp.route('/productos/<modo>')
@login_requerido
@permiso_requerido("ver_productos")
def productos(modo=None):
    productos = obtener_entidades_activas(Producto)
    categorias = obtener_entidades_activas(Categoria)
    proveedores = obtener_entidades_activas(Proveedor)

    if modo not in ['gestion', 'solo_lectura']:
        modo = 'gestion'

    if productos is None or categorias is None or proveedores is None:
        return render_template('404.html')

    return render_template('producto/productos.html',
                            productos=productos,
                            categorias=categorias,
                            proveedores=proveedores,
                            modo=modo)

# Add a new product
@productos_bp.route('/producto/agregar', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("crear_productos")
def agregar_producto():
    categorias = obtener_entidades_activas(Categoria)
    proveedores = obtener_entidades_activas(Proveedor)

    if categorias is None or proveedores is None:
        return render_template('404.html')

    if request.method == 'POST':

        codigo = request.form['codigo']
        nuevo_producto = Producto(codigo_producto=codigo,
                                  nombre=request.form['nombre'],
                                  precio=request.form['precio'],
                                  categoria_id=int(request.form['categoria']),
                                  cantidad_stock=request.form['cantidad_stock'],
                                  stock_minimo=request.form['stock_minimo'],
                                  id_proveedor=int(request.form['proveedor']),
                                  imagen_url=request.form.get('imagen') or None)

        existente = obtener_entidad_por_campo(Producto, 'codigo_producto', codigo)

        if existente:
            flash("❌ El producto ya existe.", "aggproducto")
            return redirect('/producto/agregar')
        
        resultado_crud = guardar_entidad(nuevo_producto)

        if resultado_crud:
            flash("✏️ Producto agregado correctamente.", "aggproducto")
            return redirect('/productos')
        else:
            flash("❌ Error al agregar el producto.", "aggproducto")

    return render_template('producto/agregar_producto.html', proveedores=proveedores, categorias=categorias)

# Edit an existing product
@productos_bp.route('/producto/editar/<int:id>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("editar_productos")
def editar_producto(id):
    producto = obtener_entidad_activa(Producto, id, "Producto")
    categorias = obtener_entidades_activas(Categoria)
    proveedores = obtener_entidades_activas(Proveedor)

    if request.method == 'POST':
        producto.codigo_producto = request.form['codigo']
        producto.nombre = request.form['nombre']
        producto.precio = request.form['precio']
        producto.categoria_id = int(request.form['categoria'])
        producto.cantidad_stock = request.form['cantidad_stock']
        producto.stock_minimo = request.form['stock_minimo']
        producto.id_proveedor = int(request.form['proveedor'])
        producto.imagen_url = request.form.get('imagen') or None

        resultado_crud = editar_entidad(producto)

        if resultado_crud:
            flash("✏️ Producto editado correctamente.", "producto")
            return redirect('/productos')   
        else:
            flash("❌ Error al editar el producto.", "producto")

    return render_template('producto/editar_producto.html',
                            producto=producto,
                            categorias=categorias,
                            proveedores=proveedores)

# Soft-delete (deactivate) a product
@productos_bp.route('/producto/eliminar/<int:id>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("eliminar_productos")
def eliminar_producto(id):

    producto = obtener_entidad_activa(Producto, id, "Producto")

    resultado_crud = desactivar_entidad(producto)

    if resultado_crud:
        flash("🗑️ Producto eliminado correctamente.", "producto")
        return redirect('/productos')
    else:
        flash("❌ Error al eliminar el producto.", "producto")
