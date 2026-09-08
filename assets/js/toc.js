(function () {
  'use strict';

  var MIN_HEADINGS = 3;
  var DESKTOP_QUERY = '(min-width: 900px)';

  /* Heading text minus any already-appended heading-anchor "#" link
     (see anchor-links.js) — read defensively in case it ran first. */
  function headingLabel(heading) {
    var clone = heading.cloneNode(true);
    var anchor = clone.querySelector('.heading-anchor');
    if (anchor) anchor.remove();
    return clone.textContent.trim();
  }

  function init() {
    var toc = document.getElementById('post-toc');
    var article = document.querySelector('.article-inner');
    if (!toc || !article) return;

    var headings = Array.prototype.slice.call(article.querySelectorAll('h2, h3'));
    if (headings.length < MIN_HEADINGS) return;

    var list = document.getElementById('post-toc-list');
    var links = [];
    var lastH2Li = null;

    headings.forEach(function (heading) {
      if (!heading.id) return;

      var a = document.createElement('a');
      a.href = '#' + heading.id;
      a.textContent = headingLabel(heading);

      var li = document.createElement('li');
      li.appendChild(a);

      if (heading.tagName === 'H3' && lastH2Li) {
        var sub = lastH2Li.querySelector('.post-toc-sublist');
        if (!sub) {
          sub = document.createElement('ol');
          sub.className = 'post-toc-sublist';
          lastH2Li.appendChild(sub);
        }
        sub.appendChild(li);
      } else {
        list.appendChild(li);
        if (heading.tagName === 'H2') lastH2Li = li;
      }

      links.push(a);
    });

    toc.hidden = false;

    /* ── Desktop: always expanded. Mobile: collapsed by default, user-toggleable. ── */
    var details = document.getElementById('post-toc-details');
    var desktopMQ = window.matchMedia(DESKTOP_QUERY);
    var syncOpen = function (mq) {
      if (mq.matches) details.setAttribute('open', '');
      else details.removeAttribute('open');
    };
    syncOpen(desktopMQ);
    desktopMQ.addEventListener('change', syncOpen);

    /* ── Smooth scroll + hash update, respecting prefers-reduced-motion. ── */
    var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    list.addEventListener('click', function (e) {
      var a = e.target.closest('a');
      if (!a) return;
      var target = document.getElementById(a.hash.slice(1));
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: reducedMotion ? 'auto' : 'smooth', block: 'start' });
      history.pushState(null, '', a.hash);
    });

    /* ── Scroll-spy: highlight the section currently under a thin band near the top. ── */
    var activeLink = null;
    var setActive = function (id) {
      if (activeLink) activeLink.classList.remove('active');
      activeLink = id ? links.find(function (a) { return a.hash.slice(1) === id; }) : null;
      if (activeLink) activeLink.classList.add('active');
    };

    var observer = new IntersectionObserver(function (entries) {
      var visible = entries.filter(function (entry) { return entry.isIntersecting; });
      if (visible.length) setActive(visible[visible.length - 1].target.id);
    }, { rootMargin: '-10% 0px -75% 0px', threshold: 0 });

    headings.forEach(function (heading) { observer.observe(heading); });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
