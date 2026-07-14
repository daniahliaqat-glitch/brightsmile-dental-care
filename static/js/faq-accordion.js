/* ============================================================
   BRIGHTSMILE DENTAL CARE — FAQ ACCORDION
   Handles expand/collapse behavior for FAQ and Insurance pages
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(function (item) {
        const questionBtn = item.querySelector('.faq-item__question');

        if (!questionBtn) return;

        questionBtn.addEventListener('click', function () {
            const isOpen = item.classList.contains('is-open');

            // Close all other open FAQ items within the same accordion group.
            const parentAccordion = item.closest('.faq-accordion');
            if (parentAccordion) {
                parentAccordion.querySelectorAll('.faq-item.is-open').forEach(function (openItem) {
                    if (openItem !== item) {
                        openItem.classList.remove('is-open');
                    }
                });
            }

            if (isOpen) {
                item.classList.remove('is-open');
            } else {
                item.classList.add('is-open');
            }
        });
    });

});