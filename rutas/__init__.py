# Import all system blueprints
from .productos import productos_bp
from .usuarios import usuario_bp
from .ventas import ventas_bp
from .roles import roles_bp
from .categoria import categoria_bp
from .proveedor import proveedor_bp
from .dashboard import dashboard_bp
from .compra import compra_bp
from .perfil import perfil_bp
from .movimientos import movimiento_bp
from .factura import factura_bp
from .reporte import reporte_bp
from .error import error_bp
from .inicio import inicio_bp
from .login import login_bp
from .registrarse import registrarse_bp
from .recuperar_cuenta import recuperar_bp
from .logout import logout_bp
from .cliente import cliente_bp

# List of all blueprints to register in app.py or main.py
blueprints = [
    productos_bp,       # Product management
    usuario_bp,         # User management
    ventas_bp,          # Sales and invoicing
    roles_bp,           # Roles and permissions
    categoria_bp,       # Product categories
    proveedor_bp,       # Supplier management
    dashboard_bp,       # Dashboard panel
    compra_bp,          # Purchase records
    perfil_bp,          # User profile
    movimiento_bp,      # Stock movement records
    factura_bp,         # Invoice viewing and deletion
    reporte_bp,         # Inventory and sales reports
    error_bp,           # Error handler (404, etc.)
    inicio_bp,          # Home page (landing)
    login_bp,           # User login
    registrarse_bp,     # New user registration
    recuperar_bp,       # Password recovery
    logout_bp,          # Logout
    cliente_bp          # Client registration
]
