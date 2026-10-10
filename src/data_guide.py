# -*- coding: utf-8 -*-
"""Treści przekrojowe przewodnika: wybór na pierwszy raz, plany zwiedzania,
strona „O Poznaniu” i dodatkowe informacje praktyczne. Źródła podane przy każdej sekcji."""

# Dziesięć miejsc, od których warto zacząć. Kolejność = kolejność na stronie głównej.
TOP10 = [
    "stary-rynek", "ostrow-tumski", "brama-poznania", "rogalowe-muzeum", "fara",
    "zamek-krolewski", "zamek-cesarski", "stary-browar", "jezioro-maltanskie", "srodka",
]

# Szybkie filtry na stronie głównej (oprócz „bezpłatne”, liczonego z cennika).
KIDS = {
    "nowe-zoo", "stare-zoo", "kolejka-maltanka", "termy-maltanskie", "malta-ski", "rogalowe-muzeum",
    "muzeum-pyry", "muzeum-czekolady", "muzeum-iluzji", "makiety-dawnego-poznania", "brama-poznania",
    "centrum-szyfrow-enigma", "fotoplastykon", "jezioro-maltanskie", "linie-turystyczne", "stary-rynek",
    "cytadela", "ogrod-botaniczny", "rusalka",
    "park-rataje", "stare-koryto-warty", "park-tysiaclecia", "lasek-marcelinski",
    "pomnik-koziolkow",
}
INDOOR_EXTRA = {
    "brama-poznania", "zamek-krolewski", "zamek-cesarski", "genius-loci", "stary-browar",
    "termy-maltanskie", "fort-va", "wzgorze-sw-wojciecha",
}

# Plany zwiedzania: (id, tytuł, dla kogo, wstęp, [(slug, kiedy, wskazówka)], uwagi)
PLANS = [
    ("dzien-1", "Dzień 1: Stare Miasto i Ostrów Tumski",
     "Na pierwszy dzień, najlepiej od wtorku do soboty",
     "Serce Poznania i kolebka państwa polskiego. Całą trasę przejdziesz pieszo.",
     [("zamek-krolewski", "rano", "Zacznij od wieży widokowej: z góry zobaczysz, dokąd pójdziesz dalej."),
      ("fara", "przed południem", "Barokowa fara stoi kilka minut spacerem od zamku."),
      ("stary-rynek", "przed 12:00", "Stań przed ratuszem kilka minut przed południem, żeby zobaczyć koziołki."),
      ("rogalowe-muzeum", "wczesne popołudnie", "Interaktywny pokaz o rogalu świętomarcińskim. Pokazy często się wyprzedają, więc kup bilet wcześniej."),
      ("mury-miejskie", "po drodze", "Relikty murów, bastion przy ul. 23 Lutego i baszta Katarzynek."),
      ("ostrow-tumski", "popołudnie", "Ze Starego Rynku dojdziesz spacerem ul. Wielką przez Wartę do archikatedry."),
      ("brama-poznania", "późne popołudnie", "Kładką nad Cybiną przejdziesz do multimedialnej ekspozycji o początkach państwa."),
      ("srodka", "wieczór", "Na Śródce zobacz trójwymiarowy mural i zjedz kolację.")],
     "W poniedziałek Zamek Królewski i Brama Poznania są nieczynne. W ten dzień zamień je na katedrę i spacer bulwarami nad Wartą."),
    ("dzien-2", "Dzień 2: Dzielnica Cesarska i Jeżyce",
     "Na drugi dzień",
     "Poznań z przełomu XIX i XX wieku: gmachy Dzielnicy Cesarskiej, muzea przy placu Wolności i kamienice Jeżyc.",
     [("muzeum-narodowe", "rano", "Galeria malarstwa przy Alejach Marcinkowskiego. We wtorek wystawy stałe są bezpłatne."),
      ("biblioteka-raczynskich", "po drodze", "Klasycystyczny gmach przy placu Wolności."),
      ("bazar", "po drodze", "Hotel Bazar przy ul. Paderewskiego i Alejach Marcinkowskiego."),
      ("zamek-cesarski", "od 12:00", "Zamek zwiedza się od południa. Obok stoi Pomnik Poznańskiego Czerwca 1956."),
      ("pomnik-czerwca-1956", "po drodze", "Krzyże w Parku Mickiewicza, naprzeciwko zamku."),
      ("park-mickiewicza", "po drodze", "Park między zamkiem a Operą, dobry na krótki odpoczynek."),
      ("jezyce", "popołudnie", "Secesyjne kamienice, targ na Rynku Jeżyckim i szlak Jeżycjady. Dojdziesz pieszo albo dojedziesz tramwajem."),
      ("stary-browar", "wieczór", "Ceglany XIX-wieczny browar z rzeźbami Mitoraja i innych artystów, sklepami i parkiem. Czynny do 21:00, w niedziele tylko handlowe.")],
     "Muzeum Narodowe jest zamknięte w poniedziałki."),
    ("dzien-3", "Dzień 3: Zielony Poznań",
     "Na trzeci dzień albo na ładną pogodę",
     "Cytadela, Jezioro Maltańskie i zoo. Między punktami podjedziesz tramwajem.",
     [("cytadela", "rano", "Park na około 100 hektarach z Muzeum Uzbrojenia, cmentarzami wojennymi i Rosarium."),
      ("jezioro-maltanskie", "południe", "Spacer albo rower po trasie wokół jeziora."),
      ("kolejka-maltanka", "popołudnie", "Kolejką parkową dojedziesz wzdłuż jeziora do Nowego Zoo."),
      ("nowe-zoo", "popołudnie", "Zoo na 120 hektarach. Zarezerwuj na nie kilka godzin."),
      ("termy-maltanskie", "wieczór", "Aquapark czynny codziennie do 23:00.")],
     "Maltanka kursuje sezonowo (sezon 2026 zakończył się 27 września), więc poza sezonem do zoo dojdziesz pieszo wzdłuż jeziora. Rozkład na nowy sezon poda MPK."),
    ("z-dziecmi", "Z dziećmi",
     "Rodziny z dziećmi w wieku przedszkolnym i szkolnym",
     "Krótkie przejścia, pokazy i dużo ruchu na świeżym powietrzu.",
     [("stary-rynek", "przed 12:00", "Koziołki na ratuszu to punkt obowiązkowy."),
      ("rogalowe-muzeum", "po koziołkach", "Interaktywny pokaz: jak powstaje rogal świętomarciński."),
      ("makiety-dawnego-poznania", "przed południem lub po obiedzie", "Makieta dawnego Poznania z pokazem światła i dźwięku."),
      ("kolejka-maltanka", "popołudnie", "Przejazd kolejką parkową nad Maltą (tylko w sezonie, w 2026 roku od 12 kwietnia do 27 września)."),
      ("nowe-zoo", "popołudnie", "Duże wybiegi i spacer po lesie."),
      ("malta-ski", "zamiennie", "Sztuczny stok, letni tor saneczkowy i kolejka górska nad jeziorem.")],
     "Stare Zoo przy ul. Zwierzynieckiej jest bezpłatne i leży blisko centrum. To dobra krótsza alternatywa."),
    ("deszcz", "Na deszczowy dzień",
     "Gdy pada albo jest zimno",
     "Same miejsca pod dachem.",
     [("brama-poznania", "rano", "Multimedialna ekspozycja o początkach państwa."),
      ("centrum-szyfrow-enigma", "przed południem", "Interaktywna wystawa o złamaniu Enigmy."),
      ("muzeum-narodowe", "po południu", "Malarstwo polskie i europejskie."),
      ("stary-browar", "wieczór", "Rzeźby, instalacje i wystawy w Pop Culture Gallery, wszystko pod dachem dawnego browaru."),
      ("termy-maltanskie", "wieczór", "Baseny i zjeżdżalnie do 23:00.")],
     "W poniedziałek Brama Poznania, Centrum Szyfrów Enigma i Muzeum Narodowe są nieczynne. Zamiast nich wybierz Rogalowe Muzeum, Muzeum Czekolady i Zamek Cesarski."),
    ("za-darmo", "Za darmo",
     "Przy ograniczonym budżecie",
     "Wiele najpiękniejszych miejsc zwiedzisz bez biletu. We wtorki część muzeów ma wstęp wolny.",
     [("stary-rynek", "przed 12:00", "Plac, domki budnicze, fontanny i koziołki."),
      ("fara", "przed południem", "Wnętrze fary zwiedzisz bez biletu. W soboty o 12:15 odbywają się koncerty organowe."),
      ("ostrow-tumski", "popołudnie", "Wejście do katedry jest bezpłatne."),
      ("trakt-krolewsko-cesarski", "cały dzień", "Oznakowany szlak łączy najważniejsze zabytki."),
      ("cytadela", "popołudnie", "Park z pomnikami i cmentarzami wojennymi."),
      ("stare-zoo", "zamiennie", "Najstarsze poznańskie zoo, wstęp wolny."),
      ("muzeum-powstania", "we wtorek", "We wtorek wstęp wolny."),
      ("fort-vii", "we wtorek", "We wtorek wstęp wolny.")],
     "Lista wszystkich bezpłatnych dni w muzeach jest w informacjach praktycznych."),
    ("poniedzialek", "W poniedziałek",
     "Gdy większość muzeów ma dzień przerwy",
     "Miejsca czynne także w poniedziałki.",
     [("stary-rynek", "przed 12:00", "Koziołki trykają się codziennie."),
      ("rogalowe-muzeum", "przed południem", "Pokazy odbywają się codziennie."),
      ("ostrow-tumski", "południe", "Katedrę zwiedzisz w dni powszednie."),
      ("zamek-cesarski", "od 12:00", "Zamek jest czynny codziennie."),
      ("nowe-zoo", "popołudnie", "Zoo jest czynne codziennie."),
      ("stary-browar", "wieczór", "Czynny także w poniedziałki. Rzeźby Mitoraja i innych artystów obejrzysz bezpłatnie.")],
     "Przed wyjściem sprawdź godziny na podstronie każdego miejsca, bo w święta mogą być inne."),
]

# ─── O Poznaniu ───
# Źródło: poznan.pl, „Rys historyczny”; daty z podstron atrakcji w tym przewodniku.
# Uzupełnienia 01.10.2026 sprawdzone w pl.wikipedia (Wielkie Księstwo Poznańskie, Cytadela, UAM, MTP,
# PeWuKa, Marian Rejewski, Kraj Warty, powstania 1848 i 1918, pielgrzymki Jana Pawła II 1983 i 1997)
# i w rysie historycznym poznan.pl (1939, 1945). Trzeci element (opcjonalny) = slug podstrony atrakcji.
HISTORY = [
    ("IX wiek", "Na Ostrowie Tumskim, między Wartą a Cybiną, powstaje gród."),
    ("X wiek", "Gród jest jedną z głównych siedzib księcia Mieszka I."),
    ("968", "W Poznaniu powstaje pierwsze biskupstwo na ziemiach polskich."),
    ("XI wiek", "W katedrze spoczywają pierwsi władcy Polski, w tym Bolesław Chrobry. W 1038 roku gród niszczy najazd czeskiego księcia Brzetysława I.", "ostrow-tumski"),
    ("1253", "Przemysł I nadaje Poznaniowi prawa miejskie. Na lewym brzegu Warty wytyczono Stary Rynek."),
    ("XVI wiek", "Złoty wiek miasta. W 1519 roku biskup Jan Lubrański zakłada Akademię Lubrańskiego, w latach 1550–1560 Giovanni Battista di Quadro nadaje ratuszowi renesansowy wygląd, a w latach 70. jezuici otwierają kolegium, szkołę średnią z kursami akademickimi."),
    ("1793", "W II rozbiorze Polski Poznań zostaje przyłączony do Prus."),
    ("1806", "W listopadzie do Poznania przybywa Napoleon. Przez prawie trzy tygodnie mieszka w dawnym Kolegium Jezuickim.", "kolegium-jezuickie"),
    ("1815", "Po kongresie wiedeńskim Poznań zostaje siedzibą władz Wielkiego Księstwa Poznańskiego, części Prus. Namiestnikiem jest książę Antoni Radziwiłł."),
    ("1828–1842", "Prusacy budują na Winiarach potężny fort, dziś Cytadelę. Poznań zamienia się w miasto-twierdzę otoczone fortyfikacjami.", "cytadela"),
    ("1848", "W czasie Wiosny Ludów 20 marca powstaje w Poznaniu Komitet Narodowy, a w Wielkopolsce wybucha powstanie przeciw Prusom. W maju powstańcy kapitulują."),
    ("1905–1910", "Dla cesarza Wilhelma II powstaje Zamek Cesarski, serce nowej Dzielnicy Cesarskiej.", "zamek-cesarski"),
    ("1918–1919", "26 grudnia 1918 roku Ignacy Paderewski przemawia do poznaniaków przed hotelem Bazar, a następnego dnia wybucha powstanie wielkopolskie. Zwycięskie powstanie przywraca Poznań Polsce. W 1919 roku powstaje Uniwersytet Poznański, dziś Uniwersytet im. Adama Mickiewicza.", "bazar"),
    ("1921", "Odbywa się pierwszy Targ Poznański. Od 1925 roku to targi międzynarodowe, a Poznań staje się miastem targów."),
    ("1929", "Od 16 maja do 30 września trwa Powszechna Wystawa Krajowa (PeWuKa), pokaz dorobku dziesięciu lat niepodległej Polski."),
    ("1932", "Marian Rejewski, absolwent matematyki Uniwersytetu Poznańskiego, łamie szyfr niemieckiej Enigmy. Współpracują z nim Jerzy Różycki i Henryk Zygalski, również absolwenci poznańskiej uczelni.", "centrum-szyfrow-enigma"),
    ("1939–1945", "10 września 1939 roku Niemcy zajmują Poznań i włączają go do Rzeszy jako stolicę Kraju Warty. Część mieszkańców zostaje wysiedlona. Po ciężkich walkach miasto zostaje zdobyte 23 lutego 1945 roku, zniszczone w około 55%."),
    ("1956", "28 czerwca robotnicy wychodzą na ulice. Poznański Czerwiec to pierwszy masowy protest przeciw władzy komunistycznej w PRL. W 25. rocznicę, 28 czerwca 1981 roku, odsłonięto pomnik Poznańskiego Czerwca, czyli Poznańskie Krzyże.", "pomnik-czerwca-1956"),
    ("1983 i 1997", "Poznań odwiedza papież Jan Paweł II. 20 czerwca 1983 roku beatyfikuje Urszulę Ledóchowską podczas mszy na Łęgach Dębińskich, a 3 czerwca 1997 roku spotyka się z młodzieżą na placu Mickiewicza.", "legi-debinskie"),
    ("2012", "Na przebudowanym Stadionie Miejskim odbywają się trzy mecze fazy grupowej Euro 2012.", "stadion"),
]

# Źródło: poznan.pl, „Podania i legendy” (streszczenia własne); rogale: pl.wikipedia „Rogal świętomarciński”.
LEGENDS = [
    ("O powstaniu Poznania",
     "Po długiej rozłące trzej bracia, Lech, Czech i Rus, spotkali się tam, gdzie Cybina wpada do Warty. Rozpoznali się od razu i zawołali: „Poznaję!”. Na pamiątkę spotkania zbudowali w tym miejscu gród i nazwali go Poznaniem."),
    ("O poznańskich koziołkach",
     "Gdy zegarmistrz Bartłomiej z Gubina miał pokazać rajcom nowy zegar ratuszowy, w kuchni szykowano ucztę dla wojewody. Kuchcik spalił udziec sarni, więc ukradł z łąki dwa koziołki, żeby je upiec. Zwierzęta uciekły na wieżę i zaczęły się trykać nad zegarem. Rozbawiony wojewoda wybaczył chłopcu i kazał dobudować do zegara mechanizm z koziołkami."),
    ("O ratuszowym hejnale",
     "Przemek, syn strażnika z ratuszowej wieży, uratował rannego kruka. Ptak okazał się królem kruków i dał mu srebrną trąbkę na czas zagrożenia. Gdy wróg otoczył miasto, Przemek zatrąbił na cztery strony świata. Nadleciały tysiące ptaków i przegoniły najeźdźców. Na pamiątkę postanowiono, że trębacz miejski będzie codziennie grał z wieży hejnał na cztery strony świata."),
    ("O fontannie Prozerpiny",
     "W XVII wieku bogata wdowa Petronela poślubiła młodego czeladnika kamieniarskiego. Gdy ten zakochał się w innej, oskarżyła go o próbę otrucia. Sąd ukarał go tylko grzywną i nakazał postawić własnym kosztem fontannę przed ratuszem. Tak powstała fontanna z porwaniem Prozerpiny przez Plutona."),
    ("O mieczu św. Piotra",
     "Rzymski miecz z Muzeum Archidiecezjalnego ma być tym, którym św. Piotr odciął ucho słudze arcykapłana w Ogrodzie Oliwnym. Według Jana Długosza papież podarował go pierwszemu biskupowi poznańskiemu Jordanowi."),
    ("O rogalach świętomarcińskich",
     "Według popularnej legendy w listopadzie 1891 roku proboszcz parafii św. Marcina, ks. Jan Lewicki, zaapelował do wiernych, by wzorem patrona pomogli biednym. Cukiernik Józef Melzer namówił swojego szefa, by upiec rogale. Zamożni poznaniacy je kupowali, a biedni dostawali za darmo. Kształt rogala ma przypominać podkowę zgubioną przez konia świętego. W rzeczywistości rogale na 11 listopada pieczono w Poznaniu wcześniej: najstarsza znana reklama pochodzi z 1860 roku."),
    ("O księżnej Ludgardzie",
     "Ludgarda, pierwsza żona Przemysła II, nie dała mu następcy. Według legendy w 1283 roku zginęła z tego powodu w łaźni u stóp poznańskiego zamku. Źródła historyczne podają jednak, że zmarła w Gnieźnie i tam ją pochowano."),
]

# Źródło: poznan.pl, słownik gwary poznańskiej (hasła sprawdzone pojedynczo).
DIALECT = [
    ("pyra", "ziemniak"), ("bimba", "tramwaj"), ("szneka", "drożdżówka w kształcie ślimaka"),
    ("tej", "ty (zawołanie: „Tej, chodź tu!”)"), ("laczki", "domowe pantofle bez napiętka"),
    ("tytka", "papierowa torebka"), ("ancug", "garnitur"), ("sznytka", "kromka chleba, kanapka"),
    ("gzik", "twarożek ze śmietaną i szczypiorkiem lub cebulą"), ("galoty", "majtki"),
    ("szczun", "chłopak"), ("korbol", "dynia"), ("ryczka", "niski taboret"),
    ("wuchta", "mnóstwo"), ("fyrtel", "dzielnica, okolica"), ("jupka", "kurtka"), ("bana", "pociąg"),
    ("ino", "tylko"), ("szagą", "na ukos, na skos"), ("rajzefiber", "podniecenie, niepokój przed podróżą"),
    ("mantel", "płaszcz"), ("antrejka", "przedpokój"), ("kejter", "pies, kundel"), ("ćmik", "papieros"),
    ("glanc", "połysk (stąd „szneka z glancem”)"),
]

# Źródło: Wikipedia, „Kuchnia wielkopolska”; rogal: Kapituła Rogala Świętomarcińskiego.
CUISINE = [
    ("Rogal świętomarciński", "Półfrancuskie ciasto z nadzieniem z białego maku. Od 2008 roku ma unijne Chronione Oznaczenie Geograficzne. Najwięcej je się ich 11 listopada."),
    ("Pyry z gzikiem", "Ziemniaki z twarożkiem ze śmietaną, szczypiorkiem albo cebulą."),
    ("Szare kluski", "Kluski z surowych ziemniaków, podawane z kapustą, bigosem albo okrasą z cebulki."),
    ("Czernina", "Zupa z krwi kaczej (dawniej gęsiej)."),
    ("Plyndze", "Placki ziemniaczane (w gwarze plyndz, plendz albo plindz)."),
    ("Pieczona kaczka z jabłkami", "Podawana z modrą kapustą i pyzami."),
    ("Szneka z glancem", "Drożdżówka w kształcie ślimaka, polana lukrem."),
    ("Ślepe ryby", "Gęsta zupa ziemniaczana. Ryb w niej nie ma, stąd nazwa."),
]

# Źródło: IMGW-PIB, dane publiczne, miesięczne dane synoptyczne stacji Poznań-Ławica (352160330).
# Średnie z lat 1991–2020 (aktualna norma klimatyczna WMO), policzone 01.10.2026 z 360 miesięcy, bez braków.
CLIMATE = [
    ("−0,4 °C", "średnia temperatura stycznia"),
    ("19,5 °C", "średnia temperatura lipca"),
    ("539 mm", "roczna suma opadów"),
    ("lipiec", "najbardziej deszczowy miesiąc (84 mm)"),
]

# ─── Informacje praktyczne: uzupełnienia ───
# Źródło: poznan.pl, lista toalet publicznych (POI), sprawdzone 29.09.2026 i ponownie 01.10.2026 (każda pozycja). Tylko miejsca przy trasach turystycznych.
TOILETS = [
    ("Stary Rynek", "róg ul. Różany Targ i ul. Quadro, przy bocznej ścianie ratusza", "pn–pt 8:00–22:00, sb–nd 10:00–22:00"),
    ("Plac Wolności", "tył budynku Arkadii, od strony ul. 3 Maja", "pn–pt 8:00–20:00, sb 8:00–16:00, nd nieczynna"),
    ("Międzymoście (ul. Wielka)", "w drodze ze Starego Rynku na Ostrów Tumski, automatyczna", "całodobowo"),
    ("Ostrów Tumski", "naprzeciwko Psałterii", "pn–pt 8:00–18:00, sb–nd 10:00–20:00"),
    ("Rondo Kaponiera", "pod rondem, poziom −1", "codziennie 8:00–18:00"),
    ("Cytadela", "naprzeciwko wejścia do Muzeum Uzbrojenia", "codziennie 10:00–18:00"),
    ("Cytadela, Rosarium", "automatyczna", "całodobowo"),
    ("Park Mickiewicza", "ul. Wieniawskiego, automatyczna", "całodobowo"),
    ("Most Teatralny", "ul. Roosevelta, automatyczna", "całodobowo"),
    ("Park Wilsona", "przy wejściu od ul. Głogowskiej", "pn–pt 8:00–18:00, sb–nd 10:00–18:00"),
    ("Park Sołacki", "ul. Małopolska, naprzeciwko ul. Śląskiej, automatyczna", "całodobowo"),
    ("Most św. Rocha", "przy zejściu nad Wartę, automatyczna", "całodobowo"),
    ("Rynek Jeżycki", "na rynku", "pn–sb 6:00–18:00"),
    ("Dworzec Zachodni", "budynek stacji PST", "pn–pt 6:00–22:00, sb–nd 8:00–20:00"),
]
