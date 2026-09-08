/* Mini map on travel posts (see _includes/post-map.html). Leaflet is only
   fetched once the map card is about to scroll into view, so pages without
   a map — and maps nobody scrolls to — pay nothing. */
(function () {
  'use strict';

  var el = document.getElementById('post-map');
  if (!el) return;

  var locations;
  try { locations = JSON.parse(el.dataset.locations || '[]'); } catch (e) { return; }
  locations = locations.filter(function (l) { return Number.isFinite(l.lat) && Number.isFinite(l.lng); });
  if (!locations.length) return;

  var LEAFLET = {
    css: { href: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css',
           integrity: 'sha512-h9FcoyWjHcOcmEVkxOfTLnmZFWIH0iZhZT1H2TbOq55xssQGEJHEaIm+PgoUaZbRvQTNTluNOEfb1ZRy6D3BOw==' },
    js:  { src: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js',
           integrity: 'sha512-puJW3E/qXDqYp9IfhAI54BJEaWIfloJ7JWs7OeD5i6ruC9JZL1gERT1wjtwXFlh7CjE7ZJ+/vcRZRkIYIb6p4g==' }
  };

  function loadLeaflet(done) {
    if (window.L) return done();
    var pending = 2;
    var settle = function () { if (--pending === 0) done(); };

    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = LEAFLET.css.href;
    link.integrity = LEAFLET.css.integrity;
    link.crossOrigin = 'anonymous';
    link.referrerPolicy = 'no-referrer';
    link.onload = settle;
    link.onerror = settle;
    document.head.appendChild(link);

    var script = document.createElement('script');
    script.src = LEAFLET.js.src;
    script.integrity = LEAFLET.js.integrity;
    script.crossOrigin = 'anonymous';
    script.referrerPolicy = 'no-referrer';
    script.onload = settle;
    document.head.appendChild(script);
  }

  function init() {
    if (!window.L) return;
    var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var map = L.map(el, {
      scrollWheelZoom: false,
      zoomAnimation: !reducedMotion, fadeAnimation: !reducedMotion, markerZoomAnimation: !reducedMotion
    });
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18,
      attribution: '© <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>'
    }).addTo(map);

    var markers = locations.map(function (loc, i) {
      var icon = L.divIcon({
        className: 'post-map-marker',
        html: '<span>' + (i + 1) + '</span>',
        iconSize: [28, 28], iconAnchor: [14, 14], popupAnchor: [0, -16]
      });
      var popup = document.createElement('div');
      popup.textContent = loc.label;
      var marker = L.marker([loc.lat, loc.lng], { icon: icon, title: loc.label, keyboard: true })
        .addTo(map)
        .bindPopup(popup);
      // divIcon has no `alt`; Leaflet already gives it role="button" + tabindex.
      var iconEl = marker.getElement();
      if (iconEl) iconEl.setAttribute('aria-label', (i + 1) + '. ' + loc.label);
      return marker;
    });

    if (markers.length === 1) {
      map.setView(markers[0].getLatLng(), 10);
    } else {
      map.fitBounds(L.featureGroup(markers).getBounds().pad(0.2));
    }

    document.querySelectorAll('.post-map-list-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var marker = markers[Number(btn.dataset.index)];
        if (!marker) return;
        map.panTo(marker.getLatLng(), { animate: !reducedMotion });
        marker.openPopup();
      });
    });
  }

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      if (!entries.some(function (e) { return e.isIntersecting; })) return;
      io.disconnect();
      loadLeaflet(init);
    }, { rootMargin: '200px 0px' });
    io.observe(el);
  } else {
    loadLeaflet(init);
  }
})();
