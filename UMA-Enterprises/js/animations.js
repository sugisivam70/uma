/* ==========================================================================
   UMA ENTERPRISES — GSAP, ScrollTrigger & Lenis Motion System
   ========================================================================== */
document.addEventListener('DOMContentLoaded', () => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isMobile = window.innerWidth < 768;

  let lenis = null;
  if (!prefersReducedMotion && window.Lenis) {
    lenis = new Lenis({
      duration: 1.05,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true
    });
    if (window.gsap && window.ScrollTrigger) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((time) => lenis.raf(time * 1000));
      gsap.ticker.lagSmoothing(0);
    }
  }

  if (prefersReducedMotion || !window.gsap) return;
  if (window.ScrollTrigger) gsap.registerPlugin(ScrollTrigger);

  // Hero Headline & Elements Stagger
  const heroReveals = document.querySelectorAll('.hero-reveal');
  if (heroReveals.length) {
    gsap.from(heroReveals, {
      y: 26,
      opacity: 0,
      duration: 0.85,
      stagger: 0.1,
      ease: 'power3.out',
      clearProps: 'transform,opacity'
    });
  }

  // Image Mask Clip-Path Reveal
  document.querySelectorAll('.clip-reveal').forEach((el) => {
    gsap.from(el, {
      clipPath: 'inset(0 0 100% 0)',
      duration: 1.0,
      ease: 'power3.out',
      clearProps: 'clip-path',
      scrollTrigger: { trigger: el, start: 'top 88%', once: true }
    });
  });

  // Varied Scroll Reveals
  document.querySelectorAll('.reveal-up').forEach((el) => {
    gsap.from(el, {
      y: isMobile ? 16 : 28,
      opacity: 0,
      duration: 0.72,
      ease: 'power2.out',
      clearProps: 'transform,opacity',
      scrollTrigger: { trigger: el, start: 'top 87%', once: true }
    });
  });

  document.querySelectorAll('.reveal-left').forEach((el) => {
    gsap.from(el, {
      x: isMobile ? 0 : -32,
      y: isMobile ? 16 : 0,
      opacity: 0,
      duration: 0.78,
      ease: 'power2.out',
      clearProps: 'transform,opacity',
      scrollTrigger: { trigger: el, start: 'top 86%', once: true }
    });
  });

  document.querySelectorAll('.reveal-scale').forEach((el) => {
    gsap.from(el, {
      scale: 0.94,
      opacity: 0,
      duration: 0.75,
      ease: 'power2.out',
      clearProps: 'transform,opacity',
      scrollTrigger: { trigger: el, start: 'top 86%', once: true }
    });
  });

  // Staggered Grids
  document.querySelectorAll('.stagger-group').forEach((group) => {
    const items = group.querySelectorAll('.stagger-item');
    if (!items.length) return;
    gsap.from(items, {
      y: 24,
      opacity: 0,
      duration: 0.65,
      stagger: 0.08,
      ease: 'power2.out',
      clearProps: 'transform,opacity',
      scrollTrigger: { trigger: group, start: 'top 85%', once: true }
    });
  });

  // Horizontal Showcase Scroll (Desktop)
  const hWrap = document.querySelector('.h-scroll-wrap');
  const hTrack = document.querySelector('.h-scroll-track');
  if (hWrap && hTrack && !isMobile && window.ScrollTrigger) {
    const getScrollAmount = () => -(hTrack.scrollWidth - hWrap.offsetWidth);
    if (getScrollAmount() < 0) {
      gsap.to(hTrack, {
        x: getScrollAmount,
        ease: 'none',
        scrollTrigger: {
          trigger: hWrap,
          start: 'top 22%',
          end: () => `+=${Math.abs(getScrollAmount())}`,
          pin: true,
          scrub: 1,
          invalidateOnRefresh: true
        }
      });
    }
  }

  // Animated Counters
  document.querySelectorAll('.stat-number[data-count]').forEach((counter) => {
    const target = parseInt(counter.getAttribute('data-count'), 10);
    const suffix = counter.getAttribute('data-suffix') || '';
    const obj = { val: 0 };
    gsap.to(obj, {
      val: target,
      duration: 1.5,
      ease: 'power2.out',
      scrollTrigger: { trigger: counter, start: 'top 88%', once: true },
      onUpdate: () => {
        counter.innerHTML = `${Math.floor(obj.val).toLocaleString()}<span>${suffix}</span>`;
      }
    });
  });

  // Magnetic CTA Buttons
  if (!isMobile && window.matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('.magnetic').forEach((btn) => {
      btn.addEventListener('mousemove', (e) => {
        const rect = btn.getBoundingClientRect();
        const x = (e.clientX - rect.left - rect.width / 2) * 0.16;
        const y = (e.clientY - rect.top - rect.height / 2) * 0.16;
        gsap.to(btn, { x, y, duration: 0.3, ease: 'power2.out' });
      });
      btn.addEventListener('mouseleave', () => {
        gsap.to(btn, { x: 0, y: 0, duration: 0.4, ease: 'elastic.out(1, 0.5)' });
      });
    });
  }
});
