from datetime import datetime
from configs.extensiones import db

class Proveedor(db.Model):
    __tablename__ = 'proovedores'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    telefono = db.Column(db.String(50))
    direccion = db.Column(db.Text)
    correo = db.Column(db.String(150))
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    productos = db.relationship('Producto',back_populates='proveedor')


