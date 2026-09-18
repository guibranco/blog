(function () {
  'use strict';

  var STORAGE_KEY = 'theme';
  var root = document.documentElement;
  var btn = document.getElementById('theme-toggle');
  var systemMQ = window.matchMedia('(prefers-color-scheme: dark)');

  function currentTheme() {
    return root.dataset.theme === 'dark' ? 'dark' : 'light';
  }

  /* Giscus theme for each site theme: `transparent_dark` blends with the dark
     card background instead of painting GitHub's own dark blue box inside it.
     Keep in step with the injector in _layouts/post.html. */
  function giscusThemeFor(theme) {
    return theme === 'dark' ? 'transparent_dark' : 'light';
  }

  function syncGiscusTheme(theme) {
    var iframe = document.querySelector('iframe.giscus-frame');
    if (!iframe) return;
    iframe.contentWindow.postMessage({ giscus: { setConfig: { theme: giscusThemeFor(theme) } } }, 'https://giscus.app');
  }

  function updateIcon() {
    if (!btn) return;
    var isDark = currentTheme() === 'dark';
    var icon = btn.querySelector('i');
    if (icon) icon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
    btn.setAttribute('aria-pressed', String(isDark));
  }

  function applyTheme(theme) {
    root.dataset.theme = theme;
    updateIcon();
    syncGiscusTheme(theme);
  }

  updateIcon();
  syncGiscusTheme(currentTheme());

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
     message). The injector in post.html already starts it in the right theme;
     this re-sync covers a toggle that happened while the iframe was loading. */
  window.addEventListener('message', function (event) {
    if (event.origin !== 'https://giscus.app') return;
    if (!event.data?.giscus) return;
    syncGiscusTheme(currentTheme());
  });
})();
