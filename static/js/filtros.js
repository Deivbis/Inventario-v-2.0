function filtrarCategoria() {
    const input = document.getElementById("busqueda");
    const filtro = input.value.toLowerCase();
    const filas = document.querySelectorAll("#tablaCategorias tbody tr");

      filas.forEach(fila => {
        const celdaNombre = fila.cells[1]; // índice 1 = segunda columna (Nombre)
        if (celdaNombre) {
          const texto = celdaNombre.textContent.toLowerCase();
          fila.style.display = texto.includes(filtro) ? "" : "none";
        }
    });
}

function filtrarProvedor() {
    const input = document.getElementById("busqueda");
    const filtro = input.value.toLowerCase();
    const filas = document.querySelectorAll("#tablaProveedores tbody tr");

      filas.forEach(fila => {
        const celdaNombre = fila.cells[1]; // índice 1 = segunda columna (Nombre)
        if (celdaNombre) {
          const texto = celdaNombre.textContent.toLowerCase();
          fila.style.display = texto.includes(filtro) ? "" : "none";
        }
    });
}

function filtrarProductos() {
    const inputTexto = document.getElementById("busquedaProducto").value.toLowerCase();
    const filtroCategoria = document.getElementById("filtroCategoria").value.toLowerCase();
    const filtroProveedor = document.getElementById("filtroProveedor").value.toLowerCase();

    const filas = document.querySelectorAll("#tablaproductos tr");

    for (let i = 1; i < filas.length; i++) { // Empezamos desde 1 para saltar el encabezado
        const fila = filas[i];

        const codigo = fila.cells[0].textContent.toLowerCase();   // Código del producto
        const nombre = fila.cells[1].textContent.toLowerCase();   // Nombre del producto
        const categoria = fila.cells[3].textContent.toLowerCase();
        const proveedor = fila.cells[6].textContent.toLowerCase();

        const coincideBusqueda = codigo.includes(inputTexto) || nombre.includes(inputTexto);
        const coincideCategoria = filtroCategoria === "" || categoria === filtroCategoria;
        const coincideProveedor = filtroProveedor === "" || proveedor === filtroProveedor;

        fila.style.display = (coincideBusqueda && coincideCategoria && coincideProveedor) ? "" : "none";
    }
}


function filtrarClientes() {
    const filtro = document.getElementById("busquedaCliente").value.toLowerCase();
    const filas = document.querySelectorAll("#tablaClientes tbody tr");

    filas.forEach(fila => {
        const cedula = fila.children[0].textContent.toLowerCase();
        const nombre = fila.children[1].textContent.toLowerCase();
        const apellido = fila.children[2].textContent.toLowerCase();
        const correo = fila.children[4].textContent.toLowerCase();

        const coincide = cedula.includes(filtro) || nombre.includes(filtro) || apellido.includes(filtro) || correo.includes(filtro);

            fila.style.display = coincide ? "" : "none";
        });
}

function filtrarTabla() {
    const input = document.getElementById("busqueda");
    const filtro = input.value.toLowerCase();
    const filas = document.querySelectorAll("#tablaFacturas tbody tr");

    filas.forEach(fila => {
        const celdaNombre = fila.cells[0]; // columna nombre
        if (celdaNombre) {
          const texto = celdaNombre.textContent.toLowerCase();
          fila.style.display = texto.includes(filtro) ? "" : "none";
        }
    });
}

function filtrarTabla() {
    const input = document.getElementById("busqueda");
    const filtro = input.value.toLowerCase();
    const filas = document.querySelectorAll("#tablaReportes tbody tr");

    filas.forEach(fila => {
        const celdaNombre = fila.cells[0];
        if (celdaNombre) {
            const texto = celdaNombre.textContent.toLowerCase();
            fila.style.display = texto.includes(filtro) ? "" : "none";
        }
    });
}

function generarReporte() {
    if (confirm("¿Deseas generar un nuevo reporte de inventario?")) {
        window.location.href = "/reporte/inventario";
        }
}

function filtrarUsuarios() {
        // Obtener los valores de búsqueda
    const filtroTexto = document.getElementById("busquedaProducto").value.toLowerCase();
    const filtroRol = document.getElementById("filtrorol").value.toLowerCase();
    const filtroEstado = document.getElementById("filtroestado").value.toLowerCase();

        // Obtener todas las filas de la tabla (excepto el encabezado)
    const filas = document.querySelectorAll("#tablaUsuarios tbody tr");

    filas.forEach(fila => {
        const usuario = fila.children[1].textContent.toLowerCase();  // Columna de usuario
        const rol = fila.children[6].textContent.toLowerCase();      // Columna de rol
        const estado = fila.children[7].textContent.toLowerCase();   // Columna de estado

        const coincideUsuario = usuario.includes(filtroTexto);
        const coincideRol = !filtroRol || rol === filtroRol;
        const coincideEstado = !filtroEstado || estado === filtroEstado;

        if (coincideUsuario && coincideRol && coincideEstado) {
            fila.style.display = "";
        } else {
            fila.style.display = "none";
        }
    });
}