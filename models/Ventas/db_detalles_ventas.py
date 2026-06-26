from datetime import datetime
from configs.extensiones import db

class DetalleVenta(db.Model):
    __tablename__ = 'detalle_venta'

    id = db.Column(db.Integer, primary_key=True)
    id_venta = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Numeric(10,2), nullable=False)
    subtotal = db.Column(db.Numeric(10,2), nullable=False)
    descuento = db.Column(db.Integer, nullable=False, default=0)
    estado = db.Column(db.String(20), default='Activo', nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    venta = db.relationship('Venta', back_populates='detalles')
    producto = db.relationship('Producto', back_populates='detalles_venta')
