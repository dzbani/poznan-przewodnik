/* Mapa atrakcji: Leaflet + kafelki OpenStreetMap, filtry jak na stronie głównej. */
(function () {
  var el = document.getElementById("map");
  var dataEl = document.getElementById("map-data");
  if (!el || !dataEl || typeof L === "undefined") {
    if (el) el.innerHTML = '<p class="map-error">' + (document.documentElement.lang === "en" ? "The map could not be loaded. Please refresh the page." : "Nie udało się wczytać mapy. Odśwież stronę.") + '</p>';
    return;
  }
  var data = JSON.parse(dataEl.textContent);
  var narrow = window.matchMedia("(max-width: 860px)").matches;

  var map = L.map(el, {
    minZoom: 8, maxZoom: 18, zoomSnap: 0.5, zoomDelta: 0.5,
    attributionControl: true, zoomControl: true
  });
  map.attributionControl.setPrefix(false);
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">autorzy OpenStreetMap</a>'
  }).addTo(map);
  var CENTER = [52.4084, 16.9342];
  map.setView(CENTER, narrow ? 13 : 13.5);

  var EN = document.documentElement.lang === "en";
  var T = function (pl, en) { return EN ? en : pl; };
  var ROOT = data.root || "";            // ścieżka do korzenia serwisu (img/)
  var DETAIL = data.detail || "atrakcje/";  // katalog stron atrakcji
  var plural = function (n) {
    var t = n % 10, h = n % 100;
    if (EN) return n === 1 ? "1 attraction" : n + " attractions";
    if (n === 1) return "1 atrakcja";
    if (t >= 2 && t <= 4 && (h < 12 || h > 14)) return n + " atrakcje";
    return n + " atrakcji";
  };
  var esc = function (s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; });
  };

  var list = document.getElementById("map-items");
  var count = document.getElementById("map-count");
  var byslug = {};

  data.items.forEach(function (it) {
    var cat = data.cats[it.c];
    var marker = L.circleMarker([it.lat, it.lon], {
      radius: 7, weight: 2, color: "#ffffff", fillColor: it.x ? "#8C7B6D" : cat.col, fillOpacity: 1,
      dashArray: it.ap ? "3 3" : null
    });
    var photo = it.img ? '<img src="' + ROOT + 'img/' + esc(it.img) + '.jpg" alt="" loading="lazy">' : "";
    marker.bindPopup(
      '<div class="pop">' + photo +
      '<p class="pop-cat" style="--dot:' + cat.col + '"><span class="dot"></span>' + esc(cat.n) + "</p>" +
      "<h3>" + esc(it.n) + "</h3>" +
      '<p class="pop-badge' + (it.x ? " is-closed" : "") + '">' + esc(it.b) + "</p>" +
      "<p>" + esc(it.d) + "</p>" +
      '<a class="pop-more" href="' + DETAIL + esc(it.s) + '">' + T("Szczegóły, godziny i ceny", "Details, hours and prices") + '</a>' +
      '<p class="pop-nav"><a href="' + esc(it.gm) + '" target="_blank" rel="noopener">' + T("Otwórz w Google Maps", "Open in Google Maps") + '</a>' +
      '<a href="' + esc(it.rt) + '" target="_blank" rel="noopener">' + (it.rf ? T("Trasa z dworca Poznań Główny", "Directions from Poznań Główny station") : T("Trasa komunikacją", "Directions by public transport")) + "</a></p>" +
      (it.ap ? '<p class="pop-note">' + T("Położenie przybliżone.", "Approximate location.") + '</p>' : "") +
      "</div>", { maxWidth: 260, minWidth: 220, autoPanPadding: [20, 20] });
    marker.bindTooltip(esc(it.n), { direction: "top", offset: [0, -6] });

    var li = document.createElement("li");
    li.innerHTML = '<button type="button"><span class="dot" style="--dot:' + (it.x ? "#8C7B6D" : cat.col) + '"></span>' +
      '<span class="nm">' + esc(it.n) + "</span></button>";
    li.querySelector("button").addEventListener("click", function () { focusItem(it.s); });
    list.appendChild(li);

    byslug[it.s] = { it: it, marker: marker, li: li };
  });

  function focusItem(slug) {
    var e = byslug[slug];
    if (!e) return;
    if (!map.hasLayer(e.marker)) e.marker.addTo(map);
    map.flyTo(e.marker.getLatLng(), Math.max(map.getZoom(), 15), { duration: 0.6 });
    map.once("moveend", function () { e.marker.openPopup(); });
    if (narrow) el.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  var state = { cat: "all", quick: "all" };
  function apply() {
    var n = 0;
    Object.keys(byslug).forEach(function (s) {
      var e = byslug[s], it = e.it;
      var ok = (state.cat === "all" || it.c === state.cat) && (state.quick === "all" || it.t.indexOf(state.quick) !== -1);
      if (ok) { n++; if (!map.hasLayer(e.marker)) e.marker.addTo(map); }
      else if (map.hasLayer(e.marker)) map.removeLayer(e.marker);
      e.li.hidden = !ok;
    });
    count.textContent = n === data.items.length ? T("Wszystkie: ", "All: ") + plural(n) : T("Na mapie: ", "On the map: ") + plural(n) + T(" z ", " of ") + data.items.length;
    return n;
  }
  // Wycieczki za miasto leżą do 90 km od centrum: po wybraniu tej kategorii mapa obejmuje wszystkie punkty.
  function fitVisible() {
    var pts = Object.keys(byslug).filter(function (s) { return map.hasLayer(byslug[s].marker); })
      .map(function (s) { return byslug[s].marker.getLatLng(); });
    if (pts.length) map.fitBounds(L.latLngBounds(pts), { padding: [30, 30], maxZoom: 15 });
  }
  function bind(selector, key, attr) {
    var btns = document.querySelectorAll(selector);
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        btns.forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
        state[key] = b.getAttribute(attr);
        apply();
        if (key === "cat" && state.cat === "wycieczki") fitVisible();
        else if (key === "cat" && state.cat === "all") map.setView(CENTER, narrow ? 13 : 13.5);
      });
    });
  }
  bind(".map-finder .tab", "cat", "data-filter");
  bind(".map-finder .qf:not(.locate-btn)", "quick", "data-quick");
  apply();

  var userMarker = null;
  var userLat = null, userLon = null;

  // Funkcja do liczenia odległości między dwoma punktami (metoda Haversine, wynik w km).
  function distance_km(lat1, lon1, lat2, lon2) {
    var R = 6371;
    var toRad = Math.PI / 180;
    var dLat = (lat2 - lat1) * toRad;
    var dLon = (lon2 - lon1) * toRad;
    var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(lat1 * toRad) * Math.cos(lat2 * toRad) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return R * c;
  }

  // Funkcja do formatowania odległości.
  function format_distance(km) {
    if (km < 1) return Math.round(km * 1000) + " m";
    return (km < 10 ? km.toFixed(1) : Math.round(km)) + " km";
  }

  // Funkcja do sortowania listy po odległości od użytkownika.
  function sort_by_distance() {
    if (userLat === null || userLon === null) return;
    var items_arr = [];
    Object.keys(byslug).forEach(function (s) {
      var e = byslug[s], it = e.it;
      var dist = distance_km(userLat, userLon, it.lat, it.lon);
      items_arr.push({ slug: s, dist: dist, elem: e });
    });
    items_arr.sort(function (a, b) { return a.dist - b.dist; });

    // Wyczyść listę i dodaj elementy w nowej kolejności.
    list.innerHTML = "";
    items_arr.forEach(function (item) {
      var e = item.elem, it = e.it;
      var li = document.createElement("li");
      var dist_text = ' <span class="map-dist">' + format_distance(item.dist) + '</span>';
      li.innerHTML = '<button type="button"><span class="dot" style="--dot:' + (it.x ? "#8C7B6D" : data.cats[it.c].col) + '"></span>' +
        '<span class="nm">' + esc(it.n) + "</span>" + (userLat !== null ? dist_text : "") + "</button>";
      li.querySelector("button").addEventListener("click", function () { focusItem(it.s); });
      list.appendChild(li);
    });
  }

  var locateBtn = document.getElementById("locate-btn");
  if (locateBtn) {
    locateBtn.addEventListener("click", function () {
      if (!navigator.geolocation) {
        alert(T("Geolokalizacja nie jest dostępna w Twojej przeglądarce.", "Geolocation is not available in your browser."));
        return;
      }
      locateBtn.disabled = true;
      locateBtn.textContent = T("⏳ Szukam...", "⏳ Searching...");
      navigator.geolocation.getCurrentPosition(
        function (pos) {
          userLat = pos.coords.latitude;
          userLon = pos.coords.longitude;
          if (userMarker) map.removeLayer(userMarker);
          userMarker = L.circleMarker([userLat, userLon], {
            radius: 8, weight: 3, color: "#0066CC", fillColor: "#3399FF", fillOpacity: 0.7
          }).addTo(map);
          userMarker.bindPopup("<p><strong>" + T("Jesteś tutaj", "You are here") + "</strong></p>", { maxWidth: 150 });
          userMarker.bindTooltip(T("Twoja lokalizacja", "Your location"), { direction: "top", offset: [0, -10] });
          map.flyTo([userLat, userLon], 15, { duration: 0.6 });
          // Sortuj listę po odległości od użytkownika.
          sort_by_distance();
          locateBtn.disabled = false;
          locateBtn.innerHTML = '<span class="locate-ico" aria-hidden="true">📍</span>' + T("Gdzie jestem", "Where am I");
        },
        function (err) {
          var msg = err.code === 1 ? T("Odmówiłeś dostępu do lokalizacji.", "You denied access to your location.") : T("Nie mogę ustalić Twojej lokalizacji.", "Your location could not be determined.");
          alert(msg);
          locateBtn.disabled = false;
          locateBtn.innerHTML = '<span class="locate-ico" aria-hidden="true">📍</span>' + T("Gdzie jestem", "Where am I");
        },
        { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 }
      );
    });
  }

  function fromHash() {
    var s = decodeURIComponent(location.hash.slice(1));
    if (byslug[s]) {
      map.setView(byslug[s].marker.getLatLng(), 15);
      setTimeout(function () { byslug[s].marker.openPopup(); }, 50);
    }
  }
  fromHash();
  window.addEventListener("hashchange", fromHash);
})();
