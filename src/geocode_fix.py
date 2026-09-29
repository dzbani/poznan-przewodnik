# -*- coding: utf-8 -*-
"""Druga runda geokodowania: precyzyjne zapytania dla braków i błędnych trafień."""
import json, os, time, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "coords.json")
UA = {"User-Agent": "PoznanPrzewodnik/1.0 (+https://github.com/dzbani/poznan-przewodnik)"}
data = json.load(open(OUT, encoding="utf-8"))
WRONG = ["pomnik-czerwca-1956", "pomnik-mickiewicza", "pomnik-jana-pawla-ii", "pomnik-kochanowskiego", "pomnik-paderewskiego",
         "pomnik-ratajskiego", "pomnik-komedy", "twierdza-poznan", "fontanna-z-delfinami", "pomnik-marcinkowskiego",
         "studzienka-bamberki", "kosciol-nmp-in-summo"]
for s in WRONG:
    data.pop(s, None)
Q = {
 "ostrow-tumski": ["Bazylika Archikatedralna Świętych Apostołów Piotra i Pawła, Poznań", "Katedra, Ostrów Tumski, Poznań"],
 "genius-loci": ["Rezerwat Archeologiczny Genius Loci, Poznań", "Posadzego 3, Poznań"],
 "mury-miejskie": ["Baszta Katarzynek, Poznań", "Mury obronne, Wroniecka, Poznań"],
 "pomnik-starego-marycha": ["Stary Marych, Poznań", "Pomnik Starego Marycha"],
 "pomnik-zygi-latarnika": ["Zyga Latarnik, Poznań", "Pomnik Zygi Latarnika"],
 "pomnik-kryptologow": ["Pomnik Kryptologów, Poznań", "Pomnik Pogromców Enigmy"],
 "pomnik-janickiego": ["Pomnik Klemensa Janickiego", "Klemens Janicki, Poznań"],
 "pomnik-cegielskiego": ["Pomnik Hipolita Cegielskiego", "Hipolit Cegielski, Poznań"],
 "pomnik-kosciuszki": ["Pomnik Tadeusza Kościuszki, Poznań", "Tadeusz Kościuszko, Grunwaldzka, Poznań"],
 "fontanna-park-wilsona": ["Fontanna, Park Wilsona, Poznań"],
 "kosciol-sw-antoniego": ["Kościół pw. św. Antoniego Padewskiego, Poznań", "Franciszkańska 2, Poznań"],
 "kosciol-bernardynow": ["Kościół pw. św. Franciszka Serafickiego, Poznań", "Garbary 22, Poznań"],
 "kosciol-jana-jerozolimskiego": ["Kościół pw. św. Jana Jerozolimskiego za Murami, Poznań", "Świętojańska 1, Poznań"],
 "kosciol-sw-jozefa": ["Kościół pw. św. Józefa, Działowa, Poznań", "Działowa 25, Poznań"],
 "kosciol-sw-malgorzaty": ["Kościół pw. św. Małgorzaty, Poznań", "Rynek Śródecki, Poznań"],
 "kosciol-dominikanow": ["Kościół Dominikanów, Szewska, Poznań", "Szewska 18, Poznań"],
 "kosciol-wspomozenia-wiernych": ["Kościół pw. Najświętszej Maryi Panny Wspomożenia Wiernych, Poznań", "Wroniecka 9, Poznań"],
 "kosciol-jana-vianneya": ["Kościół pw. św. Jana Vianneya, Poznań", "Podlaska 10, Poznań"],
 "fotoplastykon": ["Fotoplastykon Poznański", "Ratajczaka 44, Poznań"],
 "akademia-lubranskiego": ["Akademia Lubrańskiego, Poznań", "Lubrańskiego 1, Poznań"],
 "muzeum-iluzji": ["Muzeum Iluzji, Poznań", "Woźna 19, Poznań"],
 "muzeum-komunikacji-mpk": ["Głogowska 131, Poznań"],
 "muzeum-prl": ["Muzeum PRL-u, Poznań", "Żydowska 4, Poznań"],
 "schron-przeciwatomowy": ["Słupska 62, Poznań"],
 "gaspar": ["Oliwkowa 12, Poznań"],
 "izba-prl-w7": ["Hetmańska 90, Poznań"],
 "muzeum-ump": ["Bukowska 70, Poznań"],
 "muzeum-ziemi": ["Muzeum Ziemi, Poznań", "Bogumiła Krygowskiego 10, Poznań"],
 "muzeum-kultury-cyfrowej": ["Błękitna 1, Poznań"],
 "muzeum-bizuterii-moja": ["27 Grudnia 17, Poznań"],
 "makiety-dawnego-poznania": ["Makiety Dawnego Poznania", "Ludgardy 1, Poznań"],
 "niewidzialna-ulica": ["Niewidzialna Ulica, Poznań", "Jana Matejki 53, Poznań"],
 "legi-debinskie": ["Park Jana Pawła II, Poznań", "Łęgi Dębińskie, Poznań"],
 "park-rataje": ["Park Rataje, Poznań", "Skansen Średzkiej Kolei Powiatowej"],
 "linie-turystyczne": ["Biblioteka Uniwersytecka, Ratajczaka, Poznań"],
 "srodka": ["Rynek Śródecki, Poznań"],
 "stadion": ["Stadion Miejski, Bułgarska, Poznań", "Bułgarska 17, Poznań"],
 "pomnik-czerwca-1956": ["Pomnik Ofiar Czerwca 1956, Poznań", "Poznańskie Krzyże"],
 "pomnik-mickiewicza": ["Pomnik Adama Mickiewicza, Plac Adama Mickiewicza, Poznań"],
 "pomnik-jana-pawla-ii": ["Pomnik Jana Pawła II, Ostrów Tumski, Poznań", "Pomnik św. Jana Pawła II, Poznań"],
 "pomnik-kochanowskiego": ["Pomnik Jana Kochanowskiego, Ostrów Tumski", "Obelisk Jana Kochanowskiego, Poznań"],
 "pomnik-paderewskiego": ["Pomnik Ignacego Jana Paderewskiego, Święty Marcin, Poznań", "Święty Marcin 87, Poznań"],
 "pomnik-ratajskiego": ["Pomnik Cyryla Ratajskiego, Plac Andersa", "Plac Władysława Andersa, Poznań"],
 "pomnik-komedy": ["Pomnik Krzysztofa Komedy, Przybyszewskiego, Poznań", "Przybyszewskiego 37a, Poznań"],
 "twierdza-poznan": ["Kaponiera Kolejowa, Poznań", "Rondo Kaponiera, Poznań"],
 "fontanna-z-delfinami": ["Fontanna z delfinami, Poznań", "Studzienka Kronthala"],
 "pomnik-marcinkowskiego": ["Pomnik Karola Marcinkowskiego, Aleje Marcinkowskiego, Poznań"],
 "studzienka-bamberki": ["Studzienka Bamberki, Poznań", "Bamberka, Stary Rynek, Poznań"],
 "kosciol-nmp-in-summo": ["Kościół Najświętszej Marii Panny, Ostrów Tumski, Poznań", "Kościół NMP in Summo"],
}
for slug, qs in Q.items():
    if slug in data:
        continue
    for q in qs:
        u = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
            {"q": q, "format": "jsonv2", "limit": 1, "viewbox": "16.70,52.52,17.10,52.24", "bounded": 1, "accept-language": "pl"})
        time.sleep(1.1)
        try:
            r = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA)))
        except Exception as e:
            print("BŁĄD", slug, e); r = []
        if r:
            r = r[0]
            data[slug] = dict(lat=round(float(r["lat"]), 6), lon=round(float(r["lon"]), 6), q=q, name=r["display_name"][:120])
            print(f"{slug:30} {q[:48]:48} -> {r['display_name'][:75]}")
            break
    else:
        print(f"{slug:30} BRAK")
    json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("gotowe:", len(data))
