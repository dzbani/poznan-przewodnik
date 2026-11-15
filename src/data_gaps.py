# -*- coding: utf-8 -*-
"""Uzupełnienie luk (06.10.2026): pozycje z list poznan.pl i przewodników, których brakowało na stronie.
Fort III, Plac Wolności, Collegium Minus, Domki budnicze, Cmentarz Zasłużonych Wielkopolan.
Opisy streszczone własnymi słowami z poznan.pl, Wikipedii, visitpoznan.pl i publikacji UAM."""

P = "https://www.poznan.pl/mim/wortals/turystyka/"

GAPS = [
    dict(
        slug="fort-iii", cat="zabytki", name="Fort III",
        img="fort-iii", img_alt="Fort III na terenie Nowego Zoo, koszary i most nad fosą",
        short="Pruski fort główny z 1881 roku na terenie Nowego Zoo. Zwiedzanie z przewodnikiem w sezonie, także podziemi.",
        badge="Maj–wrzesień",
        status=None,
        lead="Fort III zbudowała armia pruska w latach 1877–1881. To jeden z 18 fortów artyleryjskich Twierdzy Poznań i zarazem jeden z dziewięciu fortów typu głównego. Nosił nazwę Graf Kirchbach. Leży na terenie Nowego Zoo przy ul. Krańcowej.",
        sections=[
            ("Co zobaczyć", [
                "Fort otacza sucha fosa o długości 850 m, głębokości 5,5 m i szerokości 9 m. Jej dostępu strzeże pięć kaponier: czołowa, dwie barkowe i dwie izby bojowe wewnątrz koszar. Na całej długości czoła i barków ciągnie się wał artyleryjski z remizami na 21 dział kalibru 15 i 12 cm.",
                "Wjazdu bronił blokhauz i most zwodzony przed bramą. W części centralnej są dwa dziedzińce rozdzielone nasypem poterny, która łączy dwukondygnacyjne koszary w szyjowej części fortu z podwalnią.",
                "Trasa obejmuje część podziemną i naziemną. Stała wystawa opowiada o historii Twierdzy Poznań, w koszarach można zobaczyć, jak żyli żołnierze, gdzie stały armaty i jakiej używano amunicji. Na wale stoi pancerna kopuła obserwacyjna i stanowisko z dobrze zachowanymi śladami łoża nadbrzeżnego, największego działa fortecznego Twierdzy Poznań, o zasięgu 7700 m.",
                "W podziemiach panuje stała temperatura około 12 °C. Jest tam wielka prochownia na 35 ton czarnego prochu i kaponiera barkowa z murami grubymi na ponad 2,5 m, która strzegła dostępu do fosy. Podziemia oświetlają, jak w czasach budowy fortu, lampy naftowe.",
            ]),
            ("Historia", [
                "Na wale artyleryjskim zbudowano murowaną działobitnię dla armaty pierścieniowej 15 cm na łożu nadbrzeżnym. W końcowej fazie budowy, w 1881 roku, pośrodku czoła powstał krótki odcinek wału dla piechoty.",
                "W latach 1887–1890 wzmocniono mury i stropy budowli podziemnych. W 1889 roku po bokach fortu zbudowano baterie dla dodatkowych dział, ze schronami amunicyjnymi.",
                "Około 1892 roku zainstalowano dwie stalowe obrotowe kopuły obserwacyjne piechoty typu W.T.90, a w pierwszych latach XX wieku kopułę obserwatora artylerii typu W.T.Neu. Drobniejsze modernizacje prowadzono do wybuchu I wojny światowej.",
                "W czasie II wojny światowej zadaszono fosy, aby umieścić w nich warsztaty i magazyny fabryki samolotów Focke-Wulf. Po wojnie rozpoczęto rozbiórkę koszar, ale pozostała część budowli nie została naruszona.",
            ]),
            ("Warto wiedzieć", [
                "Fort leży w granicach Nowego Zoo, więc oprócz biletu na fort potrzebny jest bilet do Zoo. Trasę przygotowało w porozumieniu z dyrektorem Zoo Poznańskie Towarzystwo Przyjaciół Fortyfikacji.",
                "Bilety na fort sprzedaje się przy wejściu do fortu, 200 m od kas Zoo, w dni zwiedzania od 10:30. Zwiedzanie trwa około godziny, a fotografowanie jest bezpłatne.",
                "Wnętrze można zwiedzać tylko pod opieką przewodnika. Część budowli jest uszkodzona, opuszczona i potencjalnie niebezpieczna, a fort jest częściowo używany jako magazyn.",
                "Portal miasta podaje zwiedzanie od maja do września w soboty, niedziele i święta, z wejściami o 11:00, 12:30, 14:00, 15:30 i 17:00. Grupy zorganizowane mogą umówić się także na inne godziny i w dni powszednie. Poza sezonem źródła nie podają regularnych wejść, więc terminy warto sprawdzić telefonicznie przed wizytą.",
            ]),
        ],
        address="ul. Krańcowa 81, 61-070 Poznań (teren Nowego Zoo)",
        hours=[
            ("Sezon", "maj–wrzesień; poza sezonem źródła nie podają regularnych wejść"),
            ("Soboty, niedziele i święta", "zwiedzanie z przewodnikiem, wejścia wg poznan.pl o 11:00, 12:30, 14:00, 15:30 i 17:00; sprawdź telefonicznie"),
            ("Sprzedaż biletów", "przy wejściu do fortu, w dni zwiedzania od 10:30"),
        ],
        tickets=[
            ("Fort, normalny", "8 zł"),
            ("Fort, ulgowy", "6 zł"),
            ("Z Poznańską Kartą Turystyczną", "50% rabatu"),
            ("Fotografowanie", "bezpłatnie"),
            ("Bilet do Zoo", "wymagany osobno"),
        ],
        phone="+48 501 445 566",
        www=("poznan.pl", "https://www.poznan.pl/mim/wortals/turystyka/fortyfikacje,poi,2575/-,51119.html"),
        credit="fort-iii",
        sources=[
            ("poznan.pl: Fort III", "https://www.poznan.pl/mim/wortals/turystyka/fortyfikacje,poi,2575/-,51119.html"),
            ("Poznański Szlak Forteczny: Fort III", "http://www.twierdza.poznan.pl/fort3/"),
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
        img="collegium-minus", img_alt="Collegium Minus z góry: front Auli z dwiema wieżyczkami i boczne skrzydło gmachu, na pierwszym planie pomnik",
        short="Gmach w stylu holenderskiego renesansu z lat 1907–1910, siedziba rektora UAM. W Auli odbywają się koncerty Filharmonii Poznańskiej.",
        badge="Z zewnątrz bezpłatnie",
        status=None,
        lead="Collegium Minus to gmach zbudowany dla niemieckiej Akademii Królewskiej, od 1919 roku siedziba władz Uniwersytetu im. Adama Mickiewicza. Frontem stoi do ulicy Wieniawskiego, a przylega do ulicy Święty Marcin i wyraźnie nad nią góruje.",
        sections=[
            ("Historia", [
                "Akademia Królewska powstała w Poznaniu 4 listopada 1903 roku z inicjatywy władz niemieckich. Nie miała własnej siedziby i zajęcia odbywały się m.in. w Muzeum Cesarza Fryderyka oraz w wynajętym gmachu szkoły przy ulicy Młyńskiej. Budowa siedziby była, jak pisze prof. Grzegorz Łukomski, otwartym wyzwaniem i swego rodzaju demonstracją wobec polskiej społeczności Poznania.",
                "Projekt Edwarda Fürstenau, architekta i teologa, powstał w latach 1905–1906. Prace budowlane trwały od wiosny 1907 roku: część dydaktyczną oddano 1 listopada 1909 roku, a aulę otwarto uroczyście 18 stycznia 1910 roku. W budowie wzięło udział niemal 30 firm z Poznania i Berlina, a koszt obliczono na 1 600 000 marek.",
                "Akademii gmach służył nieco ponad cztery lata, bo w czasie I wojny światowej mieścił lazaret wojskowy. Wiosną 1920 roku pożar zniszczył wysoki dach nad aulą i wieżę po lewej stronie fasady.",
                "W kwietniu 1919 roku Komisariat Naczelnej Rady Ludowej przekazał budynek tworzonej uczelni polskiej. Nazwę Collegium Minus zaproponował 5 kwietnia 1919 roku prof. Michał Sobeski, a 7 maja 1919 roku uroczyście otwarto Uniwersytet Poznański.",
                "W latach 1941–1945 w gmachu mieściły się władze niemieckiego „Uniwersytetu Rzeszy”. Walki o Poznań w lutym 1945 roku nie wyrządziły budynkowi dużych szkód. W auli toczył się proces Artura Greisera, namiestnika Kraju Warty, którego 10 lipca 1946 roku Najwyższy Trybunał Narodowy skazał na karę śmierci.",
            ]),
            ("Co zobaczyć", [
                "Gmach w stylu holenderskiego (niemieckiego) renesansu, złożony z dwóch części: budynku naukowego i reprezentacyjnej auli.",
                "Aulę Uniwersytecką: sala ma 580 m², 33 m długości i 17,5 m szerokości, a nad sceną 14 m wysokości. Słynie z doskonałej akustyki. Pierwotnie zaprojektowano ją na 1100 miejsc, dziś jest nieco ponad 800 krzeseł. Sklepienie zdobi od 1947 roku polichromia Wacława Taranczewskiego. Pierwotnie dominowały w niej 35-rejestrowe organy z bogatym prospektem, dzieło mistrza Völknera z Bydgoszczy.",
                "Salę Lubrańskiego, zwaną Małą Aulą, na pierwszym piętrze, dawną recepcję łączącą obie części gmachu. Zdobi ją kopia obrazu Jana Matejki „Założenie Akademii Lubrańskiego w Poznaniu”, wykonana przez J. Bukowskiego. Oryginał z 1886 roku jest w Muzeum Narodowym w Poznaniu. Dziś odbywają się tu m.in. posiedzenia senatu akademickiego.",
            ]),
            ("Aula i muzyka", [
                "Od 18 listopada 1947 roku aula jest także salą koncertową Państwowej Filharmonii Poznańskiej. Od 1952 roku co pięć lat odbywają się w niej Międzynarodowe Konkursy Skrzypcowe im. Henryka Wieniawskiego, przeniesione do Poznania z Warszawy m.in. ze względu na wyjątkowe walory akustyczne auli.",
            ]),
            ("Warto wiedzieć", [
                "To czynny gmach uczelni, siedziba rektoratu i Gabinetu Rektora, więc wnętrz nie zwiedza się jak muzeum. Do Auli najłatwiej wejść na koncert Filharmonii Poznańskiej lub inne wydarzenie. Repertuar jest w zakładce „Teatry i koncerty”.",
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
        phone="+48 61 829 40 00",
        www=("amu.edu.pl", "https://amu.edu.pl/"),
        credit="collegium-minus",
        sources=[
            ("UAM: Kontakt (Collegium Minus, Rektorat UAM)", "https://amu.edu.pl/uniwersytet/kontakt"),
            ("G. Łukomski: Collegium Minus – świątynia nauki i sztuki (UAM)", "https://amu.edu.pl/__data/assets/pdf_file/0020/50537/Collegium-Minus.pdf"),
        ],
        checked="06.10.2026",
    ),
    dict(
        slug="domki-budnicze", cat="zabytki", name="Domki budnicze",
        img="domki-budnicze", img_alt="Rząd kolorowych domków budniczych z arkadami na Starym Rynku w Poznaniu, z kramami i spacerującymi ludźmi; w tle wieża ratusza",
        short="Wąskie kamieniczki z podcieniami w południowej części Starego Rynku, dawne budy śledziowe i kramy.",
        badge="Bezpłatnie",
        status=None,
        lead="Domki budnicze to unikatowy zabytek dawnej zabudowy handlowej, położony w południowej części zabudowy śródrynkowej Starego Rynku. Już w XIII wieku stały tu budy śledziowe, w których oprócz ryb sprzedawano sól, świece i pochodnie oraz niektóre przedmioty codziennego użytku.",
        sections=[
            ("Historia", [
                "W końcu XV i w XVI wieku na miejscu drewnianych bud wybudowano wąskie, często jednookienne, murowane kamieniczki z kramami na dole i izbami mieszkalnymi na wyższych kondygnacjach. Zespół domków budniczych wznieśli w pierwszej połowie XVI wieku indywidualni właściciele poszczególnych działek.",
                "Wejścia do kramów chroniły podcienia, które w XIX wieku zamurowano. Podczas odbudowy po zniszczeniach z 1945 roku przywrócono im pierwotny wygląd.",
                "Zespół zamyka od południa kamieniczka z 1538 roku zwana Kancelarią Miejską lub Domem Pisarzy. Do XVIII wieku mieszkał w niej pisarz miejski, a dziś jest siedzibą Towarzystwa Miłośników Miasta Poznania.",
            ]),
            ("Co zobaczyć", [
                "Arkady podcieni, wspierające się na kolumienkach z piaskowca. Większość z nich jest autentyczna, a na kolumnie domu nr 11 wyryta jest data 1535.",
                "Pod arkadami poznańscy plastycy sprzedają swoje prace, najczęściej widoki Starego Miasta.",
            ]),
        ],
        address="Stary Rynek, 61-772 Poznań (południowa część zabudowy śródrynkowej)",
        hours=[
            ("Podcienia", "oglądanie z zewnątrz, cały czas"),
        ],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None,
        www=("poznan.pl", "https://www.poznan.pl/mim/wortals/turystyka/-,p,37,51,97.html"),
        credit="domki-budnicze",
        sources=[
            ("poznan.pl: Domki budnicze", "https://www.poznan.pl/mim/wortals/turystyka/-,p,37,51,97.html"),
            ("poznan.pl: Stary Rynek", "https://www.poznan.pl/mim/wortals/turystyka/stary-rynek,p,37,51,103.html"),
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
