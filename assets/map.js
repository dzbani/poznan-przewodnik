/* Mapa atrakcji: Leaflet + własny podkład SVG (dane OpenStreetMap), filtry jak na stronie głównej. */
(function () {
  var el = document.getElementById("map");
  var dataEl = document.getElementById("map-data");
  if (!el || !dataEl || typeof L === "undefined") {
    if (el) el.innerHTML = '<p class="map-error">Nie udało się wczytać mapy. Odśwież stronę.</p>';
    return;
  }
  var data = JSON.parse(dataEl.textContent);
  var bounds = L.latLngBounds(data.bounds);
  var narrow = window.matchMedia("(max-width: 860px)").matches;

  var map = L.map(el, {
    minZoom: 11, maxZoom: 16, zoomSnap: 0.5, zoomDelta: 0.5,
    maxBounds: bounds.pad(0.05), maxBoundsViscosity: 0.8,
    attributionControl: true, zoomControl: true
  });
  map.attributionControl.setPrefix(false);
  map.attributionControl.addAttribution('&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">autorzy OpenStreetMap</a>');
  L.imageOverlay("img/mapa-podklad.svg", bounds, { interactive: false, className: "map-base" }).addTo(map);
  map.setView([52.4084, 16.9342], narrow ? 13 : 13.5);

  var plural = function (n) {
    var t = n % 10, h = n % 100;
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
    var photo = it.img ? '<img src="img/' + esc(it.img) + '.jpg" alt="" loading="lazy">' : "";
    marker.bindPopup(
      '<div class="pop">' + photo +
      '<p class="pop-cat" style="--dot:' + cat.col + '"><span class="dot"></span>' + esc(cat.n) + "</p>" +
      "<h3>" + esc(it.n) + "</h3>" +
      '<p class="pop-badge' + (it.x ? " is-closed" : "") + '">' + esc(it.b) + "</p>" +
      "<p>" + esc(it.d) + "</p>" +
      '<a class="pop-more" href="atrakcje/' + esc(it.s) + '.html">Szczegóły, godziny i ceny</a>' +
      (it.ap ? '<p class="pop-note">Położenie przybliżone.</p>' : "") +
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
    count.textContent = n === data.items.length ? "Wszystkie: " + plural(n) : "Na mapie: " + plural(n) + " z " + data.items.length;
  }
  function bind(selector, key, attr) {
    var btns = document.querySelectorAll(selector);
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        btns.forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
        state[key] = b.getAttribute(attr);
        apply();
      });
    });
  }
  bind(".map-finder .tab", "cat", "data-filter");
  bind(".map-finder .qf", "quick", "data-quick");
  apply();

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
