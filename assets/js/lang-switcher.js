(function () {
  'use strict';

  var i18n = window.__i18n || {};
  var siteLang = window.__siteLang || 'pt-BR';
  var STORAGE_KEY = 'preferred-lang';

  // slug -> country entry, from _data/countries.yml (used for [data-country] cells)
  var countries = (window.__countries || []).reduce(function (acc, c) {
    if (c?.slug) acc[c.slug] = c;
    return acc;
  }, {});

  function detectBrowserLang() {
    var available = Object.keys(i18n);
    var candidates = navigator.languages?.length
      ? Array.from(navigator.languages)
      : [navigator.language || ''];

    for (var candidate of candidates) {
      var lang = candidate.toLowerCase();

      // Exact match (e.g. "pt-BR" → "pt-BR")
      for (let code of available) {
        if (code.toLowerCase() === lang) return code;
      }

      // Prefix match (e.g. "pt" → "pt-BR", "en-US" → "en")
      var prefix = lang.split('-')[0];
      for (let code of available) {
        if (code.toLowerCase().split('-')[0] === prefix) return code;
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

  function formatDate(isoDate, format, monthNames) {
    var parts = isoDate.split('-');
    var month = Number.parseInt(parts[1], 10);
    return format.replace('%Y', parts[0]).replace('%B', monthNames[month - 1]).replace('%d', parts[2]);
  }

  function applyLang(lang) {
    var t = i18n[lang];
    if (!t) return;

    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var v = t[el.dataset.i18n];
      if (v !== undefined) el.textContent = v;
    });

    // Same as [data-i18n] but the string may contain inline markup (<em>, <br>).
    // Values come from the trusted site i18n data file, never user input.
    document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
      var v = t[el.dataset.i18nHtml];
      if (v !== undefined) el.innerHTML = v;
    });

    var subtag = lang.split('-')[0].toLowerCase();

    // Bilingual content blocks (see _includes/i18n-block.html): show the span
    // for the active language, hide the other. Server markup ships the English
    // span [hidden], so with JS off the pt-BR text is what shows.
    var showEn = subtag === 'en';
    document.querySelectorAll('.i18n-pt').forEach(function (el) { el.hidden = showEn; });
    document.querySelectorAll('.i18n-en').forEach(function (el) { el.hidden = !showEn; });

    // Same bilingual data, but for an `alt` attribute (can't hold a hidden
    // span). journey.html ships both data-alt-pt/-en; pick the active one.
    document.querySelectorAll('[data-alt-pt]').forEach(function (el) {
      el.alt = (showEn && el.dataset.altEn) ? el.dataset.altEn : el.dataset.altPt;
    });

    var nameKey = subtag === 'pt' ? 'name' : 'name_' + subtag; // countries.yml: name (pt-BR) + name_en
    document.querySelectorAll('[data-country]').forEach(function (el) {
      var entry = countries[el.dataset.country];
      if (entry?.[nameKey]) el.textContent = entry[nameKey];
    });

    document.querySelectorAll('[data-date]').forEach(function (el) {
      if (t.date_format && t.month_names) el.textContent = formatDate(el.dataset.date, t.date_format, t.month_names);
    });

    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) {
      var v = t[el.dataset.i18nAria];
      if (v !== undefined) el.setAttribute('aria-label', v);
    });

    document.querySelectorAll('[data-i18n-title]').forEach(function (el) {
      var v = t[el.dataset.i18nTitle];
      if (v !== undefined) el.setAttribute('title', v);
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(function (el) {
      var v = t[el.dataset.i18nPlaceholder];
      if (v !== undefined) el.setAttribute('placeholder', v);
    });

    document.querySelectorAll('.lang-btn').forEach(function (btn) {
      var isActive = btn.dataset.lang === lang;
      btn.classList.toggle('lang-btn--active', isActive);
      btn.setAttribute('aria-pressed', isActive);
    });
  }

  function init() {
    applyLang(getPreferred());

    document.querySelectorAll('.lang-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var lang = btn.dataset.lang;
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
