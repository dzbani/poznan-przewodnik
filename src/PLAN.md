# Plan rozbudowy przewodnika (od 29.09.2026)

Zakres ustalony z użytkownikiem: wszystkie atrakcje turystyczne z list poznan.pl
(muzea, kościoły zabytkowe, zabytki, fortyfikacje, jeziora, ważniejsze parki),
BEZ małych parków osiedlowych i BEZ firm rozrywkowych (escape roomy, laser tag,
parki linowe, groty solne). Każda atrakcja: pełna podstrona, dane sprawdzone
w oficjalnym źródle, linki do strony obiektu i źródeł.

Źródła list: https://www.poznan.pl/mim/turystyka/ (kategorie POI)

## Partia 1 — GOTOWE 29.09.2026, artifact v6
- [x] Centrum Szyfrów Enigma
- [x] Fort VII – Muzeum Martyrologii Wielkopolan
- [x] Wielkopolskie Muzeum Wojskowe
- [x] Poznańskie Muzeum Pyry
- [x] Fotoplastykon Poznański
- [x] Akademia Lubrańskiego i Muzeum Archidiecezjalne
- [x] Biblioteka Raczyńskich
- [x] Dawne Kolegium Jezuickie
- [x] Kościół NMP in Summo
- [x] Średniowieczne mury miejskie

## Partia 2 – muzea — GOTOWE 29.09.2026, artifact v7 (MPK zamknięte, GASPAR i Izba PRL bez zdjęcia)
- [x] Muzeum Broni Pancernej
- [x] GASPAR Muzeum Starych Narzędzi i Maszyn
- [x] Muzeum Czekolady
- [x] Muzeum Farmacji
- [x] Muzeum Historii Ubioru
- [x] Muzeum Iluzji, Nauki i Sztuki
- [x] Muzeum Komunikacji Miejskiej MPK
- [x] Muzeum PRL-u
- [x] Przeciwatomowy Schron i Galeria Plakatu
- [x] Izba PRL przy dawnej Hali W7 HCP

## Partia 3 – muzea — GOTOWE 29.09.2026, artifact v8 (PMKC zamknięte; UMP i Makiety bez zdjęcia)
- [x] Muzeum Uniwersytetu Medycznego
- [x] Muzeum Ziemi UAM
- [x] Salon Muzyczny Feliksa Nowowiejskiego
- [x] Poznańskie Muzeum Kultury Cyfrowej
- [x] Muzeum Biżuterii MoJa
- [x] Mieszkanie-Pracownia Kazimiery Iłłakowiczówny
- [x] Makiety dawnego Poznania
- [x] Niewidzialna Ulica
- [x] Pałac Działyńskich
- [x] Bazar

## Partia 4 – kościoły — GOTOWE 29.09.2026, artifact v9 (wszystkie 17 kościołów, nowa kategoria „Kościoły”)
- [x] Kościół Bożego Ciała
- [x] Kościół św. Antoniego z Padwy
- [x] Kościół św. Franciszka Serafickiego
- [x] Kościół św. Jana Jerozolimskiego za Murami
- [x] Kościół św. Józefa
- [x] Kościół św. Małgorzaty
- [x] Kościół św. Marcina
- [x] Kościół NSPJ i MB Pocieszenia
- [x] Kościół Najświętszego Zbawiciela
- [x] Kościół Najświętszej Krwi Pana Jezusa

## Partia 5 – kościoły i forty — GOTOWE 29.09.2026
- [x] Kościół NMP Wspomożenia Wiernych
- [x] Kościół Wszystkich Świętych
- [x] Kościół Matki Boskiej Bolesnej
- [x] Kościół Zmartwychwstania Pańskiego
- [x] Kościół Maryi Królowej
- [x] Kościół św. Jana Vianneya
- [x] Kościół św. Anny
- [x] Twierdza Poznań (przegląd fortów)
- [x] Fort IVa
- [x] Fort Va Bonin

## Partia 6 – przyroda i inne — GOTOWE 29.09.2026, artifact v10 (komplet: 96 atrakcji, 6 kategorii)
- [x] Jezioro Kierskie
- [x] Jezioro Strzeszyńskie
- [x] Szachty
- [x] Łęgi Dębińskie (Park Jana Pawła II)
- [x] Park Wilsona
- [x] Park Chopina
- [x] Park Marcinkowskiego
- [x] Park Mickiewicza
- [x] Okrąglak
- [x] Sezonowe linie turystyczne (zabytkowe tramwaje)

## Etap 7 – „każda informacja + przyjazna strona” (29.09.2026)
- [x] Informacje praktyczne: zdrowie (SOR, NiŚOZ, dentysta, apteki), toalety, taksówki, parkowanie (cennik ZDM), rowery, przewodnicy, pogoda — artifact v12
- [x] Strona O Poznaniu: historia, legendy, gwara, kuchnia, klimat (src/data_guide.py) — v12
- [x] Plany zwiedzania (plany.html): 1/2/3 dni, z dziećmi, deszcz, za darmo, poniedziałek — v12
- [x] Wyszukiwarka, szybkie filtry (bezpłatne/dla dzieci/pod dachem), Top 10, kafelki kategorii, przycisk do góry, nowa nawigacja — v12
- [x] Duże i zabytkowe parki (src/data_parks.py, 29.09.2026): Park Tysiąclecia, Park Rataje + skansen ŚKP, Stare Koryto Warty, Park Szelągowski, Park Kasprowicza (bez zdjęcia), Park nad Wartą, Park Wieniawskiego, Park Moniuszki, Ogród Zamkowy, Rezerwat Meteoryt Morasko, Lasek Marceliński. Pominięte jako osiedlowe/małe: pozostałe pozycje z POI „parki” (m.in. Kasserna, Gorczyński, Manitiusa, Traszki, Heweliusza, Drwęskich, Wodziczki)
- [x] Pomniki i fontanny (src/data_monuments.py, nowa kategoria „pomniki”, 29.09.2026, v14): wszystkie 21+10 pozycji z POI poznan.pl; Czerwiec 1956 przeniesiony do „pomniki”; Paderewski i Wiedźma bez zdjęcia
- [x] Teatry i sale koncertowe — 30.09.2026: strona teatry.html (src/data_theatres.py, 8 scen, bez repertuaru i cen spektakli), Teatr Wielki jako atrakcja w „zabytki” (zwiedzanie Za kulisami 10 zł)
- [ ] Rozrywka komercyjna (nietypowe atrakcje) — user nie zaprzeczył przy ostatnim doprecyzowaniu

## Mapa atrakcji — GOTOWE 29.09.2026, artifact v26
- [x] mapa.html: Leaflet 1.9.4 (cdnjs) + własny podkład img/mapa-podklad.svg (dane OSM, ODbL; zewnętrzne kafelki blokuje CSP artefaktu)
- [x] Współrzędne wszystkich 137 atrakcji w src/coords.json (Nominatim + Overpass, ręczne poprawki; "approx": true = przybliżone)
- [x] Filtry jak na stronie głównej, lista, dymki z linkiem do podstrony, mapa.html#<slug> otwiera atrakcję
- [x] Znaczniki wersji ?v= przy style.css/site.js/map.js (przeglądarki trzymały stary CSS)
- Nowa atrakcja = dopisać współrzędne: python src/geocode.py (pomija istniejące) i sprawdzić wynik
- Podkład odświeżyć: python src/fetch_basemap.py (usuń basemap_raw.json) && python src/render_basemap.py

## Kalendarz wydarzeń — GOTOWE 30.09.2026
- [x] kalendarz.html z src/data_events.py (CALENDAR, 14 wydarzeń), sekcja „Nadchodzące wydarzenia” na stronie głównej liczona z kalendarza
- [x] site.js: zakończone edycje oznaczone wg daty w przeglądarce, kalendarz zaczyna się od bieżącego miesiąca
- Pominięte: Jarmark Świętojański (nie odbył się 2024 i 2025), „Poznań za pół ceny” (miasto zrezygnowało)
- Do uzupełnienia: termin Betlejem Poznańskiego 2026/27 (Plac Wolności, Stary Rynek); terminy 2027 po ogłoszeniu (pole dates)

## Wycieczki za miasto — partia 1 GOTOWE 30.09.2026
- [x] Nowa kategoria „wycieczki” (src/data_trips.py, TRIPS): Zamek w Kórniku, Arboretum Kórnickie, Pałac w Rogalinie, Katedra Gnieźnieńska, MPPP w Gnieźnie, Ostrów Lednicki, Biskupin, Wielkopolski Park Narodowy, Muzeum Rolnictwa w Szreniawie, Muzeum Fiedlera
- [x] Pole trip (lat, lon, getting): panel „Dojazd z Poznania”, odległość od Starego Rynku, trasa z dworca Poznań Główny; kategoria poza mapą (OFF_MAP w build.py)
- [ ] Partia 2 (propozycje): Wielkopolski Park Etnograficzny w Dziekanowicach, Zamek w Gołuchowie, Parowozownia Wolsztyn, Pałac w Śmiełowie, Grody Piastowskie?
- Uwaga: sezonowe — Zamek Kórnik do 30.11, Ostrów Lednicki 12.04–31.10, Szreniawa zimą tylko grupy

## Mapa na kafelkach OpenStreetMap — GOTOWE 30.09.2026
- [x] map.js: L.tileLayer tile.openstreetmap.org zamiast własnego podkładu SVG (na GitHub Pages nie ma CSP artefaktu), bez ograniczenia do granic Poznania, zoom 8–18
- [x] Wycieczki za miasto na mapie (współrzędne z pola trip), po wybraniu kategorii mapa dopasowuje widok (fitVisible)
- NIEUŻYWANE od teraz: img/mapa-podklad.svg, src/fetch_basemap.py, src/render_basemap.py, src/basemap_raw.json — można usunąć
