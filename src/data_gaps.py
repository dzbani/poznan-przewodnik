# -*- coding: utf-8 -*-
"""Uzupełnienie luk (06.10.2026): pozycje z list poznan.pl i przewodników, których brakowało na stronie.
Fort III, Plac Wolności, Collegium Minus, Domki budnicze, Cmentarz Zasłużonych Wielkopolan.
Opisy streszczone własnymi słowami z poznan.pl, Wikipedii, visitpoznan.pl i publikacji UAM."""

P = "https://www.poznan.pl/mim/wortals/wortal,2024/"

GAPS = [
    dict(
        slug="fort-iii", cat="zabytki", name="Fort III",
        img="fort-iii", img_alt="Fort III na terenie Nowego Zoo, koszary i most nad fosą",
        short="Pruski fort główny z 1881 roku na terenie Nowego Zoo. Zwiedzanie z przewodnikiem w sezonie, także podziemi.",
        badge="Maj–wrzesień",
        status=None,
        lead="Fort III zbudowała armia pruska w latach 1877–1881. To jeden z 18 fortów artyleryjskich Twierdzy Poznań i zarazem jeden z dziewięciu fortów typu głównego. Leży na terenie Nowego Zoo przy ul. Krańcowej.",
        sections=[
            ("Co zobaczyć", [
                "Fort otacza sucha fosa o długości 850 m, głębokości 5,5 m i szerokości 9 m. Jej dostępu strzeże pięć kaponier. Na całej długości czoła i barków ciągnie się wał artyleryjski z remizami na 21 dział kalibru 15 i 12 cm.",
                "Wjazdu bronił blokhauz i most zwodzony. W części centralnej są dwa dziedzińce rozdzielone nasypem poterny, która łączy dwukondygnacyjne koszary z podwalnią.",
                "Trasa obejmuje część podziemną i naziemną. Stała wystawa opowiada o historii Twierdzy Poznań, w koszarach można zobaczyć, jak żyli żołnierze, a na wale stoi pancerna kopuła obserwacyjna i stanowisko z śladami łoża największego działa twierdzy, o zasięgu 7700 m.",
                "W podziemiach panuje stała temperatura około 12 °C. Jest tam duża prochownia na 35 ton czarnego prochu i kaponiera barkowa z murami grubymi na ponad 2,5 m. Korytarze oświetlają lampy naftowe.",
            ]),
            ("Historia", [
                "W 1889 roku fort wzmocniono, dobudowując na barkach baterie dla dodatkowych dział. Kolejne modernizacje przyniosły pancerne stanowiska obserwacyjne piechoty i artylerii.",
            ]),
            ("Warto wiedzieć", [
                "Fort leży w granicach Nowego Zoo, więc oprócz biletu na fort potrzebny jest bilet do Zoo. Przewodnicy czekają przy bramie od ulicy Krańcowej 81. Zwiedzanie bez biletu do Zoo jest możliwe po wcześniejszym umówieniu się z organizatorem.",
                "Trasa trwa około godziny. Na zwiedzanie nie obowiązują zapisy. Fort przygotowało do zwiedzania Poznańskie Towarzystwo Przyjaciół Fortyfikacji.",
                "Bilety na fort sprzedaje się przy wejściu do fortu, 200 m od kas Zoo, w dni zwiedzania od 10:30.",
                "Dwa źródła różnią się co do terminów i godzin wejść: portal visitpoznan.pl (aktualizacja 5.08.2026) podaje niedziele i święta, wejścia o 13:00 i 15:00, a portal miasta soboty, niedziele i święta, wejścia o 11:00, 12:30, 14:00, 15:30 i 17:00. Pewne jest tylko, że fort zwiedza się z przewodnikiem w niedziele i święta od maja do września. Przed wizytą najlepiej zadzwonić.",
            ]),
        ],
        address="ul. Krańcowa 81, 61-070 Poznań (teren Nowego Zoo)",
        hours=[
            ("Sezon", "maj–wrzesień"),
            ("Niedziele i święta", "zwiedzanie z przewodnikiem; godziny wejść źródła podają różnie, patrz „Warto wiedzieć”"),
            ("Soboty", "tylko wg poznan.pl, sprawdź telefonicznie"),
        ],
        tickets=[
            ("Fort, normalny", "8 zł"),
            ("Fort, ulgowy", "6 zł"),
            ("Z Poznańską Kartą Turystyczną", "50% rabatu"),
            ("Bilet do Zoo", "wymagany osobno"),
        ],
        phone="+48 501 302 909",
        www=("visitpoznan.pl", "https://visitpoznan.pl/dni-twierdzy-poznan-fort-iii"),
        credit="fort-iii",
        sources=[
            ("poznan.pl: Fort III", P + "fortyfikacje,poi,2575/fort-iii,51119.html"),
            ("visitpoznan.pl: Fort III (praktyczne informacje)", "https://visitpoznan.pl/dni-twierdzy-poznan-fort-iii"),
        ],
        checked="06.10.2026",
    ),
    dict(
        slug="plac-wolnosci", cat="zabytki", name="Plac Wolności",
        img="plac-wolnosci", img_alt="Fontanna Wolności na placu Wolności w Poznaniu",
        short="Reprezentacyjny plac z Fontanną Wolności, otoczony Bazarem, Muzeum Narodowym i Biblioteką Raczyńskich.",
        badge="Bezpłatnie",
        status=None,
        lead="Plac Wolności to prostokątny plac o wymiarach 85 na 205 m, na zachód od średniowiecznego centrum. Poznaniacy mówią o nim gwarowo „Plajta”. To dziś salon miasta, a zimą miejsce Betlejemu Poznańskiego.",
        sections=[
            ("Historia", [
                "W 1798 roku miasto odkupiło teren za 2500 talarów i zniwelowało wzgórze zwane Muszą Górą, by urządzić plac. Nazwano go Placem Wilhelmowskim, na cześć króla pruskiego Fryderyka Wilhelma III.",
                "26 stycznia 1919 roku żołnierze wielkopolscy i gen. Józef Dowbor-Muśnicki złożyli tu uroczystą przysięgę. W kwietniu 1919 roku usunięto z placu niemieckie pomniki, a w czerwcu plac dostał dzisiejszą nazwę.",
            ]),
            ("Co zobaczyć", [
                "Fontannę Wolności, uruchomioną w 2012 roku na wschodnim krańcu placu.",
                "Fontannę Higiei na północnej stronie, obok Biblioteki Raczyńskich.",
                "Zabytki wokół placu: Muzeum Narodowe, Hotel Bazar i Biblioteka Raczyńskich oraz zabytkowe kamienice i domy handlowe.",
                "Cztery platany klonolistne, które w 2023 roku objęto ochroną jako pomniki przyrody.",
                "W kamienicy Towarzystwa Ubezpieczeniowego Union z lat 1910–1911 (plac Wolności 14) działa jedna z najstarszych czynnych wind w Polsce.",
            ]),
            ("Warto wiedzieć", [
                "Pod płytą placu mieści się trzypoziomowy parking na ponad 500 samochodów, otwarty w 2006 roku.",
                "Na placu odbywają się jarmarki i wydarzenia sezonowe, m.in. Betlejem Poznańskie (w sezonie 2026/27 od 20 listopada do 6 stycznia) oraz Jarmark Wielkanocny. Aktualne terminy są w kalendarzu wydarzeń.",
            ]),
        ],
        address="plac Wolności, 61-739 Poznań",
        hours=[("Plac", "dostępny całą dobę")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None,
        www=("Wikipedia", "https://pl.wikipedia.org/wiki/Plac_Wolności_w_Poznaniu"),
        credit="plac-wolnosci",
        sources=[
            ("Wikipedia: Plac Wolności w Poznaniu", "https://pl.wikipedia.org/wiki/Plac_Wolności_w_Poznaniu"),
        ],
        checked="06.10.2026",
    ),
    dict(
        slug="collegium-minus", cat="zabytki", name="Collegium Minus",
        img="aula-uam", img_alt="Collegium Minus, siedziba władz Uniwersytetu im. Adama Mickiewicza",
        short="Neorenesansowy gmach z 1910 roku, siedziba rektora UAM. W Auli odbywają się koncerty Filharmonii Poznańskiej.",
        badge="Z zewnątrz bezpłatnie",
        status=None,
        lead="Collegium Minus to gmach zbudowany dla niemieckiej Akademii Królewskiej, od 1919 roku siedziba władz Uniwersytetu im. Adama Mickiewicza. Frontem stoi do ulicy Wieniawskiego, a przylega do ulicy Święty Marcin.",
        sections=[
            ("Historia", [
                "Projekt Edwarda Fürstenau powstał w latach 1905–1906. Prace budowlane trwały od wiosny 1907 roku: część dydaktyczną oddano 1 listopada 1909 roku, a aulę otwarto uroczyście 18 stycznia 1910 roku.",
                "Gmach był demonstracją niemieckiej obecności wobec polskiej społeczności Poznania. Akademii służył nieco ponad cztery lata, bo w czasie I wojny światowej mieścił lazaret wojskowy.",
                "W kwietniu 1919 roku władze polskie przekazały budynek tworzonej uczelni. Nazwę Collegium Minus zaproponował 5 kwietnia 1919 roku prof. Michał Sobeski, a 7 maja 1919 roku uroczyście otwarto Uniwersytet Poznański.",
            ]),
            ("Co zobaczyć", [
                "Neorenesansową elewację z portykami i wysokimi szczytami od strony ulicy Wieniawskiego.",
                "Aulę Uniwersytecką: sala ma około 580 m², 33 m długości i 17,5 m szerokości, a nad sceną 14 m wysokości. Słynie z akustyki. Pierwotnie dominowały w niej 35-głosowe organy firmy Völkner z Bydgoszczy.",
                "Salę Lubrańskiego, zwaną Małą Aulą, z kopią obrazu Jana Matejki „Założenie Akademii Lubrańskiego” (oryginał z 1886 roku).",
            ]),
            ("Warto wiedzieć", [
                "To czynny gmach uczelni, więc wnętrz nie zwiedza się jak muzeum. Do Auli najłatwiej wejść na koncert Filharmonii Poznańskiej lub inne wydarzenie. Repertuar jest w zakładce „Teatry i koncerty”.",
            ]),
        ],
        address="ul. Wieniawskiego 1, 61-712 Poznań",
        hours=[
            ("Z zewnątrz", "dostępny całą dobę"),
            ("Aula", "w czasie koncertów i wydarzeń"),
        ],
        tickets=[
            ("Oglądanie z zewnątrz", "bezpłatnie"),
            ("Koncerty w Auli", "bilety sprzedaje organizator"),
        ],
        phone=None,
        www=("amu.edu.pl", "https://amu.edu.pl/"),
        credit="aula-uam",
        sources=[
            ("Wikipedia: Collegium Minus w Poznaniu", "https://pl.wikipedia.org/wiki/Collegium_Minus_w_Poznaniu"),
            ("G. Łukomski: Collegium Minus – świątynia nauki i sztuki (UAM)", "https://amu.edu.pl/__data/assets/pdf_file/0020/50537/Collegium-Minus.pdf"),
        ],
        checked="06.10.2026",
    ),
    dict(
        slug="domki-budnicze", cat="zabytki", name="Domki budnicze",
        img="domki-budnicze", img_alt="Kolorowe domki budnicze na Starym Rynku w Poznaniu",
        short="Wąskie renesansowe kamieniczki z podcieniami po południowej stronie ratusza, dawne budy rybne i kramy.",
        badge="Bezpłatnie",
        status=None,
        lead="Domki budnicze stoją po południowej stronie ratusza, w bloku śródrynkowym. To relikt dawnej zabudowy handlowej: w średniowieczu stały tu drewniane budy, w których sprzedawano śledzie, sól, świece i pochodnie.",
        sections=[
            ("Historia", [
                "W 1418 roku władze miasta ustanowiły tu 17 bud rybnych. W XVI wieku na ich miejscu wzniesiono wąskie kamieniczki z renesansowymi podcieniami, których arkady wspierają się na piaskowcowych kolumienkach. W dolnych częściach mieściły się kramy, wyżej izby mieszkalne.",
                "Na głowicy kolumny kamienicy nr 11 można odczytać datę 1535. Domki zamyka od południa kamieniczka z 1538 roku zwana Kancelarią Miejską lub Domem Pisarzy, dziś siedziba Towarzystwa Miłośników Miasta Poznania, założonego w 1922 roku przez prezydenta Cyryla Ratajskiego.",
                "W czasie II wojny światowej zabudowa została niemal zupełnie zniszczona. Odbudowano ją w latach 1953–1961 z polichromiami wg projektu Zbigniewa Bednarowicza.",
            ]),
            ("Co zobaczyć", [
                "Godło cechu budników na kamienicy nr 17: śledź i trzy palmy. Na głowicy kolumny kamienicy nr 24 jest gmerk dawnych właścicieli.",
                "Pod arkadami poznańscy plastycy sprzedają swoje prace, najczęściej widoki Starego Miasta. Mieszczą się tam też sklepy z pamiątkami.",
                "Na tyłach kamieniczek biegnie ulica Kurzanoga, która prawdopodobnie przypomina dawną kamienicę o tej nazwie.",
            ]),
        ],
        address="Stary Rynek, 61-772 Poznań (po południowej stronie ratusza)",
        hours=[
            ("Arkady", "dostępne całą dobę"),
            ("Sklepy i galerie", "według godzin poszczególnych lokali"),
        ],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None,
        www=("poznan.pl", P + "zabytki,poi,2572/domki-budnicze,41222.html"),
        credit="domki-budnicze",
        sources=[
            ("poznan.pl: Domki budnicze", P + "zabytki,poi,2572/domki-budnicze,41222.html"),
            ("Wikipedia: Domki budnicze w Poznaniu", "https://pl.wikipedia.org/wiki/Domki_budnicze_w_Poznaniu"),
        ],
        checked="06.10.2026",
    ),
    dict(
        slug="cmentarz-zasluzonych-wielkopolan", cat="zabytki", name="Cmentarz Zasłużonych Wielkopolan",
        img="cmentarz-zasluzonych-wielkopolan", img_alt="Zabytkowy nagrobek na Cmentarzu Zasłużonych Wielkopolan",
        short="Najstarsza poznańska nekropolia na Wzgórzu św. Wojciecha. Groby gen. Taczaka, prezydentów miasta i premiera Mikołajczyka.",
        badge="Bezpłatnie",
        status=None,
        lead="Cmentarz na północnym stoku Wzgórza św. Wojciecha to najstarsza nekropolia w Poznaniu. Założono go na początku XIX wieku jako cmentarz parafii farnej, a od 1948 roku jest miejscem spoczynku zasłużonych Wielkopolan.",
        sections=[
            ("Historia", [
                "Miejsce pod cmentarz wyznaczono w 1808 roku, a najstarszy zachowany nagrobek nosi datę 1813. Od końca XIX wieku, gdy parafia dostała nowy cmentarz, nazywano go starofarnym.",
                "W 1948 roku zdecydowano, że stary cmentarz stanie się nekropolią zasłużonych Wielkopolan. W 1959 roku przeniesiono tu szczątki 79 osób z likwidowanego cmentarza przy ul. Towarowej. 11 stycznia 1971 roku parafia przekazała nekropolę władzom świeckim.",
            ]),
            ("Co zobaczyć", [
                "Barokową figurę Matki Boskiej z 1771 roku, przeniesioną z klasztoru reformatów na Śródce.",
                "Nagrobek Anieli z Liszkowskich Dembińskiej, zmarłej w wieku 20 lat, wyrzeźbiony w 1889 roku w Paryżu przez Władysława Marcinkowskiego.",
                "Groby m.in. gen. Stanisława Taczaka, pierwszego dowódcy powstania wielkopolskiego, premiera Stanisława Mikołajczyka, prezydentów miasta Szymona Wronieckiego, Jarogniewa Drwęskiego i Cyryla Ratajskiego oraz pianisty Raula Koczalskiego. Hipolita Cegielskiego upamiętnia symboliczny grób.",
                "Kamień poświęcony „Wielkopolanom, którzy nie wrócili z gór”, ustawiony w 1994 roku przez Polskie Towarzystwo Tatrzańskie.",
            ]),
            ("Warto wiedzieć", [
                "Pozornie pozbawiona nagrobków polana u podnóża wzgórza to masowa mogiła ofiar epidemii cholery z lat 1831–1873.",
                "Godziny wejścia podaje portal poznan.pl. Na tej samej stronie jest wyszukiwarka grobów. To czynny cmentarz, więc obowiązuje zachowanie właściwe dla takiego miejsca.",
            ]),
        ],
        address="ul. Księcia Józefa, 61-746 Poznań (Wzgórze św. Wojciecha)",
        hours=[("Wejście", "codziennie 10:00–18:00")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None,
        www=("poznan.pl", P + "parki,poi,3338/cmentarz-zasluzonych-wielkopolan,51945.html"),
        credit="cmentarz-zasluzonych-wielkopolan",
        sources=[
            ("poznan.pl: Cmentarz Zasłużonych Wielkopolan", P + "parki,poi,3338/cmentarz-zasluzonych-wielkopolan,51945.html"),
            ("Wikipedia: Cmentarz Zasłużonych Wielkopolan", "https://pl.wikipedia.org/wiki/Cmentarz_Zasłużonych_Wielkopolan"),
        ],
        checked="06.10.2026",
    ),
]
