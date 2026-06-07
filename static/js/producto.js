document.addEventListener("DOMContentLoaded", function () {
  const imagenes = document.querySelectorAll('.img-producto');
  const modal = document.getElementById('modalImagen');
  const imagenAmpliada = document.getElementById('imagenAmpliada');
  const cerrar = document.querySelector('.close-modal');

  imagenes.forEach(img => {
    img.style.cursor = 'pointer';
    img.addEventListener('click', (e) => {
      e.stopPropagation(); // 🔒 Detiene el clic de propagarse a filas/padres
      imagenAmpliada.src = img.src;
      modal.style.display = 'flex';
    });
  });

  cerrar.addEventListener('click', () => {
    modal.style.display = 'none';
  });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.style.display = 'none';
    }
  });
});
