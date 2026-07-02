from flask import Blueprint, flash, redirect, render_template, request, url_for
from models import Rol
from services import obtener_entidades_activas, guardar_entidad
from decorators import login_requerido, permiso_requerido

# Blueprint para las rutas de gestión de roles
roles_bp = Blueprint('roles', __name__)

# Ruta: Lista todos los roles
@roles_bp.route('/roles')
@login_requerido
@permiso_requerido("ver_roles")
def lista_roles():

    roles = obtener_entidades_activas(Rol)

    if roles is None:
        return render_template('404.html')
    
    return render_template('GestionUsuarios/roles.html', roles=roles)

# Ruta: Agregar un nuevo rol (GET muestra formulario, POST procesa formulario)
@roles_bp.route('/roles/agregar', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("crear_roles")
def agregar_rol():
    if request.method == 'POST':

        neuvo_rol = Rol(nombre = request.form['nombre'],
                        descripcion = request.form['descripcion'])
        
        resultado_crud = guardar_entidad(neuvo_rol)

        if resultado_crud:
            flash("✅ Rol agregado correctamente.", "rol")
            return redirect(url_for('roles.lista_roles'))
        else:
            flash("❌ Error al agregar el rol.", "rol")

    # Si es GET, mostrar el formulario para agregar rol
    return render_template('GestionUsuarios/agregarRol.html')
