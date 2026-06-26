from datetime import datetime
from configs.extensiones import db

class Rol(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    usuarios = db.relationship('RegistroUsuario', back_populates='rol')
    permisos = db.relationship('RolPermiso', back_populates='rol')