from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash
from modelo import RegistroUsuario

# Create blueprint for login routes
login_bp = Blueprint('login', __name__)

# Route to handle user login
@login_bp.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        correo = request.form.get('correo', '').strip()
        contraseña = request.form.get('contraseña', '')

        # Look for the user by email
        usuario = RegistroUsuario.query.filter_by(correo=correo).first()

        if not usuario:
            flash("📧 Correo electrónico no encontrado.", "error")
        elif usuario.estado != 'Activo':
            flash("⛔ Usuario inactivo.", "error")
        elif not check_password_hash(usuario.contraseña, contraseña):
            flash("🔑 Contraseña incorrecta.", "error")
        else:
            # Create session
            session['usuario_id'] = usuario.id
            session['rol'] = usuario.id_rol
            session['nombre_usuario_mostrar'] = usuario.nombre
            session['rol_display_name'] = (
                "Administrador" if usuario.id_rol == 1 
                else "Vendedor" if usuario.id_rol == 2 
                else "Desconocido"
            )

            flash("✅ Inicio de sesión exitoso.", "login")
            return redirect(url_for('dashboard.dashboard')) 

    # Show login page if GET method or login fails
    return render_template('login/login.html')
