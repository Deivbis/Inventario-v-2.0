let cedulaClienteSeleccionado = null;
const productosSeleccionados = new Map();

// Buscar cliente
document.getElementById('buscadorCliente').addEventListener('input', function () {
    const filtro = this.value.toLowerCase();
    document.querySelectorAll('#tablaClientes tbody tr').forEach(row => {
        row.style.display = [...row.cells].some(cell =>
            cell.textContent.toLowerCase().includes(filtro)
        ) ? '' : 'none';
    });
});

// Buscar producto
document.getElementById('buscadorProducto').addEventListener('input', function () {
    const filtro = this.value.toLowerCase();
    document.querySelectorAll('#tablaProductos tbody tr').forEach(row => {
        row.style.display = [...row.cells].some(cell =>
            cell.textContent.toLowerCase().includes(filtro)
        ) ? '' : 'none';
    });
});

// Selección de cliente
document.querySelectorAll('#tablaClientes tbody tr').forEach(row => {
    row.addEventListener('click', () => {
        document.querySelectorAll('#tablaClientes tbody tr').forEach(r => r.classList.remove('cliente-seleccionado'));
        row.classList.add('cliente-seleccionado');
        cedulaClienteSeleccionado = row.dataset.cedula;
    });
});

// Selección de productos
function asignarEventosFilasProductos() {
    document.querySelectorAll('#tablaProductos tbody tr').forEach(row => {
        const id = row.dataset.id;
        const cantidadInput = row.querySelector(`input[name="cantidad_${id}"]`);
        row.addEventListener('click', () => {
            if (productosSeleccionados.has(id)) {
                productosSeleccionados.delete(id);
                row.classList.remove('producto-seleccionado');
                cantidadInput.disabled = true;
            } else {
                productosSeleccionados.set(id, cantidadInput);
                row.classList.add('producto-seleccionado');
                cantidadInput.disabled = false;
                cantidadInput.focus();
            }
        });
    });
}
asignarEventosFilasProductos();

// Solo actualizar celdas de stock (sin parpadeo)
async function actualizarStockProductos() {
    const res = await fetch('/productos_json');
    const productos = await res.json();

    productos.forEach(p => {
        const row = document.querySelector(`#tablaProductos tbody tr[data-id="${p.id}"]`);
        if (row) {
            const stockCell = row.cells[2];
            const stockMinCell = row.cells[3];

            // Destacar visualmente el cambio
            if (parseInt(stockCell.textContent) !== p.cantidad_stock) {
                stockCell.classList.add('highlight');
                setTimeout(() => stockCell.classList.remove('highlight'), 500);
            }

            stockCell.textContent = p.cantidad_stock;
            stockMinCell.textContent = p.stock_minimo;

            if (p.cantidad_stock <= p.stock_minimo) {
                row.classList.add('stock-bajo');
            } else {
                row.classList.remove('stock-bajo');
            }
        }
    });
}

// Registrar venta
document.getElementById('btnRegistrar').addEventListener('click', async () => {
    if (!cedulaClienteSeleccionado) {
        alert("Selecciona un cliente.");
        return;
    }

    const productos = [];
    productosSeleccionados.forEach((input, id) => {
        const cantidad = parseInt(input.value);
        if (cantidad > 0) {
            productos.push({ id_producto: parseInt(id), cantidad });
        }
    });

    if (productos.length === 0) {
        alert("Selecciona al menos un producto con cantidad válida.");
        return;
    }

    const res = await fetch('/registrar_venta', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cedula: cedulaClienteSeleccionado, productos })
    });

    const data = await res.json();
    const mensaje = document.getElementById('mensaje');

    if (data.factura_url) {
        await actualizarStockProductos();
        verificarStockMinimo();
        mensaje.innerHTML = `<div class="mensaje-exito">🧾 Factura realizada correctamente. <a href="${data.factura_url}" target="_blank">Ver factura</a></div>`;


        // ✅ Reiniciar inputs, selección y buscadores
        productosSeleccionados.forEach((input, id) => {
            input.value = 0;
            input.disabled = true;

            const row = document.querySelector(`#tablaProductos tbody tr[data-id="${id}"]`);
            if (row) {
                row.classList.remove('producto-seleccionado');
            }
        });
        productosSeleccionados.clear();

        cedulaClienteSeleccionado = null;
        document.querySelectorAll('#tablaClientes tbody tr').forEach(r => r.classList.remove('cliente-seleccionado'));

        document.getElementById('buscadorCliente').value = '';
        document.getElementById('buscadorProducto').value = '';
    } else {
        mensaje.textContent = data.mensaje || data.error;
    }

    
});

function verificarStockMinimo() {
    const filas = document.querySelectorAll('#tablaProductos tbody tr');
    const productosConStockBajo = [];

    filas.forEach(row => {
        const id = row.dataset.id;
        const stock = parseInt(row.cells[2].textContent);
        const stockMin = parseInt(row.cells[3].textContent);

        if (stock <= stockMin) {
            const nombre = row.cells[1].textContent;
            productosConStockBajo.push({ nombre, stock, stockMin });
        }
    });

    if (productosConStockBajo.length > 0) {
        const lista = document.getElementById('listaStockBajo');
        lista.innerHTML = '';
        productosConStockBajo.forEach(p => {
            const li = document.createElement('li');
            li.textContent = `${p.nombre}: ${p.stock} unidades (mínimo: ${p.stockMin})`;
            lista.appendChild(li);
        });

        document.getElementById('alertaStockMinimo').style.display = 'flex';
    }
}

function cerrarAlertaStock() {
    document.getElementById('alertaStockMinimo').style.display = 'none';
}
