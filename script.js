// ============================================================
// GAURESH NAIK CV — script.js
// Typing animation · Custom cursor · Scroll observer · Nav · Mobile menu
// ============================================================

(function () {
  'use strict';

  /* ── Helpers ─────────────────────────────────────────── */
  const isTouchDevice = () =>
    window.matchMedia('(hover: none)').matches ||
    'ontouchstart' in window;

  /* ── Custom Cursor ────────────────────────────────────── */
  if (!isTouchDevice()) {
    const dot  = document.getElementById('cursorDot');
    const ring = document.getElementById('cursorRing');

    if (dot && ring) {
      let dotX = 0, dotY = 0;
      let ringX = 0, ringY = 0;

      document.addEventListener('mousemove', (e) => {
        dotX = e.clientX;
        dotY = e.clientY;
        dot.style.left = dotX + 'px';
        dot.style.top  = dotY + 'px';
      });

      // Ring follows with smooth lag
      (function animateRing() {
        ringX += (dotX - ringX) * 0.11;
        ringY += (dotY - ringY) * 0.11;
        ring.style.left = ringX + 'px';
        ring.style.top  = ringY + 'px';
        requestAnimationFrame(animateRing);
      })();

      // Scale ring on interactive elements
      const addHoverListeners = () => {
        document
          .querySelectorAll('a, button, .skill-pill, .stat-card, .project-card, .btn, .link-btn')
          .forEach(el => {
            el.addEventListener('mouseenter', () => ring.classList.add('hovered'));
            el.addEventListener('mouseleave', () => ring.classList.remove('hovered'));
          });
      };
      addHoverListeners();

      // Fade cursor when leaving window
      document.addEventListener('mouseleave', () => {
        dot.style.opacity  = '0';
        ring.style.opacity = '0';
      });
      document.addEventListener('mouseenter', () => {
        dot.style.opacity  = '1';
        ring.style.opacity = '1';
      });
    }
  }

  /* ── Navigation Scroll Effect ─────────────────────────── */
  const navbar = document.getElementById('navbar');
  if (navbar) {
    const onScroll = () => {
      navbar.classList.toggle('scrolled', window.scrollY > 60);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll(); // run once on load
  }

  /* ── Mobile Hamburger Menu ────────────────────────────── */
  const hamburger    = document.getElementById('hamburger');
  const mobileOverlay = document.getElementById('mobileNavOverlay');
  const mobileClose  = document.getElementById('mobileClose');
  const mobileLinks  = document.querySelectorAll('.mobile-nav-link');
  const [s1, s2, s3] = hamburger ? hamburger.querySelectorAll('span') : [];
  let menuOpen = false;

  function openMenu() {
    menuOpen = true;
    mobileOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    hamburger.setAttribute('aria-expanded', 'true');
    if (s1) s1.style.transform = 'rotate(45deg) translate(5px, 5px)';
    if (s2) s2.style.opacity   = '0';
    if (s3) s3.style.transform = 'rotate(-45deg) translate(5px, -5px)';
  }

  function closeMenu() {
    menuOpen = false;
    mobileOverlay.classList.remove('open');
    document.body.style.overflow = '';
    hamburger.setAttribute('aria-expanded', 'false');
    if (s1) s1.style.transform = '';
    if (s2) s2.style.opacity   = '';
    if (s3) s3.style.transform = '';
  }

  if (hamburger) {
    hamburger.addEventListener('click', () => (menuOpen ? closeMenu() : openMenu()));
  }
  if (mobileClose) {
    mobileClose.addEventListener('click', closeMenu);
  }
  mobileLinks.forEach(link => link.addEventListener('click', closeMenu));

  // Close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menuOpen) closeMenu();
  });

  /* ── Typing Animation ─────────────────────────────────── */
  const typingEl = document.getElementById('typingText');

  if (typingEl) {
    const titles = [
      'Marketing & Sales Professional',
      'Revenue & Operations Lead',
      'Systems Builder & Automator',
      'Content Strategist',
    ];

    let titleIdx  = 0;
    let charIdx   = 0;
    let isDeleting = false;
    const TYPE_SPEED   = 62;
    const DELETE_SPEED = 32;
    const PAUSE_AFTER  = 2200;
    const PAUSE_BEFORE = 400;

    function type() {
      const current = titles[titleIdx];

      if (!isDeleting) {
        typingEl.textContent = current.slice(0, charIdx + 1);
        charIdx++;

        if (charIdx === current.length) {
          isDeleting = true;
          setTimeout(type, PAUSE_AFTER);
          return;
        }
        setTimeout(type, TYPE_SPEED);
      } else {
        typingEl.textContent = current.slice(0, charIdx - 1);
        charIdx--;

        if (charIdx === 0) {
          isDeleting  = false;
          titleIdx    = (titleIdx + 1) % titles.length;
          setTimeout(type, PAUSE_BEFORE);
          return;
        }
        setTimeout(type, DELETE_SPEED);
      }
    }

    // Delay start until hero animations finish
    setTimeout(type, 820);
  }

  /* ── IntersectionObserver — Sections ─────────────────── */
  const sections = document.querySelectorAll('.section');

  if ('IntersectionObserver' in window && sections.length) {
    const sectionObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
            // Once visible, no need to observe again
            sectionObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1 }
    );
    sections.forEach(s => sectionObserver.observe(s));
  } else {
    // Fallback: show all sections
    sections.forEach(s => s.classList.add('in-view'));
  }

  /* ── IntersectionObserver — Project Cards ────────────── */
  const projectCards = document.querySelectorAll('.project-card');

  if ('IntersectionObserver' in window && projectCards.length) {
    const cardObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry, i) => {
          if (entry.isIntersecting) {
            // stagger by index within the grid
            const cards = [...projectCards];
            const idx = cards.indexOf(entry.target);
            setTimeout(() => {
              entry.target.classList.add('in-view');
            }, idx * 90);
            cardObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1 }
    );
    projectCards.forEach(c => cardObserver.observe(c));
  } else {
    projectCards.forEach(c => c.classList.add('in-view'));
  }

  /* ── IntersectionObserver — Skill Pills (stagger) ──────── */
  const skillsSection = document.getElementById('skills');
  const allPills      = document.querySelectorAll('.skill-pill');
  let pillsTriggered  = false;

  if ('IntersectionObserver' in window && skillsSection && allPills.length) {
    const pillObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting && !pillsTriggered) {
            pillsTriggered = true;
            allPills.forEach((pill, i) => {
              setTimeout(() => pill.classList.add('visible'), i * 28);
            });
            pillObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.18 }
    );
    pillObserver.observe(skillsSection);
  } else {
    allPills.forEach(p => p.classList.add('visible'));
  }

  /* ── Smooth Scroll (anchor links) ───────────────────────  */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const href   = anchor.getAttribute('href');
      const target = document.querySelector(href);
      if (target && href !== '#') {
        e.preventDefault();
        const offset = 80; // nav height
        const top    = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* ── Contact Form Guard ──────────────────────────────── */
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      const action = contactForm.getAttribute('action') || '';
      if (action.includes('REPLACE_WITH_ID')) {
        e.preventDefault();
        // Show a friendly inline message instead of an alert
        const existing = contactForm.querySelector('.form-notice');
        if (!existing) {
          const notice = document.createElement('p');
          notice.className = 'form-notice';
          notice.style.cssText =
            'font-family:var(--font-mono);font-size:11px;color:var(--accent-amber);' +
            'border:1px dashed rgba(245,166,35,0.3);border-radius:8px;padding:10px 14px;' +
            'margin-top:4px;';
          notice.textContent =
            'Form not yet configured. Email directly: naikg8033@gmail.com';
          contactForm.appendChild(notice);
        }
      }
    });
  }

})();
