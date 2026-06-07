function buscarProducto() {
  const codigo = document.getElementById('codigo_producto').value;
  const boton = document.getElementById('boton_registrar');

  if (!codigo) {
    limpiarCampos();
    boton.disabled = true;
    mostrarMensaje('⚠️ Selecciona un producto.', 'warning');
    return;
  }

  axios.post('/buscar_producto', { codigo: codigo })
    .then(response => {
      if (response.data.encontrado) {
        document.getElementById('nombre').value = response.data.nombre;
        document.getElementById('precio').value = response.data.precio;
        document.getElementById('categoria_id').value = response.data.categoria_id;
        document.getElementById('id_proveedor').value = response.data.id_proveedor;
        document.getElementById('stock_minimo').value = response.data.stock_minimo;
        document.getElementById('imagen_url').value = response.data.imagen_url;
        document.getElementById('cantidad_stock').value = response.data.cantidad_stock;

        boton.disabled = false;
        mostrarMensaje('', 'success');
      } else {
        limpiarCampos();
        boton.disabled = true;
        mostrarMensaje('❌ Producto no encontrado.', 'danger');
      }
    })
    .catch(error => {
      console.error('Error al buscar producto:', error);
    });
}

function limpiarCampos() {
  ['nombre', 'precio', 'categoria_id', 'id_proveedor', 'stock_minimo', 'imagen_url', 'cantidad_stock'].forEach(id => {
    document.getElementById(id).value = '';
  });
}

function mostrarMensaje(texto, tipo) {
  const alertaDiv = document.getElementById('mensaje-alerta');

  // Limpiar cualquier mensaje anterior
  alertaDiv.innerHTML = '';

  if (texto) {
    const clase = tipo === 'danger' ? 'errorcompra'
                 : tipo === 'success' ? 'compra'
                 : tipo === 'warning' ? 'warning'
                 : tipo;

    const icono = tipo === 'success' ? '✅'
                : tipo === 'danger' ? '❌'
                : tipo === 'warning' ? '⚠️'
                : '';

    alertaDiv.innerHTML = `
      <div class="custom-flash ${clase}">
        <span>${icono} ${texto}</span>
      </div>
    `;

    // Autoocultar en 4 segundos
    setTimeout(() => {
      alertaDiv.firstElementChild?.classList.add('fade-out');
      setTimeout(() => alertaDiv.innerHTML = '', 500);
    }, 4000);
  }
}
