from flask import Flask
from datetime import datetime
from extensiones import db

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/inventario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ------------------------ MODELS ------------------------

# Category Model
class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False, unique=True)
    descripcion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    productos = db.relationship('Producto', back_populates='categoria')

# Supplier Model
class Proveedor(db.Model):
    __tablename__ = 'proovedores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(50))
    direccion = db.Column(db.String(255))
    correo = db.Column(db.String(255))
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    productos = db.relationship('Producto', back_populates='proveedor')

# Product Model
class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    codigo_producto = db.Column(db.String(20), unique=True, nullable=True)
    nombre = db.Column(db.String(255), nullable=False)
    imagen_url = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    cantidad_stock = db.Column(db.Integer, default=0)
    stock_minimo = db.Column(db.Integer, default=0)
    id_proveedor = db.Column(db.Integer, db.ForeignKey('proovedores.id'))
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    categoria = db.relationship('Categoria', back_populates='productos')
    proveedor = db.relationship('Proveedor', back_populates='productos')
    detalles_venta = db.relationship('DetalleVenta', back_populates='producto')

# Role Model
class Rol(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), unique=True, nullable=False)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    usuarios = db.relationship('RegistroUsuario', back_populates='rol')
    permisos = db.relationship('RolPermiso', back_populates='rol')

# Permission Model
class Permiso(db.Model):
    __tablename__ = 'permisos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), unique=True, nullable=False)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    roles = db.relationship('RolPermiso', back_populates='permiso')

# Role-Permission Link Table
class RolPermiso(db.Model):
    __tablename__ = 'rol_permiso'
    id = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id'))
    id_permiso = db.Column(db.Integer, db.ForeignKey('permisos.id'))
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    rol = db.relationship('Rol', back_populates='permisos')
    permiso = db.relationship('Permiso', back_populates='roles')

# User Model
class RegistroUsuario(db.Model):
    __tablename__ = 'registro_usuarios'
    id = db.Column(db.Integer, primary_key=True)
    contraseña = db.Column(db.String(255), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(255), nullable=False, unique=True)
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id'))

    rol = db.relationship('Rol', back_populates='usuarios')

# Customer Model
class Cliente(db.Model):
    __tablename__ = 'cliente'
    cedula = db.Column(db.String(20), primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(50))
    direccion = db.Column(db.String(255))
    correo = db.Column(db.String(255))
    estado = db.Column(db.String(20), default='Activo')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    ventas = db.relationship('Venta', back_populates='cliente')

# Sale Model
class Venta(db.Model):
    __tablename__ = 'ventas'
    id = db.Column(db.Integer, primary_key=True)
    cedula_cliente = db.Column(db.String(20), db.ForeignKey('cliente.cedula'))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float)
    estado = db.Column(db.String(20), default='Activo')

    cliente = db.relationship('Cliente', back_populates='ventas')
    detalles = db.relationship('DetalleVenta', back_populates='venta')

# Sale Detail Model
class DetalleVenta(db.Model):
    __tablename__ = 'detalle_venta'
    id = db.Column(db.Integer, primary_key=True)
    id_venta = db.Column(db.Integer, db.ForeignKey('ventas.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    cantidad = db.Column(db.Integer)
    estado = db.Column(db.String(20), default='Activo')
    precio_unitario = db.Column(db.Float)
    subtotal = db.Column(db.Float)

    venta = db.relationship('Venta', back_populates='detalles')
    producto = db.relationship('Producto', back_populates='detalles_venta')

# Stock Movement Model
class Movimiento(db.Model):
    __tablename__ = 'movimientos'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(10), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    motivo = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    producto = db.relationship('Producto', backref='movimientos')

# Password Recovery Model
class CambiarContraseña(db.Model):
    __tablename__ = 'cambiar_contraseña'
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(255), nullable=False)
    codigo = db.Column(db.String(6), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_expiracion = db.Column(db.DateTime, nullable=False)
    uso = db.Column(db.Boolean, default=False)

# Create tables if run directly
if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)
        db.create_all()
    print("✅ All tables created successfully.")
