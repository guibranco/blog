/* Assigns stable, unique, accent-free ids to every h2/h3 in the article body.
   Runs before toc.js and anchor-links.js — both just read heading.id afterwards. */
(function () {
  'use strict';

  function slugify(text) {
    var slug = text
      .normalize('NFD').replace(/[̀-ͯ]/g, '') // strip accents
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
    return slug || 'section';
  }

  function uniqueId(base, used) {
    var id = base;
    var n = 2;
    while (used.has(id)) { id = base + '-' + n; n++; }
    used.add(id);
    return id;
  }

  var article = document.querySelector('.article-inner');
  if (!article) return;

  var usedIds = new Set(
    Array.prototype.map.call(document.querySelectorAll('[id]'), function (el) { return el.id; })
  );

  article.querySelectorAll('h2, h3').forEach(function (heading) {
    if (!heading.id) heading.id = uniqueId(slugify(heading.textContent.trim()), usedIds);
    else usedIds.add(heading.id);
  });
})();
