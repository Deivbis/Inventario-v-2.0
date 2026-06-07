from flask import Flask
from config import Config
from extensiones import db, mail
from rutas import blueprints  # import blueprint list

app = Flask(__name__)
app.config.from_object(Config)

# Inicia extencion
db.init_app(app)
mail.init_app(app)

# Registra todos los blueprints
for bp in blueprints:
    app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)
