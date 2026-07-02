from flask import Blueprint, flash, redirect, render_template, request, url_for
from models import Cliente
from services import obtener_entidad_activa, obtener_entidades_activas, guardar_entidad, editar_entidad, desactivar_entidad, obtener_entidad_por_campo
from decorators import login_requerido, permiso_requerido

cliente_bp = Blueprint('cliente', __name__)

# Route to list all active clients
@cliente_bp.route('/lista-Cliente')
@login_requerido
@permiso_requerido("ver_clientes")
def lista_cliente():

    cliente = obtener_entidades_activas(Cliente)

    if cliente is None:
        return render_template('404.html')
    
    return render_template('Clientes/clientes.html', clientes=cliente)

# Route to add a new client
@cliente_bp.route('/cliente/agregar', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("crear_clientes")
def agregar_cliente():

    if request.method == 'POST':

        nuevo_cliente = Cliente(cedula=request.form['cedula'],
                                nombre=request.form['nombre'],
                                apellido=request.form['apellido'],
                                telefono=request.form['telefono'],
                                correo=request.form['correo'],
                                direccion=request.form['direccion'])
        

        cliente_existente = obtener_entidad_por_campo(Cliente, 'cedula', request.form['cedula'])
        if cliente_existente:
            flash("⚠️ La cédula ya está registrada a otro cliente.", "errorCliente")
            return render_template('Clientes/agregarClientes.html')
        
        resultado_crud = guardar_entidad(nuevo_cliente)

        if resultado_crud:
            flash("✏️ Cliente agregado correctamente.", "cliente")
            return redirect(url_for('cliente.lista_cliente'))
        else:
            flash("❌ Error al agregar el cliente.", "cliente")

    return render_template('Clientes/agregarClientes.html')

# Route to edit an existing client
@cliente_bp.route('/cliente/editar/<int:cedula>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("editar_clientes")
def editar_cliente(cedula):

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

        resultado_crud = editar_entidad(cliente)

        if resultado_crud:
            flash("✏️ Cliente editado correctamente.", "cliente")
            return redirect(url_for('cliente.lista_cliente'))
        else:
            flash("❌ Error al editar el cliente.", "cliente")

    return render_template('Clientes/editarClientes.html', cliente=cliente)

# Route to deactivate (soft-delete) a client
@cliente_bp.route('/cliente/eliminar/<int:cedula>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("eliminar_clientes")
def eliminar_cliente(cedula):

    cliente = obtener_entidad_activa(Cliente, cedula, "Cliente")

    resultado_crud = desactivar_entidad(cliente)

    if resultado_crud:
        flash("🗑️ Cliente eliminado correctamente.", "cliente")
        return redirect(url_for('cliente.lista_cliente'))
    else:
        flash("❌ Error al eliminar el cliente.", "cliente")
