from datetime import datetime, timedelta
from random import randint
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_mail import Message
from werkzeug.security import generate_password_hash
from extensiones import mail
from modelo import RegistroUsuario, CambiarContraseña, db

# Blueprint for password recovery process
recuperar_bp = Blueprint('recuperar', __name__)

# Step 1: Request recovery (send verification code via email)
@recuperar_bp.route('/recuperar-contraseña', methods=['GET', 'POST'])
def recuperar_contraseña():
    if request.method == 'POST':
        correo_usuario = request.form['email']
        codigo = str(randint(100000, 999999))  # 6-digit verification code
        expiracion = datetime.utcnow() + timedelta(minutes=15)  # Code expires in 15 minutes

        # Remove any previous unused recovery attempts
        CambiarContraseña.query.filter_by(correo=correo_usuario, uso=False).delete()
        db.session.commit()

        # Save new recovery code to the database
        nuevo_codigo = CambiarContraseña(
            correo=correo_usuario,
            codigo=codigo,
            fecha_expiracion=expiracion,
            uso=False
        )
        db.session.add(nuevo_codigo)
        db.session.commit()

        # Send verification code via email
        try:
            msg = Message("Solicitud para restablecer contraseña", recipients=[correo_usuario])
            msg.body = f'Tu código de verificación para restablecer la contraseña es: {codigo}'
            mail.send(msg)

            flash('📨 Se ha enviado un código de verificación a tu correo electrónico.', 'codigoEnviado')
            return render_template('login/confirmarCodigo.html')
        except Exception as e:
            print("Email sending error:", e)
            flash("❌ Error al enviar el correo. Por favor, intenta más tarde.", 'errorCodigo')
            return render_template('login/correo.html')

    return render_template('login/correo.html')

# Step 2: Confirm verification code
@recuperar_bp.route('/confirmar-codigo', methods=['GET', 'POST'])
def confirmar_codigo():
    correo_usuario = request.form['email']
    codigo_ingresado = request.form['codigo']

    # Check if the code is valid and not expired
    registro = CambiarContraseña.query.filter_by(
        correo=correo_usuario,
        codigo=codigo_ingresado,
        uso=False
    ).filter(
        CambiarContraseña.fecha_expiracion > datetime.utcnow()
    ).first()

    if registro:
        session['correo_verificado'] = correo_usuario
        flash('✅ Código verificado. Ahora puedes restablecer tu contraseña.', 'Contraseña')
        return redirect('/cambiar-contraseña')
    else:
        flash('❌ Código inválido o expirado.', 'errorCodigo')
        return redirect('/recuperar-contraseña')

# Step 3: Change the user's password
@recuperar_bp.route('/cambiar-contraseña', methods=['GET', 'POST'])
def cambiar_contraseña():
    if request.method == 'POST':
        nueva_contraseña = request.form['nueva_contraseña']
        correo = session.get('correo_verificado')

        if not correo:
            flash('⚠️ Sesión expirada. Por favor inicia nuevamente el proceso de recuperación.', 'errorCodigo')
            return redirect('/recuperar-contraseña')

        usuario = RegistroUsuario.query.filter_by(correo=correo).first()

        if usuario:
            # Update password with hash
            usuario.contraseña = generate_password_hash(nueva_contraseña, method='pbkdf2:sha256')
            db.session.commit()

            # Optionally mark the code as used
            CambiarContraseña.query.filter_by(correo=correo, uso=False).update({'uso': True})
            db.session.commit()

            flash('🔐 Contraseña actualizada correctamente.', 'login')
            return redirect('/login')
        else:
            flash('❌ Usuario no encontrado.', 'errorCodigo')
            return redirect('/recuperar-contraseña')

    return render_template('login/recuperar.html')
