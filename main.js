// ===============================================
// Dra. Angela Walkyria — Site
// Menu mobile · revelação ao rolar · contadores · cliques no WhatsApp
// ===============================================

(function () {
  'use strict';

  var reduzido = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Menu mobile
  var navToggle = document.querySelector('.nav-toggle');
  var mainNav = document.querySelector('.main-nav');
  if (navToggle && mainNav) {
    navToggle.addEventListener('click', function () {
      var isOpen = mainNav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    mainNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mainNav.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Rolagem suave para âncoras
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var href = this.getAttribute('href');
      if (href === '#') return;
      var target = document.querySelector(href);
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: reduzido ? 'auto' : 'smooth', block: 'start' }); }
    });
  });

  // Revelação ao rolar: cabeçalhos de seção entram sozinhos, grades entram em cascata
  if (!reduzido && 'IntersectionObserver' in window) {
    var solo = '.section-header, .sobre-text, .sobre-visual-wrap, .localizacao-text, .localizacao-map, .cta-content, .lp-grid-2 > *, .steps-list, .sintomas-cta, .depoimentos-cta';
    var grades = '.sintomas-grid, .servicos-grid, .depoimentos-grid, .trust-strip-grid, .benefits-grid, .diferenciais-grid, .plans-grid, .blog-grid';
    document.querySelectorAll(solo).forEach(function (el) { el.classList.add('reveal'); });
    document.querySelectorAll(grades).forEach(function (el) { el.classList.add('reveal-stagger'); });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('in'); io.unobserve(entry.target); }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.12 });
    document.querySelectorAll('.reveal, .reveal-stagger').forEach(function (el) { io.observe(el); });

    // Contadores da faixa de confiança
    var contadores = document.querySelectorAll('[data-count]');
    if (contadores.length) {
      var ioc = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target, alvo = parseFloat(el.getAttribute('data-count')), sufixo = el.getAttribute('data-suffix') || '';
          var decimais = (el.getAttribute('data-count').split('.')[1] || '').length;
          var inicio = null, dur = 1400;
          el.firstChild.nodeValue = (decimais ? '0,0' : '0') + sufixo;
          function passo(ts) {
            if (!inicio) inicio = ts;
            var p = Math.min((ts - inicio) / dur, 1); p = 1 - Math.pow(1 - p, 3);
            var v = alvo * p;
            el.firstChild.nodeValue = (decimais ? v.toFixed(decimais).replace('.', ',') : Math.round(v).toLocaleString('pt-BR')) + sufixo;
            if (p < 1) requestAnimationFrame(passo);
          }
          requestAnimationFrame(passo);
          ioc.unobserve(el);
        });
      }, { threshold: 0.5 });
      contadores.forEach(function (el) { ioc.observe(el); });
    }

    // Leve paralaxe na foto da capa
    var heroVisual = document.querySelector('.hero-visual-wrap');
    if (heroVisual && window.innerWidth > 900) {
      window.addEventListener('scroll', function () {
        var y = window.scrollY;
        if (y < 900) heroVisual.style.transform = 'translateY(' + (y * 0.08) + 'px)';
      }, { passive: true });
    }
  } else {
    document.querySelectorAll('.reveal, .reveal-stagger').forEach(function (el) { el.classList.add('in'); });
  }

  // Cliques no WhatsApp (GA4 / Pixel, quando configurados)
  document.querySelectorAll('a[href*="wa.me"]').forEach(function (link) {
    link.addEventListener('click', function () {
      if (typeof gtag === 'function') gtag('event', 'whatsapp_click', { event_category: 'conversion', event_label: window.location.pathname });
      if (typeof fbq === 'function') fbq('track', 'Contact');
    });
  });
})();
