from flask import Blueprint, flash, redirect, render_template, request
from models import Proveedor
from services import guardar_entidad, editar_entidad, desactivar_entidad, obtener_entidades_activas, obtener_entidad_activa
from decorators import login_requerido, permiso_requerido

# Blueprint for managing suppliers
proveedor_bp = Blueprint('proveedor', __name__)

# Route to list all active suppliers
@proveedor_bp.route('/proveedores')
@login_requerido
@permiso_requerido('ver_proveedores')
def lista_proveedores():
    proveedores = obtener_entidades_activas(Proveedor)

    if proveedores is None:
        return render_template('404.html')
    
    return render_template('proveedores/proveedor.html', proveedores=proveedores)

# Route to add a new supplier
@proveedor_bp.route('/proveedores/agregar', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido('crear_proveedores')
def agregar_proveedor():

    if request.method == 'POST':

        nuevo_proveedor = Proveedor(nombre=request.form['nombre'],
                                    telefono=request.form['telefono'],
                                    direccion=request.form['direccion'],
                                    correo=request.form['correo'])
        
        resultado_crud = guardar_entidad(nuevo_proveedor)

        if resultado_crud:
            flash("✏️ Proveedor agregado correctamente.", "proveedor")
            return redirect('/proveedores')
        else:
            flash("❌ Error al agregar el proveedor.", "proveedor")

    return render_template('proveedores/agregar_proveedor.html')

# Route to edit an existing supplier
@proveedor_bp.route('/proveedores/editar/<int:id>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido('editar_proveedores')
def editar_proveedor(id):

    proveedor = obtener_entidad_activa(Proveedor, id, "Proveedor")

    if request.method == 'POST':
        proveedor.nombre = request.form['nombre']
        proveedor.telefono = request.form['telefono']
        proveedor.direccion = request.form['direccion']
        proveedor.correo = request.form['correo']

        resultado_crud = editar_entidad(proveedor)

        if resultado_crud:
            flash("✏️ Proveedor editado correctamente.", "proveedor")
            return redirect('/proveedores')
        else:
            flash("❌ Error al editar el proveedor.", "proveedor")

    return render_template('proveedores/editar_proveedores.html', proveedor=proveedor)

# Route to deactivate (soft-delete) a supplier
@proveedor_bp.route('/proveedores/eliminar/<int:id>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido('eliminar_proveedores')
def eliminar_proveedor(id):

    proveedor = obtener_entidad_activa(Proveedor, id, "Proveedor")

    resultado_crud = desactivar_entidad(proveedor)

    if resultado_crud:
        flash("🗑️ Proveedor eliminado correctamente.", "proveedor")
        return redirect('/proveedores')
    else:
        flash("❌ Error al eliminar el proveedor.", "proveedor")

    return redirect('/proveedores')
