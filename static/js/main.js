// Ideas Dashboard - JavaScript Principal

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar tooltips de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Inicializar popovers de Bootstrap
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-dismiss alerts después de 5 segundos
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Confirmación para acciones destructivas
    document.querySelectorAll('[data-confirm]').forEach(function(element) {
        element.addEventListener('click', function(e) {
            var message = this.getAttribute('data-confirm') || '¿Estás seguro?';
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    });

    // Animación de entrada para elementos
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    // Observar elementos para animación
    document.querySelectorAll('.card, .alert').forEach(function(el) {
        observer.observe(el);
    });

    // Mejorar experiencia de formularios
    document.querySelectorAll('form').forEach(function(form) {
        form.addEventListener('submit', function(e) {
            var submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.classList.add('loading');
                submitBtn.disabled = true;
                
                // Crear spinner
                var spinner = document.createElement('span');
                spinner.className = 'spinner-border spinner-border-sm me-2';
                spinner.setAttribute('role', 'status');
                spinner.setAttribute('aria-hidden', 'true');
                
                submitBtn.insertBefore(spinner, submitBtn.firstChild);
            }
        });
    });

    // Validación en tiempo real para formularios
    document.querySelectorAll('.needs-validation').forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });

        // Validación en tiempo real
        form.querySelectorAll('input, textarea, select').forEach(function(input) {
            input.addEventListener('blur', function() {
                if (this.checkValidity()) {
                    this.classList.remove('is-invalid');
                    this.classList.add('is-valid');
                } else {
                    this.classList.remove('is-valid');
                    this.classList.add('is-invalid');
                }
            });
        });
    });

    // Contador de caracteres para textareas
    document.querySelectorAll('textarea[maxlength]').forEach(function(textarea) {
        var maxLength = textarea.getAttribute('maxlength');
        var counter = document.createElement('div');
        counter.className = 'form-text text-end';
        counter.innerHTML = '<span class="char-count">0</span>/' + maxLength + ' caracteres';
        
        textarea.parentNode.appendChild(counter);
        
        textarea.addEventListener('input', function() {
            var currentLength = this.value.length;
            var charCount = counter.querySelector('.char-count');
            charCount.textContent = currentLength;
            
            if (currentLength > maxLength * 0.9) {
                charCount.classList.add('text-warning');
            } else {
                charCount.classList.remove('text-warning');
            }
        });
    });

    // Smooth scroll para enlaces internos
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            var target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Mejorar accesibilidad
    document.querySelectorAll('button, a').forEach(function(element) {
        if (!element.getAttribute('aria-label') && !element.textContent.trim()) {
            var icon = element.querySelector('i');
            if (icon) {
                var iconClass = icon.className;
                var label = '';
                
                if (iconClass.includes('fa-edit')) label = 'Editar';
                else if (iconClass.includes('fa-trash')) label = 'Eliminar';
                else if (iconClass.includes('fa-plus')) label = 'Agregar';
                else if (iconClass.includes('fa-save')) label = 'Guardar';
                else if (iconClass.includes('fa-times')) label = 'Cancelar';
                else if (iconClass.includes('fa-arrow-left')) label = 'Volver';
                else if (iconClass.includes('fa-sign-out-alt')) label = 'Cerrar sesión';
                
                if (label) {
                    element.setAttribute('aria-label', label);
                }
            }
        }
    });

    // Lazy loading para imágenes (si las hay en el futuro)
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(function(img) {
            imageObserver.observe(img);
        });
    }

    // Notificaciones toast personalizadas
    window.showToast = function(message, type = 'info') {
        var toastContainer = document.getElementById('toast-container') || createToastContainer();
        
        var toast = document.createElement('div');
        toast.className = 'toast align-items-center text-white bg-' + type + ' border-0';
        toast.setAttribute('role', 'alert');
        toast.setAttribute('aria-live', 'assertive');
        toast.setAttribute('aria-atomic', 'true');
        
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-triangle' : 'info-circle'} me-2"></i>
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        `;
        
        toastContainer.appendChild(toast);
        
        var bsToast = new bootstrap.Toast(toast);
        bsToast.show();
        
        // Remover el toast del DOM después de que se oculte
        toast.addEventListener('hidden.bs.toast', function() {
            toast.remove();
        });
    };

    function createToastContainer() {
        var container = document.createElement('div');
        container.id = 'toast-container';
        container.className = 'toast-container position-fixed top-0 end-0 p-3';
        container.style.zIndex = '9999';
        document.body.appendChild(container);
        return container;
    }
});

// Funciones utilitarias globales
window.utils = {
    // Formatear fecha
    formatDate: function(date) {
        return new Date(date).toLocaleDateString('es-ES', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    },
    
    // Debounce para búsquedas
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = function() {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Copiar al portapapeles
    copyToClipboard: function(text) {
        navigator.clipboard.writeText(text).then(function() {
            window.showToast('Copiado al portapapeles', 'success');
        }).catch(function() {
            window.showToast('Error al copiar', 'error');
        });
    }
};
