(function () {
  'use strict';

  var STORAGE_KEY = 'theme';
  var root = document.documentElement;
  var btn = document.getElementById('theme-toggle');
  var systemMQ = window.matchMedia('(prefers-color-scheme: dark)');

  function currentTheme() {
    return root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
  }

  function syncGiscusTheme(theme) {
    var iframe = document.querySelector('iframe.giscus-frame');
    if (!iframe) return;
    iframe.contentWindow.postMessage({ giscus: { setConfig: { theme: theme } } }, 'https://giscus.app');
  }

  function updateIcon() {
    if (!btn) return;
    var icon = btn.querySelector('i');
    if (!icon) return;
    icon.className = currentTheme() === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }

  function applyTheme(theme) {
    root.setAttribute('data-theme', theme);
    updateIcon();
    syncGiscusTheme(theme);
  }

  updateIcon();

  if (btn) {
    btn.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem(STORAGE_KEY, next); } catch (e) {}
      applyTheme(next);
    });
  }

  /* Live-follow the OS setting as long as the user hasn't made an explicit choice. */
  systemMQ.addEventListener('change', function (e) {
    var stored;
    try { stored = localStorage.getItem(STORAGE_KEY); } catch (err) { stored = null; }
    if (stored === 'light' || stored === 'dark') return;
    applyTheme(e.matches ? 'dark' : 'light');
  });

  /* Giscus lazy-loads its iframe, so the first opportunity to reach it is
     whenever it posts anything back to the parent (e.g. its ready/resize
     message) — that's also when its own data-theme="light" default needs
     correcting to match the site's current theme. */
  window.addEventListener('message', function (event) {
    if (event.origin !== 'https://giscus.app') return;
    if (!(event.data && event.data.giscus)) return;
    syncGiscusTheme(currentTheme());
  });
})();
