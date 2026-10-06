// seizeapps.com — the site's only script. Nothing depends on it: content, links and the language switch
// all work without it. It remembers a language picked with the switch, flags the header at the top of the
// page, and (fine pointer, motion allowed) leans screenshots towards the pointer and lights cards under it.
(function () {
  var d = document;

  // A click on the switch is remembered and wins over the browser's languages (see LANG_PICK in gen_site.py).
  d.querySelectorAll('.lang a[hreflang]').forEach(function (a) {
    a.addEventListener('click', function () { try { localStorage.setItem('seize-lang', a.hreflang); } catch (e) {} });
  });

  var header = d.querySelector('.site-header');
  if (header) {
    var top = function () { header.classList.toggle('is-top', window.scrollY < 8); };
    addEventListener('scroll', top, { passive: true });
    top();
  }

  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !matchMedia('(hover: hover) and (pointer: fine)').matches) return;

  // One rAF per frame at most; `fn` gets the pointer as 0…1 inside the element, or null when it leaves.
  function follow(el, fn) {
    var raf = 0, e = null;
    el.addEventListener('pointermove', function (ev) {
      e = ev;
      if (!raf) raf = requestAnimationFrame(function () {
        raf = 0;
        var r = el.getBoundingClientRect();
        fn(el, (e.clientX - r.left) / r.width, (e.clientY - r.top) / r.height, r);
      });
    });
    el.addEventListener('pointerleave', function () { cancelAnimationFrame(raf); raf = 0; fn(el, null); });
  }

  // --px / --py in −1…1; the stylesheet turns them into a tilt or a parallax offset.
  d.querySelectorAll('[data-tilt]').forEach(function (el) {
    follow(el, function (el, x, y) {
      el.style.setProperty('--px', x === null ? 0 : (x * 2 - 1).toFixed(3));
      el.style.setProperty('--py', y === null ? 0 : (y * 2 - 1).toFixed(3));
    });
  });

  // The card's light sits under the pointer (moved with transform, so nothing repaints the card itself).
  d.querySelectorAll('.app-card').forEach(function (el) {
    follow(el, function (el, x, y, r) {
      if (x === null) return;
      el.style.setProperty('--mx', (x * r.width).toFixed(1) + 'px');
      el.style.setProperty('--my', (y * r.height).toFixed(1) + 'px');
    });
  });
})();
