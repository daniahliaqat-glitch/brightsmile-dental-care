/* ============================================================
   BRIGHTSMILE DENTAL CARE — DARK MODE TOGGLE
   Persists the visitor's preference across pages and reloads
   using localStorage. Defaults to light mode unless the visitor
   has explicitly toggled dark mode themselves.
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

    const darkModeToggle = document.getElementById('darkModeToggle');
    const STORAGE_KEY = 'brightsmile-theme';

    function updateToggleIcon(isDark) {
        if (!darkModeToggle) return;
        const icon = darkModeToggle.querySelector('i');
        if (!icon) return;

        if (isDark) {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    }

    /* ---------- APPLY SAVED PREFERENCE ON PAGE LOAD ---------- */
    /* Default is always LIGHT mode unless the visitor explicitly
       toggled dark mode on a previous visit (saved in localStorage). */
    const savedTheme = localStorage.getItem(STORAGE_KEY);

    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        updateToggleIcon(true);
    } else {
        document.body.classList.remove('dark-mode');
        updateToggleIcon(false);
    }

    /* ---------- TOGGLE ON CLICK AND SAVE PREFERENCE ---------- */
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function () {
            const isDark = document.body.classList.toggle('dark-mode');
            updateToggleIcon(isDark);
            localStorage.setItem(STORAGE_KEY, isDark ? 'dark' : 'light');
        });
    }

});