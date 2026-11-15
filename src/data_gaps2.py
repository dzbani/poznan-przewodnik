# -*- coding: utf-8 -*-
"""Uzupełnienie luk, część 2 (06.10.2026): Podziemia Katedry, Most Biskupa Jordana, Rynek Śródecki, Lasek Katyński.
Źródła: strona Katedry Poznańskiej, poznan.pl, Wikipedia. Opisy streszczone własnymi słowami."""

P = "https://www.poznan.pl/mim/wortals/turystyka/"

GAPS2 = [
    dict(
        slug="podziemia-katedry", cat="zabytki", name="Podziemia Katedry Poznańskiej",
        img="podziemia-katedry", img_alt="Relikty wczesnośredniowiecznego grobowca, tradycyjnie przypisywanego Bolesławowi Chrobremu, w podziemiach Katedry Poznańskiej",
        short="Relikty katedry przedromańskiej i romańskiej, pozostałości grobowców Mieszka I i Chrobrego oraz misa z X wieku.",
        badge="Sezonowo, płatne",
        status=None,
        lead="Pod Katedrą Poznańską zachowały się fragmenty wcześniejszych budowli, odkryte podczas badań archeologicznych prowadzonych przy odbudowie świątyni po II wojnie światowej. Można tu zobaczyć ślady dawnych katedr, także tej z czasów pierwszych Piastów.",
        sections=[
            ("Co zobaczyć", [
                "Fragmenty katedry przedromańskiej i romańskiej.",
                "Relikty grobowców, najprawdopodobniej pierwszych władców Polski: Mieszka I i Bolesława Chrobrego.",
                "Relikt misy z X wieku, być może chrzcielnicy, z której mógł przyjąć chrzest Mieszko I wraz z poddanymi.",
                "Lapidarium z fragmentami nagrobków, płyt i epitafiów oraz krypta, w której spoczywają arcybiskupi poznańscy.",
                "Przy wejściu wiszą plansze prof. Zofii Kurnatowskiej o dziejach katedry i Ostrowa Tumskiego, a podczas zwiedzania wyświetlany jest film.",
            ]),
            ("Historia odkryć", [
                "Główne odkrycia pochodzą z badań prowadzonych równolegle z odbudową katedry (1946–1956). Ujawniły one wcześniejsze fazy budowy świątyni, starsze od gotyku.",
            ]),
            ("Warto wiedzieć", [
                "Bilet kupuje się w punkcie obsługi turystycznej na terenie katedry lub w zakrystii. Katedra jest czynnym kościołem: nie zwiedza się jej podczas mszy, nabożeństw i koncertów, obowiązuje odpowiedni strój i cisza.",
                "Poza kryptami można wejść na wieżę widokową katedry. Więcej o samej katedrze i Ostrowie Tumskim jest na osobnej stronie.",
            ]),
        ],
        address="Ostrów Tumski 17, 61-109 Poznań",
        hours=[
            ("Sezon (1.03–15.11), dni powszednie", "9:00–16:00"),
            ("Sezon (1.03–15.11), niedziele", "14:00–18:00 (o ile nie ma dodatkowego nabożeństwa)"),
            ("Zima (16.11–koniec lutego)", "podziemia zamknięte (poznan.pl); sama katedra dla zwiedzających w dni powszednie 9:00–16:00"),
        ],
        tickets=[
            ("Normalny", "10 zł"),
            ("Ulgowy", "8 zł"),
            ("Rodzinny", "25 zł"),
            ("Wieża widokowa: normalny", "14 zł"),
            ("Wieża widokowa: ulgowy", "12 zł"),
            ("Wieża widokowa: rodzinny", "40 zł"),
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
        short="Kładka dla pieszych nad Cybiną między Śródką a Ostrowem Tumskim, zbudowana ze starego przęsła mostu św. Rocha na miejscu przeprawy z X wieku.",
        badge="Bezpłatnie",
        status=None,
        lead="Most Biskupa Jordana, dawniej zwany Cybińskim lub Śródeckim, stoi w miejscu historycznej przeprawy przez Cybinę między Śródką a Ostrowem Tumskim. Otwarto go 7 grudnia 2007 roku jako pierwszy etap reintegracji nadrzecznych obszarów Poznania. Jego konstrukcją jest przęsło dawnego mostu św. Rocha.",
        sections=[
            ("Historia przeprawy", [
                "Most przez wąską Cybinę budowano od czasu powstania pierwszych osad na Ostrowie Tumskim. W 2007 roku archeolodzy odkryli pod przyczółkiem 37 pali, niemal wyłącznie dębowych. Według analiz dendrochronologicznych most wzniósł prawdopodobnie w 979 roku Mieszko I, a naprawiano go w latach 987, 1006 i 1021, za Bolesława Chrobrego.",
                "Najstarszy zachowany widok mostu to plan Brauna i Hogenberga z 1618 roku. Drewniany most miał wtedy około 50 m długości i z powodu gnicia podpór trzeba go było wymieniać mniej więcej co 25 lat. Po lokacji miasta w 1253 roku utrzymywała go kuria biskupia, która pobierała myto.",
                "Pierwszy stały most żelazny oddano do użytku w lipcu 1905 roku. Po sześciu latach okazał się za słaby i rozebrano go, a nowy, stalowy most kratowy otwarto 13 listopada 1913 roku. 5 września 1939 roku wysadziło go wycofujące się wojsko polskie. Niemcy zbudowali drewniany, który przetrwał do lutego 1945 roku, a po wojnie most odbudowano. Około 1960 roku wymieniono podpory, a jako przęsło wykorzystano składany most wojskowy Bailey’a, który służył do 1970 roku.",
                "Po otwarciu mostu Mieszka I w 1970 roku most Bailey’a rozebrano i Śródka została odizolowana od centrum miasta. Połączenie z Ostrowem Tumskim odtworzono dopiero po 40 latach.",
            ]),
            ("Nowy most", [
                "Do budowy wykorzystano stalowe przęsło starego mostu św. Rocha, które po rozbiórce leżało nad kanałem ulgi Warty. Zdjęto je w 2002 roku z miejsca, w którym stało 89 lat, a w 2007 roku przeniesiono nad Cybinę. Ważące około 360 ton przęsło, długie na 70 m, jechało po torach kolejowych około kilometra. Najbardziej widowiskowa część operacji trwała od 28 września do 1 października 2007 roku, kiedy po raz pierwszy w Polsce przeniesiono most przez most, nad mostem Mieszka I. Na przyczółkach przęsło osadzono 25 października 2007 roku.",
                "Nazwę nadała mostowi uchwała Rady Miasta Poznania z 20 listopada 2007 roku. Patronem jest Jordan, pierwszy biskup Polski i Poznania, który według folderu Urzędu Miasta ochrzcił Mieszka I. Uroczyste otwarcie z poświęceniem przez arcybiskupa Stanisława Gądeckiego odbyło się wieczorem 7 grudnia 2007 roku.",
                "Za pomysł wykorzystania przęsła most dostał w maju 2008 roku nagrodę „Polskie drogi XXI”. Projekt kosztował około 8,6 mln zł, z czego 7 313 918,47 zł pochodziło z dotacji w ramach ZPORR. Realizatorem i zarządcą jest Zarząd Dróg Miejskich.",
            ]),
            ("Dane mostu", [
                "Rozpiętość teoretyczna 70 m, długość całkowita 72,30 m, szerokość całkowita 14,878 m, wysokość 9,495 m. Masa całkowita 360 t, w konstrukcji jest 48 986 nitów.",
            ]),
            ("Warto wiedzieć", [
                "Most leży na osi Traktu Królewsko-Cesarskiego. Konstrukcję przystosowano do nowej funkcji kładki dla pieszych. Stał się miejscem spacerów i wydarzeń, m.in. grudniowej procesji światła.",
            ]),
        ],
        address="ul. Ostrówek, Poznań (Śródka – Ostrów Tumski)",
        hours=[("Most", "dostępny całą dobę")],
        tickets=[("Przejście", "bezpłatnie")],
        phone=None,
        www=("poznan.pl", "https://www.poznan.pl/mim/wortals/czerwiec56/-,p,1025,5634,9345.html"),
        credit="most-biskupa-jordana",
        sources=[
            ("poznan.pl: Most Cybiński (Most Biskupa Jordana) – projekt ZPORR", "https://www.poznan.pl/mim/wortals/czerwiec56/-,p,1025,5634,9345.html"),
            ("Urząd Miasta Poznania: folder „Most Biskupa Jordana szansą dla Śródki” (PDF)", "https://www.poznan.pl/mim/public/wortals/attachments.att?co=show&instance=1017&parent=35557&lang=pl&id=72403"),
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
                "Trójwymiarowy mural „Opowieść śródecka z trębaczem na dachu i kotem w tle”, odsłonięty 1 października 2015 roku na kamienicy na rogu ulic Śródka i Rynek Śródecki. Powstał na podstawie zdjęcia z lat 20. XX wieku.",
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
            ("poznan.pl: 116 dębów pamięci", "https://www.poznan.pl/mim/rm/news,1202/inicjatywy-radnych,c,13/116-debow-pamieci,153082.html"),
            ("TenPoznan.pl: granitowe tablice w Lasku Katyńskim (22.09.2026)", "https://tenpoznan.pl/imiona-i-nazwiska-ofiar-zbrodni-katynskiej-wyryto-na-granitowych-tablicach/"),
        ],
        checked="06.10.2026",
    ),
]
