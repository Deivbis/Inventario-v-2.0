from flask import Blueprint, render_template

# Create blueprint for the home/start page
inicio_bp = Blueprint('inicio', __name__)

# Route for the homepage
@inicio_bp.route('/')
def inicio():
    # Render the main home page template
    return render_template('inicio.html')
