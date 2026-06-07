from flask import Blueprint, flash, redirect, session, url_for

# Create blueprint for logout route
logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout')
def logout():
    # Clear all session data
    session.clear()

    # Show informational message to the user
    flash("✅ Session cerrada correctamente.", "login")

    # Redirect to login page (make sure it's registered in blueprints)
    return redirect(url_for('login.Login'))
