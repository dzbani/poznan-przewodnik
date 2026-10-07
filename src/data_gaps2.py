# -*- coding: utf-8 -*-
"""Uzupełnienie luk, część 2 (06.10.2026): Podziemia Katedry, Most Biskupa Jordana, Rynek Śródecki, Lasek Katyński.
Źródła: strona Katedry Poznańskiej, poznan.pl, Wikipedia. Opisy streszczone własnymi słowami."""

P = "https://www.poznan.pl/mim/wortals/turystyka/"

GAPS2 = [
    dict(
        slug="podziemia-katedry", cat="zabytki", name="Podziemia Katedry Poznańskiej",
        img="podziemia-katedry", img_alt="Relikty dawnych budowli w podziemiach Katedry Poznańskiej",
        short="Relikty katedry przedromańskiej i romańskiej, pozostałości grobowców Mieszka I i Chrobrego oraz misa z X wieku.",
        badge="Sezonowo, płatne",
        status=None,
        lead="Pod Katedrą Poznańską zachowały się fragmenty wcześniejszych budowli, odkryte podczas badań archeologicznych prowadzonych przy odbudowie świątyni po II wojnie światowej. To jedno z najważniejszych miejsc początków państwa polskiego.",
        sections=[
            ("Co zobaczyć", [
                "Fragmenty katedry przedromańskiej i romańskiej: mury z kamienia łamanego i przedromańskie bazy kolumn.",
                "Relikty grobowców, najprawdopodobniej pierwszych władców Polski: Mieszka I i Bolesława Chrobrego.",
                "Relikt misy z X wieku, być może chrzcielnicy, z której mógł przyjąć chrzest Mieszko I wraz z poddanymi. Według innej hipotezy misa służyła do rozrabiania wapna.",
                "Lapidarium z fragmentami nagrobków, płyt i epitafiów oraz krypta, w której od 1963 roku spoczywają arcybiskupi i biskupi pomocniczy poznańscy.",
                "Przy wejściu wiszą plansze prof. Zofii Kurnatowskiej o dziejach katedry i Ostrowa Tumskiego, a podczas zwiedzania wyświetlany jest film.",
            ]),
            ("Historia odkryć", [
                "Główne odkrycia pochodzą z badań w 1946 roku i w latach 1951–1956, prowadzonych równolegle z odbudową katedry (1946–1956). Ujawniły one wcześniejsze fazy budowy świątyni, starsze od gotyku.",
            ]),
            ("Warto wiedzieć", [
                "Bilet kupuje się w punkcie obsługi turystycznej na terenie katedry lub w zakrystii. Katedra jest czynnym kościołem: nie zwiedza się jej podczas mszy, nabożeństw i koncertów, obowiązuje odpowiedni strój i cisza.",
                "Poza kryptami można wejść na wieżę widokową katedry. Więcej o samej katedrze i Ostrowie Tumskim jest na osobnej stronie.",
            ]),
        ],
        address="Ostrów Tumski 17, 61-109 Poznań",
        hours=[
            ("Sezon (1.03–15.11), dni powszednie", "9:00–16:00"),
            ("Sezon (1.03–15.11), niedziele", "14:00–18:00"),
            ("Zima", "podziemia zamknięte (poznan.pl)"),
        ],
        tickets=[
            ("Normalny", "10 zł"),
            ("Ulgowy", "8 zł"),
            ("Rodzinny", "25 zł"),
        ],
        phone="+48 61 852 96 42",
        www=("katedra.archpoznan.pl", "https://www.katedra.archpoznan.pl/turysci-w-katedrze/"),
        credit="podziemia-katedry",
        sources=[
            ("Katedra Poznańska: Turyści w katedrze", "https://www.katedra.archpoznan.pl/turysci-w-katedrze/"),
            ("poznan.pl: Podziemia Katedry Poznańskiej", P + "muzea-w-poznaniu,poi,202/podziemia-katedry-poznanskiej,51395.html"),
            ("Wikipedia: Archikatedra w Poznaniu", "https://pl.wikipedia.org/wiki/Bazylika_archikatedralna_Świętych_Apostołów_Piotra_i_Pawła_w_Poznaniu"),
        ],
        checked="06.10.2026",
    ),
    dict(
        slug="most-biskupa-jordana", cat="zabytki", name="Most Biskupa Jordana",
        img="most-biskupa-jordana", img_alt="Most Biskupa Jordana z widokiem na Katedrę Poznańską",
        short="Kładka pieszo-rowerowa nad Cybiną między Śródką a Ostrowem Tumskim, na miejscu przeprawy sprzed tysiąca lat.",
        badge="Bezpłatnie",
        status=None,
        lead="Most Biskupa Jordana, zwany też Cybińskim lub Śródeckim, to kładka pieszo-rowerowa nad rzeką Cybiną. Łączy Śródkę (ul. Ostrówek) z Ostrowem Tumskim i prowadzi prosto na widok katedry.",
        sections=[
            ("Historia przeprawy", [
                "Przeprawa w tym miejscu istniała od wczesnego średniowiecza. W 2007 roku odkryto relikty mostu z X wieku (37 dębowych elementów), a najstarsza wzmianka o mostach pochodzi z 1146 roku.",
                "W 1905 roku oddano stalowy most kratownicowy z torami tramwajowymi, a 13 listopada 1913 roku otwarto nowszy. Wysadziły go 5 września 1939 roku wycofujące się oddziały Wojska Polskiego. W 1970 roku ostatnią, tymczasową przeprawę rozebrano, bo ruch przejął most Mieszka I. Przerwano wtedy trakt używany od prawie tysiąca lat.",
            ]),
            ("Nowy most", [
                "Nowy most oficjalnie otwarto 7 grudnia 2007 roku. Wykorzystano w nim stalowe przęsło nurtowe z rozebranego mostu Rocha. Przęsło o rozpiętości 70 m i wadze 450 ton przeniesiono nad mostem Mieszka I, a ten moment 29 września 2007 roku oglądały setki poznaniaków.",
                "Od stycznia 2008 roku po moście biegnie też droga rowerowa. Nazwa upamiętnia Jordana, pierwszego biskupa Poznania i Polski.",
            ]),
            ("Warto wiedzieć", [
                "Na poręczach wiszą kłódki zakochanych, a most jest popularnym miejscem sesji ślubnych. Z mostu widać Katedrę Poznańską.",
            ]),
        ],
        address="ul. Ostrówek, 61-125 Poznań (Śródka – Ostrów Tumski)",
        hours=[("Most", "dostępny całą dobę")],
        tickets=[("Przejście", "bezpłatnie")],
        phone=None,
        www=("Wikipedia", "https://pl.wikipedia.org/wiki/Most_Biskupa_Jordana_w_Poznaniu"),
        credit="most-biskupa-jordana",
        sources=[
            ("Wikipedia: Most Biskupa Jordana w Poznaniu", "https://pl.wikipedia.org/wiki/Most_Biskupa_Jordana_w_Poznaniu"),
        ],
        checked="06.10.2026",
    ),
    dict(
        slug="rynek-srodecki", cat="zabytki", name="Rynek Śródecki",
        img="rynek-srodecki", img_alt="Rynek Śródecki i ulica Filipińska na Śródce",
        short="Dawny główny plac Śródki z kościołem św. Małgorzaty, klasztorem filipinów i muralem 3D.",
        badge="Bezpłatnie",
        status=None,
        lead="Rynek Śródecki był centralnym placem Śródki, dawnego osobnego miasta, które dziś jest dzielnicą Poznania. Przed wiekami stał tu własny ratusz, a do lat 60. XX wieku rynek miał większą powierzchnię niż Stary Rynek.",
        sections=[
            ("Historia", [
                "Ratusz stał w miejscu dzisiejszej kamienicy z pocztą. Rynek zmniejszył się, gdy powstała trasa Chwaliszewska (ul. Wyszyńskiego) i zburzono część kamienic: południową pierzeję i jedną kamienicę pierzei wschodniej. Dużą część zabudowy zniszczyła wcześniej wojna.",
                "Do 2010 roku stało przy rynku kino Malta.",
            ]),
            ("Co zobaczyć", [
                "Kościół św. Małgorzaty i klasztor filipinów przy rynku.",
                "Trójwymiarowy mural „Opowieść śródecka z trębaczem na dachu i kotem w tle”, odsłonięty 1 października 2015 roku na kamienicy przy ul. Śródka 3. Powstał na podstawie zdjęcia z lat 20. XX wieku.",
                "Tablicę odsłoniętą 27 grudnia 1998 roku, w 80. rocznicę Powstania Wielkopolskiego, na budynku pod nr. 15.",
            ]),
            ("Warto wiedzieć", [
                "Z rynku odchodzą ulice Bydgoska, Filipińska, Śródka i Wyszyńskiego. Do Mostu Biskupa Jordana i Ostrowa Tumskiego dojdziesz stąd pieszo.",
            ]),
        ],
        address="Rynek Śródecki, 61-125 Poznań",
        hours=[("Plac", "dostępny całą dobę")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None,
        www=("Wikipedia", "https://pl.wikipedia.org/wiki/Rynek_Śródecki"),
        credit="rynek-srodecki",
        sources=[
            ("Wikipedia: Rynek Śródecki", "https://pl.wikipedia.org/wiki/Rynek_Śródecki"),
            ("poznan.pl: Trójwymiarowy mural na Śródce", "https://www.poznan.pl/mim/info/news/trojwymiarowy-mural-na-srodce,85708.html"),
        ],
        checked="06.10.2026",
    ),
    dict(
        slug="lasek-katynski", cat="pomniki", name="Lasek Katyński",
        img=None, img_alt="",
        short="116 dębów czerwonych przy Forcie VII upamiętnia mieszkańców Wielkopolski zamordowanych przez NKWD w 1940 roku.",
        badge="Bezpłatnie",
        status=None,
        lead="Lasek Katyński powstał w sąsiedztwie Fortu VII, w którym mieści się Muzeum Martyrologii Wielkopolan. Symbolicznie przypomina o ponad 22 tysiącach polskich oficerów, policjantów, naukowców, duchownych i innych osób zamordowanych w 1940 roku.",
        sections=[
            ("Dęby Pamięci", [
                "W lasku posadzono 116 dębów czerwonych, po jednym dla każdej z 116 osób z Poznania i Wielkopolski zamordowanych w Katyniu, Charkowie i Miednoje. Tyle rodzin ze Stowarzyszenia „Katyń” w Poznaniu czekało na upamiętnienie swoich bliskich.",
                "Dęby posadzono w 2020 roku na prośbę Stowarzyszenia „Katyń” w Poznaniu, za pieniądze miasta. Drzewa stoją w szachownicowym układzie, który symbolizuje wojskowy porządek. Jesienią liście dębów czerwonych przybierają odcienie czerwieni, brązu i złota.",
            ]),
            ("Tablice", [
                "Przy drodze do Fortu VII stoi tablica informacyjna ufundowana przez Poznański Oddział IPN.",
                "18 września 2026 roku obok dębów pojawiły się granitowe płyty z imieniem i nazwiskiem ofiary, datą urodzenia i miejscem śmierci, a tam gdzie pozwalała dokumentacja, także ze stopniem wojskowym. Kody QR prowadzą do serwisu „Katyń 1940” z życiorysami.",
            ]),
            ("Warto wiedzieć", [
                "Lasek leży tuż obok Fortu VII, dawnego niemieckiego obozu, który dziś jest Muzeum Martyrologii Wielkopolan. Oba miejsca łatwo połączyć w jednej wizycie.",
            ]),
        ],
        address="ul. Polska (obok Fortu VII), 60-595 Poznań",
        hours=[("Teren", "ogólnodostępny")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None,
        www=("poznan.pl", P + "parki,poi,3338/lasek-katynski,86720.html"),
        credit=None,
        sources=[
            ("poznan.pl: Lasek Katyński", P + "parki,poi,3338/lasek-katynski,86720.html"),
            ("poznan.pl: W sąsiedztwie Fortu VII zasadzono dęby pamięci", "https://www.poznan.pl/mim/info/news/w-sasiedztwie-fortu-vii-zasadzono-deby-pamieci,141103.html"),
            ("poznan.pl: 116 dębów pamięci", "https://www.poznan.pl/mim/brm/news,1202/inicjatywy-radnych,c,13/116-debow-pamieci,153082.html"),
            ("TenPoznan.pl: granitowe tablice w Lasku Katyńskim (22.09.2026)", "https://tenpoznan.pl/imiona-i-nazwiska-ofiar-zbrodni-katynskiej-wyryto-na-granitowych-tablicach/"),
        ],
        checked="06.10.2026",
    ),
]
