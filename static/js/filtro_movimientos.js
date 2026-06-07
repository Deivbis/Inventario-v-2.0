document.addEventListener("DOMContentLoaded", function () {
  const tipoSelect = document.getElementById("filtro-tipo");
  const motivoSelect = document.getElementById("filtro-motivo");
  const productoInput = document.getElementById("filtro-producto");
  const filas = document.querySelectorAll("tbody tr");

  function filtrarTabla() {
    const tipo = tipoSelect.value.toLowerCase();
    const motivo = motivoSelect.value.toLowerCase();
    const producto = productoInput.value.toLowerCase();

    filas.forEach(fila => {
      const tipoTexto = fila.children[1].textContent.toLowerCase();
      const productoTexto = fila.children[2].textContent.toLowerCase();
      const motivoTexto = fila.children[4].textContent.toLowerCase();

      const coincideTipo = !tipo || tipoTexto.includes(tipo);
      const coincideMotivo = !motivo || motivoTexto.includes(motivo);
      const coincideProducto = !producto || productoTexto.includes(producto);

      if (coincideTipo && coincideMotivo && coincideProducto) {
        fila.style.display = "";
      } else {
        fila.style.display = "none";
      }
    });
  }

  tipoSelect.addEventListener("change", filtrarTabla);
  motivoSelect.addEventListener("change", filtrarTabla);
  productoInput.addEventListener("input", filtrarTabla);
});
