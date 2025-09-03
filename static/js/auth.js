// Ideas Dashboard - JavaScript para Autenticación

document.addEventListener('DOMContentLoaded', function() {
    // Validación en tiempo real para el formulario de registro
    const registerForm = document.querySelector('form[action*="register"]');
    if (registerForm) {
        setupRegisterValidation(registerForm);
    }

    // Validación en tiempo real para el formulario de login
    const loginForm = document.querySelector('form[action*="login"]');
    if (loginForm) {
        setupLoginValidation(loginForm);
    }

    // Confirmación de contraseña en tiempo real
    const passwordField = document.getElementById('password');
    const confirmPasswordField = document.getElementById('confirm_password');
    
    if (passwordField && confirmPasswordField) {
        confirmPasswordField.addEventListener('input', function() {
            validatePasswordMatch();
        });
        
        passwordField.addEventListener('input', function() {
            validatePasswordMatch();
        });
    }

    // Indicador de fortaleza de contraseña
    if (passwordField) {
        passwordField.addEventListener('input', function() {
            if (this.value.length > 0) {
                showPasswordStrength(this.value);
            } else {
                hidePasswordStrength();
            }
        });
    }

    // Mostrar/ocultar contraseña
    setupPasswordToggle();
});

function setupRegisterValidation(form) {
    const firstName = form.querySelector('#first_name');
    const lastName = form.querySelector('#last_name');
    const email = form.querySelector('#email');
    const password = form.querySelector('#password');
    const confirmPassword = form.querySelector('#confirm_password');

    // Validación de nombre
    if (firstName) {
        firstName.addEventListener('blur', function() {
            validateName(this, 'nombre');
        });
    }

    // Validación de apellido
    if (lastName) {
        lastName.addEventListener('blur', function() {
            validateName(this, 'apellido');
        });
    }

    // Validación de email
    if (email) {
        email.addEventListener('blur', function() {
            validateEmail(this);
        });
    }

    // Validación de contraseña
    if (password) {
        password.addEventListener('blur', function() {
            validatePassword(this);
        });
    }
}

function setupLoginValidation(form) {
    const email = form.querySelector('#login_email');
    const password = form.querySelector('#login_password');

    // Validación de email
    if (email) {
        email.addEventListener('blur', function() {
            validateEmail(this);
        });
    }

    // Validación de contraseña
    if (password) {
        password.addEventListener('blur', function() {
            if (this.value.length === 0) {
                showFieldError(this, 'La contraseña es requerida');
            } else {
                clearFieldError(this);
            }
        });
    }
}

function validateName(field, fieldName) {
    const value = field.value.trim();
    
    if (value.length === 0) {
        showFieldError(field, `El ${fieldName} es requerido`);
        return false;
    } else if (value.length < 2) {
        showFieldError(field, `El ${fieldName} debe tener al menos 2 caracteres`);
        return false;
    } else {
        clearFieldError(field);
        return true;
    }
}

function validateEmail(field) {
    const value = field.value.trim();
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    
    if (value.length === 0) {
        showFieldError(field, 'El email es requerido');
        return false;
    } else if (!emailRegex.test(value)) {
        showFieldError(field, 'El email debe ser válido');
        return false;
    } else {
        clearFieldError(field);
        return true;
    }
}

function validatePassword(field) {
    const value = field.value;
    
    if (value.length === 0) {
        showFieldError(field, 'La contraseña es requerida');
        return false;
    } else if (value.length < 8) {
        showFieldError(field, 'La contraseña debe tener al menos 8 caracteres');
        return false;
    } else {
        clearFieldError(field);
        return true;
    }
}

function validatePasswordMatch() {
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm_password');
    
    if (password && confirmPassword) {
        if (confirmPassword.value.length > 0) {
            if (password.value !== confirmPassword.value) {
                showFieldError(confirmPassword, 'Las contraseñas no coinciden');
                return false;
            } else {
                clearFieldError(confirmPassword);
                return true;
            }
        }
    }
    return true;
}

function showPasswordStrength(password) {
    let strengthContainer = document.getElementById('password-strength');
    
    if (!strengthContainer) {
        strengthContainer = document.createElement('div');
        strengthContainer.id = 'password-strength';
        strengthContainer.className = 'mt-2';
        
        // Insertar después del input-group completo, no dentro de él
        const passwordField = document.getElementById('password');
        const inputGroup = passwordField.closest('.input-group');
        const parentContainer = inputGroup.parentNode;
        
        // Insertar después del input-group
        parentContainer.insertBefore(strengthContainer, inputGroup.nextSibling);
    }
    
    const strength = calculatePasswordStrength(password);
    const strengthText = ['Muy débil', 'Débil', 'Regular', 'Fuerte', 'Muy fuerte'];
    const strengthColors = ['danger', 'warning', 'info', 'success', 'success'];
    
    strengthContainer.style.display = 'block';
    strengthContainer.innerHTML = `
        <div class="d-flex align-items-center gap-2">
            <div class="progress flex-grow-1" style="height: 6px;">
                <div class="progress-bar bg-${strengthColors[strength]}" 
                     style="width: ${(strength + 1) * 20}%"></div>
            </div>
            <small class="text-${strengthColors[strength]} fw-bold">${strengthText[strength]}</small>
        </div>
    `;
}

function hidePasswordStrength() {
    const strengthContainer = document.getElementById('password-strength');
    if (strengthContainer) {
        strengthContainer.style.display = 'none';
    }
}

function calculatePasswordStrength(password) {
    let score = 0;
    
    // Longitud
    if (password.length >= 8) score++;
    if (password.length >= 12) score++;
    if (password.length >= 16) score++;
    
    // Caracteres
    if (/[a-z]/.test(password)) score++;
    if (/[A-Z]/.test(password)) score++;
    if (/[0-9]/.test(password)) score++;
    if (/[^A-Za-z0-9]/.test(password)) score++;
    
    // Patrones comunes (restar puntos)
    if (password.length < 6) score = 0; // Muy corta
    if (/(.)\1{2,}/.test(password)) score--; // Caracteres repetidos
    if (/123|abc|qwe|asd/i.test(password)) score--; // Secuencias comunes
    
    return Math.max(0, Math.min(score, 4));
}

function setupPasswordToggle() {
    // Configurar event listeners para todos los botones de toggle
    const toggleButtons = document.querySelectorAll('button[data-field-id]');
    
    toggleButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            // Obtener el ID del campo desde el data attribute
            const fieldId = this.getAttribute('data-field-id');
            
            if (fieldId) {
                togglePassword(fieldId);
            }
        });
    });
}

// Función global para alternar la visibilidad de la contraseña
function togglePassword(fieldId) {
    const field = document.getElementById(fieldId);
    const icon = document.getElementById(fieldId + '-icon');
    
    if (field && icon) {
        if (field.type === 'password') {
            field.type = 'text';
            icon.className = 'fas fa-eye-slash';
            icon.setAttribute('title', 'Ocultar contraseña');
        } else {
            field.type = 'password';
            icon.className = 'fas fa-eye';
            icon.setAttribute('title', 'Mostrar contraseña');
        }
    }
}

function showFieldError(field, message) {
    clearFieldError(field);
    
    field.classList.add('is-invalid');
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    
    field.parentNode.appendChild(errorDiv);
}

function clearFieldError(field) {
    field.classList.remove('is-invalid');
    field.classList.add('is-valid');
    
    const errorDiv = field.parentNode.querySelector('.invalid-feedback');
    if (errorDiv) {
        errorDiv.remove();
    }
}

// Validación del formulario completo antes del envío
document.addEventListener('submit', function(e) {
    const form = e.target;
    
    if (form.action.includes('register')) {
        if (!validateRegisterForm(form)) {
            e.preventDefault();
        }
    } else if (form.action.includes('login')) {
        if (!validateLoginForm(form)) {
            e.preventDefault();
        }
    }
});

function validateRegisterForm(form) {
    const firstName = form.querySelector('#first_name');
    const lastName = form.querySelector('#last_name');
    const email = form.querySelector('#email');
    const password = form.querySelector('#password');
    const confirmPassword = form.querySelector('#confirm_password');
    
    let isValid = true;
    
    if (!validateName(firstName, 'nombre')) isValid = false;
    if (!validateName(lastName, 'apellido')) isValid = false;
    if (!validateEmail(email)) isValid = false;
    if (!validatePassword(password)) isValid = false;
    if (!validatePasswordMatch()) isValid = false;
    
    return isValid;
}

function validateLoginForm(form) {
    const email = form.querySelector('#login_email');
    const password = form.querySelector('#login_password');
    
    let isValid = true;
    
    if (!validateEmail(email)) isValid = false;
    if (password.value.length === 0) {
        showFieldError(password, 'La contraseña es requerida');
        isValid = false;
    }
    
    return isValid;
}
