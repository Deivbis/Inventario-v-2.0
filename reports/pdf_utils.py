from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black
import os
from datetime import datetime
from modelo import Producto

def generar_pdf_inventario(productos, ventas_productos_agregados, detalle_ventas, path_archivo=None, tipo_reporte=None, fecha_inicio=None, fecha_fin=None):
    # Crear carpeta para reportes
    carpeta = os.path.join("static", "reportes")
    os.makedirs(carpeta, exist_ok=True)

    # Definir ruta del PDF
    if path_archivo:
        ruta_pdf = path_archivo
    else:
        if fecha_inicio and fecha_fin:
            nombre_archivo = f"reporte_inventario_{fecha_inicio.strftime('%Y%m%d')}_a_{fecha_fin.strftime('%Y%m%d')}.pdf"
        else:
            nombre_archivo = f"reporte_inventario_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        ruta_pdf = os.path.join(carpeta, nombre_archivo)

    p = canvas.Canvas(ruta_pdf, pagesize=letter)
    width, height = letter
    y = height - 60

    # Título del PDF (establecer título en pestaña)
    if fecha_inicio and fecha_fin:
        titulo = f"Reporte de Inventario {fecha_inicio.strftime('%Y-%m-%d')} a {fecha_fin.strftime('%Y-%m-%d')}"
    else:
        titulo = "Reporte de Inventario"
    p.setTitle(titulo)

    # Función para saltar línea y manejar salto de página
    def saltar_linea(altura=15):
        nonlocal y
        y -= altura
        if y < 100:
            p.showPage()
            y = height - 60

    # Cargar logo (ajusta la ruta si es necesario)
    logo_path = os.path.join(os.path.dirname(__file__), "static", "img", "Inventory.png")
    if os.path.exists(logo_path):
        try:
            p.drawImage(logo_path, 40, height - 50, width=40, height=40)
        except Exception as e:
            print("⚠ Error al cargar logo:", e)

    # Encabezado
    p.setFillColor(HexColor("#e4f0ff"))
    p.rect(0, y, width, 60, fill=True, stroke=False)
    p.setFillColor(black)
    p.setFont("Helvetica-Bold", 16)
    p.drawCentredString(width / 2, y + 20, "REPORTE DE INVENTARIO")
    y -= 80

    # Subtítulo y rango de fechas
    p.setFont("Helvetica", 11)
    p.drawCentredString(width / 2, y + 40, "Reporte basado en el rango de fechas seleccionado")
    p.setFont("Helvetica", 10)
    if fecha_inicio and fecha_fin:
        p.drawCentredString(width / 2, y + 25, f"Desde: {fecha_inicio.strftime('%Y-%m-%d')} Hasta: {fecha_fin.strftime('%Y-%m-%d')}")

    # Tabla productos - encabezado
    p.setFont("Helvetica-Bold", 12)
    p.drawString(40, y, "PRODUCTOS")
    saltar_linea(20)

    p.setFillColor(HexColor("#d1ecf1"))
    p.rect(40, y, 520, 20, fill=True, stroke=True)
    p.setFillColor(black)
    p.setFont("Helvetica-Bold", 10)
    p.drawString(45, y + 5, "ID")
    p.drawString(75, y + 5, "Nombre")
    p.drawString(220, y + 5, "Stock")
    p.drawString(280, y + 5, "Categoría")
    p.drawString(400, y + 5, "Precio")
    p.drawString(470, y + 5, "Proveedor")
    saltar_linea(20)

    # Filas productos
    p.setFont("Helvetica", 9)
    total_productos = 0
    for producto in productos:
        p.drawString(45, y, str(producto.id))
        p.drawString(75, y, producto.nombre[:20])
        p.drawString(220, y, str(producto.cantidad_stock))
        p.drawString(280, y, producto.categoria.nombre[:15])
        p.drawString(400, y, f"${producto.precio:.2f}")
        p.drawString(470, y, producto.proveedor.nombre[:15])
        total_productos += producto.cantidad_stock
        saltar_linea()

    # Total stock
    saltar_linea(10)
    p.setFont("Helvetica-Bold", 11)
    p.drawString(40, y, f"Cantidad total de stock: {total_productos}")
    saltar_linea(30)

    # Producto más vendido
    p.setFont("Helvetica-Bold", 12)
    if ventas_productos_agregados:
        mas_vendido = max(ventas_productos_agregados, key=lambda x: x.total)
        p.drawString(40, y, f"Producto más vendido: {mas_vendido.nombre} (Código: {mas_vendido.codigo})")
        saltar_linea()
        p.setFont("Helvetica", 11)
        p.drawString(40, y, f"Total de unidades vendidas: {mas_vendido.total}")
    else:
        p.drawString(40, y, "No se registraron ventas en el periodo seleccionado.")
    saltar_linea(30)

    # Ingresos totales
    total_ingresos = sum(d.cantidad * d.precio_unitario for d in detalle_ventas)
    p.setFont("Helvetica-Bold", 11)
    p.drawString(40, y, f"Ingresos totales por ventas: ${total_ingresos:.2f}")
    saltar_linea(30)

    # Detalle de ventas - encabezado
    p.setFont("Helvetica-Bold", 12)
    p.drawString(40, y, "DETALLE DE VENTAS")
    saltar_linea(20)

    p.setFillColor(HexColor("#d1ecf1"))
    p.rect(40, y, 520, 20, fill=True, stroke=True)
    p.setFillColor(black)
    p.setFont("Helvetica-Bold", 10)
    p.drawString(45, y + 5, "ID Prod")
    p.drawString(100, y + 5, "Nombre")
    p.drawString(250, y + 5, "Cantidad")
    p.drawString(330, y + 5, "P. Unitario")
    p.drawString(430, y + 5, "Fecha")
    saltar_linea(20)

    # Filas detalle ventas
    p.setFont("Helvetica", 9)
    for item in detalle_ventas:
        fecha_str = item.venta.fecha.strftime('%Y-%m-%d %H:%M')
        p.drawString(45, y, str(item.producto.id))
        p.drawString(100, y, item.producto.nombre[:20])
        p.drawString(250, y, str(item.cantidad))
        p.drawString(330, y, f"${item.precio_unitario:.2f}")
        p.drawString(430, y, fecha_str)
        saltar_linea()

    # Finalizar y guardar PDF
    p.showPage()
    p.save()

    return ruta_pdf, total_productos


def obtener_nombre_reporte():
    carpeta = os.path.join("static", "reportes")
    os.makedirs(carpeta, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"reporte_inventario_{timestamp}.pdf"
    return os.path.join(carpeta, nombre_archivo)


def generar_factura_pdf(venta, cliente, detalles):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.colors import HexColor, black
    from reportlab.pdfgen import canvas
    import os
    from modelo import Producto

    carpeta = os.path.join('static', 'facturas')
    os.makedirs(carpeta, exist_ok=True)

    nombre_archivo = f'factura_venta_{venta.id}.pdf'
    ruta_pdf = os.path.join(carpeta, nombre_archivo)

    c = canvas.Canvas(ruta_pdf, pagesize=letter)
    width, height = letter

    # Encabezado factura
    c.setFillColor(HexColor("#e4f0ff"))
    c.rect(0, height - 60, width, 60, fill=True, stroke=False)
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 40, "FACTURA DE VENTA")

    # Datos cliente
    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, height - 80, "DATOS DEL CLIENTE")
    c.setFont("Helvetica", 10)
    c.drawString(40, height - 95, f"{cliente.nombre} {cliente.apellido}")
    c.drawString(40, height - 110, f"Cédula: {cliente.cedula}")

    # Fecha y hora venta
    c.setFont("Helvetica-Bold", 10)
    c.drawString(330, height - 80, "FECHA Y HORA")
    c.setFont("Helvetica", 10)
    c.drawString(330, height - 95, f"Fecha: {venta.fecha.strftime('%d/%m/%Y')}")
    c.drawString(330, height - 110, f"Hora: {venta.fecha.strftime('%H:%M')}")

    # Encabezado tabla detalles
    y = height - 150
    c.setFillColor(HexColor("#d1ecf1"))
    c.rect(40, y, 510, 20, fill=True, stroke=True)

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(black)
    c.drawString(50, y + 5, "Producto")
    c.drawString(230, y + 5, "Cant.")
    c.drawString(330, y + 5, "P. Unitario")
    c.drawString(450, y + 5, "Subtotal")
    y -= 20

    # Filas productos vendidos
    c.setFont("Helvetica", 10)
    total = 0
    for d in detalles:
        producto = Producto.query.get(d.id_producto)
        subtotal = d.precio_unitario * d.cantidad
        total += subtotal

        c.drawString(50, y + 5, producto.nombre)
        c.drawString(240, y + 5, str(d.cantidad))
        c.drawString(340, y + 5, f"${d.precio_unitario:.2f}")
        c.drawString(460, y + 5, f"${subtotal:.2f}")
        y -= 20

        if y < 100:
            c.showPage()
            y = height - 100

    # Total factura
    c.setStrokeColor(black)
    c.line(40, y, 550, y)
    y -= 20
    c.setFont("Helvetica-Bold", 11)
    c.drawString(400, y, "TOTAL:")
    c.drawString(460, y, f"${total:.2f}")

    c.save()
    return ruta_pdf
