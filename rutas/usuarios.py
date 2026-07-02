from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash
from models import RegistroUsuario, Rol
from decorators import login_requerido, permiso_requerido
from services import obtener_entidad_activa, obtener_entidades_activas, guardar_entidad, editar_entidad, desactivar_entidad, obtener_entidad_por_campo


# Blueprint para las rutas de gestión de usuarios
usuario_bp = Blueprint('usuarios', __name__)

# Ruta: Lista todos los usuarios registrados
@usuario_bp.route('/gestion_usuarios')
@login_requerido
@permiso_requerido("ver_usuarios")
def lista_usuarios():
    usuarios = obtener_entidades_activas(RegistroUsuario)
    roles = obtener_entidades_activas(Rol)

    if usuarios is None or roles is None:
        return render_template('404.html')
    
    estados_unicos = list(set([usuario.estado for usuario in usuarios]))  # Estados únicos (Activo/Inactivo)
    return render_template('GestionUsuarios/Usuarios.html', usuarios=usuarios, rol=roles, estados=estados_unicos)

# Ruta: Crear un nuevo usuario (GET muestra formulario, POST lo procesa)
@usuario_bp.route('/gestion_usuarios/crear_usuario', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("crear_usuarios")
def crear_usuario():
    roles = obtener_entidades_activas(Rol)

    if roles is None:
        return render_template('404.html')
    
    if request.method == 'POST':

        correo = request.form['correo']
        contrasena = request.form['contraseña']

        nuevo_usuario = RegistroUsuario(nombre = request.form['nombre'],
                                        apellido = request.form['apellido'],
                                        telefono = request.form['telefono'],
                                        correo = correo,
                                        usuario = request.form['usuario'],
                                        contraseña = generate_password_hash(contrasena, method='pbkdf2:sha256'),
                                        estado = request.form['estado'],
                                        id_rol = int(request.form['id_rol'])),

        # Verificar correo duplicado
        if obtener_entidad_por_campo(RegistroUsuario, 'correo', correo):
            flash("⚠️ El correo electrónico ya está registrado.", "errorUsuario")
            return render_template('GestionUsuarios/agregarUsuario.html', roles=roles)
        
        resultado_crud = guardar_entidad(nuevo_usuario)

        if resultado_crud:
            flash("✅ Usuario creado correctamente.", "usuario")
            return redirect(url_for('usuarios.lista_usuarios'))
        else:
            flash("❌ Error al crear el usuario.", "errorUsuario")

    return render_template('GestionUsuarios/agregarUsuario.html', roles=roles)

# Ruta: Editar un usuario existente
@usuario_bp.route('/gestion_usuarios/editar/<int:id>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("editar_usuarios")
def editar_usuario(id):
    usuario = obtener_entidad_activa(RegistroUsuario, id, "RegistroUsuario")
    roles = obtener_entidades_activas(Rol)

    if request.method == 'POST':

        usuario.nombre = request.form['nombre']
        usuario.apellido = request.form['apellido']
        usuario.telefono = request.form['telefono']
        usuario.correo = request.form['correo']
        usuario.usuario = request.form['usuario']
        usuario.estado = request.form['estado']
        usuario.id_rol = int(request.form['id_rol'])

        # Cambio opcional de contraseña
        nueva_contraseña = request.form.get('contraseña')
        if nueva_contraseña:
            usuario.contraseña = generate_password_hash(nueva_contraseña)

        # Validar que el correo no esté duplicado (excluyendo el actual)
        if RegistroUsuario.query.filter(
            RegistroUsuario.correo == usuario.correo,
            RegistroUsuario.id != id
        ).first():
            flash("⚠️ Este correo ya está en uso por otro usuario.", "errorUsuario")
            return render_template('GestionUsuarios/editar_usuario.html', usuario=usuario, roles=roles)

        resultado_crud = editar_entidad(usuario)

        if resultado_crud:
            flash("✅ Usuario editado correctamente.", "usuario")
            return redirect(url_for('usuarios.lista_usuarios'))
        else:
            flash("❌ Error al editar el usuario.", "errorUsuario")

    return render_template('GestionUsuarios/editar_usuario.html', usuario=usuario, roles=roles)

# Ruta: Cambiar el estado del usuario (activo/inactivo)
@usuario_bp.route('/gestion_usuarios/eliminar/<int:id>', methods=['GET', 'POST'])
@login_requerido
@permiso_requerido("eliminar_usuarios")
def eliminar_usuario(id):
    usuario = obtener_entidad_activa(RegistroUsuario, id, "RegistroUsuario")

    # Prevenir que el usuario desactive su propia cuenta estando conectado
    if usuario.id == session.get('usuario_id'):
        flash("❌ No puedes desactivar tu propia cuenta mientras estás conectado.", "usuario")
        return redirect(url_for('usuarios.lista_usuarios'))

    resultado_crud = desactivar_entidad(usuario)

    if resultado_crud:
        flash("✅ Usuario desactivado correctamente.", "usuario")
        return redirect(url_for('usuarios.lista_usuarios'))
    else:
        flash("❌ Error al desactivar el usuario.", "usuario")
