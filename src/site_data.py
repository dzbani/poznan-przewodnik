# -*- coding: utf-8 -*-
"""Treść przewodnika. Wszystkie godziny i ceny sprawdzone 28.09.2026
w źródłach podanych w polu "sources" każdej atrakcji.
Po zmianie danych uruchom: python src/build.py
"""

CHECKED = "01.10.2026"

CATEGORIES = [
    ("zabytki", "Zabytki i historia", "Tysiąc lat historii: od grodu Mieszka I po zamek cesarza."),
    ("pomniki", "Pomniki i fontanny", "Od barokowej fontanny przed ratuszem po Starego Marycha z rowerem."),
    ("koscioly", "Kościoły", "Od romańskiego kościoła joannitów po międzywojenne rotundy."),
    ("muzea", "Muzea", "Sztuka, archeologia, historia Wielkopolski i rogale."),
    ("przyroda", "Parki i przyroda", "Jezioro, ogrody i zieleń w granicach miasta."),
    ("rodzina", "Dla rodzin i aktywnie", "Zoo, kolejka, baseny i stok przez cały rok."),
    ("wspolczesny", "Współczesny Poznań", "Street art i dawny browar zamieniony w centrum sztuki."),
    ("wycieczki", "Wycieczki za miasto", "Zamki, pałace i kolebka Polski w zasięgu jednodniowego wyjazdu."),
]

# status: None | ("closed", "tekst") | ("warning", "tekst")
ATTRACTIONS = [
    # ─── ZABYTKI ───
    dict(
        slug="stary-rynek", cat="zabytki", name="Stary Rynek i Ratusz",
        img="hero-rynek", img_alt="Kolorowe kamienice i ratusz przy Starym Rynku w Poznaniu",
        short="Serce miasta od XIII wieku. Renesansowy ratusz i koziołki trykające się o 12:00 i 15:00.",
        badge="Bezpłatnie",
        status=("warning", "Muzeum w Ratuszu (Ratusz – Muzeum Poznania) jest zamknięte dla zwiedzających z powodu prac konserwatorsko-remontowych. Ponowne otwarcie wszystkich przestrzeni planowane jest w 2028 roku. Termin może ulec zmianie, sprawdź aktualny komunikat muzeum. Pokazy koziołków odbywają się codziennie o 12:00 i 15:00."),
        lead="Stary Rynek to główny plac Starego Miasta w Poznaniu. W jego środku stoi ratusz, którego najstarsza wzmianka pochodzi z 1310 roku.",
        sections=[
            ("O miejscu", [
                "Rynek był centrum miasta lokacyjnego, założonego między zamkiem a Wartą. Wokół placu stoją kamienice, a środek zajmuje blok zabudowy.",
                "Ratusz został wybudowany zapewne na przełomie XIII i XIV wieku. W połowie XVI wieku, po pożarze miasta, został rozbudowany przez włoskiego architekta Jana Baptystę Quadro z Lugano. Fasada zyskała formę trzypiętrowej loggii, a od strony wschodniej powstała attyka przypominająca mur obronny z trzema wieżami. Na elewacji północnej jest tablica z nazwiskiem architekta.",
                "Wielka Sień na pierwszym piętrze, zwana Salą Odrodzenia, uchodzi za jedno z najpiękniejszych wnętrz renesansowych w Polsce. Obecnie niedostępna dla zwiedzających z powodu remontu muzeum. W jednym z kasetonów sklepienia jest herb Poznania, a są tu też herby Polski i Litwy.",
            ]),
            ("Co zobaczyć", [
                "Koziołki na wieży ratusza: codziennie o 12:00 i 15:00 ukazują się nad zegarem i trykają się rogami. Pierwszy mechanizm zegarowy zainstalowano w 1551 roku, a zegarmistrz Bartłomiej z Gubina wykonał go na zamówienie rady miejskiej. W południe pod ratuszem zbiera się tłum, więc warto przyjść kilka minut wcześniej.",
                "Hejnał grany jest na żywo codziennie w południe, a kurant gra melodię co godzinę. Na elewacji ratusza są płaskorzeźby cnót (m.in. Cierpliwość, Roztropność, Miłość, Sprawiedliwość, Wiara, Nadzieja, Męstwo, Umiarkowanie), a w attyce malowidła władców Jagiellonów.",
                "Pręgierz z figurą kata z uniesionym mieczem, symbolem prawa karania śmiercią. Powstał po 1535 roku z grzywien płaconych przez zbyt strojnie ubierające się służące. Oryginał jest w muzeum, a na jego miejscu stoi replika.",
                "Bamberka: studzienka ufundowana w 1915 roku przez rodzinę Goldenringów, znaną z handlu winem. Upamiętnia osadników z okolic Bambergu, którzy przybyli do Poznania na początku XVIII wieku. Autorem figury jest Joseph Wackerle.",
                "Domki budnicze po południowej stronie ratusza, relikt dawnych kramów. Handlowano tu śledziami, solą, powrozami, pochodniami i świecami.",
                "Blok śródrynkowy: poza ratuszem stoją tu Waga Miejska, klasycystyczny Odwach (dziś Muzeum Powstania Wielkopolskiego) oraz domki budnicze.",
                "Cztery fontanny: Prozerpiny, Apollina, Neptuna i Marsa.",
            ]),
            ("Legenda o koziołkach", [
                "Podczas uczty na cześć nowego zegara młody kuchcik spalił udziec sarni. Ukradł więc dwa koziołki pasące się na łące i uciekł na wieżę, gdzie koziołki pojawiły się na gzymsie nad zegarem. Legenda nie jest potwierdzoną historią, ale tak opowiadają ją mieszkańcy.",
            ]),
            ("Warto wiedzieć", [
                "Punkt Informacji Turystycznej działa w kamienicy Stary Rynek 59/60. Można tu dostać mapy i kupić Poznańską Kartę Turystyczną.",
                "W promieniu kilkuset metrów są: Rogalowe Muzeum Poznania, Fara Poznańska, Muzeum Archeologiczne i Muzeum Powstania Wielkopolskiego.",
            ]),
        ],
        address="Stary Rynek 1, 61-768 Poznań (Ratusz)",
        hours=[("Plac", "dostępny całą dobę"), ("Koziołki", "codziennie o 12:00 i 15:00"), ("Muzeum w Ratuszu", "zamknięte; ponowne otwarcie planowane w 2028 r.")],
        tickets=[("Plac i koziołki", "bezpłatnie")],
        phone=["+48 61 856 81 93", "+48 61 852 56 13"], email="ratusz@mnp.art.pl", www=("Oficjalna strona muzeum", "https://mnp.art.pl/ratusz-muzeum-poznania"),
        credit="hero-rynek",
        sources=[("Muzeum Narodowe w Poznaniu: Ratusz – Muzeum Poznania (pokazy koziołków)", "https://mnp.art.pl/profile/koziolki-ratusz-muzeum-poznania"),
                 ("Muzeum Narodowe w Poznaniu: wizyta w Ratuszu (zamknięcie, termin)", "https://mnp.art.pl/profile/wizyta-ratusz-muzeum-poznania"),
                 ("poznan.pl: Ratusz (Odkryj Poznań)", "https://www.poznan.pl/mim/wortals/turystyka/zabytki,poi,2572/ratusz,41233.html"),
                 ("poznan.pl: Przewodnik po Starym Rynku (pręgierz, Bamberka, domki budnicze)", "https://www.poznan.pl/mim/staryrynek/index.html?co=plan"),
                 ("poznan.pl: Podania i legendy Poznania", "https://www.poznan.pl/mim/turystyka/legendy-poznania,p,27888.html"),
                 ("kultura.poznan.pl: Ratusz – Muzeum Poznania (remont)", "https://kultura.poznan.pl/mim/kultura/object.html?id_klasy=202&lang=&id_cz=12&id_obiektu=40787"),
                 ("TVP Poznań: remont ratusza i koziołki", "https://poznan.tvp.pl/93014656/ratusz-poznan-remont-rusztowania-zamkniecie-koziolki-poznan-zamkniecie-kiedy-koniec-prac-muzeum-mieszkancow-stary-rynek")],
    ),
    dict(
        slug="ostrow-tumski", cat="zabytki", name="Ostrów Tumski i Archikatedra",
        img="ostrow-tumski", img_alt="Dwuwieżowa fasada archikatedry na Ostrowie Tumskim widziana z lotu ptaka, wśród zieleni i kamienic",
        short="Najstarsza katedra w Polsce. Relikty grobów pierwszych władców i Złota Kaplica.",
        badge="Krypty i wieża płatne",
        status=None,
        lead="Ostrów Tumski to wyspa między Wartą a Cybiną, na której w X wieku stał gród pierwszych Piastów. Biskupstwo działa tu od 968 roku, a archikatedra świętych Piotra i Pawła jest najstarszą katedrą w Polsce.",
        sections=[
            ("O miejscu", [
                "Budowę pierwszego kościoła katedralnego rozpoczęto tu ok. 968 roku. W latach 1039–1058 stała tu romańska bazylika, a obecna bryła ma formy gotyckie z XIV i XV wieku. Po zniszczeniach II wojny światowej świątynię częściowo odbudowano i przywrócono jej gotycki charakter.",
                "W podziemiach katedry zachowały się relikty grobowców, najprawdopodobniej Mieszka I i Bolesława Chrobrego.",
            ]),
            ("Co zobaczyć", [
                "Złota Kaplica (Kaplica Królewska) w stylu bizantyjskim, urządzona w latach 1835–1841 według projektu Franciszka Marii Lanciego jako Mauzoleum Królewskie pierwszych władców Polski. Stoi w niej spiżowy pomnik pierwszych władców, wykonany przez Chrystiana Raucha i ustawiony w 1841 roku.",
                "Podziemia katedry: fragmenty katedry preromańskiej i romańskiej, relikty grobowców, relikty misy chrzcielnej z X wieku, a w drugiej krypcie wystawa lapidarium z kamieni odkrytych przy odbudowie katedry po II wojnie światowej.",
                "Wieża widokowa, czynna sezonowo (w 2026 roku od 1 czerwca).",
            ]),
            ("Warto wiedzieć", [
                "Katedra jest czynnym kościołem. W czasie mszy, nabożeństw i koncertów nie można jej zwiedzać, obowiązuje też stosowny strój i cisza. Przewodnicy nie mogą używać głośników ani wzmacniaczy.",
                "Po drugiej stronie Cybiny, połączona kładką, stoi Brama Poznania. Oferuje ona bilet łączony na zwiedzanie Ostrowa Tumskiego.",
            ]),
        ],
        address="ul. Ostrów Tumski 17, 61-109 Poznań",
        hours=[("Zwiedzanie (1.03–15.11)", "dni powszednie 9:00–16:00"), ("Zwiedzanie (16.11–koniec lutego)", "dni powszednie 9:00–16:00"), ("Podziemia (krypty)", "1.03–15.11: dni powszednie 9:00–16:00, niedziele 14:00–18:00 (jeśli nie ma dodatkowego nabożeństwa)"), ("Wieża widokowa", "od 1.06.2026; w sezonie 1.03–15.11 jak krypty: dni powszednie 9:00–16:00, niedziele 14:00–18:00 (jeśli nie ma dodatkowego nabożeństwa)"), ("Krypty i wieża po 15.11", "strona archidiecezji podaje je tylko na sezon 1.03–15.11, zimą godzin zwiedzania nie ma")],
        tickets=[("Zwiedzanie katedry i podziemi", "bilet kupuje się na miejscu w punkcie obsługi turystycznej w katedrze"), ("Podziemia", "10 zł, ulgowy 8 zł, rodzinny 25 zł"), ("Wieża widokowa", "14 zł, ulgowy 12 zł, rodzinny 40 zł")],
        phone="+48 61 852 96 42", www=("katedra.archpoznan.pl", "https://www.katedra.archpoznan.pl/turysci-w-katedrze/"),
        credit="ostrow-tumski",
        sources=[("poznan.pl: Katedra (Odkryj Poznań)", "https://www.poznan.pl/mim/wortals/turystyka/-,p,37,50,54.html"), ("Katedra Poznańska: Turyści w katedrze", "https://www.katedra.archpoznan.pl/turysci-w-katedrze/"),
                 ("Katedra Poznańska: historia katedry", "https://www.katedra.archpoznan.pl/historia-katedry-poznanskiej/"),
                 ("Katedra Poznańska: kaplice katedry", "https://www.katedra.archpoznan.pl/kaplice-katedry-poznanskiej/"),
                 ("Wikipedia: Archikatedra w Poznaniu", "https://pl.wikipedia.org/wiki/Bazylika_archikatedralna_Świętych_Apostołów_Piotra_i_Pawła_w_Poznaniu")],
        see_also=[("Punkty widokowe w Poznaniu: wszystkie wieże i tarasy", "punkty-widokowe")],
    ),
    dict(
        slug="brama-poznania", cat="zabytki", name="Brama Poznania ICHOT",
        img="brama-poznania", img_alt="Betonowy budynek Bramy Poznania i przeszklona kładka nad Cybiną wśród zieleni",
        short="Multimedialna ekspozycja o ponad tysiącletniej historii wyspy katedralnej, przy Ostrowie Tumskim.",
        badge="Pn nieczynne",
        status=None,
        lead="Brama Poznania to pierwsze w Polsce centrum interpretacji dziedzictwa. Nie jest muzeum i nie gromadzi eksponatów, ale łączy ekspozycję z bezpośrednim poznawaniem wyspy katedralnej, która sąsiaduje z budynkiem.",
        sections=[
            ("Co zobaczyć", [
                "Ekspozycja główna opowiada ponad 1000-letnią historię wyspy katedralnej, od założenia grodu w X wieku do współczesności. Mówi o ludziach, wydarzeniach i ważnych momentach związanych z wyspą, na której rozwijały się nauka, sztuka i handel. Historia jest opowiedziana prostym językiem, bez naukowego żargonu, a multimedialne rozwiązania pozwalają znaleźć dodatkowe informacje.",
                "Zwiedzanie prowadzi przez cztery sale: Gród, Wodę, Złoto i Witraż. Są dwie ścieżki: dla młodzieży i dorosłych oraz dla rodzin z dziećmi, ze zwiedzaniem w formie gry terenowej. W obu pomaga audioprzewodnik, dostępny w ośmiu wersjach językowych. Przestrzeń ekspozycji jest dostosowana do osób z różnymi niepełnosprawnościami.",
                "Audiowycieczka obejmuje spacer po wyspie katedralnej oraz katedrę. Bilet na ekspozycję uprawnia do niej w ciągu 10 dni od zwiedzania, ale dostępność audiowycieczek zmienia się sezonowo.",
                "Wypoczynek: przy budynku jest amfiteatr i ogrody. W pobliżu, na Śródce, są restauracje i kawiarnie.",
                "Ścieżka EkoEdukacji: trasa z 12 przystankami wzdłuż Cybiny i Wartostrady. Dla rodzin z dziećmi jest zeszyt zadań i plecak z pomocami do bezpłatnego wypożyczenia w Bramie Poznania. W Rzecznym Ogrodzie EkoEdukacji są ścieżka bosych stóp, kuchnia błotna, tor wodny, równoważnia i labirynt, a w Eksperymentalnym Ogrodzie Dziedzictwa odbywają się dyżury otwarte.",
                "Z Bramy Poznania zaczyna się Trakt Królewsko-Cesarski.",
            ]),
            ("Warto wiedzieć", [
                "Na pierwsze zwiedzanie ekspozycji warto zarezerwować od 1,5 do 2 godzin.",
                "Z Poznańską Kartą Turystyczną bilet kosztuje 21 zł (ulgowy 17 zł). Ostatnie wejście na ekspozycję jest godzinę przed zamknięciem. Strona obiektu podaje w sobotę i niedzielę zamknięcie raz o 19:00, raz o 18:00, więc godzinę warto potwierdzić.",
            ]),
        ],
        address="ul. Gdańska 2, 61-123 Poznań",
        hours=[("Poniedziałek", "nieczynne"), ("Wtorek–piątek", "9:00–18:00"), ("Sobota–niedziela", "10:00–19:00")],
        tickets=[("Normalny", "35 zł"), ("Ulgowy", "29 zł"), ("Rodzinny (do 5 osób, max 2 dorosłych)", "75 zł"), ("Łączony Ostrów Tumski", "49 zł, ulgowy 36 zł, rodzinny 109 zł"),
                 ("Karta Rodziny Dużej", "13 zł"), ("Karta Seniora (wybrane karty)", "18 zł"),
                 ("Grupa zorganizowana", "25 zł od osoby; rezerwacja: 61 647 76 29, wt–pt 9:00–14:00"),
                 ("Przewodnik dla grupy", "160 zł po polsku, 220 zł w języku obcym")],
        phone="+48 61 647 76 34", www=("bramapoznania.pl", "https://bramapoznania.pl/"),
        credit="brama-poznania",
        sources=[("Brama Poznania: ekspozycja główna", "https://bramapoznania.pl/ekspozycja-glowna"),
                 ("Brama Poznania: cennik", "https://bramapoznania.pl/cennik"),
                 ("Brama Poznania: godziny otwarcia", "https://bramapoznania.pl/godziny-otwarcia"),
                 ("Brama Poznania: najczęściej zadawane pytania", "https://bramapoznania.pl/faq"),
                 ("Brama Poznania: 10 lat", "https://bramapoznania.pl/10lat")],
        checked="20.10.2026",
    ),
    dict(
        slug="fara", cat="koscioly", name="Fara Poznańska",
        img="fara", og_pos="center top", img_alt="Barokowa fasada Fary Poznańskiej widoczna z wąskiej, brukowanej ulicy",
        short="Barokowy kościół farny z organami Ladegasta. Koncerty w każdą sobotę o 12:15.",
        badge="Wstęp wolny",
        status=None,
        lead="Fara Poznańska, czyli Kolegiata Farna pw. Matki Bożej Nieustającej Pomocy, św. Marii Magdaleny i św. Stanisława Biskupa, to barokowa świątynia z wysoką fasadą projektu Bartłomieja Nataniela Wąsowskiego. Kamień węgielny wmurowano w 1651 roku, a kościół konsekrowano w 1705 roku.",
        sections=[
            ("Co zobaczyć", [
                "Organy zbudowane w 1876 roku przez Friedricha Ladegasta, słynnego organmistrza z Weissenfels. Mają 2579 piszczałek, a największe mierzą 6 metrów.",
                "Po koncercie, około 12:45, można dołączyć do zwiedzania z przewodnikiem. Są trzy trasy: wnętrze kościoła (30–40 minut), miejsca ukryte (zakrystia i barokowy kapitularz) oraz podziemia.",
            ]),
            ("Koncerty organowe", [
                "W każdą sobotę o 12:15 od około dwudziestu lat odbywa się koncert na organach Ladegasta.",
                "Za 5 zł od osoby można też wejść z organistą na chór i obejrzeć instrument z bliska. Parafia podkreśla, że to jedyna okazja w Poznaniu, by poznać organy od środka.",
            ]),
            ("Warto wiedzieć", [
                "Kościół jest otwarty codziennie, ale parafia prosi, by nie zwiedzać go w czasie mszy.",
                "Opłata za zwiedzanie z przewodnikiem jest cegiełką na rzecz Fary. Dla grup mniejszych niż 10 osób obowiązuje opłata minimalna: 20 zł za jedną trasę, 35 zł za dwie, 50 zł za trzy.",
                "Parafia podaje też mszę w soboty o 12:45 (poza lipcem i sierpniem), więc godzinę zbiórki na zwiedzanie warto potwierdzić telefonicznie: (61) 853 03 97.",
            ]),
        ],
        address="ul. Gołębia 1, 61-834 Poznań",
        hours=[("Kościół", "codziennie 6:00–19:30"), ("Koncert organowy", "soboty 12:15"), ("Zwiedzanie z przewodnikiem", "soboty ok. 12:45")],
        tickets=[("Wejście do kościoła", "bezpłatnie"), ("Trasy z przewodnikiem", "2–5 zł od osoby, ulgowy 1,5–4 zł"), ("Wizyta u organisty", "5 zł od osoby")],
        phone="+48 61 852 69 50", www=("fara.archpoznan.pl", "https://fara.archpoznan.pl/pl/"),
        credit="fara",
        sources=[("Fara Poznańska: zwiedzanie", "https://fara.archpoznan.pl/pl/zwiedzanie?view=article&id=24%3Agodziny-otwarcia&catid=2"),
                 ("Fara Poznańska: historia kościoła", "https://fara.archpoznan.pl/pl/fara"),
                 ("Fara Poznańska: architektura", "https://fara.archpoznan.pl/pl/architektura"),
                 ("Fara Poznańska: organy Ladegasta", "https://fara.archpoznan.pl/pl/wnetrze-kosciola/47-organy-ladegasta"),
                 ("Fara Poznańska: kontakt", "https://fara.archpoznan.pl/pl/kontakt")],
    ),
    dict(
        slug="zamek-krolewski", cat="zabytki", name="Zamek Królewski i Muzeum Sztuk Użytkowych",
        img="zamek-krolewski", img_alt="Wieża i fasada Zamku Królewskiego na Górze Przemysła w jesiennym świetle",
        short="Zamek Przemysła II z Muzeum Sztuk Użytkowych i 43-metrową wieżą widokową. We wtorki wstęp wolny.",
        badge="Wt wstęp wolny",
        status=None,
        lead="Zamek na Wzgórzu Przemysła wzniesiono prawdopodobnie w XIII wieku z inicjatywy Przemysła II. Budowę mógł zacząć już jego ojciec, Przemysł I. Po zniszczeniach w 1945 roku historyzujący gmach zamku z wieżą wzniesiono dopiero w latach 2010–2013. Dziś mieści się w nim Muzeum Sztuk Użytkowych, oddział Muzeum Narodowego w Poznaniu, a w wieży jest taras widokowy.",
        sections=[
            ("O miejscu", [
                "Po wojnie, w 1965 roku, odbudowano tylko budynek Raczyńskiego, w którym działało Muzeum Rzemiosł Artystycznych (od 1991 roku Muzeum Sztuk Użytkowych). Historyzujący gmach zamku z wieżą, zbudowaną na reliktach pierwotnej wieży z XIII wieku, wzniesiono dopiero w latach 2010–2013 i połączono z budynkiem Raczyńskiego.",
                "Od 26 czerwca 2016 roku można wejść na wieżę widokową, z której rozciąga się widok na miasto.",
            ]),
            ("Muzeum Sztuk Użytkowych", [
                "Muzeum pokazuje około 2000 przedmiotów od średniowiecza do współczesności i według własnego opisu jest jedynym takim miejscem w Polsce. Stała ekspozycja zajmuje prawie 1500 m² w połączonych budynkach Raczyńskiego i Zamku Przemysła.",
                "Dominuje europejska sztuka użytkowa, wśród niej wyroby polskie. Są też obiekty z innych kontynentów, pokazane z europejskiej perspektywy. W zbiorach są m.in. meble, ceramika, szkło i metale, broń, biżuteria, tkaniny, stroje i design, a w muzeum można też posłuchać muzyki i obejrzeć filmy.",
                "Część wystawy dotyczy króla Przemysła II i znaku Orła Białego, a także dziejów zamku poznańskiego od XIII wieku do 1945 roku oraz powojennych koncepcji jego odbudowy.",
            ]),
            ("Wieża widokowa", [
                "Na wieżę można wejść po obejrzeniu wystawy. Ma 43 metry i dwa tarasy: zadaszony na wysokości 30 metrów i otwarty na samym szczycie. Widać z nich panoramę Poznania i okolic.",
                "Na górę prowadzi blisko 200 stopni. Według muzeum na tarasy widokowe wchodzi się wyłącznie schodami. 26.10.2026 strona muzeum informowała dodatkowo o awarii windy.",
                "Na tarasie może jednocześnie przebywać do 25 osób. Przy złej pogodzie taras otwarty jest zamykany.",
            ]),
            ("Warto wiedzieć", [
                "Winda w budynku dowozi na wszystkie ekspozycje. Osoby na wózkach i z wózkami dziecięcymi wchodzą alternatywnym wejściem, rampą przy budynku Raczyńskiego (ok. 15 m od głównego wejścia). Po przybyciu trzeba zadzwonić pod 61 85 68 073.",
                "Najdłużej, do 20:00, muzeum jest czynne w piątki. Kasa zamyka się 30 minut przed zamknięciem muzeum. Godziny mogą się zmienić w dni świąteczne, przy dodatkowych dniach wolnych lub przerwach technicznych.",
                "Muzeum jest nieczynne 1 stycznia, w Wielki Piątek, Wielką Sobotę, Niedzielę i Poniedziałek Wielkanocny, w Boże Ciało, 1 listopada oraz 24, 25, 26 i 31 grudnia. W dni 6 stycznia, 1 maja, 3 maja, 15 sierpnia i 11 listopada jest czynne jak w niedzielę. Najbliższe ciche godziny (15:00–17:00) przypadają 6 grudnia 2026 roku.",
                "Dzieci i młodzież w wieku 8–26 lat płacą 1 zł, a we wtorki wstęp jest bezpłatny dla wszystkich. Strona muzeum podaje też zasady dla posiadaczy Karty Dużej Rodziny i Poznańskiej Karty Turystycznej.",
            ]),
        ],
        address="Góra Przemysła 1, 61-768 Poznań",
        desc="Zamek Królewski w Poznaniu z Muzeum Sztuk Użytkowych i 43-metrową wieżą widokową: godziny, bilety, wtorki bezpłatnie. Góra Przemysła 1.",
        hours=[("Poniedziałek", "nieczynne"), ("Wtorek–środa", "10:00–16:00"), ("Czwartek", "10:00–18:00"), ("Piątek", "10:00–20:00"), ("Sobota–niedziela", "10:00–17:00")],
        tickets=[("Normalny", "20 zł"), ("Ulgowy", "13 zł"), ("Dzieci i młodzież 8–26 lat", "1 zł"), ("Wtorek", "wstęp wolny"), ("Bilet grupowy (do 25 osób)", "250 zł"), ("Wystawa czasowa", "7 zł, ulgowy 5 zł")], checked="26.10.2026",
        phone="+48 61 856 80 75", www=("mnp.art.pl", "https://mnp.art.pl/muzeum-sztuk-uzytkowych-w-zamku-krolewskim-w-poznaniu"),
        credit="zamek-krolewski",
        sources=[("MNP: Wizyta (godziny, bilety, dostępność)", "https://mnp.art.pl/profile/wizyta"),
                 ("MNP: Muzeum Sztuk Użytkowych w Zamku Królewskim", "https://mnp.art.pl/muzeum-sztuk-uzytkowych-w-zamku-krolewskim-w-poznaniu"),
                 ("MNP: Zamek", "https://mnp.art.pl/profile/zamek"),
                 ("kultura.poznan.pl: Muzeum Sztuk Użytkowych", "https://kultura.poznan.pl/mim/kultura/muzea-w-poznaniu,poi,202,12/muzeum-sztuk-uzytkowych-zamek-przemysla,15703.html"),
                 ("poznan.pl: Wieża widokowa – Wzgórze Przemysła", "https://www.poznan.pl/mim/wortals/turystyka/inne-atrakcje,poi,3391/wieza-widokowa-wzgorze-przemysla,61910.html")],
        see_also=[("Punkty widokowe w Poznaniu: wszystkie wieże i tarasy", "punkty-widokowe"),
                  ("Taras widokowy Collegium Altum", "atrakcje/taras-widokowy-collegium-altum")],
    ),
    dict(
        slug="zamek-cesarski", cat="zabytki", name="Zamek Cesarski",
        img="zamek-cesarski", img_alt="Zamek Cesarski w Poznaniu widziany z góry, z wieżą zegarową",
        short="Neoromańska rezydencja Wilhelma II z lat 1905–1910. Dziś Centrum Kultury Zamek.",
        badge="Codziennie",
        status=None,
        lead="Zamek Cesarski powstał w latach 1905–1910 jako rezydencja Wilhelma II, ostatniego niemieckiego cesarza (poznan.pl liczy budowę od 1904 roku). To neoromański gmach projektu Franza Schwechtena z dominującą 74-metrową wieżą zegarową. Po zniszczeniu w czasie II wojny światowej wieża jest o 30 m niższa.",
        sections=[
            ("O miejscu", [
                "Zamek kosztował 5 milionów marek, a cesarza gościł tylko trzykrotnie: w 1910 roku na otwarciu, w 1913 roku na inauguracji zamkowej kaplicy i w 1915 roku, gdy w rezydencji kwaterowało dowództwo niemieckiej armii na Wschodzie. Podobno cesarz osobiście ingerował w architekturę gmachu.",
                "Po wybuchu powstania wielkopolskiego zamek przeszedł w ręce Polaków. Był siedzibą najpierw ministra byłej Dzielnicy Pruskiej, a od 1922 roku prezydenta Rzeczypospolitej podczas jego pobytów w Poznaniu. Dawne apartamenty cesarskie na pierwszym piętrze zajął Prezydent, a dolne piętra Uniwersytet Poznański.",
                "W czasie II wojny światowej Niemcy przeprowadzili gruntowną przebudowę za ponad 16 mln marek, z czego milion przekazał osobiście Hitler. Projektantem był Franz Böhmer. Kaplicę zamieniono na gabinet Hitlera: rozebrano absydę, a w jej miejscu powstał niewielki balkon widoczny od ul. Święty Marcin, wykuto też paradne wejście od tej ulicy. Hitler prawdopodobnie nigdy nie zobaczył swojej poznańskiej rezydencji.",
                "31 stycznia 1945 roku rozpoczął się ostrzał zamku, który zniszczył wieżę. Po wojnie pojawiały się głosy za całkowitym zniszczeniem gmachu, ale ostatecznie rozebrano tylko zniszczoną wieżę. Od 1948 roku zamek był siedzibą władz miasta (do 1962 roku), od początku lat 60. Pałacem Kultury, a od połowy lat 90. mieści Centrum Kultury Zamek. W 1979 roku wpisano go do rejestru zabytków.",
            ]),
            ("Co zobaczyć", [
                "Od 2004 roku trwa renowacja gmachu i jego otoczenia. Budynek odzyskał oryginalne, jasne barwy, odnowiono skwer przy zamku i fontannę wzorowaną na XIII-wiecznej fontannie lwów z Alhambry w Grenadzie.",
                "W zamku działają m.in. kino Pałacowe i galerie, w tym Galeria Fotografii pf. Według poznan.pl mieszczą się tu także Teatr Animacji i klub jazzowy Blue Note.",
                "Audioprzewodnik (urządzenie albo aplikacja w telefonie z trzydniowym dostępem) ma trasy: podstawową (po polsku, angielsku i ukraińsku), dla dzieci (7–14 lat), bez barier (po polsku, windą zamiast schodów) oraz z lektorem polskiego języka migowego (tylko w aplikacji). Urządzenia wydaje Informacja CK Zamek do 18:00 (zwrot do 19:00), a zamiast urządzenia można użyć kodu dostępu w aplikacji.",
            ]),
            ("Warto wiedzieć", [
                "Od 5 września do 6 grudnia 2026 trwa wystawa „Świat jak zielnik. Natura w sztuce od XVII do XXI wieku”. W tym czasie CK Zamek poleca bilet łączony na wystawę i historyczną część zamku: normalny 40 zł z audioprzewodnikiem lub 35 zł z mapką, ulgowy 35 zł lub 30 zł.",
                "Cena ulgowa obowiązuje także posiadaczy karty OK Poznań. Bilety kupisz w kasie, w biletomacie w Holu Wielkim albo online na bilety24.pl.",
                "Strona zwiedzania i kontakt podają zamknięcie o 19:00 (sprzedaż biletów do 18:00), a niektóre inne podstrony CK Zamek 20:00, więc godzinę zamknięcia potwierdź w Informacji.",
            ]),
        ],
        address="ul. Święty Marcin 80/82, 61-809 Poznań",
        hours=[("Zwiedzanie", "codziennie 12:00–19:00"), ("Sprzedaż biletów", "do 18:00"), ("Audioprzewodniki", "wydawane do 18:00, zwrot do 19:00")],
        tickets=[("Zwiedzanie zamku", "10 zł, ulgowy 7 zł"), ("Audioprzewodnik", "20 zł, ulgowy 15 zł"), ("Bilet łączony z wystawą (5.09–6.12.2026)", "40 zł z audioprzewodnikiem, 35 zł z mapką; ulgowy 35 zł i 30 zł")],
        phone="+48 61 646 52 72", www=("ckzamek.pl", "https://ckzamek.pl/podstrony/6071-zwiedzanie-zamku/"),
        credit="zamek-cesarski",
        sources=[("CK Zamek: zwiedzanie i audioprzewodniki", "https://ckzamek.pl/podstrony/6071-zwiedzanie-zamku/"),
                 ("CK Zamek: audioprzewodniki", "https://ckzamek.pl/podstrony/7171-audioprzewodniki/"),
                 ("CK Zamek: historia i zwiedzanie", "https://ckzamek.pl/podstrony/63-historia-i-zwiedzanie/"),
                 ("CK Zamek: kontakt", "https://ckzamek.pl/podstrony/16-kontakt/"),
                 ("CK Zamek: Imieniny Ulicy Święty Marcin 2026", "https://ckzamek.pl/podstrony/12-przestrzen-miasta/"),
                 ("CK Zamek: cennik (aktualizacja 30.03.2026)", "https://ckzamek.bilety24.pl/wp-content/uploads/2026/04/CENNIK_CK_ZAMEK_aktualizacja_30.03.2026.pdf"),
                 ("poznan.pl: Zamek Cesarski – ostatni zbudowany w Europie zamek monarszy", "https://www.poznan.pl/mim/s8a/czy-wiesz-ze,doc,576/wybudowany-w-1910-r-zamek-cesarski-w-poznaniu-byl-ostatnim-zbudowanym-w-europie-zamkiem-monarszym,3286.html"),
                 ("Cyryl: Zamek Cesarski i jego rezydenci 1905–1944", "https://cyryl.poznan.pl/kolekcja/zamek-cesarski-i-jego-rezydenci-1905-1944-pocztowki-tadeusza-bonieckiego/")],
    ),
    dict(
        slug="cytadela", cat="zabytki", name="Cytadela",
        img="cytadela", img_alt="Pomnik Bohaterów u szczytu schodów w Parku Cytadela, wśród jesiennych drzew", og_pos="center top",
        short="Park na miejscu pruskiego fortu. Cmentarze wojenne, Nierozpoznani i dwa muzea.",
        badge="Park bezpłatnie",
        status=None,
        lead="Park Cytadela, największy park Poznania, zajmuje około 100 hektarów w miejscu Fortu Winiary, największego fortu artyleryjskiego ówczesnej Europy. Leży kilkanaście minut spacerem od Starego Rynku i od 2008 roku jest pomnikiem historii.",
        sections=[
            ("O miejscu", [
                "Budowę fortu rozpoczęto 23 czerwca 1828 roku, po przeniesieniu wsi Winiary i Bonin. Fort powstał w systemie nowopruskim. W grudniu 1834 roku oddano do użytku Kernwerk, czyli redutę koszarową, zaprojektowaną przez majora Johanna Leopolda Ludwiga von Brese. Według Wielkopolskiego Muzeum Niepodległości prace trwały do 1842 roku. Fort miał fosę o szerokości 6–32 m i głębokości około 7 m oraz ceglane mury grubości 1,3–1,8 m.",
                "W twierdzy więziono polskich spiskowców po powstaniach 1846, 1848 i 1863, a także jeńców wojen z Danią (1864), Austrią (1866) i Francją (1870–1871). Cytadelę opanowali powstańcy wielkopolscy i formowano tu I Pułk Strzelców Wielkopolskich.",
                "10 września 1939 roku Poznań zajął Wehrmacht. 23 lutego 1945 roku po pięciodniowym szturmie Cytadelę zdobyła Armia Czerwona.",
                "W latach 1950–1958 fort rozebrano, a cegłę wykorzystano przy budowie osiedli w Poznaniu i odbudowie Warszawy. Od 1962 roku urządzano tu Park-Pomnik Braterstwa Broni i Przyjaźni Polsko-Radzieckiej, który w 1992 roku przemianowano na Park Cytadela.",
            ]),
            ("Co zobaczyć", [
                "Pomnik Bohaterów na szczycie monumentalnych schodów prowadzących od strony centrum miasta.",
                "Nierozpoznani: instalacja Magdaleny Abakanowicz ze 112 bezgłowych figur odlanych z żeliwa w Śremie. Uroczyście otwarto ją 19 października 2002 roku z okazji 750-lecia lokacji Poznania.",
                "Cmentarze wojskowe na stokach dawnego fortu: powstania styczniowego, powstania wielkopolskiego, powstań śląskich oraz poległych w obu wojnach światowych. Pochowano tu prochy 48 lotników alianckich z Wielkiej Ucieczki ze Stalagu Luft III, zgładzonych przez Niemców w 1944 roku.",
                "Rzeźby z lat 1968–1970: „Braterstwo Broni” Dimitra Sowy z Charkowa i „Saperzy” Jana Jakóba. Pomnik marszałka Wasilija Czujkowa, odsłonięty w 1982 roku, oraz Dzwon Pokoju i Przyjaźni Między Narodami z 1986 roku.",
                "Rosarium i Ogród Daliowy, który powstał w 2025 roku w ramach Poznańskiego Budżetu Obywatelskiego.",
                "Dwa pomniki przyrody: Dąb im. gen. Wasilija Czujkowa i Dąb Cytadelowców Poznańskich.",
                "Muzeum Uzbrojenia, z plenerowym parkiem sprzętu wojskowego (czołgi, działa, moździerze, samoloty i śmigłowce) oraz ekspozycją w schronie, i Muzeum Armii „Poznań”. Oba są oddziałami Wielkopolskiego Muzeum Niepodległości.",
            ]),
            ("Twierdza Poznań", [
                "W latach 1828–1869 zbudowano twierdzę poligonalną. Oprócz fortu na Wzgórzu Winiarskim tworzyły ją umocnienia na prawym brzegu Warty (Ostrów Tumski, Miasteczko, Piotrowo, Malta, Komandoria i Śródka) oraz rdzeń na lewym brzegu. W 1902 roku zdecydowano o zniesieniu rdzenia na lewym brzegu, z wyjątkiem Cytadeli.",
                "W drugiej połowie XIX wieku powstała twierdza fortowa: dziewięć fortów głównych (I–IX) i dziewięć pośrednich, budowanych od 1873 roku według projektu gen. von Biehlera.",
                "Z twierdzy poligonalnej zachowały się m.in. resztki Fortu Winiary, część reduty Fortu Roon, zachodni mur skarpy Warty przy Wielkiej Śluzie, zachodni przyczółek Śluzy Katedralnej, osiowy blokhauz Bastionu IV oraz fragment arsenału przy ulicy Garbary.",
            ]),
            ("Warto wiedzieć", [
                "W parku są alejki pieszo-rowerowe, place zabaw, trzy siłownie plenerowe, kawiarenka i restauracja. Co sobotę odbywa się tu bieg parkrun, a w okresie wielkanocnym młodzież przygotowuje misteria pasyjne.",
                "Relikty fortyfikacji są zimowiskiem nietoperzy chronionym w sieci Natura 2000.",
                "Zwiedzanie Muzeum Uzbrojenia trwa 45–90 minut, a kasa zamykana jest 30 minut przed zamknięciem muzeum. Wejście jest bez barier. Oprowadzanie z przewodnikiem trzeba zarezerwować wcześniej (70 zł po polsku, 90 zł po angielsku).",
                "Co roku w ostatni pełny weekend sierpnia odbywają się Dni Twierdzy Poznań, podczas których forty są dostępne do zwiedzania.",
            ]),
        ],
        address="al. Armii Poznań, 61-663 Poznań",
        hours=[("Park", "ogólnodostępny"), ("Muzeum Uzbrojenia (III–X)", "wt–sb 10:00–17:00, nd 10:00–16:00"), ("Muzeum Uzbrojenia (XI–II)", "wt–nd 10:00–16:00"), ("Muzeum Armii „Poznań”", "wt–nd 10:00–16:00 (od 20.01.2026)"), ("Poniedziałek", "muzea nieczynne")],
        tickets=[("Park", "bezpłatnie"), ("Muzeum Uzbrojenia", "15 zł, ulgowy 10 zł, dzieci do 7 lat bezpłatnie"), ("Muzeum Armii „Poznań”", "10 zł, ulgowy 6 zł"), ("Bilet łączony obu muzeów", "20 zł, ulgowy 12 zł"), ("Wtorek", "muzea bezpłatnie")],
        phone="+48 61 820 45 03", www=("wmn.poznan.pl", "https://www.wmn.poznan.pl/oddzialy-4/muzeum-uzbrojenia/"),
        credit="cytadela",
        sources=[("Poznan.pl: Cytadela – park i pomnik historii", "https://www.poznan.pl/mim/info/news/cytadela-park-i-pomnik-historii,265518.html"),
                 ("Poznan.pl: Park Cytadela", "https://www.poznan.pl/mim/turystyka/parki,poi,3338/-,51946.html"),
                 ("Poznan.pl: Twierdza poligonalna – Fort Winiary", "https://www.poznan.pl/mim/main/-,p,37,3382,3484.html"),
                 ("Poznan.pl: Dawna twierdza Poznań", "https://www.poznan.pl/mim/wortals/turystyka/fortyfikacje,poi,2575/dawna-twierdza-poznan,45909.html"),
                 ("Poznan.pl: Magdalena Abakanowicz – Nierozpoznani", "https://poznan.pl/mim/wortals/cik/events/magdalena-abakanowicz-nierozpoznani,10403.html"),
                 ("Visit Poznań: Park Cytadela", "https://visitpoznan.pl/park-cytadela"),
                 ("Odkryj Wielkopolskę: Park Cytadela w Poznaniu", "https://regionwielkopolska.pl/katalog-obiektow/park-cytadela-w-poznaniu/"),
                 ("WMN: Muzeum Uzbrojenia", "https://www.wmn.poznan.pl/oddzialy/muzeum-uzbrojenia/"),
                 ("WMN: ceny biletów", "https://www.wmn.poznan.pl/ceny-biletow/"),
                 ("WMN: godziny otwarcia", "https://www.wmn.poznan.pl/godziny-otwarcia/"),
                 ("WMN: Muzeum Armii „Poznań”", "https://www.wmn.poznan.pl/oddzialy-4/muzeum-armii-poznan/")],
        see_also=[("Muzeum Uzbrojenia: czołgi i samoloty pod gołym niebem", "atrakcje/muzeum-uzbrojenia"),
                  ("Muzeum Armii „Poznań”: szlak bojowy 1939 roku", "atrakcje/muzeum-armii-poznan"),
                  ("Pomnik Armii „Poznań”", "atrakcje/pomnik-armii-poznan"),
                  ("Fort VII: Muzeum Martyrologii Wielkopolan", "atrakcje/fort-vii"),
                  ("Fort III: pruski fort w Nowym Zoo", "atrakcje/fort-iii"),
                  ("Fort IVa: zimowisko nietoperzy", "atrakcje/fort-iva"),
                  ("Fort Va Bonin: zwiedzanie z przewodnikiem w mundurze", "atrakcje/fort-va")],
    ),

    # ─── MUZEA ───
    dict(
        slug="muzeum-narodowe", cat="muzea", name="Muzeum Narodowe",
        img="muzeum-narodowe", img_alt="Fasada gmachu Muzeum Narodowego w Poznaniu z szczytem, napisem i mozaikami nad oknami",
        short="Jedyny obraz Moneta w polskich zbiorach i duży zbiór obrazów Malczewskiego.",
        badge="Wt wstęp wolny",
        status=("warning", "Według strony muzeum Galeria Sztuki Średniowiecznej, Galeria Sztuki Polskiej XVI–XVIII w. i Galeria Sztuki Europejskiej w historycznym gmachu są obecnie nieczynne."),
        lead="Galeria Malarstwa i Rzeźby to główna siedziba Muzeum Narodowego w Poznaniu, jednego z najstarszych, największych i najważniejszych muzeów w Polsce. Jego początki to Muzeum Starożytności Polskich i Słowiańskich, powołane w 1857 roku przez Towarzystwo Przyjaciół Nauk. Obecną nazwę muzeum nosi od 1950 roku.",
        sections=[
            ("Co zobaczyć", [
                "Plaża w Pourville Claude'a Moneta, jedyny obraz tego impresjonisty w polskich zbiorach.",
                "Gmach składa się z dwóch części: starej z 1904 roku i nowej z 2001 roku. Wejście dla zwiedzających i kasa są w holu nowego gmachu, w którym zwiedzanie ekspozycji stałej się zaczyna. Na trzech piętrach nowego gmachu pokazana jest sztuka polska, w tym największy zbiór obrazów Jacka Malczewskiego, oraz sztuka współczesna (m.in. Kantor, Nowosielski).",
                "W historycznym gmachu są zbiory sztuki europejskiej (piętro), w tym jedyny w Polsce zbiór malarstwa hiszpańskiego, średniowiecza i baroku polskiego z kolekcją portretów trumiennych (parter) oraz starożytności z rzymskim portretem cesarskim (podziemia). Według strony muzeum galerie sztuki średniowiecznej, polskiej XVI–XVIII wieku i europejskiej są obecnie nieczynne.",
                "Galeria Plakatu i Projektowania Graficznego, Gabinet Rycin i Rysunków oraz Gabinet Numizmatyczny nie mają ekspozycji stałej. Ich zbiory pokazywane są okazjonalnie na wystawach czasowych.",
            ]),
            ("Warto wiedzieć", [
                "Z Poznańską Kartą Turystyczną wstęp na wystawy stałe jest bezpłatny.",
                "Dla rodzin z dziećmi przy zakupie biletów można bezpłatnie otrzymać Walizkę Muzealnych Tropicieli i Przewodnik Muzealnych Tropicieli.",
                "Muzeum Narodowe w Poznaniu ma osiem oddziałów: Muzeum Sztuk Użytkowych w Zamku Królewskim, Ratusz – Muzeum Poznania, Wielkopolskie Muzeum Wojskowe, Muzeum Instrumentów Muzycznych i Muzeum Kultur Świata w Poznaniu oraz rezydencje poza miastem: Muzeum Pałac w Rogalinie, Muzeum Adama Mickiewicza w Śmiełowie i Muzeum Zamek w Gołuchowie.",
            ]),
        ],
        address="al. Marcinkowskiego 9, 61-745 Poznań",
        hours=[("Poniedziałek", "nieczynne"), ("Wtorek–środa", "10:00–16:00"), ("Czwartek", "10:00–18:00"), ("Piątek", "10:00–20:00"), ("Sobota–niedziela", "10:00–17:00")],
        tickets=[("Normalny", "20 zł"), ("Ulgowy", "13 zł"), ("Dzieci i młodzież 8–26 lat", "1 zł"), ("Wtorek", "wstęp wolny")], checked="01.10.2026",
        phone="+48 61 856 80 00", www=("mnp.art.pl", "https://mnp.art.pl/"),
        credit="muzeum-narodowe",
        sources=[("kultura.poznan.pl: Muzeum Narodowe", "https://kultura.poznan.pl/mim/kultura/muzea-w-poznaniu,poi,202,12/muzeum-narodowe-w-poznaniu,15730.html"),
                 ("Visit Poznań: Galeria Malarstwa i Rzeźby", "https://visitpoznan.pl/galeria-malarstwa-i-rzezby-muzeum-narodowe-w-poznaniu"),
                 ("MNP: O Muzeum", "https://mnp.art.pl/o-nas/muzeum"),
                 ("MNP: Historia", "https://mnp.art.pl/o-nas/historia-2")],
    ),
    dict(
        slug="rogalowe-muzeum", cat="muzea", name="Rogalowe Muzeum Poznania",
        img="rogalowe-muzeum", img_alt="Rogale świętomarcińskie i składniki (migdały, rodzynki, kandyzowana skórka) wokół serca z mąki z napisem ROGA-LOVE",
        short="Pokaz o rogalach świętomarcińskich przy Starym Rynku. Bilety warto kupić wcześniej.",
        badge="Rezerwuj wcześniej",
        status=None,
        lead="Rogalowe Muzeum to interaktywny pokaz przy Starym Rynku. Pokaz ma interaktywny charakter: uczestnicy poznają historię rogala świętomarcińskiego i to, jak powstaje według tradycyjnej receptury.",
        sections=[
            ("Pokazy", [
                "Pokaz rogalowy trwa 55–60 minut, pokaz rogalowo-koziołkowy 65 minut. W pokazie rogalowo-koziołkowym, oprócz tego, co w zwykłym pokazie, ogląda się koziołki z okien muzeum (o 12:00 przy pokazie od 11:00 i o 15:00 przy pokazie od 14:00) i poznaje historię ich mechanizmu.",
                "Pokazy po angielsku są w soboty i niedziele o 14:00, a w lipcu i sierpniu codziennie o 14:00. Czasami jest dodatkowy pokaz o 15:30, bez koziołków, w tej samej cenie. Zalecana jest przynajmniej podstawowa znajomość angielskiego.",
                "Pokazy często się wyprzedają, więc bilet najlepiej kupić z wyprzedzeniem.",
            ]),
            ("Program pokazu", [
                "Pokazy na żywo prowadzi Rogalowy Mistrz z pomocnikiem. W programie są: legenda o rogalach i pochodzenie nazwy, receptura i składniki rogala świętomarcińskiego, wspólne przygotowanie rogali tradycyjnymi narzędziami, elementy poznańskiej gwary, multimedialna prezentacja o historii Poznania, certyfikaty czeladnicze i degustacja certyfikowanych rogali (na wynos).",
                "Pokaz ma formę interaktywną, łączy przedstawienie, prezentację, pogadankę i warsztat. Na początku z publiczności wybierani są ochotnicy, którzy zakładają stroje i pomagają przy kolejnych czynnościach. Pokaz jest dla wszystkich grup wiekowych, najlepiej sprawdza się powyżej 3. roku życia.",
            ]),
            ("Warto wiedzieć", [
                "Muzeum jest czynne 7 dni w tygodniu, z wyjątkiem wybranych dni (sprawdź aktualności na stronie muzeum). Harmonogram godzin nie oznacza dostępności każdej godziny dla gości indywidualnych, bo niektóre pokazy są na wyłączność dla grup.",
                "Bilety kupisz online do 30 minut przed pokazem (płatność przelewem, kartą Visa lub Mastercard albo BLIK) lub w kasie muzeum, około 20 minut przed otwartymi pokazami, w miarę dostępności miejsc. Zalecany jest zakup online, bo zdarzają się komplety.",
                "Bilet ulgowy przysługuje osobom w wieku 3–25 lat, osobom 65+, emerytom, rencistom, osobom niepełnosprawnym i ich opiekunom oraz posiadaczom Karty Dużej Rodziny i Osobistej Karty Poznańskiej.",
            ]),
        ],
        address="Stary Rynek 41/2 (wejście od ul. Klasztornej 23), 61-772 Poznań",
        hours=[("Pokazy codziennie", "11:00 (z koziołkami), 12:30, 14:00 (z koziołkami), 15:30"), ("Dodatkowo w soboty", "17:00"), ("Po angielsku", "sb–nd 14:00, w VII–VIII codziennie")],
        tickets=[("Pokaz rogalowy", "41 zł, ulgowy 37 zł"), ("Pokaz rogalowo-koziołkowy", "47 zł, ulgowy 43 zł"), ("Pokaz po angielsku", "47 zł, bilet ulgowy w tej samej cenie"),
                 ("Bilet rodzinny (2 dorosłych i 2 dzieci w wieku 3–18 lat)", "37 zł od osoby na pokaz rogalowy, 43 zł na rogalowo-koziołkowy"), ("Dzieci do 3 lat", "1 zł")],
        phone=None, www=("rogalowemuzeum.pl", "https://rogalowemuzeum.pl/indywidualni/"),
        credit="rogalowe-muzeum",
        checked="21.10.2026",
        sources=[("Rogalowe Muzeum: dla indywidualnych, cennik od 2.01.2026", "https://rogalowemuzeum.pl/indywidualni/#cennik"),
                 ("Rogalowe Muzeum: dla indywidualnych (oferta, terminy, przebieg wizyty)", "https://rogalowemuzeum.pl/indywidualni/")],
    ),
    dict(
        slug="muzeum-powstania", cat="muzea", name="Muzeum Powstania Wielkopolskiego",
        img="muzeum-powstania", img_alt="Klasycystyczny Odwach na Starym Rynku",
        short="Historia zwycięskiego powstania 1918–1919 w klasycystycznym Odwachu na rynku.",
        badge="Wt wstęp wolny",
        status=None,
        lead="Muzeum Powstania Wielkopolskiego 1918–1919 mieści się w Odwachu na Starym Rynku, w budynku z 1787 roku. Jest oddziałem Wielkopolskiego Muzeum Niepodległości i działa tu od 2001 roku.",
        sections=[
            ("Co zobaczyć", [
                "Wystawę stałą „Powstanie Wielkopolskie 1918–1919. Droga do Niepodległości”, która pokazuje genezę, przebieg i rezultaty powstania. Ma oryginalną aranżację, nowe zabytki, plansze i multimedia, a pokazano na niej m.in. udział Armii Wielkopolskiej w wojnie polsko-bolszewickiej i Poznań międzywojenny.",
                "Sam Odwach to jeden z najwybitniejszych zabytków architektury polskiej. Wybudowano go z inicjatywy starosty generalnego wielkopolskiego Kazimierza Raczyńskiego, a projekt najprawdopodobniej wykonał architekt królewski Jan Chrystian Kamsetzer.",
            ]),
            ("Historia Odwachu", [
                "W listopadzie 1918 roku w Odwachu miała siedzibę Straż Ludowa, jedna z najważniejszych formacji Powstania Wielkopolskiego, a 27 grudnia załoga ruszyła do powstania. W 1945 roku, podczas walk o Twierdzę Poznań, budynek został poważnie zniszczony, a odbudowano go w latach 1949–1951. Od 2004 roku przed Odwachem znów stoi żołnierz w mundurze historycznym.",
            ]),
            ("Warto wiedzieć", [
                "Grupy mogą zamówić oprowadzanie po polsku (70 zł) lub po angielsku (90 zł).",
                "Na Wzgórzu Świętego Wojciecha, u zbiegu ulic Księcia Józefa i Północnej, trwa budowa nowej siedziby muzeum (budowa ruszyła w styczniu 2024 roku, projekt: pracownia WXCA). Eksponaty z Odwachu są stopniowo przekazywane do konserwacji, a wystawę stałą zobaczymy w nowej siedzibie jesienią 2028 roku. Według muzeum w najbliższych miesiącach Odwach pozostaje otwarty, a w 2027 roku zaplanowano wydarzenia pożegnalne.",
                "Godziny otwarcia mogą się zmienić w święta, dodatkowe dni wolne i na czas przerw technicznych.",
            ]),
        ],
        address="Stary Rynek 3, 61-772 Poznań",
        hours=[("Poniedziałek", "nieczynne"), ("Marzec–październik", "wt–sb 10:00–17:00, nd 10:00–16:00"), ("Listopad–luty", "wt–nd 10:00–16:00")],
        tickets=[("Normalny", "15 zł"), ("Ulgowy", "10 zł"), ("Wtorek", "wstęp wolny")],
        phone="+48 61 853 19 93", www=("wmn.poznan.pl", "https://www.wmn.poznan.pl/oddzialy-4/muzeum-powstania-wielkopolskiego-1918-1919/"),
        credit="muzeum-powstania",
        sources=[("WMN: godziny otwarcia", "https://www.wmn.poznan.pl/godziny-otwarcia/"),
                 ("WMN: ceny biletów", "https://www.wmn.poznan.pl/ceny-biletow/"),
                 ("WMN: Muzeum na walizkach", "https://www.wmn.poznan.pl/moje-aktualnosci/muzeum-na-walizkach/"),
                 ("WMN: Budowa nowej siedziby, postęp prac", "https://www.wmn.poznan.pl/moje-aktualnosci/postep-w-pracach-na-budowie-nowej-siedziby-muzeum/"),
                 ("Poznan.pl: Muzeum Powstania Wielkopolskiego 1918–1919", "https://www.poznan.pl/mim/wortals/turystyka/muzea-w-poznaniu,poi,202/muzeum-powstania-wielkopolskiego-1918-1919-oddzial-wielkopolskiego-muzeum-niepodleglosci,25961.html"),
                 ("Region Wielkopolska: Odwach w Poznaniu", "https://regionwielkopolska.pl/en/katalog-obiektow/odwach-in-poznan/")],
    ),
    dict(
        slug="muzeum-archeologiczne", cat="muzea", name="Muzeum Archeologiczne",
        img="muzeum-archeologiczne", img_pos="center 40%", img_alt="Rzeźbiony renesansowy portal z kutą kratą przy wejściu do Pałacu Górków, siedziby Muzeum Archeologicznego",
        short="Pradzieje Wielkopolski i starożytny Egipt w renesansowym Pałacu Górków.",
        badge="Wt wstęp wolny",
        status=None,
        lead="Muzeum Archeologiczne mieści się w Pałacu Górków przy ulicy Wodnej, tuż przy Starym Rynku. Jego początki sięgają 1857 roku, gdy przy Towarzystwie Przyjaciół Nauk Poznańskiego powstało Muzeum Starożytności Polskich i Słowiańskich w Wielkim Księstwie Poznańskim, od 1882 roku zwane Muzeum im. Mielżyńskich. W odbudowanym Pałacu Górków muzeum otwarto 8 czerwca 1968 roku.",
        sections=[
            ("Co zobaczyć", [
                "Cztery wystawy stałe: „Pradzieje Wielkopolski” (od początków osadnictwa ludzkiego po kres starożytności, z rekonstrukcjami m.in. szałasu, domów i grobów), „Tu powstała Polska” (archeologiczna podróż do średniowiecza, na której można przymierzyć kopię zbroi późnośredniowiecznej i zagrać w szachy), „Archeologia Sudanu” (zabytki z badań muzeum w Kadero i w rejonie IV katarakty Nilu) oraz „Sztuka naskalna Afryki Północnej” (ryty i malowidła Sahary wschodniej). Od wtorku do niedzieli można je zwiedzać z bezpłatnym audioprzewodnikiem.",
                "Na dziedzińcu stoi trzymetrowy granitowy obelisk Ramzesa II, jedyny faraoński obelisk w Polsce i jeden z niewielu w Europie. Jest wieloletnim depozytem berlińskiego Muzeum Egipskiego i Zbiorów Papirusów.",
            ]),
            ("O pałacu", [
                "Pałac Górków był miejską rezydencją magnacką, w XVI wieku ważnym ośrodkiem ruchu reformacyjnego, a później klasztorem benedyktynek. Po zniszczeniach wojennych pałac odbudowano według jedynego zachowanego rysunku, który przedstawia klasztor (Juliusz Minutoli, 1833), a projekt odbudowy opracował architekt Aleksander Holas, dlatego budynek utracił cechy renesansowej rezydencji magnackiej.",
                "Wojnę przetrwały dziedziniec z arkadowym krużgankiem i renesansowy portal bramy wejściowej z 1548 roku.",
            ]),
            ("Warto wiedzieć", [
                "Muzeum prowadzi też Rezerwat Archeologiczny Genius loci na Ostrowie Tumskim (ul. Ks. I. Posadzego 3), z wystawami stałymi „Pokolenie 966” i „Zabytki Ostrowa Tumskiego”. Na oba miejsca można kupić bilet wspólny.",
                "Nowa wystawa „Radość życia w blasku Ra”, o starożytnym Egipcie, jest wspólnym projektem muzeum i berlińskiego Muzeum Egipskiego i Zbiorów Papirusów. Według muzeum otwarcie planowane jest pod koniec listopada 2026 roku.",
                "Ostatnie wejście jest pół godziny przed zamknięciem. Oprowadzanie z przewodnikiem jest możliwe od wtorku do piątku.",
            ]),
        ],
        address="ul. Wodna 27, 61-781 Poznań",
        hours=[("Poniedziałek", "nieczynne"), ("Wtorek–czwartek", "9:00–16:00 (od 1.09 do 30.06)"), ("Piątek", "10:00–17:00"), ("Sobota", "11:00–18:00"), ("Niedziela", "12:00–16:00"), ("Lipiec–sierpień", "wt–pt 10:00–17:00")],
        tickets=[("Normalny", "20 zł"), ("Ulgowy", "15 zł"), ("Rodzinny (do 6 osób)", "50 zł"), ("Bilet wspólny z rezerwatem Genius loci", "30 zł, ulgowy 25 zł, rodzinny 80 zł"), ("Wtorek", "wstęp wolny")],
        phone="+48 61 852 82 51", www=("muzarp.poznan.pl", "https://nowa.muzarp.poznan.pl/"),
        credit="muzeum-archeologiczne",
        sources=[("Muzeum Archeologiczne: godziny otwarcia", "https://nowa.muzarp.poznan.pl/pl/godziny-otwarcia"),
                 ("Muzeum Archeologiczne: bilety", "https://nowa.muzarp.poznan.pl/pl/bilety"),
                 ("Muzeum Archeologiczne: historia muzeum", "https://nowa.muzarp.poznan.pl/pl/historia-muzeum"),
                 ("Muzeum Archeologiczne: Pałac Górków", "https://nowa.muzarp.poznan.pl/pl/palac-gorkow"),
                 ("Muzeum Archeologiczne: Pradzieje Wielkopolski", "https://nowa.muzarp.poznan.pl/pl/pradzieje-wielkopolski"),
                 ("Muzeum Archeologiczne: Tu powstała Polska", "https://nowa.muzarp.poznan.pl/pl/tu-powstala-polska"),
                 ("Muzeum Archeologiczne: Archeologia Sudanu", "https://nowa.muzarp.poznan.pl/pl/archeologia-sudanu"),
                 ("Muzeum Archeologiczne: Sztuka naskalna Afryki Północnej", "https://nowa.muzarp.poznan.pl/pl/sztuka-naskalna-afryki-polnocnej"),
                 ("Muzeum Archeologiczne: obelisk Ramzesa II", "https://nowa.muzarp.poznan.pl/pl/obelisk-ramzesa-ii"),
                 ("Muzeum Archeologiczne: Radość życia w blasku Ra", "https://nowa.muzarp.poznan.pl/pl/radosc-zycia-w-blasku-ra"),
                 ("Rezerwat Archeologiczny Genius loci: godziny otwarcia i oferta", "http://rezerwat.muzarp.poznan.pl/"),
                 ("Muzeum Archeologiczne: folder o historii muzeum i pałacu (PDF)", "https://nowa.muzarp.poznan.pl/fotki/files/files/Z%20w%C4%99dk%C4%85%20po%20wiedz%C4%99/Folder-muzuem_strony.pdf")],
    ),

    # ─── PRZYRODA ───
    dict(
        slug="jezioro-maltanskie", cat="przyroda", name="Jezioro Maltańskie",
        img="jezioro-malta", img_alt="Jezioro Maltańskie z lotu ptaka: tor regatowy z bojami i brzeg z kładką",
        short="Sztuczne jezioro z torem regatowym, nad którym są też stok, termy, kolejka i lodowisko.",
        badge="Bezpłatnie",
        status=None,
        lead="Jezioro Maltańskie powstało w 1952 roku przez spiętrzenie wód Cybiny. Ma powierzchnię 64 hektarów, a jego tor regatowy ma 2190 m długości i 170–400 m szerokości. Nazwa pochodzi od kawalerów maltańskich, czyli joannitów, którzy mieli tu siedzibę.",
        sections=[
            ("Co zobaczyć", [
                "Tor regatowy, na którym odbywają się regaty kajakarskie i wioślarskie. W 1979 roku zdecydowano o modernizacji jeziora, a w sierpniu 1990 roku zorganizowano na nim XXIII Mistrzostwa Świata w Kajakarstwie. Generalnym projektantem przebudowy był arch. Klemens Mikuła.",
                "W zachodniej części jeziora jest największa w Poznaniu fontanna, ufundowana dla upamiętnienia 750. rocznicy założenia miasta.",
                "Wzdłuż północnego brzegu jeziora biegnie wąskotorowa Kolejka Parkowa Maltanka, a jej stacja końcowa, Zwierzyniec, jest przy wejściu do Nowego Zoo. Na południowym brzegu, na Kopcu Wolności, są całoroczny stok narciarski i letni tor saneczkowy, a u jego stóp pole do nauki gry w golfa i tor do minigolfa. Nad jeziorem jest też kąpielisko, a w sąsiedztwie Termy Maltańskie, wykorzystujące podziemne ciepłe źródła.",
            ]),
            ("Warto wiedzieć", [
                "Latem nad jeziorem odbywają się spektakle Międzynarodowego Festiwalu Teatralnego Malta, a zimą na zachodnim brzegu działa lodowisko.",
            ]),
        ],
        address="Jezioro Maltańskie, 61-131 Poznań",
        hours=[("Teren wokół jeziora", "dostępny całą dobę")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("visitpoznan.pl", "https://visitpoznan.pl/jezioro-maltanskie"),
        credit="jezioro-malta",
        sources=[("POSiR: Historia Malty", "https://posir.poznan.pl/obiekty/malta/historia"),
                 ("Poznan.pl: Jezioro Maltańskie", "https://www.poznan.pl/mim/turystyka/jeziora,poi,2574/-,41237.html"),
                 ("Visit Poznań: Jezioro Maltańskie", "https://visitpoznan.pl/jezioro-maltanskie"),
                 ("Odkryj Wielkopolskę: Malta w Poznaniu", "https://regionwielkopolska.pl/katalog-obiektow/malta-w-poznaniu/")],
        see_also=[("Lodowisko Malta: sezonowe lodowisko", "atrakcje/lodowisko-malta"),
                  ("Malta Ski: stok, tor saneczkowy, kolejka górska", "atrakcje/malta-ski"),
                  ("Termy Maltańskie", "atrakcje/termy-maltanskie"),
                  ("Kolejka Parkowa Maltanka", "atrakcje/kolejka-maltanka")],
    ),
    dict(
        slug="ogrod-botaniczny", cat="przyroda", name="Ogród Botaniczny UAM",
        img="ogrod-botaniczny", img_alt="Pawilon Ekspozycyjno-Dydaktyczny w Ogrodzie Botanicznym UAM, na pierwszym planie kwitnące piwonie",
        short="22 hektary roślin: alpinarium, rosarium i kolekcje piwonii, kosaćców i liliowców.",
        badge="Wstęp wolny",
        status=None,
        lead="Ogród Botaniczny Uniwersytetu im. Adama Mickiewicza założono w 1925 roku (prace nad jego tworzeniem trwały od 1922). Zajmuje około 22 hektarów, a na jego terenie rośnie ponad 6000 taksonów roślin.",
        sections=[
            ("Co zobaczyć", [
                "Alpinarium z roślinami gór od strefy umiarkowanej po subarktyczną, o powierzchni około 6000 m², z blisko 1300 taksonami, urządzone głównie z granitu i wapieni (około 3 tys. ton), z siedmioma zbiornikami wodnymi.",
                "Rosarium z 2950 różami w 29 odmianach oraz kolekcje piwonii (około 120 odmian), kosaćców (około 230) i liliowców (około 280).",
                "Kolekcja roślin rzadkich, zagrożonych wyginięciem i chronionych w Polsce (Dział Roślin Rzadkich i Zagrożonych, pięć kwater).",
                "Kolekcję głazów narzutowych z największym w Poznaniu eratykiem skandynawskim, ważącym blisko 150 ton.",
                "Partery ogrodowe leżą na wspólnej osi z Pawilonem Ekspozycyjno-Dydaktycznym, widocznym na zdjęciu głównym.",
            ]),
        ],
        address="ul. Dąbrowskiego 165, 60-594 Poznań",
        hours=[("Marzec", "9:00–17:00"), ("Kwiecień i wrzesień", "9:00–19:00"), ("Maj–sierpień", "9:00–20:00"), ("Październik", "9:00–18:00"), ("Listopad–luty", "9:00–15:00")],
        tickets=[("Wstęp do ogrodu", "bezpłatnie")],
        phone="+48 61 829 20 13", www=("ogrod.amu.edu.pl", "https://ogrod.amu.edu.pl/"),
        credit="ogrod-botaniczny",
        sources=[("Ogród Botaniczny UAM: godziny otwarcia", "https://ogrod.amu.edu.pl/en/en-godziny-otwarcia/"),
                 ("PIK Poznań: Ogród Botaniczny UAM", "https://pik.poznan.pl/miejsca/ogrod-botaniczny-uniwersytetu-im-adama-mickiewicza-w-poznaniu/"),
                 ("Ogród Botaniczny UAM: kolekcje gruntowe", "https://ogrod.amu.edu.pl/kolekcje-gruntowe/"),
                 ("Ogród Botaniczny UAM: kolekcje szklarniowe", "https://ogrod.amu.edu.pl/kolekcje-szklarniowe/"),
                 ("Ogród Botaniczny UAM: historia i działalność", "https://ogrod.amu.edu.pl/historia-i-dzialalnosc/"),
                 ("Wikipedia: Ogród Botaniczny UAM", "https://pl.wikipedia.org/wiki/Ogród_Botaniczny_Uniwersytetu_im._Adama_Mickiewicza_w_Poznaniu")],
    ),
    dict(
        slug="palmiarnia", cat="przyroda", name="Palmiarnia Poznańska",
        img="palmiarnia-hero", img_alt="Wnętrze Palmiarni Poznańskiej",
        short="Jedna z największych palmiarni w Europie. Obecnie zamknięta z powodu przebudowy.",
        badge="Zamknięte",
        status=("closed", "Palmiarnia jest czasowo zamknięta dla zwiedzających w związku z przebudową obiektu (komunikat z 31.08.2026). Data ponownego otwarcia nie została ogłoszona."),
        lead="Palmiarnia w Parku Wilsona działa od 1911 roku. Ma 4600 m² powierzchni i jest największą palmiarnią w Polsce oraz jedną z największych w Europie.",
        sections=[
            ("O miejscu", [
                "W 12 pawilonach rośnie około 1100 gatunków roślin. W akwariach żyje 170 gatunków ryb.",
                "Palmiarnię zamknięto już raz, w 1978 roku, z powodu złego stanu konstrukcji. Po przebudowie z lat 1983–1992 otwarto ją ponownie w październiku 1992 roku.",
            ]),
            ("Warto wiedzieć", [
                "Park Wilsona, w którym stoi Palmiarnia, jest dostępny normalnie.",
                "O terminie otwarcia palmiarnia poinformuje na swojej stronie internetowej.",
            ]),
        ],
        address="ul. Matejki 18, 60-766 Poznań",
        hours=[("Obecnie", "zamknięte (przebudowa)")],
        tickets=[("Obecnie", "brak zwiedzania")],
        phone=None, www=("palmiarnia.poznan.pl", "https://palmiarnia.poznan.pl/"),
        credit="palmiarnia-hero",
        sources=[("Palmiarnia Poznańska: komunikat o zamknięciu", "https://palmiarnia.poznan.pl/"),
                 ("Wikipedia: Palmiarnia Poznańska", "https://pl.wikipedia.org/wiki/Palmiarnia_Poznańska")],
    ),

    # ─── RODZINA ───
    dict(
        slug="nowe-zoo", cat="rodzina", name="Nowe Zoo",
        img="zoo", img_alt="Słonie w Nowym Zoo w Poznaniu",
        short="120 hektarów lasu, słoniarnia, azyl dla niedźwiedzi i ptaki drapieżne.",
        badge="Codziennie",
        status=None,
        lead="Nowe Zoo otwarto 16 września 1974 roku na Białej Górze nad Maltą. Ma 120 hektarów powierzchni i jest drugim co do wielkości ogrodem zoologicznym w Polsce.",
        sections=[
            ("Co zobaczyć", [
                "Słoniarnię z wybiegiem dla słoni afrykańskich.",
                "Trzyhektarowy azyl dla niedźwiedzi, stworzony razem z niemiecko-austriacką fundacją.",
                "Kolekcję ptaków drapieżnych i sów, jedną z najbogatszych w Europie.",
                "Pawilon nosorożców czarnych i pawilon zwierząt nocnych.",
                "Fort III z lat 1877–1881, fragment dawnej Twierdzy Poznań.",
            ]),
            ("Warto wiedzieć", [
                "W sezonie (w 2026 roku do 27 września) można tu dojechać Kolejką Parkową Maltanka, która kursuje wzdłuż jeziora do stacji Zwierzyniec przy wejściu do zoo.",
                "Biletu nie trzeba drukować, wystarczy kod w telefonie.",
                "Parking jest płatny od 1 kwietnia do 31 października.",
                "Kasy zamykają się godzinę przed zamknięciem zoo.",
            ]),
        ],
        address="ul. Krańcowa 81, 61-070 Poznań",
        hours=[("Marzec i październik", "9:00–17:00"), ("Kwiecień–wrzesień", "9:00–19:00"), ("Listopad–luty", "9:00–16:00")],
        tickets=[("III–X, pn–pt", "45 zł, ulgowy 30 zł, rodzinny 80 zł"), ("III–X, sb–nd i święta", "55 zł, ulgowy 35 zł, rodzinny 115 zł"), ("1 i 3 maja, Boże Ciało, 15 sierpnia", "60 zł, ulgowy 40 zł, rodzinny 130 zł"), ("XI–II", "20 zł, rodzinny 35 zł"), ("Dzieci do 3 lat", "bezpłatnie")],
        phone="+48 61 646 33 44", www=("zoo.poznan.pl", "https://zoo.poznan.pl/informacje-nowe-zoo/"),
        credit="zoo",
        sources=[("Zoo Poznań: ceny biletów", "https://zoo.poznan.pl/ceny-biletow-wstepu-do-ogrodu-zoologicznego/"),
                 ("Zoo Poznań: informacje – Nowe Zoo", "https://zoo.poznan.pl/informacje-nowe-zoo/"),
                 ("Wikipedia: Nowe Zoo w Poznaniu", "https://pl.wikipedia.org/wiki/Nowe_Zoo_w_Poznaniu")],
    ),
    dict(
        slug="stare-zoo", cat="rodzina", name="Stare Zoo",
        img="stare-zoo", img_alt="Grota w Starym Zoo w Poznaniu",
        short="Jedno z najstarszych zoo w Polsce, dziś bezpłatny park blisko dworca.",
        badge="Wstęp wolny",
        status=None,
        lead="Stare Zoo powstało w 1871 roku i jest drugim najstarszym ogrodem zoologicznym w Polsce. Od 2009 roku działa jako bezpłatny park z mniejszymi zwierzętami.",
        sections=[
            ("Co zobaczyć", [
                "Pawilon Zwierząt Zmiennocieplnych z 2012 roku z gadami, płazami i rybami, w tym waranami z Komodo.",
                "Zabytkową grotę z 1906 roku, pawilon naczelnych z 1927 roku i woliery dla ptaków brodzących.",
                "Muzeum Historii Zoo w dawnej lwiarni, otwarte w 2022 roku, również bezpłatne.",
            ]),
            ("Warto wiedzieć", [
                "Zoo zajmuje 5,24 hektara na Jeżycach, niedaleko dworca Poznań Główny. To dobre miejsce na krótki spacer z dziećmi.",
            ]),
        ],
        address="ul. Zwierzyniecka 19, 60-814 Poznań",
        hours=[("Marzec i październik", "9:00–17:00"), ("Kwiecień–wrzesień", "9:00–19:00"), ("Listopad–luty", "9:00–16:00")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone="+48 61 848 08 47", www=("zoo.poznan.pl", "https://zoo.poznan.pl/informacje-stare-zoo/"),
        credit="stare-zoo",
        sources=[("Zoo Poznań: informacje – Stare Zoo", "https://zoo.poznan.pl/informacje-stare-zoo/"),
                 ("Wikipedia: Stare Zoo w Poznaniu", "https://pl.wikipedia.org/wiki/Stare_Zoo_w_Poznaniu")],
    ),
    dict(
        slug="kolejka-maltanka", cat="rodzina", name="Kolejka Parkowa Maltanka",
        img="kolejka-maltanka", img_alt="Parowóz Kolejki Parkowej Maltanka przy stacji Maltanka, w tle wieże Archikatedry Poznańskiej",
        short="Wąskotorowa kolejka wzdłuż Malty do Nowego Zoo. Kursuje sezonowo.",
        badge="Sezonowo",
        status=("closed", "Sezon 2026 zakończył się 27 września, więc kolejka teraz nie kursuje. Rusza ponownie wiosną (w 2026 roku pierwszy kurs odbył się 12 kwietnia). Terminy sezonu 2027 poda MPK Poznań."),
        lead="Maltanka to wąskotorowa kolejka parkowa prowadzona przez MPK Poznań. Kursuje wzdłuż Jeziora Maltańskiego między stacjami Maltanka i Zwierzyniec, przy wejściu do Nowego Zoo.",
        sections=[
            ("Warto wiedzieć", [
                "Sezon 2026 trwał od 12 kwietnia do 27 września, a od 24 kwietnia kolejka kursowała codziennie.",
                "Od 1 maja 2026 można kupić bilet tam i z powrotem. Bilety sprzedają obie stacje końcowe.",
                "Trasa ma niespełna 4 km. Stacje to Maltanka, Ptyś (w okolicy Term Maltańskich), Balbinka (mijanka dwóch pociągów) i Zwierzyniec.",
            ]),
        ],
        address="Kolejka Parkowa Maltanka, ul. Jana Pawła II 1, 61-131 Poznań",
        hours=[("W sezonie, dni robocze", "co godzinę, 9:30–18:30"), ("W sezonie, weekendy i święta", "co 30 minut, 10:00–19:00"), ("Poza sezonem (od 28.09.2026)", "kolejka nie kursuje")],
        tickets=[("W jedną stronę", "18 zł, ulgowy (do 16 lat) 12 zł, rodzinny 48 zł"), ("Tam i z powrotem", "24 zł, ulgowy 16 zł, rodzinny 64 zł"),
                 ("Bilet rodzinny", "do 5 osób, w tym najwyżej 2 powyżej 16 lat"),
                 ("Bilet wycieczkowy", "10 zł w jedną stronę, 13 zł tam i z powrotem (zorganizowana grupa dzieci i młodzieży do 16 lat, minimum 10 osób)")],
        phone="+48 618 396 690", www=("mpk.poznan.pl", "https://www.mpk.poznan.pl/strefa-pasazera/turystyka/maltanka/"),
        credit="kolejka-maltanka",
        sources=[("MPK Poznań: Kolejka Parkowa Maltanka", "https://www.mpk.poznan.pl/strefa-pasazera/turystyka/maltanka/"),
                 ("MPK Poznań: bilety na Maltankę 2026", "https://www.mpk.poznan.pl/nowy-rodzaj-biletow-na-maltanke-w-sezonie-2026/"),
                 ("MPK Poznań: start sezonu 2026", "https://www.mpk.poznan.pl/kolejka-parkowa-maltanka-rozpoczyna-sezon-pierwszy-kurs-w-niedziele-12-kwietnia-2026/")],
    ),
    dict(
        slug="termy-maltanskie", cat="rodzina", name="Termy Maltańskie",
        img="termy-maltanskie", img_alt="Zewnętrzny basen ze zjeżdżalniami i hala Term Maltańskich, widok z góry, nad Wartą",
        short="Aquapark z 13 zjeżdżalniami, baseny sportowe i Sauny & Wellness nad Jeziorem Maltańskim, czynne do 23:00.",
        badge="Codziennie",
        status=None,
        lead="Termy Maltańskie to kompleks sportowo-rekreacyjny nad Jeziorem Maltańskim. Woda w basenach pochodzi z odwiertu geotermalnego o głębokości 1306 metrów. Kompleks ma aquapark, baseny sportowe i strefę Sauny & Wellness.",
        sections=[
            ("Co zobaczyć", [
                "Aquapark: 13 zjeżdżalni, m.in. Kamikadze, Turbo (zjazd ok. 60 km/h), Pontonowa, Dzika Rzeka, Rodzinna, Wielotorowa, Multimedialna i klasyczne, oraz Wulkan, który góruje nad strefą. Baseny mają wodę o temperaturze 30–36 °C, a plaża zewnętrzna ma nadmorski złoty piasek.",
                "Ok. 10 basenów, m.in. falowy (200 cm), wypływowe, Złote Kaskady, brodzik, wodny plac zabaw, geotermalny i sezonowe baseny zewnętrzne. Dwa całoroczne baseny mają widok na jezioro.",
                "Baseny sportowe: olimpijski o długości 50 m i głębokości 2 m, który pomostem można podzielić na dwa baseny 25-metrowe, z trybunami dla prawie 4000 osób; basen do skoków o głębokości 5 m z wieżą do skoków o wysokościach 3, 5, 7,5 i 10 m.",
                "Sauny & Wellness: trzy światy (Równowagi na poziomie 0, Zmysłów i Żywiołów na poziomie -1). Sauny suche, m.in. Ziołowa, Event, Infrared; łaźnie parowe, m.in. Turecka, Kwiatowa, Indyjska; sauny zewnętrzne fińskie Panorama i KELO; Tężnia Solna i Grota Śnieżna. Miejsca do masażu (stół do ceremonii Hammam, gabinety, apartament). Zielony Taras z kameralnymi miejscami, osobnym barem i basenem, oraz 2 klimatyczne bary. Strefa tylko dla osób od 18. roku życia.",
            ]),
            ("Warto wiedzieć", [
                "Kompleks jest zamknięty w Wielką Sobotę i Niedzielę Wielkanocną, 1 listopada, 24 i 25 grudnia oraz 31 grudnia.",
                "Bilet do aquaparku obejmuje też baseny sportowe, a bilet do Sauny & Wellness obejmuje aquapark i baseny sportowe. Sauny & Wellness są tylko dla osób pełnoletnich.",
                "Przekroczenie czasu kosztuje 1 zł za minutę (60 zł za godzinę), a po 23:00 stawka wynosi 5 zł za minutę.",
                "Bilety Karty Dużej Rodziny (rodzinny i indywidualny) są w kasach, ale honorowana jest tylko karta z kodem terytorialnym Poznania (pierwsze siedem cyfr numeru: 3064011). Okaż ją razem z dowodem tożsamości, także dla dzieci. Rabat nie łączy się z promocjami.",
                "Grupy zorganizowane od 15 osób (plus opiekun) kupują bilety grupowe tylko do aquaparku, po zgłoszeniu grupy na bok@termymaltanskie.com.pl. Seniorzy mają tańsze bilety w dni powszednie przed południem (aquapark 9:00–12:00, baseny sportowe 8:00–12:00, sauny 14:30–17:30).",
                "Wejście dla osób z niepełnosprawnością, także na wózkach, znajduje się na parterze, przez dolny hol.",
                "W Strefie Saun można wypożyczyć prześcieradła (10 zł) i szlafroki (15 zł), a ręczniki kupić za 20 zł. Pokój Opiekuna z Dzieckiem, za recepcją Strefy Saun, ma przewijak, kojec i toaletę.",
            ]),
        ],
        address="ul. Termalna 1, 61-028 Poznań",
        hours=[("Aquapark", "codziennie 9:00–23:00"), ("Baseny sportowe", "pn–sb 6:00–23:00, nd i święta 7:00–23:00"), ("Sauny & Wellness", "pn–pt 14:30–23:00, sb–nd 11:30–23:00")],
        tickets=[("Aquapark, normalny (1 / 2 / 3 godz. / cały dzień)", "46 zł / 61 zł / 75 zł / 109 zł"), ("Aquapark, ulgowy", "37 zł / 52 zł / 65 zł / 94 zł"),
                 ("Aquapark, rodzinny (2 dorosłych + 1 dziecko lub 1 + 2)", "93 zł / 123 zł / 152 zł / 219 zł, kolejne dziecko +13 zł / 20 zł / 28 zł / 36 zł"),
                 ("Sauny & Wellness, normalny (1 / 2 / 3 godz. / cały dzień)", "67 zł / 81 zł / 95 zł / 145 zł"), ("Sauny & Wellness, ulgowy", "57 zł / 71 zł / 83 zł / 119 zł"),
                 ("Baseny sportowe, normalny (1 / 2 godz.)", "20 zł / 29 zł"), ("Baseny sportowe, ulgowy", "18 zł / 24 zł"),
                 ("Dzieci do 3 lat", "bezpłatnie")],
        phone="+48 459 595 590", www=("termymaltanskie.com.pl", "https://termymaltanskie.com.pl/"),
        credit="termy-maltanskie",
        sources=[("Termy Maltańskie: cenniki", "https://termymaltanskie.com.pl/cenniki/"), ("Termy Maltańskie: FAQ", "https://termymaltanskie.com.pl/faq/"), ("Termy Maltańskie: aquapark", "https://termymaltanskie.com.pl/aquapark/"), ("Termy Maltańskie: baseny sportowe", "https://termymaltanskie.com.pl/baseny-sportowe/"), ("Termy Maltańskie: sauny", "https://termymaltanskie.com.pl/sauny/")],
    ),
    dict(
        slug="malta-ski", cat="rodzina", name="Malta Ski",
        img="malta-ski", img_alt="Stok Malta Ski zimą",
        short="Sztuczny stok, letni tor saneczkowy i kolejka górska nad jeziorem.",
        badge="Zależnie od pogody",
        status=None,
        lead="Malta Ski to całoroczny ośrodek nad Jeziorem Maltańskim. Zimą działa sztuczny stok narciarski, a latem letni tor saneczkowy i inne atrakcje.",
        sections=[
            ("Co tu jest", [
                "Sztuczny stok narciarski o długości około 150 metrów.",
                "Letni tor saneczkowy o długości 560 metrów.",
                "Całoroczną kolejkę górską Adrenaline, minigolf i plac zabaw.",
            ]),
            ("Warto wiedzieć", [
                "Godziny otwarcia zależą od pogody i zmieniają się w ciągu roku. Aktualne godziny i cennik podaje strona maltaski.pl.",
                "Kolejka górska i tor saneczkowy są partnerami Poznańskiej Karty Turystycznej.",
            ]),
        ],
        address="ul. Wiankowa 2, 61-131 Poznań",
        hours=[("Godziny", "zależne od pogody, na maltaski.pl"), ("Sezony wg maltaski.pl", "zimowy 17.10–31.03, letni 1.04–31.10")],
        tickets=[("Cennik", "na maltaski.pl")],
        phone=None, www=("maltaski.pl", "https://maltaski.pl/"),
        credit="malta-ski",
        sources=[("Visit Poznań: Malta Ski", "https://visitpoznan.pl/centrum-sportowo-rekreacyjne-malta-ski"),
                 ("Malta Ski", "https://maltaski.pl/")],
        see_also=[("Lodowisko Malta: sezonowe lodowisko", "atrakcje/lodowisko-malta"),
                  ("Jezioro Maltańskie", "atrakcje/jezioro-maltanskie"),
                  ("Termy Maltańskie", "atrakcje/termy-maltanskie")],
    ),

    # ─── WSPÓŁCZESNY ───
    dict(
        slug="stary-browar", cat="wspolczesny", name="Stary Browar",
        img="stary-browar", img_alt="Ceglany gmach Starego Browaru od strony ulic Półwiejskiej i Kościuszki", og_pos="center top",
        short="XIX-wieczny browar Huggerów przebudowany na centrum handlu i sztuki, z rzeźbami Mitoraja i nagradzaną architekturą.",
        badge="Bezpłatnie",
        status=None,
        lead="Stary Browar to nie tylko centrum handlowe. To XIX-wieczny ceglany browar Huggerów, zamieniony w 2003 roku w centrum handlu i sztuki według idei „50 50”: połowa to biznes, połowa to sztuka. Po korytarzach i dziedzińcach można chodzić jak po galerii z rzeźbami i instalacjami znanych artystów, a wstęp jest bezpłatny.",
        sections=[
            ("Historia", [
                "Ambrosius Hugger, piwowar ze Schwarzwaldu, otworzył pierwszy browar w Poznaniu w 1844 roku przy ulicy Wronieckiej. Jego synowie Julius i Alfons w 1876 roku kupili posesję na rogu Półwiejskiej i zbudowali tu Browary Huggerów. W 1918 roku zakład warzył prawie 72 tysiące hektolitrów piwa rocznie.",
                "W czasie walk o Poznań w 1945 roku browar został mocno zniszczony. Po wojnie go upaństwowiono, a w 1980 roku zamknięto. Budynki niszczały, a do 1997 roku działała w nich tylko mała wytwórnia wód gazowanych.",
                "W 1998 roku teren kupiła spółka Grażyny Kulczyk. Zanim ruszyła budowa, w ruinach wystawiano spektakle, w tym „Makbeta” Verdiego transmitowanego na żywo w TVP2. Pierwszą część centrum, Atrium, otwarto 5 listopada 2003 roku, Dziedziniec Sztuki 29 kwietnia 2004 roku, a drugie skrzydło, Pasaż, 11 marca 2007 roku. Od 2015 roku właścicielem centrum jest fundusz Deutsche Asset & Wealth Management (dziś Deutsche Asset Management), a opisane niżej rzeźby i instalacje nadal można tu oglądać.",
            ]),
            ("Architektura", [
                "Najstarsze budynki, czyli Warzelnia, Słodownia i Suszarnia z charakterystycznym kominem, powstały około 1890 roku. Zbudowano je w stylu arkadowym (Rundbogenstil), typowym dla ówczesnych fabryk: z czerwonej cegły licówki, z półkoliście zamkniętymi oknami i ceglanymi ozdobami.",
                "Przebudowę zaprojektowało poznańskie Studio ADS, założone przez Piotra Berełkowskiego, czterokrotnego laureata nagrody im. Jana Baptysty Quadro. Stare mury połączono z nowoczesnymi konstrukcjami ze stali i szkła.",
                "Stary Browar znalazł się wśród 20 budynków wybranych na wystawę „Polska. Ikony architektury”, pokazującą najważniejszą polską architekturę po 1989 roku. Międzynarodowa Rada Centrów Handlowych (ICSC) uznała go za najlepsze centrum handlowe na świecie w 2005 roku, a w 2008 roku ponownie za najlepsze centrum handlowe.",
                "Po zmroku warto obejrzeć zachodnią fasadę Pasażu. To wspólne dzieło Studia ADS i artysty Adama Garnka: szklaną bryłę dzielą poziome pasy, a instalacja świetlna w środku zamienia ją w migoczącą, półprzezroczystą ozdobę.",
            ]),
            ("Dzieła sztuki do zobaczenia", [
                "„Thsuki-no-hikari” (Blask Księżyca) Igora Mitoraja w Atrium: monumentalny fragment ludzkiej twarzy wzorowany na rzeźbie antycznej. Poznaniacy mówią na nią „Maska” albo po prostu „Mitoraj” i to jedno z najpopularniejszych miejsc spotkań w mieście.",
                "„Eros alato” (Eros skrzydlaty) i „Torso del lago” (Tors nad jeziorem), dwie mniejsze prace Mitoraja zawieszone na ceglanych ścianach. Pęknięcia i rysy na idealnych, klasycznych ciałach mówią o przemijaniu.",
                "„Opertus Lunula Umbra” (Ukryty Cień Księżyca) koreańskiego artysty U-Rama Choe: kinetyczna rzeźba zawieszona nad Szachownicą. O określonych godzinach porusza się jak oddychające zwierzę, dlatego poznaniacy nazywają ją „Krewetką”.",
                "„Konflikt między dobrem a złem” Piotra Kurki: czarno-biała marmurowa ławka, na której można usiąść. Na białej części siedzi kruk. Według lokalnej legendy kto go pogłaszcze, łatwiej rozwiąże życiowe problemy.",
                "„Citta Gentile” (Wrażliwe Miasto) Alessandra Mendiniego, słynnego włoskiego designera: rzeźby w kształcie liter wymyślonego przez niego alfabetu, przygotowane specjalnie dla Starego Browaru.",
                "„Henyo-Penyo Myomyonmyo” japońskiego artysty Mr., ucznia Takashiego Murakamiego. Bywalcy nazywają tę postać chłopca w dżinsach „Heńkiem”. Rzeźba należy do cyklu nawiązującego do ataku na Hiroszimę.",
                "Instalacja Leona Tarasewicza: zielono-żółte pasy, które w 2003 roku, na 750-lecie Poznania, zdobiły kolumny Teatru Wielkiego. Dziś są w Atrium, na jednej z najbardziej ruchliwych tras w budynku.",
                "Kufel z brązu Wojciecha Kujawskiego, ozdobiony sześcioma postaciami, odsłonięty w 2007 roku na otwarcie Pasażu. Przy odsłonięciu ustanowiono dwa rekordy Guinnessa: największego kufla do piwa na świecie i największej ilości piwa wypitej z jednego naczynia.",
            ]),
            ("Wystawy i zwiedzanie", [
                "Na Dziedzińcu działa Pop Culture Gallery, prowadzona przez Stary Browar. Pokazuje wystawy łączące modę, sztukę, design i technologię. Były tu już m.in. wystawy Andy'ego Warhola, Björk, Davida LaChapelle'a, Gianniego Versace i Ryszarda Kai. Aktualną wystawę sprawdzisz na stronie centrum.",
                "Stary Browar organizuje zwiedzanie z przewodnikiem po architekturze, historii i kolekcji dzieł sztuki. Termin trzeba uzgodnić z punktem informacyjnym co najmniej dwa tygodnie wcześniej (informacja@starybrowar.com, tel. 61 859 60 50).",
                "W kompleksie działa hotel Blow Up Hall (wejście od ul. Kościuszki 42). W hotelu, restauracji arte i pasażu są rzeźby, instalacje i sztuka użytkowa z kolekcji właścicieli, tworzona we współpracy z polskimi artystami. Według strony hotelu restauracja arte jest czynna codziennie 12:00–22:00, a b.bar 16:00–24:00 (rezerwacja stolika: tel. 61 629 94 02).",
                "Przy centrum jest zabytkowy park, dobre miejsce na odpoczynek po zwiedzaniu.",
            ]),
            ("Warto wiedzieć", [
                "W centrum jest blisko 200 sklepów, kilkadziesiąt restauracji i kawiarni, 8 sal kinowych i klub muzyczny.",
                "Parking ma 1000 miejsc w obu skrzydłach (Atrium: poziomy +3, +4 i +5, Pasaż: poziomy −1, −2 i −3), a wjazd jest od ulicy Kościuszki. Jest płatny, ale paragony za co najmniej 90 zł dają 4 godziny parkowania bezpłatnie (walidacja w Punktach Informacyjnych, tylko w dniu zakupów).",
                "Punkt Informacyjny w Pasażu: tel. 61 667 14 00, poniedziałek–sobota 10:00–21:00, niedziela 10:00–20:00. Strona „O centrum” podaje przy Pasażu numer 61 677 14 00, ale „Kontakt” i strona Pop Culture Gallery 61 667 14 00.",
            ]),
        ],
        address="ul. Półwiejska 42, 61-888 Poznań",
        hours=[("Poniedziałek–sobota", "9:00–21:00"), ("Niedziele handlowe", "10:00–20:00"), ("Pozostałe niedziele", "czynne tylko wybrane lokale"), ("Pop Culture Gallery", "12:00–20:00"), ("Food Hall", "poniedziałek–sobota 12:00–22:00, niedziele handlowe 12:00–20:00"), ("Carrefour Market", "poniedziałek–sobota 8:00–22:00, niedziele handlowe 9:30–20:30")],
        tickets=[("Wstęp i oglądanie dzieł sztuki", "bezpłatnie"), ("Wystawy w Pop Culture Gallery", "zależnie od wystawy")],
        phone="+48 61 859 60 50", www=("starybrowar5050.com", "https://starybrowar5050.com/o-centrum/"),
        credit="stary-browar",
        sources=[("Stary Browar: o centrum, historia i dzieła sztuki", "https://starybrowar5050.com/o-centrum/"),
                 ("Stary Browar: kontakt, godziny otwarcia i parking", "https://starybrowar5050.com/kontakt/"),
                 ("Wiadomości Handlowe: Stary Browar zmienia właściciela (30.11.2015)", "https://www.wiadomoscihandlowe.pl/handel-i-dystrybucja/handel-hurtowy-i-grupy-zakupowe/stary-browar-zmienia-wlasciciela-2431468"),
                 ("Stary Browar: Pop Culture Gallery", "https://starybrowar5050.com/sklepy/pop-culture-gallery-stary-browar/"),
                 ("Poznański Prestiż: wywiad z zarządem Starego Browaru (2023)", "https://poznanskiprestiz.pl/pp-x-stary-browar/stary-browar-od-20-lat-w-sercu-poznania/"),
                 ("Hotel Blow Up Hall: sztuka i książki", "https://blowuphall.com/sztuka-i-ksiazki/"),
                 ("Hotel Blow Up Hall: restauracja", "https://blowuphall.com/restauracja/"),
                 ("poznan.pl: Stary Browar", "https://www.poznan.pl/mim/turystyka/inne-atrakcje,poi,3391/stary-browar,46255.html")],
    ),
    dict(
        slug="srodka", cat="wspolczesny", name="Śródka i mural 3D",
        img="srodka", img_alt="Trójwymiarowy mural na Śródce: kamienice z trębaczem na dachu i kotem w tle", og_pos="center 15%",
        short="Trójwymiarowy mural z trębaczem na dachu i kotem w tle, na rogu ulic Śródka i Rynek Śródecki.",
        badge="Bezpłatnie",
        status=None,
        lead="Śródka to historyczna dzielnica Poznania. Jej najbardziej znany punkt to trójwymiarowy mural „Opowieść śródecka z trębaczem na dachu i kotem w tle”, na ścianie kamienicy na rogu ulic Śródka i Rynek Śródecki.",
        sections=[
            ("O muralu", [
                "Mural wykonano w technice 3D i odsłonięto 1 października 2015 roku. Pomysł zgłosił Gerard Cofta, lokalny społecznik i członek Rady Osiedla, zainspirowany fotografią z lat 20. XX wieku. Szkic przygotował prof. Radosław Barek, architekt rysownik.",
                "Realizacji podjęła się Fundacja Artystyczno-Edukacyjna PUENTA, w ramach projektu „W środku Śródki 2015”, dofinansowanego przez Miasto Poznań w konkursie „Centrum Warte Poznania”. Farby ufundowała firma Budchem.",
            ]),
            ("Co przedstawia", [
                "Mural opowiada historię dzielnicy i jest wspomnieniem dawnego życia małego miasteczka, w którym mieszkało i pracowało wielu rzemieślników i kupców.",
                "Mały zielony domek, w którego drzwiach stoi rzeźnik, nawiązuje do dawnej zabudowy i działającej tu kiedyś jatki rzeźniczej. Hejnalista na dachu przypomina nieistniejący już ratusz śródecki, z którego trębacz grał hejnał. Na jednej ze ścian jest jeździec na koniu z białym orłem na tarczy: Władysław Odonic, książę wielkopolski, który w 1231 roku nadał Śródce prawa miejskie. Kot skradający się po kalenicy najwyższego dachu jest dla mieszkańców symbolem tego miejsca.",
            ]),
        ],
        address="róg ul. Śródka i Rynku Śródeckiego, 61-125 Poznań",
        hours=[("Mural", "widoczny całą dobę")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", "https://www.poznan.pl/mim/info/news/trojwymiarowy-mural-na-srodce,85708.html"),
        credit="srodka",
        sources=[("poznan.pl: Trójwymiarowy mural na Śródce", "https://www.poznan.pl/mim/info/news/trojwymiarowy-mural-na-srodce,85708.html"),
                 ("poznan.pl: Mural „Opowieść śródecka z trębaczem na dachu i kotem w tle”", "https://www.poznan.pl/mim/s8a/-,p,1025,5634,31659.html")],
    ),
]

# Atrakcje dodane 28.09.2026 (druga tura). Po scaleniu lista jest sortowana według kategorii.
MORE = [
    dict(
        slug="pomnik-czerwca-1956", cat="pomniki", name="Pomnik Poznańskiego Czerwca 1956",
        img="pomnik-czerwca-1956", img_alt="Dwa połączone krzyże Pomnika Poznańskiego Czerwca 1956",
        short="Poznańskie Krzyże upamiętniające Poznański Czerwiec 1956.",
        badge="Bezpłatnie",
        status=None,
        lead="Pomnik na placu Adama Mickiewicza, nazywany Poznańskimi Krzyżami, upamiętnia bunt robotników z 28 czerwca 1956 roku.",
        sections=[
            ("O pomniku", [
                "28 czerwca 1956 roku robotnicy Zakładów im. Stalina, dziś Zakładów Cegielskiego, podjęli strajk generalny i zorganizowali demonstrację, krwawo stłumioną przez milicję i wojsko. Według badań IPN zginęło co najmniej 58 osób, a kilkaset zostało rannych.",
                "Postulat budowy pomnika zgłosił 10 października 1980 roku Roman Schefke z Akademii Rolniczej w Poznaniu na zebraniu delegatów NSZZ „Solidarność” Regionu Wielkopolska. 6 listopada 1980 roku powstał Społeczny Komitet Budowy Pomnika Poznańskiego Czerwca 1956, któremu przewodniczył Roman Brandstaetter.",
                "Konkurs na projekt rozstrzygnięto 28 stycznia 1981 roku, a wpłynęły do niego 67 prace. Komitet nie zaakceptował zwycięskiego projektu „Kierunek”, a jego autorzy wycofali go 5 lutego 1981 roku. Wybrano projekt „Jedność” rzeźbiarza Adama Graczyka i architekta Włodzimierza Wojciechowskiego.",
                "Pomnik stanął na placu Adama Mickiewicza, obok pomnika wieszcza, w miejscu, gdzie wcześniej stał Pomnik Wdzięczności. Pierwotnie planowano kamień, ale ze względu na krótki termin użyto platerowanej blachy nierdzewnej z Huty Batory w Chorzowie. Budowę w znacznym stopniu wykonali, w większości społecznie i po godzinach pracy, pracownicy Zakładów im. H. Cegielskiego, a także ZNTK i Pometu.",
                "23 maja 1981 roku wmurowano w podstawę akt erekcyjny. Pomnik odsłonięto 28 czerwca 1981 roku. Dokonał tego Stanisław Matyja, uważany za nieformalnego przywódcę buntu z 1956 roku. Na odsłonięcie przyszło szacunkowo 200 tysięcy osób, wśród nich Lech Wałęsa i Anna Walentynowicz, a odczytano telegram od Jana Pawła II.",
                "Po wprowadzeniu stanu wojennego 13 grudnia 1981 roku pomnik stał się symbolem walki o wolność. Po pacyfikacji kopalni „Wujek” domalowano na nim datę 1981, którą dziesięć lat później, podczas renowacji, umieszczono na stałe.",
            ]),
            ("Symbolika", [
                "Na pomniku widnieje hasło niesione przez demonstrantów na transparentach: „O wolność, prawo i chleb”. Dopisek „o Boga” dodano dopiero w 2005 roku.",
                "Według Marii Skrzypczak z Muzeum Powstania Poznańskiego – Czerwiec 1956 dwa krzyże, z których jeden jest wysunięty do przodu, przedstawiają marsz robotników w pochodzie, a wspólna belka oznacza jedność robotniczą. Więzy łączące krzyże symbolizują ucisk władzy socjalistycznej, a mniejszy element, orzeł, godło i Polskę budzącą się ku wolności.",
            ]),
            ("Warto wiedzieć", [
                "W Zamku Cesarskim działa Muzeum Powstania Poznańskiego – Czerwiec 1956.",
            ]),
        ],
        address="pl. Adama Mickiewicza, 61-712 Poznań",
        hours=[("Pomnik", "dostępny całą dobę")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", "https://www.poznan.pl/mim/wortals/czerwiec56/-,p,58421,58426.html"),
        credit="pomnik-czerwca-1956",
        sources=[("Poznan.pl: Poznański Czerwiec 1956, pomnik", "https://www.poznan.pl/mim/wortals/czerwiec56/-,p,58421,58426.html"),
                 ("Visit Poznań: Muzeum Powstania Poznańskiego – Czerwiec 1956", "https://visitpoznan.pl/muzeum-powstania-poznanskiego-czerwiec-1956"),
                 ("Dzieje.pl (PAP): Pomnik Poznańskiego Czerwca 1956 – miejsce pamięci i symbol Poznania", "https://dzieje.pl/aktualnosci/pomnik-poznanskiego-czerwca-1956-miejsce-pamieci-i-symbol-poznania")],
    ),
    dict(
        slug="genius-loci", cat="zabytki", name="Rezerwat Archeologiczny Genius Loci",
        img="genius-loci", img_alt="Drewniana makieta z kłód i kamieni w ekspozycji Rezerwatu Archeologicznego Genius Loci, obok szklane schody",
        short="Oryginalny wał obronny grodu z X wieku na Ostrowie Tumskim.",
        badge="Nd wstęp wolny",
        status=None,
        lead="Rezerwat Genius Loci na Ostrowie Tumskim pokazuje doskonale zachowane konstrukcje wału obronnego grodu poznańskiego z X wieku. Prowadzi go Muzeum Archeologiczne, a otwarto go w 2012 roku.",
        sections=[
            ("Co zobaczyć", [
                "Drewniane konstrukcje wału obronnego grodu z czasów pierwszych Piastów, zachowane w ziemi przez ponad tysiąc lat.",
                "Wystawy i prezentacje multimedialne, które pokazują, jak budowano umocnienia we wczesnym średniowieczu.",
            ]),
            ("Warto wiedzieć", [
                "Dojazd (według rozkładu ZTM z 10.10.2026): przystanek Katedra obsługują autobusy 167, 213, 223 i 911 oraz linia T7, a tramwaje 5, 6, 7 i 8 zatrzymują się na Rondzie Śródka. Strona rezerwatu podaje starsze numery linii, które nie zgadzają się z obecnym rozkładem.",
                "Obiekt jest przystosowany dla osób z niepełnosprawnościami.",
                "Jest bilet na trzy miejsca na Ostrowie Tumskim (Brama Poznania, Genius Loci i Akademia Lubrańskiego) w cenie 49 zł.",
                "Ostatnie wejście jest pół godziny przed zamknięciem.",
            ]),
        ],
        address="ul. Ks. I. Posadzego 3, 61-108 Poznań",
        hours=[("Poniedziałek", "nieczynne"), ("Wtorek–czwartek", "10:00–16:00"), ("Piątek–sobota", "10:00–18:00"), ("Niedziela", "10:00–15:00")],
        tickets=[("Normalny", "20 zł"), ("Ulgowy", "15 zł"), ("Rodzinny (2 dorosłych + 4 dzieci)", "50 zł"), ("Niedziela", "wstęp wolny na ekspozycje"),
                 ("Wspólny z Pałacem Górków (Muzeum Archeologiczne)", "30 zł, ulgowy 25 zł, rodzinny 80 zł")],
        phone="+48 61 852 21 67", www=("rezerwat.muzarp.poznan.pl", "https://rezerwat.muzarp.poznan.pl/"),
        credit="genius-loci",
        sources=[("Genius Loci: bilety", "https://rezerwat.muzarp.poznan.pl/pl/bilety"),
                 ("dzieje.pl: Rezerwat archeologiczny na Ostrowie Tumskim (otwarcie, 29.06.2012)", "https://dzieje.pl/rozmaitosci/rezerwat-archeologiczny-na-ostrowie-tumskim-w-poznaniu"),
                 ("Genius Loci: godziny otwarcia", "https://rezerwat.muzarp.poznan.pl/pl/godziny-otwarcia"),
                 ("Genius Loci: dla zwiedzających", "https://rezerwat.muzarp.poznan.pl/pl/dla-zwiedzajacych")],
    ),
    dict(
        slug="wzgorze-sw-wojciecha", cat="zabytki", name="Wzgórze św. Wojciecha",
        img="wzgorze-sw-wojciecha", img_alt="Kościół św. Wojciecha w Poznaniu z drewnianą dzwonnicą", og_pos="center top",
        short="Krypta Zasłużonych Wielkopolan: grób Józefa Wybickiego i serce gen. Dąbrowskiego.",
        badge="Po umówieniu",
        status=None,
        lead="Przy kościele św. Wojciecha znajduje się Krypta Zasłużonych Wielkopolan, założona w 1923 roku z inicjatywy proboszcza ks. Bogusława Kościelskiego. Wzorowano ją na krakowskiej Skałce.",
        sections=[
            ("Kto tu spoczywa", [
                "Józef Wybicki, autor słów „Mazurka Dąbrowskiego”, oraz Antoni Kosiński, współtwórca Legionów Dąbrowskiego.",
                "Heliodor Święcicki, założyciel i pierwszy rektor Uniwersytetu Poznańskiego.",
                "Kompozytorzy Feliks Nowowiejski, twórca melodii „Roty”, i Tadeusz Szeligowski.",
                "W krypcie spoczywają też m.in. płk Andrzej Niegolewski, uczestnik szarży pod Somosierrą, i podróżnik Paweł Edmund Strzelecki.",
                "W krypcie stoją ponadto dwie urny: z sercem gen. Jana Henryka Dąbrowskiego i z ziemią z miejsca pochówku gen. Ignacego Prądzyńskiego. W nawie południowej kościoła spoczywa Karol Marcinkowski, lekarz i społecznik.",
            ]),
            ("Kościół i dzwonnica", [
                "Kościół św. Wojciecha po raz pierwszy wymieniono w 1244 roku, a z dokumentów wynika pośrednio, że wzniesiono go już w 1222. Obecna gotycka świątynia pochodzi z XV wieku, nawy boczne dobudowano w pierwszej połowie XVI wieku, a późnorenesansowe szczyty sto lat później.",
                "Wnętrze zdobi polichromia Antoniego Procajłowicza z początku XX wieku. W 1945 roku kościół poważnie ucierpiał podczas walk o Cytadelę i został odbudowany w latach 1946–1949.",
                "Przed kościołem stoi drewniana dzwonnica kryta gontem, z przełomu XVI i XVII wieku. To najstarszy drewniany zabytek w mieście.",
            ]),
            ("Warto wiedzieć", [
                "W 1997 roku otwarto nową część krypty przy nawie południowej kościoła.",
                "Kryptę zwiedza się tylko po wcześniejszym umówieniu telefonicznym z parafią. W czasie mszy i uroczystości jest nieczynna.",
            ]),
        ],
        address="ul. Święty Wojciech 1, 61-746 Poznań",
        hours=[("Krypta", "po uzgodnieniu telefonicznym"), ("W czasie mszy", "nieczynna")],
        tickets=[("Zwiedzanie", "po uzgodnieniu z parafią")],
        phone="+48 793 842 860", www=("kultura.poznan.pl", "https://kultura.poznan.pl/mim/kultura/muzea-w-poznaniu,poi,202,12/krypta-zasluzonych-wielkopolan,35331.html"),
        credit="wzgorze-sw-wojciecha",
        sources=[("kultura.poznan.pl: Krypta Zasłużonych Wielkopolan", "https://kultura.poznan.pl/mim/kultura/muzea-w-poznaniu,poi,202,12/krypta-zasluzonych-wielkopolan,35331.html"),
                 ("Wikipedia: Kościół św. Wojciecha w Poznaniu", "https://pl.wikipedia.org/wiki/Kościół_św._Wojciecha_w_Poznaniu")],
    ),
    dict(
        slug="muzeum-instrumentow", cat="muzea", name="Muzeum Instrumentów Muzycznych",
        img="muzeum-instrumentow", img_alt="Kamienica Muzeum Instrumentów Muzycznych przy Starym Rynku",
        short="Skrzypce Wieniawskiego i klawesyn, na którym grał młody Mozart.",
        badge="Pn nieczynne",
        status=None,
        lead="Muzeum Instrumentów Muzycznych, oddział Muzeum Narodowego, mieści się w kamienicy przy Starym Rynku. Wystawa stała „Nowe brzmienie” jest podzielona na 16 galerii i opowiada o muzyce europejskiej od późnego średniowiecza po XX wiek.",
        sections=[
            ("Co zobaczyć", [
                "Skrzypce F. Ganda z 1846 roku, które należały do Henryka Wieniawskiego.",
                "Dwumanuałowy klawesyn Burkata Shudiego z 1765 roku, wykonany na zamówienie króla Prus Fryderyka II. Grali na nim młody Wolfgang Amadeusz Mozart i Carl Philipp Emanuel Bach, syn Jana Sebastiana Bacha.",
                "Najcenniejszy zbiór muzeum to instrumenty lutnicze z XVII–XX wieku: skrzypce i viole da gamba z warsztatów polskich mistrzów Dankwarta i Groblicza, skrzypce włoskich mistrzów, m.in. Guadaniniego i rodziny Amatich, oraz wiolonczela J.-B. Vuillaume'a. W kolekcji są też tradycyjne instrumenty kultur świata.",
                "Instrumenty pokazane w kontekście epoki, zespołu, miejsca i tradycji. Na tabletach z przewodnikiem multimedialnym można posłuchać, jak brzmią.",
            ]),
            ("Warto wiedzieć", [
                "Muzeum jest jedyną tego typu placówką w Polsce. Oddział Muzeum Instrumentów Muzycznych powstał w listopadzie 1945 roku z inicjatywy Zdzisława Szulca, kolekcjonera i uczestnika powstania wielkopolskiego. Obecną siedzibę w Kamienicy Grodzkich na rogu Starego Rynku i ulicy Woźnej otwarto 4 grudnia 1952 roku, a całkowicie nową ekspozycję po kilkuletnim remoncie 13 września 2019 roku. Dziś zbiory liczą blisko 3000 obiektów.",
                "Muzeum mieści się w dwukondygnacyjnej kamienicy bez windy. Parter jest częściowo dostępny architektonicznie, a w budynku nie ma toalety dla osób z niepełnosprawnością.",
                "Kasa zamykana jest 30 minut przed zamknięciem muzeum. Muzeum jest nieczynne m.in. 1 stycznia, od Wielkiego Piątku do Poniedziałku Wielkanocnego, w Boże Ciało, 1 listopada oraz 24, 25, 26 i 31 grudnia. Jest otwarte (jak w niedzielę) 6 stycznia, 1 i 3 maja, 15 sierpnia i 11 listopada.",
                "Od 1946 roku działa tu jedyna w Polsce pracownia konserwacji instrumentów muzycznych.",
                "Muzeum współorganizuje najstarszy na świecie Międzynarodowy Konkurs Lutniczy im. Henryka Wieniawskiego. W sali koncertowej im. Marcina Groblicza odbywają się koncerty sylwestrowe.",
                "Z Poznańską Kartą Turystyczną wstęp jest bezpłatny.",
            ]),
        ],
        address="Stary Rynek 45, 61-772 Poznań",
        hours=[("Poniedziałek", "nieczynne"), ("Wtorek–środa", "10:00–16:00"), ("Czwartek", "10:00–18:00"), ("Piątek", "10:00–20:00"), ("Sobota–niedziela", "10:00–17:00")],
        tickets=[("Normalny", "15 zł"), ("Ulgowy", "10 zł"), ("Dzieci i młodzież 8–26 lat", "1 zł"), ("Wtorek", "wstęp wolny"), ("Z Poznańską Kartą Turystyczną", "bezpłatnie")], checked="01.10.2026",
        phone="+48 61 852 08 57", www=("mnp.art.pl", "https://mnp.art.pl/muzeum-instrumentow-muzycznych"),
        credit="muzeum-instrumentow",
        sources=[("MNP: Wizyta (godziny, bilety, dostępność)", "https://mnp.art.pl/profile/wizyta-muzeum-instrumentow-muzycznych"),
                 ("MNP: Muzeum Instrumentów Muzycznych", "https://mnp.art.pl/muzeum-instrumentow-muzycznych"),
                 ("MNP: Kim jesteśmy, historia i zbiory", "https://mnp.art.pl/profile/muzeum-instrumentow-muzycznych"),
                 ("Poznan.pl: Muzeum Instrumentów Muzycznych", "https://www.poznan.pl/mim/turystyka/muzea-w-poznaniu,poi,202/-,15707.html"),
                 ("Visit Poznań: Muzeum Instrumentów Muzycznych", "https://visitpoznan.pl/muzeum-instrumentow-muzycznych")],
    ),
    dict(
        slug="muzeum-czerwca-1956", cat="muzea", name="Muzeum Poznańskiego Czerwca 1956",
        img="muzeum-czerwca-1956", img_alt="Ekspozycja Muzeum Powstania Poznańskiego – Czerwiec 1956",
        short="Historia buntu robotników z 28 czerwca 1956 roku, w Zamku Cesarskim.",
        badge="Nd wstęp wolny",
        status=None,
        lead="Muzeum Powstania Poznańskiego – Czerwiec 1956 opowiada o buncie robotniczym z 28 czerwca 1956 roku, pierwszym masowym proteście przeciw władzy komunistycznej w Polsce. Mieści się w Zamku Cesarskim.",
        sections=[
            ("Co zobaczyć", [
                "Reprodukcje fotografii z czerwca 1956 roku, pamiątki po ofiarach i makiety projektów Pomnika Poznańskiego Czerwca.",
                "Materiały multimedialne o historii Polski od 1945 roku do końca PRL.",
            ]),
            ("Warto wiedzieć", [
                "Od 1 stycznia 2026 roku muzeum jest samodzielną instytucją kultury. Po przerwie otworzyło się ponownie 1 lutego 2026 roku.",
                "Dzień bezpłatnego wstępu przeniesiono z wtorku na niedzielę.",
                "Z Poznańską Kartą Turystyczną wstęp jest bezpłatny.",
                "Oprowadzanie z przewodnikiem: 100 zł dla grupy do 25 osób, 40 zł dla maksymalnie 5 osób.",
            ]),
        ],
        address="ul. Święty Marcin 80/82 (Zamek Cesarski), 61-809 Poznań",
        hours=[("Godziny otwarcia", "potwierdź telefonicznie przed wizytą")],
        tickets=[("Normalny", "15 zł"), ("Ulgowy", "10 zł"), ("Niedziela", "wstęp wolny")],
        phone="+48 61 852 94 64", www=("wmn.poznan.pl", "https://www.wmn.poznan.pl/lokalizacja_wystaw/muzeum-powstania-poznanskiego/"),
        credit="muzeum-czerwca-1956",
        sources=[("WMN: ponowne otwarcie muzeum (1.02.2026)", "https://www.wmn.poznan.pl/moje-aktualnosci/muzeum-powstania-poznanskiego-czerwiec-1956-w-poznaniu-ponownie-otwiera-sie-dla-zwiedzajacych/"),
                 ("WMN: Muzeum Powstania Poznańskiego – Czerwiec 1956", "https://www.wmn.poznan.pl/lokalizacja_wystaw/muzeum-powstania-poznanskiego/"),
                 ("Visit Poznań: Muzeum Powstania Poznańskiego", "https://visitpoznan.pl/muzeum-powstania-poznanskiego-czerwiec-1956")],
    ),
    dict(
        slug="muzeum-kultur-swiata", cat="muzea", name="Muzeum Kultur Świata",
        img="muzeum-kultur-swiata", img_alt="Klasycystyczny budynek Muzeum Kultur Świata przy ul. Grobla",
        short="Dawne Muzeum Etnograficzne w klasycystycznej siedzibie loży masońskiej.",
        badge="Pn nieczynne",
        status=None,
        lead="Muzeum Kultur Świata to dawne Muzeum Etnograficzne, oddział Muzeum Narodowego. Nową nazwę dostało w 2025 roku. Mieści się w późnoklasycystycznym budynku z lat 1817–1819, dawnej siedzibie loży masońskiej.",
        sections=[
            ("Co zobaczyć", [
                "Zbiory kultury polskiej i wielkopolskiej oraz kultur z odległych regionów świata, pokazywane na wystawach czasowych.",
            ]),
            ("Warto wiedzieć", [
                "Wejście do muzeum jest od ul. Mostowej 7, przez park.",
                "Muzeum organizuje oprowadzania, lekcje, warsztaty, koncerty i spotkania weekendowe.",
            ]),
        ],
        address="ul. Grobla 25 (wejście od ul. Mostowej 7), 61-858 Poznań",
        hours=[("Poniedziałek", "nieczynne"), ("Wtorek–środa", "10:00–16:00"), ("Czwartek", "10:00–18:00"), ("Piątek", "10:00–20:00"), ("Sobota–niedziela", "10:00–17:00")],
        tickets=[("Normalny", "20 zł"), ("Ulgowy", "13 zł"), ("Dzieci i młodzież 8–26 lat", "1 zł"), ("Wtorek", "wstęp wolny")], checked="01.10.2026",
        phone="+48 61 852 30 06", www=("mnp.art.pl", "https://mnp.art.pl/muzeum-kultur-swiata"),
        credit="muzeum-kultur-swiata",
        sources=[("poznan.pl: Muzeum Kultur Świata", "https://www.poznan.pl/mim/turystyka/muzea-w-poznaniu,poi,202,12/muzeum-etnograficzne-oddzial-muzeum-narodowego,15728.html"),
                 ("PIK Poznań: Muzeum Kultur Świata", "https://pik.poznan.pl/miejsca/muzeum-etnograficzne-w-poznaniu/")],
    ),
    dict(
        slug="muzeum-sienkiewicza", cat="muzea", name="Muzeum Literackie Henryka Sienkiewicza",
        img="muzeum-sienkiewicza", img_pos="center 60%", img_alt="Zdobiona sgraffitami kamienica przy Starym Rynku 84, siedziba Muzeum Literackiego Henryka Sienkiewicza, z rzeźbą w niszy i fontanną na pierwszym planie",
        short="Pamiątki po nobliście w XVI-wiecznej kamienicy na rynku. W soboty wstęp wolny.",
        badge="Sb wstęp wolny",
        status=None,
        lead="Muzeum Literackie Henryka Sienkiewicza to oddział Biblioteki Raczyńskich w XVI-wiecznej kamienicy przy Starym Rynku 84. Jest najmłodszym muzeum poświęconym pisarzowi w Polsce.",
        sections=[
            ("O muzeum", [
                "Autor „Trylogii” rzadko bywał w Wielkopolsce, a w tej kamienicy nie gościł nigdy. Z Poznaniem związał go Ignacy Moś, charyzmatyczny kolekcjoner, który większość życia poświęcił na gromadzenie pamiątek po pisarzu, a zbiory przekazał Bibliotece Raczyńskich.",
                "Siedzibą muzeum jest zabytkowa kamienica, której dawnymi właścicielami byli m.in. Jan Baptysta Quadro, budowniczy renesansowego ratusza, oraz prezydent miasta Cyryl Ratajski.",
            ]),
            ("Co zobaczyć", [
                "Maskę pośmiertną i odlew prawej dłoni pisarza, dzieła rzeźbiarza Franciszka Blacka.",
                "Osobisty egzemplarz „Quo vadis” na papierze japońskim, z heliograwiurami Piotra Stachiewicza, pochodzący z prywatnej biblioteki pisarza. Mosiowi podarował go syn Sienkiewicza.",
                "Replikę medalu Nagrody Nobla z 1905 roku.",
                "Rzeźbę „Ursus walczący z turem” Marcina Rożka.",
                "Pierwsze wydania niemal wszystkich powieści Sienkiewicza i ich przekłady na języki z całego świata, także tak rzadkie jak chiński, japoński, gruziński, arabski i hebrajski.",
            ]),
        ],
        address="Stary Rynek 84, 61-772 Poznań",
        hours=[("Wtorek, piątek, sobota", "9:00–16:00"), ("Środa, czwartek", "12:00–19:00"), ("Poniedziałek, niedziela, święta", "nieczynne")],
        tickets=[("Normalny", "10 zł"), ("Ulgowy", "5 zł"), ("Sobota", "wstęp wolny")],
        phone="+48 61 852 89 71", www=("bracz.edu.pl", "https://bracz.edu.pl/muzeum-sienkiewicza/"),
        credit="muzeum-sienkiewicza",
        sources=[("Biblioteka Raczyńskich: Muzeum Sienkiewicza", "https://bracz.edu.pl/muzeum-sienkiewicza/"),
                 ("Visit Poznań: Muzeum Literackie Henryka Sienkiewicza", "https://visitpoznan.pl/muzeum-literackie-henryka-sienkiewicza")],
    ),
    dict(
        slug="muzeum-bambrow", cat="muzea", name="Muzeum Bambrów Poznańskich",
        img="muzeum-bambrow", img_alt="Studzienka Bamberki, symbol Bambrów Poznańskich (zdjęcie ilustracyjne)",
        short="Historia osadników spod Bambergu, którzy w XVIII wieku zasiedlili podpoznańskie wsie.",
        badge="Pt–sb",
        status=None,
        lead="Muzeum prowadzi Towarzystwo Bambrów Poznańskich. Opowiada o osadnikach spod Bambergu we Frankonii, którzy w latach 1719–1753 przybyli do wsi wokół Poznania, zniszczonych przez wojnę północną i zarazę.",
        sections=[
            ("Kim byli Bambrzy", [
                "Pierwsi osadnicy przybyli do Lubonia w 1719 roku. Kolejni osiedlali się na Dębcu i Boninie (1730), na Ratajach i Wildzie (1746–1747) oraz na Jeżycach i Górczynie (1750–1753).",
                "Byli rolnikami i zaopatrywali miasto w żywność. Dostali korzystne warunki: dzierżawę ziemi, materiały budowlane, ziarno siewne i kilka lat zwolnienia z podatków.",
                "W XIX wieku ukształtował się charakterystyczny strój kobiecy z kwiatowym kornetem, który ważył nawet 3 kg. Pod koniec XIX wieku Bambrzy w większości się spolszczyli.",
            ]),
            ("Warto wiedzieć", [
                "Oprowadzanie po muzeum jest bezpłatne. Grupy zorganizowane powinny wcześniej zgłosić wizytę.",
                "Muzeum jest dostępne dla osób z niepełnosprawnościami.",
            ]),
        ],
        address="ul. Mostowa 7/9, 61-854 Poznań",
        hours=[("Piątek i sobota", "10:00–14:00")],
        tickets=[("Oprowadzanie", "bezpłatne, po umówieniu")],
        phone="+48 602 658 961", www=("bambrzy.poznan.pl", "https://www.bambrzy.poznan.pl/"),
        credit="muzeum-bambrow",
        sources=[("Towarzystwo Bambrów Poznańskich: informacje dla zwiedzających", "https://www.bambrzy.poznan.pl/node/7"),
                 ("Wikipedia: Bambrzy", "https://pl.wikipedia.org/wiki/Bambrzy")],
    ),
    dict(
        slug="rusalka", cat="przyroda", name="Jezioro Rusałka",
        img="rusalka", img_alt="Jezioro Rusałka w Poznaniu",
        short="Leśne jezioro z plażą i strzeżonym kąpieliskiem w zachodniej części miasta.",
        badge="Bezpłatnie",
        status=None,
        lead="Rusałka to jezioro o powierzchni 36,7 hektara w klinie zieleni Golęcin, w zachodniej części Poznania. Latem działa tu piaszczysta plaża z kąpieliskiem miejskim.",
        sections=[
            ("Kąpielisko", [
                "Kąpielisko ma 96 metrów linii brzegowej. W sezonie pilnują go ratownicy.",
                "Są dwie strefy: dla nieumiejących pływać, o głębokości do 1,2 metra (czerwone boje), i dla pływających, do 4 metrów (żółte boje).",
                "W 2026 roku sezon kąpielowy trwał od 20 czerwca do 6 września.",
            ]),
            ("Co jeszcze jest nad jeziorem", [
                "Plac zabaw, siłownia plenerowa, boiska do siatkówki plażowej i boccii, ścieżka rowerowa, park rozrywki Frajda oraz punkty gastronomiczne.",
                "Na kąpielisku jest wózek plażowy typu amfibia dla osób z niepełnosprawnościami. O dostępność pytaj ratowników.",
            ]),
        ],
        address="ul. Golęcińska 27, 60-626 Poznań",
        hours=[("Teren wokół jeziora", "dostępny całą dobę"), ("Kąpielisko strzeżone", "w sezonie letnim")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("posir.poznan.pl", "https://posir.poznan.pl/obiekty/rusalka/kapielisko"),
        credit="rusalka",
        sources=[("POSiR: kąpielisko Rusałka", "https://posir.poznan.pl/obiekty/rusalka/kapielisko"),
                 ("Poznańskie Klimaty: sezon kąpielowy 2026", "https://www.poznanskieklimaty.pl/sezon-kapielowy-w-poznaniu-2026-kiedy-otwieraja-sie-plaze-nad-jeziorami/")],
    ),
    dict(
        slug="stadion", cat="wspolczesny", name="Enea Stadion i Muzeum Lecha",
        img="stadion", img_alt="Parowóz przed stadionem miejskim w Poznaniu",
        short="Zwiedzanie stadionu Euro 2012: szatnia, tunel, ławka rezerwowych i muzeum klubu.",
        badge="Pn–sb",
        status=None,
        lead="Stadion Miejski przy ulicy Bułgarskiej to dom Lecha Poznań. Przebudowany obiekt otwarto 20 września 2010 roku, a w 2012 roku rozegrano tu trzy mecze fazy grupowej Euro 2012. Według Wikipedii mieści 43 269 widzów (po powiększeniu w 2012 roku).",
        sections=[
            ("Zwiedzanie", [
                "Stadion zwiedza się wyłącznie z przewodnikiem, samodzielne wejście nie jest możliwe. Wycieczka trwa około godziny, w grupie do 35 osób, po polsku lub angielsku. Obejmuje szatnię gości (trasa nie prowadzi do szatni gospodarzy), tunel, którym piłkarze wychodzą na boisko, ławki rezerwowych i multimedialne Muzeum Lecha Poznań.",
                "Godziny w tabeli to wzorzec. Terminarz na cały tydzień pojawia się na stronie biletowej w weekend poprzedzający, bo zależy od wydarzeń na stadionie, więc część dni bywa bez wycieczek: w tygodniu 19–25.10.2026 nie było ich w środę, czwartek i niedzielę, a w poniedziałek i piątek odbyły się o 14:00 i 16:00. Aktualny kalendarz sprawdź przed wizytą w „Kalendarzu Wycieczek z Muzeum” na stronie bilety.lechpoznan.pl.",
            ]),
            ("Jak wejść", [
                "Wycieczka startuje spod sklepu Stacja Kolejorz (pon.–pt. 10:00–19:00, sobota 10:00–15:00). Bilet kupisz online (nie trzeba go drukować, wystarczy podać przewodnikowi numer) albo u przewodnika na miejscu, ale bez rezerwacji i bilety mogą się skończyć. Bilet na konkretny dzień można wykorzystać w innym terminie po wiadomości na wycieczki@lechpoznan.pl.",
                "Parking A1 dla zwiedzających jest przy ulicy Ptasiej, naprzeciwko salonu Mercedesa, koło białego namiotu.",
                "Stadion jest przystosowany dla osób na wózkach inwalidzkich. Z wózkiem dziecięcym można wejść, ale strona radzi zostawić go w samochodzie lub w Stacji Kolejorz.",
            ]),
            ("Warto wiedzieć", [
                "Ulgowy bilet przysługuje dzieciom i młodzieży do ukończenia 18 lat, osobom uczącym się do ukończenia 26 lat, seniorom powyżej 65 lat i osobom z niepełnosprawnościami (ich opiekunowie wchodzą bezpłatnie). Dzieci do ukończenia 4. roku życia wchodzą bezpłatnie.",
                "Rodziny dostają zniżkę od ceny końcowej, naliczaną w podsumowaniu transakcji: 10% za 2 bilety normalne i 1 ulgowy, 15% za 2 normalne i 2 ulgowe, 20% za 2 normalne i 3 lub więcej ulgowych.",
                "Posiadacze karnetu z programu Lechici mają bilet na zwiedzanie 50% taniej (raz w sezonie, ze swojego konta). Po okazaniu biletu obowiązuje w tym samym dniu 20% rabatu w restauracji MasterLech.",
                "Infolinia w sprawie wycieczek indywidualnych (tel. 660 423 851) jest czynna od poniedziałku do piątku 11:00–16:00, z wyłączeniem świąt, dni wolnych i dni meczowych. Grupy i inne pytania: wycieczki@lechpoznan.pl.",
                "Są też inne wycieczki: dla grup zorganizowanych (poniedziałek–piątek, od 20 zł od osoby plus 90 zł od grupy za przewodnika), przedmeczowa (zaczyna się 2,5 godziny przed meczem Ekstraklasy, a cena zależy od meczu i obejmuje bilet na mecz oraz parking) i ekskluzywna z obiadem w MasterLech (voucher 200 zł, ulgowy 150 zł, termin ustalany 10–14 dni wcześniej, bez weekendów, dni meczowych i świąt).",
            ]),
        ],
        address="ul. Bułgarska 17, 60-320 Poznań",
        hours=[("V–IX, pn–pt", "12:00, 14:00, 16:00, 17:30"), ("X–IV, pn–pt", "12:00, 14:00, 16:00"), ("Sobota (cały rok)", "10:00, 11:30, 12:45, 14:00")],
        tickets=[("Normalny", "35 zł"), ("Ulgowy", "25 zł"), ("Dzieci do 4 lat", "bezpłatnie")],
        phone="+48 660 423 851", www=("bilety.lechpoznan.pl", "https://bilety.lechpoznan.pl/CMS?page=zwiedzanie"),
        credit="stadion",
        sources=[("Lech Poznań: zwiedzanie stadionu i muzeum", "https://bilety.lechpoznan.pl/CMS?page=zwiedzanie"),
                 ("Wikipedia: Stadion Miejski w Poznaniu", "https://pl.wikipedia.org/wiki/Stadion_Miejski_w_Poznaniu")],
    ),
    dict(
        slug="jezyce", cat="wspolczesny", name="Jeżyce",
        img="jezyce", img_alt="Kamienice przy Rynku Jeżyckim",
        short="Secesyjne kamienice, targ na Rynku Jeżyckim i szlak Jeżycjady Małgorzaty Musierowicz.",
        badge="Bezpłatnie",
        status=None,
        lead="Jeżyce to jedna z najbardziej lubianych dzielnic Poznania. Dawna wieś, wspomniana już w 1253 roku, w 1900 roku została włączona do miasta i szybko zabudowała się kamienicami, wiele z nich z secesyjnymi zdobieniami.",
        sections=[
            ("O dzielnicy", [
                "Pierwsza pisemna wzmianka o Jeżycach pojawia się w przywileju lokacyjnym Poznania z 1253 roku. Przez wieki była to wieś rolnicza. W XVIII wieku osiedlili się tu Bambrzy, osadnicy spod Bambergu.",
                "W 1848 roku na Jeżycach otwarto pierwszy dworzec kolejowy w Poznaniu. Po włączeniu do miasta w 1900 roku wiejską zabudowę zastąpiły wielopiętrowe kamienice czynszowe. Dawny wiejski układ przetrwał w owalnym kształcie ulicy Kościelnej.",
            ]),
            ("Co zobaczyć", [
                "Rynek Jeżycki, serce dzielnicy. Działa na nim jedno z najstarszych targowisk w Poznaniu: warzywa, owoce, kwiaty, pieczywo, sery, miód i używane książki.",
                "Secesyjne kamienice przy ulicach Dąbrowskiego, Mickiewicza, Słowackiego i Prusa, a także wille przy ulicach Roosevelta i Zacisze.",
                "Teatr Nowy przy ulicy Dąbrowskiego i kościół Najświętszego Serca Pana Jezusa i św. Floriana z 1906 roku.",
            ]),
            ("Szlak Jeżycjady", [
                "Na Jeżycach toczy się akcja „Jeżycjady”, cyklu powieści Małgorzaty Musierowicz. Poznańska Lokalna Organizacja Turystyczna przygotowała razem z autorką Poznański Szlak Jeżycjady: około 7 km (skrócony wariant 3 km) przez Jeżyce i Dzielnicę Cesarską, z cytatami i nagraniami czytanymi przez pisarkę.",
            ]),
            ("Warto wiedzieć", [
                "Na Jeżycach są też Stare Zoo i Ogród Botaniczny UAM. Oba miejsca opisujemy na osobnych stronach.",
            ]),
        ],
        address="Rynek Jeżycki, 60-847 Poznań",
        hours=[("Dzielnica", "dostępna całą dobę"), ("Targowisko na Rynku Jeżyckim", "pn–sb 6:00–20:00, nd nieczynne")],
        tickets=[("Spacer", "bezpłatnie")],
        phone=None, www=("visitpoznan.pl", "https://visitpoznan.pl/rynek-jezycki-poznanski-szlak-jezycjady"),
        credit="jezyce",
        sources=[("poznan.pl: Jeżyce – historia", "https://www.poznan.pl/mim/rewitalizacja/-,p,38552,38561,42846.html"),
                 ("Wikipedia: Jeżyce", "https://pl.wikipedia.org/wiki/Jeżyce"),
                 ("Visit Poznań: Rynek Jeżycki (Poznański Szlak Jeżycjady)", "https://visitpoznan.pl/rynek-jezycki-poznanski-szlak-jezycjady"),
                 ("Targowiska: Rynek Jeżycki", "https://www.targowiska.com.pl/lokalizacje/rynek-jezycki/")],
    ),
    dict(
        slug="bulwary-warta", cat="przyroda", name="Bulwary nad Wartą",
        img="bulwary-warta", img_alt="Plaża miejska nad Wartą na Szelągu",
        short="Wartostrada: 13,6 km ścieżek pieszych i rowerowych wzdłuż rzeki, latem plaże miejskie.",
        badge="Bezpłatnie",
        status=None,
        lead="Wartostrada to system ścieżek pieszych i rowerowych wzdłuż Warty. Dwie trasy po obu brzegach rzeki mają łącznie 13,6 km i prowadzą od Mostu Przemysła I na południu do Mostu Lecha na północy.",
        sections=[
            ("O trasie", [
                "Budowa Wartostrady zaczęła się w 2011 roku, a trasę rozbudowywano w latach 2015–2020 i 2020–2022. Ścieżki są przeznaczone dla pieszych i rowerzystów na każdym poziomie.",
                "Trasa łączy m.in. Most Królowej Jadwigi, Most św. Rocha i Most Bolesława Chrobrego. Prowadzi obok Bramy Poznania i przez parki: Park Szelągowski i Park nad Wartą.",
                "Na trasie są punkty widokowe, stacje naprawy rowerów i parkingi Bike&Ride.",
            ]),
            ("Plaże miejskie", [
                "Latem nad Wartą działają plaże miejskie, m.in. na Chwaliszewie i Szelągu. Terminy sezonu i atrakcje miasto ogłasza co roku.",
            ]),
            ("Warto wiedzieć", [
                "Z Wartostrady łatwo dojść do Ostrowa Tumskiego, Bramy Poznania i Śródki, więc spacer nad rzeką można połączyć z ich zwiedzaniem.",
            ]),
        ],
        address="Wartostrada (odcinek śródmiejski), 61-124 Poznań",
        hours=[("Ścieżki", "dostępne całą dobę"), ("Plaże miejskie", "w sezonie letnim")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", "https://www.poznan.pl/"),
        credit="bulwary-warta",
        sources=[("Wikipedia: Wartostrada", "https://pl.wikipedia.org/wiki/Wartostrada"),
                 ("poznan.pl: plaże miejskie", "https://www.poznan.pl/mim/main/-,p,1182,25430,25431.html")],
    ),
    dict(
        slug="park-solacki", cat="przyroda", name="Park Sołacki",
        img="park-solacki", img_alt="Staw w Parku Sołackim",
        short="Stuletni park krajobrazowy ze stawami na Bogdance, wśród willi Sołacza.",
        badge="Bezpłatnie",
        status=None,
        lead="Park Sołacki urządzono w latach 1908–1911 według projektu Hermanna Kube, ówczesnego dyrektora Ogrodów Miejskich w Poznaniu. Ma prawie 15 hektarów i powstał na podmokłych terenach doliny Bogdanki.",
        sections=[
            ("O parku", [
                "To park w stylu angielskim. Rośnie tu około 3000 drzew i 12 000 krzewów, obok gatunków rodzimych także egzotyczne, m.in. choina kanadyjska, cypryśnik błotny i daglezja.",
                "Spiętrzona Bogdanka tworzy Stawy Sołackie o nieregularnych brzegach.",
                "Od 1983 roku park jest wpisany do rejestru zabytków razem z willową dzielnicą Sołacz.",
            ]),
            ("Co zobaczyć", [
                "Stawy, mostki i wodospad na Bogdance.",
                "Zieloną wiatę tramwajową przy ulicy Małopolskiej z 1913 roku, kiedy do Sołacza dojechał tramwaj.",
                "Rzeźbę „Dwie kobiety” Sylwestra Ambroziaka z 2008 roku.",
                "Budynek z 1912 roku, w którym po remoncie w 2022 roku działa hotel z restauracją Port Sołacz.",
            ]),
            ("Warto wiedzieć", [
                "W parku są place zabaw i alejki spacerowe. Można tu spotkać m.in. mandarynki i dzięcioły.",
            ]),
        ],
        address="Park Sołacki, 60-631 Poznań",
        hours=[("Park", "ogólnodostępny")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", "https://www.poznan.pl/mim/smartcity/infoteka,1016/park-solacki-zielen-z-ponad-100-letnia-historia,265390.html"),
        credit="park-solacki",
        sources=[("poznan.pl: Park Sołacki – zieleń z ponad 100-letnią historią", "https://www.poznan.pl/mim/smartcity/infoteka,1016/park-solacki-zielen-z-ponad-100-letnia-historia,265390.html"),
                 ("Wikipedia: Park Sołacki", "https://pl.wikipedia.org/wiki/Park_Sołacki")],
    ),
    dict(
        slug="trakt-krolewsko-cesarski", cat="zabytki", name="Trakt Królewsko-Cesarski",
        img="trakt-krolewsko-cesarski", img_alt="Oznakowanie Traktu Królewsko-Cesarskiego z koroną przy Bramie Poznania",
        short="Główny szlak turystyczny Poznania: od Bramy Poznania przez Ostrów Tumski i Stary Rynek do Zamku.",
        badge="Bezpłatnie",
        status=None,
        lead="Trakt Królewsko-Cesarski to główny szlak turystyczno-kulturowy Poznania. Łączy najciekawsze części miasta i opowiada historię Poznania oraz czterdziestu pokoleń jego mieszkańców.",
        sections=[
            ("Przebieg", [
                "Główna oś ma około 3 km i prowadzi na zachód od Bramy Poznania przez Ostrów Tumski z katedrą, Stary Rynek z ratuszem i Stare Miasto po Śródmieście z muzeami i teatrami oraz Zamek Cesarski.",
                "Pierwotnie szlak wyznaczono od kościoła św. Jana Jerozolimskiego za Murami do kościoła Najświętszego Serca Pana Jezusa i św. Floriana na Jeżycach. Wokół głównej osi biegną szlaki dodatkowe.",
                "Na trasie są m.in. katedra, Zamek Królewski, ratusz, dawne Kolegium Jezuickie, Biblioteka Raczyńskich i Zamek Cesarski.",
            ]),
            ("Jak zwiedzać", [
                "Trasę oznaczają bordowe tabliczki z wyciętą koroną, logo traktu, umieszczone na elementach miejskiej infrastruktury.",
                "Szlak można przejść pieszo albo przejechać rowerem i komunikacją miejską. Zwiedzanie jest bezpłatne, a na stronie traktu są darmowe foldery i mapa.",
                "Co roku odbywają się bezpłatne spacery z przewodnikiem.",
            ]),
            ("O szlaku", [
                "Trakt powstał w latach 2006–2013 według koncepcji z 2004 roku, a w 2015 roku przebieg zmodyfikowano. Zarządza nim Poznańskie Centrum Dziedzictwa, miejska instytucja kultury.",
            ]),
        ],
        address="Brama Poznania, ul. Gdańska 2, 61-123 Poznań",
        hours=[("Szlak", "dostępny całą dobę")],
        tickets=[("Zwiedzanie", "bezpłatnie")],
        phone=None, www=("trakt.poznan.pl", "https://trakt.poznan.pl/"),
        credit="trakt-krolewsko-cesarski",
        sources=[("trakt.poznan.pl: Poznaj Trakt Królewsko-Cesarski", "https://trakt.poznan.pl/poznaj-trakt-krolewsko-cesarski"),
                 ("Wikipedia: Trakt Królewsko-Cesarski w Poznaniu", "https://pl.wikipedia.org/wiki/Trakt_Królewsko-Cesarski_w_Poznaniu")],
    ),
]

_ORDER = {k: i for i, (k, _, _) in enumerate(CATEGORIES)}
from data_extra import EXTRA  # noqa: E402  (atrakcje z rozbudowy od 29.09.2026)
from data_churches import CHURCHES  # noqa: E402  (zabytkowe kościoły, partia 4)
from data_final import FINAL  # noqa: E402  (forty, jeziora, parki, Okrąglak, linie turystyczne)
from data_parks import PARKS  # noqa: E402  (etap 7: duże i zabytkowe parki, Morasko, Lasek Marceliński)
from data_monuments import MONUMENTS  # noqa: E402  (etap 7: pomniki i fontanny z POI poznan.pl)
from data_theatres import THEATRE_ATTR  # noqa: E402  (Teatr Wielki, 30.09.2026)
from data_trips import TRIPS  # noqa: E402  (wycieczki za miasto, 30.09.2026)
from data_gaps import GAPS  # noqa: E402
from data_gaps2 import GAPS2  # noqa: E402
from data_trips2 import TRIPS2  # noqa: E402  (wycieczki, partia 2, 06.10.2026)  (uzupełnienie luk po porównaniu z poznan.pl, 06.10.2026)
from data_gaps3 import GAPS3  # noqa: E402  (taras Collegium Altum i muzea w Cytadeli/Zamku, po porównaniu z konkurencją 10.10.2026)
from data_gaps4 import GAPS4  # noqa: E402  (Lodowisko Malta, 19.10.2026)
# Data sprawdzenia godzin i cen każdej atrakcji (pole checked). Domyślnie według partii danych;
# przy ponownej weryfikacji jednej atrakcji wpisz jej własne checked="DD.MM.RRRR".
_CHECKED_BY_BATCH = [
    (ATTRACTIONS + MORE, "28.09.2026"),
    (EXTRA + CHURCHES + FINAL + PARKS + MONUMENTS, "29.09.2026"),
    (TRIPS + THEATRE_ATTR, "30.09.2026"),
    (GAPS + GAPS2 + TRIPS2, "06.10.2026"),
    (GAPS3, "10.10.2026"),
    (GAPS4, "19.10.2026"),
]
_CHECKED_SLUGS = {"park-solacki": "29.09.2026", "trakt-krolewsko-cesarski": "29.09.2026",  # czwarta tura
                  "stary-browar": "30.09.2026"}  # rozbudowa opisu, nowy adres i godziny
for _batch, _date in _CHECKED_BY_BATCH:
    for _a in _batch:
        _a.setdefault("checked", _CHECKED_SLUGS.get(_a["slug"], _date))
ATTRACTIONS = sorted(ATTRACTIONS + MORE + EXTRA + CHURCHES + FINAL + PARKS + MONUMENTS + TRIPS + THEATRE_ATTR + GAPS + GAPS2 + TRIPS2 + GAPS3 + GAPS4, key=lambda a: _ORDER[a["cat"]])

# Przegląd 09.10.2026: godziny i ceny 70 atrakcji z liczbami porównano z oficjalnymi stronami obiektów
# (cenniki PDF, strony muzeów, kasy biletowe). Atrakcje bezpłatne i całodobowe (opisowe godziny) nie mają
# liczb do porównania, więc zostają przy dawnej dacie.
_VERIFIED_20261009 = {
    "stary-rynek", "ostrow-tumski", "brama-poznania", "zamek-krolewski",
    "zamek-cesarski", "cytadela", "genius-loci", "fort-iva",
    "fort-va", "teatr-wielki", "fort-iii", "cmentarz-zasluzonych-wielkopolan",
    "podziemia-katedry", "fontanna-park-wilsona", "fara", "muzeum-narodowe",
    "rogalowe-muzeum", "muzeum-powstania", "muzeum-archeologiczne", "muzeum-instrumentow",
    "muzeum-czerwca-1956", "muzeum-kultur-swiata", "muzeum-sienkiewicza", "muzeum-bambrow",
    "centrum-szyfrow-enigma", "fort-vii", "muzeum-wojskowe", "muzeum-pyry",
    "fotoplastykon", "akademia-lubranskiego", "muzeum-broni-pancernej", "muzeum-farmacji",
    "muzeum-historii-ubioru", "muzeum-iluzji", "muzeum-prl", 
    "muzeum-czekolady", "salon-nowowiejskiego", "muzeum-bizuterii-moja", "mieszkanie-illakowiczowny",
    "makiety-dawnego-poznania", "niewidzialna-ulica", "ogrod-botaniczny",
    "park-wilsona", "park-rataje", "nowe-zoo", "stare-zoo",
    "kolejka-maltanka", "termy-maltanskie", "linie-turystyczne", "stary-browar",
    "stadion", "jezyce", "zamek-kornik", "arboretum-kornik",
    "rogalin", "katedra-gniezno", "mppp-gniezno", "ostrow-lednicki",
    "biskupin", "wpn", "szreniawa", "fiedler",
    "zamek-goluchow", "palac-smielow", "wpe-dziekanowice", "parowozownia-wolsztyn",
    "muzeum-lesnictwa-goluchow", "skansen-miniatur-pobiedziska", "grod-pobiedziska",
}
for _a in ATTRACTIONS:
    if _a["slug"] in _VERIFIED_20261009:
        _a["checked"] = "09.10.2026"

# Ponowne sprawdzenie godzin i cen 10.10.2026 (audyt): strona CK Zamek i cennik PDF z 30.03.2026.
for _a in ATTRACTIONS:
    if _a["slug"] == "zamek-cesarski":
        _a["checked"] = "10.10.2026"

# Numery linii ZTM sprawdzone 10.10.2026 w oficjalnym pliku rozkładów (GTFS ważny 10–31.10.2026).
_ZTM_SLUGS = ("genius-loci", "fort-vii", "muzeum-historii-ubioru", "szachty", "legi-debinskie", "park-chopina",
              "park-mickiewicza", "muzeum-armii-poznan", "muzeum-uzbrojenia", "park-marcinkowskiego")
for _a in ATTRACTIONS:
    if _a["slug"] in _ZTM_SLUGS:
        _a["sources"] = list(_a["sources"]) + [("ZTM Poznań: rozkłady jazdy (plik GTFS ważny 10–31.10.2026)", "https://www.ztm.poznan.pl/")]

# Sezonowość sprawdzona 10.10.2026 w komunikatach MPK (koniec sezonu Maltanki i linii turystycznych), na maltaski.pl i na stronie katedry.
for _a in ATTRACTIONS:
    if _a["slug"] == "linie-turystyczne":
        _a["checked"] = "10.10.2026"
    # Maltanka: porównanie karty ze stroną MPK i komunikatami (start sezonu, bilety od 1.05, koniec sezonu 27.09) 2.11.2026.
    if _a["slug"] == "kolejka-maltanka":
        _a["checked"] = "02.11.2026"
    # Enea Stadion i Muzeum Lecha: porównanie karty ze stroną zwiedzania (bilety.lechpoznan.pl) i Wikipedią 27.10.2026.
    if _a["slug"] == "stadion":
        _a["checked"] = "27.10.2026"
    # Stary Browar: porównanie karty ze stroną centrum (o centrum, kontakt, Pop Culture Gallery) 27.10.2026.
    if _a["slug"] == "stary-browar":
        _a["checked"] = "27.10.2026"
    # Zamek Cesarski: porównanie karty ze stronami CK Zamek (zwiedzanie, historia, audioprzewodniki, kontakt, Imieniny Ulicy) 26.10.2026.
    if _a["slug"] == "zamek-cesarski":
        _a["checked"] = "26.10.2026"
    # Zamek Królewski i Muzeum Sztuk Użytkowych: pełne porównanie ze stronami MNP (wizyta, muzeum, zamek) 26.10.2026.
    if _a["slug"] == "zamek-krolewski":
        _a["checked"] = "26.10.2026"
    # Fara: pełne porównanie karty ze stroną parafii (zwiedzanie, historia, architektura, organy, kontakt) 26.10.2026.
    if _a["slug"] == "fara":
        _a["checked"] = "26.10.2026"
    # Ostrów Tumski: pełne porównanie karty ze stroną katedry (turyści, historia, kaplice) 26.10.2026.
    if _a["slug"] == "ostrow-tumski":
        _a["checked"] = "26.10.2026"
    if _a["slug"] == "malta-ski":
        _a["checked"] = "19.10.2026"   # sezony zimowy 17.10–31.03 i letni 1.04–31.10 wg maltaski.pl

# Przegląd sezonowy 24.10.2026: godziny i ceny porównane ze stronami obiektów (biskupin.pl, grodpobiedziska.pl,
# wzgorzelecha.pl, bkpan.poznan.pl, muzeum-szreniawa.pl). Poprawione: zamek w Kórniku (godziny sezonu niskiego,
# koniec sezonu 14.12) i Szreniawa (zmiana na godziny zimowe 24.10).
for _a in ATTRACTIONS:
    if _a["slug"] in ("biskupin", "grod-pobiedziska", "katedra-gniezno"):
        _a["checked"] = "24.10.2026"
    # Zamek w Kórniku: karta porównana ze stroną bkpan.poznan.pl 3.11.2026.
    if _a["slug"] == "kolegium-jezuickie":   # karta porównana z poznan.pl, Wikipedią, kierunkowo.pl i Visit Poznań 5.11.2026
        _a["checked"] = "05.11.2026"
    if _a["slug"] == "mury-miejskie":   # karta porównana z Wikipedią i Medieval Heritage 7.11.2026 (baszta armatnia zamiast bastionu, daty rozbiórki, ścieżka 2008)
        _a["checked"] = "07.11.2026"
    if _a["slug"] == "bazar":   # karta porównana z Wikipedią i poznan.pl 6.11.2026 (daty budowy, Orbis, rozbudowa Sławskiego, Paderewski, link i adres)
        _a["checked"] = "06.11.2026"
    if _a["slug"] == "biblioteka-raczynskich":   # karta porównana z bracz.edu.pl (historia, zbiory, kontakt, filie) i Wikipedią 5.11.2026
        _a["checked"] = "05.11.2026"
    if _a["slug"] == "wzgorze-sw-wojciecha":   # karta porównana z Wikipedią i kultura.poznan.pl 4.11.2026 (poprawiona urna Prądzyńskiego, dodana sekcja o kościele)
        _a["checked"] = "04.11.2026"
    if _a["slug"] == "giecz":   # nowa karta, dane z lednicamuzeum.pl (grafika godzin, cennik, historia) 4.11.2026
        _a["checked"] = "04.11.2026"
    if _a["slug"] in ("zamek-kornik", "gaspar", "ostrow-lednicki", "wpe-dziekanowice"):   # Lednica 3.11.2026: godziny (grafiki), ceny i kontakt wg lednicamuzeum.pl. Gaspar: karta porównana z Turturi, Visit Poznań i kultura.poznan.pl 3.11.2026.
        _a["checked"] = "03.11.2026"

# Przegląd sezonowy 30.10.2026: godziny i ceny porównane ze stronami oficjalnymi (zoo, ogród botaniczny, WMN, Fort VII,
# katedra, Czekolady, Gołuchów, WPN, Palmiarnia). Bez Muzeum Archeologicznego i Cytadeli (część danych strona nie podaje).
for _a in ATTRACTIONS:
    if _a["slug"] in ("nowe-zoo", "stare-zoo", "ogrod-botaniczny", "muzeum-powstania", "muzeum-uzbrojenia", "fort-vii",
                      "podziemia-katedry", "muzeum-czekolady", "zamek-goluchow", "wpn", "palmiarnia"):
        _a["checked"] = "30.10.2026"

# Przegląd treści 30.10.2026: porównane ze stronami oficjalnymi (godziny, ceny, kontakt, komunikaty).
_CHECKED_20261030 = {
    "brama-poznania", "centrum-szyfrow-enigma", "genius-loci", "fort-iva", "fort-va", "teatr-wielki", "cmentarz-zasluzonych-wielkopolan",
    "muzeum-czerwca-1956", "muzeum-sienkiewicza", "mieszkanie-illakowiczowny", "muzeum-pyry", "fotoplastykon", "muzeum-broni-pancernej",
    "muzeum-farmacji", "muzeum-historii-ubioru", "muzeum-prl", "muzeum-bizuterii-moja", "niewidzialna-ulica", "muzeum-armii-poznan",
    "rogalowe-muzeum", "termy-maltanskie", "park-wilsona", "fontanna-park-wilsona", "park-rataje", "mppp-gniezno",
    "palac-smielow", "muzeum-lesnictwa-goluchow", "skansen-miniatur-pobiedziska", "muzeum-archeologiczne", "muzeum-armii-poznan",
    "muzeum-narodowe", "muzeum-instrumentow", "muzeum-kultur-swiata", "muzeum-wojskowe", "fiedler", "akademia-lubranskiego", "muzeum-iluzji",
}
for _a in ATTRACTIONS:
    if _a["slug"] in _CHECKED_20261030:
        _a["checked"] = "30.10.2026"

# Szreniawa 30.10.2026: pełne porównanie karty ze stronami muzeum (godziny, bilety, kontakt, wystawy stałe).
for _a in ATTRACTIONS:
    if _a["slug"] == "szreniawa":
        _a["checked"] = "30.10.2026"
    # Ostrów Lednicki i WPE: tabela godzin 2026 (obrazek na lednicamuzeum.pl) i cennik porównane 24.10.2026, bez zmian w danych.
    if _a["slug"] == "parowozownia-wolsztyn":
        _a["checked"] = "24.10.2026"   # Wolsztyn: cennik (ważny od 1.01.2025), godziny zimowe 7:00–16:00 i telefon wg parowozowniawolsztyn.pl
    # Wolsztyn: pełne porównanie karty ze stroną parowozowni 26.10.2026 (godziny, ceny, rozkład, historia, zbiory).
    if _a["slug"] == "parowozownia-wolsztyn":
        _a["checked"] = "26.10.2026"
    # Makiety Dawnego Poznania: strona muzeum (pokazy, cennik) 24.10.2026; zima trwa do 30.04, nie do 31.03.
    if _a["slug"] == "makiety-dawnego-poznania":
        _a["checked"] = "24.10.2026"
    # Fort III: terminy wg poznan.pl, martwe źródło visitpoznan.pl usunięte 28.10.2026.
    if _a["slug"] == "fort-iii":
        _a["checked"] = "28.10.2026"
    # Pałac w Rogalinie: pełne porównanie karty ze stronami MNP (pałac, wizyta, galeria, powozownia, gabinet, park) i cennikiem PDF 2026, 29.10.2026.
    if _a["slug"] == "rogalin":
        _a["checked"] = "29.10.2026"

# Fort IVa: karta porównana z poznan.pl i Wikipedią 8.11.2026 (lata budowy, ul. Lechicka, bitwa 13/14.02.1945, Natura 2000).
for _a in ATTRACTIONS:
    if _a["slug"] == "fort-iva":
        _a["checked"] = "08.11.2026"

# Podziemia Katedry: karta porównana z poznan.pl, stroną katedry i Wikipedią 9.11.2026 (okrzeski, grobowce, wieża, godziny zimowe).
for _a in ATTRACTIONS:
    if _a["slug"] == "podziemia-katedry":
        _a["checked"] = "09.11.2026"

# Ogród Botaniczny UAM: karta porównana ze stronami ogrodu 9.11.2026 (godziny, kolekcje, liczby taksonów).
for _a in ATTRACTIONS:
    if _a["slug"] == "ogrod-botaniczny":
        _a["checked"] = "10.11.2026"

# Muzeum Leśnictwa w Gołuchowie: karta porównana ze stronami OKL (historia, Oficyna, Owczarnia, Dybul) 9.11.2026.
for _a in ATTRACTIONS:
    if _a["slug"] == "muzeum-lesnictwa-goluchow":
        _a["checked"] = "09.11.2026"

# Termy Maltańskie: karta porównana z cennikami i godzinami na termymaltanskie.com.pl 9.11.2026.
for _a in ATTRACTIONS:
    if _a["slug"] == "termy-maltanskie":
        _a["checked"] = "10.11.2026"
    if _a["slug"] == "stary-rynek":
        _a["checked"] = "11.11.2026"
    if _a["slug"] == "ostrow-tumski":
        _a["checked"] = "11.11.2026"

# Edycje 11.11.2026 (format numerów stacjonarnych, e-maile): data sprawdzenia ustawiona na dzień edycji.
for _a in ATTRACTIONS:
    if _a["slug"] in ("teatr-wielki", "puszcza-zielonka", "zagroda-zwierzat-goluchow", "zamek-cesarski", "biblioteka-raczynskich", "termy-maltanskie"):
        _a["checked"] = "11.11.2026"

# Puszcza Zielonka: opis jezior i LZD poprawiony wg uwag ZPKWW (mail z 9.11.2026), jeziora porównane z Wikipedią.
for _a in ATTRACTIONS:
    if _a["slug"] == "puszcza-zielonka":
        _a["checked"] = "11.11.2026"

# Wikipedia usunięta ze źródeł (11.11.2026) tam, gdzie wszystkie lata i liczby z karty są na oficjalnej stronie poznan.pl.
_WIKI_DROP = {"fontanna-prozerpiny", "studzienka-bamberki", "fontanna-apolla", "fontanna-neptuna", "fontanna-marsa",
              "pomnik-zygi-latarnika", "pomnik-kryptologow", "fontanna-lwow", "pomnik-powstancow", "pomnik-marcinkowskiego",
              "pomnik-janickiego", "pomnik-jana-pawla-ii", "pomnik-ratajskiego",
              "pomnik-koziolkow", "pomnik-starego-marycha", "pomnik-mickiewicza", "pomnik-panstwa-podziemnego", "pomnik-armii-poznan",
              "pomnik-15-pulku-ulanow", "fontanna-higiei", "fontanna-z-delfinami", "pomnik-kochanowskiego", "pomnik-cegielskiego",
              "pomnik-kosciuszki", "pomnik-komedy", "studzienka-taschnera", "fort-iva", "ostrow-tumski", "podziemia-katedry", "brama-poznania", "rogalowe-muzeum", "fara", "zamek-krolewski", "stary-browar"}
for _a in ATTRACTIONS:
    if _a["slug"] in _WIKI_DROP:
        _a["sources"] = [_s for _s in _a["sources"] if "wikipedia" not in _s[1].lower()]
        _a["checked"] = "11.11.2026"

# Termy Maltańskie: skrócone etykiety cen (12.11.2026).
for _a in ATTRACTIONS:
    if _a["slug"] == "termy-maltanskie":
        _a["checked"] = "12.11.2026"

# Jezioro Maltańskie: źródła oficjalne zamiast Wikipedii (12.11.2026).
for _a in ATTRACTIONS:
    if _a["slug"] in ("jezioro-maltanskie", "srodka", "rynek-srodecki", "zamek-cesarski", "muzeum-narodowe", "muzeum-powstania", "muzeum-archeologiczne", "muzeum-instrumentow", "muzeum-iluzji", "fotoplastykon", "cytadela", "pomnik-czerwca-1956"):
        _a["checked"] = "12.11.2026"


# Zamek w Gołuchowie: opis przepisany wyłącznie na podstawie dwóch stron MNP (muzeum-zamek-w-goluchowie, wizyta-muzeum-zamek-w-goluchowie) 10.11.2026.
for _a in ATTRACTIONS:
    if _a["slug"] == "zamek-goluchow":
        _a["checked"] = "10.11.2026"

# E-maile w boksie Kontakt (data_emails.py): tylko adresy z oficjalnych stron obiektów. Data „Sprawdzono” bez zmian.
from data_emails import EMAILS as _EMAILS
for _a in ATTRACTIONS:
    if _a["slug"] in _EMAILS and not _a.get("email"):
        _a["email"] = _EMAILS[_a["slug"]]

