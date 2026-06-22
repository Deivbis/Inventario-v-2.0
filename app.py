from flask import Flask
from configs.config import Config
from extensiones import db, mail
from rutas import blueprints  # import blueprint list
from decorators.auth import tiene_permiso

app = Flask(__name__)
app.config.from_object(Config)

# Inicia extencion
db.init_app(app)
mail.init_app(app)

# Registra todos los blueprints
for bp in blueprints:
    app.register_blueprint(bp)

@app.context_processor
def inject_permissions():
    return dict(
        tiene_permiso=tiene_permiso
    )

if __name__ == "__main__":
    app.run(debug=True)
