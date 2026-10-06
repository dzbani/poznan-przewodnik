# -*- coding: utf-8 -*-
"""Wycieczki za miasto, partia 2 (06.10.2026): Gołuchów, Śmiełów, Dziekanowice, Wolsztyn.
Godziny i ceny ze stron obiektów (sprawdzone 06.10.2026), historia streszczona z Wikipedii.
Pułapki: godziny Wielkopolskiego Parku Etnograficznego są tylko na grafice muzeum (m-WPE.jpg);
cennik Parowozowni Wolsztyn obowiązuje od 1.01.2025 (nowszego nie ma na stronie);
poznan.pl i inne serwisy podają dla tych obiektów nieaktualne godziny."""

TRIPS2 = [
    dict(
        slug="zamek-goluchow", cat="wycieczki", name="Zamek w Gołuchowie",
        img="zamek-goluchow", img_alt="Zamek w Gołuchowie z basztami i dachami łupkowymi",
        short="Renesansowy zamek przebudowany dla Izabelli Czartoryskiej, z wnętrzami i zbiorami sztuki. We wtorki wstęp wolny.",
        badge="Wt–nd",
        status=None,
        lead="Zamek w Gołuchowie zbudowano w latach 1550–1560 dla Rafała Leszczyńskiego. W XIX wieku odbudowała go Izabella z Czartoryskich Działyńska i urządziła w nim muzeum. Dziś mieści się tu oddział Muzeum Narodowego w Poznaniu, a wokół rozciąga się park z arboretum.",
        sections=[
            ("Historia", [
                "Wczesnorenesansowy zamek z wieżami w narożach zbudowano w latach 1550–1560. W początkach XVII wieku, za Wacława Leszczyńskiego, dostał rezydencjonalne skrzydła i arkadowe loggie. W 1695 roku Leszczyńscy sprzedali Gołuchów Suskim, a kolejni właściciele doprowadzili zamek do ruiny.",
                "Ruiny kupił w 1856 roku Tytus Działyński (część źródeł podaje 1853) jako prezent ślubny dla syna Jana Kantego i Izabelli z Czartoryskich. Izabella odbudowała zamek w latach 1875–1885, częściowo według szkiców Eugène'a Viollet-le-Duca. Projekt końcowy przygotował francuski architekt Maurycy Auguste Ouradou.",
                "Od 1951 roku w zamku działa oddział Muzeum Narodowego w Poznaniu. W grudniu 2016 roku zamek kupił od Fundacji Książąt Czartoryskich Skarb Państwa.",
            ]),
            ("Co zobaczyć", [
                "Zabytkowe wnętrza z włoskimi, francuskimi i hiszpańskimi kominkami, obramieniami okien i mozaikami.",
                "Zbiory sztuki zgromadzone przez Izabellę Czartoryską, m.in. „Ostatnią wieczerzę” Fransa Florisa z XVI wieku oraz kolekcję waz greckich.",
                "Park-arboretum o powierzchni 158 ha z rzadkimi drzewami oraz kaplicę-mauzoleum z 1892 roku, w której spoczywa Izabella.",
            ]),
            ("Warto wiedzieć", [
                "Wejścia odbywają się co pół godziny, w grupach do 30 osób. Ostatnie wejście jesienią i zimą (wt–pt) jest o 15:00, a w lipcu i sierpniu o 16:00.",
                "Zwiedzanie z przewodnikiem jest możliwe tylko po wcześniejszej rezerwacji telefonicznej lub mailowej. Budynek ma trzy kondygnacje i nie ma windy, a przy wejściu głównym są schody.",
            ]),
        ],
        address="ul. Działyńskich 2, 63-322 Gołuchów",
        hours=[
            ("Wt–nd, 1.01–30.06 i 1.09–31.12", "9:00–16:00"),
            ("Wt–pt, 1.07–31.08", "9:00–16:00"),
            ("Sb–nd, 1.07–31.08", "10:00–17:00"),
            ("Poniedziałek", "nieczynne"),
        ],
        tickets=[
            ("Normalny", "20 zł"), ("Ulgowy", "13 zł"), ("Wiek 8–26 lat", "1 zł"),
            ("Dzieci do 7 lat", "bezpłatnie"), ("Przewodnik (do 30 osób)", "150 zł plus bilety"),
            ("Wtorek", "bezpłatnie"),
        ],
        phone="+48 62 761 50 94", www=("mnp.art.pl", "https://mnp.art.pl/profile/wizyta-muzeum-zamek-w-goluchowie"),
        credit="zamek-goluchow",
        trip=dict(lat=51.852639, lon=17.933336, getting=[
            ("Komunikacja", "Połączenie z Poznania sprawdź w wyszukiwarce tras (link powyżej)."),
        ]),
        sources=[("Muzeum Narodowe w Poznaniu: wizyta w Muzeum Zamek w Gołuchowie (godziny, ceny 2026)", "https://mnp.art.pl/profile/wizyta-muzeum-zamek-w-goluchowie"),
                 ("Wikipedia: Zamek w Gołuchowie", "https://pl.wikipedia.org/wiki/Zamek_w_Gołuchowie")],
    ),
    dict(
        slug="palac-smielow", cat="wycieczki", name="Pałac w Śmiełowie (Muzeum Mickiewicza)",
        img="palac-smielow", img_alt="Klasycystyczny pałac w Śmiełowie z jońskim portykiem",
        short="Klasycystyczny pałac z końca XVIII wieku, w którym w 1831 roku mieszkał Mickiewicz. Muzeum i park. We wtorki wstęp wolny.",
        badge="Wt–nd",
        status=None,
        lead="Pałac w Śmiełowie to klasycystyczna rezydencja z końca XVIII wieku, zaprojektowana przez Stanisława Zawadzkiego. W sierpniu 1831 roku zatrzymał się w niej Adam Mickiewicz. Od 1970 roku pałac należy do Muzeum Narodowego w Poznaniu i jest muzeum poety.",
        sections=[
            ("Pałac i park", [
                "Budynek ma monumentalny portyk joński i neopalladiańskie galerie arkadowe. Do pałacu dochodzą charakterystyczne oficyny z dachami mansardowymi.",
                "Wokół rozciąga się około 14 hektarów parku w stylu angielskim. Podobno Mickiewicz posadził tu w 1831 roku dąb, symbol odrodzenia Polski.",
            ]),
            ("Muzeum", [
                "Muzeum łączy pamiątki związane z Mickiewiczem z historią samego pałacu i jego dawnych właścicieli.",
            ]),
            ("Warto wiedzieć", [
                "Kasa zamyka się 30 minut przed zamknięciem muzeum. Budynek nie ma windy, przy wejściu głównym są schody, a toaleta nie jest dostosowana do osób z niepełnosprawnościami.",
                "Muzeum jest nieczynne m.in. 1 stycznia, w Wielkanoc, w Boże Ciało, 1 listopada oraz 24–26 i 31 grudnia. W dni 6 stycznia, 1 maja, 3 maja, 15 sierpnia i 11 listopada obowiązują godziny niedzielne.",
            ]),
        ],
        address="Śmiełów 1, 63-210 Żerków",
        hours=[
            ("Wt–pt", "9:00–16:00"), ("Sb–nd", "10:00–16:00"), ("Poniedziałek", "nieczynne"),
        ],
        tickets=[
            ("Normalny", "15 zł"), ("Ulgowy", "10 zł"), ("Wiek 8–26 lat", "1 zł"), ("Wtorek", "bezpłatnie"),
        ],
        phone="+48 62 740 31 64", www=("mnp.art.pl", "https://mnp.art.pl/profile/wizyta-muzeum-mickiewicza-w-smielowie"),
        credit="palac-smielow",
        trip=dict(lat=52.10645, lon=17.5712, getting=[
            ("Komunikacja", "Połączenie z Poznania sprawdź w wyszukiwarce tras (link powyżej)."),
        ]),
        sources=[("Muzeum Narodowe w Poznaniu: wizyta w Muzeum Mickiewicza w Śmiełowie (godziny, ceny 2026)", "https://mnp.art.pl/profile/wizyta-muzeum-mickiewicza-w-smielowie"),
                 ("Muzeum Narodowe w Poznaniu: Muzeum A. Mickiewicza w Śmiełowie", "https://mnp.art.pl/en/oddzialy/muzeum-a-mickiewicza-w-smielowie/"),
                 ("Wikipedia: Pałac w Śmiełowie", "https://pl.wikipedia.org/wiki/Pałac_w_Śmiełowie")],
    ),
    dict(
        slug="wpe-dziekanowice", cat="wycieczki", name="Wielkopolski Park Etnograficzny w Dziekanowicach",
        img="wpe-dziekanowice", img_alt="Strzechą kryta chata i stodoła w skansenie w Dziekanowicach",
        short="Skansen dawnej wielkopolskiej wsi nad jeziorem Lednica: chaty, kościół, młyn i wiatraki. Czynny od kwietnia do października.",
        badge="Kwiecień–październik",
        status=("warning", "Park jest czynny od 12 kwietnia do 31 października. Od 2 listopada do 11 kwietnia jest zamknięty (wszystkie oddziały muzeum są nieczynne od 21 grudnia do 2 marca)."),
        lead="Wielkopolski Park Etnograficzny w Dziekanowicach to skansen, który pokazuje tradycyjną wieś wielkopolską z przełomu XIX i XX wieku. Należy do Muzeum Pierwszych Piastów na Lednicy i leży nad jeziorem Lednica, niedaleko Ostrowa Lednickiego.",
        sections=[
            ("O skansenie", [
                "Budowę zaczęto 29 września 1975 roku, pierwszą ekspozycję udostępniono 1 czerwca 1982 roku, a status muzeum park uzyskał 25 maja 1993 roku.",
                "W skansenie stoją domy, budynki gospodarcze i stodoły z wyposażeniem. Najstarsze obiekty pochodzą z 1602 roku, a najmłodsze z 1935 roku.",
            ]),
            ("Co zobaczyć", [
                "Zagrody wiejskie, drewniany kościół i kaplicę.",
                "Barokowy dwór z folwarkiem, karczmę, młyn wodny i wiatraki.",
                "Wnętrza zagród z oryginalnym wyposażeniem, pokazujące życie i pracę dawnej wsi.",
            ]),
            ("Warto wiedzieć", [
                "Bilety sprzedaje się do 45 minut przed zamknięciem ekspozycji, a bilety z audioprzewodnikiem do godziny przed zamknięciem. Przerwy w kasie: wt–pt 12:40–13:00, w weekendy i święta 13:40–14:00.",
                "Parking jest bezpłatny. Przewodnika i lekcje muzealne rezerwuje się mailowo (wpe@lednica.pl).",
                "Ostrów Lednicki jest w tym samym muzeum, ma podobne godziny, ale własne bilety.",
            ]),
        ],
        address="Dziekanowice 32, 62-261 Lednogóra",
        hours=[
            ("Wt–pt, 12.04–31.10", "9:00–17:00"),
            ("Sb–nd i święta, 12.04–30.04 i 1.09–31.10", "10:00–17:00"),
            ("Sb–nd i święta, 1.05–31.08", "10:00–18:00"),
            ("Poniedziałek", "nieczynne"),
            ("1.11–11.04", "nieczynne"),
        ],
        tickets=[
            ("Normalny", "25 zł (z audioprzewodnikiem 35 zł)"),
            ("Ulgowy", "17 zł (z audioprzewodnikiem 20 zł)"),
            ("Dzieci do 7 lat", "bezpłatnie"),
            ("Czwartek", "bezpłatnie"),
        ],
        phone="+48 61 427 50 10", www=("lednicamuzeum.pl", "https://lednicamuzeum.pl/strona,wielkopolski-park-etnograficzny-w-dziekanowicach.html"),
        credit="wpe-dziekanowice",
        trip=dict(lat=52.514211, lon=17.38155, getting=[
            ("Samochód", "Parking na terenie parku jest bezpłatny."),
            ("Komunikacja", "Połączenie z Poznania sprawdź w wyszukiwarce tras (link powyżej)."),
        ]),
        sources=[("Muzeum Pierwszych Piastów na Lednicy: godziny otwarcia i bilety 2026", "https://lednicamuzeum.pl/strona,godziny-otwarcia.html"),
                 ("Muzeum Pierwszych Piastów na Lednicy: Wielkopolski Park Etnograficzny", "https://lednicamuzeum.pl/strona,wielkopolski-park-etnograficzny-w-dziekanowicach.html"),
                 ("Muzeum Pierwszych Piastów na Lednicy: godziny WPE (grafika 2026)", "https://lednicamuzeum.pl/files/2026/Godziny%20otwarcia/m-WPE.jpg"),
                 ("Wikipedia: Wielkopolski Park Etnograficzny w Dziekanowicach", "https://pl.wikipedia.org/wiki/Wielkopolski_Park_Etnograficzny_w_Dziekanowicach")],
    ),
    dict(
        slug="parowozownia-wolsztyn", cat="wycieczki", name="Parowozownia Wolsztyn",
        img="parowozownia-wolsztyn", img_alt="Półkolista parowozownia w Wolsztynie z obrotnicą",
        short="Czynna parowozownia z 1907 roku, skąd wyjeżdżają parowozy z pociągami pasażerskimi. Zwiedzanie codziennie 7:00–16:00.",
        badge="Codziennie",
        status=None,
        lead="Parowozownia w Wolsztynie to czynna stacja parowozów, z której do dziś wyjeżdżają pociągi z lokomotywą parową. Halę z wieżą ciśnień zbudowano w 1907 roku. To nie skansen, tylko żywe miejsce, gdzie przygotowuje się parowozy do jazdy.",
        sections=[
            ("Historia", [
                "W 1907 roku powstała czterotorowa hala parowozowa z wieżą ciśnień, w 1912 roku 16-metrowa obrotnica, a w 1949 roku powiększono ją do 20 m. W 1991 roku parowozownię przemianowano na Parowozownię Wolsztyn i zorganizowano pierwszą Paradę Parowozów.",
                "29 czerwca 2016 roku utworzono tu instytucję kultury, a 15 maja 2017 roku wznowiono regularne przewozy pasażerskie. Od 2004 roku odbywa się też konkurs Miss Świata Parowozów.",
            ]),
            ("Co zobaczyć", [
                "Około 20 lokomotyw różnych serii, w tym słynny parowóz Pm36-2 „Piękna Helena”. W regularnej służbie jeździ powojenny parowóz Pt47-65.",
                "Zabytkową obrotnicę, wieżę ciśnień i małe muzeum z dawnymi biletami, sygnalizacją i latarniami kolejarzy oraz makietą fragmentu stacji Wolsztyn.",
                "Co roku na przełomie kwietnia i maja odbywa się Parada Parowozów (jubileuszowa, 30. edycja miała miejsce 2 maja 2026 roku).",
            ]),
            ("Warto wiedzieć", [
                "Strona parowozowni radzi przyjść krótko przed odjazdem lokomotywy, żeby zobaczyć tradycyjne przygotowanie parowozu do drogi.",
                "Pociągi z parowozem jeżdżą na trasie Poznań–Wolsztyn. W ruchu planowym nie kursują w niedziele i święta. Bilety kupisz na stronie Kolei Wielkopolskich, w kasie na dworcu lub u kierownika pociągu. Rozkład jest na stronie parowozowni.",
                "Cennik na stronie parowozowni obowiązuje od 1 stycznia 2025 roku. Zwiedzanie z przewodnikiem wymaga wcześniejszej rezerwacji.",
            ]),
        ],
        address="ul. Fabryczna 1, 64-200 Wolsztyn",
        hours=[
            ("Codziennie, także w niedziele i święta", "7:00–16:00"),
            ("Ostatnie wejście", "15:00"),
        ],
        tickets=[
            ("Normalny", "20 zł"), ("Ulgowy", "15 zł"), ("Przewodnik (rezerwacja)", "80 zł"),
            ("Dzieci do 7 lat", "bezpłatnie"),
        ],
        phone="+48 506 985 166", www=("parowozowniawolsztyn.pl", "https://www.parowozowniawolsztyn.pl/"),
        credit="parowozownia-wolsztyn",
        trip=dict(lat=52.106184, lon=16.112819, getting=[
            ("Pociąg", "Z Poznania Głównego do Wolsztyna jeżdżą pociągi Kolei Wielkopolskich, część kursów obsługuje parowóz (rozkład na stronie parowozowni)."),
            ("Komunikacja", "Połączenie z Poznania sprawdź w wyszukiwarce tras (link powyżej)."),
        ]),
        sources=[("Parowozownia Wolsztyn: strona główna (godziny od 1.10.2026)", "https://www.parowozowniawolsztyn.pl/"),
                 ("Parowozownia Wolsztyn: godziny otwarcia", "https://parowozowniawolsztyn.pl/?page_id=2131"),
                 ("Parowozownia Wolsztyn: ceny biletów (cennik od 1.01.2025)", "https://parowozowniawolsztyn.pl/?page_id=2136"),
                 ("Parowozownia Wolsztyn: rozkład jazdy parowozów", "https://parowozowniawolsztyn.pl/?page_id=2141"),
                 ("Wikipedia: Parowozownia Wolsztyn", "https://pl.wikipedia.org/wiki/Parowozownia_Wolsztyn")],
    ),
    dict(
        slug="zagroda-zwierzat-goluchow", cat="wycieczki", name="Pokazowa Zagroda Zwierząt w Gołuchowie",
        img="zagroda-zwierzat-goluchow", img_alt="Żubr w Pokazowej Zagrodzie Zwierząt w Gołuchowie",
        short="Ponad 20 ha lasu, w którym żyją żubry, koniki polskie, daniele i dziki. Wstęp bezpłatny, czynna od świtu do zmierzchu.",
        badge="Bezpłatnie",
        status=None,
        lead="Pokazowa Zagroda Zwierząt należy do Ośrodka Kultury Leśnej w Gołuchowie, obok zamku i parku-arboretum. Zajmuje ponad 20 hektarów ogrodzonego lasu mieszanego z sosną i dębem. Najważniejszym gatunkiem są żubry. Wstęp jest bezpłatny, a zagroda otwarta przez cały rok.",
        sections=[
            ("Zwierzęta", [
                "Zagrodę założono w kwietniu 1977 roku z myślą o rosnącej liczbie żubrów i rozproszeniu ich hodowli. Do końca 2024 roku hodowano tu 128 żubrów, w tym 114 urodzonych w Gołuchowie.",
                "Oprócz żubrów można zobaczyć koniki polskie, daniele i dziki. Zwierzęta oglądasz z wyznaczonych alejek.",
            ]),
            ("Warto wiedzieć", [
                "Zagroda jest czynna codziennie, od wschodu do zachodu słońca. Wstęp jest bezpłatny. Rocznie odwiedza ją około 120 tysięcy osób.",
                "Przy wejściu trzeba przejść przez maty dezynfekcyjne. Dzieci do 12 lat mogą przebywać na terenie tylko pod opieką dorosłych.",
                "Obowiązuje zakaz karmienia, dotykania i płoszenia zwierząt, fotografowania z lampą błyskową oraz poruszania się poza alejkami. Nie wolno wprowadzać zwierząt domowych (poza psami przewodnikami), a także jeździć rowerem, na rolkach czy hulajnodze.",
                "Obok działa Muzeum Leśnictwa w dawnych zabudowaniach folwarku (wt–nd 10:00–16:00, bilet pełny 25 zł, ulgowy 18 zł) oraz bezpłatny park-arboretum. Zamek w Gołuchowie jest osobnym muzeum.",
            ]),
        ],
        address="ul. Działyńskich 2, 63-322 Gołuchów",
        hours=[
            ("Zagroda, codziennie, cały rok", "od wschodu do zachodu słońca"),
        ],
        tickets=[("Wstęp", "bezpłatnie")],
        phone="+48 62 76 15 045", www=("okl.lasy.gov.pl", "https://www.okl.lasy.gov.pl/pokazowa-zagroda"),
        credit="zagroda-zwierzat-goluchow",
        trip=dict(lat=51.8595602, lon=17.9241702, getting=[
            ("Komunikacja", "Połączenie z Poznania sprawdź w wyszukiwarce tras (link powyżej)."),
        ]),
        sources=[("Ośrodek Kultury Leśnej w Gołuchowie: Pokazowa Zagroda Zwierząt", "https://www.okl.lasy.gov.pl/pokazowa-zagroda"),
                 ("Ośrodek Kultury Leśnej w Gołuchowie: informacja turystyczna", "https://www.okl.lasy.gov.pl/informacja-turystyczna"),
                 ("OKL: regulamin Pokazowej Zagrody Zwierząt (zarządzenie nr 6/2025 z 5.03.2025)", "https://www.okl.lasy.gov.pl/documents/998963/51382627/Regulamin+PZZ/533eea8b-4846-42fe-475f-d01c1ebd3256")],
    ),
]
