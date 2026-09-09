/* /viagens/ — country + year filters that keep the Leaflet map, the
   "articles by country" table and the URL (?country=&year=) in sync.
   Data model comes from window.__travelPosts (emitted by Liquid). */
(function () {
  'use strict';

  var posts = window.__travelPosts || [];
  var mapEl = document.getElementById('map');
  var countrySelect = document.getElementById('travel-filter-country');
  var yearSelect = document.getElementById('travel-filter-year');
  var tbody = document.querySelector('.travels-table tbody');
  if (!posts.length || !mapEl || !countrySelect || !yearSelect || !tbody || !window.L) return;

  var i18n = window.__i18n || {};
  var countries = (window.__countries || []).reduce(function (acc, c) {
    if (c && c.slug) acc[c.slug] = c;
    return acc;
  }, {});

  var lang = window.__siteLang || 'pt-BR';
  function t() { return i18n[lang] || i18n[window.__siteLang] || {}; }

  // countries.yml: `name` is the English (canonical) label, `name_<subtag>`
  // the translation for the active UI language (e.g. name_pt).
  function countryName(key) {
    var entry = countries[key];
    if (!entry) return key;
    var subtag = lang.split('-')[0].toLowerCase();
    return entry['name_' + subtag] || entry.name;
  }

  // Mirrors the site's date_short ("%d/%m/%Y" / "%m/%d/%Y") on an ISO date.
  function formatShort(iso) {
    var parts = iso.split('-');
    return (t().date_short || '%d/%m/%Y')
      .replace('%Y', parts[0]).replace('%m', parts[1]).replace('%d', parts[2]);
  }

  /* ── Map ── */
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var map = L.map('map', {
    zoomAnimation: !reducedMotion, fadeAnimation: !reducedMotion, markerZoomAnimation: !reducedMotion
  });
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>'
  }).addTo(map);

  function buildPopup(post, loc) {
    var popup = document.createElement('div');
    var strong = document.createElement('strong');
    var link = document.createElement('a');
    link.href = post.url;
    link.textContent = post.title;
    strong.appendChild(link);
    popup.appendChild(strong);
    popup.appendChild(document.createElement('br'));
    var small = document.createElement('small');
    small.style.fontFamily = 'monospace';
    small.textContent = loc.label + ' · ' + formatShort(post.date);
    popup.appendChild(small);
    return popup;
  }

  var markers = [];
  posts.forEach(function (post) {
    post.locations.forEach(function (loc) {
      if (!Number.isFinite(loc.lat) || !Number.isFinite(loc.lng)) return;
      var m = L.marker([loc.lat, loc.lng], { alt: loc.label, title: loc.label });
      m.bindPopup(buildPopup(post, loc));
      markers.push({ post: post, marker: m });
    });
  });
  var group = L.featureGroup().addTo(map);
  var allMarkers = markers.map(function (entry) { return entry.marker; });
  var emptyNotice = document.getElementById('travel-map-empty');

  /* ── Filter state ── */
  var state = { country: '', year: '' };

  function matches(post) {
    return (!state.country || post.countries.indexOf(state.country) !== -1) &&
           (!state.year || post.year === state.year);
  }

  function fitTo(layers) {
    if (layers.length === 1) {
      map.setView(layers[0].getLatLng(), 8);
    } else if (layers.length > 1) {
      map.fitBounds(L.featureGroup(layers).getBounds().pad(0.15));
    }
  }

  function renderMap() {
    group.clearLayers();
    markers.forEach(function (entry) {
      if (matches(entry.post)) group.addLayer(entry.marker);
    });
    var visible = group.getLayers();
    // No match: fall back to the all-posts view and say so on the map itself,
    // rather than leaving an empty map parked on whatever region was last shown.
    fitTo(visible.length ? visible : allMarkers);
    if (emptyNotice) emptyNotice.hidden = visible.length > 0;
  }

  /* ── Table — same markup Liquid renders on first paint ── */
  function renderTable() {
    var groups = {};
    posts.filter(matches).forEach(function (post) {
      post.countries.forEach(function (key) {
        (groups[key] = groups[key] || []).push(post);
      });
    });

    // Liquid sorts by the canonical English name (code-point order); keep that order.
    var keys = Object.keys(groups).sort(function (a, b) {
      var na = countries[a] ? countries[a].name : a;
      var nb = countries[b] ? countries[b].name : b;
      return na < nb ? -1 : na > nb ? 1 : 0;
    });

    tbody.textContent = '';

    if (!keys.length) {
      var tr = document.createElement('tr');
      var td = document.createElement('td');
      td.colSpan = 3;
      td.className = 'travels-table-empty';
      td.setAttribute('data-i18n', 'travels_no_results');
      td.textContent = t().travels_no_results || '';
      tr.appendChild(td);
      tbody.appendChild(tr);
      return;
    }

    keys.forEach(function (key) {
      var rows = groups[key].slice().sort(function (a, b) { return b.ts - a.ts; });
      rows.forEach(function (post, i) {
        var tr = document.createElement('tr');

        if (i === 0) {
          var tdCountry = document.createElement('td');
          tdCountry.className = 'travels-table-country';
          tdCountry.rowSpan = rows.length;
          if (countries[key]) tdCountry.setAttribute('data-country', key);
          tdCountry.textContent = countryName(key);
          tr.appendChild(tdCountry);
        }

        var tdTitle = document.createElement('td');
        var a = document.createElement('a');
        a.href = post.url;
        a.textContent = post.title;
        tdTitle.appendChild(a);
        tr.appendChild(tdTitle);

        var tdDate = document.createElement('td');
        tdDate.className = 'travels-table-date';
        tdDate.appendChild(document.createTextNode(formatShort(post.date)));
        if (post.updated) {
          tdDate.appendChild(document.createTextNode(' · '));
          var span = document.createElement('span');
          span.setAttribute('data-i18n', 'updated_on');
          span.textContent = t().updated_on || '';
          tdDate.appendChild(span);
          tdDate.appendChild(document.createTextNode(' ' + formatShort(post.updated)));
        }
        tr.appendChild(tdDate);

        tbody.appendChild(tr);
      });
    });
  }

  /* ── URL ── */
  function hasOption(select, value) {
    return Array.prototype.some.call(select.options, function (o) { return o.value === value; });
  }

  function readUrl() {
    var params = new URLSearchParams(location.search);
    var c = params.get('country') || '';
    var y = params.get('year') || '';
    state.country = hasOption(countrySelect, c) ? c : '';
    state.year = hasOption(yearSelect, y) ? y : '';
    countrySelect.value = state.country;
    yearSelect.value = state.year;
  }

  function writeUrl() {
    var url = new URL(location.href);
    if (state.country) url.searchParams.set('country', state.country); else url.searchParams.delete('country');
    if (state.year) url.searchParams.set('year', state.year); else url.searchParams.delete('year');
    history.replaceState(null, '', url);
  }

  function apply() {
    renderMap();
    renderTable();
  }

  countrySelect.addEventListener('change', function () { state.country = countrySelect.value; apply(); writeUrl(); });
  yearSelect.addEventListener('change', function () { state.year = yearSelect.value; apply(); writeUrl(); });
  document.getElementById('travel-filters').addEventListener('submit', function (e) { e.preventDefault(); });

  // Rows rebuilt here carry data-country / data-i18n so lang-switcher.js keeps
  // localizing them; dates need a rebuild, so re-render on a language change.
  document.querySelectorAll('.lang-btn').forEach(function (btn) {
    btn.addEventListener('click', function () { lang = btn.dataset.lang || lang; renderTable(); });
  });
  var active = document.querySelector('.lang-btn--active');
  if (active && active.dataset.lang) lang = active.dataset.lang;

  readUrl();
  renderMap();
  if (state.country || state.year) renderTable();
})();
