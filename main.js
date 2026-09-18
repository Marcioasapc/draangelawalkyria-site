// ===============================================
// Dra. Angela Walkyria — Site
// Mobile menu + smooth interactions
// ===============================================

(function() {
  'use strict';

  // Mobile menu toggle
  const navToggle = document.querySelector('.nav-toggle');
  const mainNav = document.querySelector('.main-nav');

  if (navToggle && mainNav) {
    navToggle.addEventListener('click', function() {
      const isOpen = mainNav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close mobile menu when clicking a link
    mainNav.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        mainNav.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Track WhatsApp clicks (basic analytics)
  document.querySelectorAll('a[href*="wa.me"]').forEach(function(link) {
    link.addEventListener('click', function() {
      if (typeof gtag === 'function') {
        gtag('event', 'whatsapp_click', {
          event_category: 'conversion',
          event_label: window.location.pathname
        });
      }
      if (typeof fbq === 'function') {
        fbq('track', 'Contact');
      }
    });
  });

})();
