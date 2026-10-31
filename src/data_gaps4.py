# -*- coding: utf-8 -*-
"""Uzupełnienie luk, partia 4 (19.10.2026): Lodowisko Malta (sezonowe lodowisko POSiR przy Torze Regatowym Malta).
Godziny, ceny i zasady pochodzą ze stron POSiR Poznań, sprawdzonych 19.10.2026 (pola sources).
Pole see_also: lista (etykieta, ścieżka względem katalogu głównego bez .html)."""

POSIR = "https://posir.poznan.pl/"

GAPS4 = [
    dict(
        slug="lodowisko-malta", cat="rodzina", name="Lodowisko Malta",
        img="lodowisko-malta", img_alt="Łyżwiarze na lodzie w namiocie Lodowiska Malta (zdjęcie z 2016 roku)",
        short="Sezonowe lodowisko w namiocie przy Torze Regatowym Malta. Sezon 2026/27 ruszył 10 października.",
        badge="Sezonowo, płatne",
        status=("warning", "1 listopada 2026 lodowiska POSiR są nieczynne (komunikat POSiR z 28.10.2026)."),
        lead="Lodowisko Malta to sezonowe lodowisko Poznańskich Ośrodków Sportu i Rekreacji w namiocie przy starcie Toru Regatowego Malta. Nowy sezon łyżwiarski ruszył tu w sobotę 10 października 2026 roku.",
        sections=[
            ("Co tu jest", [
                "Lodowisko pod dachem namiotu, otwarte codziennie, także wieczorem. Można wypożyczyć łyżwy, kaski i jeździki (podpórki dla początkujących w kształcie pingwina, misia lub foki). Działa też punkt ostrzenia łyżew.",
                "W sezonie co tydzień, w piątki i soboty w godzinach 19:00–23:00, odbywają się imprezy Ice Party z poznańskimi DJ-ami. Ceny osobnego biletu POSiR nie podaje, obowiązuje cennik lodowiska.",
                "Na stronie lodowiska jest też podstrona z informacjami o nauce jazdy na łyżwach.",
            ]),
            ("Warto wiedzieć", [
                "Bilet obejmuje 60 minut jazdy. Po przekroczeniu godziny pobierana jest dopłata za każdą rozpoczętą minutę (cena biletu podzielona przez 60). Przy wcześniejszym wyjściu pieniądze nie są zwracane.",
                "Lód jest czyszczony trzy razy dziennie, po 30 minut: o 12:30, 15:30 i 18:30. W tym czasie nie można jeździć, więc w dni powszednie bilet „po 15:30” działa od 16:00.",
                "Rodziny z poznańską Kartą Dużej Rodziny płacą 75% ceny biletu. Posiadacze karty OK Poznań mogą wejść za 1 zł w ramach rocznej puli wejść na obiekty POSiR. Karty MultiSport i FitProfit dają wejście na lód bez opłaty. Zniżkę lub wejście dają też m.in. Poznańska Karta Turystyczna, Poznańska Złota Karta i Medicover Sport (zasady zależą od karty). Żadna z kart nie obejmuje wypożyczalni. Honorowi Dawcy Krwi i dawcy przeszczepu mają 20% rabatu na bilet. Zniżek nie można łączyć.",
                "Drugie lodowisko sezonowe POSiR działa w Hali Sportowej Wilda (ul. o. Mariana Żelazka 1a), codziennie 7:00–21:45, według komunikatu POSiR z tymi samymi cenami biletów.",
                "Zdjęcie na tej stronie pochodzi z 2016 roku, a lodowisko stoi w namiocie, więc dziś może wyglądać nieco inaczej.",
            ]),
        ],
        address="przy starcie Toru Regatowego Malta, ul. Jana Pawła II (od ul. Baraniaka), Poznań",
        hours=[("Niedziela–czwartek", "8:00–22:00"), ("Piątek–sobota", "8:00–23:00"),
               ("Przerwy na czyszczenie lodu", "12:30–13:00, 15:30–16:00, 18:30–19:00")],
        tickets=[("Normalny, pn–pt do 15:30 (60 min)", "16 zł"), ("Ulgowy, pn–pt do 15:30 (60 min)", "11 zł"),
                 ("Normalny, po 15:30 oraz sb, nd i święta (60 min)", "24 zł"), ("Ulgowy, po 15:30 oraz sb, nd i święta (60 min)", "19 zł"),
                 ("Bilet rodzinny (3 osoby)", "46 zł w dni powszednie, 54 zł w weekendy"),
                 ("Bilet dodatkowy do rodzinnego", "11 zł w dni powszednie, 16 zł w weekendy"),
                 ("Senior, poniedziałki", "5 zł za godzinę"),
                 ("Karnet 10-godzinny", "ulgowy 140 zł, normalny 200 zł"),
                 ("Karnet 40-godzinny", "ulgowy 500 zł, normalny 700 zł"),
                 ("Nauka jazdy (60 min)", "od 140 zł, strony POSiR podają różne kwoty, potwierdź telefonicznie"),
                 ("Wypożyczenie łyżew", "18 zł"), ("Wypożyczenie kasku", "9 zł"), ("Jeździk dla początkujących", "20 zł"),
                 ("Ostrzenie łyżew", "24 zł"), ("Szafka", "6 zł")],
        phone="+48 502 859 940", www=("posir.poznan.pl", POSIR + "obiekty/malta/lodowisko"),
        credit="lodowisko-malta",
        sources=[
            ("POSiR Poznań: Lodowisko Malta", POSIR + "obiekty/malta/lodowisko"),
            ("POSiR Poznań: cennik Lodowiska Malta", POSIR + "obiekty/malta/lodowisko/cennik"),
            ("POSiR Poznań: Od 10 października ruszają sezonowe lodowiska w Poznaniu", POSIR + "aktualnosci/od-10-pazdziernika-ruszaja-sezonowe-lodowiska-w-poznaniu"),
        ],
        see_also=[("Jezioro Maltańskie", "atrakcje/jezioro-maltanskie"),
                  ("Malta Ski: stok, tor saneczkowy, kolejka górska", "atrakcje/malta-ski"),
                  ("Termy Maltańskie", "atrakcje/termy-maltanskie")],
        checked="31.10.2026",
    ),
]
