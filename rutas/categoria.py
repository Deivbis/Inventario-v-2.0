from flask import Blueprint, flash, redirect, render_template, request
from modelo import Categoria, db
from decorators.auth import login_requerido
from utils.utils import obtener_entidad_activa  # Utility function to fetch active entities

# Create blueprint for category management
categoria_bp = Blueprint('categoria', __name__)

# Route to list all active categories
@categoria_bp.route('/Categorias')
@login_requerido
def lista_Categoria():
    # Fetch all categories with 'Activo' status
    categorias = Categoria.query.filter_by(estado='Activo').all()
    return render_template('categoria/categoria.html', categorias=categorias)

# Route to add a new category
@categoria_bp.route('/Categoria/agregar', methods=['GET', 'POST'])
@login_requerido
def agregar_categoria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']

        # Create new category instance
        nueva_categoria = Categoria(nombre=nombre, descripcion=descripcion)

        try:
            db.session.add(nueva_categoria)
            db.session.commit()
            flash("✅ Categoría agregada correctamente.", "categoria")
            return redirect('/Categorias')
        except Exception as e:
            db.session.rollback()
            flash("❌ Error al intentar agregar la categoría.", "aggCategoria")

    return render_template('categoria/aggCategoria.html')

# Route to edit an existing category
@categoria_bp.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
@login_requerido
def editar_categoria(id):
    # Get the category only if it's active
    categoria = obtener_entidad_activa(Categoria, id, "Categoría")

    if request.method == 'POST':
        try:
            categoria.nombre = request.form['nombre']
            categoria.descripcion = request.form['descripcion']
            db.session.commit()
            flash("✏️ Categoría editada correctamente.", "categoria")
            return redirect('/Categorias')
        except Exception as e:
            db.session.rollback()
            flash("❌ Error al editar la categoría.", "editarcategoria")

    return render_template('categoria/editarCategoria.html', categoria=categoria)

# Route to deactivate (soft-delete) a category
@categoria_bp.route('/categorias/eliminar/<int:id>', methods=['GET', 'POST'])
@login_requerido
def eliminar_categoria(id):
    # Get the category only if it's active
    categoria = obtener_entidad_activa(Categoria, id, "Categoría")

    # No need to check again if it's active — already validated
    categoria.estado = 'Inactivo'
    db.session.commit()
    flash("🗑️ Categoría eliminada correctamente.", "categoria")
    
    return redirect('/Categorias')
