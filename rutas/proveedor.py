from flask import Blueprint, flash, redirect, render_template, request
from models import Proveedor
from configs import db
from decorators import login_requerido
from services.entidad_activa import obtener_entidad_activa

# Blueprint for managing suppliers
proveedor_bp = Blueprint('proveedor', __name__)

# Route to list all active suppliers
@proveedor_bp.route('/proveedores')
@login_requerido
def lista_proveedores():
    proveedores = Proveedor.query.filter_by(estado='Activo').all()
    return render_template('proveedores/proveedor.html', proveedores=proveedores)

# Route to add a new supplier
@proveedor_bp.route('/proveedores/agregar', methods=['GET', 'POST'])
@login_requerido
def agregar_proveedor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        correo = request.form['correo']

        nuevo_proveedor = Proveedor(
            nombre=nombre,
            telefono=telefono,
            direccion=direccion,
            correo=correo
        )
        db.session.add(nuevo_proveedor)
        db.session.commit()
        flash("✅ Proveedor agregado correctamente.", "proveedor")
        return redirect('/proveedores')

    return render_template('proveedores/agregar_proveedor.html')

# Route to edit an existing supplier
@proveedor_bp.route('/proveedores/editar/<int:id>', methods=['GET', 'POST'])
@login_requerido
def editar_proveedor(id):
    # This utility ensures the supplier exists and is active
    proveedor = obtener_entidad_activa(Proveedor, id, "Proveedor")

    if request.method == 'POST':
        proveedor.nombre = request.form['nombre']
        proveedor.telefono = request.form['telefono']
        proveedor.direccion = request.form['direccion']
        proveedor.correo = request.form['correo']
        db.session.commit()
        flash("✏️ Proveedor actualizado correctamente.", "proveedor")
        return redirect('/proveedores')

    return render_template('proveedores/editar_proveedores.html', proveedor=proveedor)

# Route to deactivate (soft-delete) a supplier
@proveedor_bp.route('/proveedores/eliminar/<int:id>', methods=['GET', 'POST'])
@login_requerido
def eliminar_proveedor(id):
    # This utility already checks for existence and active status
    proveedor = obtener_entidad_activa(Proveedor, id, "Proveedor")

    proveedor.estado = 'Inactivo'
    db.session.commit()
    flash("🗑️ Proveedor eliminado correctamente.", "proveedor")

    return redirect('/proveedores')
