# -*- coding: utf-8 -*-
"""Angielska wersja przewodnika: strony pod /en/ (indeks) i /en/attractions/<slug> (atrakcje).
Wywoływane z build.py (main). Fakty (adres, współrzędne, zdjęcia, źródła) bierzemy z polskich danych,
a teksty z data_en.py. Strony PL i EN wskazują się nawzajem przez hreflang (robi to build.main)."""
import datetime
import json
from html import escape

import seo
from build import (ATTRACTIONS, BY_SLUG, COORDS, PLANS, distance_km, CONTACT_EMAIL, COPYRIGHT_YEAR, CREDITS, FONTS, GA_ID, SITE_URL,
                   asset_v, icon, maps_url, media_html, route_url)
from data_en import CATEGORIES_EN, EN
from plans_en import PLANS_EN

EN_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]


def en_date(dmy):
    """'09.10.2026' -> '9 October 2026'."""
    d, m, y = dmy.split(".")
    return f"{int(d)} {EN_MONTHS[int(m) - 1]} {y}"


def merged(slug):
    """Polska atrakcja z nadpisanymi polami tekstowymi z tłumaczenia."""
    a = dict(BY_SLUG[slug])
    e = EN[slug]
    a.update(name=e["name"], img_alt=e["img_alt"], short=e["short"], badge=e["badge"], lead=e["lead"],
             sections=e["sections"], hours=e["hours"], tickets=e["tickets"])
    if e.get("address"):
        a["address"] = e["address"]
    a["status"] = ((BY_SLUG[slug]["status"][0], e["status"]) if BY_SLUG[slug]["status"] and e.get("status") else None)
    return a


def translated():
    """Atrakcje z tłumaczeniem, w kolejności polskiego przewodnika."""
    return [a["slug"] for a in ATTRACTIONS if a["slug"] in EN]


def page_en(title, body, prefix="", desc="", head="", alt="", active=""):
    """Szablon strony angielskiej. prefix = ścieżka do korzenia serwisu; alt = polski odpowiednik (od korzenia)."""
    cur = ' aria-current="page"' if active == "attractions" else ""
    cur_pr = ' aria-current="page"' if active == "practical" else ""
    cur_pl = ' aria-current="page"' if active == "plans" else ""
    return f"""<!DOCTYPE html>
<html lang="en">
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
<link rel="preload" href="{prefix}fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{prefix}fonts/playfair-display-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{prefix}fonts/inter-latin-ext.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{prefix}fonts/playfair-display-latin-ext.woff2" as="font" type="font/woff2" crossorigin>
{head}<link rel="stylesheet" href="{prefix}assets/style.css?v={asset_v("style.css")}">
</head>
<body>
<a class="skip" href="#tresc">Skip to content</a>
<header class="topbar">
  <div class="topbar-in">
    <a class="logo" href="{prefix}en/" aria-label="Odkrywaj Poznań – Discover Poznań, home"><img class="logo-mark" src="{prefix}img/logo-znak.svg" alt="" width="72" height="40"><img class="logo-word" src="{prefix}img/logo-napis.svg" alt="Odkrywaj Poznań" width="108" height="40"></a>
    <button type="button" class="menu-btn" aria-expanded="false" aria-controls="menu"><span class="menu-ico" aria-hidden="true"><span></span><span></span><span></span></span>Menu</button>
    <nav id="menu" aria-label="Main navigation">
      <ul>
        <li><a href="{prefix}en/"{cur}>Attractions</a></li>
        <li><a href="{prefix}en/plans.html"{cur_pl}>Itineraries</a></li>
        <li><a href="{prefix}en/practical.html"{cur_pr}>Practical</a></li>
        <li><a href="{prefix}{alt}" hreflang="pl" lang="pl">Polski</a></li>
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
      <p class="muted">An unofficial guide, not affiliated with the City of Poznań Office. Each attraction page shows the date its hours and prices were checked. Please confirm them with the venue before you visit.</p>
      <p class="muted footer-contact">Spotted a mistake or outdated information? Write to: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
    </div>
    <ul class="footer-links">
      <li><a href="{prefix}en/">All attractions (English)</a></li>
      <li><a href="{prefix}atrakcje.html" hreflang="pl" lang="pl">Full guide in Polish</a></li>
      <li><a href="https://visitpoznan.pl/en/" target="_blank" rel="noopener">Visit Poznań (official portal)</a></li>
    </ul>
  </div>
  <div class="wrap footer-bar">
    <span class="footer-name">Odkrywaj Poznań</span>
    <ul class="footer-legal">
      <li><a href="{prefix}en/privacy.html">Privacy</a></li>
      <li><button type="button" class="linkish" data-consent-open>Cookie settings</button></li>
      <li><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li>
    </ul>
    <span class="footer-copy">© {COPYRIGHT_YEAR} odkrywajpoznan.pl</span>
  </div>
</footer>
<div class="consent" role="region" aria-label="Analytics consent" data-ga="{GA_ID}" hidden>
  <p>We would like to count visits with Google Analytics to learn which parts of the guide are useful. This needs cookies, so we will switch statistics on only with your consent. <a href="{prefix}en/privacy.html#cookies">Details</a></p>
  <div class="consent-btns">
    <button type="button" class="btn btn-consent" data-consent="denied">Decline</button>
    <button type="button" class="btn btn-consent" data-consent="granted">Accept</button>
  </div>
</div>
<button type="button" class="to-top" aria-label="Back to top" hidden>{icon("up")}</button>
<script src="{prefix}assets/site.js?v={asset_v("site.js")}"></script>
</body>
</html>
"""


def credit_badge_en(slug, prefix):
    c = CREDITS[slug]
    txt = escape(f'Photo: {c["artist"]}' + (f', {c["license"]}' if c["license"] else ""))
    return (f'<a class="photo-credit" href="{prefix}zdjecia.html#foto-{slug}" data-credit="{txt}" '
            f'aria-label="{txt}. Show source">i</a>')


def kv_rows(rows):
    return "".join(f'<tr><th scope="row">{escape(k)}</th><td>{escape(v)}</td></tr>' for k, v in rows)


def card_en(a, prefix):
    badge_cls = "badge badge-closed" if a["status"] and a["status"][0] == "closed" else "badge"
    cat = CATEGORIES_EN[a["cat"]][0]
    return f"""<li class="card">
  <a href="{prefix}en/attractions/{a['slug']}.html">
    <div class="card-media">{media_html(a, prefix, lazy=True)}
      <span class="{badge_cls}">{escape(a['badge'])}</span></div>
    <div class="card-body">
      <p class="eyebrow">{escape(cat)}</p>
      <h3>{escape(a['name'])}</h3>
      <p>{escape(a['short'])}</p>
      <span class="more">Details {icon('arrow')}</span>
    </div>
  </a>
</li>"""


def seo_title(pl, name):
    if pl["cat"] == "wycieczki":
        tail = "opening hours, tickets, how to get there from Poznań"
    elif pl["cat"] == "pomniki":
        tail = "history and location"
    elif pl["cat"] == "koscioly":
        tail = "history, visiting, how to get there"
    elif seo._is_paid(pl):
        tail = "opening hours, tickets, how to get there"
    elif seo._always_open(pl):
        tail = "what to see, how to get there"
    else:
        tail = "opening hours, how to get there"
    return f"{name} – {tail} | Odkrywaj Poznań"


def seo_description(a, pl):
    e = EN[a["slug"]]
    if e.get("desc"):
        return e["desc"]
    address = f"Address: {a['address']}."
    out = a["short"]
    return f"{out} {address}" if len(out) + len(address) + 1 <= seo.DESC_MAX else out


def json_ld(a, pl, cat_name, lat_lon):
    url = f"{SITE_URL}en/attractions/{a['slug']}"
    extra = seo.SLUG_TYPE.get(pl["slug"]) or seo.CAT_TYPE.get(pl["cat"])
    place = {"@context": "https://schema.org", "@type": ["TouristAttraction", extra] if extra else "TouristAttraction",
             "name": a["name"], "description": a["short"], "url": url, "inLanguage": "en", "address": seo._address(pl)}
    if pl.get("img"):
        place["image"] = f"{SITE_URL}img/{pl['img']}.jpg"
    if lat_lon:
        place["geo"] = {"@type": "GeoCoordinates", "latitude": lat_lon[0], "longitude": lat_lon[1]}
    if pl["phone"]:
        place["telephone"] = pl["phone"]
    if seo._is_free(pl):
        place["isAccessibleForFree"] = True
    elif seo._is_paid(pl):
        place["isAccessibleForFree"] = False
    hours = seo.opening_hours(pl)
    if hours:
        place["openingHoursSpecification"] = hours
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}en/"},
        {"@type": "ListItem", "position": 2, "name": cat_name, "item": f"{SITE_URL}en/"},
        {"@type": "ListItem", "position": 3, "name": a["name"], "item": url}]}
    return "".join('<script type="application/ld+json">\n'
                   + json.dumps(d, ensure_ascii=False, indent=1).replace("</", "<\\/") + "\n</script>\n"
                   for d in (place, crumbs))


def build_attraction_en(slug, idx, slugs):
    pl = BY_SLUG[slug]
    a = merged(slug)
    e = EN[slug]
    p = "../../"
    cat_name = CATEGORIES_EN[a["cat"]][0]
    status = ""
    if a["status"]:
        kind, text = a["status"]
        label = "Temporarily closed" if kind == "closed" else "Important before you go"
        status = (f'<div class="status status-{kind}" role="note">{icon("alert", "ico ico-lg")}<div>'
                  f'<p class="status-h">{label}</p><p>{escape(text)}</p></div></div>')
    sections = "".join(f"<section><h2>{escape(h)}</h2>{''.join(f'<p>{escape(t)}</p>' for t in ps)}</section>"
                       for h, ps in a["sections"])
    contact = ""
    if a["phone"]:
        contact += f'<p>{icon("phone")} <span class="sel">{escape(a["phone"])}</span></p>'
    contact += f'<p>{icon("globe")} <a href="{escape(a["www"][1])}" target="_blank" rel="noopener">{escape(a["www"][0])}</a></p>'
    sources = "".join(f'<li><a href="{escape(u)}" target="_blank" rel="noopener" hreflang="pl">{escape(t)}</a></li>'
                      for t, u in pl["sources"])
    see = ""
    for (_, target), label in zip(pl.get("see_also", []), e.get("see_also", [])):
        see += f'<li><a href="{p}{escape(target)}.html" hreflang="pl">{escape(label)}</a></li>'
    see_html = f'<section class="seealso"><h2>See also</h2><ul>{see}</ul></section>' if see else ""
    prev_s = slugs[idx - 1]
    next_s = slugs[(idx + 1) % len(slugs)]
    rest = [s for s in slugs if s != slug]
    more = ([s for s in rest if BY_SLUG[s]["cat"] == pl["cat"]] + [s for s in rest if BY_SLUG[s]["cat"] != pl["cat"]])[:3]
    others = "".join(card_en(merged(s), p) for s in more)
    from urllib.parse import quote
    report = (f"mailto:{CONTACT_EMAIL}?subject={quote('Correction: ' + a['name'])}"
              f"&body={quote(f'Page: {SITE_URL}en/attractions/{slug}' + chr(10) + chr(10) + 'What is outdated or wrong:' + chr(10))}")
    trip = ""
    if pl.get("trip") and e.get("getting"):
        t = pl["trip"]
        getting = "".join(f"<p><strong>{escape(k)}.</strong> {escape(v)}</p>" for k, v in e["getting"])
        trip = (f'<div class="panel"><h2>{icon("route")} Getting there from Poznań</h2><div class="trip-go">'
                f'<p class="trip-dist">About {distance_km(t["lat"], t["lon"])} km from the centre of Poznań as the crow flies.</p>'
                f'{getting}</div></div>')
    route_label = "Directions from Poznań Główny station" if pl.get("trip") else "Directions by public transport"
    body = f"""
<nav class="wrap crumbs" aria-label="Breadcrumbs">
  <a href="{p}en/">Home</a> <span aria-hidden="true">/</span>
  <span>{escape(cat_name)}</span> <span aria-hidden="true">/</span>
  <span aria-current="page">{escape(a['name'])}</span>
</nav>

<header class="wrap a-hero">
  <figure class="a-hero-img">
    {media_html(a, p, sizes="(max-width: 760px) 92vw, 640px", priority=True)}
    {credit_badge_en(a['credit'], p) if a.get("img") else ""}
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
    {see_html}
    <section class="sources">
      <h2>Sources (in Polish)</h2>
      <ul>{sources}</ul>
    </section>
  </article>

  <aside class="a-side" aria-label="Practical information">
    <div class="panel">
      <h2>{icon('pin')} Address</h2>
      <p class="sel">{escape(a['address'])}</p>
      <p class="links"><a href="{maps_url(pl)}" target="_blank" rel="noopener">Show on map</a>
      <a href="{route_url(pl)}" target="_blank" rel="noopener">{icon('route')} {route_label}</a></p>
    </div>
    {trip}
    <div class="panel">
      <h2>{icon('clock')} Opening hours</h2>
      <table class="kv"><tbody>{kv_rows(a['hours'])}</tbody></table>
    </div>
    <div class="panel">
      <h2>{icon('ticket')} Tickets</h2>
      <table class="kv"><tbody>{kv_rows(a['tickets'])}</tbody></table>
    </div>
    <div class="panel">
      <h2>Contact</h2>
      {contact}
    </div>
    <p class="checked">Checked {en_date(a['checked'])}. Hours and prices may change, so please confirm them on the venue's website before you visit.</p>
    <p class="report"><a href="{report}">{icon('alert')} Report outdated information</a></p>
  </aside>
</div>

<section class="wrap section">
  <div class="section-head"><h2>More to explore</h2></div>
  <ul class="cards">{others}</ul>
  <nav class="pager" aria-label="Previous and next attraction">
    <a href="{prev_s}.html">{icon('back')} {escape(EN[prev_s]['name'])}</a>
    <a href="{next_s}.html">{escape(EN[next_s]['name'])} {icon('arrow')}</a>
  </nav>
</section>
"""
    t = pl.get("trip")
    lat_lon = (t["lat"], t["lon"]) if t else (COORDS[slug]["lat"], COORDS[slug]["lon"])
    return page_en(seo_title(pl, a["name"]), body, prefix=p, desc=seo_description(a, pl), alt=f"atrakcje/{slug}.html",
                   active="attractions", head=json_ld(a, pl, cat_name, lat_lon))


def build_index_en(slugs):
    cards = "".join(card_en(merged(s), "../") for s in slugs)
    body = f"""
<section class="wrap section list-page">
  <div class="section-head">
    <p class="kicker">Visitor guide</p>
    <h1>Discover Poznań</h1>
    <p class="lead">An independent guide to the city's best sights, with opening hours, ticket prices and directions checked against official sources.</p>
    <p class="muted">The English edition is growing. The pages below are fully translated; the complete guide, with more than a hundred attractions, plans and practical information, is in Polish. <a href="../atrakcje.html" hreflang="pl" lang="pl">Open the Polish guide</a></p>
  </div>
  <p><a class="btn btn-ghost" href="plans.html">Sightseeing itineraries: 1, 2 and 3 days, with children, rainy day {icon('arrow')}</a>
  <a class="btn btn-ghost" href="practical.html">Practical information: getting here, tickets, parking, emergencies {icon('arrow')}</a></p>
  <ul class="cards">{cards}</ul>
</section>
"""
    return page_en("Discover Poznań – an independent visitor guide | Odkrywaj Poznań", body, prefix="../",
                   desc="Independent guide to Poznań: what to see, opening hours, ticket prices and how to get there, checked against official sources.",
                   alt="index.html", active="attractions")


# Strona PL → strona EN (do hreflang w build.main)
def build_privacy_en():
    import privacy_en
    return page_en("Privacy – Odkrywaj Poznań", privacy_en.body(en_date), prefix="../",
                   desc="Privacy of the Odkrywaj Poznań guide: Google Analytics statistics only with your consent, cookies, server and external services.",
                   alt="prywatnosc.html")


def build_practical_en():
    import practical_en
    from site_data import CHECKED
    return page_en("Practical information for visitors to Poznań | Odkrywaj Poznań", practical_en.body(en_date(CHECKED)),
                   prefix="../", alt="informacje.html", active="practical",
                   desc="Getting to Poznań from the airport and station, public transport tickets, the Tourist Card, luggage storage, parking, cycling, emergency numbers and medical help.")


def plan_stop_en(slug, when, hint):
    a = merged(slug)
    hours = "; ".join(f"{k}: {v}" for k, v in a["hours"][:2])
    link = f"attractions/{slug}.html"
    return f"""<li class="stop">
  <a class="stop-img" href="{link}" tabindex="-1" aria-hidden="true">{media_html(a, "../", lazy=True)}</a>
  <div>
    <p class="stop-when">{escape(when)}</p>
    <h3><a href="{link}">{escape(a['name'])}</a></h3>
    <p>{escape(hint)}</p>
    <p class="stop-hours">{icon('clock')} {escape(hours)}</p>
  </div>
</li>"""


def build_plans_en():
    from urllib.parse import quote_plus
    blocks, toc = [], []
    for pid, _title, _who, _intro, stops, _note in PLANS:
        e = PLANS_EN[pid]
        mode = "walking" if pid in ("jeden-dzien", "dzien-1", "dzien-2", "za-darmo") else "transit"
        pts = [quote_plus(f'{BY_SLUG[s]["name"]}, {BY_SLUG[s]["address"]}') for s, _, _ in stops]
        route = (f"https://www.google.com/maps/dir/?api=1&travelmode={mode}&origin={pts[0]}&destination={pts[-1]}"
                 + (f"&waypoints={'%7C'.join(pts[1:-1][:8])}" if len(pts) > 2 else ""))
        items = "".join(plan_stop_en(s, w, h) for (s, _, _), (w, h) in zip(stops, e["stops"]))
        blocks.append(f"""<section id="{pid}" class="plan-block">
  <div class="plan-head">
    <p class="kicker">{escape(e['who'])}</p>
    <h2>{escape(e['title'])}</h2>
    <p class="lead">{escape(e['intro'])}</p>
    <p><a class="btn btn-ghost btn-sm" href="{escape(route)}" target="_blank" rel="noopener">{icon('route')} Route in Google Maps</a></p>
  </div>
  <ol class="stops">{items}</ol>
  <p class="plan-note">{icon('alert')} {escape(e['note'])}</p>
</section>""")
        toc.append(f'<a href="#{pid}">{escape(e["title"].split(":")[0])}</a>')
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Planning your visit</p>
  <h1>Sightseeing itineraries</h1>
  <p class="lead">Ready-made routes for first-time visitors to Poznań. At each stop we give the opening hours, and full information is on the attraction's page.</p>
  <nav class="toc" aria-label="Choose an itinerary">{''.join(toc)}</nav>
</header>
<div class="wrap plans">{''.join(blocks)}</div>
"""
    return page_en("Sightseeing itineraries for Poznań: 1, 2 and 3 days | Odkrywaj Poznań", body, prefix="../", alt="plany.html", active="plans",
                   desc="Ready-made sightseeing itineraries for Poznań: 1, 2 and 3 days, with children, on a rainy day, in winter, for free and on Monday.")


def page_map():
    m = {"index.html": "en/index.html", "prywatnosc.html": "en/privacy.html", "informacje.html": "en/practical.html",
         "plany.html": "en/plans.html"}
    for s in translated():
        m[f"atrakcje/{s}.html"] = f"en/attractions/{s}.html"
    return m


def build_all():
    slugs = translated()
    out = {"en/index.html": build_index_en(slugs), "en/privacy.html": build_privacy_en(),
           "en/practical.html": build_practical_en(),
           "en/plans.html": build_plans_en()}
    for i, s in enumerate(slugs):
        out[f"en/attractions/{s}.html"] = build_attraction_en(s, i, slugs)
    return out
