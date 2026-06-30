from flask import Blueprint, flash, redirect, render_template, request
from models import Categoria
from services import guardar_entidad,editar_entidad,desactivar_entidad,obtener_entidad_activa, obtener_entidades_activas
from decorators import login_requerido, permiso_requerido

# Create blueprint for category management
categoria_bp = Blueprint('categoria', __name__)

# Route to list all active categories
@categoria_bp.route('/Categorias')
@login_requerido
@permiso_requerido('ver_categorias')
def lista_Categoria():

    categorias = obtener_entidades_activas(Categoria)

    if categorias is None:
        return render_template('404.html')

    return render_template('categoria/categoria.html', categorias=categorias)

# Route to add a new category
@categoria_bp.route('/Categoria/agregar', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido('crear_categorias')
def agregar_categoria():
    if request.method == 'POST':

        nueva_categoria = Categoria(nombre = request.form['nombre'], descripcion = request.form['descripcion'])

        resultado_crud = guardar_entidad(nueva_categoria)

        if resultado_crud:
            flash("✏️ Categoría agregada correctamente.")
            return redirect("/Categorias")
        else:
            flash(f"❌ Error al agregar la categoría.")

    return render_template('categoria/aggCategoria.html')


# Route to edit an existing category
@categoria_bp.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido('editar_categorias')
def editar_categoria(id):

    categoria = obtener_entidad_activa(Categoria, id, "Categoría")

    if request.method == 'POST':
        categoria.nombre = request.form['nombre']
        categoria.descripcion = request.form['descripcion']
            
        resultado_crud = editar_entidad(categoria)

        if resultado_crud:
            flash("✏️ Categoría editada correctamente.")
            return redirect('/Categorias')
        else:
            flash("❌ Error al editar la categoría.")

    return render_template('categoria/editarCategoria.html', categoria=categoria)

# Route to deactivate (soft-delete) a category
@categoria_bp.route('/categorias/eliminar/<int:id>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido('eliminar_categorias')
def eliminar_categoria(id):
    # Get the category only if it's active
    categoria = obtener_entidad_activa(Categoria, id, "Categoría")

    resultado_crud = desactivar_entidad(categoria)

    if resultado_crud:
        flash("🗑️ Categoría eliminada correctamente.")
        return redirect('/Categorias')
    else:
        flash("❌ Error al eliminar la categoría.")
