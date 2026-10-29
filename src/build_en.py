# -*- coding: utf-8 -*-
"""Angielska wersja przewodnika: strony pod /en/ (indeks) i /en/attractions/<slug> (atrakcje).
Wywoływane z build.py (main). Fakty (adres, współrzędne, zdjęcia, źródła) bierzemy z polskich danych,
a teksty z data_en.py. Strony PL i EN wskazują się nawzajem przez hreflang (robi to build.main)."""
import datetime
import json
import re
from html import escape

import seo
from build import (LINKS_CHECKED, CHECKED as SITE_CHECKED, ATTRACTIONS, BY_SLUG, COORDS, PLANS, CALENDAR, tags, CAL_CHECKED, THEATRES, THEATRES_CHECKED, VIEWPOINTS, HISTORY, CLIMATE, distance_km, CONTACT_EMAIL, COPYRIGHT_YEAR, CREDITS, FONTS, GA_ID, SITE_URL,
                   asset_v, icon, img_v, maps_url, media_html, quick_facts, route_url)
from data_en import CATEGORIES_EN, EN
from plans_en import PLANS_EN
from calendar_en import CAL_EN
import theatres_en
import museums_en
import viewpoints_en
import about_en
import method_en

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


def page_en(title, body, prefix="", desc="", head="", alt="", active="", scripts=""):
    """Szablon strony angielskiej. prefix = ścieżka do korzenia serwisu; alt = polski odpowiednik (od korzenia)."""
    cur = ' aria-current="page"' if active == "attractions" else ""
    cur_map = ' aria-current="page"' if active == "map" else ""
    cur_ab = ' aria-current="page"' if active == "about" else ""
    cur_pr = ' aria-current="page"' if active == "practical" else ""
    cur_pl = ' aria-current="page"' if active == "plans" else ""
    cur_cal = ' aria-current="page"' if active == "calendar" else ""
    cur_th = ' aria-current="page"' if active == "theatres" else ""
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
        <li><a href="{prefix}en/attractions.html"{cur}>Attractions</a></li>
        <li><a href="{prefix}en/map.html"{cur_map}>Map</a></li>
        <li><a href="{prefix}en/plans.html"{cur_pl}>Itineraries</a></li>
        <li><a href="{prefix}en/calendar.html"{cur_cal}>Events</a></li>
        <li><a href="{prefix}en/practical.html"{cur_pr}>Practical</a></li>
        <li><a href="{prefix}en/about.html"{cur_ab}>About Poznań</a></li>
        <li class="nav-extra"><a href="{prefix}en/theatres.html"{cur_th}>Theatres and concerts</a></li>
        <li class="nav-lang"><a href="{prefix}{alt}" hreflang="pl" lang="pl">Polski</a></li>
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
      <li><a href="{prefix}en/attractions.html">All attractions</a></li>
      <li><a href="{prefix}en/museums.html">Museums: hours and prices</a></li>
      <li><a href="{prefix}en/changes.html">What has changed</a></li>
      <li><a href="{prefix}en/viewpoints.html">Viewpoints in Poznań</a></li>
      <li><a href="{prefix}en/map.html">Map of attractions</a></li>
      <li><a href="{prefix}en/plans.html">Itineraries</a></li>
      <li><a href="{prefix}en/practical.html">Practical information</a></li>
      <li><a href="{prefix}en/about.html">About Poznań: history, legends, dialect</a></li>
      <li><a href="{prefix}en/calendar.html">Events calendar</a></li>
      <li><a href="{prefix}en/theatres.html">Theatres and concerts</a></li>
      <li><a href="{prefix}en/photo-credits.html">Photo credits</a></li>
      <li><a href="{prefix}en/how-we-verify.html">How we verify information</a></li>
      <li><a href="https://visitpoznan.pl/en/" target="_blank" rel="noopener">Visit Poznań (official portal)</a></li>
      <li><a href="https://daybyday.today/" target="_blank" rel="noopener">By the same author: daybyday.today</a></li>
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
{scripts}<script src="{prefix}assets/site.js?v={asset_v("site.js")}"></script>
</body>
</html>
"""


def credit_badge_en(slug, prefix):
    c = CREDITS[slug]
    lic = CREDIT_LICENSE_EN.get(c["license"], c["license"])
    txt = escape(f'Photo: {c["artist"]}' + (f', {lic}' if lic else ""))
    return (f'<a class="photo-credit" href="{prefix}en/photo-credits.html#foto-{slug}" data-credit="{txt}" '
            f'aria-label="{txt}. Show source">i</a>')


def kv_rows(rows):
    return "".join(f'<tr><th scope="row">{escape(k)}</th><td>{escape(v)}</td></tr>' for k, v in rows)


CHIP = {"free": "Free", "kids": "For children"}


def card_en(a, prefix, num=None):
    pl = BY_SLUG[a["slug"]]
    badge_cls = "badge badge-closed" if a["status"] and a["status"][0] == "closed" else "badge"
    cat = CATEGORIES_EN[a["cat"]][0]
    tg = tags(pl)
    words = " ".join([a["name"], pl["name"], a["short"], cat, a["address"], a["badge"]])
    num_html = f'<span class="num" aria-hidden="true">{num}</span>' if num else ""
    chips = "".join(f'<span class="chip chip-{t}">{CHIP[t]}</span>' for t in tg if t != "indoor")
    chips_html = f'<p class="chips">{chips}</p>' if chips else ""
    return f"""<li class="card" data-cat="{a['cat']}" data-tags="{' '.join(tg)}" data-words="{escape(words)}">
  <a href="{prefix}en/attractions/{a['slug']}.html">
    <div class="card-media">{media_html(a, prefix, lazy=True, no_photo="No photo")}
      <span class="{badge_cls}">{escape(a['badge'])}</span>{num_html}</div>
    <div class="card-body">
      <p class="eyebrow">{escape(cat)}</p>
      <h3>{escape(a['name'])}</h3>
      <p>{escape(a['short'])}</p>
      {chips_html}
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
    out = f"{name} – {tail} | Odkrywaj Poznań"
    # Długie tytuły skracamy etapami (Google ucina ok. 60 znaków): najpierw końcówkę, a gdy to za mało, także markę.
    for long, short in ((" from Poznań", ""), ("how to get there", "getting there"), ("opening hours", "hours")):
        if len(out) > 70:
            tail = tail.replace(long, short)
            out = f"{name} – {tail} | Odkrywaj Poznań"
    if len(out) > 80:
        out = f"{name} – {tail}"
    return out


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
        label = re.sub(r" \(in Polish\)$", "", label)
        tslug = target.split("/")[-1]
        if target == "punkty-widokowe":
            see += f'<li><a href="{p}en/viewpoints.html">{escape(label)}</a></li>'
        elif target.startswith("atrakcje/") and tslug in EN:
            see += f'<li><a href="{tslug}.html">{escape(label)}</a></li>'
        else:
            see += f'<li><a href="{p}{escape(target)}.html" hreflang="pl">{escape(label)} (in Polish)</a></li>'
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
    {media_html(a, p, sizes="(max-width: 760px) 92vw, 640px", priority=True, no_photo="No photo")}
    {credit_badge_en(a['credit'], p) if a.get("img") else ""}
  </figure>
  <div class="a-hero-text">
    <p class="kicker">{escape(cat_name)}</p>
    <h1>{escape(a['name'])}</h1>
    <p class="lead">{escape(a['lead'])}</p>
    {quick_facts(a, ("Hours", "Tickets", "see below", "Summary: opening hours and tickets"))}
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
    <div class="panel" id="hours">
      <h2>{icon('clock')} Opening hours</h2>
      <table class="kv"><tbody>{kv_rows(a['hours'])}</tbody></table>
    </div>
    <div class="panel" id="tickets">
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
  <a class="stop-img" href="{link}" tabindex="-1" aria-hidden="true">{media_html(a, "../", lazy=True, no_photo="No photo")}</a>
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


def fmt_range_en(start, end):
    """'2026-06-21', '2026-06-28' -> '21–28 June 2026'."""
    a, b = datetime.date.fromisoformat(start), datetime.date.fromisoformat(end)
    ma, mb = EN_MONTHS[a.month - 1], EN_MONTHS[b.month - 1]
    if a == b:
        return f"{a.day} {ma} {a.year}"
    if (a.year, a.month) == (b.year, b.month):
        return f"{a.day}–{b.day} {ma} {a.year}"
    if a.year == b.year:
        return f"{a.day} {ma} – {b.day} {mb} {a.year}"
    return f"{a.day} {ma} {a.year} – {b.day} {mb} {b.year}"


def cal_event_en(e):
    t = CAL_EN[e["id"]]
    if e["dates"]:
        badge = f'<p class="event-date">{escape(fmt_range_en(*e["dates"]))}</p>'
        end = f' data-end="{e["dates"][1]}"'
    else:
        badge = '<p class="event-date event-tba">Date to be announced</p>'
        end = ""
    desc = "".join(f"<p>{escape(p)}</p>" for p in t["desc"])
    note = f'<p class="cal-note">{icon("alert")} {escape(t["note"])}</p>' if t["note"] else ""
    src = "".join(f'<li><a href="{escape(u)}" target="_blank" rel="noopener" hreflang="pl">{escape(s)}</a></li>' for s, u in e["sources"])
    return f"""<article id="{e['id']}" class="event cal-event"{end}>
  <div class="cal-badges">{badge}<p class="event-past" hidden>Edition ended</p></div>
  <h3>{escape(t['name'])}</h3>
  <p class="cal-when">{icon('clock')} {escape(t['when'])}</p>
  <p class="muted">{icon('pin')} {escape(t['place'])}</p>
  {desc}
  {note}
  <p><a href="{escape(e['link'][1])}" target="_blank" rel="noopener">{icon('globe')} {escape(e['link'][0])}</a></p>
  <details class="sources"><summary>Sources (in Polish)</summary><ul>{src}</ul></details>
</article>"""


def build_calendar_en():
    months, toc = [], []
    for m in range(1, 13):
        evs = sorted((e for e in CALENDAR if e["month"] == m), key=lambda e: e["dates"][0] if e["dates"] else "9")
        if not evs:
            continue
        mid = f"m{m:02d}"
        toc.append(f'<a href="#{mid}">{EN_MONTHS[m - 1]}</a>')
        months.append(f"""<section id="{mid}" class="cal-month">
  <h2>{EN_MONTHS[m - 1]}</h2>
  <div class="events">{''.join(cal_event_en(e) for e in evs)}</div>
</section>""")
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Planning your visit</p>
  <h1>Events calendar</h1>
  <p class="lead">The most important annual festivals, fairs and events in Poznań, month by month. For each event we give the date of the nearest or latest edition. When the new date has not yet been announced, we say when the event usually takes place. The calendar starts with the current month.</p>
  <nav class="toc" aria-label="Choose a month">{''.join(toc)}</nav>
</header>
<div class="wrap cal">{''.join(months)}
  <p class="muted small">Dates checked {en_date(CAL_CHECKED)} on the organisers' websites. Please confirm them with the organiser before you travel. The city's current cultural programme: <a href="https://kultura.poznan.pl/" target="_blank" rel="noopener">kultura.poznan.pl</a> (in Polish). Permanent venues: <a href="theatres.html">theatres and concerts</a>.</p>
</div>
"""
    return page_en("Events in Poznań: festivals, fairs and holidays by month | Odkrywaj Poznań", body, prefix="../",
                   alt="kalendarz.html", active="calendar",
                   desc="Annual events in Poznań: Malta Festival, Ethno Port, Museums' Night, the St Martin Street Name Day, Christmas fairs, the marathon and more. Dates and venues.")


def venue_card_en(v):
    t = theatres_en.VENUES_EN[v["id"]]
    img = ""
    if v["img"]:
        img = (f'<figure class="venue-img"><img src="../img/{v["img"]}.jpg?v={img_v(v["img"])}" alt="" loading="lazy" decoding="async">'
               f'{credit_badge_en(v["img"], "../")}</figure>')
    lang = (f'<p class="venue-lang venue-lang-ok">{theatres_en.LANG_OK}</p>' if v["lang"]
            else f'<p class="venue-lang">{theatres_en.LANG_PL}</p>')
    desc = "".join(f"<p>{escape(p)}</p>" for p in t["desc"])
    links = "".join(f'<a href="{escape(u)}" target="_blank" rel="noopener">{icon("globe")} {escape(label)}</a>'
                    for (_, u), label in zip(v["links"], t["links"]))
    if v["attraction"]:
        slug = v["attraction"]
        if slug in EN:
            links += f'<a href="attractions/{slug}.html">{icon("arrow")} {escape(EN[slug]["name"])} in the guide</a>'
        else:
            links += f'<a href="../atrakcje/{slug}.html" hreflang="pl">{icon("arrow")} {escape(BY_SLUG[slug]["name"])} in the guide (in Polish)</a>'
    from urllib.parse import quote_plus
    maps = "https://www.google.com/maps/search/?api=1&query=" + quote_plus(f'{v["name"]}, {v["address"]}')
    return f"""<article id="{v['id']}" class="venue">
  {img}
  <div class="venue-body">
    <p class="kicker">{escape(t['kind'])}</p>
    <h2>{escape(t['name'])}</h2>
    {lang}
    {desc}
    <p class="muted">{icon('pin')} <a href="{maps}" target="_blank" rel="noopener">{escape(v['address'])}</a></p>
    <p class="venue-links">{links}</p>
  </div>
</article>"""


def build_theatres_en():
    from data_theatres import THEATRE_SOURCES
    toc = "".join(f'<a href="#{v["id"]}">{escape(theatres_en.VENUES_EN[v["id"]]["name"].split(" (")[0])}</a>' for v in THEATRES)
    src = "".join(f'<li><a href="{escape(u)}" target="_blank" rel="noopener" hreflang="pl">{escape(t)}</a></li>' for t, u in THEATRE_SOURCES)
    more = theatres_en.MORE
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Culture</p>
  <h1>Theatres and concerts</h1>
  <p class="lead">{escape(theatres_en.INTRO)}</p>
  <nav class="toc" aria-label="Choose a venue">{toc}</nav>
</header>
<div class="wrap venues">
  {''.join(venue_card_en(v) for v in THEATRES)}
  <aside class="panel venue-more">
    <h2>Good to know</h2>
    <p>{escape(more[0])}</p>
    <p>Concerts, theatre stages and festivals also operate at the <a href="attractions/zamek-cesarski.html">Zamek Culture Centre (Imperial Castle)</a>. The annual festivals, including Malta Festival and Ethno Port, are in the <a href="calendar.html">events calendar</a>.</p>
  </aside>
  <section class="sources">
    <h2>Sources (in Polish)</h2>
    <ul>{src}</ul>
    <p class="muted small">Checked {en_date(THEATRES_CHECKED)}.</p>
  </section>
</div>
"""
    return page_en("Theatres and concerts in Poznań: opera, philharmonic, drama and dance | Odkrywaj Poznań", body, prefix="../",
                   alt="teatry.html", active="theatres",
                   desc="Theatres and concert halls in Poznań: the Grand Theatre (Opera), Philharmonic, Teatr Polski, Teatr Nowy and more. Addresses, box offices, repertoire.")


def build_museums_en():
    from museums_table import derive, open_monday, sort_key, DAYS, LABEL, is_museum
    from build import is_closed

    def en_of(a):
        if a["slug"] in EN:
            e = EN[a["slug"]]
            return e["name"], e["hours"], e["tickets"]
        m = museums_en.MUSEUMS_EN[a["slug"]]
        return m["name"], m["hours"], m["tickets"]

    mus = sorted((a for a in ATTRACTIONS if is_museum(a)), key=lambda a: sort_key(en_of(a)[0]))
    info = {a["slug"]: derive(a) for a in mus}

    def link(a):
        name = escape(en_of(a)[0])
        if a["slug"] in EN:
            return f'<a href="attractions/{a["slug"]}.html">{name}</a>'
        return f'<a href="../atrakcje/{a["slug"]}.html" hreflang="pl">{name}</a> <span class="muted small">(page in Polish)</span>'

    def free_cell(a):
        d = info[a["slug"]]
        if d["free_always"]:
            return "always"
        return ", ".join(museums_en.DAY_EN[x] for x in d["free_days"]) or "—"

    rows = []
    for a in mus:
        name, hours_en, tickets_en = en_of(a)
        hours = "".join(f'<div><span class="muted">{escape(l)}:</span> {escape(x)}</div>' for l, x in hours_en)
        tick = [(le, xe) for (lp, xp), (le, xe) in zip(a["tickets"], tickets_en)
                if not ("wstęp wolny" in xp.lower() or lp.lower() in LABEL.values())]
        tickets = "".join(f'<div><span class="muted">{escape(l)}:</span> {escape(x)}</div>' for l, x in tick) or "—"
        note = '<div class="muted small">Temporarily closed</div>' if is_closed(a) else ""
        rows.append(f"""<tr id="{a['slug']}"><th scope="row">{link(a)}{note}<div class="muted small">checked {en_date(a['checked'])}</div></th>
<td data-label="Hours">{hours}</td><td data-label="Tickets">{tickets}</td><td data-label="Free admission">{escape(free_cell(a))}</td></tr>""")

    monday_html = "".join(f"<li>{link(a)}</li>" for a in mus if open_monday(a, info[a["slug"]]))
    free_by_day = []
    for day in DAYS:
        names = [a for a in mus if day in info[a["slug"]]["free_days"]]
        if names:
            free_by_day.append(f"<li><strong>{museums_en.DAY_EN[day]}:</strong> " + ", ".join(link(a) for a in names) + "</li>")
    always = [a for a in mus if info[a["slug"]]["free_always"]]
    if always:
        free_by_day.append("<li><strong>Always free:</strong> " + ", ".join(link(a) for a in always) + "</li>")
    pkt = [a for a in mus if any("poznańską kartą turystyczną" in l.lower() and "bezpłatn" in x.lower() for l, x in a["tickets"])]
    pkt_html = ", ".join(link(a) for a in pkt)

    body = f"""
<header class="wrap page-head">
  <p class="kicker">Overview</p>
  <h1>Museums in Poznań: opening hours, prices and free days</h1>
  <p class="lead">{len(mus)} museums from the guide in one table: when they are open, how much a ticket costs and on which days admission is free. The data comes from the attraction pages, so you can check every figure at its source (<a href="how-we-verify.html">how we verify information</a>).</p>
  <nav class="toc" aria-label="Contents">
    <a href="#table">Table</a><a href="#monday">Open on Monday</a><a href="#free">Free admission</a>
  </nav>
</header>

<div class="wrap prose">
<section id="monday">
  <h2>Open on Monday</h2>
  <p>On Mondays most museums are closed. Below are only those where our sources state explicitly that they are open on Mondays. If a museum has no Monday hours in our data, we do not put it on this list.</p>
  <ul>{monday_html}</ul>
</section>

<section id="free">
  <h2>Free admission by day</h2>
  <ul>{"".join(free_by_day)}</ul>
  <p>Free with the Poznań Tourist Card: {pkt_html}.</p>
</section>

<section id="table">
  <h2>All museums</h2>
  <p>In alphabetical order. Hours and prices are copied from the attraction pages without shortening, and next to each name you can see the date we last checked them.</p>
  <div class="table-wrap compare-wrap"><table class="grid compare">
  <thead><tr><th scope="col">Museum</th><th scope="col">Hours</th><th scope="col">Tickets</th><th scope="col">Free admission</th></tr></thead>
  <tbody>
  {"".join(rows)}
  </tbody></table></div>
  <p class="muted small">Hours and prices change. Before your visit, confirm them on the museum's website (link on the attraction page). A dash in the table means that we do not have the information from a reliable source.</p>
</section>
</div>
"""
    return page_en("Museums in Poznań: opening hours, ticket prices and free days | Odkrywaj Poznań", body, prefix="../",
                   alt="muzea.html", active="attractions",
                   desc=f"Overview of {len(mus)} museums in Poznań: opening hours, standard and reduced ticket prices, free-admission days and museums open on Monday.")


def build_viewpoints_en():
    def link(slug):
        return f'<a href="attractions/{slug}.html">{escape(EN[slug]["name"])}</a>'

    sections = []
    for slug, _what, _ in VIEWPOINTS:
        sections.append(f"""<section id="{slug}">
  <h2>{link(slug)}</h2>
  <p>{escape(viewpoints_en.WHAT[slug])}</p>
  <p class="muted small">Checked {en_date(BY_SLUG[slug]['checked'])}. <a href="attractions/{slug}.html">Hours, prices and directions</a></p>
</section>""")
    free = [s for s, _, pr in VIEWPOINTS if pr == "bezpłatny"]
    paid = [s for s, _, pr in VIEWPOINTS if pr == "płatny"]
    count_word = viewpoints_en.COUNT_WORD.get(len(VIEWPOINTS), str(len(VIEWPOINTS)))
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Overview</p>
  <h1>Viewpoints in Poznań: towers and terraces with a view of the city</h1>
  <p class="lead">{count_word} places from which you can see Poznań and its surroundings from above: a terrace and towers in the city, and two free towers at Szachty and in Czmoniec. Each place has a page with hours, prices and directions (<a href="how-we-verify.html">how we verify information</a>).</p>
</header>

<div class="wrap prose">
<section>
  <h2>Which one to choose</h2>
  <ul>
    <li><strong>In the city, with a ticket:</strong> {", ".join(link(s) for s in paid)}.</li>
    <li><strong>Free:</strong> {", ".join(link(s) for s in free)}.</li>
  </ul>
  <p class="muted small">Hours and prices change, so check them on the place's page and on the venue's website before your visit.</p>
</section>
{"".join(sections)}
</div>
"""
    return page_en("Viewpoints in Poznań: towers and terraces with a view of the city | Odkrywaj Poznań", body, prefix="../",
                   alt="punkty-widokowe.html", active="attractions",
                   desc="Where to see Poznań from above: the Collegium Altum terrace, the Royal Castle tower (43 m), the archcathedral tower and the free towers at Szachty and in Czmoniec.")


def build_about_en():
    L = about_en.LABELS

    def more(slug):
        if slug in EN:
            return f' <a href="attractions/{slug}.html">{escape(EN[slug]["name"])} →</a>'
        return f' <a href="../atrakcje/{slug}.html" hreflang="pl">{escape(BY_SLUG[slug]["name"])} (in Polish) →</a>'

    timeline = "".join(
        f'<li><p class="tl-date">{escape(d)}</p><p>{escape(t)}{more(pl[2]) if len(pl) > 2 else ""}</p></li>'
        for (d, t), pl in zip(about_en.HISTORY, HISTORY))
    legends = "".join(f'<article class="legend"><h3>{escape(t)}</h3><p>{escape(x)}</p></article>' for t, x in about_en.LEGENDS)
    words = "".join(f'<div><dt>{escape(w)}</dt><dd>{escape(m)}</dd></div>' for w, m in about_en.DIALECT)
    dishes = "".join(f'<li><h3>{escape(n)}</h3><p>{escape(d)}</p></li>' for n, d in about_en.CUISINE)
    climate = "".join(f'<div class="fact"><p class="fact-k">{escape(v)}</p><p>{escape(l)}</p></div>' for v, l in about_en.CLIMATE)
    ext = lambda url, text: f'<a href="{url}" target="_blank" rel="noopener" hreflang="pl">{text}</a>'
    rogal = '<a href="attractions/rogalowe-muzeum.html">Croissant Museum</a>'
    pyry = '<a href="attractions/muzeum-pyry.html">Poznań Potato Museum</a>'
    body = f"""
<header class="wrap page-head">
  <p class="kicker">{L['kicker']}</p>
  <h1>{L['title']}</h1>
  <p class="lead">{about_en.INTRO}</p>
  <nav class="toc" aria-label="Contents">
    <a href="#history">History</a><a href="#legends">Legends</a><a href="#dialect">Dialect</a>
    <a href="#food">Food</a><a href="#climate">Climate</a>
  </nav>
</header>

<div class="wrap prose">
<section id="history">
  <h2>{L['h_history']}</h2>
  <ol class="timeline">{timeline}</ol>
  <p class="muted">Sources (in Polish): {ext("https://www.poznan.pl/mim/turystyka/rys-historyczny-poznania,p,25064,25065.html?wo_id=2024", "poznan.pl: historical outline")}, Wikipedia articles on individual events, and the attraction pages in this guide.</p>
</section>

<section id="legends">
  <h2>{L['h_legends']}</h2>
  <div class="legends">{legends}</div>
  <p class="muted">Sources (in Polish): {ext("https://www.poznan.pl/mim/wortals/turystyka/podania-i-legendy,p,27888,27889.html", "poznan.pl: tales and legends")} (summaries) and {ext("https://pl.wikipedia.org/wiki/Rogal_%C5%9Bwi%C4%99tomarci%C5%84ski", "Wikipedia: rogal świętomarciński")}.</p>
</section>

<section id="dialect">
  <h2>{L['h_dialect']}</h2>
  <p>{L['dialect_intro']}</p>
  <dl class="glossary">{words}</dl>
  <p class="muted">Source (in Polish): {ext("https://www.poznan.pl/mim/slownik/", "poznan.pl: dictionary of the Poznań dialect")}.</p>
</section>

<section id="food">
  <h2>{L['h_food']}</h2>
  <ul class="dishes">{dishes}</ul>
  <p>{L['food_p1'].format(rogal=rogal, pyry=pyry)}</p>
  <p>{L['food_p2']}</p>
  <p class="muted">Sources (in Polish): {ext("https://pl.wikipedia.org/wiki/Kuchnia_wielkopolska", "Wikipedia: Greater Poland cuisine")}, {ext("https://www.poznan.pl/mim/info/news/25-restauracji-z-poznania-i-okolic-z-wyroznieniami-michelin-2026,281300.html", "poznan.pl: Michelin 2026 distinctions")}.</p>
</section>

<section id="climate">
  <h2>{L['h_climate']}</h2>
  <div class="facts facts-flat">{climate}</div>
  <p>{L['climate_p']}</p>
  <p class="muted">{L['climate_src'].format(imgw_data=ext("https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/miesieczne/synop/", "IMGW-PIB data"), imgw=ext("https://meteo.imgw.pl/", "IMGW"))}</p>
</section>
</div>
"""
    return page_en("About Poznań: history, legends, dialect, food and climate | Odkrywaj Poznań", body, prefix="../",
                   alt="o-poznaniu.html", active="about",
                   desc="A short history of Poznań, the legends of the goats and the bugle call, a glossary of the Poznań dialect, Greater Poland food and climate.")


def build_changes_en():
    import data_changes as dc
    import changes_en
    ext = lambda url, text: f'<a href="{url}" target="_blank" rel="noopener">{escape(text)}</a>'

    def from_status(slugs):
        out = []
        for slug in slugs:
            a = merged(slug)
            pl = BY_SLUG[slug]
            src = next((x for x in pl["sources"] if "wikipedia.org" not in x[1]), pl["sources"][0])
            out.append(f"""<li class="change"><h3><a href="attractions/{slug}.html">{escape(a['name'])}</a></h3>
<p>{escape(a['status'][1])}</p>
<p class="muted small">As of {en_date(pl['checked'])}. Source (in Polish): {ext(src[1], src[0])}</p></li>""")
        return "".join(out)

    rules = []
    for r in sorted(dc.RULES, key=lambda r: r["sort"], reverse=True):
        e = changes_en.RULES_EN[r["sort"]]
        page_href, page_label = e["page"]
        if page_label is None:
            page_label = EN[page_href.split("/")[-1][:-5]]["name"]
        rules.append(f"""<li class="change"><p class="change-meta"><span class="chip">{changes_en.KIND[r['kind']]}</span> {escape(e['when'])}</p>
<h3>{escape(e['title'])}</h3><p>{escape(e['text'])}</p>
<p class="muted small"><a href="{page_href}">{escape(page_label)}</a> · Source (in Polish): {ext(r['src'][1], e['src'])}</p></li>""")
    newest = max(datetime.datetime.strptime(BY_SLUG[s]["checked"], "%d.%m.%Y").date() for s in dc.CLOSED + dc.SEASONAL)
    body = f"""
<header class="wrap page-head">
  <p class="kicker">News</p>
  <h1>What has changed</h1>
  <p class="lead">Closures, renovations, new prices and rules that may upset your sightseeing plans. Every entry has a source and a link to the attraction. We list only what an official source confirms.</p>
  <nav class="toc" aria-label="Contents">
    <a href="#closed">Closed or under renovation</a><a href="#winter">Season and winter 2026/27</a><a href="#rules">Prices, names and rules</a>
  </nav>
</header>

<div class="wrap prose">
<section id="closed">
  <h2>Closed or under renovation</h2>
  <ul class="changes">{from_status(dc.CLOSED)}</ul>
</section>

<section id="winter">
  <h2>Season and winter 2026/27</h2>
  <p>Some attractions outside the city operate only in the season. Below is what changes when the summer season ends.</p>
  <ul class="changes">{from_status(dc.SEASONAL)}</ul>
</section>

<section id="rules">
  <h2>Prices, names and rules</h2>
  <ul class="changes">{"".join(rules)}</ul>
</section>

<p class="muted small">The log covers changes known on the day each attraction was checked (the latest: {en_date(newest.strftime("%d.%m.%Y"))}). Where our information comes from: <a href="how-we-verify.html">how we verify</a>. Noticed a change that is not listed here? Write to <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>
</div>
"""
    return page_en("What has changed: closures, renovations and new prices in Poznań | Odkrywaj Poznań", body,
                   prefix="../", alt="zmiany.html", active="attractions",
                   desc="Current closures and renovations of Poznań attractions (Town Hall, Palm House), winter seasonal limits and changes of prices, names and rules. Every entry has a source.")


def build_method_en():
    dates = sorted(datetime.datetime.strptime(a["checked"], "%d.%m.%Y").date() for a in ATTRACTIONS)
    f = lambda d: en_date(d.strftime("%d.%m.%Y"))
    return page_en("How we verify information – where our hours, prices and descriptions come from | Odkrywaj Poznań",
                   method_en.body(len(ATTRACTIONS), f(dates[0]), f(dates[-1]), en_date(SITE_CHECKED), en_date(LINKS_CHECKED)),
                   prefix="../", alt="jak-weryfikujemy.html", active="",
                   desc="Where we get opening hours, prices and descriptions, what we do when sources disagree and how to report a mistake in the Odkrywaj Poznań guide.")


CREDIT_LICENSE_EN = {"Za zgodą autora": "Used with the author's permission", "Za zgodą muzeum": "Used with the museum's permission", "Licencja indywidualna": "Individual licence"}
CREDIT_CHANGES_EN = {"pomniejszono i skompresowano": "downsized and compressed",
                     "pomniejszono, skompresowano i przycięto kadr": "downsized, compressed and cropped"}
CREDIT_TITLE_EN = {"rogalin": "Rogalin Palace – the view from the courtyard side", "taras-widokowy-collegium-altum": "Collegium Altum Viewing Terrace – the University of Economics tower in autumn", "zamek-krolewski": "Royal Castle in Poznań – the tower and façade", "puszcza-zielonka": "Zielonka Forest Landscape Park – the forest in autumn", "parowozownia-wolsztyn": "Wolsztyn Steam Locomotive Depot – a row of steam locomotives in front of the depot doors", "izba-prl-w7": "PRL Room in the former Hall W7 – interior with memorabilia", "schron-przeciwatomowy": "Nuclear Shelter and Poster Gallery – the building at ul. Słupska 62", "skansen-miniatur-pobiedziska": "Piast Trail Miniature Park – miniatures and picnic tables", "teatr-wielki": "Grand Theatre in Poznań – the building in the evening", "muzeum-archeologiczne": "Archaeological Museum – the Renaissance portal of the Górka Palace", "genius-loci": "Genius Loci Archaeological Reserve – a wooden model in the exhibition", "mieszkanie-illakowiczowny": "Kazimiera Iłłakowiczówna Apartment-Studio – the poet's study", "muzeum-broni-pancernej": "Museum of Armoured Weapons – the T-72 “Wilk” tank", "muzeum-bizuterii-moja": "MoJA Jewellery Museum – the entrance and window", "muzeum-armii-poznan": "“Poznań” Army Museum – the gate and information board", "makiety-dawnego-poznania": "Model of Old Poznań – panorama", "rogalowe-muzeum": "St Martin's Croissant Museum – croissants and ingredients", "muzeum-sienkiewicza": "Henryk Sienkiewicz Literary Museum – the townhouse on the Old Market Square", "muzeum-pyry": "Poznań Potato Museum – the sign by the entrance", "muzeum-prl": "PRL Museum – a dial telephone, a typewriter and period printed matter", "grod-pobiedziska": "Pobiedziska Stronghold – the wooden gate, footbridge and palisade", "arboretum-kornik": "Kórnik Arboretum – blooming magnolias and the castle", "muzeum-narodowe": "National Museum in Poznań – the façade", "fort-vii": "Fort VII – the entrance gate", "brama-poznania": "Gate of Poznań – the building and the footbridge over the Cybina", "centrum-szyfrow-enigma": "Enigma Cipher Centre – inside the exhibition", "muzeum-ump": "Medical University Museum – the exhibition", "muzeum-czekolady": "Chocolate Museum – shopfront and entrance", "hero-rynek": "Old Market Square in Poznań – panorama with the Town Hall and townhouses"}


def build_photo_credits_en():
    """Odpowiednik build.build_credits: te same dane z CREDITS, tłumaczone tylko etykiety i opisy zmian."""
    rows = []
    for c in sorted(CREDITS.values(), key=lambda c: c["slug"]):
        lic = escape(CREDIT_LICENSE_EN.get(c["license"], c["license"]))
        if c.get("licurl"):
            lic = f'<a href="{escape(c["licurl"])}" target="_blank" rel="noopener">{lic}</a>'
        changes = escape(CREDIT_CHANGES_EN[c.get("modified", "pomniejszono i skompresowano")])
        title = escape(CREDIT_TITLE_EN.get(c["slug"], c["title"]))
        rows.append(f"<tr id=\"foto-{c['slug']}\"><td><img src=\"../img/{c.get('file', c['slug'] + '.jpg')}?v={img_v(c.get('file', c['slug'] + '.jpg')[:-4])}\" alt=\"\" loading=\"lazy\"></td>"
                    f"<td><a href=\"{escape(c['page'])}\" target=\"_blank\" rel=\"noopener\">{title}</a></td>"
                    f"<td>{escape(c['artist'])}</td><td>{lic}</td><td>{changes}</td></tr>")
    body = f"""
<header class="wrap page-head">
  <p class="kicker">Sources</p>
  <h1>Photo credits</h1>
  <p class="lead">Most photographs come from Wikimedia Commons and are used under Creative Commons licences or are in the public domain. The rest are published with the permission of their authors or museums, as the “Licence” column shows. Click the file title to see the original, or the licence name to read its terms.</p>
  <p class="muted">For this guide the photographs were downsized and compressed, and on the pages they may be shown in a cropped frame. Any other changes are described in the “Changes” column. Modified versions of photographs under open licences are shared under the same licences as the originals.</p>
</header>
<div class="wrap"><div class="table-wrap"><table class="grid credits">
  <thead><tr><th scope="col"><span class="sr">Thumbnail</span></th><th scope="col">File</th><th scope="col">Author</th><th scope="col">Licence</th><th scope="col">Changes</th></tr></thead>
  <tbody>{''.join(rows)}</tbody>
</table></div></div>
"""
    return page_en("Photo credits – authors and licences of the photographs | Odkrywaj Poznań", body, prefix="../",
                   alt="zdjecia.html", active="",
                   desc="Authors and licences of the photographs used in the Odkrywaj Poznań guide: photographers' names, Creative Commons licences and links to the originals.")


def page_map():
    m = {"zdjecia.html": "en/photo-credits.html", "index.html": "en/index.html", "prywatnosc.html": "en/privacy.html", "informacje.html": "en/practical.html",
         "plany.html": "en/plans.html", "kalendarz.html": "en/calendar.html", "teatry.html": "en/theatres.html", "muzea.html": "en/museums.html", "atrakcje.html": "en/attractions.html", "mapa.html": "en/map.html",
         "punkty-widokowe.html": "en/viewpoints.html", "jak-weryfikujemy.html": "en/how-we-verify.html", "o-poznaniu.html": "en/about.html",
         "zmiany.html": "en/changes.html"}
    for s in translated():
        m[f"atrakcje/{s}.html"] = f"en/attractions/{s}.html"
    return m


def build_all():
    import pages_en
    slugs = translated()
    out = {"en/index.html": pages_en.build_home_en(), "en/attractions.html": pages_en.build_attractions_en(),
           "en/map.html": pages_en.build_map_en(), "en/privacy.html": build_privacy_en(),
           "en/practical.html": build_practical_en(),
           "en/plans.html": build_plans_en(),
           "en/calendar.html": build_calendar_en(),
           "en/theatres.html": build_theatres_en(),
           "en/museums.html": build_museums_en(),
           "en/viewpoints.html": build_viewpoints_en(),
           "en/about.html": build_about_en(),
           "en/how-we-verify.html": build_method_en(),
           "en/photo-credits.html": build_photo_credits_en(),
           "en/changes.html": build_changes_en()}
    for i, s in enumerate(slugs):
        out[f"en/attractions/{s}.html"] = build_attraction_en(s, i, slugs)
    return out
