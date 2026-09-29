# -*- coding: utf-8 -*-
"""Pobiera dane podkładu mapy z OpenStreetMap (Overpass) i zapisuje uproszczony GeoJSON-owy zbiór
warstw do src/basemap_raw.json. Dane © autorzy OpenStreetMap, licencja ODbL.
Uruchom: python src/fetch_basemap.py"""
import json
import urllib.error
import os
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "PoznanPrzewodnik/1.0 (+https://github.com/dzbani/poznan-przewodnik)"}
BB = "52.25,16.72,52.51,17.08"  # S,W,N,E

LAYERS = {
    "boundary": f'relation["boundary"="administrative"]["admin_level"="8"]["name"="Poznań"];',
    "water": f'(way["natural"="water"]({BB});relation["natural"="water"]({BB});way["waterway"="riverbank"]({BB}););',
    "river": f'way["waterway"="river"]({BB});',
    "green": f'(way["leisure"="park"]({BB});relation["leisure"="park"]({BB});way["landuse"="forest"]({BB});relation["landuse"="forest"]({BB});way["natural"="wood"]({BB});relation["natural"="wood"]({BB});way["landuse"="cemetery"]({BB}););',
    "roads": f'way["highway"~"^(motorway|trunk|primary|secondary)$"]({BB});',
    "rail": f'way["railway"="rail"]["usage"="main"]({BB});',
}


def overpass(body):
    q = f"[out:json][timeout:180];{body}out geom qt;"
    for attempt in range(6):
        req = urllib.request.Request("https://overpass-api.de/api/interpreter",
                                     data=urllib.parse.urlencode({"data": q}).encode(), headers=UA)
        try:
            return json.load(urllib.request.urlopen(req, timeout=240))
        except urllib.error.HTTPError as e:
            if e.code in (429, 504):
                print(f"  serwer zajęty ({e.code}), czekam {30 * (attempt + 1)} s", flush=True)
                time.sleep(30 * (attempt + 1))
                continue
            raise
    raise RuntimeError("Overpass nie odpowiada")


def rings_from_relation(rel):
    """Skleja fragmenty (role outer/inner) w zamknięte pierścienie."""
    out = {"outer": [], "inner": []}
    for role in ("outer", "inner"):
        segs = [[(p["lon"], p["lat"]) for p in m.get("geometry", [])] for m in rel.get("members", [])
                if m.get("type") == "way" and m.get("role", "outer") in ((role,) if role == "inner" else ("outer", ""))]
        segs = [s for s in segs if len(s) > 1]
        while segs:
            ring = segs.pop(0)
            changed = True
            while ring[0] != ring[-1] and changed:
                changed = False
                for i, s in enumerate(segs):
                    if s[0] == ring[-1]:
                        ring += s[1:]
                    elif s[-1] == ring[-1]:
                        ring += s[::-1][1:]
                    elif s[-1] == ring[0]:
                        ring = s[:-1] + ring
                    elif s[0] == ring[0]:
                        ring = s[::-1][:-1] + ring
                    else:
                        continue
                    segs.pop(i)
                    changed = True
                    break
            if len(ring) > 3:
                out[role].append(ring)
    return out


RAW = os.path.join(HERE, "basemap_raw.json")
result = json.load(open(RAW, encoding="utf-8")) if os.path.exists(RAW) else {}
for name, body in LAYERS.items():
    if name in result:
        continue
    print("pobieram", name, "...", flush=True)
    d = overpass(body)
    feats = []
    for e in d["elements"]:
        tags = e.get("tags", {})
        if e["type"] == "way" and "geometry" in e:
            pts = [(p["lon"], p["lat"]) for p in e["geometry"]]
            feats.append({"kind": "way", "tags": {k: tags[k] for k in ("highway", "name", "waterway", "leisure", "landuse", "natural") if k in tags},
                          "closed": pts[0] == pts[-1], "pts": pts})
        elif e["type"] == "relation":
            r = rings_from_relation(e)
            if r["outer"]:
                feats.append({"kind": "poly", "tags": {k: tags[k] for k in ("name", "leisure", "landuse", "natural") if k in tags},
                              "outer": r["outer"], "inner": r["inner"]})
    result[name] = feats
    print(f"  {name}: {len(feats)} obiektów")
    json.dump(result, open(RAW, "w", encoding="utf-8"))
    time.sleep(10)

json.dump(result, open(os.path.join(HERE, "basemap_raw.json"), "w", encoding="utf-8"))
print("zapisano src/basemap_raw.json", os.path.getsize(os.path.join(HERE, "basemap_raw.json")) // 1024, "KB")
