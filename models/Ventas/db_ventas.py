from datetime import datetime
from configs.extensiones import db

class Venta(db.Model):
    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)
    cedula_cliente = db.Column(db.String(20), db.ForeignKey('cliente.cedula'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('registro_usuarios.id'), nullable=False)
    subtotal = db.Column(db.Numeric(10,2), nullable=False, default=0)
    descuento = db.Column(db.Numeric(10,0), nullable=False, default=0)
    metodo_pago = db.Column(db.String(50), default='efectivo', nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Numeric(10,2))
    estado = db.Column(db.String(20), default='Activo')

    cliente = db.relationship('Cliente',back_populates='ventas')
    usuario = db.relationship('RegistroUsuario')
    detalles = db.relationship('DetalleVenta',back_populates='venta')