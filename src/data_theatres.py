# -*- coding: utf-8 -*-
"""Teatry i koncerty (30.09.2026): strona teatry.html (THEATRES) i Teatr Wielki jako atrakcja (THEATRE_ATTR).
Lista scen z POI poznan.pl „Teatry” i „Sale koncertowe”, adresy i kasy sprawdzone na stronach teatrów.
Celowo BEZ repertuaru i cen spektakli (zmieniają się co miesiąc) — tylko linki do repertuaru.
Pominięte małe sceny niezależne z listy poznan.pl (grają rzadko i po polsku)."""

THEATRES_CHECKED = "30.09.2026"

# lang: True = można iść bez znajomości polskiego (opera, balet, koncerty, taniec)
THEATRES = [
    dict(
        id="teatr-wielki", name="Teatr Wielki im. Stanisława Moniuszki (Opera)",
        kind="Opera, operetka, balet, koncerty", lang=True, img="teatr-wielki", attraction="teatr-wielki",
        desc=["Poznańska opera gra w gmachu projektu Maxa Littmanna z Pegazem na dachu, jednym z symboli miasta. Budynek można też zwiedzić za kulisami.",
              "Kasa jest czynna od wtorku do soboty w godzinach 13:00–19:00, a w niedziele 2 godziny przed spektaklem (tylko gdy są jeszcze bilety). Bilety sprzedaje też Centrum Informacji Kulturalnej przy ul. Ratajczaka 44."],
        address="ul. Fredry 9, 61-701 Poznań",
        links=[("Repertuar", "https://opera.poznan.pl/pl/repertuar"), ("Bilety online", "https://bilety.opera.poznan.pl/")],
    ),
    dict(
        id="filharmonia", name="Filharmonia Poznańska (Aula Uniwersytecka)",
        kind="Koncerty symfoniczne i kameralne", lang=True, img="aula-uam", attraction="collegium-minus",
        desc=["Filharmonia działa od 1947 roku, a koncerty daje w neorenesansowej Auli Uniwersyteckiej w gmachu Collegium Minus z 1910 roku, przy placu Mickiewicza. Aula słynie ze znakomitej akustyki.",
              "W strukturze Filharmonii jest też chór chłopięcy i męski Poznańskie Słowiki. W Auli grają również inni wykonawcy, a na ich koncerty bilety sprzedają organizatorzy.",
              "Kasa biletowa jest przy wejściu do Auli. Od października do czerwca działa od wtorku do piątku w godzinach 13:00–17:00, a w dni koncertów Filharmonii także od godziny przed koncertem."],
        address="ul. Wieniawskiego 1, 61-712 Poznań",
        links=[("Repertuar i bilety", "https://filharmoniapoznanska.pl/"), ("Kasa biletowa", "https://filharmoniapoznanska.pl/bilety-i-karnety/kasa-biletowa/")],
    ),
    dict(
        id="teatr-polski", name="Teatr Polski",
        kind="Teatr dramatyczny", lang=False, img="teatr-polski", attraction=None,
        desc=["Najstarszy teatr w Poznaniu, otwarty w 1875 roku. Zbudowano go ze składek Polaków żyjących pod zaborem pruskim, co upamiętnia napis „Naród sobie” na fasadzie.",
              "Kasa jest czynna od wtorku do piątku w godzinach 10:00–18:00 (lub do rozpoczęcia spektaklu), a w soboty i niedziele na godzinę przed spektaklem."],
        address="ul. 27 Grudnia 8/10, 61-737 Poznań",
        links=[("Repertuar", "https://teatr-polski.pl/repertuar/"), ("Zwiedzanie teatru", "https://teatr-polski.pl/zwiedzanie-teatru/")],
    ),
    dict(
        id="teatr-nowy", name="Teatr Nowy im. Izabelli Cywińskiej",
        kind="Teatr dramatyczny", lang=False, img="teatr-nowy", attraction=None,
        desc=["Legendą teatr stał się za dyrekcji Izabelli Cywińskiej, od 1973 roku. Wiele przedstawień z lat 1973–1989 to ważne wydarzenia w historii polskiego teatru.",
              "W 1992 roku na scenie Teatru Nowego, podczas próby „Króla Leara”, zmarł Tadeusz Łomnicki."],
        address="ul. Dąbrowskiego 5, 60-838 Poznań",
        links=[("Repertuar", "https://teatrnowy.pl/repertuar/"), ("Ceny i zakup biletów", "https://teatrnowy.pl/ceny-zasady-kupna-biletow/")],
    ),
    dict(
        id="teatr-muzyczny", name="Teatr Muzyczny",
        kind="Musicale i komedie muzyczne", lang=False, img="teatr-muzyczny", attraction=None,
        desc=["Teatr zaczął działać w 1956 roku jako Państwowa Operetka Poznańska. Dziś gra głównie musicale.",
              "Przy ulicy Święty Marcin powstaje nowa siedziba teatru. Przed wizytą sprawdź na stronie teatru, gdzie odbywa się spektakl."],
        address="ul. Niezłomnych 1e, 61-894 Poznań",
        links=[("Repertuar i bilety", "https://teatr-muzyczny.pl/")],
    ),
    dict(
        id="ptt", name="Polski Teatr Tańca",
        kind="Taniec współczesny", lang=True, img=None, attraction=None,
        desc=["Zespół założony w 1973 roku, którego pierwszym dyrektorem był choreograf Conrad Drzewiecki. Już w pierwszych latach zaliczano go do najlepszych zespołów w Europie i zapraszano na międzynarodowe festiwale. Współpracowali z nim choreografowie z całego świata, m.in. Mats Ek i Ohad Naharin."],
        address="ul. Taczaka 8, 61-818 Poznań",
        links=[("Repertuar i bilety", "https://ptt-poznan.pl/bilety/informacje")],
    ),
    dict(
        id="teatr-animacji", name="Teatr Animacji",
        kind="Teatr lalkowy, spektakle dla dzieci i dorosłych", lang=False, img="zamek-cesarski", attraction="zamek-cesarski",
        desc=["Teatr lalek działa w Poznaniu od 1945 roku, od 1989 roku pod nazwą Teatr Animacji. Gra w budynku Centrum Kultury Zamek, czyli w dawnym Zamku Cesarskim (wejście główne).",
              "Kasa jest czynna od godziny przed spektaklem i w każdy piątek w godzinach 15:00–18:00. Bilet na spektakl dla dzieci kosztuje 55 zł (ulgowy 50 zł)."],
        address="ul. Święty Marcin 80/82, 61-809 Poznań",
        links=[("Repertuar", "https://www.teatranimacji.pl/pl/repertuar"), ("Ceny biletów", "https://www.teatranimacji.pl/en/tickets")],
    ),
    dict(
        id="teatr-osmego-dnia", name="Teatr Ósmego Dnia",
        kind="Teatr alternatywny", lang=False, img="teatr-osmego-dnia", attraction=None,
        desc=["Legendarny teatr alternatywny, założony w 1964 roku jako teatr studencki. W czasach PRL jego spektakle ostro komentowały rzeczywistość, a w latach 1986–1989 zespół działał wyłącznie za granicą, grając m.in. przedstawienia uliczne w całej Europie.",
              "Siedziba jest na II piętrze. Teatr otwiera się godzinę przed wydarzeniem, a przy wejściu jest winda i platforma."],
        address="ul. Ratajczaka 44, 61-728 Poznań",
        links=[("Repertuar", "https://teatrosmegodnia.pl/repertuar/")],
    ),
]

THEATRE_SOURCES = [
    ("poznan.pl: Teatry (lista i opisy)", "https://www.poznan.pl/mim/main/teatry,poi,179/"),
    ("poznan.pl: Aula Uniwersytetu im. Adama Mickiewicza", "https://www.poznan.pl/mim/main/sale-koncertowe,poi,189,15/aula-uniwersytetu-im-adama-mickiewicza,16344.html"),
    ("Teatr Wielki: zaplanuj wizytę (kasy)", "https://opera.poznan.pl/pl/zaplanuj-wizyte"),
    ("Filharmonia Poznańska: kasa biletowa", "https://filharmoniapoznanska.pl/bilety-i-karnety/kasa-biletowa/"),
    ("Teatr Polski: kontakt i kasa", "https://teatr-polski.pl/kontakt/"),
    ("Teatr Animacji: kontakt", "https://teatranimacji.pl/pl/kontakt"),
    ("Teatr Ósmego Dnia: kontakt", "https://teatrosmegodnia.pl/kontakt/"),
    ("poznan.pl: Jak będzie wyglądał nowy Teatr Muzyczny", "https://www.poznan.pl/mim/info/news/jak-bedzie-wygladal-nowy-teatr-muzyczny,272160.html"),
    ("Wikipedia: Collegium Minus w Poznaniu", "https://pl.wikipedia.org/wiki/Collegium_Minus_w_Poznaniu"),
    ("Wikipedia: Filharmonia Poznańska", "https://pl.wikipedia.org/wiki/Filharmonia_Pozna%C5%84ska_im._Tadeusza_Szeligowskiego"),
]

THEATRE_ATTR = [
    dict(
        slug="teatr-wielki", cat="zabytki", name="Teatr Wielki (Opera)",
        img="teatr-wielki", img_alt="Oświetlony wieczorem gmach Teatru Wielkiego w Poznaniu, odbity w wodzie",
        short="Gmach opery z Pegazem na dachu, projektu Maxa Littmanna. Można zwiedzić go za kulisami albo przyjść na operę lub balet.",
        badge="Opera i balet",
        status=None,
        lead="Gmach Teatru Wielkiego zaprojektował monachijski architekt Max Littmann. Budowę nowoczesnego gmachu teatru miejskiego rozpoczęto w 1909 roku. Neoklasycystyczną fasadę wieńczy figura Pegaza, dzięki której budynek nazywa się gmachem pod Pegazem.",
        sections=[
            ("Co zobaczyć", [
                "Neoklasycystyczną fasadę z sześciokolumnowym portykiem. Nad portykiem jest tympanon z cytatem z wiersza „Artyści” Friedricha Schillera o godności ludzkości, a na dachu stoi kamienny Pegaz.",
                "Widownię bez lóż, nazywaną „demokratyczną”. Bryła budynku czyniła teatr porównywalnym ze scenami w Dessau, Monachium, Linzu czy Królewcu.",
                "Salę Drabowicza, scenę kameralną urządzoną w dawnej teatralnej palarni. W sezonie 2009/10 zaczął się tu cykl „Opera kieszonkowa” z dziełami jednoaktowymi, niedokończonymi i salonowymi.",
            ]),
            ("Historia", [
                "Poznań miał wcześniej Teatr Królewski z 1804 roku, który stał na dzisiejszym placu Wolności i miał widownię dla tysiąca widzów. W 1875 roku wybudowano pierwszy stały teatr polski. Budowę obecnego gmachu rozpoczęto w 1909 roku, wraz z nowym założeniem urbanistycznym miasta wprowadzanym przez władze pruskie.",
                "W 1919 roku teatr przejęły władze polskie. 31 sierpnia 1919 roku wieczorny spektakl „Halki” Stanisława Moniuszki poprzedziła poranna akademia z udziałem prezydenta Poznania Jarogniewa Drwęskiego i gości z całego kraju. W pierwszym dwudziestoleciu zrealizowano tu 12 prawykonań polskich oper i baletów, w tym polskie prawykonanie baletu „Harnasie” Karola Szymanowskiego (9 kwietnia 1938).",
                "Po wojnie poznańska opera jako pierwsza w kraju wznowiła działalność. Inauguracyjną premierę „Krakowiaków i Górali” Karola Kurpińskiego, 2 czerwca 1945 roku, poprzedziły koncerty w zniszczonym wojną gmachu. Trzydzieści jeden lat po inauguracji z 1919 roku, czyli w 1950 roku, teatr otrzymał patronat Stanisława Moniuszki.",
                "Remont w latach 2021–2023 objął mechanikę sceny, oświetlenie, elektroakustykę i systemy bezpieczeństwa. Trwał ponad 25 miesięcy, a pracowało przy nim ponad 120 osób. Według teatru poznańska opera jest od tego czasu pierwszą na świecie z immersyjnym systemem dźwięku przestrzennego.",
                "Realizacje oper „Paria” (2019) i „Jawnuta” (2023) otrzymały od jury International Opera Awards wyróżnienie zwane operowym Oscarem w kategorii „opera odkryta na nowo”. Poznańska opera jest jedynym polskim teatrem, który otrzymał tę statuetkę dwukrotnie.",
            ]),
            ("Za kulisami", [
                "Teatr prowadzi zwiedzanie „Za kulisami Teatru”. W czasie spaceru po wnętrzach opery można zobaczyć miejsca, w których toczy się teatralne życie, i dowiedzieć się, ile osób pracuje nad przygotowaniem spektaklu.",
                "Zwiedzanie trwa 45–60 minut, kosztuje 10 zł od osoby i jest dla osób od 7 do 107 lat. Termin ustala się indywidualnie, pisząc na adres edukacja@opera.poznan.pl.",
            ]),
            ("Bilety i spektakle", [
                "W repertuarze są opery, operetki, balety i koncerty. Balet nie wymaga znajomości polskiego.",
                "Kasa jest czynna od wtorku do soboty w godzinach 13:00–19:00, a w niedziele 2 godziny przed spektaklem, tylko gdy są jeszcze bilety na bieżące wydarzenie. Bilety można kupić też w Centrum Informacji Kulturalnej przy ul. Ratajczaka 44 oraz na bilety.opera.poznan.pl. Kasa nie przyjmuje zwrotów.",
                "Bilety ulgowe przysługują dzieciom i młodzieży szkolnej, studentom do 26 lat, rencistom i emerytom. Teatr honoruje Kartę Dużej Rodziny: dorośli kupują bilet ulgowy, a dzieci za 50 zł, tylko w kasach teatru. Ceny podaje cennik na stronie teatru.",
                "Rezerwacje dotyczą wyłącznie grup zorganizowanych i prowadzi je Biuro Obsługi Widzów (pon–pt 8:00–16:00, tel. +48 61 85 20 825 lub +48 61 65 90 280, bow@opera.poznan.pl).",
            ]),
            ("Dojazd", [
                "Najbliższe przystanki wg strony teatru: Fredry (tramwaje 3, 7, 8, 11, 16, 19, 202), Zamek (autobusy 163, 168, 169, 171, 212, 222) i Most Teatralny (tramwaje 7, 10, 11, 15, 16, 19, 202). Przed spektaklem można wejść do Tośka Cantine od strony ulicy Wieniawskiego (tel. +48 61 852 00 70).",
            ]),
        ],
        address="ul. Fredry 9, 61-701 Poznań",
        hours=[("Kasa, wt–sb", "13:00–19:00"), ("Kasa, niedziele", "2 godziny przed spektaklem, tylko gdy są bilety"),
               ("Biuro Obsługi Widzów (grupy)", "pon–pt 8:00–16:00"), ("Zwiedzanie za kulisami", "terminy ustalane indywidualnie")],
        tickets=[("Zwiedzanie „Za kulisami Teatru”", "10 zł od osoby"), ("Karta Dużej Rodziny, dzieci", "50 zł (tylko w kasach teatru)"), ("Spektakle", "ceny zależą od wydarzenia")],
        phone="+48 61 659 02 31", www=("opera.poznan.pl", "https://opera.poznan.pl/pl/"),
        credit="teatr-wielki",
        sources=[("Teatr Wielki: Historia teatru", "https://opera.poznan.pl/historia-teatru"),
                 ("Teatr Wielki: Za kulisami Teatru", "https://opera.poznan.pl/pl/za-kulisami-teatru"),
                 ("Teatr Wielki: zaplanuj wizytę (kasy, bilety, dojazd)", "https://opera.poznan.pl/pl/zaplanuj-wizyte"),
                 ("Teatr Wielki: kontakt", "https://opera.poznan.pl/kontakt"),
                 ("poznan.pl: Teatr Wielki im. Stanisława Moniuszki", "https://www.poznan.pl/mim/main/teatry,poi,179/teatr-wielki-im-stanislawa-moniuszki,16030.html")],
    ),
]
