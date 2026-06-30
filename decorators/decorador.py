from functools import wraps
from flask import session, flash, redirect, url_for, abort
from models import RolPermiso, Permiso
from services import tiene_permiso

# Decorator to require user to be logged in
def login_requerido(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print("SESSION DECORADOR:", dict(session))
        if 'usuario_id' not in session:
            flash('You must be logged in to access this page.', 'warning')
            return redirect(url_for('login.Login'))
        return f(*args, **kwargs)
    return decorated

#Decorator to require user permiso to access a route
def permiso_requerido(nombre_permiso):

    def decorator(f):

        @wraps(f)
        def decorated(*args, **kwargs):

            if "id_rol" not in session:
                flash("Debes iniciar sesión.", "danger")
                return redirect(url_for("login.Login"))

            if not tiene_permiso(session["id_rol"], nombre_permiso):
                flash("No tienes permisos para esta acción.", "danger")
                abort(403)

            return f(*args, **kwargs)

        return decorated

    return decorator
                      
        
