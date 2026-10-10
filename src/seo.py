# -*- coding: utf-8 -*-
"""SEO podstron atrakcji: tytuł pod zapytania o konkretne miejsce, opis z faktów (godziny, bilety, adres)
i dane strukturalne schema.org (JSON-LD). Wszystko liczone z pól atrakcji w danych, bez osobnej treści."""
import json
import re

DESC_MAX = 155

# Dni tygodnia w etykietach godzin: pełna nazwa → (skrót do opisu, dzień schema.org).
DAYS = [("poniedziałek", "pn", "Monday"), ("wtorek", "wt", "Tuesday"), ("środa", "śr", "Wednesday"),
        ("czwartek", "czw", "Thursday"), ("piątek", "pt", "Friday"), ("sobota", "sb", "Saturday"),
        ("niedziela", "nd", "Sunday")]
DAY_WORD = {full: i for i, (full, _, _) in enumerate(DAYS)}
DAY_WORD.update({short: i for i, (_, short, _) in enumerate(DAYS)})
DAY_RE = re.compile(r"\b(" + "|".join(full for full, _, _ in DAYS) + r")\b", re.I)
TIME_RE = re.compile(r"^(\d{1,2}):(\d{2})–(\d{1,2}):(\d{2})$")
CLOSED = "nieczynne"

# Typ schema.org obok TouristAttraction, gdy oczywisty. Reszta zostaje samym TouristAttraction.
CAT_TYPE = {"muzea": "Museum", "koscioly": "Church", "pomniki": "LandmarksOrHistoricalBuildings"}
SLUG_TYPE = {
    "nowe-zoo": "Zoo", "stare-zoo": "Zoo",
    "ogrod-botaniczny": "Park", "szachty": "Park", "legi-debinskie": "Park", "ogrod-zamkowy": "Park",
    "lasek-marcelinski": "Park", "stare-koryto-warty": "Park", "arboretum-kornik": "Park", "wpn": "Park",
    "jezioro-maltanskie": "LakeBodyOfWater", "rusalka": "LakeBodyOfWater", "jezioro-kierskie": "LakeBodyOfWater",
    "jezioro-strzeszynskie": "LakeBodyOfWater",
    "zamek-kornik": "Museum", "rogalin": "Museum", "mppp-gniezno": "Museum", "ostrow-lednicki": "Museum",
    "biskupin": "Museum", "szreniawa": "Museum", "fiedler": "Museum", "katedra-gniezno": "Church",
    "zamek-krolewski": "Museum", "brama-poznania": "Museum", "genius-loci": "Museum",
}


def _is_free(a):
    vals = [v.lower() for _, v in a["tickets"]]
    return bool(vals) and all("bezpłat" in v or "wstęp wolny" in v for v in vals)


def _is_paid(a):
    return any("zł" in v for _, v in a["tickets"])


def _always_open(a):
    """Miejsca bez godzin otwarcia: pomniki, parki, place (dostępne całą dobę, ogólnodostępne)."""
    words = ("całą dobę", "ogólnodostępn", "dostępny, tylko", "przez cały rok", "z zewnątrz")
    return all(any(w in v for w in words) for _, v in a["hours"][:1])


def title(a):
    """Tytuł pod zapytanie „<miejsce> godziny otwarcia / bilety / dojazd”. Nazwa na początku,
    bo Google ucina końcówkę dłuższych tytułów."""
    if a["cat"] == "wycieczki":
        tail = "godziny otwarcia, bilety, dojazd z Poznania"
    elif a["cat"] == "pomniki":
        tail = "historia i lokalizacja"
    elif a["cat"] == "koscioly":
        tail = "historia, zwiedzanie, dojazd"
    elif _is_paid(a):
        tail = "godziny otwarcia, bilety, dojazd"
    elif _always_open(a):
        tail = "co zobaczyć, dojazd"
    else:
        tail = "godziny otwarcia, dojazd"
    out = f"{a['name']} – {tail} | Odkrywaj Poznań"
    # Bardzo długie nazwy: skracamy końcówkę, żeby tytuł nie przekraczał 100 znaków.
    for long, short in ((" z Poznania", ""), ("godziny otwarcia", "godziny")):
        if len(out) > 100:
            tail = tail.replace(long, short)
            out = f"{a['name']} – {tail} | Odkrywaj Poznań"
    return out


def _short_days(label):
    return DAY_RE.sub(lambda m: DAYS[DAY_WORD[m.group(1).lower()]][1], label)


def _lower_label(k):
    """Wielka litera tylko na początku etykiety („Zwiedzanie”) → mała w środku zdania; nazwy własne
    („Muzeum Przyrodnicze”) zostają."""
    words = k.split()
    return k if len(words) > 1 and words[1][:1].isupper() else k[:1].lower() + k[1:]


def _hours_row(k, v):
    k = _short_days(k)
    if k.lower().startswith("godziny"):
        return v
    k = _lower_label(k)
    # Etykieta z samych dni („wt–pt”, „pt i sb”, „codziennie”) łączy się z godzinami bez dwukropka.
    only_days = all(t in DAY_WORD or t in ("i", "codziennie") for t in re.split(r"[–,\s]+", k.lower()) if t)
    return f"{k} {v}" if only_days else f"{k}: {v}"


def _has_digit(text):
    return any(c.isdigit() for c in text)


def _hours(a, budget):
    """Wszystkie wiersze godzin albo nic: obcięta lista sugerowałaby, że w pozostałe dni jest zamknięte.
    Opisy bez liczb („poza nabożeństwami”) pomijamy, bo nic nie mówią i powtarzają się na wielu stronach."""
    text = "Godziny: " + "; ".join(_hours_row(k, v) for k, v in a["hours"]) + "."
    return text if _has_digit(text) and len(text) <= budget else ""


def _tickets(a, budget):
    if _is_free(a):
        short = a["short"].lower()
        return "" if "wstęp wolny" in short or "bezpłat" in short else "Wstęp bezpłatny."
    out = ""
    for k, v in a["tickets"]:
        if not _has_digit(v) and "bezpłat" not in v:
            continue
        row = f"{_lower_label(k)} {v}"
        cand = f"Bilety: {row}." if not out else f"{out[:-1]}; {row}."
        if len(cand) > budget:
            break
        out = cand
    return out


def description(a):
    """Meta description z konkretów, o które pyta turysta: godziny, cena, adres.
    Pole desc na karcie nadpisuje opis liczony z danych (dla dwóch kart z identycznymi godzinami i adresem)."""
    if a.get("desc"):
        return a["desc"]
    address = f"Adres: {a['address']}."
    if a["status"] and a["status"][0] == "closed":
        parts = ["Czasowo zamknięte.", a["short"], address]
    elif _always_open(a) or a["cat"] == "pomniki":
        # Godziny nic tu nie mówią; liczy się, co to jest i gdzie stoi.
        parts = [a["short"], address]
    else:
        hours = _hours(a, DESC_MAX - len(address) - 1)
        rest = DESC_MAX - len(address) - len(hours) - 2
        tickets = _tickets(a, rest)
        parts = [hours or a["short"], tickets, address]
    desc = ""
    for p in parts:
        cand = f"{desc} {p}".strip()
        if p and len(cand) <= DESC_MAX:
            desc = cand
    return desc or a["short"]


def _day_set(label):
    """„Wtorek–piątek”, „Środa, czwartek”, „Codziennie” → indeksy dni; None, gdy etykieta to nie same dni."""
    label = label.lower().strip()
    if label == "codziennie":
        return list(range(7))
    days = []
    for part in re.split(r",\s*|\s+i\s+", label):
        ends = part.split("–")
        if not all(e.strip() in DAY_WORD for e in ends) or len(ends) > 2:
            return None
        lo, hi = DAY_WORD[ends[0].strip()], DAY_WORD[ends[-1].strip()]
        days += list(range(lo, hi + 1)) if lo <= hi else list(range(lo, 7)) + list(range(0, hi + 1))
    return days


def opening_hours(a):
    """Godziny w formacie schema.org tylko dla prostych, całorocznych tygodniowych rozkładów.
    Rozkłady sezonowe, z wyjątkami albo opisowe pomijamy, bo błędne dane strukturalne są gorsze niż żadne."""
    if a["status"] and a["status"][0] == "closed":
        return None
    rows = a["hours"]
    if len(rows) == 1 and rows[0][1].startswith("codziennie "):
        rows = [("Codziennie", rows[0][1][len("codziennie "):])]
    spec = {}
    for k, v in rows:
        if v == CLOSED:
            continue
        days, m = _day_set(k), TIME_RE.match(v)
        if days is None or not m:
            return None
        hh = (f"{int(m[1]):02d}:{m[2]}", f"{int(m[3]):02d}:{m[4]}")
        for d in days:
            spec.setdefault(hh, set()).add(d)
    if not spec:
        return None
    return [{"@type": "OpeningHoursSpecification", "dayOfWeek": [DAYS[d][2] for d in sorted(ds)],
             "opens": o, "closes": c} for (o, c), ds in spec.items()]


def _address(a):
    segs = [s.strip() for s in a["address"].split(",")]
    out = {"@type": "PostalAddress", "addressCountry": "PL"}
    m = re.match(r"^(\d{2}-\d{3})\s+(.+)$", segs[-1])
    if m:
        out["postalCode"], out["addressLocality"] = m[1], m[2]
        street = segs[:-1]
    elif len(segs) > 1 and re.match(r"^Poznań(-\w+)?$", segs[-1]):
        out["addressLocality"] = segs[-1]
        street = segs[:-1]
    else:
        out["addressLocality"] = "Poznań"
        street = segs if len(segs) > 1 else []
    if street:
        out["streetAddress"] = ", ".join(street)
    return out


def json_ld(a, site_url, cat_name, lat_lon):
    url = f"{site_url}atrakcje/{a['slug']}"
    extra = SLUG_TYPE.get(a["slug"]) or CAT_TYPE.get(a["cat"])
    place = {
        "@context": "https://schema.org",
        "@type": ["TouristAttraction", extra] if extra else "TouristAttraction",
        "name": a["name"],
        "description": a["short"],
        "url": url,
        "address": _address(a),
    }
    if a.get("img"):
        place["image"] = f"{site_url}img/{a['img']}.jpg"
    if lat_lon:
        place["geo"] = {"@type": "GeoCoordinates", "latitude": lat_lon[0], "longitude": lat_lon[1]}
    if a["phone"]:
        place["telephone"] = a["phone"]
    if _is_free(a):
        place["isAccessibleForFree"] = True
    elif _is_paid(a):
        place["isAccessibleForFree"] = False
    hours = opening_hours(a)
    if hours:
        place["openingHoursSpecification"] = hours
    crumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Strona główna", "item": site_url},
            {"@type": "ListItem", "position": 2, "name": cat_name, "item": f"{site_url}atrakcje#kat-{a['cat']}"},
            {"@type": "ListItem", "position": 3, "name": a["name"], "item": url},
        ],
    }
    blocks = []
    for d in (place, crumbs):
        # „</” w JSON zamknęłoby znacznik script; ensure_ascii=False zostawia polskie litery czytelne.
        txt = json.dumps(d, ensure_ascii=False, indent=1).replace("</", "<\\/")
        blocks.append(f'<script type="application/ld+json">\n{txt}\n</script>\n')
    return "".join(blocks)
