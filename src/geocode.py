# -*- coding: utf-8 -*-
"""Geokodowanie atrakcji przez Nominatim (OpenStreetMap), max 1 zapytanie/s.
Wynik: src/coords.json {slug: {lat, lon, q, name}}. Ręczne poprawki: src/coords_manual.json (mają pierwszeństwo).
Uruchom: python src/geocode.py  (pomija slugi, które już mają współrzędne)"""
import json, os, sys, time, urllib.parse, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_data import ATTRACTIONS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "coords.json")
UA = {"User-Agent": "PoznanPrzewodnik/1.0 (+https://github.com/dzbani/poznan-przewodnik)"}
BBOX = (16.70, 52.24, 17.10, 52.52)  # lon_min, lat_min, lon_max, lat_max
data = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}


def search(q):
    u = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
        {"q": q, "format": "jsonv2", "limit": 3, "viewbox": "16.70,52.52,17.10,52.24", "bounded": 1, "accept-language": "pl"})
    time.sleep(1.1)
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA)))


for a in ATTRACTIONS:
    if a["slug"] in data:
        continue
    addr = a["address"].split("(")[0].replace(", Poznań", "").strip(" ,")
    tries = [f'{a["name"]}, Poznań', f'{addr}, Poznań'] if "Poznań" in a["address"] or True else []
    hit = None
    for q in tries:
        try:
            r = search(q)
        except Exception as e:
            print("BŁĄD", a["slug"], e); r = []
        if r:
            hit = (q, r[0]); break
    if hit:
        q, r = hit
        data[a["slug"]] = dict(lat=round(float(r["lat"]), 6), lon=round(float(r["lon"]), 6), q=q, name=r["display_name"][:120])
        print(f'{a["slug"]:32} {q[:45]:45} -> {r["display_name"][:70]}')
    else:
        print(f'{a["slug"]:32} BRAK')
    json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("gotowe:", len(data), "/", len(ATTRACTIONS))
