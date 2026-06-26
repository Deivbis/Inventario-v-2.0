from datetime import datetime
from configs.extensiones import db

class CambiarContraseña(db.Model):
    __tablename__ = 'cambiar_contraseña'

    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(255), nullable=False)
    codigo = db.Column(db.String(6), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_expiracion = db.Column(db.DateTime, nullable=False)
    uso = db.Column(db.Boolean, default=False, nullable=False)





