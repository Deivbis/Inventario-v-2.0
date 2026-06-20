from flask import Blueprint, flash, redirect, render_template, request, url_for
from modelo import Rol, db
from decorador import login_requerido, role_required

# Blueprint para las rutas de gestión de roles
roles_bp = Blueprint('roles', __name__)

# Ruta: Lista todos los roles
@roles_bp.route('/roles')
@login_requerido
@role_required(['Administrador'])
def lista_roles():
    # Consultar todos los roles desde la base de datos
    roles = Rol.query.all()
    
    # Renderizar la plantilla de lista de roles
    return render_template('GestionUsuarios/roles.html', roles=roles)

# Ruta: Agregar un nuevo rol (GET muestra formulario, POST procesa formulario)
@roles_bp.route('/roles/agregar', methods=['GET', 'POST'])
@login_requerido
def agregar_rol():
    if request.method == 'POST':
        # Obtener datos del formulario enviado
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']

        # Crear nueva instancia de rol
        nuevo_rol = Rol(nombre=nombre, descripcion=descripcion)

        # Agregar y guardar en la base de datos
        db.session.add(nuevo_rol)
        db.session.commit()

        # Mostrar mensaje de éxito y redirigir a la lista de roles
        flash("✅ Rol agregado correctamente.", "rol")
        return redirect(url_for('roles.lista_roles'))

    # Si es GET, mostrar el formulario para agregar rol
    return render_template('GestionUsuarios/agregarRol.html')
