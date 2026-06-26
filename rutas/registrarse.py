from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash
from models import RegistroUsuario
from configs import db

# Blueprint for user registration
registrarse_bp = Blueprint('registrarse', __name__)

# Route for user registration (GET shows form, POST handles submission)
@registrarse_bp.route('/registrar', methods=['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        # Retrieve form data
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        id_rol = 2  # Default role: Vendedor (Salesperson)

        # Hash the password securely
        contraseña_hash = generate_password_hash(contraseña, method='pbkdf2:sha256')

        # Validate if the email is already registered
        if RegistroUsuario.query.filter_by(correo=correo).first():
            flash("⚠️ El correo ya está registrado. Por favor, usa otro o inicia sesión.", "danger")
            return render_template('login/registrar.html', nombre=nombre, apellido=apellido, telefono=telefono, correo=correo)

        # Create and save new user
        try:
            nuevo_usuario = RegistroUsuario(
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                correo=correo,
                contraseña=contraseña_hash,
                id_rol=id_rol
            )
            db.session.add(nuevo_usuario)
            db.session.commit()

            flash("✅ ¡Registro exitoso! Ya puedes iniciar sesión.", "login")
            return redirect(url_for('login.Login'))

        except Exception as e:
            db.session.rollback()
            flash(f"❌ Error en el registro. Ocurrió un error inesperado: {e}", "danger")
            return render_template('login/registrar.html', nombre=nombre, apellido=apellido, telefono=telefono, correo=correo)

    # Display registration form on GET request
    return render_template('login/registrar.html')

# Route for Terms and Conditions page
@registrarse_bp.route('/terminos-y-condiciones')
def terminos_y_condiciones():
    return render_template('login/terminos.html')
