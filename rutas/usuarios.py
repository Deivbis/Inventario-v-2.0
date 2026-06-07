from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash
from modelo import RegistroUsuario, Rol, db
from decorador import login_requerido
from utils.utils import obtener_entidad_activa

# Blueprint para las rutas de gestión de usuarios
usuario_bp = Blueprint('usuarios', __name__)

# Ruta: Lista todos los usuarios registrados
@usuario_bp.route('/gestion_usuarios')
@login_requerido
def lista_usuarios():
    usuarios = RegistroUsuario.query.all()  # Obtener todos los usuarios
    roles = Rol.query.all()  # Obtener todos los roles
    estados_unicos = list(set([usuario.estado for usuario in usuarios]))  # Estados únicos (Activo/Inactivo)
    return render_template('GestionUsuarios/Usuarios.html', usuarios=usuarios, rol=roles, estados=estados_unicos)

# Ruta: Crear un nuevo usuario (GET muestra formulario, POST lo procesa)
@usuario_bp.route('/gestion_usuarios/crear_usuario', methods=['GET', 'POST'])
@login_requerido
def crear_usuario():
    roles = Rol.query.all()
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo = request.form['correo']
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        estado = request.form['estado']
        rol = int(request.form['id_rol'])

        # Verificar correo duplicado
        if RegistroUsuario.query.filter_by(correo=correo).first():
            flash("⚠️ El correo electrónico ya está registrado.", "errorUsuario")
            return render_template('GestionUsuarios/agregarUsuario.html', roles=roles)

        # Encriptar la contraseña
        contraseña_hash = generate_password_hash(contraseña, method='pbkdf2:sha256')

        # Crear nuevo usuario y guardar en la base de datos
        nuevo_usuario = RegistroUsuario(
            nombre=nombre, apellido=apellido, telefono=telefono,
            correo=correo, usuario=usuario, contraseña=contraseña_hash,
            estado=estado, id_rol=rol
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash("✅ Usuario creado correctamente.", "usuario")
        return redirect(url_for('usuarios.lista_usuarios'))

    return render_template('GestionUsuarios/agregarUsuario.html', roles=roles)

# Ruta: Editar un usuario existente
@usuario_bp.route('/gestion_usuarios/editar/<int:id>', methods=['GET', 'POST'])
@login_requerido
def editar_usuario(id):
    usuario = obtener_entidad_activa(RegistroUsuario, id, "RegistroUsuario")
    roles = Rol.query.all()

    if request.method == 'POST':
        # Actualizar campos del usuario
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

        # Intentar guardar los cambios
        try:
            db.session.commit()
            flash("✅ Usuario actualizado correctamente.", "usuario")
            return redirect(url_for('usuarios.lista_usuarios'))
        except Exception as e:
            db.session.rollback()
            flash(f"❌ Error al actualizar el usuario: {e}", "errorUsuario")

    return render_template('GestionUsuarios/editar_usuario.html', usuario=usuario, roles=roles)

# Ruta: Cambiar el estado del usuario (activo/inactivo)
@usuario_bp.route('/gestion_usuarios/eliminar/<int:id>', methods=['GET', 'POST'])
@login_requerido
def eliminar_usuario(id):
    usuario = obtener_entidad_activa(RegistroUsuario, id, "RegistroUsuario")

    # Prevenir que el usuario desactive su propia cuenta estando conectado
    if usuario.id == session.get('usuario_id'):
        flash("❌ No puedes desactivar tu propia cuenta mientras estás conectado.", "usuario")
        return redirect(url_for('usuarios.lista_usuarios'))

    # Cambiar estado entre 'Activo' e 'Inactivo'
    usuario.estado = 'Inactivo' if usuario.estado == 'Activo' else 'Activo'
    mensaje = "Usuario desactivado con éxito." if usuario.estado == 'Inactivo' else "Usuario activado con éxito."

    db.session.commit()
    flash(f"✅ {mensaje}", "usuario")
    return redirect(url_for('usuarios.lista_usuarios'))
