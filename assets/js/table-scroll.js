/* Wraps every table in the article body in a scrollable region, so wide
   tables (compare tables, financial breakdowns, travel itineraries) never
   force the whole page to scroll horizontally on narrow viewports. */
(function () {
  'use strict';

  var article = document.querySelector('.article-inner');
  if (!article) return;

  var tables = article.querySelectorAll('table');
  if (!tables.length) return;

  var ariaLabel = window.__i18n?.[window.__siteLang]?.table_scroll_aria || 'Table with horizontal scroll';

  function updateEdges(wrapper) {
    var atStart = wrapper.scrollLeft <= 0;
    var atEnd = wrapper.scrollLeft + wrapper.clientWidth >= wrapper.scrollWidth - 1;
    wrapper.classList.toggle('can-scroll-left', !atStart);
    wrapper.classList.toggle('can-scroll-right', !atEnd);
  }

  function updateOverflow(wrapper) {
    var overflows = wrapper.scrollWidth > wrapper.clientWidth;
    wrapper.classList.toggle('overflows', overflows);
    // Only a tab stop when there's actually something to scroll to — an
    // always-present tabindex would add a pointless stop on every table.
    if (overflows) wrapper.setAttribute('tabindex', '0');
    else wrapper.removeAttribute('tabindex');
    updateEdges(wrapper);
  }

  tables.forEach(function (table) {
    if (table.closest('.table-scroll')) return;

    var wrapper = document.createElement('div');
    wrapper.className = 'table-scroll';
    wrapper.setAttribute('role', 'region');
    wrapper.setAttribute('aria-label', ariaLabel);
    wrapper.setAttribute('data-i18n-aria', 'table_scroll_aria');

    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);

    wrapper.addEventListener('scroll', function () { updateEdges(wrapper); }, { passive: true });

    if (window.ResizeObserver) {
      new ResizeObserver(function () { updateOverflow(wrapper); }).observe(wrapper);
    } else {
      updateOverflow(wrapper);
      window.addEventListener('resize', function () { updateOverflow(wrapper); }, { passive: true });
    }
  });
})();
