/* Adds a "#" affordance to every h2/h3 in the article body (ids assigned by
   heading-ids.js) that copies the section's absolute URL to the clipboard. */
(function () {
  'use strict';

  var article = document.querySelector('.article-inner');
  if (!article) return;

  var toast = document.getElementById('share-toast');
  var toastTimer = null;
  function showToast() {
    if (!toast) return;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.classList.remove('show'); }, 2000);
  }

  var ariaLabel = window.__i18n?.[window.__siteLang]?.copy_link_aria || 'Copy link to this section';

  article.querySelectorAll('h2, h3').forEach(function (heading) {
    if (!heading.id) return;

    var a = document.createElement('a');
    a.className = 'heading-anchor';
    a.href = '#' + heading.id;
    a.textContent = '#';
    a.setAttribute('aria-label', ariaLabel);
    a.setAttribute('data-i18n-aria', 'copy_link_aria');

    a.addEventListener('click', function () {
      if (!navigator.clipboard) return;
      var url = location.origin + location.pathname + '#' + heading.id;
      navigator.clipboard.writeText(url).then(showToast).catch(function () {});
    });

    heading.appendChild(a);
  });
})();
