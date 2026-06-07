document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle');
    const dashboardContainer = document.getElementById('dashboard');
    const hasSubmenus = document.querySelectorAll('.has-submenu');

    const config = typeof window.config !== 'undefined' ? window.config : {
        mostrar_sidebar_por_defecto: 'true',
        habilitar_animaciones_ui: 'true'
    };

    if (dashboardContainer && menuToggle) {
        if (config.mostrar_sidebar_por_defecto === 'true') {
            dashboardContainer.classList.add('menu-open');
            menuToggle.classList.add('open');
        } else {
            dashboardContainer.classList.remove('menu-open');
            menuToggle.classList.remove('open');
        }
    }

    if (config.habilitar_animaciones_ui === 'false') {
        document.documentElement.style.setProperty('--transition-speed', '0s');
        const elementsWithTransitions = document.querySelectorAll('[style*="transition"], [class*="transition"]');
        elementsWithTransitions.forEach(el => {
            el.style.setProperty('transition', 'none', 'important');
            el.style.setProperty('animation', 'none', 'important');
        });
    } else {
        document.documentElement.style.removeProperty('--transition-speed');
        document.querySelectorAll('[style*="transition"], [class*="transition"]').forEach(el => {
            el.style.removeProperty('transition');
            el.style.removeProperty('animation');
        });
    }

    if (menuToggle && dashboardContainer) {
        menuToggle.addEventListener('click', function() {
            dashboardContainer.classList.toggle('menu-open');
            menuToggle.classList.toggle('open');
        });
    }

    hasSubmenus.forEach(item => {
        const link = item.querySelector('a');
        const arrowIcon = link.querySelector('.arrow');

        link.addEventListener('click', function(e) {
            e.preventDefault();
            item.classList.toggle('open');
            if (arrowIcon) {
                arrowIcon.classList.toggle('rotate');
            }
            const isExpanded = item.classList.contains('open');
            link.setAttribute('aria-expanded', isExpanded);
        });
    });

    window.addEventListener('resize', function() {
        if (window.innerWidth <= 768) {
            if (dashboardContainer && dashboardContainer.classList.contains('menu-open')) {
                dashboardContainer.classList.remove('menu-open');
                menuToggle.classList.remove('open');
            }
        }
    });

    if (typeof salesLabels !== 'undefined' && typeof salesData !== 'undefined' && typeof categoryLabels !== 'undefined' && typeof categoryData !== 'undefined') {
        const salesCtx = document.getElementById('salesChart');
        if (salesCtx) {
            new Chart(salesCtx.getContext('2d'), {
                type: 'bar',
                data: {
                    labels: salesLabels,
                    datasets: [{
                        label: 'Ingresos Mensuales ($)',
                        data: salesData,
                        backgroundColor: 'rgba(75, 192, 192, 0.6)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Ingresos ($)'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Mes'
                            }
                        }
                    }
                }
            });
        }


        const categoryCtx = document.getElementById('categoryChart');
        if (categoryCtx) {
            new Chart(categoryCtx.getContext('2d'), {
                type: 'bar',
                data: {
                    labels: categoryLabels,
                    datasets: [{
                        label: 'Cantidad de Productos',
                        data: categoryData,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.6)',
                            'rgba(54, 162, 235, 0.6)',
                            'rgba(255, 206, 86, 0.6)',
                            'rgba(75, 192, 192, 0.6)',
                            'rgba(153, 102, 255, 0.6)',
                            'rgba(255, 159, 64, 0.6)'
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        tooltip: {
                            callbacks: {
                                label: function(tooltipItem) {
                                    return tooltipItem.label + ': ' + tooltipItem.raw + ' productos';
                                }
                            }
                        }
                    }
                }
            });
        }
    }
});

// Lógica para mantener un solo submenu abierto a la vez
document.addEventListener("DOMContentLoaded", function () {
  const submenuLinks = document.querySelectorAll('.has-submenu > a');

  submenuLinks.forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault();

      const parentLi = this.parentElement;
      const submenu = this.nextElementSibling;
      const isOpen = submenu.style.display === 'block';

      // Cerramos todos los submenús
      document.querySelectorAll('.has-submenu .submenu').forEach(sub => {
        sub.style.display = 'none';
      });

      document.querySelectorAll('.has-submenu').forEach(item => {
        item.classList.remove('open');
      });

      // Si no estaba abierto, lo abrimos
      if (!isOpen) {
        submenu.style.display = 'block';
        parentLi.classList.add('open');
      }
    });
  });
});
