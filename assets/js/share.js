/* Share affordances on a post: the hero's share button and the share card
   (_includes/share.html). With the Web Share API the button opens the native
   sheet; otherwise the hero button copies the URL, and the card's copy button
   confirms in place (label swap + toast). The network links in the card are
   plain anchors and need nothing from here. */
(function () {
  'use strict';

  var toast = document.getElementById('share-toast');
  var toastTimer = null;

  // Resolved on every call, so a UI-language switch after load is honoured.
  function t(key, fallback) {
    var table = (window.__i18n && window.__i18n[window.__siteLang]) || {};
    return table[key] || fallback;
  }

  function showToast(text) {
    if (!toast) return;
    if (text) toast.textContent = text;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.classList.remove('show'); }, 2000);
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) return navigator.clipboard.writeText(text);
    // Old WebViews: select an off-screen textarea and use the legacy command.
    return new Promise(function (resolve, reject) {
      var area = document.createElement('textarea');
      area.value = text;
      area.setAttribute('readonly', '');
      area.style.position = 'fixed';
      area.style.opacity = '0';
      document.body.appendChild(area);
      area.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      document.body.removeChild(area);
      if (ok) resolve(); else reject(new Error('copy failed'));
    });
  }

  function confirmCopy(button) {
    var label = button.querySelector('[data-share-copy-label]');
    var original = label ? label.textContent : '';
    button.classList.add('is-copied');
    if (label) label.textContent = t('share_copied', 'Link copiado!');
    showToast(t('url_copied', toast ? toast.textContent : 'URL copiada!'));
    setTimeout(function () {
      button.classList.remove('is-copied');
      if (label) label.textContent = original;
    }, 2200);
  }

  for (const root of document.querySelectorAll('.post-share')) {
    var data = {
      title: root.dataset.shareTitle || document.title,
      text: root.dataset.shareText || document.title,
      url: root.dataset.shareUrl || location.href
    };
    var native = root.querySelector('[data-share-native]');
    if (native && navigator.share) {
      native.hidden = false;
      native.addEventListener('click', function () {
        navigator.share(data).catch(function () { /* dismissed or unsupported payload */ });
      });
    }
    var copyButton = root.querySelector('[data-share-copy]');
    if (copyButton) {
      copyButton.addEventListener('click', function () {
        copyText(data.url).then(function () { confirmCopy(copyButton); }, function () {
          showToast(t('share_copy_failed', 'Não deu para copiar — selecione o link abaixo'));
        });
      });
    }
  }

  var hero = document.getElementById('share-btn');
  if (hero) {
    hero.addEventListener('click', function () {
      var data = { title: document.title, url: location.href };
      if (navigator.share) {
        navigator.share(data).catch(function () { /* dismissed */ });
      } else {
        copyText(data.url).then(function () { showToast(); }, function () {
          showToast(t('share_copy_failed', 'Não deu para copiar — selecione o link abaixo'));
        });
      }
    });
  }
})();
