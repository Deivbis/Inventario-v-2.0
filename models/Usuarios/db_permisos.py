from datetime import datetime
from configs.extensiones import db

class Permiso(db.Model):
    __tablename__ = 'permisos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    roles = db.relationship('RolPermiso', back_populates='permiso')