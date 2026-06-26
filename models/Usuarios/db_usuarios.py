from datetime import datetime
from configs.extensiones import db

class RegistroUsuario(db.Model):
    __tablename__ = 'registro_usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False, unique=True)
    telefono = db.Column(db.String(50), nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    rol = db.relationship('Rol', back_populates='usuarios')
    movimientos = db.relationship('Movimiento', back_populates='usuario')

