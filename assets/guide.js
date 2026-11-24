// User Guide enhancements: search, a collapsed contents list on small screens, and a
// highlight for the current section. Everything works without this file except search.
(function () {
  'use strict';

  var input = document.getElementById('g-q');
  var box = document.getElementById('g-results');
  var lang = document.documentElement.lang || 'en';
  var INDEX = '/assets/guide-index' + (lang === 'en' ? '' : '.' + lang) + '.json';
  var index = null, loading = null;

  function fold(s) {
    return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[’']/g, '');
  }
  function esc(s) {
    return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }
  function load() {
    if (index) return Promise.resolve(index);
    if (!loading) {
      loading = fetch(INDEX).then(function (r) { return r.json(); }).then(function (rows) {
        rows.forEach(function (r) { r._t = fold(r.c + ' ' + r.s); r._x = fold(r.x); });
        index = rows;
        return rows;
      });
    }
    return loading;
  }

  function search(q) {
    var terms = fold(q).split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    var hits = [];
    index.forEach(function (r) {
      var score = 0;
      for (var i = 0; i < terms.length; i++) {
        var t = terms[i], inTitle = r._t.indexOf(t) >= 0, inText = r._x.indexOf(t) >= 0;
        if (!inTitle && !inText) return;
        score += (inTitle ? 10 : 0) + (inText ? 2 : 0);
        if (r._t.indexOf(t) === 0) score += 3;
      }
      hits.push({ r: r, score: score });
    });
    hits.sort(function (a, b) { return b.score - a.score; });
    return hits.slice(0, 14).map(function (h) { return h.r; });
  }

  function snippet(r, terms) {
    var text = r.x, low = r._x, pos = -1;
    for (var i = 0; i < terms.length && pos < 0; i++) pos = low.indexOf(terms[i]);
    var start = Math.max(0, pos - 60), out = text.slice(start, start + 170);
    if (start > 0) out = '…' + out;
    if (start + 170 < text.length) out += '…';
    out = esc(out);
    terms.forEach(function (t) {
      if (t.length < 2) return;
      out = out.replace(new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>');
    });
    return out;
  }

  function render(q) {
    var terms = fold(q).split(/\s+/).filter(Boolean);
    document.body.classList.toggle('g-searching', terms.length > 0);
    if (!terms.length) { box.hidden = true; box.innerHTML = ''; return; }
    var rows = search(q);
    box.hidden = false;
    if (!rows.length) { box.innerHTML = '<p class="g-none">' + esc(box.getAttribute('data-none') || 'No matches for {q}.').replace('{q}', esc(q)) + '</p>'; return; }
    box.innerHTML = '<ul>' + rows.map(function (r) {
      var title = r.s ? esc(r.c) + ' <span aria-hidden="true">›</span> ' + esc(r.s) : esc(r.c);
      return '<li><a href="' + r.u + '"><span class="rt">' + title + '</span><span class="rs">' + snippet(r, terms) + '</span></a></li>';
    }).join('') + '</ul>';
  }

  if (input && box) {
    var timer;
    input.addEventListener('focus', load);
    input.addEventListener('input', function () {
      clearTimeout(timer);
      timer = setTimeout(function () { load().then(function () { render(input.value); }); }, 80);
    });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { input.value = ''; render(''); }
      if (e.key === 'ArrowDown') { var a = box.querySelector('a'); if (a) { a.focus(); e.preventDefault(); } }
    });
    box.addEventListener('keydown', function (e) {
      var cur = document.activeElement;
      if (e.key === 'ArrowDown' && cur.closest('li') && cur.closest('li').nextElementSibling) { cur.closest('li').nextElementSibling.querySelector('a').focus(); e.preventDefault(); }
      if (e.key === 'ArrowUp') {
        var prev = cur.closest('li') && cur.closest('li').previousElementSibling;
        (prev ? prev.querySelector('a') : input).focus(); e.preventDefault();
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === '/' && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName) && !e.metaKey && !e.ctrlKey) {
        e.preventDefault(); input.focus(); input.select();
      }
    });
  }

  // Small screens: start with the contents list closed so the chapter comes first.
  var nav = document.querySelector('.g-nav');
  if (nav && window.matchMedia('(max-width: 899px)').matches) nav.removeAttribute('open');

  // Keep the current chapter visible in the long contents list.
  var cur = document.querySelector('.g-nav a[aria-current="page"]');
  if (cur && cur.scrollIntoView && window.matchMedia('(min-width: 900px)').matches) {
    var side = document.querySelector('.g-side');
    if (side) side.scrollTop = Math.max(0, cur.offsetTop - side.clientHeight / 3);
  }

  // "On this page": mark the section being read.
  var links = document.querySelectorAll('.g-toc a');
  if (links.length && 'IntersectionObserver' in window) {
    var map = {};
    links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          links.forEach(function (a) { a.classList.remove('on'); });
          var a = map[e.target.id]; if (a) a.classList.add('on');
        }
      });
    }, { rootMargin: '-15% 0px -75% 0px' });
    Object.keys(map).forEach(function (id) { var h = document.getElementById(id); if (h) io.observe(h); });
  }
})();
