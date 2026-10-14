# -*- coding: utf-8 -*-
"""Kontrola angielskich tłumaczeń (data_en.py) względem polskich danych (site_data.py).

Użycie:
  python src/check_en.py                 raport: nieaktualne tłumaczenia i niezgodności liczb
  python src/check_en.py --stamp slug…   zapisuje obecny stan polskiego tekstu jako „przetłumaczony”
  python src/check_en.py --stamp-all     to samo dla wszystkich tłumaczeń (po przeglądzie całości)
  python src/check_en.py --stamp-practical  stempel angielskiej strony Practical (src/practical_en.py)
  python src/check_en.py --stamp-privacy zapisuje stempel angielskiej polityki prywatności (src/privacy_en.py)

Co sprawdza:
1. Czy polski tekst atrakcji zmienił się od ostatniego „stempla” (en_stamps.json): jeśli tak, tłumaczenie
   trzeba zaktualizować (zwłaszcza godziny i ceny), a potem uruchomić --stamp.
2. Czy w polskich i angielskich godzinach/cenach występują te same godziny (9:00) i te same kwoty (35 zł = PLN 35),
   żeby wyłapać literówkę w liczbie.
3. Czy liczba wierszy godzin, cen i sekcji zgadza się z polskim oryginałem.
Kod wyjścia 1, gdy coś jest nie tak (można użyć przed commitem)."""
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_en import EN  # noqa: E402
from site_data import ATTRACTIONS  # noqa: E402

STAMPS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "en_stamps.json")
PL = {a["slug"]: a for a in ATTRACTIONS}
FIELDS = ("name", "short", "badge", "status", "lead", "sections", "address", "hours", "tickets", "phone", "see_also")


def pl_hash(a):
    data = {k: a.get(k) for k in FIELDS}
    if a.get("trip"):  # tylko wycieczki za miasto; bez klucza, żeby nie unieważniać starszych stempli
        data["trip"] = a["trip"]
    return hashlib.sha1(json.dumps(data, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:12]


def main_text(html):
    """Sama treść strony (bez nawigacji i stopki), żeby zmiana menu nie unieważniała tłumaczenia."""
    return html[html.index('<main id="tresc">'):html.index("</main>")]


def practical_hash():
    """Skrót polskiej strony Informacje praktyczne (build.build_info), by wykryć zmianę bez zmiany angielskiej."""
    import build
    return hashlib.sha1(main_text(build.build_info()).encode("utf-8")).hexdigest()[:12]


def plans_hash():
    """Skrót polskich planów zwiedzania (data_guide.PLANS)."""
    from data_guide import PLANS
    return hashlib.sha1(json.dumps(PLANS, ensure_ascii=False).encode("utf-8")).hexdigest()[:12]


def calendar_hash():
    """Skrót polskiego kalendarza wydarzeń (data_events.CALENDAR)."""
    from data_events import CALENDAR
    return hashlib.sha1(json.dumps(CALENDAR, ensure_ascii=False).encode("utf-8")).hexdigest()[:12]


def event_numbers(parts):
    """Wszystkie liczby (godziny, lata, kwoty) z tekstów wydarzenia; „13 505” i „13,505” dają te same liczby."""
    text = " ".join(parts)
    text = re.sub(r"\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b", r"\1 \3", text)  # 10.10.2026 -> „10 2026” (miesiąc słowami w EN)
    text = re.sub(r"(\d)[ ,.](\d{3})\b", r"\1\2", text)  # separatory tysięcy i przecinek dziesiętny: 13 505 = 13,505, 21,097 = 21.097
    text = re.sub(r"\b(\d{1,2})\.\d{2}\b", r"\1", text)  # 1.03–15.11 = 1 Mar–15 Nov: porównujemy same dni
    return sorted(re.findall(r"\d+", text))


def theatres_hash():
    """Skrót polskich danych teatrów (data_theatres.THEATRES)."""
    from data_theatres import THEATRES
    return hashlib.sha1(json.dumps(THEATRES, ensure_ascii=False).encode("utf-8")).hexdigest()[:12]


def museums_hash():
    """Skrót polskiej strony Muzea (build.build_museums) bez nawigacji i stopki."""
    import build
    return hashlib.sha1(main_text(build.build_museums()).encode("utf-8")).hexdigest()[:12]


def viewpoints_hash():
    """Skrót polskiej strony Punkty widokowe (build.build_viewpoints) bez nawigacji i stopki."""
    import build
    return hashlib.sha1(main_text(build.build_viewpoints()).encode("utf-8")).hexdigest()[:12]


def about_hash():
    """Skrót polskiej strony O Poznaniu (build.build_about) bez nawigacji i stopki."""
    import build
    return hashlib.sha1(main_text(build.build_about()).encode("utf-8")).hexdigest()[:12]


def privacy_hash():
    """Skrót polskiej strony Prywatność (build.build_privacy), by wykryć zmianę polityki bez zmiany angielskiej."""
    import build
    return hashlib.sha1(main_text(build.build_privacy()).encode("utf-8")).hexdigest()[:12]


def load():
    return json.load(open(STAMPS, encoding="utf-8")) if os.path.exists(STAMPS) else {}


def numbers(rows, kind):
    text = " ".join(f"{k} {v}" for k, v in rows)
    price = r"(\d+)(?:–(\d+))?\s*zł" if kind == "pl" else r"PLN\s*(\d+)(?:–(\d+))?"
    prices = [n for pair in re.findall(price, text) for n in pair if n]  # zakres „2–5 zł” = dwie kwoty
    return sorted(re.findall(r"\d{1,2}:\d{2}", text) + prices)


def check():
    stamps, problems = load(), []
    for slug, e in EN.items():
        a = PL.get(slug)
        if not a:
            problems.append(f"{slug}: brak takiej atrakcji w polskich danych")
            continue
        if stamps.get(slug) != pl_hash(a):
            problems.append(f"{slug}: polski tekst zmienił się od tłumaczenia (zaktualizuj EN, potem --stamp {slug})"
                            if slug in stamps else f"{slug}: tłumaczenie bez stempla (--stamp {slug})")
        for key in ("hours", "tickets"):
            if len(e[key]) != len(a[key]):
                problems.append(f"{slug}: {key}: {len(e[key])} wierszy w EN, {len(a[key])} w PL")
            if numbers(e[key], "en") != numbers(a[key], "pl"):
                problems.append(f"{slug}: {key}: różne godziny/kwoty. PL {numbers(a[key], 'pl')} ≠ EN {numbers(e[key], 'en')}")
        if len(e["sections"]) != len(a["sections"]):
            problems.append(f"{slug}: {len(e['sections'])} sekcji w EN, {len(a['sections'])} w PL")
        if bool(e.get("status")) != bool(a["status"]):
            problems.append(f"{slug}: komunikat o statusie jest tylko w jednej wersji")
        if bool(a.get("trip")) and len(e.get("getting", [])) != len(a["trip"]["getting"]):
            problems.append(f"{slug}: różna liczba wierszy „Dojazd z Poznania” (getting)")
        if len(e.get("see_also", [])) != len(a.get("see_also", [])):
            problems.append(f"{slug}: różna liczba odsyłaczy „Zobacz też”")
    if stamps.get("_privacy") != privacy_hash():
        problems.append("prywatnosc: polska polityka zmieniła się od tłumaczenia (zaktualizuj privacy_en.py, potem --stamp-privacy)"
                        if "_privacy" in stamps else "prywatnosc: brak stempla (--stamp-privacy)")
    from data_guide import PLANS
    from plans_en import PLANS_EN
    for pid, _t, _w, _i, stops, _n in PLANS:
        e = PLANS_EN.get(pid)
        if not e:
            problems.append(f"plany: brak angielskiego planu „{pid}”")
        elif len(e["stops"]) != len(stops):
            problems.append(f"plany: {pid}: {len(e['stops'])} punktów w EN, {len(stops)} w PL")
        for s, _w2, _h in stops:
            if s not in EN:
                problems.append(f"plany: {pid}: atrakcja „{s}” nie ma tłumaczenia")
    from data_events import CALENDAR
    from calendar_en import CAL_EN
    for ev in CALENDAR:
        t = CAL_EN.get(ev["id"])
        if not t:
            problems.append(f"kalendarz: brak angielskiego opisu wydarzenia „{ev['id']}”")
            continue
        if len(t["desc"]) != len(ev["desc"]):
            problems.append(f"kalendarz: {ev['id']}: {len(t['desc'])} akapitów w EN, {len(ev['desc'])} w PL")
        if bool(t["note"]) != bool(ev["note"]):
            problems.append(f"kalendarz: {ev['id']}: uwaga jest tylko w jednej wersji")
        pl_nums = event_numbers([ev["name"], ev["when"], ev["place"], ev["note"]] + ev["desc"])
        en_nums = event_numbers([t["name"], t["when"], t["place"], t["note"]] + t["desc"])
        if pl_nums != en_nums:
            problems.append(f"kalendarz: {ev['id']}: różne liczby. PL {pl_nums} ≠ EN {en_nums}")
    from data_theatres import THEATRES
    from theatres_en import VENUES_EN
    for v in THEATRES:
        t = VENUES_EN.get(v["id"])
        if not t:
            problems.append(f"teatry: brak angielskiego opisu sceny „{v['id']}”")
            continue
        if len(t["desc"]) != len(v["desc"]):
            problems.append(f"teatry: {v['id']}: {len(t['desc'])} akapitów w EN, {len(v['desc'])} w PL")
        if len(t["links"]) != len(v["links"]):
            problems.append(f"teatry: {v['id']}: {len(t['links'])} etykiet linków w EN, {len(v['links'])} w PL")
        if event_numbers(v["desc"] + [v["kind"]]) != event_numbers(t["desc"] + [t["kind"]]):
            problems.append(f"teatry: {v['id']}: różne liczby (godziny, ceny, lata) między PL a EN")
    from museums_en import MUSEUMS_EN
    for a in PL.values():
        if a["cat"] != "muzea" or a["slug"] in EN:
            continue
        m = MUSEUMS_EN.get(a["slug"])
        if not m:
            problems.append(f"muzea: brak angielskich danych muzeum „{a['slug']}” (museums_en.py)")
            continue
        for key in ("hours", "tickets"):
            if len(m[key]) != len(a[key]):
                problems.append(f"muzea: {a['slug']}: {key}: {len(m[key])} wierszy w EN, {len(a[key])} w PL")
            elif numbers(m[key], "en") != numbers(a[key], "pl"):
                problems.append(f"muzea: {a['slug']}: {key}: różne godziny/kwoty. PL {numbers(a[key], 'pl')} ≠ EN {numbers(m[key], 'en')}")
    from data_gaps3 import VIEWPOINTS
    from viewpoints_en import WHAT
    for slug, what, _ in VIEWPOINTS:
        if slug not in WHAT:
            problems.append(f"punkty widokowe: brak angielskiego opisu „{slug}”")
        elif event_numbers([what]) != event_numbers([WHAT[slug]]):
            problems.append(f"punkty widokowe: {slug}: różne liczby między PL a EN")
        if slug not in EN:
            problems.append(f"punkty widokowe: atrakcja „{slug}” nie ma tłumaczenia")
    import data_guide as dg
    import about_en as ab
    pairs = [("HISTORY", dg.HISTORY, ab.HISTORY), ("LEGENDS", dg.LEGENDS, ab.LEGENDS), ("DIALECT", dg.DIALECT, ab.DIALECT),
             ("CUISINE", dg.CUISINE, ab.CUISINE), ("CLIMATE", dg.CLIMATE, ab.CLIMATE)]
    for name, pl_list, en_list in pairs:
        if len(pl_list) != len(en_list):
            problems.append(f"o poznaniu: {name}: {len(en_list)} pozycji w EN, {len(pl_list)} w PL")
            continue
        pl_txt = [x for it in pl_list for x in it[:2]]
        en_txt = [x for it in en_list for x in it[:2]]
        pl_n = [ab.NUMBER_EXCEPTIONS.get(n, n) for n in event_numbers(pl_txt)]
        en_n = event_numbers([re.sub(r"\b\d{1,2}(st|nd|rd|th) century", "", t) for t in en_txt])
        if sorted(pl_n) != sorted(en_n):
            problems.append(f"o poznaniu: {name}: różne liczby między PL a EN. PL {sorted(pl_n)} ≠ EN {sorted(en_n)}")
    if stamps.get("_about") != about_hash():
        problems.append("o poznaniu: polska strona zmieniła się od tłumaczenia (przejrzyj about_en.py, potem --stamp-about)"
                        if "_about" in stamps else "o poznaniu: brak stempla (--stamp-about)")
    if stamps.get("_viewpoints") != viewpoints_hash():
        problems.append("punkty widokowe: polska strona zmieniła się od tłumaczenia (przejrzyj viewpoints_en.py, potem --stamp-viewpoints)"
                        if "_viewpoints" in stamps else "punkty widokowe: brak stempla (--stamp-viewpoints)")
    if stamps.get("_museums") != museums_hash():
        problems.append("muzea: polska strona zmieniła się od tłumaczenia (przejrzyj museums_en.py, potem --stamp-museums)"
                        if "_museums" in stamps else "muzea: brak stempla (--stamp-museums)")
    if stamps.get("_theatres") != theatres_hash():
        problems.append("teatry: polskie dane zmieniły się od tłumaczenia (przejrzyj theatres_en.py, potem --stamp-theatres)"
                        if "_theatres" in stamps else "teatry: brak stempla (--stamp-theatres)")
    if stamps.get("_calendar") != calendar_hash():
        problems.append("kalendarz: polski kalendarz zmienił się od tłumaczenia (przejrzyj calendar_en.py, potem --stamp-calendar)"
                        if "_calendar" in stamps else "kalendarz: brak stempla (--stamp-calendar)")
    if stamps.get("_plans") != plans_hash():
        problems.append("plany: polskie plany zmieniły się od tłumaczenia (przejrzyj plans_en.py, potem --stamp-plans)"
                        if "_plans" in stamps else "plany: brak stempla (--stamp-plans)")
    if stamps.get("_practical") != practical_hash():
        problems.append("informacje: polska strona zmieniła się od tłumaczenia (przejrzyj practical_en.py, potem --stamp-practical)"
                        if "_practical" in stamps else "informacje: brak stempla (--stamp-practical)")
    return problems


def main():
    args = sys.argv[1:]
    if args and args[0] == "--stamp-museums":
        stamps = load()
        stamps["_museums"] = museums_hash()
        json.dump(stamps, open(STAMPS, "w", encoding="utf-8", newline="\n"), indent=1, ensure_ascii=False, sort_keys=True)
        print("Zapisano stempel: muzea")
        return
    if args and args[0] == "--stamp-theatres":
        stamps = load()
        stamps["_theatres"] = theatres_hash()
        json.dump(stamps, open(STAMPS, "w", encoding="utf-8", newline="\n"), indent=1, ensure_ascii=False, sort_keys=True)
        print("Zapisano stempel: teatry")
        return
    if args and args[0] == "--stamp-about":
        stamps = load()
        stamps["_about"] = about_hash()
        json.dump(stamps, open(STAMPS, "w", encoding="utf-8", newline="\n"), indent=1, ensure_ascii=False, sort_keys=True)
        print("Zapisano stempel: o poznaniu")
        return
    if args and args[0] == "--stamp-viewpoints":
        stamps = load()
        stamps["_viewpoints"] = viewpoints_hash()
        json.dump(stamps, open(STAMPS, "w", encoding="utf-8", newline="\n"), indent=1, ensure_ascii=False, sort_keys=True)
        print("Zapisano stempel: punkty widokowe")
        return
    if args and args[0] == "--stamp-calendar":
        stamps = load()
        stamps["_calendar"] = calendar_hash()
        json.dump(stamps, open(STAMPS, "w", encoding="utf-8", newline="\n"), indent=1, ensure_ascii=False, sort_keys=True)
        print("Zapisano stempel: kalendarz")
        return
    if args and args[0] == "--stamp-plans":
        stamps = load()
        stamps["_plans"] = plans_hash()
        json.dump(stamps, open(STAMPS, "w", encoding="utf-8", newline="\n"), indent=1, ensure_ascii=False, sort_keys=True)
        print("Zapisano stempel: plany")
        return
    if args and args[0] == "--stamp-practical":
        stamps = load()
        stamps["_practical"] = practical_hash()
        json.dump(stamps, open(STAMPS, "w", encoding="utf-8", newline="\n"), indent=1, ensure_ascii=False, sort_keys=True)
        print("Zapisano stempel: informacje")
        return
    if args and args[0] == "--stamp-privacy":
        stamps = load()
        stamps["_privacy"] = privacy_hash()
        json.dump(stamps, open(STAMPS, "w", encoding="utf-8", newline="\n"), indent=1, ensure_ascii=False, sort_keys=True)
        print("Zapisano stempel: prywatnosc")
        return
    if args and args[0] in ("--stamp", "--stamp-all"):
        stamps = load()
        slugs = list(EN) if args[0] == "--stamp-all" else args[1:]
        for s in slugs:
            stamps[s] = pl_hash(PL[s])
        json.dump(stamps, open(STAMPS, "w", encoding="utf-8", newline="\n"), indent=1, ensure_ascii=False, sort_keys=True)
        print(f"Zapisano stemple: {', '.join(slugs)}")
        return
    problems = check()
    print(f"Tłumaczeń: {len(EN)}")
    for p in problems:
        print("  ! " + p)
    print("OK: wszystkie tłumaczenia zgodne z polskimi danymi." if not problems else f"Problemów: {len(problems)}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
