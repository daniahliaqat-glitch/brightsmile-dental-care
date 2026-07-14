/* ============================================================
   BRIGHTSMILE DENTAL CARE — FORM VALIDATION
   Lightweight client-side validation for public-facing forms
   (appointment booking, contact form, newsletter, testimonials)
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

    const validatedForms = document.querySelectorAll('form[data-validate="true"]');

    validatedForms.forEach(function (form) {
        form.addEventListener('submit', function (event) {
            let isValid = true;

            const requiredFields = form.querySelectorAll('[required]');

            requiredFields.forEach(function (field) {
                clearFieldError(field);

                if (!field.value || field.value.trim() === '') {
                    showFieldError(field, 'This field is required.');
                    isValid = false;
                    return;
                }

                if (field.type === 'email' && !isValidEmail(field.value)) {
                    showFieldError(field, 'Please enter a valid email address.');
                    isValid = false;
                }

                if (field.type === 'tel' && field.value.replace(/\D/g, '').length < 7) {
                    showFieldError(field, 'Please enter a valid phone number.');
                    isValid = false;
                }
            });

            if (!isValid) {
                event.preventDefault();
            }
        });

        // Clear error styling as the visitor starts correcting a field.
        form.querySelectorAll('input, textarea, select').forEach(function (field) {
            field.addEventListener('input', function () {
                clearFieldError(field);
            });
        });
    });

    function isValidEmail(value) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    }

    function showFieldError(field, message) {
        field.classList.add('is-invalid');

        let errorEl = field.parentElement.querySelector('.field-error');
        if (!errorEl) {
            errorEl = document.createElement('span');
            errorEl.classList.add('field-error');
            field.parentElement.appendChild(errorEl);
        }
        errorEl.textContent = message;
    }

    function clearFieldError(field) {
        field.classList.remove('is-invalid');
        const errorEl = field.parentElement.querySelector('.field-error');
        if (errorEl) {
            errorEl.remove();
        }
    }

});