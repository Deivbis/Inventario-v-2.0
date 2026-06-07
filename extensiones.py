from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# Initialize SQLAlchemy for database interactions
db = SQLAlchemy()

# Initialize Flask-Mail for sending emails
mail = Mail()
