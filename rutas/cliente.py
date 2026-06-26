from flask import Blueprint, flash, redirect, render_template, request, url_for
from models import Cliente
from configs import db
from decorators import login_requerido
from utils.utils import obtener_entidad_activa  # Utility function to fetch active entities

cliente_bp = Blueprint('cliente', __name__)

# Route to list all active clients
@cliente_bp.route('/lista-Cliente')
@login_requerido
def lista_cliente():
    # Fetch all clients with 'Activo' status
    cliente = Cliente.query.filter_by(estado='Activo').all()
    return render_template('Clientes/clientes.html', clientes=cliente)

# Route to add a new client
@cliente_bp.route('/cliente/agregar', methods=['GET', 'POST'])
@login_requerido
def agregar_cliente():
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo = request.form['correo']
        direccion = request.form['direccion']
        
        # Check if client with the same ID already exists
        cliente_existente = Cliente.query.filter_by(cedula=cedula).first()
        if cliente_existente:
            flash("⚠️ La cédula ya está registrada a otro cliente.", "errorCliente")
            return render_template('Clientes/agregarClientes.html')
        
        # Create a new client
        nuevo_cliente = Cliente(
            cedula=cedula,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            correo=correo,
            direccion=direccion
        )
        
        db.session.add(nuevo_cliente)
        db.session.commit()
        flash("✅ Cliente agregado correctamente.", "cliente")
        return redirect(url_for('cliente.lista_cliente'))

    return render_template('Clientes/agregarClientes.html')

# Route to edit an existing client
@cliente_bp.route('/cliente/editar/<int:cedula>', methods=['GET', 'POST'])
@login_requerido
def editar_cliente(cedula):
    # Fetch the client only if active
    cliente = obtener_entidad_activa(Cliente, cedula, "Cliente")
    
    if request.method == 'POST':
        cedula_nueva = request.form['cedula']
        
        # Check if the new ID already exists in another client
        cedula_existente = Cliente.query.filter(
            Cliente.cedula == cedula_nueva,
            Cliente.cedula != cedula
        ).first()
        
        if cedula_existente:
            flash("⚠️ La cédula ingresada ya está asociada a otro cliente.", "errorCliente")
            return render_template('Clientes/editarClientes.html', cliente=cliente)

        # Update client data
        cliente.cedula = cedula_nueva
        cliente.nombre = request.form['nombre']
        cliente.apellido = request.form['apellido']
        cliente.telefono = request.form['telefono']
        cliente.correo = request.form['correo']
        cliente.direccion = request.form['direccion']

        db.session.commit()
        flash("✏️ Cliente actualizado correctamente.", "cliente")
        return redirect(url_for('cliente.lista_cliente'))

    return render_template('Clientes/editarClientes.html', cliente=cliente)

# Route to deactivate (soft-delete) a client
@cliente_bp.route('/cliente/eliminar/<int:cedula>', methods=['GET', 'POST'])
@login_requerido
def eliminar_cliente(cedula):
    # Fetch the client only if active
    cliente = obtener_entidad_activa(Cliente, cedula, "Cliente")

    # No need to check if status is 'Activo' — already validated
    cliente.estado = 'Inactivo'
    db.session.commit()
    flash("🗑️ Cliente eliminado correctamente.", "cliente")

    return redirect(url_for('cliente.lista_cliente'))
