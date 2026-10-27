# -*- coding: utf-8 -*-
"""Uzupełnienie luk po porównaniu z konkurencją (10.10.2026): VisitPoznań (Top 10, muzea, atrakcje dla dzieci),
Wikivoyage i przewodniki. Taras widokowy Collegium Altum oraz trzy muzea, które były opisane tylko w kartach
Cytadeli i Zamku Królewskiego (Muzeum Uzbrojenia, Muzeum Armii „Poznań”, Muzeum Sztuk Użytkowych).
Wszystkie fakty pochodzą ze stron obiektów i wymienionych w polu sources źródeł, sprawdzonych 10.10.2026.
Pole see_also: lista (etykieta, ścieżka względem katalogu głównego bez .html), np. ("Cytadela", "atrakcje/cytadela")."""

WMN = "https://www.wmn.poznan.pl/"
TARAS = "https://taras.ue.poznan.pl/"

GAPS3 = [
    dict(
        slug="taras-widokowy-collegium-altum", cat="wspolczesny", name="Taras widokowy Collegium Altum (UEP)",
        img="taras-widokowy-collegium-altum", img_alt="Czerwony wieżowiec Collegium Altum nad dachami Poznania",
        short="Panorama Poznania na cztery strony świata z 18. piętra czerwonego wieżowca Uniwersytetu Ekonomicznego.",
        badge="Codziennie 9–19",
        status=None,
        lead="Taras widokowy na 18. piętrze Collegium Altum Uniwersytetu Ekonomicznego pokazuje Poznań na cztery strony świata. Po wielu latach przerwy ponownie otwarto go dla zwiedzających 16 czerwca 2025 roku.",
        sections=[
            ("O miejscu", [
                "Collegium Altum to czerwony wieżowiec z elewacją z czerwonych płyt metalowych i stalową konstrukcją. Jest wyraźnym elementem panoramy miasta. Budowę rozpoczęto w 1976 roku.",
                "Taras mieści się na 18. piętrze, obok holu windowego. Działał do 2004 roku, potem na tym piętrze urządzono laboratoria komputerowe i przez wiele lat był zamknięty dla zwiedzających. Pomysłodawcą jego ponownego uruchomienia był ówczesny prezes SARP Piotr Kostka. Uroczyste otwarcie odbyło się 11 czerwca 2025 roku, a dla zwiedzających taras otwarto 16 czerwca.",
            ]),
            ("Na miejscu", [
                "W cenie biletu można korzystać z lornetek. Na tarasie jest kawiarnia SkyCoffee (kawa, herbata, zimne napoje, rogaliki i tarty), a w środy, czwartki, piątki i soboty wieczorem działa tam także SkyPong, czyli gra w ping ponga z menu barowym.",
                "Dzieci mają podesty do oglądania panoramy oraz rebusy i zagadki. Na wszystkich czeka strefa wypoczynku z kanapami, ramka do zdjęć na tle panoramy, karty z opisami widocznych obiektów i kody QR na szybach. Ekran Fly Radar pokazuje samoloty w czasie rzeczywistym, także te, które podchodzą do lądowania na Ławicy.",
            ]),
            ("Co zobaczyć", [
                "Z góry widać m.in. Stary Rynek, Ostrów Tumski z katedrą, Zamek Królewski i Zamek Cesarski, Plac Wolności, Okrąglak, Stary Browar, Teatr Wielki, Dworzec Poznań Główny, Międzynarodowe Targi Poznańskie, Stadion Miejski, Cytadelę i Jezioro Maltańskie.",
                "Oficjalna lista na stronie tarasu obejmuje ponad 30 miejsc, także Wartę, Ratusz i Port Lotniczy Ławica.",
            ]),
            ("Warto wiedzieć", [
                "Indywidualnie taras jest czynny codziennie od 9:00 do 19:00, tak podają strony „Informacje podstawowe” i „Cennik”. Zakładka FAQ na tej samej stronie jest nieaktualna i podaje starsze godziny (pn–pt 12:00–20:00, sb–nd 9:00–20:00), więc przed wizytą warto zadzwonić.",
                "Bilety dla osób indywidualnych kupuje się w biletomatach w holu windowym na 18. piętrze (można płacić kartą i zbliżeniowo), rezerwacja nie jest potrzebna. Bilet uprawnia do jednego, nieprzerwanego wejścia. Trzeba go zachować do wyjścia i przyłożyć do czytnika.",
                "W dni powszednie w godzinach 9:00–12:00 wszyscy płacą cenę ulgową. Ulgowy przysługuje też m.in. dzieciom powyżej 3. roku życia i młodzieży z legitymacją, osobom z niepełnosprawnościami (z jednym opiekunem), emerytom i rencistom oraz posiadaczom Karty Dużej Rodziny. We wtorki studenci innych uczelni płacą 10 zł, a studenci UEP wchodzą bezpłatnie. Według FAQ na stronie tarasu bezpłatnie wchodzą też posiadacze Poznań City Card, ale warto to potwierdzić telefonicznie.",
                "Grupy zorganizowane (co najmniej 10 osób) rezerwują wizytę online z minimum 3-dniowym wyprzedzeniem. Na każde 10 osób opiekun grupy wchodzi bezpłatnie. Zwiedzanie grupowe trwa 45 minut i odbywa się w dni powszednie 9:00–12:00. Oprowadzanie z przewodnikiem jest tylko dla grup.",
                "Budynek ma podjazd i windę, a cały taras jest dostępny dla osób na wózkach. Na tarasie jest domofon do kontaktu z personelem, a w toalecie system alarmowy do wezwania pomocy. Strona nie podaje, czy toaleta jest przystosowana dla wózków.",
                "Psów nie wolno wprowadzać, poza oznaczonymi psami asystującymi. Dzieci muszą mieć opiekę dorosłych. Robienie zdjęć jest dozwolone, a sesje komercyjne wymagają wcześniejszego kontaktu z obsługą tarasu (taras@ue.poznan.pl).",
                "Parking UEP: ul. Towarowa 55, miejsc jest mało, a w okolicy działa też płatna strefa parkowania. Od września do czerwca parking jest czynny w dni powszednie 16:00–24:00, w weekendy 6:00–24:00, a w lipcu i sierpniu codziennie 6:00–24:00.",
            ]),
        ],
        address="ul. Powstańców Wielkopolskich 16, 61-895 Poznań",
        hours=[("Codziennie", "9:00–19:00"), ("Grupy (pn–pt)", "9:00–12:00, po rezerwacji online")],
        tickets=[("Normalny", "20 zł"), ("Ulgowy", "15 zł"), ("Pn–pt 9:00–12:00", "wszyscy płacą cenę ulgową"),
                 ("Grupa od 10 osób (tylko online)", "15 zł od osoby"), ("Studenci (wtorek)", "10 zł")],
        phone="+48 516 672 351", www=("taras.ue.poznan.pl", TARAS),
        credit="taras-widokowy-collegium-altum",
        sources=[
            ("Taras widokowy UEP: informacje podstawowe", TARAS + "informacje-podstawowe.html"),
            ("Taras widokowy UEP: cennik", TARAS + "cennik.html"),
            ("Taras widokowy UEP: dostępność obiektu", TARAS + "dostepnosc-dla-osob-z-niepelnosprawnosciami.html"),
            ("Taras widokowy UEP: FAQ", TARAS + "faq.html"),
            ("National Geographic Traveler: powrót tarasu (14.06.2025)",
             "https://www.national-geographic.pl/traveler/kierunki/po-20-latach-do-poznania-wraca-slynna-atrakcja-na-turystow-czeka-zapierajacy-dech-w-piersi-widok/"),
        ],
        see_also=[("Punkty widokowe w Poznaniu: wszystkie wieże i tarasy", "punkty-widokowe"),
                  ("Zamek Królewski i wieża widokowa", "atrakcje/zamek-krolewski"),
                  ("Okrąglak, widoczny z tarasu", "atrakcje/okraglak")],
        checked="27.10.2026",
    ),
    dict(
        slug="muzeum-uzbrojenia", cat="muzea", name="Muzeum Uzbrojenia",
        img="muzeum-uzbrojenia", img_alt="Wejście do Muzeum Uzbrojenia w Parku Cytadela, przed bramą czołgi i samolot",
        short="Czołgi, działa i samoloty w murach dawnego Fortu Winiary na Cytadeli. We wtorki wstęp wolny.",
        badge="Wt wstęp wolny",
        status=None,
        lead="Muzeum Uzbrojenia znajduje się w Parku Cytadela, w pozostałościach XIX-wiecznego Fortu Winiary. To oddział Wielkopolskiego Muzeum Niepodległości z dużą kolekcją sprzętu wojskowego, w tym z czołgami i samolotami pod gołym niebem.",
        sections=[
            ("Co zobaczyć", [
                "Plenerowy park sprzętu wojskowego: kilkanaście pojazdów wojskowych oraz samoloty, wśród nich czołgi i działa samobieżne.",
                "Wikipedia wymienia wśród najcenniejszych eksponatów radziecką wyrzutnię rakiet BM-13 „Katiusza” na podwoziu ciężarówki Studebaker z 1944 roku, czołg T-34/85 i działo samobieżne ISU-122. Wnętrza dwóch ostatnich bywają udostępniane w wybrane święta i wydarzenia.",
                "Wystawa stała „Za mundurem panny sznurem” pokazuje mundury, uzbrojenie i oporządzenie polskich formacji.",
            ]),
            ("Historia", [
                "Fort Winiary zbudowali Prusacy w latach 1828–1842. W latach 60. XX wieku fort w dużej części rozebrano i urządzono na jego miejscu park o powierzchni 100 hektarów.",
                "Muzeum powstało w latach 60. XX wieku. Od 1998 roku nosi nazwę Muzeum Uzbrojenia. Wcześniej działało m.in. jako Muzeum Wyzwolenia Miasta Poznania, a potem Muzeum Cytadeli Poznańskiej.",
            ]),
            ("Warto wiedzieć", [
                "W tym samym parku działa Muzeum Armii „Poznań”. Bilet wspólny na oba muzea kosztuje 20 zł (ulgowy 12 zł).",
                "We wtorki wstęp do muzeum jest bezpłatny. Zwiedzanie z przewodnikiem wymaga wcześniejszej rezerwacji i kosztuje 70 zł po polsku oraz 90 zł po angielsku. Lekcja muzealna kosztuje 100 zł. Bilety można kupić też online na tobilet.pl.",
                "Według komunikatu muzeum z czerwca 2025 roku obiekt jest czynny 10:00–17:00, a ostatnie wejście jest o 16:30. Muzeum bywa zamykane na czas dużych wydarzeń w parku, więc przed wizytą sprawdź komunikaty na jego stronie.",
                "Dojazd (według rozkładu ZTM z 10.10.2026): tramwaje 4 i 19 (przystanek Murawa) oraz 3, 4, 10 i 19 (przystanek Pasieka) albo autobusy do przystanków Urząd Marszałkowski, Winogrady, Armii Poznań i Grochowe Łąki. Bezpłatny parking jest przy parku, wjazd od ulicy Garbary.",
            ]),
        ],
        address="al. Armii Poznań, Park Cytadela, 61-663 Poznań",
        hours=[("Poniedziałek", "nieczynne"), ("Wtorek–sobota (III–X)", "10:00–17:00"), ("Niedziela (III–X)", "10:00–16:00"),
               ("Wtorek–niedziela (XI–II)", "10:00–16:00")],
        tickets=[("Normalny", "15 zł"), ("Ulgowy", "10 zł"), ("Bilet wspólny z Muzeum Armii „Poznań”", "20 zł, ulgowy 12 zł"),
                 ("Dzieci do 7 lat", "bezpłatnie"), ("Wtorek", "wstęp wolny")],
        phone="+48 61 820 45 03", www=("wmn.poznan.pl", WMN + "oddzialy-4/muzeum-uzbrojenia/"),
        credit="muzeum-uzbrojenia",
        sources=[
            ("WMN: Muzeum Uzbrojenia", WMN + "oddzialy-4/muzeum-uzbrojenia/"),
            ("WMN: ceny biletów", WMN + "ceny-biletow/"),
            ("WMN: godziny otwarcia", WMN + "godziny-otwarcia/"),
            ("Wikipedia: Muzeum Uzbrojenia w Poznaniu", "https://pl.wikipedia.org/wiki/Muzeum_Uzbrojenia_w_Poznaniu"),
        ],
        see_also=[("Muzeum Armii „Poznań”, w tym samym parku", "atrakcje/muzeum-armii-poznan"),
                  ("Cytadela: park, cmentarze i Nierozpoznani", "atrakcje/cytadela")],
        checked="10.10.2026",
    ),
    dict(
        slug="muzeum-armii-poznan", cat="muzea", name="Muzeum Armii „Poznań”",
        img="muzeum-armii-poznan", img_alt="Tablica informacyjna i ceglany słup bramy z napisem Muzeum Armii Poznań, wśród zieleni Parku Cytadela",
        short="Szlak bojowy Armii „Poznań” z 1939 roku w kazamatach Fortu Winiary. We wtorki wstęp wolny.",
        badge="Wt wstęp wolny",
        status=None,
        lead="Muzeum Armii „Poznań” mieści się w kazamatach Fortu Winiary w Parku Cytadela. Opowiada o Armii „Poznań”, którą w 1939 roku dowodził gen. Tadeusz Kutrzeba, oraz o wojsku II Rzeczypospolitej w Wielkopolsce. To oddział Wielkopolskiego Muzeum Niepodległości.",
        sections=[
            ("Co zobaczyć", [
                "Wystawa stała „Wierni przysiędze” przedstawia szlak bojowy Armii „Poznań”.",
                "Zbiory obejmują dokumenty, sztandary, broń, umundurowanie i materiały ikonograficzne dotyczące Wojska Polskiego z okresu międzywojennego, zwłaszcza jednostek wielkopolskich. Wyróżnia się kolekcja zdjęć z codziennego życia i służby w wielkopolskich garnizonach.",
                "Ważnym źródłem jest wielkoformatowy plan Poznania z 1932 roku z zaznaczonymi obiektami i gruntami wojskowymi.",
            ]),
            ("O miejscu", [
                "Muzeum zajmuje korytarz kazamatowy zwany Małą Śluzą. Pierwotnie była to Estakada Zachodnia Fortu Winiary, która łączyła go z Fortem św. Wojciecha (Hakego).",
                "W 1974 roku na murze przeciwskarpy odsłonięto pierwszą z czternastu tablic upamiętniających jednostki i formacje Armii „Poznań”. Stałą ekspozycję muzeum otwarto 31 sierpnia 1982 roku.",
            ]),
            ("Warto wiedzieć", [
                "Od 20 stycznia 2026 roku muzeum jest czynne od wtorku do niedzieli w godzinach 10:00–16:00. Ostatnie wejście na ekspozycję jest o 15:30.",
                "W tym samym parku działa Muzeum Uzbrojenia. Bilet wspólny na oba muzea kosztuje 20 zł (ulgowy 12 zł). We wtorki wstęp jest bezpłatny. Oprowadzanie z przewodnikiem po polsku kosztuje 30 zł (cennik WMN), a termin warto ustalić z muzeum. Bilety można kupić też online na tobilet.pl.",
                "Dojazd (według rozkładu ZTM z 10.10.2026): tramwaje 4 i 19 (przystanek Murawa) oraz 3, 4, 10 i 19 (przystanek Pasieka) albo autobusy do przystanków Urząd Marszałkowski, Winogrady, Armii Poznań i Grochowe Łąki. Bezpłatny parking jest przy parku, wjazd od ulicy Garbary.",
            ]),
        ],
        address="al. Armii Poznań, Park Cytadela (Mała Śluza), 61-663 Poznań",
        hours=[("Poniedziałek", "nieczynne"), ("Wtorek–niedziela", "10:00–16:00"), ("Ostatnie wejście", "15:30")],
        tickets=[("Normalny", "10 zł"), ("Ulgowy", "6 zł"), ("Bilet wspólny z Muzeum Uzbrojenia", "20 zł, ulgowy 12 zł"),
                 ("Wtorek", "wstęp wolny")],
        phone="+48 663 866 414", www=("wmn.poznan.pl", WMN + "oddzialy-4/muzeum-armii-poznan/"),
        credit="muzeum-armii-poznan",
        sources=[
            ("WMN: Muzeum Armii „Poznań”", WMN + "oddzialy-4/muzeum-armii-poznan/"),
            ("WMN: ceny biletów", WMN + "ceny-biletow/"),
        ],
        see_also=[("Muzeum Uzbrojenia, w tym samym parku", "atrakcje/muzeum-uzbrojenia"),
                  ("Pomnik Armii „Poznań”", "atrakcje/pomnik-armii-poznan"),
                  ("Cytadela: park, cmentarze i Nierozpoznani", "atrakcje/cytadela")],
        checked="10.10.2026",
    ),
]

# Strona zbiorcza „Punkty widokowe”: opisy z kart atrakcji (nie dodają nowych faktów), kolejność = od centrum.
VIEWPOINTS = [
    ("taras-widokowy-collegium-altum",
     "Taras na 18. piętrze czerwonego wieżowca Uniwersytetu Ekonomicznego. Panorama na cztery strony świata, a oficjalna lista widocznych miejsc liczy ponad 30 pozycji. Bilety kupisz w biletomatach na miejscu, taras jest czynny codziennie.",
     "płatny"),
    ("zamek-krolewski",
     "Wieża Zamku Królewskiego ma 43 metry i dwa tarasy: zadaszony na wysokości 30 metrów i otwarty na samym szczycie. Na górę prowadzi blisko 200 stopni, a według muzeum na tarasy widokowe wchodzi się wyłącznie schodami. Wieżę zwiedza się po obejrzeniu wystawy Muzeum Sztuk Użytkowych.",
     "płatny"),
    ("ostrow-tumski",
     "Wieża archikatedry na Ostrowie Tumskim. Czynna sezonowo, w 2026 roku od 1 czerwca. W sezonie (1.03–15.11) obowiązują te same godziny co w kryptach.",
     "płatny"),
    ("szachty",
     "Wieża widokowa na Szachtach ma 25 metrów i 120 stopni. Widać z niej wieżowce, stadion i biurowce w centrum, a wokół są stawy w dawnych gliniankach. Wstęp jest bezpłatny.",
     "bezpłatny"),
    ("czmoniec-bobrowy-szlak",
     "Drewniana wieża o wysokości około 14 metrów w Czmońcu (gmina Kórnik) stoi nad łąkami i starorzeczami Warty. Platforma na szczycie mieści jednocześnie do 20 osób. Teren jest otwarty, bez biletów.",
     "bezpłatny"),
]
