// Progressive enhancement only: the site is fully readable without this file.
(function () {
  var root = document.documentElement;
  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  root.classList.add('js');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
})();

// Language choice: remember it, and send a returning reader to their language.
(function () {
  var KEY = 'pluria-lang';
  var menu = document.querySelector('.lang-menu');
  if (!menu) return;
  var here = document.documentElement.lang;
  try {
    var pref = localStorage.getItem(KEY);
    if (pref && pref !== here && here === 'en' && !location.hash) {
      var a = menu.querySelector('a[data-lang="' + pref + '"]');
      if (a) { location.replace(a.getAttribute('href')); return; }
    }
  } catch (e) {}
  menu.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[data-lang]');
    if (!a) return;
    try { localStorage.setItem(KEY, a.getAttribute('data-lang')); } catch (err) {}
  });
  document.addEventListener('click', function (e) { if (!menu.contains(e.target)) menu.removeAttribute('open'); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') menu.removeAttribute('open'); });
})();
