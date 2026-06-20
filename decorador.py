from functools import wraps
from flask import session, flash, redirect, url_for, abort

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

# Decorator to require user role(s) to access a route
def role_required(roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if 'rol_nombre' not in session or session['rol_nombre'] not in roles:
                flash('You do not have permission to access this page.', 'danger')
                abort(403)
            return f(*args, **kwargs)
        return decorated
    return decorator
