/* ==========================================================================
   UMA ENTERPRISES — Main UI, Page Transitions & Central Placeholder Config
   ========================================================================== */
window.UMA_CONTACT_CONFIG = {
  companyName: 'UMA Enterprises',
  phone: '+91 XXXXX XXXXX',
  email: 'info@example.com',
  whatsapp: 'Placeholder number',
  address: 'Industrial Area, City, State, India – XXXXXX',
  location: 'Placeholder location',
  liveContactEnabled: false
};

document.addEventListener('DOMContentLoaded', () => {
  if (window.lucide) {
    window.lucide.createIcons();
  }

  // Page Curtain Reveal
  const curtain = document.querySelector('.page-curtain');
  if (curtain) {
    setTimeout(() => curtain.classList.add('is-hidden'), 280);
  }

  // Smooth Page Transition on internal HTML links
  document.querySelectorAll('a[href$=".html"]').forEach((link) => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (!href || href.startsWith('http') || link.target === '_blank') return;
      if (curtain) {
        e.preventDefault();
        curtain.classList.remove('is-hidden');
        setTimeout(() => { window.location.href = href; }, 220);
      }
    });
  });

  // Floating Header, Progress Bar & Back-to-Top
  const header = document.querySelector('.site-header');
  const backToTop = document.querySelector('.util-top');
  const scrollProgress = document.querySelector('.scroll-progress');

  const onScroll = () => {
    const y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle('is-scrolled', y > 36);
    if (backToTop) backToTop.classList.toggle('is-visible', y > 420);
    if (scrollProgress) {
      const docH = document.documentElement.scrollHeight - window.innerHeight;
      scrollProgress.style.width = `${docH > 0 ? Math.min(100, (y / docH) * 100) : 0}%`;
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (backToTop) {
    backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  // Mobile Drawer
  const navToggle = document.querySelector('.nav-toggle');
  const mobileDrawer = document.querySelector('.mobile-drawer');
  if (navToggle && mobileDrawer) {
    navToggle.addEventListener('click', () => {
      const isOpen = mobileDrawer.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', String(isOpen));
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });
    mobileDrawer.querySelectorAll('a').forEach((a) => {
      a.addEventListener('click', () => {
        mobileDrawer.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  // Placeholder WhatsApp Handler
  document.querySelectorAll('[data-placeholder-whatsapp]').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      alert('WhatsApp enquiry is currently in placeholder mode. Configure a live number before launch.');
    });
  });

  // FAQ Accordion
  document.querySelectorAll('.faq-trigger').forEach((trigger) => {
    trigger.addEventListener('click', () => {
      const item = trigger.closest('.faq-item');
      const content = item.querySelector('.faq-content');
      const isOpen = item.classList.toggle('is-open');
      trigger.setAttribute('aria-expanded', String(isOpen));
      content.style.maxHeight = isOpen ? `${content.scrollHeight}px` : '0px';
    });
  });

  // Expandable Component Information Buttons
  document.querySelectorAll('.expand-btn').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const detail = btn.nextElementSibling;
      if (!detail) return;
      const isOpen = detail.classList.toggle('is-open');
      detail.style.maxHeight = isOpen ? `${detail.scrollHeight}px` : '0px';
      btn.setAttribute('aria-expanded', String(isOpen));
    });
  });

  // Contact Form Validation (No fake success messages)
  const enquiryForm = document.getElementById('uma-enquiry-form');
  if (enquiryForm) {
    enquiryForm.addEventListener('submit', (e) => {
      e.preventDefault();
      let valid = true;
      const fields = [
        { id: 'fullName', msg: 'Please enter your full name.' },
        { id: 'companyName', msg: 'Please enter your company or organization name.' },
        { id: 'emailAddress', msg: 'Please enter a valid email address.', type: 'email' },
        { id: 'phoneNumber', msg: 'Please enter a valid contact phone number.' },
        { id: 'productService', msg: 'Please select a product or service category.' },
        { id: 'projectRequirements', msg: 'Please describe your project requirements.' }
      ];

      fields.forEach((f) => {
        const input = document.getElementById(f.id);
        const errEl = input ? input.parentElement.querySelector('.form-error') : null;
        if (!input || !errEl) return;
        const val = input.value.trim();
        let ok = val.length > 0;
        if (ok && f.type === 'email') ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val);
        errEl.textContent = ok ? '' : f.msg;
        if (!ok) valid = false;
      });

      const notice = document.getElementById('form-status-notice');
      if (!notice) return;
      if (valid) {
        notice.className = 'form-notice info is-visible';
        notice.textContent = 'Form validation passed. Live email submission is disabled while placeholder contact details (info@example.com) are active.';
      } else {
        notice.className = 'form-notice';
        notice.textContent = '';
      }
    });
  }
});
