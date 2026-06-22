from datetime import datetime, timedelta
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from sqlalchemy import and_
from modelo import Categoria, Venta, DetalleVenta, Cliente, Producto, db
from decorators.auth import login_requerido,role_required

# Create blueprint for the dashboard module
dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_requerido
@role_required(['Administrador','vendedor','Supervisor','bodeguero'])
def dashboard():
    # Check if the user has an active session with required data
    if 'id_rol' not in session or 'usuario_nombre_mostrar' not in session or 'rol_nombre' not in session:
        flash("Debes iniciar sesión para acceder al panel.", "login")
        return redirect(url_for('login.Login'))

    # Default dashboard configuration (can be reused across views)
    dashboard_config = {
        'mostrar_sidebar_por_defecto': 'true',
        'habilitar_animaciones_ui': 'true',
        'mensaje_bienvenida_dashboard': 'Tienes acceso completo al sistema',
        'nombre_negocio': 'Inventary S.A.S.',
        'email_contacto': 'info@inventary.com',
        'direccion_negocio': '123 Fictitious St., Inventory City',
        'telefono_negocio': '+57 300 123 4567',
        'logo_url': 'https://placehold.co/150x50/007bff/ffffff?text=Logo',
    }

    # Main indicators
    total_productos = Producto.query.filter_by(estado='Activo').count()
    total_clientes = Cliente.query.filter_by(estado='Activo').count()
    total_ventas = Venta.query.count()
    ingresos_totales = db.session.query(db.func.sum(Venta.total)).scalar() or 0

    # Sales from the last 6 months
    sales_by_month = {}
    today = datetime.now()
    for i in range(6):
        current_month_date = today - timedelta(days=30 * i)
        month_key = current_month_date.strftime("%B %Y")
        monthly_total = db.session.query(db.func.sum(Venta.total))\
            .filter(db.func.DATE_FORMAT(Venta.fecha, '%Y-%m') == current_month_date.strftime('%Y-%m'))\
            .scalar() or 0
        sales_by_month[month_key] = monthly_total

    # Order sales from oldest to newest
    sales_by_month_ordered = dict(reversed(list(sales_by_month.items())))

    # Products by category (for chart visualization)
    products_by_category = db.session.query(
        Categoria.nombre, 
        db.func.count(Producto.id)
    ).join(Producto, Categoria.id == Producto.categoria_id)\
     .filter(Producto.estado == 'Activo')\
     .group_by(Categoria.nombre)\
     .all()

    category_labels = [nombre for nombre, _ in products_by_category]
    category_data = [cantidad for _, cantidad in products_by_category]

    # Products with low stock (for alerts)
    low_stock_products = Producto.query.filter(
        and_(
            Producto.estado == 'Activo',
            Producto.cantidad_stock < Producto.stock_minimo
        )
    ).order_by(Producto.cantidad_stock.asc()).limit(5).all()

    # Dictionary with all dashboard stats to be passed to the view
    stats = {
        'total_productos': total_productos,
        'total_clientes': total_clientes,
        'total_ventas': total_ventas,
        'ingresos_totales': ingresos_totales,
        'sales_by_month': sales_by_month_ordered,
        'products_by_category_labels': category_labels,
        'products_by_category_data': category_data,
        'low_stock_products': [{
            'codigo': p.codigo_producto,
            'nombre': p.nombre,
            'stock': p.cantidad_stock,
            'minimo': p.stock_minimo
        } for p in low_stock_products]
    }

    # Render dashboard based on user role
    if session['id_rol'] == 1:  # Administrator
        return render_template(
            'Ventana_admin.html',
            user_display_name=session['usuario_nombre_mostrar'],
            user_role_name=session['rol_nombre'],
            stats=stats,
            config=dashboard_config
        )
    elif session['id_rol'] == 2:  # Salesperson
        return render_template(
            'Ventana_vendedor.html',
            user_display_name=session['usuario_nombre_mostrar'],
            user_role_name=session['rol_nombre'],
            config=dashboard_config
        )
    else:
        flash("Tu rol de usuario no está reconocido. Contacta al administrador si crees que esto es un error.", "login")
        return redirect(url_for('login.Login'))
