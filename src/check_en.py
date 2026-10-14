# -*- coding: utf-8 -*-
"""Kontrola angielskich tłumaczeń (data_en.py) względem polskich danych (site_data.py).

Użycie:
  python src/check_en.py                 raport: nieaktualne tłumaczenia i niezgodności liczb
  python src/check_en.py --stamp slug…   zapisuje obecny stan polskiego tekstu jako „przetłumaczony”
  python src/check_en.py --stamp-all     to samo dla wszystkich tłumaczeń (po przeglądzie całości)

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
    return hashlib.sha1(json.dumps(data, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:12]


def load():
    return json.load(open(STAMPS, encoding="utf-8")) if os.path.exists(STAMPS) else {}


def numbers(rows, kind):
    text = " ".join(f"{k} {v}" for k, v in rows)
    if kind == "pl":
        return sorted(re.findall(r"\d{1,2}:\d{2}", text) + re.findall(r"(\d+)\s*zł", text))
    return sorted(re.findall(r"\d{1,2}:\d{2}", text) + re.findall(r"PLN\s*(\d+)", text))


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
        if len(e.get("see_also", [])) != len(a.get("see_also", [])):
            problems.append(f"{slug}: różna liczba odsyłaczy „Zobacz też”")
    return problems


def main():
    args = sys.argv[1:]
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
