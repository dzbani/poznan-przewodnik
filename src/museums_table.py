"""Zestawienie muzeów: wyciąga z istniejących danych (hours/tickets) kolumny do jednej tabeli.

Nie dodaje żadnych nowych faktów: wszystko pochodzi z pól hours i tickets atrakcji. Gdy z pola nie da się
jednoznacznie odczytać wartości, kolumna pokazuje „zobacz stronę obiektu” zamiast zgadywać.
Uruchom `python src/museums_table.py`, żeby zobaczyć, jak każdy wiersz został odczytany (do ręcznej kontroli).
"""
import re
import sys

DAYS = ["pn", "wt", "sr", "cz", "pt", "sb", "nd"]
NAMES = {"poniedziałek": "pn", "poniedziałki": "pn", "wtorek": "wt", "środa": "sr", "środę": "sr", "czwartek": "cz",
         "piątek": "pt", "sobota": "sb", "sobotę": "sb", "niedziela": "nd", "niedziele": "nd"}
LABEL = {"pn": "poniedziałek", "wt": "wtorek", "sr": "środa", "cz": "czwartek", "pt": "piątek", "sb": "sobota", "nd": "niedziela"}


def day_list(label):
    """Dni tygodnia wymienione w etykiecie: 'Wtorek–środa', 'Wtorek, piątek, sobota', 'Niedziela i święta'."""
    t = label.lower()
    found = [(m.start(), NAMES[m.group(0)]) for m in re.finditer("|".join(sorted(NAMES, key=len, reverse=True)), t)]
    days = [d for _, d in found]
    if len(days) == 2 and re.search(r"[–-]", t) and not re.search(r",| i ", t):
        a, b = DAYS.index(days[0]), DAYS.index(days[1])
        return DAYS[a:b + 1] if a <= b else DAYS[a:] + DAYS[:b + 1]
    return days


def derive(a):
    h, t = a["hours"], a["tickets"]
    closed, opened = set(), set()
    for label, txt in h:
        d = day_list(label)
        low = txt.lower()
        if "nieczynn" in low or "zamkni" in low:
            closed.update(d)
        elif d and re.search(r"\d", txt):
            opened.update(d)
    explicit_all_but = any("pozostałe dni" in l.lower() for l, _ in h)
    if explicit_all_but:
        pozostale = next(tx for l, tx in h if "pozostałe dni" in l.lower())
        if "nieczynn" in pozostale.lower():
            closed.update(set(DAYS) - opened)
        else:
            opened.update(set(DAYS) - closed)
    normal = next((x for l, x in t if l.lower().startswith("normalny")), None)
    reduced = next((x for l, x in t if l.lower().startswith("ulgowy")), None)
    free_always = any(l.lower() in ("wstęp",) and "bezpłatn" in x.lower() for l, x in t)
    free_days = []
    for l, x in t:
        if "wstęp wolny" in x.lower() or (l.lower() in NAMES and "bezpłatn" in x.lower()):
            free_days += [d for d in day_list(l) if d not in free_days]
    price = None
    if normal and reduced:
        price = f"{normal} / {reduced}"
    elif normal:
        price = normal
    elif free_always:
        price = "bezpłatnie"
    return dict(closed=sorted(closed, key=DAYS.index), opened=sorted(opened, key=DAYS.index), price=price,
                free_always=free_always, free_days=free_days, normal=normal, reduced=reduced)


def open_monday(a, d):
    """Tak tylko wtedy, gdy dane wprost mówią, że w poniedziałek jest otwarte; „nie wiadomo” liczy się jak nie."""
    if "pn" in d["closed"]:
        return False
    if "pn" in d["opened"]:
        return True
    return any("codziennie" in l.lower() and re.search(r"\d", x) for l, x in a["hours"])


_PL = str.maketrans("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ", "acelnoszzACELNOSZZ")


def sort_key(name):
    return name.translate(_PL).casefold()


if __name__ == "__main__":
    sys.path.insert(0, "src")
    from site_data import ATTRACTIONS
    for a in ATTRACTIONS:
        if a["cat"] != "muzea":
            continue
        d = derive(a)
        print(("PN " if open_monday(a, d) else "   ") + f"{a['name'][:44]:44} | cena: {d['price'] or '—':14} | wolny: {','.join(d['free_days']) or ('zawsze' if d['free_always'] else '—'):8} | nieczynne: {','.join(d['closed']) or '—':22} | otwarte: {','.join(d['opened']) or '—'}")
