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
        short="Najstarszy poznański cmentarz na Wzgórzu św. Wojciecha. Groby gen. Taczaka, prezydentów miasta i Marcelego Mottego.",
        badge="Bezpłatnie",
        status=None,
        lead="Cmentarz Zasłużonych Wielkopolan leży na północnym stoku Wzgórza św. Wojciecha. To najstarszy z ponad 20 poznańskich cmentarzy: powstał w latach 1808–1810 jako cmentarz parafii farnej św. Marii Magdaleny, a rangę cmentarza zasłużonych uzyskał w 1948 roku.",
        sections=[
            ("Historia", [
                "Cmentarz powstał dzięki staraniom Stanisława Kolanowskiego, znanego poznańskiego piwowara, opodal cmentarza poznańskich protestantów z końca XVI wieku. Przez ponad 100 lat chowano tu wiernych parafii farnej, a w nieoznaczonych zbiorowych mogiłach spoczęły ofiary epidemii cholery. Od końca XIX wieku, gdy parafia dostała nowy cmentarz przy dzisiejszej ulicy Grunwaldzkiej, nazywano go starofarnym.",
                "Podczas walk o pobliską Cytadelę w 1945 roku zniszczeniu bezpowrotnie uległo wiele wartościowych nagrobków. Po II wojnie światowej rozważano likwidację cmentarza i zamianę go w park, ale na przełomie lat 40. i 50. zdecydowano o urządzeniu tu Cmentarza Zasłużonych Wielkopolan. Prochy wielu osób przeniesiono tu z innych cmentarzy w latach 1959–62, a nekropolię objęto ochroną konserwatorską.",
                "Razem z Kryptą Zasłużonych na Wzgórzu św. Wojciecha cmentarz tworzy narodowy panteon Wielkopolski.",
            ]),
            ("Co zobaczyć", [
                "Barokową figurę Matki Boskiej z 1771 roku, ustawioną niedaleko głównego wejścia. W 1829 roku przeniesiono ją sprzed dawnego klasztoru Reformatów na Śródce.",
                "Pomnik Anieli z Liszkowskich Dembińskiej (zm. 1888), wykonany w 1889 roku w Paryżu przez Władysława Marcinkowskiego. Najstarsze zachowane nagrobki pochodzą z 1813 i 1815 roku.",
                "Groby m.in. gen. Stanisława Taczaka, pierwszego dowódcy powstania wielkopolskiego, prezydentów miasta Szymona Wronieckiego, Jarogniewa Drwęskiego i Cyryla Ratajskiego, premiera RP Stanisława Mikołajczyka, Marcelego Mottego, pianisty Raula Koczalskiego, aktorki Nuny Młodziejowskiej-Szczurkiewiczowej i rzeźbiarza Władysława Marcinkowskiego. Hipolita Cegielskiego upamiętnia symboliczny grób.",
                "Kamień poświęcony „Wielkopolanom, którzy nie wrócili z gór”, ustawiony w 1994 roku przez Polskie Towarzystwo Tatrzańskie.",
                "Spoczywają tu weterani wojen napoleońskich i powstań narodowych, społecznicy oraz ludzie nauki i kultury, m.in. lekarze Ludwik Gąsiorowski (1807–63), Tomasz Drobnik (1858–1901), Bolesław Krysiewicz (1862–1932) i Ireneusz Wierzejewski (1881–1930) oraz naukowcy: filolog Bolesław Erzepki (1852–1932), historyk Józef Łukaszewicz (1799–1873) i botanik Józef Paczoski (1864–1942).",
                "Pochowani zostali tu także ojcowie i bracia karmelici bosi, żyjący w latach 1618–1801 w pobliskim klasztorze św. Józefa.",
                "Zachowane nagrobki są przeglądem ponad stuletnich dziejów rodzimej sztuki sepulkralnej.",
            ]),
            ("Warto wiedzieć", [
                "Najniżej położona część cmentarza, bez nagrobków, kryje szczątki ofiar epidemii cholery (według Zarządu Zieleni Miejskiej z 1831 roku, według poznan.pl z lat 1831–1878). Zarząd Zieleni Miejskiej podaje, że cmentarz ma 2 ha, a w 577 mogiłach pochowano 868 osób. Poznan.pl podaje 889 osób w 575 mogiłach, a na jednej ze stron powierzchnię 1,8 ha.",
                "To czynny cmentarz, nadal wykorzystywany do pochówku wybitnych obywateli związanych z Wielkopolską, więc obowiązuje zachowanie właściwe dla takiego miejsca. Zwiedzać go można codziennie od 10 do 18, a przez całą dobę jest objęty nadzorem. Wyszukiwarka grobów jest na stronie poznan.pl.",
                "Dojazd wg poznan.pl: autobusy 168, 169 i 171 do przystanku „Urząd Marszałkowski” albo samochodem do ulicy Księcia Józefa.",
                "Administratorem jest Zarząd Zieleni Miejskiej w Poznaniu (ul. Strzegomska 3, tel. 61 646 33 44, kancelaria@zzmpoznan.pl). W porozumieniu z Miejskim Konserwatorem Zabytków prowadzi on działania na rzecz zachowania tego dziedzictwa.",
            ]),
        ],
        address="ul. Księcia Józefa, Wzgórze św. Wojciecha, Poznań",
        hours=[("Zwiedzanie", "codziennie 10:00–18:00")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone="+48 61 646 33 44",
        www=("poznan.pl", "https://www.poznan.pl/mim/wortals/turystyka/parki,poi,3338/cmentarz-zasluzonych-wielkopolan,51945.html"),
        credit="cmentarz-zasluzonych-wielkopolan",
        sources=[
            ("poznan.pl: Cmentarz Zasłużonych Wielkopolan (Znajdź grób bliskich)", "https://www.poznan.pl/mim/main/-,p,1943,12925.html"),
            ("poznan.pl: Cmentarz Zasłużonych Wielkopolan (Odkryj Poznań)", "https://www.poznan.pl/mim/wortals/turystyka/parki,poi,3338/cmentarz-zasluzonych-wielkopolan,51945.html"),
            ("Zarząd Zieleni Miejskiej: „Poznańskie Powązki”", "https://zzmpoznan.pl/mim/wortals/zzm/news,9860/poznanskie-powazki,265514.html"),
        ],
        checked="06.10.2026",
    ),
]
