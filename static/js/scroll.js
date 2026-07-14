/* ============================================================
   BRIGHTSMILE DENTAL CARE — SCROLL BEHAVIOR
   Handles: scroll progress bar, scroll-to-top button,
   scroll-triggered fade-in animations, and counter animations
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

    /* ---------- SCROLL PROGRESS BAR ---------- */
    const scrollProgressBar = document.getElementById('scrollProgressBar');

    function updateScrollProgress() {
        if (!scrollProgressBar) return;
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        scrollProgressBar.style.width = progress + '%';
    }

    window.addEventListener('scroll', updateScrollProgress);
    updateScrollProgress();

    /* ---------- SCROLL TO TOP BUTTON ---------- */
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');

    if (scrollToTopBtn) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 400) {
                scrollToTopBtn.classList.add('is-visible');
            } else {
                scrollToTopBtn.classList.remove('is-visible');
            }
        });

        scrollToTopBtn.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    /* ---------- SCROLL-TRIGGERED FADE-IN ANIMATIONS ---------- */
    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    if ('IntersectionObserver' in window && animatedElements.length > 0) {
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15 });

        animatedElements.forEach(function (el) {
            observer.observe(el);
        });
    } else {
        // Fallback: reveal everything immediately if unsupported.
        animatedElements.forEach(function (el) {
            el.classList.add('is-visible');
        });
    }

    /* ---------- ANIMATED COUNTERS (e.g. 15+ Years, 2500+ Patients) ---------- */
    const counterElements = document.querySelectorAll('.counter');

    function animateCounter(el) {
        const target = parseInt(el.getAttribute('data-target'), 10) || 0;
        const suffix = el.getAttribute('data-suffix') || '';
        const duration = 1500;
        const startTime = performance.now();

        function step(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const value = Math.floor(progress * target);
            el.textContent = value + suffix;

            if (progress < 1) {
                requestAnimationFrame(step);
            } else {
                el.textContent = target + suffix;
            }
        }

        requestAnimationFrame(step);
    }

    if ('IntersectionObserver' in window && counterElements.length > 0) {
        const counterObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        counterElements.forEach(function (el) {
            counterObserver.observe(el);
        });
    }

});