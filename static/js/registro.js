document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('contraseña');
    const confirmPasswordInput = document.getElementById('confirmar_contraseña')
    const passwordStrengthDisplay = document.querySelector('.password-strength');
    const passwordMatchFeedbackDisplay = document.querySelector('.password-match-feedback');

    // Función para alternar visibilidad de contraseña
    window.togglePasswordVisibility = function(id) {
        const input = document.getElementById(id);
        const icon = input.nextElementSibling.querySelector('i');

        if (input.type === 'password') {
            input.type = 'text';
            icon.classList.remove('fa-eye');
            icon.classList.add('fa-eye-slash');
        } else {
            input.type = 'password';
            icon.classList.remove('fa-eye-slash');
            icon.classList.add('fa-eye');
        }
    };

    if (passwordInput && passwordStrengthDisplay) {
        passwordInput.addEventListener('input', updatePasswordStrength);
    }
    if (confirmPasswordInput && passwordMatchFeedbackDisplay) {
        confirmPasswordInput.addEventListener('input', checkPasswordMatch);
    }

    if (passwordInput) updatePasswordStrength();
    if (confirmPasswordInput) checkPasswordMatch();


    function updatePasswordStrength() {
        const password = passwordInput.value;
        let strength = 0;
        let feedback = '';
        passwordStrengthDisplay.className = 'password-strength';

        if (password.length >= 8) strength++;
        if (/[A-Z]/.test(password)) strength++;
        if (/[a-z]/.test(password)) strength++;
        if (/[0-9]/.test(password)) strength++;
        if (/[^A-Za-z0-9]/.test(password)) strength++;

        if (password.length > 0) {
            if (strength <= 2) {
                feedback = 'Débil';
                passwordStrengthDisplay.classList.add('weak');
            } else if (strength <= 4) {
                feedback = 'Moderada';
                passwordStrengthDisplay.classList.add('moderate');
            } else {
                feedback = 'Fuerte';
                passwordStrengthDisplay.classList.add('strong');
            }
            passwordStrengthDisplay.textContent = `Fortaleza: ${feedback}`;
        } else {
            passwordStrengthDisplay.textContent = '';
        }
        checkPasswordMatch();
    }

    function checkPasswordMatch() {
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;
        passwordMatchFeedbackDisplay.className = 'password-match-feedback';

        if (confirmPassword.length > 0) {
            if (password === confirmPassword) {
                passwordMatchFeedbackDisplay.textContent = 'Las contraseñas coinciden.';
                passwordMatchFeedbackDisplay.classList.add('match');
            } else {
                passwordMatchFeedbackDisplay.textContent = 'Las contraseñas no coinciden.';
                passwordMatchFeedbackDisplay.classList.add('no-match');
            }
        } else {
            passwordMatchFeedbackDisplay.textContent = ''; 
        }
    }
});