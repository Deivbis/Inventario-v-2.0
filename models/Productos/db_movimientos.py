from datetime import datetime
from configs.extensiones import db

class Movimiento(db.Model):
    __tablename__ = 'movimientos'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Text, nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    registro_usuario_id = db.Column(db.Integer, db.ForeignKey('registro_usuarios.id'), nullable=False)
    stock_anterior = db.Column(db.Integer, nullable=False, default=0)
    stock_nuevo = db.Column(db.Integer, nullable=False, default=0)
    observacion = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    motivo = db.Column(db.Text, nullable=False)
    estado = db.Column(db.String(20), default='Activo')
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    producto = db.relationship('Producto', back_populates='movimientos')
    usuario = db.relationship('RegistroUsuario', back_populates='movimientos')