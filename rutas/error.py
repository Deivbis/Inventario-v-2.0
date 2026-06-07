from flask import Blueprint, render_template

# Create a blueprint to handle error pages
error_bp = Blueprint('error', __name__)

# Custom handler for 404 Not Found errors
@error_bp.errorhandler(404)
def pagina_no_encontrada(error):
    # Render custom 404 error page
    return render_template('404.html'), 404
