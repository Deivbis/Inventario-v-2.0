from datetime import datetime
from configs.extensiones import db

class Producto(db.Model):
    __tablename__ = 'producto'

    id = db.Column(db.Integer, primary_key=True)
    codigo_producto = db.Column(db.String(20), unique=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    imagen_url = db.Column(db.String(255))
    precio = db.Column(db.Numeric(10,2), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    cantidad_stock = db.Column(db.Integer, nullable=False)
    stock_minimo = db.Column(db.Integer, nullable=False)
    stock_maximo = db.Column(db.Integer, nullable=False)
    unidad_medida = db.Column(db.String(100), nullable=False)
    id_proveedor =  db.Column(db.Integer,db.ForeignKey('proovedores.id'))
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    categoria = db.relationship('Categoria', back_populates='productos')
    proveedor = db.relationship('Proveedor', back_populates='productos')
    detalles_venta = db.relationship('DetalleVenta', back_populates='producto')
    movimientos = db.relationship('Movimiento',back_populates='producto')
