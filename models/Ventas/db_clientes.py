from datetime import datetime
from configs.extensiones import db

class Cliente(db.Model):
    __tablename__ = 'cliente'

    cedula = db.Column(db.String(20), primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    apellido = db.Column(db.String(100))
    telefono = db.Column(db.String(50))
    correo = db.Column(db.String(150))
    direccion = db.Column(db.Text)
    tipo_cliente = db.Column(db.String(50), nullable=False, default='normal')
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    ventas = db.relationship('Venta', back_populates='cliente')

