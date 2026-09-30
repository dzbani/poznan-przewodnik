// Wspólny skrypt wszystkich stron przewodnika.

// 0. Menu „☰” na wąskich ekranach: otwieranie, zamykanie klawiszem Esc, kliknięciem obok i po wyborze pozycji.
(function () {
  var bar = document.querySelector('.topbar');
  var btn = bar && bar.querySelector('.menu-btn');
  if (!btn) return;
  function set(open) {
    bar.classList.toggle('menu-open', open);
    btn.setAttribute('aria-expanded', String(open));
  }
  btn.addEventListener('click', function () { set(!bar.classList.contains('menu-open')); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && bar.classList.contains('menu-open')) { set(false); btn.focus(); }
  });
  document.addEventListener('click', function (e) {
    if (bar.classList.contains('menu-open') && !bar.contains(e.target)) set(false);
  });
  bar.querySelectorAll('nav a').forEach(function (a) { a.addEventListener('click', function () { set(false); }); });
})();

// 1. Każda strona otwiera się od góry. Przeglądarka (i okno podglądu Artifactu)
//    potrafi przywrócić pozycję przewinięcia z poprzedniej strony, przez co podstrona
//    otwierała się na samym dole. Wyjątek: link z kotwicą (#sekcja) przewija do sekcji.
(function () {
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';

  var userScrolled = false;
  ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function (ev) {
    window.addEventListener(ev, function () { userScrolled = true; }, { passive: true, once: true });
  });

  function place() {
    if (userScrolled) return;
    var id = decodeURIComponent(location.hash.slice(1));
    var target = id && document.getElementById(id);
    if (target) target.scrollIntoView({ block: 'start' });
    else window.scrollTo(0, 0);
  }

  place();
  document.addEventListener('DOMContentLoaded', place);
  window.addEventListener('load', place);
  window.addEventListener('pageshow', place);
  // Podgląd Artifactu może przywrócić pozycję chwilę po wczytaniu, więc powtarzamy krótko.
  [50, 200, 500, 1000].forEach(function (ms) { setTimeout(place, ms); });
})();

// 2. Wyszukiwarka i filtry na stronie atrakcje.html. Bez JavaScriptu widać wszystkie atrakcje.
//    Strona główna przekazuje hasło i filtr w adresie: atrakcje.html?q=zoo, ?f=free, #kat-muzea.
(function () {
  var list = document.getElementById('atrakcje');
  var tabs = document.querySelectorAll('.tab[data-filter]');
  var quick = document.querySelectorAll('.qf[data-quick]');
  var inputs = document.querySelectorAll('[data-search-input]');
  var state = { cat: 'all', quick: 'all', q: '' };

  // Porównujemy bez polskich znaków i wielkości liter: „zoo” = „Zoo”, „kosciol” = „kościół”.
  function norm(s) {
    return s.toLowerCase().replace(/ł/g, 'l').normalize('NFD').replace(/[̀-ͯ]/g, '');
  }

  var cards = list ? Array.prototype.slice.call(list.querySelectorAll('.card')) : [];
  cards.forEach(function (c) { c._words = norm(c.dataset.words || ''); });
  var groups = list ? list.querySelectorAll('.cat-group') : [];
  var result = list && list.querySelector('.result');
  var empty = list && list.querySelector('.empty');

  function apply() {
    var words = norm(state.q).split(/\s+/).filter(Boolean);
    var shown = 0;
    groups.forEach(function (g) {
      var inCat = state.cat === 'all' || g.dataset.cat === state.cat;
      var n = 0;
      g.querySelectorAll('.card').forEach(function (c) {
        var ok = inCat &&
          (state.quick === 'all' || (' ' + c.dataset.tags + ' ').indexOf(' ' + state.quick + ' ') >= 0) &&
          words.every(function (w) { return c._words.indexOf(w) >= 0; });
        c.hidden = !ok;
        if (ok) n++;
      });
      g.hidden = n === 0;
      shown += n;
    });
    tabs.forEach(function (t) { t.setAttribute('aria-pressed', String(t.dataset.filter === state.cat)); });
    quick.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.quick === state.quick)); });
    var filtered = state.cat !== 'all' || state.quick !== 'all' || words.length;
    if (result) result.textContent = filtered ? 'Znaleziono: ' + shown + ' z ' + cards.length : '';
    if (empty) empty.hidden = shown > 0;
  }

  function show(cat) { state.cat = cat; apply(); }

  function reset() {
    state = { cat: 'all', quick: 'all', q: '' };
    inputs.forEach(function (i) { i.value = ''; });
    apply();
  }

  if (list) {
    tabs.forEach(function (t) { t.addEventListener('click', function () { show(t.dataset.filter); }); });
    quick.forEach(function (b) {
      b.addEventListener('click', function () { state.quick = b.dataset.quick; apply(); });
    });
    inputs.forEach(function (inp) {
      inp.addEventListener('input', function () {
        state.q = inp.value;
        inputs.forEach(function (o) { if (o !== inp) o.value = inp.value; });
        apply();
      });
    });
    var resetBtn = list.querySelector('[data-reset]');
    if (resetBtn) resetBtn.addEventListener('click', reset);

    // Link z podstrony (#kat-zabytki) od razu pokazuje tę kategorię.
    var fromHash = function () {
      var m = location.hash.match(/^#kat-([a-z]+)$/);
      if (m && list.querySelector('.cat-group[data-cat="' + m[1] + '"]')) {
        state.quick = 'all'; state.q = ''; inputs.forEach(function (i) { i.value = ''; });
        show(m[1]);
        document.getElementById('kat-' + m[1]).scrollIntoView({ block: 'start' });
      }
    };
    // Hasło i szybki filtr ze strony głównej: atrakcje.html?q=koziołki, atrakcje.html?f=kids.
    var params = new URLSearchParams(location.search);
    var q = (params.get('q') || '').trim();
    var f = params.get('f');
    if (f && list.querySelector('.qf[data-quick="' + f + '"]')) state.quick = f;
    if (q) {
      state.q = q;
      inputs.forEach(function (i) { i.value = q; });
    }
    if (q || f) apply();
    fromHash();
    window.addEventListener('hashchange', fromHash);
  }

  // 3. Płynne przewijanie dla linków wewnątrz tej samej strony (#sekcja).
  //    Kafelek kategorii (#kat-x) najpierw włącza filtr, żeby grupa była widoczna.
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href').slice(1);
      var m = id.match(/^kat-([a-z]+)$/);
      if (m && list) {
        state.quick = 'all'; state.q = ''; inputs.forEach(function (i) { i.value = ''; });
        show(m[1]);
      }
      var target = id && document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      history.replaceState(null, '', '#' + id);
    });
  });
})();

// 4. Przycisk „do góry” pojawia się po przewinięciu o dwa ekrany.
(function () {
  var btn = document.querySelector('.to-top');
  if (!btn) return;
  function toggle() { btn.hidden = window.scrollY < window.innerHeight * 2; }
  window.addEventListener('scroll', toggle, { passive: true });
  toggle();
  btn.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
})();

// 5. Wydarzenia: zakończone edycje są oznaczane według dzisiejszej daty w przeglądarce,
//    a na stronie głównej widać tylko najbliższe (data-upcoming) jeszcze trwające wydarzenia.
(function () {
  var d = new Date();
  var today = d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
  document.querySelectorAll('.cal-event[data-end]').forEach(function (ev) {
    if (ev.dataset.end >= today) return;
    ev.classList.add('is-past');
    var badge = ev.querySelector('.event-past');
    if (badge) badge.hidden = false;
  });
  // Kalendarz zaczyna się od bieżącego miesiąca; wcześniejsze miesiące trafiają na koniec (przyszły rok).
  var cal = document.querySelector('.cal');
  if (cal) {
    var month = d.getMonth() + 1, toc = document.querySelector('.toc');
    var secs = Array.prototype.slice.call(cal.querySelectorAll('.cal-month'));
    var tail = cal.querySelector('.cal > p:last-child');
    secs.filter(function (s) { return parseInt(s.id.slice(1), 10) < month; }).forEach(function (s) {
      cal.insertBefore(s, tail);
      var link = toc && toc.querySelector('a[href="#' + s.id + '"]');
      if (link) toc.appendChild(link);
    });
  }
  var box = document.querySelector('.events[data-upcoming]');
  if (!box) return;
  var max = parseInt(box.dataset.upcoming, 10), shown = 0;
  box.querySelectorAll('.event[data-end]').forEach(function (ev) {
    var on = ev.dataset.end >= today && shown < max;
    ev.hidden = !on;
    if (on) shown++;
  });
  var empty = box.parentNode.querySelector('.events-empty');
  if (empty) empty.hidden = shown > 0;
})();

// 6. Zgoda na statystyki (Google Analytics 4). Skrypt Google ładuje się WYŁĄCZNIE po „Akceptuję”.
//    Wybór zapamiętujemy w przeglądarce (to niezbędne, by nie pytać na każdej stronie).
//    „Ustawienia cookies” w stopce pozwala zmienić decyzję; cofnięcie zgody usuwa cookies GA.
(function () {
  var box = document.querySelector('.consent');
  if (!box) return;
  var id = box.dataset.ga, KEY = 'op-zgoda-statystyki', loaded = false;
  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function save(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function loadGA() {
    if (loaded || !id) return;
    loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    gtag('consent', 'default', { analytics_storage: 'granted', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' });
    gtag('js', new Date());
    gtag('config', id);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
    document.head.appendChild(s);
  }
  function dropCookies() {
    var host = location.hostname, parts = host.split('.'), domains = ['', host, '.' + host];
    if (parts.length > 2) domains.push('.' + parts.slice(-2).join('.'));
    document.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (!/^_ga/.test(name)) return;
      domains.forEach(function (d) {
        document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + (d ? '; domain=' + d : '');
      });
    });
  }
  function decide(v) {
    save(v);
    box.hidden = true;
    if (v === 'granted') loadGA();
    else {
      if (window.gtag) gtag('consent', 'update', { analytics_storage: 'denied' });
      dropCookies();
    }
  }
  box.querySelectorAll('[data-consent]').forEach(function (b) {
    b.addEventListener('click', function () { decide(b.dataset.consent); });
  });
  document.querySelectorAll('[data-consent-open]').forEach(function (b) {
    b.addEventListener('click', function () { box.hidden = false; box.querySelector('[data-consent]').focus(); });
  });
  var v = read();
  if (v === 'granted') loadGA();
  else if (v !== 'denied') box.hidden = false;
})();
