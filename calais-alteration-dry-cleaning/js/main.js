/* ==========================================================================
   Calais Alteration & Dry Cleaning — main.js
   GSAP + ScrollTrigger for choreography, Lenis for smooth scroll.
   Everything gated behind gsap.matchMedia() and prefers-reduced-motion.
   ========================================================================== */

(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var isFinePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var isDesktop = window.matchMedia('(min-width: 1025px)').matches;

  document.getElementById('year').textContent = new Date().getFullYear();

  gsap.registerPlugin(ScrollTrigger);

  /* ------------------------------------------------------------------ */
  /* Lenis smooth scroll                                                 */
  /* ------------------------------------------------------------------ */

  var lenis = null;
  if (!reduceMotion && window.Lenis) {
    lenis = new window.Lenis({ duration: 1.15, smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
    gsap.ticker.lagSmoothing(0);
  }

  /* ------------------------------------------------------------------ */
  /* Load sequence — needle-and-thread stitch draw, once per session     */
  /* ------------------------------------------------------------------ */

  if (!reduceMotion) {
    gsap.set('.hero__eyebrow, .hero__sub, .hero__actions, .hero__proof', { opacity: 0, y: 24 });
  }

  (function loadSequence() {
    var loader = document.getElementById('loader');
    var alreadySeen = sessionStorage.getItem('calais-loaded');

    if (alreadySeen || reduceMotion) {
      loader.style.display = 'none';
      revealHero();
      return;
    }

    sessionStorage.setItem('calais-loaded', '1');
    document.body.style.overflow = 'hidden';

    var tl = gsap.timeline({
      onComplete: function () {
        loader.classList.add('is-done');
        loader.style.display = 'none';
        document.body.style.overflow = '';
      }
    });

    tl.set('.loader__mark', { opacity: 0, y: 16 })
      .to('.loader__mark', { opacity: 1, y: 0, duration: 0.4, ease: 'power2.out' })
      .to('.loader__stitch', { scaleX: 1, duration: 0.5, ease: 'power2.inOut' }, '+=0.05')
      .to('.loader__mark', { opacity: 1, duration: 0.15 })
      .to('.loader__door', { yPercent: -100, duration: 0.55, ease: 'expo.inOut' }, '+=0.05')
      .add(revealHero, '-=0.35');
  })();

  function revealHero() {
    if (reduceMotion) {
      gsap.set(['.hero__eyebrow', '.hero__sub', '.hero__actions', '.hero__proof', '.line'], { opacity: 1, y: 0 });
      return;
    }
    var tl = gsap.timeline({ defaults: { ease: 'expo.out' } });
    tl.to('.hero__eyebrow', { opacity: 1, duration: 0.6 }, 0.1)
      .to('.hero__headline .line', { y: '0%', duration: 1, stagger: 0.08 }, 0.15)
      .to('.hero__sub', { opacity: 1, y: 0, duration: 0.8 }, 0.55)
      .to('.hero__actions', { opacity: 1, y: 0, duration: 0.8 }, 0.65)
      .to('.hero__proof', { opacity: 1, y: 0, duration: 0.8 }, 0.75);
  }

  /* ------------------------------------------------------------------ */
  /* matchMedia — desktop-only heavy effects                             */
  /* ------------------------------------------------------------------ */

  var mm = gsap.matchMedia();

  mm.add('(min-width: 1025px) and (prefers-reduced-motion: no-preference)', function () {

    /* Hero parallax + scroll exit */
    gsap.to('.hero__img', {
      scale: 1.22,
      filter: 'saturate(0.5)',
      ease: 'none',
      scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true }
    });
    gsap.to('.hero__content', {
      yPercent: -18,
      opacity: 0.6,
      ease: 'none',
      scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true }
    });

    /* Trust strip entrance */
    gsap.from('.trust__item', {
      y: 40, opacity: 0, duration: 0.9, ease: 'power4.out', stagger: 0.08,
      scrollTrigger: { trigger: '.trust', start: 'top 80%' }
    });

    /* Difference columns */
    gsap.utils.toArray('.difference__col').forEach(function (col, i) {
      gsap.from(col, {
        y: 60, opacity: 0, duration: 1, ease: 'power4.out',
        delay: i * 0.1,
        scrollTrigger: { trigger: col, start: 'top 85%' }
      });
    });

    return function cleanup() {};
  });

  /* Split headings — word/line stagger with blur-to-sharp, all viewports */
  mm.add('(prefers-reduced-motion: no-preference)', function () {
    document.querySelectorAll('.split-heading').forEach(function (heading) {
      var text = heading.textContent;
      var words = text.split(' ');
      heading.innerHTML = words.map(function (w) {
        return '<span class="word" style="display:inline-block;overflow:hidden;"><span style="display:inline-block;">' + w + '&nbsp;</span></span>';
      }).join('');
      var inner = heading.querySelectorAll('.word > span');
      gsap.set(inner, { y: '110%', filter: 'blur(6px)' });
      gsap.to(inner, {
        y: '0%', filter: 'blur(0px)', duration: 0.95, ease: 'expo.out', stagger: 0.05,
        scrollTrigger: { trigger: heading, start: 'top 88%' }
      });
    });

    /* Image reveals — fabric-fold wipe */
    document.querySelectorAll('.reveal-mask').forEach(function (mask) {
      var img = mask.querySelector('img');
      gsap.set(mask, { clipPath: 'inset(100% 0 0 0)' });
      var tl = gsap.timeline({ scrollTrigger: { trigger: mask, start: 'top 85%' } });
      tl.to(mask, { clipPath: 'inset(0% 0 0 0)', duration: 1.2, ease: 'expo.out' })
        .to(img, { scale: 1, duration: 1.4, ease: 'power3.out' }, '-=1.05');
    });

    return function cleanup() {};
  });

  /* ------------------------------------------------------------------ */
  /* Pinned horizontal services scroller ("the rack")                    */
  /* ------------------------------------------------------------------ */

  mm.add('(min-width: 1025px)', function () {
    var track = document.getElementById('servicesTrack');
    var wrap = document.getElementById('servicesTrackWrap');
    var bar = document.getElementById('servicesProgressBar');
    if (!track || !wrap) return function () {};

    var scrollAmount = function () { return track.scrollWidth - wrap.clientWidth; };

    var st = ScrollTrigger.create({
      trigger: wrap,
      start: 'top top',
      end: function () { return '+=' + scrollAmount(); },
      pin: true,
      scrub: 0.6,
      invalidateOnRefresh: true,
      onUpdate: function (self) {
        gsap.set(track, { x: -scrollAmount() * self.progress });
        gsap.set(bar, { width: (self.progress * 100) + '%' });
      }
    });

    return function cleanup() { st.kill(); };
  });

  /* ------------------------------------------------------------------ */
  /* Process — scroll-linked stitched progress line                      */
  /* ------------------------------------------------------------------ */

  (function processLine() {
    var line = document.getElementById('processProgress');
    var list = document.querySelector('.process__list');
    if (!line || !list || reduceMotion) return;
    gsap.to(line, {
      height: '100%',
      ease: 'none',
      scrollTrigger: { trigger: list, start: 'top 60%', end: 'bottom 70%', scrub: true }
    });
  })();

  /* ------------------------------------------------------------------ */
  /* Count-up stats (trust strip)                                        */
  /* ------------------------------------------------------------------ */

  (function countUp() {
    var nodes = document.querySelectorAll('[data-count]');
    nodes.forEach(function (node) {
      var target = parseFloat(node.getAttribute('data-count'));
      var decimal = node.getAttribute('data-decimal');
      var full = decimal ? parseFloat(target + '.' + decimal) : target;
      var done = false;
      ScrollTrigger.create({
        trigger: node,
        start: 'top 90%',
        once: true,
        onEnter: function () {
          if (done || reduceMotion) { node.textContent = full; return; }
          done = true;
          var obj = { val: 0 };
          gsap.to(obj, {
            val: full,
            duration: 1.4,
            ease: 'power2.out',
            onUpdate: function () {
              node.textContent = decimal ? obj.val.toFixed(1) : Math.round(obj.val);
            }
          });
        }
      });
    });
  })();

  /* ------------------------------------------------------------------ */
  /* Nav — condense on scroll, hide on scroll down / show on scroll up   */
  /* ------------------------------------------------------------------ */

  (function navBehavior() {
    var header = document.getElementById('siteHeader');
    var lastY = window.scrollY;

    ScrollTrigger.create({
      start: 0,
      end: 'max',
      onUpdate: function (self) {
        var y = window.scrollY;
        header.classList.toggle('is-condensed', y > 80);
        if (y > lastY && y > 200) {
          header.classList.add('is-hidden');
        } else {
          header.classList.remove('is-hidden');
        }
        lastY = y;
      }
    });
  })();

  /* ------------------------------------------------------------------ */
  /* Mobile menu                                                         */
  /* ------------------------------------------------------------------ */

  (function mobileMenu() {
    var toggle = document.getElementById('menuToggle');
    var menu = document.getElementById('mobileMenu');
    if (!toggle || !menu) return;

    function close() {
      toggle.setAttribute('aria-expanded', 'false');
      menu.classList.remove('is-open');
      menu.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    toggle.addEventListener('click', function () {
      var isOpen = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(isOpen));
      menu.setAttribute('aria-hidden', String(!isOpen));
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', close);
    });
  })();

  /* ------------------------------------------------------------------ */
  /* Accordion — height-animated                                        */
  /* ------------------------------------------------------------------ */

  (function accordion() {
    var triggers = document.querySelectorAll('.accordion__trigger');
    triggers.forEach(function (trigger) {
      var panel = document.getElementById(trigger.getAttribute('aria-controls'));
      gsap.set(panel, { height: 0 });

      trigger.addEventListener('click', function () {
        var isOpen = trigger.getAttribute('aria-expanded') === 'true';

        triggers.forEach(function (other) {
          if (other !== trigger) {
            other.setAttribute('aria-expanded', 'false');
            var otherPanel = document.getElementById(other.getAttribute('aria-controls'));
            gsap.to(otherPanel, { height: 0, duration: 0.4, ease: 'power2.inOut' });
          }
        });

        trigger.setAttribute('aria-expanded', String(!isOpen));
        if (isOpen) {
          gsap.to(panel, { height: 0, duration: 0.4, ease: 'power2.inOut' });
        } else {
          gsap.set(panel, { height: 'auto' });
          gsap.from(panel, { height: 0, duration: 0.45, ease: 'power2.inOut' });
        }
      });
    });
  })();

  /* ------------------------------------------------------------------ */
  /* Magnetic CTAs — desktop / fine pointer only                         */
  /* ------------------------------------------------------------------ */

  if (isFinePointer && !reduceMotion) {
    document.querySelectorAll('[data-magnetic]').forEach(function (el) {
      var radius = 60;
      el.addEventListener('mousemove', function (e) {
        var rect = el.getBoundingClientRect();
        var x = e.clientX - (rect.left + rect.width / 2);
        var y = e.clientY - (rect.top + rect.height / 2);
        var dist = Math.sqrt(x * x + y * y);
        if (dist < radius + rect.width / 2) {
          gsap.to(el, { x: x * 0.25, y: y * 0.25, duration: 0.3, ease: 'power2.out' });
        }
      });
      el.addEventListener('mouseleave', function () {
        gsap.to(el, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.4)' });
      });
    });
  }

  /* ------------------------------------------------------------------ */
  /* Custom cursor                                                       */
  /* ------------------------------------------------------------------ */

  if (isFinePointer && isDesktop && !reduceMotion) {
    var cursor = document.getElementById('cursor');
    var dot = cursor.querySelector('.cursor__dot');
    var ring = cursor.querySelector('.cursor__ring');
    var label = cursor.querySelector('.cursor__label');

    var mouse = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
    var ringPos = { x: mouse.x, y: mouse.y };

    document.body.classList.add('hide-native-cursor');

    window.addEventListener('mousemove', function (e) {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
      gsap.set(dot, { x: mouse.x, y: mouse.y });
    });

    gsap.ticker.add(function () {
      ringPos.x += (mouse.x - ringPos.x) * 0.15;
      ringPos.y += (mouse.y - ringPos.y) * 0.15;
      gsap.set(ring, { x: ringPos.x, y: ringPos.y });
    });

    var labels = {
      call: 'Call',
      quote: 'Quote',
      home: 'Home'
    };

    document.querySelectorAll('[data-cursor]').forEach(function (el) {
      var key = el.getAttribute('data-cursor');
      el.addEventListener('mouseenter', function () {
        cursor.classList.add('is-active');
        label.textContent = labels[key] || '';
      });
      el.addEventListener('mouseleave', function () {
        cursor.classList.remove('is-active');
        label.textContent = '';
      });
    });

    document.querySelectorAll('#servicesTrackWrap').forEach(function (el) {
      el.addEventListener('mouseenter', function () {
        cursor.classList.add('is-active');
        label.textContent = 'Drag';
      });
      el.addEventListener('mouseleave', function () {
        cursor.classList.remove('is-active');
        label.textContent = '';
      });
    });
  } else {
    document.getElementById('cursor').style.display = 'none';
  }

  /* ------------------------------------------------------------------ */
  /* Contact form — inline validation, no navigation on success          */
  /* ------------------------------------------------------------------ */

  (function contactForm() {
    var form = document.getElementById('contactForm');
    var success = document.getElementById('contactSuccess');
    if (!form) return;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      /* CLIENT INPUT: wire this up to a real form endpoint (email service, CRM, etc.) */
      form.hidden = true;
      success.hidden = false;
      success.focus && success.focus();
    });
  })();

  /* Refresh ScrollTrigger after fonts / layout settle */
  window.addEventListener('load', function () {
    ScrollTrigger.refresh();
  });

})();
