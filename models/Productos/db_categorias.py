from datetime import datetime
from configs.extensiones import db

class Categoria(db.Model):
    __tablename__ = 'categoria'

    id = db.Column(db.Integer,  primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    productos = db.relationship('Producto', back_populates='categoria')