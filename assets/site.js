// Wspólny skrypt wszystkich stron przewodnika.

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

// 2. Wyszukiwarka i filtry na stronie głównej. Bez JavaScriptu widać wszystkie atrakcje.
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
      // Wyszukiwarka w nagłówku przenosi do listy wyników po Enterze.
      if (inp.id === 'q-hero') {
        inp.addEventListener('keydown', function (e) {
          if (e.key !== 'Enter') return;
          e.preventDefault();
          list.scrollIntoView({ behavior: 'smooth', block: 'start' });
          document.getElementById('q').focus({ preventScroll: true });
        });
      }
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
    fromHash();
    window.addEventListener('hashchange', fromHash);
  }

  // 3. Logo „Poznań” na stronie głównej: powrót na samą górę i reset filtrów.
  //    Na podstronach link prowadzi normalnie do strony głównej.
  var logo = document.querySelector('.logo');
  if (logo && list) {
    logo.addEventListener('click', function (e) {
      e.preventDefault();
      reset();
      if (location.hash) history.replaceState(null, '', location.pathname + location.search);
      window.scrollTo(0, 0);
    });
  }

  // 4. Płynne przewijanie dla linków wewnątrz tej samej strony (#sekcja).
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

// 5. Przycisk „do góry” pojawia się po przewinięciu o dwa ekrany.
(function () {
  var btn = document.querySelector('.to-top');
  if (!btn) return;
  function toggle() { btn.hidden = window.scrollY < window.innerHeight * 2; }
  window.addEventListener('scroll', toggle, { passive: true });
  toggle();
  btn.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
})();

// 6. Wydarzenia: zakończone edycje są oznaczane według dzisiejszej daty w przeglądarce,
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
