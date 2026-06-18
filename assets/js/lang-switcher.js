(function () {
  'use strict';

  var i18n = window.__i18n || {};
  var siteLang = window.__siteLang || 'pt-BR';
  var STORAGE_KEY = 'preferred-lang';

  function detectBrowserLang() {
    var available = Object.keys(i18n);
    var candidates = (navigator.languages && navigator.languages.length)
      ? Array.from(navigator.languages)
      : [navigator.language || ''];

    for (var i = 0; i < candidates.length; i++) {
      var lang = candidates[i].toLowerCase();

      // Exact match (e.g. "pt-BR" → "pt-BR")
      for (var j = 0; j < available.length; j++) {
        if (available[j].toLowerCase() === lang) return available[j];
      }

      // Prefix match (e.g. "pt" → "pt-BR", "en-US" → "en")
      var prefix = lang.split('-')[0];
      for (var j = 0; j < available.length; j++) {
        if (available[j].toLowerCase().split('-')[0] === prefix) return available[j];
      }
    }

    return siteLang;
  }

  function getPreferred() {
    try { return localStorage.getItem(STORAGE_KEY) || detectBrowserLang(); } catch (e) { return detectBrowserLang(); }
  }

  function setPreferred(lang) {
    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) {}
  }

  function applyLang(lang) {
    var t = i18n[lang];
    if (!t) return;

    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var v = t[el.getAttribute('data-i18n')];
      if (v !== undefined) el.textContent = v;
    });

    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) {
      var v = t[el.getAttribute('data-i18n-aria')];
      if (v !== undefined) el.setAttribute('aria-label', v);
    });

    document.querySelectorAll('[data-i18n-title]').forEach(function (el) {
      var v = t[el.getAttribute('data-i18n-title')];
      if (v !== undefined) el.setAttribute('title', v);
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(function (el) {
      var v = t[el.getAttribute('data-i18n-placeholder')];
      if (v !== undefined) el.setAttribute('placeholder', v);
    });

    document.querySelectorAll('.lang-btn').forEach(function (btn) {
      var isActive = btn.getAttribute('data-lang') === lang;
      btn.classList.toggle('lang-btn--active', isActive);
      btn.setAttribute('aria-pressed', isActive);
    });
  }

  function init() {
    applyLang(getPreferred());

    document.querySelectorAll('.lang-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var lang = btn.getAttribute('data-lang');
        setPreferred(lang);
        applyLang(lang);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
