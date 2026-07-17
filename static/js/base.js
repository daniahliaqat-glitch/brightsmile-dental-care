/* ============================================================
   BRIGHTSMILE DENTAL CARE — BASE JAVASCRIPT
   Handles: loading screen, mobile navbar, dropdowns, sticky navbar
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

    /* ---------- LOADING SCREEN ---------- */
    const loadingScreen = document.getElementById('loadingScreen');
    if (loadingScreen) {
        window.addEventListener('load', function () {
            setTimeout(function () {
                loadingScreen.classList.add('is-hidden');
            }, 400);
        });
    }

    /* ---------- MOBILE NAVBAR TOGGLE ---------- */
    const navbarToggle = document.getElementById('navbarToggle');
    const navbarLinks = document.getElementById('navbarLinks');

    if (navbarToggle && navbarLinks) {
        // Create overlay element for mobile drawer
        const overlay = document.createElement('div');
        overlay.classList.add('navbar-overlay');
        document.body.appendChild(overlay);

        function openMobileMenu() {
            navbarLinks.classList.add('is-open');
            overlay.classList.add('is-visible');
            document.body.style.overflow = 'hidden';
        }

        function closeMobileMenu() {
            navbarLinks.classList.remove('is-open');
            overlay.classList.remove('is-visible');
            document.body.style.overflow = '';
        }

        navbarToggle.addEventListener('click', function () {
            if (navbarLinks.classList.contains('is-open')) {
                closeMobileMenu();
            } else {
                openMobileMenu();
            }
        });

        overlay.addEventListener('click', closeMobileMenu);

        // Close mobile menu when a nav link is clicked
        // Close mobile menu when an actual nav link is clicked
        // (but NOT dropdown toggle buttons like "Pages", which should
        // expand their submenu instead of closing the whole drawer)
        navbarLinks.querySelectorAll('.navbar__link:not(.navbar__dropdown-toggle)').forEach(function (link) {
            link.addEventListener('click', closeMobileMenu);
        });
    }

    /* ---------- MOBILE DROPDOWN TOGGLES (Pages, User Menu) ---------- */
    const dropdownToggles = document.querySelectorAll('.navbar__dropdown-toggle');

    dropdownToggles.forEach(function (toggle) {
        toggle.addEventListener('click', function (event) {
            if (window.innerWidth <= 991) {
                event.preventDefault();
                const parentDropdown = toggle.closest('.navbar__dropdown');
                parentDropdown.classList.toggle('is-open');
            }
        });
    });

    /* ---------- STICKY NAVBAR SHADOW ON SCROLL ---------- */
    const mainNavbar = document.getElementById('mainNavbar');
    if (mainNavbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 10) {
                mainNavbar.classList.add('is-scrolled');
            } else {
                mainNavbar.classList.remove('is-scrolled');
            }
        });
    }

    /* ---------- AUTO-DISMISS MESSAGES AFTER 5 SECONDS ---------- */
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(40px)';
            setTimeout(function () {
                alert.remove();
            }, 300);
        }, 5000);
    });

});