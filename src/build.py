# -*- coding: utf-8 -*-
"""Generator stron przewodnika. Uruchom: python src/build.py
Tworzy: index.html, atrakcje.html, informacje.html, plany.html, kalendarz.html, teatry.html, o-poznaniu.html, zdjecia.html, atrakcje/<slug>.html"""
import datetime
import json
import os
import re
import shutil
from html import escape
from urllib.parse import quote_plus

from site_data import ATTRACTIONS, CATEGORIES, CHECKED
from data_guide import (TOP10, KIDS, INDOOR_EXTRA, PLANS, HISTORY, LEGENDS, DIALECT, CUISINE,
                        CLIMATE, TOILETS)
from data_events import CALENDAR, CAL_CHECKED
from data_theatres import THEATRES, THEATRE_SOURCES, THEATRES_CHECKED
import seo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDITS = {c["slug"]: c for c in json.load(open(os.path.join(ROOT, "img", "credits.json"), encoding="utf-8"))}
CAT = {k: (name, desc) for k, name, desc in CATEGORIES}
BY_SLUG = {a["slug"]: a for a in ATTRACTIONS}
CAT_WORDS = {4: "czterech", 5: "pięciu", 6: "sześciu", 7: "siedmiu", 8: "ośmiu"}

# Czcionki są na własnym serwerze (/fonts, @font-face na początku style.css); bez Google Fonts.
FONTS = ""

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



def resp_set(name, widths):
    """Wersje WebP zdjęcia img/<name>.jpg o podanych szerokościach (img/r/); tworzone przy pierwszym buildzie.
    Zwraca [(szerokość, plik względem katalogu głównego)] bez powiększania małych źródeł."""
    src = os.path.join(ROOT, "img", name + ".jpg")
    from PIL import Image
    im = None
    out = []
    for w in widths:
        dst = os.path.join(ROOT, "img", "r", f"{name}-{w}.webp")
        if not os.path.exists(dst):
            if im is None:
                im = Image.open(src).convert("RGB")
            if im.width < w:
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(dst, "WEBP", quality=72, method=6)
        out.append((w, f"img/r/{name}-{w}.webp"))
    if not out:
        w = Image.open(src).width
        dst = os.path.join(ROOT, "img", "r", f"{name}-{w}.webp")
        if not os.path.exists(dst):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            Image.open(src).convert("RGB").save(dst, "WEBP", quality=72, method=6)
        out.append((w, f"img/r/{name}-{w}.webp"))
    return out


def srcset_attr(name, prefix, widths=(640, 1200)):
    return ", ".join(f"{prefix}{f} {w}w" for w, f in resp_set(name, widths))


def media_html(a, prefix, lazy=False, sizes="(max-width: 600px) 92vw, (max-width: 1100px) 45vw, 380px"):
    """Zdjęcie atrakcji albo plansza z nazwą, gdy na Commons nie ma zdjęcia z podanym autorem."""
    if not a.get("img"):
        return f'<div class="no-photo" role="img" aria-label="Brak zdjęcia: {escape(a["name"])}"><span>{escape(a["name"])}</span></div>'
    extra = ' loading="lazy" decoding="async"' if lazy else ""
    return (f'<img src="{prefix}img/{a["img"]}.jpg" srcset="{srcset_attr(a["img"], prefix)}" sizes="{sizes}" '
            f'alt="{escape(a["img_alt"])}"{extra}>')


def credit_badge(slug, prefix=""):
    """Dyskretna ikonka „i” w rogu zdjęcia: autor i licencja w dymku, klik prowadzi do strony autorów."""
    c = CREDITS[slug]
    txt = escape(f'Zdjęcie: {c["artist"]}' + (f', {c["license"]}' if c["license"] else ""))
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
<script>document.documentElement.classList.add("js")</script>
<link rel="icon" href="{prefix}img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{prefix}img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="{prefix}img/favicon-48.png" sizes="48x48" type="image/png">
<link rel="icon" href="{prefix}img/favicon-96.png" sizes="96x96" type="image/png">
<link rel="apple-touch-icon" href="{prefix}img/apple-touch-icon.png">
<link rel="manifest" href="{prefix}manifest.webmanifest">
<meta name="theme-color" content="#22437F">
<meta name="description" content="{escape(desc)}">
{FONTS}
{head}<link rel="stylesheet" href="{prefix}assets/style.css?v={asset_v("style.css")}">
</head>
<body>
<a class="skip" href="#tresc">Przejdź do treści</a>
<header class="topbar">
  <div class="topbar-in">
    <a class="logo" href="{prefix or './'}" aria-label="Odkrywaj Poznań – strona główna"><img class="logo-mark" src="{prefix}img/logo-znak.svg" alt="" width="72" height="40"><img class="logo-word" src="{prefix}img/logo-napis.svg" alt="Odkrywaj Poznań" width="108" height="40"></a>
    <button type="button" class="menu-btn" aria-expanded="false" aria-controls="menu"><span class="menu-ico" aria-hidden="true"><span></span><span></span><span></span></span>Menu</button>
    <nav id="menu" aria-label="Nawigacja główna">
      <ul>
        {nav_link("atrakcje.html", "Atrakcje", "atrakcje")}
        {nav_link("mapa.html", "Mapa", "mapa")}
        {nav_link("plany.html", "Plany zwiedzania", "plany")}
        {nav_link("kalendarz.html", "Wydarzenia", "kalendarz")}
        {nav_link("informacje.html", "Praktycznie", "info")}
        {nav_link("o-poznaniu.html", "O Poznaniu", "o")}
        <li class="nav-extra"><a href="{prefix}teatry.html"{' aria-current="page"' if active == "teatry" else ""}>Teatry i koncerty</a></li>
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
      <p class="footer-logo"><img src="{prefix}img/logo.svg" alt="Odkrywaj Poznań" width="120" height="120" loading="lazy"></p>
      <p class="muted">Nieoficjalny przewodnik, niezwiązany z Urzędem Miasta Poznania.
      Datę sprawdzenia godzin i cen podajemy na stronie każdej atrakcji. Przed wizytą potwierdź je na stronie obiektu.</p>
      <p class="muted footer-contact">Widzisz błąd lub nieaktualną informację? Napisz: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
    </div>
    <ul class="footer-links">
      <li><a href="{prefix}atrakcje.html">Wszystkie atrakcje</a></li>
      <li><a href="{prefix}muzea.html">Muzea: godziny i ceny</a></li>
      <li><a href="{prefix}mapa.html">Mapa atrakcji</a></li>
      <li><a href="{prefix}plany.html">Plany zwiedzania</a></li>
      <li><a href="{prefix}informacje.html">Informacje praktyczne</a></li>
      <li><a href="{prefix}o-poznaniu.html">O Poznaniu: historia, legendy, gwara</a></li>
      <li><a href="{prefix}kalendarz.html">Kalendarz wydarzeń</a></li>
      <li><a href="{prefix}teatry.html">Teatry i koncerty</a></li>
      <li><a href="{prefix}zdjecia.html">Autorzy zdjęć</a></li>
      <li><a href="{prefix}jak-weryfikujemy.html">Jak weryfikujemy informacje</a></li>
      <li><a href="https://visitpoznan.pl/" target="_blank" rel="noopener">Visit Poznań (oficjalny portal)</a></li>
    </ul>
  </div>
  <div class="wrap footer-bar">
    <span class="footer-name">Odkrywaj Poznań</span>
    <ul class="footer-legal">
      <li><a href="{prefix}prywatnosc.html">Prywatność</a></li>
      <li><button type="button" class="linkish" data-consent-open>Ustawienia cookies</button></li>
      <li><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li>
    </ul>
    <span class="footer-copy">© {COPYRIGHT_YEAR} odkrywajpoznan.pl</span>
  </div>
</footer>
<div class="consent" role="region" aria-label="Zgoda na statystyki" data-ga="{GA_ID}" hidden>
  <p>Chcemy liczyć odwiedziny w Google Analytics, żeby wiedzieć, które części przewodnika są przydatne. To wymaga plików cookies, więc włączymy statystyki tylko za Twoją zgodą. <a href="{prefix}prywatnosc.html#cookies">Szczegóły</a></p>
  <div class="consent-btns">
    <button type="button" class="btn btn-consent" data-consent="denied">Odrzucam</button>
    <button type="button" class="btn btn-consent" data-consent="granted">Akceptuję</button>
  </div>
</div>
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


def finder_parts():
    tabs = ['<button type="button" class="tab" aria-pressed="true" data-filter="all">Wszystkie</button>']
    tabs += [f'<button type="button" class="tab" aria-pressed="false" data-filter="{k}">{escape(n)}</button>' for k, n, _ in CATEGORIES]
    quick = [("all", "Wszystko"), ("free", "Bezpłatne"), ("kids", "Dla dzieci"), ("indoor", "Pod dachem, na deszcz")]
    quick_html = "".join(
        f'<button type="button" class="qf" aria-pressed="{str(k == "all").lower()}" data-quick="{k}">{escape(n)}</button>'
        for k, n in quick) + '<button type="button" id="locate-btn" class="qf locate-btn" aria-label="Pokaż moją lokalizację"><span class="locate-ico" aria-hidden="true">📍</span>Gdzie jestem</button>'
    groups = []
    for k, n, d in CATEGORIES:
        items = [a for a in ATTRACTIONS if a["cat"] == k]
        groups.append(f"""<section class="cat-group" data-cat="{k}" aria-labelledby="kat-{k}">
  <div class="cat-head"><h3 id="kat-{k}">{escape(n)}</h3><p>{escape(d)}</p></div>
  <ul class="cards">{''.join(card(a) for a in items)}</ul>
</section>""")
    return tabs, quick_html, groups


def build_attractions():
    tabs, quick_html, groups = finder_parts()
    listing = f"""
<section id="atrakcje" class="wrap section list-page">
  <div class="section-head">
    <p class="kicker">Wszystkie atrakcje</p>
    <h1>Co zobaczyć w Poznaniu</h1>
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
"""
    return page("Atrakcje – Odkrywaj Poznań", listing, desc="Wszystkie atrakcje Poznania w kategoriach: zabytki, muzea, kościoły, parki, pomniki, rozrywka i wycieczki za miasto. Wyszukiwarka i filtry.", active="atrakcje")


def build_index():
    HERO_SRCSET = srcset_attr("hero-rynek", "", (800, 1280, 1920))
    tiles = []
    for k, n, d in CATEGORIES:
        items = [a for a in ATTRACTIONS if a["cat"] == k]
        cover = next(a for a in items if a.get("img"))
        tiles.append(f"""<li><a class="tile" href="atrakcje.html#kat-{k}">
  <img src="img/{cover['img']}.jpg" srcset="{srcset_attr(cover['img'], '')}" sizes="(max-width: 700px) 46vw, 25vw" alt="" loading="lazy" decoding="async">
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
  <img class="hero-bg" src="img/hero-rynek.jpg" srcset="{HERO_SRCSET}" sizes="100vw" width="2000" height="1500" alt="Kolorowe kamienice przy Starym Rynku w Poznaniu" fetchpriority="high">
  <div class="wrap hero-in">
  <div class="hero-text">
    <p class="kicker">Przewodnik dla odwiedzających</p>
    <h1>Poznań na pierwszy raz</h1>
    <p class="lead">{count_attractions(len(ATTRACTIONS))} w {CAT_WORDS.get(len(CATEGORIES), len(CATEGORIES))} kategoriach, z godzinami otwarcia, cenami biletów i dojazdem. Do tego gotowe plany zwiedzania i wszystko, co trzeba wiedzieć przed przyjazdem.</p>
    <form class="search hero-search" role="search" action="atrakcje.html" method="get">
      <label for="q-hero" class="sr">Szukaj atrakcji</label>
      {icon('search')}<input id="q-hero" name="q" type="search" placeholder="Szukaj: koziołki, zoo, muzeum…" autocomplete="off" enterkeyhint="search">
    </form>
    <div class="actions">
      <a class="btn btn-gold" href="#top10">Od czego zacząć {icon('arrow')}</a>
      <a class="btn btn-ghost" href="plany.html">Plany zwiedzania</a>
      <a class="btn btn-ghost" href="informacje.html">Informacje praktyczne</a>
    </div>
  </div>
  </div>
<a class="hero-credit" href="zdjecia.html#foto-hero-rynek">Fot. .abyr</a>
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
  <div class="home-browse">
    <p class="home-quick"><span class="muted">Szybko:</span>
      <a class="qlink" href="atrakcje.html?f=free">Bezpłatne</a>
      <a class="qlink" href="atrakcje.html?f=kids">Dla dzieci</a>
      <a class="qlink" href="atrakcje.html?f=indoor">Pod dachem, na deszcz</a></p>
    <p class="home-all"><a class="btn btn-gold" href="atrakcje.html">Wszystkie atrakcje ({len(ATTRACTIONS)}) {icon('arrow')}</a>
      <a class="btn btn-ghost" href="mapa.html">{icon('pin')} Na mapie</a></p>
  </div>
</section>

<section class="wrap" aria-labelledby="zamkniete">
  <details class="notice-fold">
    <summary>{icon('alert', 'ico ico-lg')}<h2 id="zamkniete">Czasowo zamknięte lub ważne przed wizytą</h2><span class="notice-n">{len(closed)}</span></summary>
    <ul>{closed_html}</ul>
  </details>
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
    preload = f'<link rel="preload" as="image" imagesrcset="{HERO_SRCSET}" imagesizes="100vw" fetchpriority="high">\n'
    return page("Odkrywaj Poznań – przewodnik dla odwiedzających", body, desc="Przewodnik dla turystów: atrakcje Poznania w kategoriach, plany zwiedzania, godziny otwarcia, ceny biletów i informacje praktyczne.", head=preload)


def kv_rows(rows):
    return "".join(f"<tr><th scope=\"row\">{escape(k)}</th><td>{escape(v)}</td></tr>" for k, v in rows)


def report_url(a):
    """Wiadomość e-mail z nazwą atrakcji i adresem strony, żeby zgłaszający nie musiał ich opisywać."""
    from urllib.parse import quote
    subject = f"Poprawka: {a['name']}"
    body = f"Strona: {SITE_URL}atrakcje/{a['slug']}\n\nCo jest nieaktualne lub błędne:\n"
    return f"mailto:{CONTACT_EMAIL}?subject={quote(subject)}&body={quote(body)}"


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
  <a href="../">Strona główna</a> <span aria-hidden="true">/</span>
  <a href="../atrakcje.html#kat-{a['cat']}">{escape(cat_name)}</a> <span aria-hidden="true">/</span>
  <span aria-current="page">{escape(a['name'])}</span>
</nav>

<header class="wrap a-hero">
  <figure class="a-hero-img">
    {media_html(a, "../", sizes="(max-width: 760px) 92vw, 640px")}
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
      <a href="../mapa.html#{a['slug']}">Na mapie przewodnika</a></p>
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
    <p class="checked">Sprawdzono {a['checked']}. Godziny i ceny mogą się zmienić, więc przed wizytą potwierdź je na stronie obiektu. <a href="../jak-weryfikujemy.html">Jak weryfikujemy</a></p>
    <p class="report"><a href="{report_url(a)}">{icon('alert')} Zgłoś nieaktualną informację</a></p>
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
    t = a.get("trip")
    lat_lon = (t["lat"], t["lon"]) if t else (COORDS[a["slug"]]["lat"], COORDS[a["slug"]]["lon"])
    return page(seo.title(a), body, prefix="../", desc=seo.description(a), active="atrakcje",
                head=seo.json_ld(a, SITE_URL, cat_name, lat_lon))


def build_info():
    it_points = [
        ("Stary Rynek", "Stary Rynek 59/60", "pn–sb 9:30–18:00, nd 9:00–17:00", "+48 61 852 61 56"),
        ("Plac Kolegiacki", "pl. Kolegiacki 17", "sezonowo 1.05–30.09: pn–sb 10:00–18:00, nd 9:00–17:00", "+48 883 400 034"),
        ("Lotnisko Ławica", "ul. Bukowska 285", "codziennie (źródła podają różne godziny: 7:00–19:00 albo 8:00–20:00)", "info@airport-poznan.com.pl"),
        ("Brama Poznania", "ul. Gdańska 2", "wt–pt 9:00–18:00, sb–nd 10:00–19:00", "+48 61 647 76 34"),
    ]
    it_rows = "".join(f"<tr><th scope=\"row\">{escape(n)}</th><td>{escape(ad)}</td><td>{escape(h)}</td><td class=\"sel\">{escape(c)}</td></tr>" for n, ad, h, c in it_points)
    free_days = ""
    for day, label in (("Poniedziałek", "W poniedziałki"), ("Wtorek", "We wtorki"), ("Środa", "W środy"), ("Czwartek", "W czwartki"),
                       ("Piątek", "W piątki"), ("Sobota", "W soboty"), ("Niedziela", "W niedziele")):
        items = [a for a in ATTRACTIONS if any(k == day for k, _ in a["tickets"])]
        if items:
            lis = "".join(f'<li><a href="atrakcje/{a["slug"]}.html">{escape(a["name"])}</a></li>' for a in items)
            free_days += f'<h3>{label} wstęp wolny</h3><ul class="link-list">{lis}</ul>'

    # Tylko miejsca bez biletu. „Dzieci do 3 lat bezpłatnie” w płatnym cenniku nie wystarcza.
    free_all = [a for a in ATTRACTIONS if is_free(a)]
    free_all_html = "".join(f'<li><a href="atrakcje/{a["slug"]}.html">{escape(a["name"])}</a></li>' for a in free_all)
    closed_html = "".join(f'<li><a href="atrakcje/{a["slug"]}.html">{escape(a["name"])}</a>: {escape(a["status"][1])}</li>'
                          for a in ATTRACTIONS if a["status"] and a["status"][0] == "closed")
    def closed_monday(a):
        # Etykiety typu „Poniedziałek–wtorek”, „Niedziela–poniedziałek”, „Poniedziałek, niedziela, święta”.
        named = set()
        for k, v in a["hours"]:
            named.update(seo._day_set(k.replace(", święta", "")) or [])
        for k, v in a["hours"]:
            if "nieczynne" in v and "nieczynne dla" not in v:
                days = seo._day_set(k.replace(", święta", ""))
                if k.lower() == "pozostałe dni":  # np. Muzeum Farmacji: czynne tylko w czwartki
                    days = [d for d in range(7) if d not in named]
                if days and 0 in days:
                    return True
        return False
    mon_closed = [a for a in ATTRACTIONS if not is_closed(a) and closed_monday(a)]
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
  <p>Lotnisko leży przy ul. Bukowskiej 285. Między terminalem a dworcem Poznań Główny kursują autobusy linii <strong>148</strong> i <strong>159</strong>. Od 18 kwietnia 2026 roku jeżdżą na zmianę, więc z przystanków Poznań Główny, Rondo Kaponiera i Bałtyk oraz spod terminalu odjeżdżają co 7–8 minut w godzinach szczytu, a poza szczytem i w weekendy co 10 minut. Linia <strong>177</strong> kursuje co 30 minut w szczycie i co 40 minut poza nim.</p>
  <p>Bilet kupisz kartą płatniczą przy terminalu w autobusie. Na lotnisku działa punkt informacji turystycznej.</p>
  <p class="muted">Źródło: <a href="https://www.ztm.poznan.pl/aktualnosci/komunikaty/linie-nr-148-159-oraz-177-zmiany-w-komunikacji-na-trasie-poznan-glowny-port-lotniczy-lawica-od-18-kwietnia/" target="_blank" rel="noopener">ZTM Poznań: linie 148, 159 i 177 od 18 kwietnia 2026</a></p>
  <h3>Dworzec Poznań Główny</h3>
  <p>Budynek dworca jest połączony z centrum handlowym Avenida. Autobusy na lotnisko (148 i 159) odjeżdżają z przystanku Poznań Główny.</p>
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
      <tr><th scope="row">24 godziny, strefa A</th><td>18 zł</td><td>9 zł</td></tr>
      <tr><th scope="row">24 godziny, strefy A+B+C+D</th><td>24 zł</td><td>12 zł</td></tr>
      <tr><th scope="row">7 dni, strefa A</th><td>59 zł</td><td>29,50 zł</td></tr>
      <tr><th scope="row">7 dni, strefy A+B+C+D</th><td>94 zł</td><td>47 zł</td></tr>
    </tbody>
  </table></div>
  <h3>Jak kupić bilet</h3>
  <p>W tramwajach i autobusach są terminale do płatności zbliżeniowej. Kupisz w nich bilety czasowe i 24-godzinne: wybierz bilet na ekranie i przyłóż kartę płatniczą albo telefon. Terminal nie drukuje biletu, a przy kontroli wystarczy okazać kartę, którą płaciłeś. Bilety kupisz też w aplikacjach moBILET, SkyCash, GoPay, jakdojade.pl i zBiletem oraz w biletomatach na przystankach.</p>
  <p>Opłaca się promocja „Rodzina 24 h”: dwa jednocześnie skasowane normalne bilety 24-godzinne obejmują 2 dorosłych i do 3 dzieci w wieku do 18 lat. Z kolei bilet 24-godzinny skasowany od piątku 20:00 do soboty 24:00 jest ważny do niedzieli 24:00 („Weekend 24 h”).</p>
  <p class="muted">Źródła: <a href="https://www.ztm.poznan.pl/wszystko-o-biletach/cennik-biletow/" target="_blank" rel="noopener">ZTM Poznań: cennik biletów</a>, <a href="https://www.ztm.poznan.pl/wszystko-o-biletach/rodzaje-i-formy-biletow/" target="_blank" rel="noopener">ZTM: rodzaje i formy biletów</a>, <a href="https://www.opspoznan.pl/" target="_blank" rel="noopener">portal pasażera: zakup w terminalu</a></p>
</section>

<section id="karta">
  <h2>Poznańska Karta Turystyczna</h2>
  <p>Karta daje bezpłatny wstęp do większości poznańskich muzeów oraz zniżki m.in. w restauracjach, obiektach sportowych i na bilet do Nowego Zoo. Pakiet Poznań jest dostępny na 24, 48 lub 72 godziny, w wersji normalnej lub ulgowej, z komunikacją miejską albo bez niej. Jest też pakiet „Dookoła Poznania” z atrakcjami w powiecie poznańskim.</p>
  <p>Kupisz ją online, w aplikacji oraz w punktach informacji turystycznej na Starym Rynku, na placu Kolegiackim (sezonowo) i na lotnisku, a także w sklepie z pamiątkami w Bramie Poznania. Aktualne ceny pakietów są na stronie <a href="https://karta.visitpoznan.pl/" target="_blank" rel="noopener">karta.visitpoznan.pl</a>.</p>
</section>

<section id="informacja">
  <h2>Informacja turystyczna</h2>
  <p>Punkty prowadzi Poznańska Lokalna Organizacja Turystyczna, która wydaje też oficjalny portal <a href="https://visitpoznan.pl/" target="_blank" rel="noopener">visitpoznan.pl</a>.</p>
  <div class="table-wrap"><table class="grid">
    <thead><tr><th scope="col">Punkt</th><th scope="col">Adres</th><th scope="col">Godziny</th><th scope="col">Kontakt</th></tr></thead>
    <tbody>{it_rows}</tbody>
  </table></div>
  <p class="muted">Źródło: <a href="https://visitpoznan.pl/it" target="_blank" rel="noopener">visitpoznan.pl: Informacja Turystyczna</a></p>
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
    return page("Informacje praktyczne – Odkrywaj Poznań", body, desc="Dojazd, komunikacja miejska, karta turystyczna, informacja turystyczna, zdrowie, toalety, taksówki, parkowanie i numery alarmowe w Poznaniu.", active="info")


def info_extra():
    """Dodatkowe sekcje informacji praktycznych: zdrowie, toalety, taksówki, parkowanie, rowery, przewodnicy, pogoda."""
    toilets = "".join(f"<tr><th scope=\"row\">{escape(n)}</th><td>{escape(w)}</td><td>{escape(h)}</td></tr>" for n, w, h in TOILETS)
    return f"""
<section id="zdrowie">
  <h2>Zdrowie i pomoc medyczna</h2>
  <p>W nagłym zagrożeniu życia dzwoń pod <strong>112</strong> albo <strong>999</strong>. Połączenie jest bezpłatne.</p>
  <h3>Szpitalne oddziały ratunkowe (SOR)</h3>
  <p>SOR-y działają m.in. w tych szpitalach:</p>
  <ul>
    <li>Szpital Wojewódzki w Poznaniu, ul. Juraszów 7/19</li>
    <li>Wielospecjalistyczny Szpital Miejski im. Józefa Strusia, ul. Szwajcarska 3</li>
  </ul>
  <p>Na SOR jedź tylko w stanach nagłych. Przy mniej pilnych dolegliwościach wieczorem, w nocy i w weekend pomoże nocna i świąteczna opieka zdrowotna.</p>
  <h3>Nocna i świąteczna opieka zdrowotna</h3>
  <p>Działa od poniedziałku do piątku w godzinach 18:00–8:00 oraz całodobowo w soboty, niedziele i święta. Nie musisz mieszkać w Poznaniu, żeby z niej skorzystać. Wybrane punkty z listy podanej przez miasto (poznan.pl, grudzień 2025):</p>
  <div class="table-wrap"><table class="grid">
    <thead><tr><th scope="col">Placówka</th><th scope="col">Adres</th><th scope="col">Telefon</th></tr></thead>
    <tbody>
      <tr><th scope="row">Centrum Medyczne HCP</th><td>ul. 28 Czerwca 1956 r. 194</td><td class="sel">61 227 41 88</td></tr>
      <tr><th scope="row">Poznański Ośrodek Specjalistycznych Usług Medycznych (POSUM)</th><td>al. Solidarności 36</td><td class="sel">61 647 77 15</td></tr>
      <tr><th scope="row">Specjalistyczny Zespół Opieki Zdrowotnej nad Matką i Dzieckiem</th><td>ul. Adama Wrzoska 1</td><td class="sel">61 616 20 20</td></tr>
    </tbody>
  </table></div>
  <p>Pełną listę punktów i informację, gdzie najbliżej uzyskasz pomoc, podaje Telefoniczna Informacja Pacjenta NFZ: <strong class="sel">800 190 590</strong>.</p>
  <h3>Dentysta w nocy i w święta</h3>
  <p>Doraźną pomoc stomatologiczną zapewnia Pozdent Stomatologia, ul. Czajcza 1a (Wilda), tel. <span class="sel">61 835 18 01</span>.</p>
  <h3>Apteki</h3>
  <p>Listę aptek czynnych w nocy i w święta podaje <a href="https://www.woia.pl/" target="_blank" rel="noopener">Wielkopolska Okręgowa Izba Aptekarska</a>.</p>
  <p class="muted">Źródła: <a href="https://www.poznan.pl/mim/info/news/gdzie-do-lekarza-w-swieta,269048.html" target="_blank" rel="noopener">poznan.pl: gdzie do lekarza w święta</a>.</p>
</section>

<section id="toalety">
  <h2>Toalety publiczne</h2>
  <p>Miejskie toalety przy trasach turystycznych. Toalety automatyczne z tej listy są czynne całą dobę.</p>
  <div class="table-wrap"><table class="grid">
    <thead><tr><th scope="col">Miejsce</th><th scope="col">Gdzie dokładnie</th><th scope="col">Godziny</th></tr></thead>
    <tbody>{toilets}</tbody>
  </table></div>
  <p class="muted">Źródło: <a href="https://www.poznan.pl/mim/turystyka/toalety-publiczne,poi,4094/" target="_blank" rel="noopener">poznan.pl: toalety publiczne</a>, pełna lista z mapą.</p>
</section>

<section id="taksowki">
  <h2>Taksówki i przejazdy na aplikację</h2>
  <p>Taksówkę zamówisz telefonicznie albo w aplikacji, np. iTaxi, tel. <span class="sel">737 737 737</span>. W Poznaniu działają też przewozy na aplikację, takie jak Uber i Bolt.</p>
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
  <p>Podane ceny dotyczą kierowców spoza Poznania. Opłatę wnosi się w parkomacie, inne formy płatności opisuje strona ZDM. W niedziele postój jest bezpłatny we wszystkich strefach, a w strefie niebieskiej także w soboty.</p>
  <p>Wygodniej zostawić auto na parkingu <strong>Park&amp;Ride</strong> i dojechać do centrum komunikacją miejską. Miejskie parkingi P&amp;R to: Szymanowskiego (przy PST), św. Michała, Biskupińska (przy stacji Poznań Strzeszyn), Rondo Starołęka i Junikowo PKM (Plewiska, przy stacji Poznań Junikowo). Z biletem okresowym ZTM na karcie PEKA postój jest bezpłatny.</p>
  <p class="muted">Źródła: <a href="https://zdm.poznan.pl/oplaty-za-postoj" target="_blank" rel="noopener">ZDM Poznań: opłaty za postój</a> (cennik od 1.09.2025), <a href="https://zdm.poznan.pl/parkowanie-parkingi-park-ride-1" target="_blank" rel="noopener">ZDM: parkingi Park&amp;Ride</a>.</p>
</section>

<section id="rowery">
  <h2>Rowerem</h2>
  <p>Poznań ma sieć dróg rowerowych. Wzdłuż Warty biegnie <a href="atrakcje/bulwary-warta.html">Wartostrada</a>, ścieżka piesza i rowerowa nad rzeką.</p>
  <p>Mapę rowerową Poznania 2026 znajdziesz na stronie <a href="https://www.poznan.pl/rowery/" target="_blank" rel="noopener">poznan.pl/rowery</a>.</p>
</section>

<section id="przewodnicy">
  <h2>Zwiedzanie z przewodnikiem</h2>
  <p>Oprowadzanie z przewodnikiem organizuje m.in. <a href="https://www.przewodnicy-pttk.org/pl/strona-glowna/" target="_blank" rel="noopener">Koło Przewodników PTTK im. Marcelego Mottego</a> (pl. Kolegiacki 16). Przewodnika można też zamówić w punktach informacji turystycznej.</p>
  <p>Na samodzielny spacer przydadzą się <a href="https://visitpoznan.pl/audioprzewodniki-po-poznaniu" target="_blank" rel="noopener">audioprzewodniki Visit Poznań</a> oraz oznakowany <a href="atrakcje/trakt-krolewsko-cesarski.html">Trakt Królewsko-Cesarski</a>.</p>
</section>

<section id="pogoda">
  <h2>Pogoda i pory roku</h2>
  <p>Poznań ma klimat umiarkowany. Najcieplejszy jest lipiec (średnio 19,5 °C), najzimniejszy styczeń (średnio −0,4 °C). Lipiec jest też najbardziej deszczowy, więc latem warto mieć parasol.</p>
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
    return page("Plany zwiedzania – Odkrywaj Poznań", body, desc="Gotowe plany zwiedzania Poznania: 1, 2 i 3 dni, z dziećmi, na deszcz, za darmo i w poniedziałek.", active="plany")


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
    return page("Teatry i koncerty – Odkrywaj Poznań", body, desc="Teatry i sale koncertowe w Poznaniu: Teatr Wielki (opera i balet), Filharmonia Poznańska, Teatr Polski, Teatr Nowy, Teatr Muzyczny, Polski Teatr Tańca, Teatr Animacji. Adresy, kasy, linki do repertuaru.", active="teatry")


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
    return page("Kalendarz wydarzeń – Odkrywaj Poznań", body, desc="Coroczne wydarzenia w Poznaniu: Malta Festival, Ethno Port, Noc Muzeów, Imieniny Ulicy Święty Marcin, jarmarki świąteczne, maraton i inne. Terminy i miejsca.", active="kalendarz")


def build_about():
    def tl_more(h):
        # Opcjonalny trzeci element: slug atrakcji, o której można przeczytać więcej.
        if len(h) < 3:
            return ""
        return f' <a href="atrakcje/{h[2]}.html">{escape(BY_SLUG[h[2]]["name"])} →</a>'
    timeline = "".join(f'<li><p class="tl-date">{escape(h[0])}</p><p>{escape(h[1])}{tl_more(h)}</p></li>' for h in HISTORY)
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
  <p class="muted">Źródła: <a href="https://www.poznan.pl/mim/turystyka/rys-historyczny-poznania,p,25064,25065.html?wo_id=2024" target="_blank" rel="noopener">poznan.pl: rys historyczny</a>, hasła Wikipedii o poszczególnych wydarzeniach oraz podstrony atrakcji w tym przewodniku.</p>
</section>

<section id="legendy">
  <h2>Legendy</h2>
  <div class="legends">{legends}</div>
  <p class="muted">Źródło: <a href="https://www.poznan.pl/mim/wortals/turystyka/podania-i-legendy,p,27888,27889.html" target="_blank" rel="noopener">poznan.pl: podania i legendy</a> (streszczenia) i <a href="https://pl.wikipedia.org/wiki/Rogal_%C5%9Bwi%C4%99tomarci%C5%84ski" target="_blank" rel="noopener">Wikipedia: rogal świętomarciński</a>.</p>
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
  <p class="muted">Źródła: <a href="https://pl.wikipedia.org/wiki/Kuchnia_wielkopolska" target="_blank" rel="noopener">Wikipedia: kuchnia wielkopolska</a>, <a href="https://www.poznan.pl/mim/info/news/25-restauracji-z-poznania-i-okolic-z-wyroznieniami-michelin-2026,281300.html" target="_blank" rel="noopener">poznan.pl: wyróżnienia Michelin 2026</a>.</p>
</section>

<section id="klimat">
  <h2>Klimat</h2>
  <div class="facts facts-flat">{climate}</div>
  <p>Latem jest ciepło, ale bywają ulewy. Zimą temperatura często spada poniżej zera. Na zwiedzanie najprzyjemniejsze są późna wiosna i wczesna jesień.</p>
  <p class="muted">Średnie z lat 1991–2020, stacja Poznań-Ławica. Obliczenia na podstawie <a href="https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/miesieczne/synop/" target="_blank" rel="noopener">danych IMGW-PIB</a>. Prognoza: <a href="https://meteo.imgw.pl/" target="_blank" rel="noopener">IMGW</a>.</p>
</section>
</div>
"""
    return page("O Poznaniu: historia, legendy, gwara i kuchnia – Odkrywaj Poznań", body, desc="Historia Poznania w pigułce, legendy o koziołkach i hejnale, słowniczek gwary poznańskiej, kuchnia wielkopolska i klimat.", active="o")


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
    return page("Autorzy zdjęć – Odkrywaj Poznań", body, desc="Autorzy i licencje zdjęć użytych w przewodniku.")


COORDS = json.load(open(os.path.join(ROOT, "src", "coords.json"), encoding="utf-8"))
# Kolory kategorii na mapie (czytelne na jasnym podkładzie, różne odcienie).
CAT_COLORS = {"zabytki": "#8B1A1A", "pomniki": "#8A5A12", "koscioly": "#5B3F8C", "muzea": "#1F5E8C",
              "przyroda": "#2F7D4A", "rodzina": "#C2571B", "wspolczesny": "#0F7C80",
              "wycieczki": "#6B6B2A"}


def build_map():
    cat_names = {k: n for k, n, _ in CATEGORIES}
    items = []
    for a in ATTRACTIONS:
        c = a["trip"] if a.get("trip") else COORDS[a["slug"]]
        items.append({"s": a["slug"], "n": a["name"], "c": a["cat"], "lat": c["lat"], "lon": c["lon"],
                      "d": a["short"], "b": a["badge"], "img": a.get("img"), "t": tags(a),
                      "x": is_closed(a), "ap": bool(c.get("approx")),
                      # Nawigacja w Google Maps (zwykłe linki: nic nie jest wysyłane do Google przed kliknięciem).
                      "gm": maps_url(a), "rt": route_url(a), "rf": bool(a.get("trip"))})
    data = {"items": items, "cats": {k: {"n": cat_names[k], "col": CAT_COLORS[k]} for k in cat_names}}
    quick = [("all", "Wszystko"), ("free", "Bezpłatne"), ("kids", "Dla dzieci"), ("indoor", "Pod dachem, na deszcz")]
    quick_html = "".join(f'<button type="button" class="qf" aria-pressed="{str(k == "all").lower()}" data-quick="{k}">{escape(n)}</button>'
                         for k, n in quick) + '<button type="button" id="locate-btn" class="qf locate-btn" aria-label="Pokaż moją lokalizację"><span class="locate-ico" aria-hidden="true">📍</span>Gdzie jestem</button>'
    tabs = ['<button type="button" class="tab" aria-pressed="true" data-filter="all">Wszystkie</button>'] + [
        f'<button type="button" class="tab" aria-pressed="false" data-filter="{k}"><span class="dot" style="--dot:{CAT_COLORS[k]}"></span>{escape(n)}</button>'
        for k, n, _ in CATEGORIES]
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    body = f"""
<header class="wrap page-head map-head">
  <p class="kicker">Mapa</p>
  <h1>Atrakcje na mapie</h1>
  <p class="lead">{count_attractions(len(ATTRACTIONS))} na jednej mapie, razem z wycieczkami za miasto.<span class="lead-more"> Kliknij punkt albo nazwę na liście, żeby zobaczyć opis i przejść do szczegółów.</span></p>
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
<p class="wrap map-note small muted">Mapa i położenie atrakcji: © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">autorzy OpenStreetMap</a>, dane na licencji ODbL. Punkty z przerywaną obwódką mają położenie przybliżone. Przyciski w opisie punktu otwierają Google Maps z położeniem atrakcji albo trasą komunikacją.</p>
<script type="application/json" id="map-data">{js}</script>
"""
    return page("Mapa atrakcji – Odkrywaj Poznań", body, desc="Wszystkie atrakcje Poznania z przewodnika na jednej mapie, z filtrami.",
                active="mapa", head=f'<link rel="stylesheet" href="assets/leaflet.css?v={asset_v("leaflet.css")}">\n',
                scripts=f'<script src="assets/leaflet.js?v={asset_v("leaflet.js")}"></script>\n'
                        f'<script src="assets/map.js?v={asset_v("map.js")}"></script>\n')


# Google Analytics 4: ładowany przez site.js WYŁĄCZNIE po kliknięciu „Akceptuję” w banerze zgody.
GA_ID = "G-S4K8EW3YGQ"
COPYRIGHT_YEAR = datetime.date.today().year

# Kontakt w sprawie strony i prywatności (strona prowadzona pod nazwą serwisu, decyzja z 30.09.2026).
CONTACT_EMAIL = "kontakt@odkrywajpoznan.pl"
LINKS_CHECKED = "07.10.2026"   # data ostatniego uruchomienia src/check_links.py; podbić po kolejnej kontroli
PRIVACY_UPDATED = "05.10.2026"


def build_method():
    mail = f'<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>'
    dates = sorted(datetime.datetime.strptime(a["checked"], "%d.%m.%Y").date() for a in ATTRACTIONS)
    fmt = lambda d: d.strftime("%d.%m.%Y")
    body = f"""
<header class="wrap page-head">
  <p class="kicker">O serwisie</p>
  <h1>Jak weryfikujemy informacje</h1>
  <p class="lead">W przewodniku ważniejsze od tego, żeby było dużo, jest to, żeby było prawdziwie. Poniżej opisujemy, skąd bierzemy dane, co robimy, gdy źródła się nie zgadzają, i czego nie obiecujemy.</p>
  <nav class="toc" aria-label="Spis treści">
    <a href="#zrodla">Skąd bierzemy dane</a><a href="#sprzecznosci">Gdy źródła się nie zgadzają</a><a href="#daty">Daty sprawdzenia</a>
    <a href="#czego-nie">Czego nie robimy</a><a href="#zdjecia">Zdjęcia</a><a href="#bledy">Znalazłeś błąd?</a>
  </nav>
</header>

<div class="wrap prose">
<section id="zrodla">
  <h2>Skąd bierzemy dane</h2>
  <ul>
    <li><strong>Godziny, ceny, adresy i telefony</strong> bierzemy ze strony samego obiektu albo z oficjalnych portali: miejskiego poznan.pl, turystycznego visitpoznan.pl i serwisów organizatorów, na przykład muzeów. Wyszukiwarki i agregatory często pokazują stare dane. Przykład: Rogalowe Muzeum Poznania miało w wynikach wyszukiwania ceny sprzed podwyżki, a według strony muzeum od 2 stycznia 2026 roku bilet kosztuje 41 i 47 zł.</li>
    <li><strong>Opisy historyczne</strong> opieramy na oficjalnych portalach i na Wikipedii. Z Wikipedii nie bierzemy godzin ani cen.</li>
    <li><strong>Każda z {len(ATTRACTIONS)} atrakcji</strong> ma pod opisem listę źródeł z linkami, więc możesz sprawdzić, skąd pochodzi dana informacja.</li>
    <li><strong>Klimat Poznania</strong> policzyliśmy z surowych danych IMGW z lat 1991–2020 (stacja Poznań-Ławica), a nie przepisaliśmy z innych stron.</li>
    <li><strong>Kalendarz wydarzeń</strong> zawiera tylko to, co potwierdza strona organizatora albo oficjalny portal. Daty kolejnej edycji wpisujemy dopiero wtedy, gdy organizator je ogłosi, nie na podstawie szacunków.</li>
  </ul>
</section>

<section id="sprzecznosci">
  <h2>Gdy źródła się nie zgadzają</h2>
  <p>Nie wybieramy „na oko”. W takiej sytuacji robimy jedną z dwóch rzeczy: podajemy tylko to, co potwierdzają wszystkie źródła, i opisujemy rozbieżność z nazwami źródeł, albo pomijamy daną informację i odsyłamy do obiektu.</p>
  <ul>
    <li><a href="atrakcje/fort-iii.html">Fort III</a>: dwa oficjalne portale różnie podają dni i godziny wejść. Napisaliśmy, co jest pewne, a rozbieżność opisaliśmy wprost.</li>
    <li><a href="atrakcje/muzeum-czerwca-1956.html">Muzeum Poznańskiego Czerwca 1956</a>: godzin nie udało się potwierdzić w żadnym aktualnym źródle, więc ich nie podajemy i prosimy o kontakt z muzeum.</li>
    <li><a href="atrakcje/niewidzialna-ulica.html">Niewidzialna Ulica</a>: źródła podają różne ceny, więc odsyłamy do strony obiektu zamiast wpisywać jedną z nich.</li>
  </ul>
</section>

<section id="daty">
  <h2>Daty sprawdzenia</h2>
  <p>Pod każdą atrakcją widać datę „Sprawdzono”. To dzień, w którym ostatnio porównaliśmy dane ze źródłami. Obecnie wszystkie atrakcje były sprawdzane od {fmt(dates[0])} do {fmt(dates[-1])}, a część „Informacje praktyczne” {CHECKED}.</p>
  <p>Godziny i ceny zmieniają się, a data nie jest gwarancją, że dziś jest tak samo. Przed wizytą potwierdź je na stronie obiektu. Nie obiecujemy odświeżania danych w stałym rytmie, ale zmiany, o których się dowiadujemy, sprawdzamy i wprowadzamy.</p>
  <p>Linki do źródeł kontrolujemy automatycznie (ostatnia kontrola: {LINKS_CHECKED}), a gdy źródło przestaje istnieć, usuwamy je razem z informacjami, które tylko na nim się opierały.</p>
</section>

<section id="czego-nie">
  <h2>Czego nie robimy</h2>
  <ul>
    <li>Nie podajemy numerów telefonów, godzin ani cen, jeśli nie mamy ich z wiarygodnego źródła.</li>
    <li>Nie podajemy linii ani przystanków do atrakcji bez sprawdzenia. Zamiast tego jest link do trasy komunikacją publiczną w Mapach Google.</li>
    <li>Nie piszemy recenzji ani ocen i nie przyjmujemy płatnych wpisów. Na stronie nie ma reklam.</li>
    <li>Opieramy się na źródłach publicznych, a nie na własnych relacjach z wizyt w każdym miejscu.</li>
  </ul>
  <p>Przewodnik prowadzi prywatna, niekomercyjna strona niezwiązana z Urzędem Miasta Poznania (<a href="prywatnosc.html#kto">więcej</a>).</p>
</section>

<section id="zdjecia">
  <h2>Zdjęcia</h2>
  <p>Większość zdjęć pochodzi z Wikimedia Commons na otwartych licencjach. Autora i licencję zdjęcia znajdziesz po kliknięciu ikonki „i” w rogu zdjęcia, a wszystkie razem na stronie <a href="zdjecia.html">Autorzy zdjęć</a>. Gdy na Commons nie ma zdjęcia z podanym autorem, zamiast niego pokazujemy planszę z nazwą miejsca.</p>
</section>

<section id="bledy">
  <h2>Znalazłeś błąd?</h2>
  <p>Przy każdej atrakcji jest link „Zgłoś nieaktualną informację”, który otwiera gotowy e-mail z nazwą miejsca. Możesz też napisać na {mail}. Zgłoszenie sprawdzamy w źródłach, zanim zmienimy dane.</p>
</section>
</div>
"""
    return page("Jak weryfikujemy informacje – Odkrywaj Poznań", body,
                desc="Skąd bierzemy godziny, ceny i opisy, co robimy, gdy źródła się nie zgadzają, i jak zgłosić błąd. Zasady weryfikacji informacji w przewodniku Odkrywaj Poznań.")


def build_museums():
    from museums_table import derive, open_monday, sort_key, DAYS, LABEL
    mus = sorted((a for a in ATTRACTIONS if a["cat"] == "muzea"), key=lambda a: sort_key(a["name"]))
    info = {a["slug"]: derive(a) for a in mus}
    link = lambda a: f'<a href="atrakcje/{a["slug"]}.html">{escape(a["name"])}</a>'

    def free_cell(a):
        d = info[a["slug"]]
        if d["free_always"]:
            return "zawsze"
        return ", ".join(LABEL[x] for x in d["free_days"]) or "—"

    rows = []
    for a in mus:
        d = info[a["slug"]]
        hours = "".join(f"<div><span class=\"muted\">{escape(l)}:</span> {escape(x)}</div>" for l, x in a["hours"])
        tick = [(l, x) for l, x in a["tickets"] if not ("wstęp wolny" in x.lower() or l.lower() in LABEL.values())]
        tickets = "".join(f"<div><span class=\"muted\">{escape(l)}:</span> {escape(x)}</div>" for l, x in tick) or "—"
        note = '<div class="muted small">Czasowo zamknięte</div>' if is_closed(a) else ""
        rows.append(f"""<tr id="{a['slug']}"><th scope="row">{link(a)}{note}<div class="muted small">sprawdzono {a['checked']}</div></th>
<td>{hours}</td><td>{tickets}</td><td>{escape(free_cell(a))}</td></tr>""")

    monday = [a for a in mus if open_monday(a, info[a["slug"]])]
    monday_html = "".join(f"<li>{link(a)}</li>" for a in monday)
    free_by_day = []
    for day in DAYS:
        names = [a for a in mus if day in info[a["slug"]]["free_days"]]
        if names:
            free_by_day.append(f"<li><strong>{LABEL[day].capitalize()}:</strong> " + ", ".join(link(a) for a in names) + "</li>")
    always = [a for a in mus if info[a["slug"]]["free_always"]]
    if always:
        free_by_day.append("<li><strong>Zawsze bezpłatnie:</strong> " + ", ".join(link(a) for a in always) + "</li>")
    pkt = [a for a in mus if any("poznańską kartą turystyczną" in l.lower() and "bezpłatn" in x.lower() for l, x in a["tickets"])]
    pkt_html = ", ".join(link(a) for a in pkt)

    body = f"""
<header class="wrap page-head">
  <p class="kicker">Zestawienie</p>
  <h1>Muzea w Poznaniu: godziny, ceny i dni bezpłatne</h1>
  <p class="lead">{len(mus)} muzeów z przewodnika w jednej tabeli: kiedy są otwarte, ile kosztuje bilet i w które dni wstęp jest wolny. Dane pochodzą z kart atrakcji, więc każdą liczbę możesz sprawdzić w źródle (<a href="jak-weryfikujemy.html">jak weryfikujemy informacje</a>).</p>
  <nav class="toc" aria-label="Spis treści">
    <a href="#tabela">Tabela</a><a href="#poniedzialek">Otwarte w poniedziałek</a><a href="#bezplatnie">Wstęp wolny</a>
  </nav>
</header>

<div class="wrap prose">
<section id="poniedzialek">
  <h2>Otwarte w poniedziałek</h2>
  <p>W poniedziałek większość muzeów jest nieczynna. Poniżej tylko te, w których nasze źródła wprost podają, że w poniedziałek jest otwarte. Jeśli muzeum nie ma godzin dla poniedziałku w naszych danych, nie wpisujemy go na tę listę.</p>
  <ul>{monday_html}</ul>
</section>

<section id="bezplatnie">
  <h2>Wstęp wolny według dni</h2>
  <ul>{"".join(free_by_day)}</ul>
  <p>Z Poznańską Kartą Turystyczną bezpłatnie: {pkt_html}.</p>
</section>

<section id="tabela">
  <h2>Wszystkie muzea</h2>
  <p>W kolejności alfabetycznej. Godziny i ceny są przepisane z kart atrakcji bez skracania, a przy nazwie widać datę, kiedy je ostatnio sprawdziliśmy.</p>
  <div class="table-wrap"><table class="grid compare">
  <thead><tr><th scope="col">Muzeum</th><th scope="col">Godziny</th><th scope="col">Bilety</th><th scope="col">Wstęp wolny</th></tr></thead>
  <tbody>
  {"".join(rows)}
  </tbody></table></div>
  <p class="muted small">Godziny i ceny zmieniają się. Przed wizytą potwierdź je na stronie muzeum (link na karcie atrakcji). Brak informacji w tabeli oznacza, że nie mamy jej z wiarygodnego źródła.</p>
</section>
</div>
"""
    return page("Muzea w Poznaniu: godziny otwarcia, ceny biletów i dni bezpłatne – Odkrywaj Poznań", body,
                desc=f"Zestawienie {len(mus)} muzeów w Poznaniu: godziny otwarcia, ceny biletów normalnych i ulgowych, dni wstępu wolnego i muzea otwarte w poniedziałek.",
                active="atrakcje")


def build_privacy():
    mail = f'<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>'
    ext = lambda url, text: f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Informacje prawne</p>
  <h1>Prywatność</h1>
  <p class="lead">Krótko: nie ma tu reklam, formularzy ani kont. Jedyne, o co prosimy, to zgoda na anonimowe statystyki odwiedzin w Google Analytics. Bez Twojej zgody strona nie zapisuje cookies i nie łączy się z Google.</p>
  <nav class="toc" aria-label="Spis treści">
    <a href="#kto">Kto prowadzi stronę</a><a href="#cookies">Cookies i statystyki</a><a href="#geolokalizacja">Geolokalizacja</a><a href="#hosting">Serwer</a>
    <a href="#zewnetrzne">Usługi zewnętrzne</a><a href="#prawa">Twoje prawa</a>
  </nav>
</header>

<div class="wrap prose">
<section id="kto">
  <h2>Kto prowadzi stronę</h2>
  <p>Przewodnik „Odkrywaj Poznań” (odkrywajpoznan.pl) to prywatna, niekomercyjna strona, niezwiązana z Urzędem Miasta Poznania. Administratorem danych ze statystyk opisanych niżej jest „Odkrywaj Poznań”. W sprawach strony i prywatności pisz na adres {mail}.</p>
</section>

<section id="cookies">
  <h2>Cookies i statystyki</h2>
  <p>Przy pierwszej wizycie pytamy, czy możemy liczyć odwiedziny w <strong>Google Analytics 4</strong>. Dzięki temu wiemy, które strony są czytane i co warto rozwijać. Oba przyciski, „Akceptuję” i „Odrzucam”, są równorzędne, a odmowa niczego nie blokuje.</p>
  <ul>
    <li><strong>Gdy odrzucisz albo nic nie wybierzesz:</strong> skrypt Google nie jest wczytywany, nie powstają żadne cookies i nic nie jest wysyłane do Google.</li>
    <li><strong>Gdy zaakceptujesz:</strong> przeglądarka pobiera skrypt z googletagmanager.com i wysyła do Google Analytics informacje o wizycie: otwierane strony, adres strony, z której przychodzisz, przybliżoną lokalizację (miasto, kraj ustalone z adresu IP, który Google Analytics 4 nie przechowuje), typ urządzenia, system i przeglądarkę, rozdzielczość ekranu oraz język. Google zapisuje cookies <code>_ga</code> i <code>_ga_S4K8EW3YGQ</code>, które pozwalają odróżnić powracającą przeglądarkę od nowej. Wygasają po 2 latach.</li>
  </ul>
  <p>Nie używamy funkcji reklamowych Google ani sygnałów Google (zgody na nie są wyłączone), nie łączymy statystyk z innymi danymi i nie próbujemy ustalić, kim jesteś. Widzimy tylko zbiorcze raporty.</p>
  <p><strong>Podstawa prawna:</strong> Twoja zgoda (art. 6 ust. 1 lit. a RODO, art. 399 Prawa komunikacji elektronicznej). Możesz ją w każdej chwili cofnąć przyciskiem <button type="button" class="linkish" data-consent-open>Ustawienia cookies</button> (jest też w stopce każdej strony). Po cofnięciu zgody usuwamy cookies Google Analytics z Twojej przeglądarki. Cofnięcie nie wpływa na zgodność z prawem wcześniejszego zbierania statystyk.</p>
  <p><strong>Odbiorca i przekazanie poza EOG:</strong> dane trafiają do Google Ireland Limited. Mogą być przetwarzane także przez Google LLC w USA, które uczestniczy w programie EU-U.S. Data Privacy Framework (decyzja Komisji Europejskiej stwierdzająca odpowiedni stopień ochrony). Zasady: {ext("https://policies.google.com/privacy?hl=pl", "polityka prywatności Google")}, {ext("https://business.safety.google/adsprocessorterms/", "warunki przetwarzania danych")}.</p>
  <p><strong>Jak długo:</strong> dane o wizytach są przechowywane w Google Analytics przez 14 miesięcy, potem Google je usuwa.</p>
  <p><strong>Twój wybór</strong> zapisujemy w pamięci przeglądarki (localStorage, wpis <code>op-zgoda-statystyki</code>), żeby nie pytać na każdej stronie. To nie jest cookie, nie jest nigdzie wysyłane i znika po wyczyszczeniu danych strony w przeglądarce.</p>
  <p>Jeśli dodasz stronę do ekranu głównego telefonu, przeglądarka może przechowywać jej pliki w zwykłej pamięci podręcznej. Nie są to dane o Tobie.</p>
</section>

<section id="geolokalizacja">
  <h2>Geolokalizacja</h2>
  <p>Na stronie Mapa masz przycisk <strong>„Gdzie jestem"</strong>. Jeśli go klikniesz, przeglądarka poprosi Cię o pozwolenie na dostęp do Twojej lokalizacji GPS. To zupełnie opcjonalne.</p>
  <ul>
    <li><strong>Jeśli na przycisk nie klikniesz:</strong> żadna lokalizacja nie jest gromadzona. Mapę możesz przeglądać normalnie, klikając nazwy i filtrując atrakcje.</li>
    <li><strong>Jeśli wyrażysz zgodę:</strong> przeglądarce pozwolisz użyć GPS (lub przybliżonego położenia z WiFi/sieci komórkowej). Informacja o Twojej lokalizacji <strong>zostaje tylko w Twojej przeglądarce</strong> — nigdzie nam nie jest wysyłana. Używamy jej wyłącznie do:
      <ul>
        <li>wyświetlenia Twojego markera na mapie,</li>
        <li>sortowania listy atrakcji od najbliższych, z odległościami w kilometrach.</li>
      </ul>
    </li>
    <li><strong>Jeśli odmówisz:</strong> przycisk pozostaje dostępny do następnej próby. Możesz odwołać zgodę w ustawieniach przeglądarki.</li>
  </ul>
  <p><strong>Obsługa:</strong> geolokalizacja pracuje z przeglądarkami obsługującymi <code>navigator.geolocation</code> (Chrome, Firefox, Safari, Edge). Dane nie trafią nigdzie poza Twoją przeglądarkę.</p>
</section>

<section id="hosting">
  <h2>Serwer</h2>
  <p>Strona jest udostępniana przez usługę GitHub Pages (GitHub, Inc.). Jak każdy serwer, GitHub zapisuje w dziennikach techniczne dane o połączeniu, m.in. adres IP, datę i godzinę oraz adres otwieranej strony, w celu zapewnienia bezpieczeństwa i działania usługi. Nie mamy dostępu do tych dzienników. Zasady: {ext("https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement", "polityka prywatności GitHub")}.</p>
  <p>Domena jest zarejestrowana w OVH.</p>
</section>

<section id="zewnetrzne">
  <h2>Usługi zewnętrzne</h2>
  <p>Czcionki, zdjęcia i skrypty strony są na naszym serwerze. Wyjątki to:</p>
  <ul>
    <li><strong>Google Analytics</strong> (googletagmanager.com, google-analytics.com), wyłącznie po Twojej zgodzie, opisane wyżej;</li>
    <li><strong>mapa atrakcji</strong> (tylko strona Mapa): jej podkład pochodzi z serwerów OpenStreetMap, więc przeglądarka przekazuje im adres IP ({ext("https://osmfoundation.org/wiki/Privacy_Policy", "zasady OSMF")}).</li>
  </ul>
  <p>Linki „Pokaż na mapie” i „Trasa” otwierają Mapy Google, a pozostałe linki prowadzą do stron muzeów, organizatorów i innych serwisów. Po przejściu na nie obowiązują ich własne zasady prywatności.</p>
</section>

<section id="prawa">
  <h2>Twoje prawa</h2>
  <p>W zakresie statystyk masz prawo do cofnięcia zgody, dostępu do danych, ich sprostowania, usunięcia, ograniczenia przetwarzania i przeniesienia. Statystyki nie pozwalają nam jednak ustalić, które dane dotyczą właśnie Ciebie, więc najprostszym sposobem jest cofnięcie zgody, które usuwa identyfikator z Twojej przeglądarki. W innych sprawach napisz na {mail}.</p>
  <p>Wobec GitHub, OpenStreetMap i Google masz te same prawa na podstawie RODO. Możesz też złożyć skargę do Prezesa Urzędu Ochrony Danych Osobowych ({ext("https://uodo.gov.pl", "uodo.gov.pl")}).</p>
  <p class="muted">Ostatnia aktualizacja: {PRIVACY_UPDATED}.</p>
</section>
</div>
"""
    return page("Prywatność – Odkrywaj Poznań", body, desc="Zasady prywatności przewodnika Odkrywaj Poznań: statystyki Google Analytics tylko za zgodą, cookies, serwer i usługi zewnętrzne.")


def build_404():
    """GitHub Pages pokazuje 404.html pod każdym błędnym adresem, także w podkatalogach,
    dlatego wszystkie ścieżki są od katalogu głównego (prefiks „/”)."""
    tiles = "".join(
        f'<li><a href="/atrakcje.html#kat-{k}"><h3>{escape(n)}</h3><p>{escape(d)}</p></a></li>'
        for k, n, d in CATEGORIES)
    body = f"""
<section class="wrap page-head nf">
  <p class="kicker">Błąd 404</p>
  <h1>Nie ma takiej strony</h1>
  <p class="lead">Adres mógł się zmienić albo zawiera literówkę. Wyszukaj atrakcję albo zacznij od jednej z poniższych stron.</p>
  <form class="search nf-search" role="search" action="/atrakcje.html" method="get">
    <label for="q-404" class="sr">Szukaj atrakcji</label>
    {icon('search')}<input id="q-404" name="q" type="search" placeholder="Szukaj: koziołki, zoo, muzeum…" autocomplete="off" enterkeyhint="search">
  </form>
  <p class="actions nf-actions">
    <a class="btn btn-gold" href="/">Strona główna {icon('arrow')}</a>
    <a class="btn btn-ghost" href="/atrakcje.html">Wszystkie atrakcje</a>
    <a class="btn btn-ghost" href="/mapa.html">{icon('pin')} Mapa</a>
    <a class="btn btn-ghost" href="/plany.html">Plany zwiedzania</a>
  </p>
</section>
<section class="wrap section">
  <div class="section-head"><p class="kicker">Kategorie</p><h2>Czego szukasz?</h2></div>
  <ul class="plan-grid">{tiles}</ul>
</section>
<script>
  // Podpowiedź w wyszukiwarce z ostatniej części błędnego adresu, np. /atrakcje/stary-rynekk -> „stary rynekk”.
  (function () {{
    var last = decodeURIComponent(location.pathname.split('/').filter(Boolean).pop() || '');
    var words = last.replace(/\\.html?$/, '').replace(/[-_]+/g, ' ').trim();
    if (words) document.getElementById('q-404').value = words;
  }})();
</script>
"""
    return page("Nie ma takiej strony – Odkrywaj Poznań", body, prefix="/",
                desc="Nie znaleziono strony w przewodniku Odkrywaj Poznań.",
                head='<meta name="robots" content="noindex">\n')


SITE_URL = "https://odkrywajpoznan.pl/"
LINK_RE = re.compile(r'\b(href|action)="([^"]*)"')


def clean_links(html):
    """Adresy wewnętrzne bez .html (GitHub Pages podaje /plany jako plany.html).
    Linki zewnętrzne, kotwice i pliki inne niż HTML zostają bez zmian."""
    def fix(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"^(https?:|//|mailto:|tel:|#|data:)", url):
            return m.group(0)
        path, rest = re.match(r"^([^#?]*)(.*)$", url).groups()
        if path.endswith("index.html"):
            path = path[:-len("index.html")] or "./"
        elif path.endswith(".html"):
            path = path[:-len(".html")]
        else:
            return m.group(0)
        return f'{attr}="{path}{rest}"'
    return LINK_RE.sub(fix, html)


OG_W, OG_H = 1200, 630


def og_image(name):
    """Zdjęcie 1200×630 do podglądu linku (Open Graph); tworzone z img/<name>.jpg przy pierwszym buildzie."""
    out_dir = os.path.join(ROOT, "img", "og")
    dst = os.path.join(out_dir, name + ".jpg")
    if not os.path.exists(dst):
        from PIL import Image
        os.makedirs(out_dir, exist_ok=True)
        im = Image.open(os.path.join(ROOT, "img", name + ".jpg")).convert("RGB")
        k = max(OG_W / im.width, OG_H / im.height)
        im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
        x, y = (im.width - OG_W) // 2, (im.height - OG_H) // 2
        im.crop((x, y, x + OG_W, y + OG_H)).save(dst, "JPEG", quality=70, optimize=True, progressive=True)
    return f"{SITE_URL}img/og/{name}.jpg"


def og_tags(html, url, image, alt):
    """Open Graph + karta Twittera; tytuł i opis bierzemy z gotowej strony, żeby były identyczne jak w Google."""
    title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)
    m = re.search(r'<meta name="description" content="(.*?)">', html, re.S)
    desc = m.group(1) if m else ""
    tags = [("og:type", "website"), ("og:locale", "pl_PL"), ("og:site_name", "Odkrywaj Poznań"),
            ("og:title", title), ("og:description", desc), ("og:url", url),
            ("og:image", image), ("og:image:width", str(OG_W)), ("og:image:height", str(OG_H)),
            ("og:image:alt", escape(alt))]
    out = "".join(f'<meta property="{k}" content="{v}">\n' for k, v in tags if v)
    out += '<meta name="twitter:card" content="summary_large_image">\n'
    return out


def main():
    os.makedirs(os.path.join(ROOT, "atrakcje"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    for name in ("style.css", "site.js", "map.js", "leaflet.css", "leaflet.js"):
        shutil.copy(os.path.join(ROOT, "src", name), os.path.join(ROOT, "assets", name))
    out = {"index.html": build_index(), "informacje.html": build_info(), "plany.html": build_plans(),
           "kalendarz.html": build_calendar(), "teatry.html": build_theatres(), "atrakcje.html": build_attractions(),
           "prywatnosc.html": build_privacy(), "jak-weryfikujemy.html": build_method(), "muzea.html": build_museums(),
           "o-poznaniu.html": build_about(), "zdjecia.html": build_credits(), "mapa.html": build_map()}
    for i, a in enumerate(ATTRACTIONS):
        out[f"atrakcje/{a['slug']}.html"] = build_attraction(a, i)
    urls = []
    by_slug = {a["slug"]: a for a in ATTRACTIONS}
    for path, html in out.items():
        # Adres kanoniczny bez .html: te same strony działają też pod /x.html, więc wskazujemy Google właściwy.
        clean = "" if path == "index.html" else path[:-len(".html")]
        urls.append(SITE_URL + clean)
        att = by_slug.get(path[len("atrakcje/"):-len(".html")]) if path.startswith("atrakcje/") else None
        if att and att.get("img"):
            og_img, og_alt = og_image(att["img"]), att["img_alt"]
        else:
            og_img, og_alt = og_image("hero-rynek"), "Stary Rynek w Poznaniu"
        html = html.replace("</title>\n", f'</title>\n<link rel="canonical" href="{SITE_URL}{clean}">\n'
                            + og_tags(html, SITE_URL + clean, og_img, og_alt), 1)
        with open(os.path.join(ROOT, path), "w", encoding="utf-8", newline="\n") as f:
            f.write(clean_links(html))
    # Strona błędu: bez canonical i poza mapą strony.
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(clean_links(build_404()))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "".join(f"  <url><loc>{escape(u)}</loc></url>\n" for u in urls) + "</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n")
    missing =[a["img"] for a in ATTRACTIONS if a.get("img") and not os.path.exists(os.path.join(ROOT, "img", a["img"] + ".jpg"))]
    print(f"Zapisano {len(out)} stron. Brakujące zdjęcia: {missing or 'brak'}")


if __name__ == "__main__":
    main()
