  // ── Shared by every Calculator script and inlined into it at build time (ADR-0017) ──
  function bandTop(band) { return band.up_to == null ? Infinity : Number(band.up_to); }
  // Progressive charge: each slice of `amount` inside a band pays that band's rate.
  function progressive(amount, bands) {
    var total = 0, lower = 0;
    for (const band of bands) {
      var top = bandTop(band);
      if (amount > lower) total += (Math.min(amount, top) - lower) * Number(band.rate);
      if (amount <= top) break;
      lower = top;
    }
    return total;
  }
  // Bracket table (IRRF style): whole base × the band's rate, minus the band's deduction.
  function bracket(base, bands) {
    for (var i = 0; i < bands.length; i++) {
      if (base <= bandTop(bands[i]) || i === bands.length - 1) {
        return Math.max(0, base * Number(bands[i].rate) - Number(bands[i].deduct || 0));
      }
    }
    return 0;
  }
  // The value of `key` in `inp` at which `measure(inp)` reaches `target`, by bisection in [0, hi]; `measure` must grow with it.
  function solve(measure, inp, key, target, hi) {
    var lo = 0;
    for (var i = 0; i < 80; i++) {
      var mid = (lo + hi) / 2;
      if (measure({ ...inp, [key]: mid }) < target) lo = mid; else hi = mid;
    }
    return (lo + hi) / 2;
  }
  // ── DOM: builders, formatters and the wiring every Calculator repeats, used once it is on a page ──
  var LOCALES = { 'pt-BR': 'pt-BR', 'en': 'en-IE' };
  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text != null) node.textContent = text;
    return node;
  }
  function row(table, label, value, cls) {
    var tr = el('tr', cls);
    tr.appendChild(el('td', null, label));
    tr.appendChild(el('td', null, value));
    table.appendChild(tr);
  }
  function headline(card, label, value, sub) {
    card.appendChild(el('p', 'calc-headline-label', label));
    card.appendChild(el('p', 'calc-headline', value));
    if (sub) card.appendChild(el('p', 'calc-sub', sub));
  }
  // Number formatting in the Post language: money in a currency, percent, "1,25×" and a plain number.
  function formatters(lang) {
    var locale = LOCALES[lang] || lang, cache = {};
    function nf(key, options) {
      if (!cache[key]) cache[key] = new Intl.NumberFormat(locale, options);
      return cache[key];
    }
    return {
      money: function (value, currency, decimals) { return nf(currency + decimals, { style: 'currency', currency: currency, minimumFractionDigits: decimals, maximumFractionDigits: decimals }).format(value); },
      pct: function (value, digits) { var d = digits == null ? 1 : digits; return nf('pct' + d, { style: 'percent', maximumFractionDigits: d }).format(value); },
      times: function (value) { return nf('times', { minimumFractionDigits: 2, maximumFractionDigits: 2 }).format(value) + '×'; },
      plain: function (value) { return nf('plain', { maximumFractionDigits: 4 }).format(value); }
    };
  }
  // What every init needs from a Calculator's root: its data and labels, the form and output nodes, field readers, formatters.
  function setup(root) {
    root.dataset.calcInit = '';
    var data = JSON.parse(root.querySelector('[data-calc-data]').textContent);
    var lang = root.dataset.lang || 'pt-BR';
    var form = root.querySelector('.calc-form');
    return {
      data: data, labels: data.labels[lang] || data.labels['pt-BR'], form: form,
      results: root.querySelector('.calc-results'), error: root.querySelector('.calc-error'), fmt: formatters(lang),
      field: function (name) { return form.elements[name]; },
      num: function (name) { var v = Number.parseFloat(form.elements[name].value); return Number.isFinite(v) ? v : Number.NaN; }
    };
  }
  // Re-renders on every input, shows the form (hidden until now for the no-JavaScript fallback) and renders once.
  function start(ui, render) {
    ui.form.addEventListener('input', render);
    ui.form.addEventListener('submit', function (e) { e.preventDefault(); render(); });
    ui.form.hidden = false;
    render();
  }
