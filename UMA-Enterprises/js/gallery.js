/* ==========================================================================
   UMA ENTERPRISES — Category Filtering & Full-Screen Lightbox
   ========================================================================== */
document.addEventListener('DOMContentLoaded', () => {
  const filterBtns = document.querySelectorAll('.filter-btn[data-filter]');
  const filterItems = document.querySelectorAll('.filter-item[data-category]');

  if (filterBtns.length && filterItems.length) {
    filterBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        filterBtns.forEach((b) => b.classList.remove('is-active'));
        btn.classList.add('is-active');
        const selected = btn.getAttribute('data-filter');
        filterItems.forEach((item) => {
          const cats = (item.getAttribute('data-category') || '').split(/\s+/);
          item.style.display = (selected === 'all' || cats.includes(selected)) ? '' : 'none';
        });
        if (window.ScrollTrigger) ScrollTrigger.refresh();
      });
    });
  }

  const lightbox = document.getElementById('uma-lightbox');
  if (!lightbox) return;

  const lbImg = lightbox.querySelector('.lightbox-img');
  const lbTitle = lightbox.querySelector('.lightbox-title');
  const lbDesc = lightbox.querySelector('.lightbox-desc');
  const lbClose = lightbox.querySelector('.lightbox-close');

  const openLightbox = (src, title, desc) => {
    if (lbImg) { lbImg.src = src; lbImg.alt = title || 'Illustrative Composite Visual'; }
    if (lbTitle) lbTitle.textContent = title || '';
    if (lbDesc) lbDesc.textContent = desc || '';
    lightbox.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  };

  const closeLightbox = () => {
    lightbox.classList.remove('is-open');
    document.body.style.overflow = '';
  };

  document.querySelectorAll('[data-lightbox]').forEach((trigger) => {
    trigger.addEventListener('click', (e) => {
      if (e.target.closest('.expand-btn')) return;
      const src = trigger.getAttribute('data-src') || trigger.querySelector('img')?.src;
      const title = trigger.getAttribute('data-title') || '';
      const desc = trigger.getAttribute('data-desc') || '';
      if (src) openLightbox(src, title, desc);
    });
  });

  if (lbClose) lbClose.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => { if (e.target === lightbox) closeLightbox(); });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox.classList.contains('is-open')) closeLightbox();
  });
});
