(function () {
  'use strict';

  var i18n = window.__i18n || {};
  var siteLang = window.__siteLang || 'pt-BR';
  var articleLang = window.__articleLang || siteLang;
  var STORAGE_KEY = 'preferred-lang';

  function getPreferred() {
    try { return localStorage.getItem(STORAGE_KEY) || articleLang; } catch (e) { return articleLang; }
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
      btn.classList.toggle('lang-btn--active', btn.getAttribute('data-lang') === lang);
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
