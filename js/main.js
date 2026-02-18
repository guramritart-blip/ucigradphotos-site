/**
 * UCI Grad Photos - Main JavaScript
 * Vanilla JS, no dependencies.
 */

document.addEventListener('DOMContentLoaded', function () {

  // -------------------------------------------------------
  // 1. Navbar scroll behavior
  // -------------------------------------------------------
  const navbar = document.querySelector('.navbar, nav');

  if (navbar) {
    function handleNavbarScroll() {
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }
    window.addEventListener('scroll', handleNavbarScroll, { passive: true });
    handleNavbarScroll();
  }

  // -------------------------------------------------------
  // 2. Mobile menu toggle
  // -------------------------------------------------------
  const hamburger = document.querySelector('.hamburger, .menu-toggle, .mobile-menu-btn');
  const mobileNav = document.querySelector('.mobile-nav');

  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', function () {
      const isOpen = mobileNav.classList.toggle('active');
      hamburger.classList.toggle('active');
      document.body.style.overflow = isOpen ? 'hidden' : '';
      hamburger.setAttribute('aria-expanded', String(isOpen));
    });

    mobileNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileNav.classList.remove('active');
        hamburger.classList.remove('active');
        document.body.style.overflow = '';
        hamburger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // -------------------------------------------------------
  // 3. Intersection Observer fade-in animations
  // -------------------------------------------------------
  const fadeEls = document.querySelectorAll('.fade-in');

  if (fadeEls.length && 'IntersectionObserver' in window) {
    const fadeObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          fadeObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -80px 0px'
    });

    fadeEls.forEach(function (el) {
      for (var i = 1; i <= 4; i++) {
        if (el.classList.contains('stagger-' + i)) {
          el.style.transitionDelay = (i * 0.15) + 's';
        }
      }
      fadeObserver.observe(el);
    });
  } else {
    fadeEls.forEach(function (el) {
      el.classList.add('visible');
    });
  }

  // -------------------------------------------------------
  // 4. Smooth scroll for anchor links
  // -------------------------------------------------------
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;

      var target = document.querySelector(targetId);
      if (!target) return;

      e.preventDefault();

      var navbarHeight = navbar ? navbar.offsetHeight : 0;
      var targetPosition = target.getBoundingClientRect().top + window.scrollY - navbarHeight;

      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });

      history.pushState(null, null, targetId);
    });
  });

  // -------------------------------------------------------
  // 5. FAQ accordion
  // -------------------------------------------------------
  document.querySelectorAll('.faq-question').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var parent = this.closest('.faq-item');
      var isActive = parent && parent.classList.contains('open');

      document.querySelectorAll('.faq-item').forEach(function (item) {
        item.classList.remove('open');
        var q = item.querySelector('.faq-question');
        if (q) q.setAttribute('aria-expanded', 'false');
      });

      if (!isActive && parent) {
        parent.classList.add('open');
        this.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // -------------------------------------------------------
  // 6. Portfolio lightbox
  // -------------------------------------------------------
  var portfolioImages = document.querySelectorAll(
    '.image-grid-item img, .portfolio-grid img, .gallery-grid img'
  );
  var currentLightboxIndex = 0;
  var lightboxOverlay = null;
  var lightboxImg = null;

  function buildLightbox() {
    lightboxOverlay = document.createElement('div');
    lightboxOverlay.className = 'lightbox';
    lightboxOverlay.setAttribute('role', 'dialog');
    lightboxOverlay.setAttribute('aria-label', 'Image lightbox');
    lightboxOverlay.innerHTML =
      '<div class="lightbox-close" role="button" aria-label="Close">&times;</div>' +
      '<div class="lightbox-nav lightbox-prev" role="button" aria-label="Previous">&#8249;</div>' +
      '<img alt="" />' +
      '<div class="lightbox-nav lightbox-next" role="button" aria-label="Next">&#8250;</div>';
    document.body.appendChild(lightboxOverlay);

    lightboxImg = lightboxOverlay.querySelector('img');

    lightboxOverlay.querySelector('.lightbox-close').addEventListener('click', closeLightbox);
    lightboxOverlay.querySelector('.lightbox-prev').addEventListener('click', function () {
      navigateLightbox(-1);
    });
    lightboxOverlay.querySelector('.lightbox-next').addEventListener('click', function () {
      navigateLightbox(1);
    });

    lightboxOverlay.addEventListener('click', function (e) {
      if (e.target === lightboxOverlay) closeLightbox();
    });
  }

  function openLightbox(index) {
    if (!lightboxOverlay) buildLightbox();
    currentLightboxIndex = index;
    var src = portfolioImages[index].getAttribute('data-full') || portfolioImages[index].src;
    var alt = portfolioImages[index].alt || '';
    lightboxImg.src = src;
    lightboxImg.alt = alt;
    lightboxOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (!lightboxOverlay) return;
    lightboxOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  function navigateLightbox(direction) {
    var total = portfolioImages.length;
    if (total <= 1) return;
    currentLightboxIndex = (currentLightboxIndex + direction + total) % total;
    var src = portfolioImages[currentLightboxIndex].getAttribute('data-full') || portfolioImages[currentLightboxIndex].src;
    lightboxImg.src = src;
    lightboxImg.alt = portfolioImages[currentLightboxIndex].alt || '';
  }

  portfolioImages.forEach(function (img, i) {
    img.style.cursor = 'pointer';
    img.addEventListener('click', function () {
      openLightbox(i);
    });
  });

  document.addEventListener('keydown', function (e) {
    if (!lightboxOverlay || !lightboxOverlay.classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') navigateLightbox(-1);
    if (e.key === 'ArrowRight') navigateLightbox(1);
  });

  // -------------------------------------------------------
  // 7. Portfolio filtering
  // -------------------------------------------------------
  var filterBtns = document.querySelectorAll('[data-filter]');
  var portfolioItems = document.querySelectorAll('[data-category]');

  if (filterBtns.length && portfolioItems.length) {
    filterBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var filter = this.getAttribute('data-filter');
        filterBtns.forEach(function (b) { b.classList.remove('active'); });
        this.classList.add('active');
        portfolioItems.forEach(function (item) {
          item.style.display = (filter === 'all' || item.getAttribute('data-category') === filter) ? '' : 'none';
        });
      });
    });
  }

  // -------------------------------------------------------
  // 8. Calendly integration helper
  // -------------------------------------------------------
  var calendlyWidget = document.querySelector('.calendly-inline-widget');
  var calendlyPopupBtns = document.querySelectorAll('.calendly-popup');

  if (calendlyWidget || calendlyPopupBtns.length) {
    if (!document.querySelector('script[src*="calendly.com"]')) {
      var script = document.createElement('script');
      script.src = 'https://assets.calendly.com/assets/external/widget.js';
      script.async = true;
      document.head.appendChild(script);
    }

    calendlyPopupBtns.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        var url = this.getAttribute('data-calendly-url') || this.href;
        if (window.Calendly) {
          window.Calendly.initPopupWidget({ url: url });
        }
      });
    });
  }

  // -------------------------------------------------------
  // 9. Current page nav highlight
  // -------------------------------------------------------
  var currentPath = window.location.pathname.replace(/\/$/, '') || '/';
  var currentPage = currentPath.split('/').pop() || 'index.html';

  document.querySelectorAll('.navbar a, .mobile-nav a').forEach(function (link) {
    var href = link.getAttribute('href');
    if (!href) return;
    var linkPage = href.replace(/^\.?\/?/, '').replace(/\/$/, '').split('/').pop() || 'index.html';
    if (linkPage === currentPage || (href === '/' && currentPage === 'index.html')) {
      link.classList.add('active');
    }
  });

});
