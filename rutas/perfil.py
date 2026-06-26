from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash
from models import RegistroUsuario
from configs import db
from decorators import login_requerido

# Create blueprint for user profile management
perfil_bp = Blueprint('perfil', __name__)

@perfil_bp.route('/mi_perfil', methods=['GET', 'POST'])
@login_requerido
def mi_perfil():
    user_id = session.get('usuario_id')
    usuario_actual = RegistroUsuario.query.get_or_404(user_id)

    if request.method == 'POST':
        try:
            # Update personal information
            usuario_actual.nombre = request.form['nombre']
            usuario_actual.apellido = request.form['apellido']
            usuario_actual.telefono = request.form['telefono']
            usuario_actual.correo = request.form['correo']

            # Check if the user wants to change the password
            nueva_contraseña = request.form.get('nueva_contraseña')
            confirmar_contraseña = request.form.get('confirmar_contraseña')

            if nueva_contraseña:
                if nueva_contraseña == confirmar_contraseña:
                    usuario_actual.contraseña = generate_password_hash(nueva_contraseña, method='pbkdf2:sha256')
                else:
                    flash('❌ Las contraseñas no coinciden.', 'perfil')
                    return render_template('perfil/editar_perfil.html', usuario=usuario_actual,
                                           user_display_name=session.get('nombre_usuario_mostrar'),
                                           user_role_name=session.get('rol_nombre'))

            # Check if email is already used by another user (excluding current user)
            email_duplicado = RegistroUsuario.query.filter(
                RegistroUsuario.correo == usuario_actual.correo,
                RegistroUsuario.id != user_id
            ).first()

            if email_duplicado:
                flash('❌ El correo electrónico ya está siendo usado por otro usuario.', 'perfil')
                return render_template('perfil/editar_perfil.html', usuario=usuario_actual,
                                       user_display_name=session.get('nombre_usuario_mostrar'),
                                       user_role_name=session.get('rol_nombre'))

            db.session.commit()
            flash('✅ Perfil actualizado correctamente.', 'perfil')

            # Update name in session
            session['nombre_usuario_mostrar'] = usuario_actual.nombre

            return redirect(url_for('perfil.mi_perfil'))

        except Exception as e:
            db.session.rollback()
            flash(f'❌ Error al actualizar el perfil: {str(e)}', 'perfil')

    return render_template('perfil/editar_perfil.html', usuario=usuario_actual,
                           user_display_name=session.get('nombre_usuario_mostrar'),
                           user_role_name=session.get('rol_nombre'))
