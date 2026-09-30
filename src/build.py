# -*- coding: utf-8 -*-
"""Generator stron przewodnika. Uruchom: python src/build.py
Tworzy: index.html, informacje.html, plany.html, kalendarz.html, teatry.html, o-poznaniu.html, zdjecia.html, atrakcje/<slug>.html"""
import datetime
import json
import os
import shutil
from html import escape
from urllib.parse import quote_plus

from site_data import ATTRACTIONS, CATEGORIES, CHECKED
from data_guide import (TOP10, KIDS, INDOOR_EXTRA, PLANS, HISTORY, LEGENDS, DIALECT, CUISINE,
                        CLIMATE, TOILETS)
from data_events import CALENDAR, CAL_CHECKED
from data_theatres import THEATRES, THEATRE_SOURCES, THEATRES_CHECKED

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDITS = {c["slug"]: c for c in json.load(open(os.path.join(ROOT, "img", "credits.json"), encoding="utf-8"))}
CAT = {k: (name, desc) for k, name, desc in CATEGORIES}
BY_SLUG = {a["slug"]: a for a in ATTRACTIONS}
CAT_WORDS = {4: "czterech", 5: "pięciu", 6: "sześciu", 7: "siedmiu", 8: "ośmiu"}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500'
         '&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">')

ICON = {
    "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "ticket": '<path d="M3 8a2 2 0 0 0 0 4v4h18v-4a2 2 0 0 0 0-4V4H3z"/><path d="M13 4v16" stroke-dasharray="2 2"/>',
    "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 12l5 2v4a2 2 0 0 1-2 2A15 15 0 0 1 3 5a2 2 0 0 1 2-2"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "route": '<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h7a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h7"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "back": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "up": '<path d="M12 19V5M6 11l6-6 6 6"/>',
    "alert": '<path d="M12 3 2 20h20z"/><path d="M12 10v4M12 17h.01"/>',
}


MONTHS = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień",
          "Wrzesień", "Październik", "Listopad", "Grudzień"]
MONTHS_GEN = ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca", "sierpnia",
              "września", "października", "listopada", "grudnia"]
UPCOMING_MAX = 4


def fmt_range(start, end):
    """'2026-06-21', '2026-06-28' -> '21–28 czerwca 2026'."""
    a, b = datetime.date.fromisoformat(start), datetime.date.fromisoformat(end)
    if a == b:
        return f"{a.day} {MONTHS_GEN[a.month - 1]} {a.year}"
    if (a.year, a.month) == (b.year, b.month):
        return f"{a.day}–{b.day} {MONTHS_GEN[a.month - 1]} {a.year}"
    if a.year == b.year:
        return f"{a.day} {MONTHS_GEN[a.month - 1]} – {b.day} {MONTHS_GEN[b.month - 1]} {a.year}"
    return f"{a.day} {MONTHS_GEN[a.month - 1]} {a.year} – {b.day} {MONTHS_GEN[b.month - 1]} {b.year}"


def icon(name, cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>'


def count_attractions(n):
    """Polska odmiana: 1 sprawdzona atrakcja, 2–4 sprawdzone atrakcje, 5+ sprawdzonych atrakcji."""
    if n == 1:
        return "1 sprawdzona atrakcja"
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return f"{n} sprawdzone atrakcje"
    return f"{n} sprawdzonych atrakcji"


def maps_url(a):
    return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(f'{a["name"]}, {a["address"]}')


def route_url(a):
    # Wycieczki za miasto: trasa z dworca Poznań Główny; w mieście: z bieżącej lokalizacji.
    origin = "&origin=" + quote_plus("Poznań Główny") if a.get("trip") else ""
    return ("https://www.google.com/maps/dir/?api=1&travelmode=transit" + origin + "&destination="
            + quote_plus(f'{a["name"]}, {a["address"]}'))


CENTER = (52.4084, 16.9342)  # Stary Rynek


def distance_km(lat, lon):
    """Odległość w linii prostej od Starego Rynku, zaokrąglona do 5 km."""
    import math
    p1, p2 = math.radians(CENTER[0]), math.radians(lat)
    dp, dl = p2 - p1, math.radians(lon - CENTER[1])
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return max(5, round(2 * 6371 * math.asin(math.sqrt(h)) / 5) * 5)


def media_html(a, prefix, lazy=False):
    """Zdjęcie atrakcji albo plansza z nazwą, gdy na Commons nie ma zdjęcia z podanym autorem."""
    if not a.get("img"):
        return f'<div class="no-photo" role="img" aria-label="Brak zdjęcia: {escape(a["name"])}"><span>{escape(a["name"])}</span></div>'
    extra = ' loading="lazy" decoding="async"' if lazy else ""
    return f'<img src="{prefix}img/{a["img"]}.jpg" alt="{escape(a["img_alt"])}"{extra}>'


def credit_badge(slug, prefix=""):
    """Dyskretna ikonka „i” w rogu zdjęcia: autor i licencja w dymku, klik prowadzi do strony autorów."""
    c = CREDITS[slug]
    txt = escape(f'Zdjęcie: {c["artist"]}, {c["license"]}')
    return (f'<a class="photo-credit" href="{prefix}zdjecia.html#foto-{slug}" data-credit="{txt}" '
            f'aria-label="{txt}. Pokaż źródło">i</a>')


def asset_v(name):
    """Znacznik wersji pliku (skrót zawartości), żeby przeglądarki nie trzymały starej kopii po aktualizacji."""
    import hashlib
    return hashlib.md5(open(os.path.join(ROOT, "src", name), "rb").read()).hexdigest()[:8]


def page(title, body, prefix="", desc="", active="", head="", scripts=""):
    def nav_link(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<li><a href="{prefix}{href}"{cur}>{label}</a></li>'
    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
{FONTS}
{head}<link rel="stylesheet" href="{prefix}assets/style.css?v={asset_v("style.css")}">
</head>
<body>
<a class="skip" href="#tresc">Przejdź do treści</a>
<header class="topbar">
  <div class="topbar-in">
    <a class="logo" href="{prefix}index.html">Poznań<span>przewodnik dla odwiedzających</span></a>
    <nav aria-label="Nawigacja główna">
      <ul>
        {nav_link("index.html#atrakcje", "Atrakcje", "atrakcje")}
        {nav_link("mapa.html", "Mapa", "mapa")}
        {nav_link("plany.html", "Plany zwiedzania", "plany")}
        {nav_link("kalendarz.html", "Wydarzenia", "kalendarz")}
        {nav_link("informacje.html", "Praktycznie", "info")}
        {nav_link("o-poznaniu.html", "O Poznaniu", "o")}
      </ul>
    </nav>
  </div>
</header>
<main id="tresc">
{body}
</main>
<footer class="footer">
  <div class="wrap footer-in">
    <div>
      <p class="footer-logo">Poznań</p>
      <p class="muted">Nieoficjalny przewodnik, niezwiązany z Urzędem Miasta Poznania.
      Datę sprawdzenia godzin i cen podajemy na stronie każdej atrakcji. Przed wizytą potwierdź je na stronie obiektu.</p>
    </div>
    <ul class="footer-links">
      <li><a href="{prefix}index.html#atrakcje">Atrakcje</a></li>
      <li><a href="{prefix}mapa.html">Mapa atrakcji</a></li>
      <li><a href="{prefix}plany.html">Plany zwiedzania</a></li>
      <li><a href="{prefix}informacje.html">Informacje praktyczne</a></li>
      <li><a href="{prefix}o-poznaniu.html">O Poznaniu: historia, legendy, gwara</a></li>
      <li><a href="{prefix}kalendarz.html">Kalendarz wydarzeń</a></li>
      <li><a href="{prefix}teatry.html">Teatry i koncerty</a></li>
      <li><a href="{prefix}zdjecia.html">Autorzy zdjęć</a></li>
      <li><a href="https://visitpoznan.pl/" target="_blank" rel="noopener">Visit Poznań (oficjalny portal)</a></li>
    </ul>
  </div>
</footer>
<button type="button" class="to-top" aria-label="Wróć na górę strony" hidden>{icon("up")}</button>
{scripts}<script src="{prefix}assets/site.js?v={asset_v("site.js")}"></script>
</body>
</html>
"""


def is_closed(a):
    return bool(a["status"]) and a["status"][0] == "closed"


def is_free(a):
    """Wstęp bez biletu: pierwsza pozycja cennika to „bezpłatnie/bezpłatne”."""
    return not is_closed(a) and a["tickets"][0][1].startswith("bezpłatn")


def is_indoor(a):
    return not is_closed(a) and (a["cat"] in ("muzea", "koscioly") or a["slug"] in INDOOR_EXTRA)


def tags(a):
    t = []
    if is_free(a):
        t.append("free")
    if a["slug"] in KIDS:
        t.append("kids")
    if is_indoor(a):
        t.append("indoor")
    return t


TAG_LABEL = {"free": "Bezpłatne", "kids": "Dla dzieci", "indoor": "Pod dachem"}


def card(a, prefix="", num=None):
    cat_name = CAT[a["cat"]][0]
    badge_cls = "badge badge-closed" if is_closed(a) else "badge"
    words = " ".join([a["name"], a["short"], cat_name, a["address"], a["badge"]])
    num_html = f'<span class="num" aria-hidden="true">{num}</span>' if num else ""
    chips = "".join(f'<span class="chip chip-{t}">{TAG_LABEL[t]}</span>' for t in tags(a) if t != "indoor")
    chips_html = f'<p class="chips">{chips}</p>' if chips else ""
    return f"""<li class="card" data-cat="{a['cat']}" data-tags="{' '.join(tags(a))}" data-words="{escape(words)}">
  <a href="{prefix}atrakcje/{a['slug']}.html">
    <div class="card-media">{media_html(a, prefix, lazy=True)}
      <span class="{badge_cls}">{escape(a['badge'])}</span>{num_html}</div>
    <div class="card-body">
      <p class="eyebrow">{escape(cat_name)}</p>
      <h3>{escape(a['name'])}</h3>
      <p>{escape(a['short'])}</p>
      {chips_html}
      <span class="more">Szczegóły {icon('arrow')}</span>
    </div>
  </a>
</li>"""


def build_index():
    tabs = ['<button type="button" class="tab" aria-pressed="true" data-filter="all">Wszystkie</button>']
    tabs += [f'<button type="button" class="tab" aria-pressed="false" data-filter="{k}">{escape(n)}</button>' for k, n, _ in CATEGORIES]
    quick = [("all", "Wszystko"), ("free", "Bezpłatne"), ("kids", "Dla dzieci"), ("indoor", "Pod dachem, na deszcz")]
    quick_html = "".join(
        f'<button type="button" class="qf" aria-pressed="{str(k == "all").lower()}" data-quick="{k}">{escape(n)}</button>'
        for k, n in quick)
    groups = []
    tiles = []
    for k, n, d in CATEGORIES:
        items = [a for a in ATTRACTIONS if a["cat"] == k]
        groups.append(f"""<section class="cat-group" data-cat="{k}" aria-labelledby="kat-{k}">
  <div class="cat-head"><h3 id="kat-{k}">{escape(n)}</h3><p>{escape(d)}</p></div>
  <ul class="cards">{''.join(card(a) for a in items)}</ul>
</section>""")
        cover = next(a for a in items if a.get("img"))
        tiles.append(f"""<li><a class="tile" href="#kat-{k}">
  <img src="img/{cover['img']}.jpg" alt="" loading="lazy" decoding="async">
  <span class="tile-t">{escape(n)}</span><span class="tile-n">{len(items)}</span></a></li>""")
    top = "".join(card(BY_SLUG[s], num=i) for i, s in enumerate(TOP10, 1))
    # Wszystkie wydarzenia z datą; site.js ukrywa zakończone i pokazuje najbliższe UPCOMING_MAX.
    # Bez JS widać stan z dnia budowania strony.
    today = datetime.date.today().isoformat()
    dated = sorted((e for e in CALENDAR if e["dates"]), key=lambda e: e["dates"][0])
    shown = 0
    ev_items = []
    for e in dated:
        visible = e["dates"][1] >= today and shown < UPCOMING_MAX
        shown += visible
        ev_items.append(f"""<article class="event" data-end="{e['dates'][1]}"{'' if visible else ' hidden'}>
  <p class="event-date">{escape(fmt_range(*e['dates']))}</p>
  <h3><a href="kalendarz.html#{e['id']}">{escape(e['name'])}</a></h3>
  <p>{escape(e['desc'][0])}</p>
  <p class="muted">{icon('pin')} {escape(e['place'])}</p>
</article>""")
    events = "".join(ev_items)
    closed = [a for a in ATTRACTIONS if a["status"]]
    closed_html = "".join(
        f'<li><a href="atrakcje/{a["slug"]}.html">{escape(a["name"])}</a>: {escape(a["status"][1].split(". ")[0])}.</li>'
        for a in closed)
    plans = "".join(f'<li><a href="plany.html#{pid}"><h3>{escape(t)}</h3><p>{escape(who)}</p></a></li>'
                    for pid, t, who, *_ in PLANS)
    body = f"""
<section class="hero hero-full">
  <img class="hero-bg" src="img/hero-stary-rynek.jpg" srcset="img/hero-stary-rynek-1200.jpg 1200w, img/hero-stary-rynek.jpg 2560w" sizes="100vw" alt="Kolorowe kamienice przy Starym Rynku w Poznaniu" fetchpriority="high">
  <div class="wrap hero-in">
  <div class="hero-text">
    <p class="kicker">Przewodnik dla odwiedzających</p>
    <h1>Poznań na pierwszy raz</h1>
    <p class="lead">{count_attractions(len(ATTRACTIONS))} w {CAT_WORDS.get(len(CATEGORIES), len(CATEGORIES))} kategoriach, z godzinami otwarcia, cenami biletów i dojazdem. Do tego gotowe plany zwiedzania i wszystko, co trzeba wiedzieć przed przyjazdem.</p>
    <form class="search hero-search" role="search" onsubmit="return false">
      <label for="q-hero" class="sr">Szukaj atrakcji</label>
      {icon('search')}<input id="q-hero" type="search" placeholder="Szukaj: koziołki, zoo, muzeum…" autocomplete="off" data-search-input>
    </form>
    <div class="actions">
      <a class="btn btn-gold" href="#top10">Od czego zacząć {icon('arrow')}</a>
      <a class="btn btn-ghost" href="plany.html">Plany zwiedzania</a>
      <a class="btn btn-ghost" href="informacje.html">Informacje praktyczne</a>
    </div>
  </div>
  </div>
<a class="hero-credit" href="zdjecia.html#foto-hero-stary-rynek">Fot. Egor Komarov / Unsplash</a>
</section>

<section class="wrap facts" aria-label="Najważniejsze informacje">
  <div class="fact"><p class="fact-k">Wtorek</p><p>Bezpłatne wystawy stałe m.in. w Muzeum Narodowym i Muzeum Archeologicznym. <a href="informacje.html#muzea">Inne dni bezpłatne</a></p></div>
  <div class="fact"><p class="fact-k">Poniedziałek</p><p>Większość muzeów jest zamknięta. <a href="plany.html#poniedzialek">Co robić w poniedziałek</a></p></div>
  <div class="fact"><p class="fact-k">12:00</p><p>Koziołki trykają się codziennie na wieży ratusza. Przyjdź kilka minut wcześniej.</p></div>
  <div class="fact"><p class="fact-k">18 zł</p><p>Bilet 24-godzinny na tramwaje i autobusy w strefie A. Kupisz go kartą w pojeździe. <a href="informacje.html#komunikacja">Ceny biletów</a></p></div>
</section>

<section id="top10" class="wrap section">
  <div class="section-head">
    <p class="kicker">Pierwszy raz w Poznaniu?</p>
    <h2>10 miejsc, od których warto zacząć</h2>
    <p class="muted">Najważniejsze zabytki i ulubione miejsca poznaniaków. Większość leży w centrum, w zasięgu spaceru.</p>
  </div>
  <ol class="cards top-list">{top}</ol>
</section>

<section class="wrap section" aria-labelledby="kat-h">
  <div class="section-head"><p class="kicker">Kategorie</p><h2 id="kat-h">Czego szukasz?</h2></div>
  <ul class="tiles">{''.join(tiles)}</ul>
</section>

<section class="wrap notice" aria-labelledby="zamkniete">
  {icon('alert', 'ico ico-lg')}
  <div><h2 id="zamkniete">Czasowo zamknięte lub ważne przed wizytą</h2><ul>{closed_html}</ul></div>
</section>

<section id="atrakcje" class="wrap section">
  <div class="section-head">
    <p class="kicker">Wszystkie atrakcje</p>
    <h2>Co zobaczyć w Poznaniu</h2>
    <p class="muted">Wpisz nazwę albo wybierz kategorię i filtr. Kliknij atrakcję, żeby zobaczyć pełny opis, godziny, ceny i dojazd.</p>
    <p class="map-cta"><a class="btn btn-ghost" href="mapa.html">{icon('pin')} Zobacz wszystkie na mapie</a></p>
  </div>
  <div class="finder">
    <div class="search">
      <label for="q" class="sr">Szukaj atrakcji</label>
      {icon('search')}<input id="q" type="search" placeholder="Nazwa, ulica albo rodzaj miejsca" autocomplete="off" data-search-input>
    </div>
    <div class="quick" role="group" aria-label="Szybkie filtry">{quick_html}</div>
    <div class="tabs" role="group" aria-label="Filtruj według kategorii">{''.join(tabs)}</div>
    <p class="result" aria-live="polite"></p>
  </div>
  {''.join(groups)}
  <p class="empty" hidden>Nic nie pasuje do wyszukiwania. Spróbuj innego słowa albo <button type="button" class="linkish" data-reset>pokaż wszystkie atrakcje</button>.</p>
</section>

<section class="wrap section plan" aria-labelledby="plany-h">
  <div class="section-head"><p class="kicker">Gotowe trasy</p><h2 id="plany-h">Plany zwiedzania</h2>
  <p class="muted">Trasy na 1, 2 lub 3 dni, z dziećmi, na deszcz, za darmo i na poniedziałek.</p></div>
  <ul class="plan-grid">{plans}</ul>
</section>

<section class="wrap section plan" aria-labelledby="plan-h">
  <div class="section-head"><p class="kicker">Planowanie wizyty</p><h2 id="plan-h">Zanim przyjedziesz</h2></div>
  <ul class="plan-grid">
    <li><a href="informacje.html#przyjazd"><h3>Przyjazd</h3><p>Z lotniska Ławica do dworca co kilka minut jeżdżą autobusy 148 i 159.</p></a></li>
    <li><a href="informacje.html#komunikacja"><h3>Komunikacja miejska</h3><p>Ceny biletów ZTM i jak zapłacić kartą w tramwaju.</p></a></li>
    <li><a href="informacje.html#karta"><h3>Poznańska Karta Turystyczna</h3><p>Bezpłatny wstęp do większości muzeów i zniżki.</p></a></li>
    <li><a href="informacje.html#informacja"><h3>Informacja turystyczna</h3><p>Punkty na Starym Rynku, pl. Kolegiackim, lotnisku i w Bramie Poznania.</p></a></li>
    <li><a href="informacje.html#muzea"><h3>Muzea: dni i godziny</h3><p>Kiedy wejść za darmo, a kiedy muzea są zamknięte.</p></a></li>
    <li><a href="informacje.html#zdrowie"><h3>Zdrowie</h3><p>Szpitale, nocna pomoc lekarska, dentysta i apteki.</p></a></li>
    <li><a href="informacje.html#toalety"><h3>Toalety publiczne</h3><p>Gdzie są przy trasach turystycznych i w jakich godzinach.</p></a></li>
    <li><a href="informacje.html#parkowanie"><h3>Samochodem</h3><p>Strefy płatnego parkowania, ceny i parkingi Park&amp;Ride.</p></a></li>
    <li><a href="o-poznaniu.html"><h3>O Poznaniu</h3><p>Historia, legendy, gwara, kuchnia i pogoda.</p></a></li>
    <li><a href="teatry.html"><h3>Teatry i koncerty</h3><p>Opera, filharmonia, taniec i teatr lalek. Co zrozumiesz bez polskiego.</p></a></li>
  </ul>
</section>

<section id="wydarzenia" class="wrap section">
  <div class="section-head"><p class="kicker">Kalendarz</p><h2>Nadchodzące wydarzenia</h2></div>
  <div class="events" data-upcoming="{UPCOMING_MAX}">{events}</div>
  <p class="events-empty muted"{'' if shown == 0 else ' hidden'}>Najbliższe terminy nie są jeszcze ogłoszone. Sprawdź, kiedy zwykle odbywają się wydarzenia, w kalendarzu.</p>
  <p><a class="btn btn-ghost" href="kalendarz.html">Kalendarz wydarzeń na cały rok {icon('arrow')}</a></p>
  <p class="muted small">Bieżący program kulturalny: <a href="https://kultura.poznan.pl/" target="_blank" rel="noopener">kultura.poznan.pl</a></p>
</section>
"""
    return page("Poznań na pierwszy raz", body, desc="Przewodnik dla turystów: atrakcje Poznania w kategoriach, plany zwiedzania, godziny otwarcia, ceny biletów i informacje praktyczne.", active="atrakcje")


def kv_rows(rows):
    return "".join(f"<tr><th scope=\"row\">{escape(k)}</th><td>{escape(v)}</td></tr>" for k, v in rows)


def trip_panel(a):
    t = a.get("trip")
    if not t:
        return ""
    rows = "".join(f"<p><strong>{escape(k)}.</strong> {escape(v)}</p>" for k, v in t["getting"])
    return f"""<div class="panel">
      <h2>{icon('route')} Dojazd z Poznania</h2>
      <div class="trip-go">
      <p class="trip-dist">Ok. {distance_km(t['lat'], t['lon'])} km od centrum Poznania w linii prostej.</p>
      {rows}
      </div>
    </div>"""


def build_attraction(a, idx):
    cat_name = CAT[a["cat"]][0]
    status = ""
    if a["status"]:
        kind, text = a["status"]
        label = "Czasowo zamknięte" if kind == "closed" else "Ważne przed wizytą"
        status = f'<div class="status status-{kind}" role="note">{icon("alert", "ico ico-lg")}<div><p class="status-h">{label}</p><p>{escape(text)}</p></div></div>'
    sections = "".join(
        f"<section><h2>{escape(h)}</h2>{''.join(f'<p>{escape(p)}</p>' for p in ps)}</section>" for h, ps in a["sections"])
    contact = ""
    if a["phone"]:
        contact += f'<p>{icon("phone")} <span class="sel">{escape(a["phone"])}</span></p>'
    contact += f'<p>{icon("globe")} <a href="{escape(a["www"][1])}" target="_blank" rel="noopener">{escape(a["www"][0])}</a></p>'
    same = [x for x in ATTRACTIONS if x["cat"] == a["cat"] and x["slug"] != a["slug"]]
    others = "".join(card(x, "../") for x in same[:3])
    sources = "".join(f'<li><a href="{escape(u)}" target="_blank" rel="noopener">{escape(t)}</a></li>' for t, u in a["sources"])
    prev_a = ATTRACTIONS[idx - 1]
    next_a = ATTRACTIONS[(idx + 1) % len(ATTRACTIONS)]
    body = f"""
<nav class="wrap crumbs" aria-label="Okruszki">
  <a href="../index.html">Strona główna</a> <span aria-hidden="true">/</span>
  <a href="../index.html#kat-{a['cat']}">{escape(cat_name)}</a> <span aria-hidden="true">/</span>
  <span aria-current="page">{escape(a['name'])}</span>
</nav>

<header class="wrap a-hero">
  <figure class="a-hero-img">
    {media_html(a, "../")}
    {credit_badge(a['credit'], "../") if a.get("img") else ""}
  </figure>
  <div class="a-hero-text">
    <p class="kicker">{escape(cat_name)}</p>
    <h1>{escape(a['name'])}</h1>
    <p class="lead">{escape(a['lead'])}</p>
  </div>
</header>

<div class="wrap a-layout">
  <article class="a-main">
    {status}
    {sections}
    <section class="sources">
      <h2>Źródła informacji</h2>
      <ul>{sources}</ul>
    </section>
  </article>

  <aside class="a-side" aria-label="Informacje praktyczne">
    <div class="panel">
      <h2>{icon('pin')} Adres</h2>
      <p class="sel">{escape(a['address'])}</p>
      <p class="links"><a href="{maps_url(a)}" target="_blank" rel="noopener">Pokaż na mapie</a>
      <a href="{route_url(a)}" target="_blank" rel="noopener">{icon('route')} {'Trasa z dworca Poznań Główny' if a.get('trip') else 'Trasa komunikacją'}</a>
      {'' if a.get('trip') else f'<a href="../mapa.html#{a["slug"]}">Na mapie przewodnika</a>'}</p>
    </div>
    {trip_panel(a)}
    <div class="panel">
      <h2>{icon('clock')} Godziny otwarcia</h2>
      <table class="kv"><tbody>{kv_rows(a['hours'])}</tbody></table>
    </div>
    <div class="panel">
      <h2>{icon('ticket')} Bilety</h2>
      <table class="kv"><tbody>{kv_rows(a['tickets'])}</tbody></table>
    </div>
    <div class="panel">
      <h2>Kontakt</h2>
      {contact}
    </div>
    <p class="checked">Sprawdzono {a['checked']}. Godziny i ceny mogą się zmienić, więc przed wizytą potwierdź je na stronie obiektu.</p>
  </aside>
</div>

<section class="wrap section">
  <div class="section-head"><h2>Więcej w kategorii: {escape(cat_name)}</h2></div>
  <ul class="cards">{others}</ul>
  <nav class="pager" aria-label="Poprzednia i następna atrakcja">
    <a href="{prev_a['slug']}.html">{icon('back')} {escape(prev_a['name'])}</a>
    <a href="{next_a['slug']}.html">{escape(next_a['name'])} {icon('arrow')}</a>
  </nav>
</section>
"""
    return page(f"{a['name']} – Poznań", body, prefix="../", desc=a["short"], active="atrakcje")


def build_info():
    it_points = [
        ("Stary Rynek", "Stary Rynek 59/60", "pn–sb 9:30–18:00, nd 9:00–17:00", "+48 61 852 61 56"),
        ("Plac Kolegiacki", "pl. Kolegiacki 17", "sezonowo 1.05–30.09: pn–sb 10:00–18:00, nd 9:00–17:00", "+48 883 400 034"),
        ("Lotnisko Ławica", "ul. Bukowska 285", "codziennie 7:00–19:00", "info@airport-poznan.com.pl"),
        ("Brama Poznania", "ul. Gdańska 2", "wt–pt 9:00–18:00, sb–nd 10:00–19:00", "+48 61 647 76 34"),
    ]
    it_rows = "".join(f"<tr><th scope=\"row\">{escape(n)}</th><td>{escape(ad)}</td><td>{escape(h)}</td><td class=\"sel\">{escape(c)}</td></tr>" for n, ad, h, c in it_points)
    free_days = ""
    for day, label in (("Wtorek", "We wtorki"), ("Sobota", "W soboty"), ("Niedziela", "W niedziele")):
        items = [a for a in ATTRACTIONS if any(k == day for k, _ in a["tickets"])]
        if items:
            lis = "".join(f'<li><a href="atrakcje/{a["slug"]}.html">{escape(a["name"])}</a></li>' for a in items)
            free_days += f'<h3>{label} wstęp wolny</h3><ul class="link-list">{lis}</ul>'

    free_all = [a for a in ATTRACTIONS if any(v.startswith("bezpłatnie") for _, v in a["tickets"]) and not a["status"] or a["slug"] in ("stary-rynek",)]
    free_all_html = "".join(f'<li><a href="atrakcje/{a["slug"]}.html">{escape(a["name"])}</a></li>' for a in dict((x["slug"], x) for x in free_all).values())
    closed_html = "".join(f'<li><a href="atrakcje/{a["slug"]}.html">{escape(a["name"])}</a>: {escape(a["status"][1])}</li>'
                          for a in ATTRACTIONS if a["status"] and a["status"][0] == "closed")
    mon_closed = [a for a in ATTRACTIONS if any(k == "Poniedziałek" and "nieczynne" in v for k, v in a["hours"])]
    mon_html = "".join(f'<li><a href="atrakcje/{a["slug"]}.html">{escape(a["name"])}</a></li>' for a in mon_closed)
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Planowanie wizyty</p>
  <h1>Informacje praktyczne</h1>
  <p class="lead">Jak dojechać i poruszać się po mieście, gdzie szukać pomocy lekarskiej, toalety czy parkingu. Dane sprawdzone {CHECKED}.</p>
  <nav class="toc" aria-label="Spis treści">
    <a href="#przyjazd">Przyjazd</a><a href="#komunikacja">Komunikacja</a><a href="#karta">Karta turystyczna</a>
    <a href="#informacja">Informacja turystyczna</a><a href="#muzea">Muzea</a><a href="#bezplatne">Bezpłatnie</a>
    <a href="#alarmowe">Numery alarmowe</a><a href="#zdrowie">Zdrowie</a><a href="#toalety">Toalety</a>
    <a href="#taksowki">Taksówki</a><a href="#parkowanie">Parkowanie</a><a href="#rowery">Rowerem</a>
    <a href="#przewodnicy">Przewodnicy</a><a href="#pogoda">Pogoda</a><a href="#smaki">Lokalne smaki</a>
  </nav>
</header>

<div class="wrap prose">
<section id="przyjazd">
  <h2>Przyjazd</h2>
  <h3>Lotnisko Poznań-Ławica</h3>
  <p>Lotnisko leży przy ul. Bukowskiej 285. Od kwietnia 2026 roku z terminalu do dworca Poznań Główny jeżdżą autobusy linii <strong>148</strong> i <strong>159</strong>: w godzinach szczytu co 7–8 minut, poza szczytem i w weekendy co 10 minut. Linia 148 jedzie przez Rondo Kaponiera. Rzadziej, co 30–40 minut, kursuje też linia <strong>177</strong>.</p>
  <p>Bilet kupisz kartą płatniczą przy terminalu w autobusie. Na lotnisku działa punkt informacji turystycznej, czynny codziennie 7:00–19:00.</p>
  <h3>Dworzec Poznań Główny</h3>
  <p>Dworzec kolejowy stoi przy ul. Dworcowej i ma 11 peronów. Jest połączony z centrum handlowym Avenida. Przystanek autobusów na lotnisko (148 i 159) znajduje się przy ul. Dworcowej, od strony Avenidy.</p>
</section>

<section id="komunikacja">
  <h2>Komunikacja miejska</h2>
  <p>Tramwaje i autobusy organizuje Zarząd Transportu Miejskiego (ZTM). Cennik obowiązuje od 1 września 2025 roku. Bilety czasowe obowiązują we wszystkich strefach i pozwalają na przesiadki.</p>
  <div class="table-wrap"><table class="grid">
    <thead><tr><th scope="col">Bilet</th><th scope="col">Normalny</th><th scope="col">Ulgowy</th></tr></thead>
    <tbody>
      <tr><th scope="row">do 15 minut</th><td>5 zł</td><td>2,50 zł</td></tr>
      <tr><th scope="row">do 45 minut</th><td>7 zł</td><td>3,50 zł</td></tr>
      <tr><th scope="row">do 90 minut</th><td>9 zł</td><td>4,50 zł</td></tr>
      <tr><th scope="row">24 godziny, strefa A</th><td>18 zł</td><td></td></tr>
      <tr><th scope="row">24 godziny, strefy A+B+C+D</th><td>24 zł</td><td>12 zł</td></tr>
      <tr><th scope="row">7 dni, strefa A</th><td>59 zł</td><td></td></tr>
      <tr><th scope="row">7 dni, strefy A+B+C+D</th><td>94 zł</td><td>47 zł</td></tr>
    </tbody>
  </table></div>
  <h3>Jak kupić bilet</h3>
  <p>W tramwajach i autobusach są terminale do płatności zbliżeniowej. Wybierz bilet na ekranie i przyłóż kartę płatniczą albo telefon. Przy kontroli przyłóż do czytnika kontrolera tę samą kartę, którą płaciłeś. Bilety kupisz też w aplikacji PEKA.</p>
  <p>Opłaca się bilet rodzinny 24-godzinny: dwa bilety dla dorosłych obejmują 2 dorosłych i do 3 dzieci w wieku do 18 lat. Jest też bilet weekendowy, ważny od piątku 20:00 do niedzieli 24:00.</p>
  <p class="muted">Źródło: <a href="https://www.ztm.poznan.pl/wszystko-o-biletach/cennik-biletow/" target="_blank" rel="noopener">ZTM Poznań: cennik biletów</a></p>
</section>

<section id="karta">
  <h2>Poznańska Karta Turystyczna</h2>
  <p>Karta daje bezpłatny wstęp do większości poznańskich muzeów oraz zniżki m.in. w restauracjach, obiektach sportowych i w zoo. Jest dostępna na 24, 48 lub 72 godziny, w wersji normalnej lub ulgowej, z komunikacją miejską albo bez niej.</p>
  <p>Kupisz ją online, w aplikacji na iOS i Androida oraz w punktach informacji turystycznej. Aktualne ceny pakietów są na stronie <a href="https://karta.visitpoznan.pl/" target="_blank" rel="noopener">karta.visitpoznan.pl</a>.</p>
</section>

<section id="informacja">
  <h2>Informacja turystyczna</h2>
  <p>Punkty prowadzi Poznańska Lokalna Organizacja Turystyczna, która wydaje też oficjalny portal <a href="https://visitpoznan.pl/" target="_blank" rel="noopener">visitpoznan.pl</a>.</p>
  <div class="table-wrap"><table class="grid">
    <thead><tr><th scope="col">Punkt</th><th scope="col">Adres</th><th scope="col">Godziny</th><th scope="col">Kontakt</th></tr></thead>
    <tbody>{it_rows}</tbody>
  </table></div>
</section>

<section id="muzea">
  <h2>Muzea: kiedy za darmo, kiedy zamknięte</h2>
  {free_days}
  <h3>W poniedziałki zamknięte</h3>
  <ul class="link-list">{mon_html}</ul>
  <h3>Czasowo zamknięte</h3>
  <ul>
    <li>Ratusz – Muzeum Poznania: remont od 1.07.2026 do 30.11.2027 (<a href="atrakcje/stary-rynek.html">Stary Rynek</a>).</li>
    {closed_html}
  </ul>
</section>

<section id="bezplatne">
  <h2>Bezpłatnie</h2>
  <ul class="link-list">{free_all_html}</ul>
</section>

<section id="smaki">
  <h2>Lokalne smaki</h2>
  <p>Symbolem Poznania jest rogal świętomarciński: półfrancuskie ciasto z nadzieniem z białego maku. Od 2008 roku ma unijne Chronione Oznaczenie Geograficzne. Oryginalne rogale pieką tylko wielkopolskie cukiernie z certyfikatem Kapituły Poznańskiego Tradycyjnego Rogala Świętomarcińskiego. Najwięcej zjada się ich 11 listopada.</p>
  <p>Restauracja Muga ma gwiazdkę Michelin czwarty rok z rzędu. W Przewodniku Michelin 2026 znalazło się 25 lokali z Poznania i okolic.</p>
</section>

<section id="alarmowe">
  <h2>Numery alarmowe</h2>
  <div class="table-wrap"><table class="grid">
    <tbody>
      <tr><th scope="row">Numer alarmowy (wszystkie służby)</th><td class="sel big">112</td></tr>
      <tr><th scope="row">Pogotowie ratunkowe</th><td class="sel big">999</td></tr>
      <tr><th scope="row">Straż pożarna</th><td class="sel big">998</td></tr>
      <tr><th scope="row">Policja</th><td class="sel big">997</td></tr>
      <tr><th scope="row">Straż miejska</th><td class="sel big">986</td></tr>
    </tbody>
  </table></div>
  <p>Połączenia z numerami alarmowymi są bezpłatne.</p>
</section>
{info_extra()}
</div>
"""
    return page("Informacje praktyczne – Poznań", body, desc="Dojazd, komunikacja miejska, karta turystyczna, informacja turystyczna, zdrowie, toalety, taksówki, parkowanie i numery alarmowe w Poznaniu.", active="info")


def info_extra():
    """Dodatkowe sekcje informacji praktycznych: zdrowie, toalety, taksówki, parkowanie, rowery, przewodnicy, pogoda."""
    toilets = "".join(f"<tr><th scope=\"row\">{escape(n)}</th><td>{escape(w)}</td><td>{escape(h)}</td></tr>" for n, w, h in TOILETS)
    return f"""
<section id="zdrowie">
  <h2>Zdrowie i pomoc medyczna</h2>
  <p>W nagłym zagrożeniu życia dzwoń pod <strong>112</strong> albo <strong>999</strong>. Połączenie jest bezpłatne.</p>
  <h3>Szpitalne oddziały ratunkowe (SOR)</h3>
  <ul>
    <li>Szpital Wojewódzki w Poznaniu, ul. Juraszów 7/19</li>
    <li>Wielospecjalistyczny Szpital Miejski im. Józefa Strusia, ul. Szwajcarska 3</li>
  </ul>
  <p>Na SOR jedź tylko w stanach nagłych. Przy mniej pilnych dolegliwościach wieczorem, w nocy i w weekend pomoże nocna i świąteczna opieka zdrowotna.</p>
  <h3>Nocna i świąteczna opieka zdrowotna</h3>
  <p>Działa od poniedziałku do piątku w godzinach 18:00–8:00 oraz całodobowo w soboty, niedziele i święta. Nie musisz mieszkać w Poznaniu, żeby z niej skorzystać. Wybrane punkty:</p>
  <div class="table-wrap"><table class="grid">
    <thead><tr><th scope="col">Placówka</th><th scope="col">Adres</th><th scope="col">Telefon</th></tr></thead>
    <tbody>
      <tr><th scope="row">Centrum Medyczne HCP</th><td>ul. 28 Czerwca 1956 r. 194</td><td class="sel">61 227 41 88</td></tr>
      <tr><th scope="row">Poznański Ośrodek Specjalistycznych Usług Medycznych (POSUM)</th><td>al. Solidarności 36</td><td class="sel">61 647 77 15</td></tr>
      <tr><th scope="row">Specjalistyczny Zespół Opieki Zdrowotnej nad Matką i Dzieckiem</th><td>ul. Adama Wrzoska 1</td><td class="sel">61 616 20 20</td></tr>
    </tbody>
  </table></div>
  <p>Pełną listę punktów i informację, gdzie najbliżej uzyskasz pomoc, podaje całodobowa Telefoniczna Informacja Pacjenta NFZ: <strong class="sel">800 190 590</strong>.</p>
  <h3>Dentysta w nocy i w święta</h3>
  <p>Doraźną pomoc stomatologiczną zapewnia POZDENT, tel. <span class="sel">61 835 18 01</span>.</p>
  <h3>Apteki</h3>
  <p>Każda apteka ma na drzwiach informację o najbliższej aptece dyżurnej, czynnej w nocy i w święta.</p>
  <p class="muted">Źródła: <a href="https://www.poznan.pl/mim/info/news/gdzie-do-lekarza-w-swieta,269048.html" target="_blank" rel="noopener">poznan.pl: gdzie do lekarza w święta</a>.</p>
</section>

<section id="toalety">
  <h2>Toalety publiczne</h2>
  <p>Miejskie toalety przy trasach turystycznych. Toalety automatyczne są czynne całą dobę. Toaletę znajdziesz też w każdym muzeum, centrum handlowym i na dworcu.</p>
  <div class="table-wrap"><table class="grid">
    <thead><tr><th scope="col">Miejsce</th><th scope="col">Gdzie dokładnie</th><th scope="col">Godziny</th></tr></thead>
    <tbody>{toilets}</tbody>
  </table></div>
  <p class="muted">Źródło: <a href="https://www.poznan.pl/mim/turystyka/toalety-publiczne,poi,4094/" target="_blank" rel="noopener">poznan.pl: toalety publiczne</a>, pełna lista z mapą.</p>
</section>

<section id="taksowki">
  <h2>Taksówki i przejazdy na aplikację</h2>
  <p>Taksówkę zamówisz telefonicznie albo w aplikacji. Całą dobę działa m.in. iTaxi, tel. <span class="sel">737 737 737</span>. W Poznaniu działają też przewozy na aplikację, takie jak Uber i Bolt. Postoje taksówek są m.in. przy dworcu Poznań Główny i na lotnisku.</p>
  <p>Przed kursem zapytaj o cenę albo sprawdź ją w aplikacji.</p>
</section>

<section id="parkowanie">
  <h2>Samochodem: parkowanie</h2>
  <p>Centrum miasta jest objęte strefą płatnego parkowania. Wjazd do strefy oznacza znak „P – postój płatny”. Są trzy obszary z różnymi cenami:</p>
  <div class="table-wrap"><table class="grid">
    <thead><tr><th scope="col">Strefa</th><th scope="col">Obszar</th><th scope="col">Kiedy płatna</th><th scope="col">1. godz.</th><th scope="col">2. godz.</th><th scope="col">3. godz.</th><th scope="col">kolejne</th></tr></thead>
    <tbody>
      <tr><th scope="row">SPP (niebieska)</th><td>Wilda, Łazarz, część Jeżyc, Ostrów Tumski, Śródka i okolice</td><td>pn–pt 8:00–20:00, sobota bezpłatnie</td><td>5,00 zł</td><td>6,00 zł</td><td>7,00 zł</td><td>5,00 zł</td></tr>
      <tr><th scope="row">ŚSPP Jeżyce (czerwona)</th><td>od ul. Roosevelta do ul. Polnej i Kościelnej, ul. św. Floriana</td><td>pn–sb 8:00–20:00</td><td>7,50 zł</td><td>9,00 zł</td><td>10,00 zł</td><td>7,50 zł</td></tr>
      <tr><th scope="row">ŚSPP Centrum (czerwona)</th><td>Stare Miasto</td><td>pn–sb 8:00–20:00</td><td>9,50 zł</td><td>11,00 zł</td><td>13,00 zł</td><td>9,50 zł</td></tr>
    </tbody>
  </table></div>
  <p>Podane ceny dotyczą kierowców spoza Poznania. Zapłacisz w parkomacie albo w aplikacji mobilnej. W niedziele postój jest bezpłatny we wszystkich strefach, a w strefie niebieskiej także w soboty.</p>
  <p>Wygodniej zostawić auto na parkingu <strong>Park&amp;Ride</strong> przy pętli tramwajowej i dojechać do centrum tramwajem. Takie parkingi są m.in. przy pętlach Sobieskiego, Strzeszyn, Rondo Starołęka i Św. Michała.</p>
  <p class="muted">Źródła: <a href="https://zdm.poznan.pl/oplaty-za-postoj" target="_blank" rel="noopener">ZDM Poznań: opłaty za postój</a> (cennik od 1.09.2025), <a href="https://zdm.poznan.pl/" target="_blank" rel="noopener">ZDM: parkingi Park&amp;Ride</a>.</p>
</section>

<section id="rowery">
  <h2>Rowerem</h2>
  <p>Poznań ma sieć dróg rowerowych i kilka tras rekreacyjnych przez tereny zielone. Najpopularniejsze prowadzą wzdłuż Warty (Wartostrada), przez Cytadelę, wokół Malty i Rusałki, na Dębinę, przez Lasek Marceliński i na Morasko.</p>
  <p>Mapę rowerową miasta na 2026 rok i opisy tras znajdziesz na stronie <a href="https://www.poznan.pl/rowery/" target="_blank" rel="noopener">poznan.pl/rowery</a>.</p>
</section>

<section id="przewodnicy">
  <h2>Zwiedzanie z przewodnikiem</h2>
  <p>Oprowadzanie z licencjonowanym przewodnikiem organizuje m.in. Koło Przewodników PTTK im. Marcelego Mottego. O przewodników i wycieczki możesz też zapytać w punktach informacji turystycznej.</p>
  <p>Na samodzielny spacer przydadzą się <a href="https://visitpoznan.pl/audioprzewodniki-po-poznaniu/" target="_blank" rel="noopener">audioprzewodniki Visit Poznań</a> oraz oznakowany <a href="atrakcje/trakt-krolewsko-cesarski.html">Trakt Królewsko-Cesarski</a>.</p>
</section>

<section id="pogoda">
  <h2>Pogoda i pory roku</h2>
  <p>Poznań ma klimat umiarkowany. Najcieplejszy jest lipiec (średnio 18,2 °C), najzimniejszy styczeń (średnio −1,0 °C). Lipiec jest też najbardziej deszczowy, więc latem warto mieć parasol.</p>
  <p>Aktualną prognozę podaje <a href="https://meteo.imgw.pl/" target="_blank" rel="noopener">IMGW</a>. Więcej o klimacie: <a href="o-poznaniu.html#klimat">O Poznaniu</a>.</p>
</section>
"""


def plan_stop(slug, when, hint):
    a = BY_SLUG[slug]
    hours = "; ".join(f"{k}: {v}" for k, v in a["hours"][:2])
    return f"""<li class="stop">
  <a class="stop-img" href="atrakcje/{slug}.html" tabindex="-1" aria-hidden="true">{media_html(a, "", lazy=True)}</a>
  <div>
    <p class="stop-when">{escape(when)}</p>
    <h3><a href="atrakcje/{slug}.html">{escape(a['name'])}</a></h3>
    <p>{escape(hint)}</p>
    <p class="stop-hours">{icon('clock')} {escape(hours)}</p>
  </div>
</li>"""


def build_plans():
    blocks = []
    for pid, title, who, intro, stops, note in PLANS:
        mode = "walking" if pid in ("dzien-1", "dzien-2", "za-darmo") else "transit"
        pts = [quote_plus(f'{BY_SLUG[s]["name"]}, {BY_SLUG[s]["address"]}') for s, _, _ in stops]
        route = (f"https://www.google.com/maps/dir/?api=1&travelmode={mode}&origin={pts[0]}&destination={pts[-1]}"
                 + (f"&waypoints={'%7C'.join(pts[1:-1][:8])}" if len(pts) > 2 else ""))
        blocks.append(f"""<section id="{pid}" class="plan-block">
  <div class="plan-head">
    <p class="kicker">{escape(who)}</p>
    <h2>{escape(title)}</h2>
    <p class="lead">{escape(intro)}</p>
    <p><a class="btn btn-ghost btn-sm" href="{escape(route)}" target="_blank" rel="noopener">{icon('route')} Trasa w Mapach Google</a></p>
  </div>
  <ol class="stops">{''.join(plan_stop(*st) for st in stops)}</ol>
  <p class="plan-note">{icon('alert')} {escape(note)}</p>
</section>""")
    toc = "".join(f'<a href="#{pid}">{escape(t.split(":")[0])}</a>' for pid, t, *_ in PLANS)
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Planowanie wizyty</p>
  <h1>Plany zwiedzania</h1>
  <p class="lead">Gotowe trasy dla odwiedzających Poznań pierwszy raz. Przy każdym punkcie podajemy godziny otwarcia, a pełne informacje są na podstronie atrakcji.</p>
  <nav class="toc" aria-label="Wybierz plan">{toc}</nav>
</header>
<div class="wrap plans">{''.join(blocks)}</div>
"""
    return page("Plany zwiedzania – Poznań", body, desc="Gotowe plany zwiedzania Poznania: 1, 2 i 3 dni, z dziećmi, na deszcz, za darmo i w poniedziałek.", active="plany")


def venue_card(v):
    img = ""
    if v["img"]:
        img = f"""<figure class="venue-img"><img src="img/{v['img']}.jpg" alt="" loading="lazy" decoding="async">{credit_badge(v['img'])}</figure>"""
    lang = ('<p class="venue-lang venue-lang-ok">Bez znajomości polskiego</p>' if v["lang"]
            else '<p class="venue-lang">Spektakle po polsku</p>')
    desc = "".join(f"<p>{escape(p)}</p>" for p in v["desc"])
    links = "".join(f'<a href="{escape(u)}" target="_blank" rel="noopener">{icon("globe")} {escape(t)}</a>' for t, u in v["links"])
    if v["attraction"]:
        links += f'<a href="atrakcje/{v["attraction"]}.html">{icon("arrow")} {escape(BY_SLUG[v["attraction"]]["name"])} w przewodniku</a>'
    maps = "https://www.google.com/maps/search/?api=1&query=" + quote_plus(f'{v["name"]}, {v["address"]}')
    return f"""<article id="{v['id']}" class="venue">
  {img}
  <div class="venue-body">
    <p class="kicker">{escape(v['kind'])}</p>
    <h2>{escape(v['name'])}</h2>
    {lang}
    {desc}
    <p class="muted">{icon('pin')} <a href="{maps}" target="_blank" rel="noopener">{escape(v['address'])}</a></p>
    <p class="venue-links">{links}</p>
  </div>
</article>"""


def build_theatres():
    toc = "".join(f'<a href="#{v["id"]}">{escape(v["name"].split(" (")[0])}</a>' for v in THEATRES)
    src = "".join(f'<li><a href="{escape(u)}" target="_blank" rel="noopener">{escape(t)}</a></li>' for t, u in THEATRE_SOURCES)
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Kultura</p>
  <h1>Teatry i koncerty</h1>
  <p class="lead">Najważniejsze sceny Poznania: opera, filharmonia, teatry dramatyczne, taniec i teatr lalek. Przy każdej scenie podajemy, co gra, jak kupić bilety i czy spektakl zrozumie osoba nieznająca polskiego. Aktualny repertuar i ceny są na stronach teatrów.</p>
  <nav class="toc" aria-label="Wybierz scenę">{toc}</nav>
</header>
<div class="wrap venues">
  {''.join(venue_card(v) for v in THEATRES)}
  <aside class="panel venue-more">
    <h2>Warto wiedzieć</h2>
    <p>Bilety na wiele wydarzeń sprzedaje Centrum Informacji Kulturalnej przy ul. Ratajczaka 44.</p>
    <p>Koncerty, sceny teatralne i festiwale działają też w <a href="atrakcje/zamek-cesarski.html">Centrum Kultury Zamek</a>. Coroczne festiwale, m.in. Malta Festival i Ethno Port, są w <a href="kalendarz.html">kalendarzu wydarzeń</a>.</p>
  </aside>
  <section class="sources">
    <h2>Źródła informacji</h2>
    <ul>{src}</ul>
    <p class="muted small">Sprawdzono {THEATRES_CHECKED}.</p>
  </section>
</div>
"""
    return page("Teatry i koncerty – Poznań", body, desc="Teatry i sale koncertowe w Poznaniu: Teatr Wielki (opera i balet), Filharmonia Poznańska, Teatr Polski, Teatr Nowy, Teatr Muzyczny, Polski Teatr Tańca, Teatr Animacji. Adresy, kasy, linki do repertuaru.")


def cal_event(e):
    if e["dates"]:
        badge = f'<p class="event-date">{escape(fmt_range(*e["dates"]))}</p>'
        end = f' data-end="{e["dates"][1]}"'
    else:
        badge = '<p class="event-date event-tba">Termin wkrótce</p>'
        end = ""
    desc = "".join(f"<p>{escape(p)}</p>" for p in e["desc"])
    note = f'<p class="cal-note">{icon("alert")} {escape(e["note"])}</p>' if e["note"] else ""
    src = "".join(f'<li><a href="{escape(u)}" target="_blank" rel="noopener">{escape(t)}</a></li>' for t, u in e["sources"])
    return f"""<article id="{e['id']}" class="event cal-event"{end}>
  <div class="cal-badges">{badge}<p class="event-past" hidden>Edycja zakończona</p></div>
  <h3>{escape(e['name'])}</h3>
  <p class="cal-when">{icon('clock')} {escape(e['when'])}</p>
  <p class="muted">{icon('pin')} {escape(e['place'])}</p>
  {desc}
  {note}
  <p><a href="{escape(e['link'][1])}" target="_blank" rel="noopener">{icon('globe')} {escape(e['link'][0])}</a></p>
  <details class="sources"><summary>Źródła informacji</summary><ul>{src}</ul></details>
</article>"""


def build_calendar():
    months = []
    toc = []
    for m in range(1, 13):
        evs = sorted((e for e in CALENDAR if e["month"] == m), key=lambda e: e["dates"][0] if e["dates"] else "9")
        if not evs:
            continue
        mid = f"m{m:02d}"
        toc.append(f'<a href="#{mid}">{MONTHS[m - 1]}</a>')
        months.append(f"""<section id="{mid}" class="cal-month">
  <h2>{MONTHS[m - 1]}</h2>
  <div class="events">{''.join(cal_event(e) for e in evs)}</div>
</section>""")
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Planowanie wizyty</p>
  <h1>Kalendarz wydarzeń</h1>
  <p class="lead">Najważniejsze coroczne festiwale, jarmarki i imprezy w Poznaniu, miesiąc po miesiącu. Przy każdym wydarzeniu podajemy termin najbliższej lub ostatniej edycji. Gdy nowy termin nie jest jeszcze ogłoszony, piszemy, kiedy wydarzenie zwykle się odbywa. Kalendarz zaczyna się od bieżącego miesiąca.</p>
  <nav class="toc" aria-label="Wybierz miesiąc">{''.join(toc)}</nav>
</header>
<div class="wrap cal">{''.join(months)}
  <p class="muted small">Terminy sprawdzono {CAL_CHECKED} na stronach organizatorów. Przed przyjazdem potwierdź je u organizatora. Bieżący program kulturalny miasta: <a href="https://kultura.poznan.pl/" target="_blank" rel="noopener">kultura.poznan.pl</a>. Stałe sceny: <a href="teatry.html">teatry i koncerty</a>.</p>
</div>
"""
    return page("Kalendarz wydarzeń – Poznań", body, desc="Coroczne wydarzenia w Poznaniu: Malta Festival, Ethno Port, Noc Muzeów, Imieniny Ulicy Święty Marcin, jarmarki świąteczne, maraton i inne. Terminy i miejsca.", active="kalendarz")


def build_about():
    timeline = "".join(f'<li><p class="tl-date">{escape(d)}</p><p>{escape(t)}</p></li>' for d, t in HISTORY)
    legends = "".join(f'<article class="legend"><h3>{escape(t)}</h3><p>{escape(x)}</p></article>' for t, x in LEGENDS)
    words = "".join(f'<div><dt>{escape(w)}</dt><dd>{escape(m)}</dd></div>' for w, m in DIALECT)
    dishes = "".join(f'<li><h3>{escape(n)}</h3><p>{escape(d)}</p></li>' for n, d in CUISINE)
    climate = "".join(f'<div class="fact"><p class="fact-k">{escape(v)}</p><p>{escape(l)}</p></div>' for v, l in CLIMATE)
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Poznaj miasto</p>
  <h1>O Poznaniu</h1>
  <p class="lead">Krótka historia, legendy, słowa z gwary i smaki, które warto znać przed przyjazdem.</p>
  <nav class="toc" aria-label="Spis treści">
    <a href="#historia">Historia</a><a href="#legendy">Legendy</a><a href="#gwara">Gwara</a>
    <a href="#kuchnia">Kuchnia</a><a href="#klimat">Klimat</a>
  </nav>
</header>

<div class="wrap prose">
<section id="historia">
  <h2>Historia w pigułce</h2>
  <ol class="timeline">{timeline}</ol>
  <p class="muted">Źródła: <a href="https://www.poznan.pl/mim/turystyka/rys-historyczny-poznania,p,25064,25065.html?wo_id=2024" target="_blank" rel="noopener">poznan.pl: rys historyczny</a> oraz podstrony atrakcji w tym przewodniku.</p>
</section>

<section id="legendy">
  <h2>Legendy</h2>
  <div class="legends">{legends}</div>
  <p class="muted">Źródło: <a href="https://www.poznan.pl/mim/wortals/turystyka/podania-i-legendy,p,27888,27889.html" target="_blank" rel="noopener">poznan.pl: podania i legendy</a> (streszczenia).</p>
</section>

<section id="gwara">
  <h2>Mówisz po poznańsku?</h2>
  <p>Poznaniacy wciąż używają słów z gwary. Te usłyszysz najczęściej:</p>
  <dl class="glossary">{words}</dl>
  <p class="muted">Źródło: <a href="https://www.poznan.pl/mim/slownik/" target="_blank" rel="noopener">poznan.pl: słownik gwary poznańskiej</a>.</p>
</section>

<section id="kuchnia">
  <h2>Co zjeść w Poznaniu</h2>
  <ul class="dishes">{dishes}</ul>
  <p>Oryginalne rogale świętomarcińskie pieką tylko wielkopolskie cukiernie z certyfikatem Kapituły Poznańskiego Tradycyjnego Rogala Świętomarcińskiego. Historię rogala poznasz w <a href="atrakcje/rogalowe-muzeum.html">Rogalowym Muzeum</a>, a ziemniaków w <a href="atrakcje/muzeum-pyry.html">Muzeum Pyry</a>.</p>
  <p>Restauracja Muga ma gwiazdkę Michelin czwarty rok z rzędu. W Przewodniku Michelin 2026 znalazło się 25 lokali z Poznania i okolic.</p>
  <p class="muted">Źródło: <a href="https://pl.wikipedia.org/wiki/Kuchnia_wielkopolska" target="_blank" rel="noopener">Wikipedia: kuchnia wielkopolska</a>.</p>
</section>

<section id="klimat">
  <h2>Klimat</h2>
  <div class="facts facts-flat">{climate}</div>
  <p>Latem jest ciepło, ale bywają ulewy. Zimą temperatura często spada poniżej zera. Na zwiedzanie najprzyjemniejsze są późna wiosna i wczesna jesień.</p>
  <p class="muted">Średnie z lat 1971–2000. Źródło: <a href="https://pl.wikipedia.org/wiki/Pozna%C5%84#Klimat" target="_blank" rel="noopener">Wikipedia: Poznań, klimat</a>. Prognoza: <a href="https://meteo.imgw.pl/" target="_blank" rel="noopener">IMGW</a>.</p>
</section>
</div>
"""
    return page("O Poznaniu: historia, legendy, gwara i kuchnia", body, desc="Historia Poznania w pigułce, legendy o koziołkach i hejnale, słowniczek gwary poznańskiej, kuchnia wielkopolska i klimat.", active="o")


def build_credits():
    rows = []
    for c in sorted(CREDITS.values(), key=lambda c: c["slug"]):
        lic = escape(c['license'])
        if c.get("licurl"):
            lic = f'<a href="{escape(c["licurl"])}" target="_blank" rel="noopener">{lic}</a>'
        changes = escape(c.get("modified", "pomniejszono i skompresowano"))
        rows.append(f"<tr id=\"foto-{c['slug']}\"><td><img src=\"img/{c.get('file', c['slug'] + '.jpg')}\" alt=\"\" loading=\"lazy\"></td>"
                    f"<td><a href=\"{escape(c['page'])}\" target=\"_blank\" rel=\"noopener\">{escape(c['title'])}</a></td>"
                    f"<td>{escape(c['artist'])}</td><td>{lic}</td><td>{changes}</td></tr>")
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Źródła</p>
  <h1>Autorzy zdjęć</h1>
  <p class="lead">Wszystkie zdjęcia pochodzą z Wikimedia Commons i są używane zgodnie z licencjami Creative Commons albo pochodzą z domeny publicznej. Kliknij tytuł pliku, żeby zobaczyć oryginał, albo nazwę licencji, żeby przeczytać jej treść.</p>
  <p class="muted">Na potrzeby przewodnika zdjęcia zostały pomniejszone i skompresowane, a na stronach mogą być wyświetlane w przyciętym kadrze. Inne zmiany opisuje kolumna „Zmiany”. Zmienione wersje udostępniamy na tych samych licencjach co oryginały.</p>
</header>
<div class="wrap"><div class="table-wrap"><table class="grid credits">
  <thead><tr><th scope="col"><span class="sr">Miniatura</span></th><th scope="col">Plik</th><th scope="col">Autor</th><th scope="col">Licencja</th><th scope="col">Zmiany</th></tr></thead>
  <tbody>{''.join(rows)}</tbody>
</table></div></div>
"""
    return page("Autorzy zdjęć – Poznań", body, desc="Autorzy i licencje zdjęć użytych w przewodniku.")


COORDS = json.load(open(os.path.join(ROOT, "src", "coords.json"), encoding="utf-8"))
# Kolory kategorii na mapie (czytelne na jasnym podkładzie, różne odcienie).
CAT_COLORS = {"zabytki": "#8B1A1A", "pomniki": "#8A5A12", "koscioly": "#5B3F8C", "muzea": "#1F5E8C",
              "przyroda": "#2F7D4A", "rodzina": "#C2571B", "wspolczesny": "#0F7C80",
              "wycieczki": "#6B6B2A"}
OFF_MAP = {"wycieczki"}  # poza podkładem mapy (tylko Poznań)
MAP_BOUNDS = [[52.25, 16.72], [52.51, 17.08]]  # ten sam prostokąt co podkład (src/fetch_basemap.py)


def build_map():
    cat_names = {k: n for k, n, _ in CATEGORIES if k not in OFF_MAP}
    mapped = [a for a in ATTRACTIONS if a["cat"] not in OFF_MAP]
    items = []
    for a in mapped:
        c = COORDS[a["slug"]]
        items.append({"s": a["slug"], "n": a["name"], "c": a["cat"], "lat": c["lat"], "lon": c["lon"],
                      "d": a["short"], "b": a["badge"], "img": a.get("img"), "t": tags(a),
                      "x": is_closed(a), "ap": bool(c.get("approx"))})
    data = {"items": items, "cats": {k: {"n": cat_names[k], "col": CAT_COLORS[k]} for k in cat_names},
            "bounds": MAP_BOUNDS}
    quick = [("all", "Wszystko"), ("free", "Bezpłatne"), ("kids", "Dla dzieci"), ("indoor", "Pod dachem, na deszcz")]
    quick_html = "".join(f'<button type="button" class="qf" aria-pressed="{str(k == "all").lower()}" data-quick="{k}">{escape(n)}</button>'
                         for k, n in quick)
    tabs = ['<button type="button" class="tab" aria-pressed="true" data-filter="all">Wszystkie</button>'] + [
        f'<button type="button" class="tab" aria-pressed="false" data-filter="{k}"><span class="dot" style="--dot:{CAT_COLORS[k]}"></span>{escape(n)}</button>'
        for k, n, _ in CATEGORIES if k not in OFF_MAP]
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    body = f"""
<header class="wrap page-head map-head">
  <p class="kicker">Mapa</p>
  <h1>Atrakcje na mapie</h1>
  <p class="lead">{count_attractions(len(mapped))} w Poznaniu na jednej mapie. Wycieczki za miasto mają na swoich podstronach trasę dojazdu. Kliknij punkt albo nazwę na liście, żeby zobaczyć opis i przejść do szczegółów.</p>
  <div class="finder map-finder">
    <div class="quick" role="group" aria-label="Szybkie filtry">{quick_html}</div>
    <div class="tabs" role="group" aria-label="Filtruj według kategorii">{''.join(tabs)}</div>
  </div>
</header>
<div class="wrap map-layout">
  <div id="map" class="map" role="region" aria-label="Mapa atrakcji Poznania"></div>
  <aside class="map-side" aria-label="Lista atrakcji na mapie">
    <p class="result" id="map-count" aria-live="polite"></p>
    <ol class="map-list" id="map-items"></ol>
  </aside>
</div>
<p class="wrap map-note small muted">Podkład mapy i położenie atrakcji: dane © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">autorzy OpenStreetMap</a>, licencja ODbL. Punkty z przerywaną obwódką mają położenie przybliżone. Do nawigacji użyj linku „Trasa komunikacją” na stronie atrakcji.</p>
<script type="application/json" id="map-data">{js}</script>
"""
    return page("Mapa atrakcji – Poznań", body, desc="Wszystkie atrakcje Poznania z przewodnika na jednej mapie, z filtrami.",
                active="mapa", head=f'<link rel="stylesheet" href="assets/leaflet.css?v={asset_v("leaflet.css")}">\n',
                scripts='<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>\n'
                        f'<script src="assets/map.js?v={asset_v("map.js")}"></script>\n')


def main():
    os.makedirs(os.path.join(ROOT, "atrakcje"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    for name in ("style.css", "site.js", "map.js", "leaflet.css"):
        shutil.copy(os.path.join(ROOT, "src", name), os.path.join(ROOT, "assets", name))
    out = {"index.html": build_index(), "informacje.html": build_info(), "plany.html": build_plans(),
           "kalendarz.html": build_calendar(), "teatry.html": build_theatres(),
           "o-poznaniu.html": build_about(), "zdjecia.html": build_credits(), "mapa.html": build_map()}
    for i, a in enumerate(ATTRACTIONS):
        out[f"atrakcje/{a['slug']}.html"] = build_attraction(a, i)
    for path, html in out.items():
        with open(os.path.join(ROOT, path), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
    missing = [a["img"] for a in ATTRACTIONS if a.get("img") and not os.path.exists(os.path.join(ROOT, "img", a["img"] + ".jpg"))]
    print(f"Zapisano {len(out)} stron. Brakujące zdjęcia: {missing or 'brak'}")


if __name__ == "__main__":
    main()
