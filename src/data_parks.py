# -*- coding: utf-8 -*-
"""Etap 7, partia parków (29.09.2026): duże i zabytkowe parki oraz tereny zielone.
Źródła: portal miasta poznan.pl (kategoria Parki), Instytut Obserwatorium
Astronomiczne UAM, PTOP „Salamandra”, Wikipedia. Opisy streszczone własnymi słowami.
Celowo bez numerów linii i przystanków (na podstronie jest link „Trasa komunikacją”)."""

P = "https://www.poznan.pl/mim/wortals/wortal,2024/parki,poi,3338/"

PARKS = [
    dict(
        slug="park-tysiaclecia", cat="przyroda", name="Park Tysiąclecia",
        img="park-tysiaclecia", img_alt="Głazy pamiątkowe w Parku Tysiąclecia jesienią",
        short="Leśny park na Nowym Mieście z 28 pamiątkowymi głazami, amfiteatrem i miasteczkiem ruchu drogowego.",
        badge="Bezpłatnie",
        status=None,
        lead="Park Tysiąclecia ma 26,3 hektara. Urządzono go na terenie leśnym, w miejscu dawnej strzelnicy wojskowej i dawnego cmentarza przy ulicy Świętojańskiej.",
        sections=[
            ("Historia", [
                "Pierwsze plany parku pojawiły się w 1928 roku, a w 1931 roku ogłoszono konkurs na zagospodarowanie tak zwanego Cybińskiego Klina Zieleni. Prace ruszyły dopiero po odbudowie miasta ze zniszczeń wojennych.",
                "Park otwarto 16 lipca 1966 roku jako pierwszy z pięciu nowo projektowanych parków miejskich. Prace wykończeniowe trwały do 1970 roku.",
            ]),
            ("Co zobaczyć", [
                "28 pomników z głazów narzutowych rozstawionych wzdłuż alejek.",
                "Niewielki amfiteatr i szerokie aleje spacerowe z zatoczkami, w których stoją ławki.",
            ]),
            ("Dla rodzin", [
                "W północnej części parku jest miasteczko ruchu drogowego, gdzie dzieci uczą się przepisów jako piesi i rowerzyści. Przydaje się też przed egzaminem na kartę rowerową.",
                "Duży plac zabaw, trampoliny, siłownia plenerowa i miejsce do wyprowadzania psów.",
            ]),
        ],
        address="ul. Termalna / ul. Komandoria, Poznań",
        hours=[("Park", "ogólnodostępny")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", P + "park-tysiaclecia,51954.html"),
        credit="park-tysiaclecia",
        sources=[("poznan.pl: Park Tysiąclecia", P + "park-tysiaclecia,51954.html")],
    ),
    dict(
        slug="park-rataje", cat="przyroda", name="Park Rataje i skansen kolejki",
        img="park-rataje", img_alt="Parowóz w skansenie Średzkiej Kolei Powiatowej w Parku Rataje",
        short="Drugi co do wielkości park Poznania: ogród zmysłów i skansen kolejki z parowozem, który w południe „buchnie” dymem.",
        badge="Bezpłatnie",
        status=None,
        lead="Park Rataje, otwarty w 2018 roku na pograniczu Rataj i Żegrza, jest drugim co do wielkości parkiem w Poznaniu, po Cytadeli. Podzielono go na dziewięć stref tematycznych: rekreacyjnych, edukacyjnych i historycznych.",
        sections=[
            ("Skansen Średzkiej Kolei Powiatowej", [
                "W centralnej części parku, niedaleko kościoła Nawiedzenia NMP, stoją dwa parowozy: wąskotorowy Dn2t „Baziel” i Tkt48-130 z wagonem restauracyjnym dawnego WARS-u. Obok są fragment torów, rogatki, semafor mechaniczny, żuraw wodny, kozioł oporowy i zabytkowy zegar stacyjny.",
                "Codziennie o 12:00, a latem także o 14:00 i 16:00, parowóz wąskotorowy wypuszcza dym i gwiżdże.",
                "Skansen upamiętnia kolej zbudowaną od 1898 roku. Wąskotorowa linia główna prowadziła z Kobylegopola do Środy Wielkopolskiej i Zaniemyśla i wiozła przede wszystkim buraki cukrowe. Po przejęciu przez PKP w 1949 roku kolej stopniowo likwidowano. Do dziś kursuje tylko odcinek Środa Wielkopolska – Zaniemyśl.",
            ]),
            ("Co jeszcze zobaczyć", [
                "Ogród zmysłów, czyli ogrody tematyczne działające na wzrok, słuch, węch, smak i dotyk, ze ścieżką sensoryczną.",
                "Aleję drzew pamięci, alejki spacerowe i rowerowe oraz polanę piknikową.",
            ]),
            ("Dla rodzin", [
                "Plac zabaw z dużą kolorową ciuchcią obok skansenu, tor parkour, terenowy park rowerowy (pumptrack), siłownia plenerowa, boisko i wybieg dla psów.",
            ]),
        ],
        address="os. Rzeczypospolitej / os. Polan, Poznań",
        hours=[("Park", "ogólnodostępny"), ("Pokaz parowozu", "codziennie 12:00; latem także 14:00 i 16:00")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", P + "park-rataje,86717.html"),
        credit="park-rataje",
        sources=[("poznan.pl: Park Rataje", P + "park-rataje,86717.html")],
    ),
    dict(
        slug="stare-koryto-warty", cat="przyroda", name="Park Stare Koryto Warty",
        img="stare-koryto-warty", img_alt="Amfiteatr w Parku Stare Koryto Warty",
        short="Park w miejscu zasypanego koryta Warty, między Starym Miastem a Ostrowem Tumskim. Amfiteatr, fontanna, plac zabaw.",
        badge="Bezpłatnie",
        status=None,
        lead="Park Stare Koryto Warty na Chwaliszewie powstał w miejscu dawnego koryta rzeki, zasypanego w latach 60. XX wieku. Otwarto go w 2016 roku. Ma blisko 3 hektary.",
        sections=[
            ("Pomysł na park", [
                "Projekt pracowni 1050 nawiązuje do meandrów rzeki i roślinności dolin rzecznych. Na osi dawnego koryta celowo nie posadzono drzew, żeby było widać, którędy płynęła Warta. Drzewa rosną tylko na obrzeżach.",
                "Posadzono ponad 100 drzew, 16 tysięcy krzewów i około 10 tysięcy bylin i traw ozdobnych, dobranych tak, żeby park dobrze wyglądał także zimą.",
            ]),
            ("Co zobaczyć", [
                "Amfiteatr, plac z fontanną i ścieżki spacerowe.",
                "Pawilon dawnej „Nowej Gazowni” przy ulicy Ewangelickiej. Od 2018 roku działa w nim „Pawilon”, miejsce kulturalne prowadzone przez Galerię Miejską Arsenał.",
                "Tablicę z 2021 roku upamiętniającą poznańskich kawalerów Orderu Uśmiechu.",
            ]),
            ("Dla rodzin", [
                "Plac zabaw z 2017 roku z osobną strefą „Labirynt” dla dzieci w wieku 1–3 lata. Urządzenia są dostosowane także do dzieci z niepełnosprawnościami. Są trampoliny, ścianka wspinaczkowa, zjazd linowy i podesty grające.",
                "W parku są dwie toalety automatyczne.",
            ]),
        ],
        address="pl. Międzymoście / ul. Ewangelicka, Poznań",
        hours=[("Park", "ogólnodostępny")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", P + "park-stare-koryto-warty,62630.html"),
        credit="stare-koryto-warty",
        sources=[("poznan.pl: Park Stare Koryto Warty", P + "park-stare-koryto-warty,62630.html")],
    ),
    dict(
        slug="park-szelagowski", cat="przyroda", name="Park Szelągowski",
        img="park-szelagowski", img_alt="Ruiny dawnych schodów w Parku Szelągowskim",
        short="Zabytkowy park na skarpie nad Wartą, obok Cytadeli: widoki na dolinę rzeki, ruiny schodów i żelaziste źródełko.",
        badge="Bezpłatnie",
        status=None,
        lead="Park Szelągowski leży na skarpie doliny Warty, na Szelągu, i sąsiaduje z Parkiem Cytadela. Z jego zbocza rozciągają się widoki na dolinę rzeki.",
        sections=[
            ("Historia", [
                "Nazwa pochodzi od kupieckiej rodziny Szylingów. Najsłynniejszy z nich, burmistrz Mikołaj Szyling, założył tu w XVI wieku fabrykę prochu. Od początku XIX wieku okolica była ulubionym celem wycieczek poznaniaków.",
                "W 1922 roku teren kupiło Bractwo Kurkowe i urządziło Ogród Strzelecki z największą w Polsce krytą strzelnicą i tarasami restauracyjnymi na kilka tysięcy gości.",
                "W czerwcu 1945 roku odbyły się tu pierwsze powojenne Wianki. Po wojnie teren podupadł, a w 2009 roku park uporządkowano.",
            ]),
            ("Co zobaczyć", [
                "Ruiny monumentalnych schodów prowadzących w stronę rzeki.",
                "Małe źródełko wody żelazistej, które barwi ziemię na rdzawy kolor.",
                "Okazałe topole czarne o obwodzie do sześciu metrów, platan klonolistny i aleję kasztanowców.",
                "Pomnik Bractwa Kurkowego z 2017 roku i Dom Weterana, przykład późnego modernizmu.",
            ]),
            ("Warto wiedzieć", [
                "Wzdłuż parku biegnie Wartostrada, więc łatwo połączyć spacer z Cytadelą i bulwarami nad Wartą.",
            ]),
        ],
        address="ul. Szelągowska, Poznań",
        hours=[("Park", "ogólnodostępny")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", P + "park-szelagowski,86695.html"),
        credit="park-szelagowski",
        sources=[("poznan.pl: Park Szelągowski", P + "park-szelagowski,86695.html")],
    ),
    dict(
        slug="park-kasprowicza", cat="przyroda", name="Park Kasprowicza",
        img=None, img_alt="",
        short="Park na Łazarzu przy hali Arena, z obeliskiem poety, placami zabaw i stolikami do szachów.",
        badge="Bezpłatnie",
        status=None,
        lead="Park Kasprowicza leży na Łazarzu, między ulicami Reymonta, Wyspiańskiego, Jarochowskiego i Chociszewskiego. Ma 9,3 hektara i urządzono go w latach 1936–1939.",
        sections=[
            ("Historia", [
                "W czasie okupacji Niemcy zdewastowali park, bo planowali przenieść tu poznańskie zoo. Na początku lat 60. XX wieku teren uporządkowano i posadzono nowe drzewa i krzewy.",
            ]),
            ("Co zobaczyć", [
                "Halę widowiskowo-sportową Arena, stojącą na terenie parku.",
                "Kamienny obelisk z płaskorzeźbą twarzy Jana Kasprowicza autorstwa Edwarda Haupta z 1967 roku, na rogu ulic Jarochowskiego i Niegolewskich.",
            ]),
            ("Dla rodzin", [
                "Dwa place zabaw, siłownia plenerowa, street workout, stoliki do gry w szachy i warcaby, stół do ping-ponga i wybieg dla psów.",
            ]),
        ],
        address="ul. Reymonta / ul. Jarochowskiego, Poznań",
        hours=[("Park", "ogólnodostępny")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", P + "park-jana-kasprowicza,51948.html"),
        credit=None,
        sources=[("poznan.pl: Park Jana Kasprowicza", P + "park-jana-kasprowicza,51948.html")],
    ),
    dict(
        slug="park-nad-warta", cat="przyroda", name="Park nad Wartą",
        img="park-nad-warta", img_alt="Aleja w Parku nad Wartą zimą",
        short="Jeden z największych parków Poznania: 17 hektarów nadrzecznego lasu, staw i przystanie kajakowe.",
        badge="Bezpłatnie",
        status=None,
        lead="Park nad Wartą ma nieco ponad 17 hektarów. Ciągnie się wzdłuż wschodniego brzegu Warty, od ulicy Krzywoustego do ulicy Hetmańskiej, obok osiedla Piastowskiego na Ratajach.",
        sections=[
            ("Co zobaczyć", [
                "Park ma naturalny, leśny charakter: rosną tu kasztanowce, wierzby i topole. W centralnej części jest staw.",
                "Nad rzeką stoją przystanie kajakowe klubów wioślarskich i kajakowych, m.in. KS Posnania, Polonii, Warty, Energetyka i AZS.",
            ]),
            ("Sport i rodzina", [
                "Trzy place zabaw, boisko do piłki i siatkówki plażowej, skatepark, street workout, korty tenisowe i kręgielnia.",
            ]),
        ],
        address="wzdłuż Warty, przy os. Piastowskim, Poznań",
        hours=[("Park", "ogólnodostępny")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", P + "park-nad-warta,86712.html"),
        credit="park-nad-warta",
        sources=[("poznan.pl: Park nad Wartą", P + "park-nad-warta,86712.html")],
    ),
    dict(
        slug="park-wieniawskiego", cat="przyroda", name="Park Wieniawskiego",
        img="park-wieniawskiego", img_alt="Trawniki i alejki Parku Wieniawskiego",
        short="Zabytkowy park przy Teatrze Wielkim, zwany dawniej „Teatralką”, z górką saneczkową.",
        badge="Bezpłatnie",
        status=None,
        lead="Park Wieniawskiego, w okresie międzywojennym nazywany „Teatralką”, leży w centrum Poznania, w północnej części Dzielnicy Cesarskiej, tuż obok Teatru Wielkiego. Założono go w latach 1907–1910.",
        sections=[
            ("Co zobaczyć", [
                "Górkę saneczkową w południowej części parku, na której szczycie zachowały się dawne elementy małej architektury.",
                "Pawilon gastronomiczny nazywany tradycyjnie Stajenką Pegaza, co nawiązuje do sąsiedztwa teatru.",
                "Około 260 drzew 34 gatunków. Najcenniejsze są oliwnik wąskolistny i wiązowiec zachodni.",
                "W zachodniej części parku stoi nieczynna, zabytkowa nastawnia kolejowa.",
            ]),
            ("Sąsiedztwo", [
                "Od ulicy Fredry park graniczy z dawnym Bankiem Listów Zastawnych i willą Adolfa Landsberga, a od południa z pomnikiem Polskiego Państwa Podziemnego.",
            ]),
        ],
        address="ul. Wieniawskiego / ul. Fredry, Poznań",
        hours=[("Park", "ogólnodostępny")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", P + "park-henryka-wieniawskiego,51956.html"),
        credit="park-wieniawskiego",
        sources=[("poznan.pl: Park Henryka Wieniawskiego", P + "park-henryka-wieniawskiego,51956.html")],
    ),
    dict(
        slug="park-moniuszki", cat="przyroda", name="Park Moniuszki",
        img="park-moniuszki", img_alt="Drzewa w Parku Moniuszki",
        short="Jeden z najstarszych parków miejskich Poznania, kameralny, w samym centrum, z popiersiem kompozytora.",
        badge="Bezpłatnie",
        status=None,
        lead="Park Moniuszki to zabytkowy park o powierzchni 2,2 hektara w centrum Poznania, między ulicami Libelta, Noskowskiego, Chopina i aleją Niepodległości.",
        sections=[
            ("Historia", [
                "Powstał około 1870 roku jako ogród prywatny. W 1906 roku miasto wykupiło grunty i zamieniło ogród w park publiczny.",
                "Nosił imię Goethego, w 1919 roku stał się Parkiem Miejskim, a od 1921 roku jest parkiem Stanisława Moniuszki. Stary drzewostan mocno ucierpiał w 1945 roku podczas walk o pobliską Cytadelę.",
            ]),
            ("Co zobaczyć", [
                "Popiersie Moniuszki z 1924 roku, ufundowane przez chóry Wielkopolskiego Związku Kół Śpiewaczych. Zniszczone w czasie okupacji, zostało odtworzone po wojnie przez Edwarda Haupta.",
                "Graby i dęby. To spokojne miejsce na odpoczynek w śródmieściu, kilka minut od Zamku Cesarskiego.",
            ]),
        ],
        address="ul. Libelta / ul. Chopina, Poznań",
        hours=[("Park", "ogólnodostępny")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", P + "park-stanislawa-moniuszki,51952.html"),
        credit="park-moniuszki",
        sources=[("poznan.pl: Park Stanisława Moniuszki", P + "park-stanislawa-moniuszki,51952.html")],
    ),
    dict(
        slug="ogrod-zamkowy", cat="przyroda", name="Ogród Zamkowy",
        img="ogrod-zamkowy", img_alt="Pomnik Katyński w Ogrodzie Zamkowym",
        short="Dawny prywatny ogród cesarza Wilhelma II przy Zamku Cesarskim, z Pomnikiem Katyńskim i rzeźbą Abakanowicz.",
        badge="Bezpłatnie",
        status=None,
        lead="Ogród Zamkowy im. Ofiar Katynia i Sybiru to dawny prywatny ogród rezydencji cesarza Wilhelma II, przy północnej ścianie Zamku Cesarskiego, na rogu alei Niepodległości i ulicy Fredry.",
        sections=[
            ("Historia", [
                "Częścią ogrodu był Ogród Różany z fontanną Lwów. Główna część pełniła rolę kameralnego „salonu” z półkolistym placykiem i aleją lipową. Ogród był symetrycznym odbiciem Parku Mickiewicza po drugiej stronie alei Niepodległości.",
                "W latach 2001–2004 ogród odnowiono i odtworzono kute ogrodzenia. Obecną nazwę nosi od 2014 roku.",
            ]),
            ("Co zobaczyć", [
                "Pomnik Ofiar Katynia i Sybiru (Pomnik Katyński) Roberta Sobocińskiego.",
                "Rzeźbę Magdaleny Abakanowicz „5 Figur” w Dziedzińcu Różanym.",
                "Ławeczkę archeologa Józefa Kostrzewskiego.",
                "Chroniony od 2024 roku platan klonolistny o obwodzie 411 cm.",
            ]),
        ],
        address="ul. Fredry / al. Niepodległości, Poznań",
        hours=[("Ogród", "teren ogrodzony – godzin otwarcia nie podano w źródle")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", P + "park-ogrod-zamkowy-im-ofiar-katynia-i-sybiru,86632.html"),
        credit="ogrod-zamkowy",
        sources=[("poznan.pl: Ogród Zamkowy im. Ofiar Katynia i Sybiru", P + "park-ogrod-zamkowy-im-ofiar-katynia-i-sybiru,86632.html")],
    ),
    dict(
        slug="morasko", cat="przyroda", name="Rezerwat Meteoryt Morasko",
        img="morasko", img_alt="Las w rezerwacie Meteoryt Morasko",
        short="Kratery po deszczu meteorytów sprzed ok. 5 tys. lat i Góra Moraska, najwyższe wzniesienie Poznania.",
        badge="Bezpłatnie",
        status=None,
        lead="Rezerwat przyrody Meteoryt Morasko, utworzony w 1976 roku, leży na północnym skraju Poznania, przy granicy z Suchym Lasem. Chroni kratery, które według większości badaczy powstały po upadku żelaznych meteorytów około 5 tysięcy lat temu, oraz fragment lasu dębowo-grabowego.",
        sections=[
            ("Kratery i meteoryty", [
                "W rezerwacie jest kilka kraterów. Największy ma kilkadziesiąt metrów średnicy i ponad 11 metrów głębokości, a część z nich wypełnia woda.",
                "Pierwszy meteoryt znaleziono tu w 1914 roku. Kolejne odnajdywane są do dziś. W 2012 roku wykopano meteoryt o masie około 261 kg, największy znany w Polsce.",
                "Poznań to jedno z nielicznych miast na świecie, które mają w swoich granicach kratery meteorytowe.",
            ]),
            ("Przyroda", [
                "Większość rezerwatu porasta grąd, czyli las dębowo-grabowy. Wiosną kwitną tu m.in. lilia złotogłów, kopytnik i konwalia.",
                "W wypełnionych wodą kraterach wiosną gromadzą się płazy, m.in. traszki i kumak nizinny. Z ptaków żyją tu dzięcioł czarny i kruk.",
                "W rezerwacie wznosi się Góra Moraska, najwyższe wzniesienie Poznania, oraz jeziorko Zimna Woda.",
            ]),
            ("Warto wiedzieć", [
                "Przez rezerwat prowadzą szlak turystyczny i ścieżka dydaktyczna z tablicami, przygotowane przez Obserwatorium Astronomiczne UAM i Towarzystwo „Salamandra”.",
                "W rezerwacie wolno chodzić tylko po wyznaczonych szlakach. Nie wolno zbierać roślin ani szukać meteorytów.",
                "Zabierz wygodne buty: to spacer leśnymi ścieżkami, bez infrastruktury parkowej.",
            ]),
        ],
        address="Morasko, północna granica Poznania",
        hours=[("Rezerwat", "dostępny, tylko wyznaczonymi szlakami")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("UAM – ścieżka dydaktyczna", "https://www.astro.amu.edu.pl/en/outreach/mor-cra/"),
        credit="morasko",
        sources=[
            ("Instytut Obserwatorium Astronomiczne UAM: ścieżka w rezerwacie", "https://www.astro.amu.edu.pl/en/outreach/mor-cra/"),
            ("PTOP „Salamandra”: Rezerwat Meteoryt Morasko", "https://www.salamandra.org.pl/rezerwat.html"),
            ("Wikipedia: Rezerwat przyrody Meteoryt Morasko", "https://pl.wikipedia.org/wiki/Rezerwat_przyrody_Meteoryt_Morasko"),
        ],
    ),
    dict(
        slug="lasek-marcelinski", cat="przyroda", name="Lasek Marceliński",
        img="lasek-marcelinski", img_alt="Lasek Marceliński jesienią",
        short="Ponad 200 hektarów miejskiego lasu na zachodzie Poznania: ścieżka przyrodnicza, górka saneczkowa, trasy rowerowe.",
        badge="Bezpłatnie",
        status=None,
        lead="Lasek Marceliński, przez przyrodników nazywany Uroczyskiem Marcelin, to miejski las w zachodniej części Poznania, między osiedlem Bajkowym a cmentarzem na Junikowie. Powstał po II wojnie światowej na dawnych polach uprawnych i zajmuje ponad 200 hektarów.",
        sections=[
            ("Co robić", [
                "Spacerować i jeździć na rowerze: las ma kilkanaście kilometrów dróg i ścieżek gruntowych. Biegnie przez niego też szlak konny.",
                "Przejść ścieżkę przyrodniczo-leśną z dwiema pętlami, o długości 2,9 i 2,1 km. Zaczyna się przy leśniczówce Marcelin i siedzibie Zarządu Zieleni Miejskiej przy ulicy Strzegomskiej.",
                "Wejść na górkę saneczkowo-rowerową, usypaną z dawnych odpadów przemysłowych. Zimą zjeżdżają z niej dzieci na sankach, latem rowerzyści.",
            ]),
            ("Warto wiedzieć", [
                "Przy polanie z górką rośnie okazały wiąz szypułkowy, przesadzony tu w 2002 roku z centrum Poznania.",
                "Przy ścieżce jest śródleśny staw z polaną i ławkami. W lesie są też place zabaw.",
                "Parking jest przy ulicy Strzegomskiej. Rowerem można tu dojechać drogami rowerowymi, m.in. od strony stadionu.",
            ]),
        ],
        address="ul. Strzegomska, Poznań",
        hours=[("Las", "ogólnodostępny")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", "https://www.poznan.pl/mim/main/-,p,35473,35918,35919.html"),
        credit="lasek-marcelinski",
        sources=[
            ("poznan.pl: Rowerem po Lasku Marcelińskim", "https://www.poznan.pl/mim/main/-,p,35473,35918,35919.html"),
            ("Wikipedia: Lasek Marceliński", "https://pl.wikipedia.org/wiki/Lasek_Marceli%C5%84ski"),
        ],
    ),
]
