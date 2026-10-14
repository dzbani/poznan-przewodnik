# -*- coding: utf-8 -*-
"""Angielska strona główna, lista atrakcji i mapa: lustrzane odbicie polskich stron (build.build_index,
build_attractions, build_map), ale tylko z atrakcjami, które mają tłumaczenie (data_en.EN).
Wywoływane z build_en.build_all."""
import datetime
import json
from html import escape

from build import (ATTRACTIONS, BY_SLUG, CAT_COLORS, CATEGORIES, COORDS, PLANS, CALENDAR, TOP10, UPCOMING_MAX, asset_v,
                   icon, is_closed, maps_url, route_url, srcset_attr, tags)
from build_en import (CAL_EN, EN, PLANS_EN, card_en, en_date, fmt_range_en, merged, page_en, translated)
from data_en import CATEGORIES_EN

QUICK = [("all", "Everything"), ("free", "Free"), ("kids", "For children"), ("indoor", "Indoors, for rainy days")]


def counts_by_cat():
    slugs = translated()
    return {k: [s for s in slugs if BY_SLUG[s]["cat"] == k] for k, _, _ in CATEGORIES}


def count_phrase(n):
    return "1 checked attraction" if n == 1 else f"{n} checked attractions"


def build_home_en():
    slugs = translated()
    by_cat = counts_by_cat()
    n_cats = sum(1 for v in by_cat.values() if v)
    cat_words = {4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}
    hero_srcset = srcset_attr("hero-rynek", "../", (800, 1280, 1920))

    tiles = []
    for k, _, _ in CATEGORIES:
        items = by_cat[k]
        if not items:
            continue
        cover = next(BY_SLUG[s] for s in items if BY_SLUG[s].get("img"))
        tiles.append(f"""<li><a class="tile" href="attractions.html#kat-{k}">
  <img src="../img/{cover['img']}.jpg" srcset="{srcset_attr(cover['img'], '../')}" sizes="(max-width: 700px) 46vw, 25vw" alt="" loading="lazy" decoding="async">
  <span class="tile-t">{escape(CATEGORIES_EN[k][0])}</span><span class="tile-n">{len(items)}</span></a></li>""")

    top = "".join(card_en(merged(s), "../", num=i) for i, s in enumerate(TOP10, 1))

    # Wydarzenia: wszystkie z datą; site.js ukrywa zakończone i pokazuje najbliższe UPCOMING_MAX.
    today = datetime.date.today().isoformat()
    dated = sorted((e for e in CALENDAR if e["dates"]), key=lambda e: e["dates"][0])
    shown, ev_items = 0, []
    for e in dated:
        t = CAL_EN[e["id"]]
        visible = e["dates"][1] >= today and shown < UPCOMING_MAX
        shown += visible
        ev_items.append(f"""<article class="event" data-end="{e['dates'][1]}"{'' if visible else ' hidden'}>
  <p class="event-date">{escape(fmt_range_en(*e['dates']))}</p>
  <h3><a href="calendar.html#{e['id']}">{escape(t['name'])}</a></h3>
  <p>{escape(t['desc'][0])}</p>
  <p class="muted">{icon('pin')} {escape(t['place'])}</p>
</article>""")

    closed = [s for s in slugs if EN[s].get("status")]
    closed_html = "".join(
        f'<li><a href="attractions/{s}.html">{escape(EN[s]["name"])}</a>: {escape(EN[s]["status"].split(". ")[0].rstrip("."))}.</li>' for s in closed)
    plans = "".join(f'<li><a href="plans.html#{pid}"><h3>{escape(PLANS_EN[pid]["title"])}</h3><p>{escape(PLANS_EN[pid]["who"])}</p></a></li>'
                    for pid, *_ in PLANS)

    body = f"""
<section class="hero hero-full">
  <img class="hero-bg" src="../img/hero-rynek.jpg" srcset="{hero_srcset}" sizes="100vw" width="2000" height="1500" alt="Colourful townhouses on the Old Market Square in Poznań" fetchpriority="high">
  <div class="wrap hero-in">
  <div class="hero-text">
    <p class="kicker">Visitor guide</p>
    <h1>Poznań for the first time</h1>
    <p class="lead">{count_phrase(len(slugs)).capitalize()} in {cat_words.get(n_cats, n_cats)} categories, with opening hours, ticket prices and directions. Plus ready-made itineraries and everything you need to know before you arrive.</p>
    <form class="search hero-search" role="search" action="attractions.html" method="get">
      <label for="q-hero" class="sr">Search attractions</label>
      {icon('search')}<input id="q-hero" name="q" type="search" placeholder="Search: goats, zoo, museum…" autocomplete="off" enterkeyhint="search">
    </form>
    <div class="actions">
      <a class="btn btn-gold" href="#top10">Where to start {icon('arrow')}</a>
      <a class="btn btn-ghost" href="plans.html">Itineraries</a>
      <a class="btn btn-ghost" href="practical.html">Practical information</a>
    </div>
  </div>
  </div>
<a class="hero-credit" href="photo-credits.html#foto-hero-rynek">Photo: .abyr</a>
</section>

<section class="wrap facts" aria-label="Key information">
  <div class="fact"><p class="fact-k">Tuesday</p><p>Free permanent exhibitions at the National Museum and the Archaeological Museum, among others. <a href="museums.html">Other free days</a></p></div>
  <div class="fact"><p class="fact-k">Monday</p><p>Most museums are closed. <a href="plans.html#poniedzialek">What to do on Monday</a></p></div>
  <div class="fact"><p class="fact-k">12:00</p><p>The goats butt heads every day on the town hall tower. Arrive a few minutes early.</p></div>
  <div class="fact"><p class="fact-k">PLN 18</p><p>A 24-hour ticket for trams and buses in zone A. You can buy it by card on the vehicle. <a href="practical.html#transport">Ticket prices</a></p></div>
</section>

<section id="top10" class="wrap section">
  <div class="section-head">
    <p class="kicker">First time in Poznań?</p>
    <h2>10 places to start with</h2>
    <p class="muted">The most important sights and the locals' favourite places. Most are in the centre, within walking distance.</p>
  </div>
  <ol class="cards top-list">{top}</ol>
</section>

<section class="wrap section" aria-labelledby="kat-h">
  <div class="section-head"><p class="kicker">Categories</p><h2 id="kat-h">What are you looking for?</h2></div>
  <ul class="tiles">{''.join(tiles)}</ul>
  <div class="home-browse">
    <p class="home-quick"><span class="muted">Quick:</span>
      <a class="qlink" href="attractions.html?f=free">Free</a>
      <a class="qlink" href="attractions.html?f=kids">For children</a>
      <a class="qlink" href="attractions.html?f=indoor">Indoors, for rainy days</a></p>
    <p class="home-all"><a class="btn btn-gold" href="attractions.html">All attractions ({len(slugs)}) {icon('arrow')}</a>
      <a class="btn btn-ghost" href="map.html">{icon('pin')} On the map</a></p>
  </div>
</section>

<section class="wrap" aria-labelledby="closed-h">
  <details class="notice-fold">
    <summary>{icon('alert', 'ico ico-lg')}<h2 id="closed-h">Temporarily closed or important before you visit</h2><span class="notice-n">{len(closed)}</span></summary>
    <ul>{closed_html}</ul>
  </details>
</section>

<section class="wrap section plan" aria-labelledby="plans-h">
  <div class="section-head"><p class="kicker">Ready-made routes</p><h2 id="plans-h">Itineraries</h2>
  <p class="muted">Routes for 1, 2 or 3 days, with children, for rainy days, for free and for Monday.</p></div>
  <ul class="plan-grid">{plans}</ul>
</section>

<section class="wrap section plan" aria-labelledby="before-h">
  <div class="section-head"><p class="kicker">Planning your visit</p><h2 id="before-h">Before you arrive</h2></div>
  <ul class="plan-grid">
    <li><a href="practical.html#arrival"><h3>Arriving</h3><p>From Ławica Airport, buses 148 and 159 run to the station every few minutes.</p></a></li>
    <li><a href="practical.html#transport"><h3>Public transport</h3><p>ZTM ticket prices and how to pay by card on a tram.</p></a></li>
    <li><a href="practical.html#card"><h3>Poznań Tourist Card</h3><p>Free entry to most museums, and discounts.</p></a></li>
    <li><a href="practical.html#info"><h3>Tourist information</h3><p>Points on the Old Market Square, Kolegiacki Square, at the airport and in the Gate of Poznań.</p></a></li>
    <li><a href="museums.html"><h3>Museums: days and hours</h3><p>When to go in for free, and when the museums are closed.</p></a></li>
    <li><a href="practical.html#health"><h3>Health</h3><p>Hospitals, night medical care, a dentist and pharmacies.</p></a></li>
    <li><a href="practical.html#toilets"><h3>Public toilets</h3><p>Where they are along tourist routes and their opening hours.</p></a></li>
    <li><a href="practical.html#parking"><h3>By car</h3><p>Paid parking zones, prices and Park&amp;Ride car parks.</p></a></li>
    <li><a href="about.html"><h3>About Poznań</h3><p>History, legends, dialect, food and weather.</p></a></li>
    <li><a href="theatres.html"><h3>Theatres and concerts</h3><p>Opera, philharmonic, dance and puppet theatre. What you can follow without Polish.</p></a></li>
  </ul>
</section>

<section id="events" class="wrap section">
  <div class="section-head"><p class="kicker">Calendar</p><h2>Upcoming events</h2></div>
  <div class="events" data-upcoming="{UPCOMING_MAX}">{''.join(ev_items)}</div>
  <p class="events-empty muted"{'' if shown == 0 else ' hidden'}>The nearest dates have not been announced yet. See in the calendar when events usually take place.</p>
  <p><a class="btn btn-ghost" href="calendar.html">Events calendar for the whole year {icon('arrow')}</a></p>
  <p class="muted small">The current cultural programme: <a href="https://kultura.poznan.pl/" target="_blank" rel="noopener">kultura.poznan.pl</a> (in Polish)</p>
</section>
"""
    preload = f'<link rel="preload" as="image" imagesrcset="{hero_srcset}" imagesizes="100vw" fetchpriority="high">\n'
    return page_en("Odkrywaj Poznań – a visitor guide to Poznań", body, prefix="../", alt="index.html", active="", head=preload,
                   desc="A guide for visitors: attractions of Poznań by category, itineraries, opening hours, ticket prices and practical information.")


def finder_parts_en():
    by_cat = counts_by_cat()
    tabs = ['<button type="button" class="tab" aria-pressed="true" data-filter="all">All</button>']
    tabs += [f'<button type="button" class="tab" aria-pressed="false" data-filter="{k}">{escape(CATEGORIES_EN[k][0])}</button>'
             for k, _, _ in CATEGORIES if by_cat[k]]
    quick = "".join(f'<button type="button" class="qf" aria-pressed="{str(k == "all").lower()}" data-quick="{k}">{escape(n)}</button>'
                    for k, n in QUICK)
    groups = []
    for k, _, _ in CATEGORIES:
        if not by_cat[k]:
            continue
        name, desc = CATEGORIES_EN[k]
        groups.append(f"""<section class="cat-group" data-cat="{k}" aria-labelledby="kat-{k}">
  <div class="cat-head"><h2 id="kat-{k}">{escape(name)}</h2><p>{escape(desc)}</p></div>
  <ul class="cards">{''.join(card_en(merged(s), "../") for s in by_cat[k])}</ul>
</section>""")
    return tabs, quick, groups


def build_attractions_en():
    tabs, quick, groups = finder_parts_en()
    body = f"""
<section id="atrakcje" class="wrap section list-page">
  <div class="section-head">
    <p class="kicker">All attractions</p>
    <h1>What to see in Poznań</h1>
    <p class="muted">Type a name or choose a category and a filter. Click an attraction to see the full description, hours, prices and directions.</p>
    <p class="map-cta"><a class="btn btn-ghost" href="map.html">{icon('pin')} See them all on the map</a></p>
  </div>
  <div class="finder">
    <div class="search">
      <label for="q" class="sr">Search attractions</label>
      {icon('search')}<input id="q" type="search" placeholder="Name, street or type of place" autocomplete="off" data-search-input>
    </div>
    <div class="quick" role="group" aria-label="Quick filters">{quick}</div>
    <div class="tabs" role="group" aria-label="Filter by category">{''.join(tabs)}</div>
    <p class="result" aria-live="polite"></p>
  </div>
  {''.join(groups)}
  <p class="empty" hidden>Nothing matches your search. Try another word or <button type="button" class="linkish" data-reset>show all attractions</button>.</p>
</section>
"""
    return page_en("Attractions in Poznań: sights, museums, churches, parks and day trips | Odkrywaj Poznań", body, prefix="../",
                   alt="atrakcje.html", active="attractions",
                   desc="Attractions of Poznań by category: sights, monuments, churches, museums, parks, family attractions and day trips. Search and filters.")


def build_map_en():
    slugs = translated()
    by_cat = counts_by_cat()
    cat_names = {k: CATEGORIES_EN[k][0] for k, _, _ in CATEGORIES}
    items, seen = [], {}
    for s in slugs:
        pl = BY_SLUG[s]
        a = merged(s)
        c = pl["trip"] if pl.get("trip") else COORDS[s]
        key = (round(c["lat"], 5), round(c["lon"], 5))
        n_same = seen.get(key, 0)
        seen[key] = n_same + 1
        items.append({"s": s, "n": a["name"], "c": pl["cat"], "lat": round(c["lat"] + 0.00012 * n_same, 6),
                      "lon": round(c["lon"] + 0.00009 * n_same, 6), "d": a["short"], "b": a["badge"], "img": pl.get("img"),
                      "t": tags(pl), "x": is_closed(pl), "ap": bool(c.get("approx")),
                      "gm": maps_url(pl), "rt": route_url(pl), "rf": bool(pl.get("trip"))})
    data = {"items": items, "cats": {k: {"n": cat_names[k], "col": CAT_COLORS[k]} for k in cat_names},
            "root": "../", "detail": "attractions/"}
    quick = "".join(f'<button type="button" class="qf" aria-pressed="{str(k == "all").lower()}" data-quick="{k}">{escape(n)}</button>'
                    for k, n in QUICK)
    quick += '<button type="button" id="locate-btn" class="qf locate-btn" aria-label="Where am I: show my location"><span class="locate-ico" aria-hidden="true">📍</span>Where am I</button>'
    tabs = ['<button type="button" class="tab" aria-pressed="true" data-filter="all">All</button>'] + [
        f'<button type="button" class="tab" aria-pressed="false" data-filter="{k}"><span class="dot" style="--dot:{CAT_COLORS[k]}"></span>{escape(cat_names[k])}</button>'
        for k, _, _ in CATEGORIES if by_cat[k]]
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    body = f"""
<header class="wrap page-head map-head">
  <p class="kicker">Map</p>
  <h1>Attractions on the map</h1>
  <p class="lead">{count_phrase(len(slugs)).capitalize()} on one map, including day trips outside the city.<span class="lead-more"> Click a point or a name in the list to see the description and go to the details.</span></p>
  <div class="finder map-finder">
    <div class="quick" role="group" aria-label="Quick filters">{quick}</div>
    <div class="tabs" role="group" aria-label="Filter by category">{''.join(tabs)}</div>
  </div>
</header>
<div class="wrap map-layout">
  <div id="map" class="map" role="region" aria-label="Map of Poznań attractions"></div>
  <aside class="map-side" aria-label="List of attractions on the map">
    <p class="result" id="map-count" aria-live="polite"></p>
    <ol class="map-list" id="map-items"></ol>
  </aside>
</div>
<p class="wrap map-note small muted">Map and the location of attractions: © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap contributors</a>, data under the ODbL licence. Points with a dashed outline have an approximate location. The buttons in a point's description open Google Maps with the attraction's location or a public-transport route.</p>
<script type="application/json" id="map-data">{js}</script>
"""
    return page_en("Map of Poznań attractions | Odkrywaj Poznań", body, prefix="../", alt="mapa.html", active="map",
                   desc="Poznań attractions from the guide on one map, with filters.",
                   head=f'<link rel="stylesheet" href="../assets/leaflet.css?v={asset_v("leaflet.css")}">\n',
                   scripts=f'<script src="../assets/leaflet.js?v={asset_v("leaflet.js")}"></script>\n'
                           f'<script src="../assets/map.js?v={asset_v("map.js")}"></script>\n')
