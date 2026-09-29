# -*- coding: utf-8 -*-
"""Rysuje podkład mapy (img/mapa-podklad.svg) z src/basemap_raw.json.
Rzut Web Mercator, ten sam prostokąt co w fetch_basemap.py, więc Leaflet może go nałożyć jako imageOverlay.
Dane © autorzy OpenStreetMap (ODbL). Uruchom: python src/render_basemap.py"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
S, W, N, E = 52.25, 16.72, 52.51, 17.08
R = 6378137.0
UNIT = 10.0  # 1 jednostka SVG = 10 m w rzucie Mercatora


def merc(lon, lat):
    return R * math.radians(lon), R * math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))


X0, Y1 = merc(W, N)
X1, Y0 = merc(E, S)
VW, VH = round((X1 - X0) / UNIT), round((Y1 - Y0) / UNIT)


def proj(pt):
    x, y = merc(*pt)
    return (x - X0) / UNIT, (Y1 - y) / UNIT


def simplify(pts, tol):
    """Douglas-Peucker."""
    if len(pts) < 3:
        return pts
    (ax, ay), (bx, by) = pts[0], pts[-1]
    dx, dy = bx - ax, by - ay
    L = math.hypot(dx, dy) or 1e-9
    dmax, idx = 0, 0
    for i in range(1, len(pts) - 1):
        px, py = pts[i]
        d = abs(dy * px - dx * py + bx * ay - by * ax) / L if (dx or dy) else math.hypot(px - ax, py - ay)
        if d > dmax:
            dmax, idx = d, i
    if dmax > tol:
        return simplify(pts[:idx + 1], tol)[:-1] + simplify(pts[idx:], tol)
    return [pts[0], pts[-1]]


def area(pts):
    return abs(sum(pts[i][0] * pts[i + 1][1] - pts[i + 1][0] * pts[i][1] for i in range(len(pts) - 1))) / 2


def d_ring(pts, tol, closed=True, min_area=0):
    p = simplify([proj(q) for q in pts], tol)
    if closed and (len(p) < 4 or area(p) < min_area):
        return ""
    s = "M" + " ".join(f"{x:.0f} {y:.0f}" for x, y in p)
    return s + ("Z" if closed else "")


raw = json.load(open(os.path.join(HERE, "basemap_raw.json"), encoding="utf-8"))


def polys(layer, tol, min_area, pred=lambda t: True):
    out = []
    for f in raw[layer]:
        if not pred(f["tags"]):
            continue
        if f["kind"] == "way" and f["closed"]:
            d = d_ring(f["pts"], tol, True, min_area)
        elif f["kind"] == "poly":
            d = "".join(d_ring(r, tol, True, min_area) for r in f["outer"])
            if d:
                d += "".join(d_ring(r, tol, True, min_area / 4) for r in f["inner"])
        else:
            continue
        if d:
            out.append(d)
    return out


def lines(layer, tol, pred=lambda t: True):
    out = []
    for f in raw[layer]:
        if f["kind"] == "way" and pred(f["tags"]):
            d = d_ring(f["pts"], tol, False)
            if d:
                out.append(d)
    return out


green = polys("green", 0.8, 60)                     # parki, lasy, cmentarze > ok. 0,6 ha
water = polys("water", 0.6, 25)
rivers = lines("river", 0.6)
roads_major = lines("roads", 0.6, lambda t: t.get("highway") in ("motorway", "trunk", "primary"))
roads_minor = lines("roads", 0.6, lambda t: t.get("highway") == "secondary")
rail = lines("rail", 0.8)
boundary = [d for d in polys("boundary", 0.8, 0)][:1]

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VW} {VH}" width="{VW}" height="{VH}">',
       '<title>Podkład mapy Poznania. Dane © autorzy OpenStreetMap (ODbL)</title>',
       f'<rect width="{VW}" height="{VH}" fill="#F3EEE4"/>']
if boundary:
    svg.append(f'<path d="{boundary[0]}" fill="#FBF8F2" fill-rule="evenodd"/>')
svg.append(f'<path d="{"".join(green)}" fill="#DCE8CF" fill-rule="evenodd"/>')
svg.append(f'<path d="{"".join(rail)}" fill="none" stroke="#C9BFB0" stroke-width="3" stroke-dasharray="10 7"/>')
svg.append(f'<path d="{"".join(roads_minor)}" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
svg.append(f'<path d="{"".join(roads_major)}" fill="none" stroke="#E6D8B8" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>')
svg.append(f'<path d="{"".join(roads_major)}" fill="none" stroke="#FFFDF7" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/>')
svg.append(f'<path d="{"".join(rivers)}" fill="none" stroke="#A9CBE0" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
svg.append(f'<path d="{"".join(water)}" fill="#A9CBE0" fill-rule="evenodd"/>')
if boundary:
    svg.append(f'<path d="{boundary[0]}" fill="none" stroke="#B8912F" stroke-width="4" stroke-dasharray="18 10" stroke-opacity="0.7"/>')
svg.append('</svg>')

out = os.path.join(ROOT, "img", "mapa-podklad.svg")
open(out, "w", encoding="utf-8").write("\n".join(svg))
print(out, os.path.getsize(out) // 1024, "KB", f"viewBox {VW}x{VH}",
      "| zieleń", len(green), "woda", len(water), "rzeki", len(rivers), "drogi", len(roads_major) + len(roads_minor), "tory", len(rail))
