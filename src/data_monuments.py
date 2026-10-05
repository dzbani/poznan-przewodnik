# -*- coding: utf-8 -*-
"""Etap 7, partia pomników i fontann (29.09.2026): wszystkie pozycje z list POI
poznan.pl „Pomniki” i „Fontanny i studzienki”. Źródła: poznan.pl, Wikipedia,
Malta Festival (Wiedźma z Chwaliszewa). Opisy streszczone własnymi słowami.
Pomnik Poznańskiego Czerwca 1956 jest w site_data.py (kategoria przeniesiona tutaj)."""

from urllib.parse import quote

PM = "https://www.poznan.pl/mim/wortals/wortal,2024/pomniki,poi,2473/"
PF = "https://www.poznan.pl/mim/wortals/wortal,2024/fontanny-i-studzienki,poi,2571/"


def wiki(title):
    return ("Wikipedia: " + title, "https://pl.wikipedia.org/wiki/" + quote(title.replace(" ", "_")))


def M(slug, name, img_alt, short, lead, sections, address, src, extra_sources=(),
      img=True, hours=None, badge="Bezpłatnie", credit=None):
    return dict(
        slug=slug, cat="pomniki", name=name,
        img=slug if img is True else img, img_alt=img_alt if img else "",
        short=short, badge=badge, status=None, lead=lead, sections=sections,
        address=address,
        hours=hours or [("Dostęp", "przez całą dobę, z zewnątrz")],
        tickets=[("Wstęp", "bezpłatnie")],
        phone=None, www=("poznan.pl", src[1]),
        credit=credit if credit else (slug if img is True else None),
        sources=[src, *extra_sources],
    )


MONUMENTS = [
    M("pomnik-koziolkow", "Pomnik Koziołków",
      "Rzeźba dwóch trykających się koziołków na placu Kolegiackim",
      "Dwa trykające się koziołki z brązu na placu Kolegiackim. Można na nich usiąść do zdjęcia.",
      "Pomnik przedstawia dwa trykające się koziołki, nawiązujące do najbardziej znanego symbolu Poznania: koziołków, które w południe wychodzą na wieżę ratusza.",
      [("O pomniku", [
          "Zaprojektował go Robert Sobociński, a stanął w 2002 roku na placu Kolegiackim, niedaleko głównego wejścia do Urzędu Miasta w dawnym kolegium jezuickim.",
          "W 2019 roku, na czas przebudowy placu, rzeźbę przeniesiono do Parku Chopina. Na swoje miejsce wróciła po zakończeniu prac.",
      ]),
       ("Warto wiedzieć", [
          "Rzeźba stoi nisko, a na grzbietach koziołków można usiąść, dlatego to jedno z najpopularniejszych miejsc na pamiątkowe zdjęcie z Poznania.",
          "Prawdziwe koziołki trykają się codziennie o 12:00 na wieży ratusza, kilka minut spacerem stąd.",
      ])],
      "pl. Kolegiacki, 61-841 Poznań",
      ("poznan.pl: Pomnik Poznańskich Koziołków", PM + "poznanskich-koziolkow,51451.html"),
      [wiki("Pomnik koziołków w Poznaniu")]),

    M("fontanna-prozerpiny", "Fontanna Prozerpiny",
      "Barokowa Fontanna Prozerpiny przed ratuszem wieczorem",
      "Jedyna zachowana historyczna fontanna Starego Rynku, z 1766 roku, przed ratuszem.",
      "Fontanna Prozerpiny stoi przed ratuszem na Starym Rynku. To barokowe dzieło Augustyna Schöpsa, ukończone w 1766 roku, i jedyna z czterech historycznych fontann rynku, która przetrwała do dziś.",
      [("Historia", [
          "Studnie na rynku wspominano już w 1568 roku, kiedy zamówiono do nich drewniane figury lwa i jelenia. W 1615 roku zastąpiono je posągami Apolla, Jowisza, Marsa i Neptuna.",
          "W 1758 roku rajcy zlecili budowę nowej fontanny Augustynowi Schöpsowi. Prace trwały do 1766 roku.",
          "W 2010 roku kibice Lecha Poznań świętujący mistrzostwo Polski uszkodzili fontannę. Naprawiono ją po miesiącu, za pieniądze zebrane przez samych kibiców.",
      ]),
       ("Co zobaczyć", [
          "Scenę porwania Prozerpiny przez Plutona, władcę podziemi, wykutą w piaskowcu.",
          "Płaskorzeźby czterech żywiołów na ścianach basenu (ogień, woda, powietrze i ziemia) oraz herb Poznania.",
      ])],
      "Stary Rynek (przed ratuszem), 61-772 Poznań",
      ("poznan.pl: Fontanna Prozerpiny", PF + "fontanna-prozerpiny,41208.html"),
      [wiki("Fontanna Prozerpiny w Poznaniu")]),

    M("studzienka-bamberki", "Studzienka Bamberki",
      "Studzienka z figurą Bamberki przy ratuszu",
      "Brązowa figura dziewczyny w stroju bamberskim przy zachodniej ścianie ratusza, z 1915 roku.",
      "Studzienka Bamberki stoi przy zachodniej ścianie ratusza. Jej ozdobą jest brązowa figura kobiety w stroju bamberskim, z nosidłami i konwiami. Upamiętnia Bambrów, osadników spod Bambergu, którzy w XVIII wieku zasiedlili podpoznańskie wsie.",
      [("Historia", [
          "Studzienkę odsłonięto w 1915 roku. Ufundował ją poznański kupiec i winiarz Leopold Goldenring. Cokół zaprojektował budowniczy Stahl, a figurę wyrzeźbił Józef Wackerle.",
          "Rzeźbiarzowi pozowała Jadwiga Gadziemska, pracownica winiarni Goldenringa, która sama nie pochodziła z rodziny bamberskiej.",
          "Basen służył kiedyś jako poidło dla koni, korzystali z niego też mieszkańcy. Po wojnie studzienkę kilka razy przenoszono, a w 1977 roku wróciła na Stary Rynek.",
      ]),
       ("Warto wiedzieć", [
          "Kazimiera Iłłakowiczówna napisała o niej wiersz „Bambereczka”.",
          "Więcej o Bambrach opowiada Muzeum Bambrów Poznańskich przy ulicy Mostowej.",
      ])],
      "Stary Rynek (zachodnia ściana ratusza), 61-768 Poznań",
      ("poznan.pl: Studzienka Bamberki", PF + "studzienka-bamberki,41217.html"),
      [wiki("Studzienka Bamberki w Poznaniu")]),

    M("fontanna-apolla", "Fontanna Apolla",
      "Fontanna Apolla na Starym Rynku, w tle kamienice i ratusz",
      "Współczesna fontanna z 2002 roku z posągiem Apolla, w południowo-wschodnim narożniku rynku.",
      "Fontanna Apolla stoi w południowo-wschodnim narożniku Starego Rynku, u wylotu ulic Wodnej i Świętosławskiej. Odsłonięto ją w 2002 roku, a jej autorem jest Marian Konieczny.",
      [("Historia", [
          "Już w XVII wieku stała tu jedna z czterech rynkowych fontann, z której mieszkańcy czerpali wodę do końca XIX wieku. Współczesna fontanna nawiązuje do tej tradycji.",
          "Posąg od początku budził emocje: krytykowano proporcje postaci i jej nagość, a zastrzeżenia zgłaszał też konserwator zabytków.",
      ]),
       ("Warto wiedzieć", [
          "To jedna z czterech fontann rynku. Pozostałe to Prozerpiny, Neptuna i Marsa, więc łatwo obejść wszystkie podczas jednego spaceru.",
      ])],
      "Stary Rynek (róg ul. Wodnej i Świętosławskiej), 61-772 Poznań",
      ("poznan.pl: Fontanna Apolla", PF + "fontanna-apolla,41209.html"),
      [wiki("Fontanna Apolla w Poznaniu")]),

    M("fontanna-neptuna", "Fontanna Neptuna",
      "Posąg Neptuna na fontannie na Starym Rynku",
      "Fontanna z 2004 roku w miejscu dawnego targu rybnego, u wylotu ulic Paderewskiego i Szkolnej.",
      "Fontanna Neptuna stoi w południowo-zachodniej części Starego Rynku, u wylotu ulic Paderewskiego i Szkolnej. Zaprojektował ją Marcin Sobczak, a odsłonięto ją w 2004 roku.",
      [("Historia miejsca", [
          "Przez wieki działał tu targ rybny. Poznań był silnie związany z Wartą i jej odnogami: wielu mieszkańców pracowało jako rybacy, flisacy i piaskarze. Przypominają o tym nazwy ulic, takie jak Wodna, Mostowa, Grobla czy Rybaki.",
          "Fontanna stoi w miejscu dawnej studni z XVII wieku. Podobnie jak fontanny Apolla i Marsa jest współczesnym nawiązaniem do dawnych rynkowych studni.",
      ])],
      "Stary Rynek (u wylotu ul. Paderewskiego), 61-772 Poznań",
      ("poznan.pl: Fontanna Neptuna", PF + "fontanna-neptuna,41210.html"),
      [wiki("Fontanna Neptuna w Poznaniu")]),

    M("fontanna-marsa", "Fontanna Marsa",
      "Fontanna Marsa na Starym Rynku, w tle ratusz",
      "Najmłodsza z czterech fontann Starego Rynku, odsłonięta w 2005 roku.",
      "Fontanna Marsa stoi w północno-zachodniej części Starego Rynku. Odsłonięto ją w 2005 roku. Autorem rzeźby jest Rafał Nowak, a fundatorami Wanda i Romuald Szperlińscy.",
      [("Historia", [
          "W XVII wieku stała tu jedna z rynkowych fontann, która do końca XIX wieku dostarczała mieszkańcom wodę. Nowa fontanna przywróciła to historyczne miejsce.",
          "Rzeźba przedstawia rzymskiego boga wojny, jedną z czterech postaci, które od 1615 roku zdobiły studnie na rynku.",
      ])],
      "Stary Rynek (część północno-zachodnia), 61-772 Poznań",
      ("poznan.pl: Fontanna Marsa", PF + "fontanna-marsa,41211.html"),
      [wiki("Fontanna Marsa w Poznaniu")]),

    M("pomnik-starego-marycha", "Pomnik Starego Marycha",
      "Rzeźba Starego Marycha z rowerem na ulicy Półwiejskiej",
      "Brązowy poznaniak z rowerem, bohater radiowych gawęd gwarą. Popularne miejsce na zdjęcie.",
      "Stary Marych to fikcyjna postać typowego poznaniaka mówiącego gwarą, bohater radiowych słuchowisk „Blubry Starego Marycha” Juliusza Kubla. Pomnik stoi na północnym krańcu deptaka przy ulicy Półwiejskiej.",
      [("O pomniku", [
          "Pomysł wyszedł od poznańskiej redakcji „Gazety Wyborczej”, która w 1998 roku ogłosiła plebiscyt „Poznaniak na cokół!”. Czytelnicy wybrali Starego Marycha, jedyną fikcyjną postać wśród kandydatów.",
          "Rzeźbę zaprojektował Robert Sobociński. Marych ma twarz Mariana Pogasza, który czytał słuchowiska w radiu. Prowadzi rower z tradycyjną teczką przewieszoną przez kierownicę.",
          "Pomnik odsłonięto 21 marca 2001 roku, w 90. rocznicę urodzin Stanisława Strugarka, popularyzatora gwary poznańskiej.",
      ]),
       ("Warto wiedzieć", [
          "O gwarze poznańskiej i jej najważniejszych słowach przeczytasz na stronie O Poznaniu.",
      ])],
      "ul. Półwiejska / ul. Strzelecka, 61-888 Poznań",
      ("poznan.pl: Pomnik Starego Marycha", PM + "starego-marycha,51450.html"),
      [wiki("Pomnik Starego Marycha w Poznaniu")]),

    M("pomnik-zygi-latarnika", "Pomnik Zygi Latarnika",
      "Rzeźba latarnika przy zabytkowej latarni gazowej na Grobli",
      "Brązowy latarnik przy prawdziwej latarni gazowej, obok dawnej gazowni na Grobli.",
      "Zyga, czyli po poznańsku Zygmunt, to fikcyjny latarnik. Jego brązowa figura stoi na skwerze przy ulicy Grobla, obok Starej Gazowni.",
      [("O pomniku", [
          "Pomnik odsłonięto 29 maja 2003 roku. Był efektem akcji „Ocalmy latarnie” prowadzonej przez „Gazetę Wyborczą” i gazownię, która miała uratować zabytkowe latarnie gazowe w Poznaniu.",
          "Autorem rzeźby jest Robert Sobociński. Częścią kompozycji jest oryginalna, odnowiona latarnia gazowa przeniesiona z ulicy Słowackiego na Jeżycach.",
      ])],
      "ul. Grobla (skwer przy Starej Gazowni), 61-858 Poznań",
      ("poznan.pl: Pomnik Zygi Latarnika", PM + "zygi-latarnika,51570.html"),
      [wiki("Pomnik Zygi Latarnika")]),

    M("pomnik-mickiewicza", "Pomnik Adama Mickiewicza",
      "Pomnik Adama Mickiewicza na placu Mickiewicza",
      "Pomnik z 1960 roku przy Poznańskich Krzyżach. Pierwszy pomnik poety na ziemiach polskich stanął w Poznaniu w 1859 roku.",
      "Obecny pomnik Adama Mickiewicza, dzieło Bazylego Wojtowicza, odsłonięto w 1960 roku na placu Mickiewicza. To czterometrowa figura na dwumetrowym cokole.",
      [("Pierwszy pomnik Mickiewicza", [
          "Po śmierci poety w 1855 roku poznaniacy zebrali pieniądze na pomnik i zamówili go u Władysława Oleszczyńskiego w Paryżu. Władze pruskie długo nie zgadzały się na lokalizację, zgodę wydano dopiero pod koniec 1858 roku.",
          "Pomnik odsłonięto 7 maja 1859 roku w ogrodzie przy kościele św. Marcina. Był to pierwszy pomnik Mickiewicza na ziemiach polskich. W 1904 roku zastąpiono go odlewem z brązu, a w 1939 roku Niemcy zniszczyli oba monumenty.",
          "Miejsce pierwszego pomnika przy kościele św. Marcina upamiętnia dziś tablica.",
      ]),
       ("Warto wiedzieć", [
          "Na tym samym placu stoi Pomnik Poznańskiego Czerwca 1956, a obok rozciąga się Park Mickiewicza przed Teatrem Wielkim.",
      ])],
      "pl. Adama Mickiewicza, 61-712 Poznań",
      ("poznan.pl: Pomnik Adama Mickiewicza", PM + "adama-mickiewicza,40372.html"),
      [wiki("Pomnik Adama Mickiewicza w Poznaniu")]),

    M("pomnik-kryptologow", "Pomnik Kryptologów (Pogromców Enigmy)",
      "Trójgraniasty pomnik kryptologów przed Zamkiem Cesarskim",
      "Obelisk z ciągów cyfr przed Zamkiem Cesarskim, poświęcony trzem poznańskim matematykom, którzy złamali Enigmę.",
      "Pomnik przed głównym wejściem do Zamku Cesarskiego upamiętnia Mariana Rejewskiego, Jerzego Różyckiego i Henryka Zygalskiego, matematyków związanych z Uniwersytetem Poznańskim, którzy złamali szyfr niemieckiej maszyny Enigma.",
      [("O pomniku", [
          "Odsłonięto go w 2007 roku. Zaprojektowali go Grażyna Bielska-Kozakiewicz i Mariusz Kozakiewicz.",
          "Ma formę metalowego graniastosłupa o podstawie trójkąta. Ściany pokrywają ciągi cyfr, w które wpisano nazwiska kryptologów, jako hołd dla matematyki i ludzkiej myśli.",
          "U dołu są napisy po polsku i angielsku z biografiami trzech matematyków.",
      ]),
       ("Warto wiedzieć", [
          "Przed wojną w Zamku mieściły się pomieszczenia uniwersytetu. Kilka kroków dalej działa Centrum Szyfrów Enigma z multimedialną wystawą o tej historii.",
      ])],
      "ul. Święty Marcin 80/82 (przed Zamkiem Cesarskim), 61-809 Poznań",
      ("poznan.pl: Pomnik Pogromców Enigmy", PM + "pogromcow-enigmy,51452.html"),
      [wiki("Pomnik kryptologów w Poznaniu")]),

    M("fontanna-lwow", "Fontanna Lwów",
      "Fontanna wsparta na ośmiu lwach na dziedzińcu Zamku Cesarskiego",
      "Fontanna wzorowana na Dziedzińcu Lwów w Alhambrze, ukryta na dziedzińcu Zamku Cesarskiego.",
      "Fontanna Lwów stoi na Dziedzińcu Różanym Zamku Cesarskiego. Zarówno dziedziniec, jak i fontanna są wzorowane na słynnym Dziedzińcu Lwów w pałacu Alhambra w Grenadzie.",
      [("O fontannie", [
          "Powstała razem z zamkiem, zaprojektowanym przez Franza Schwechtena i ukończonym około 1910 roku.",
          "Ma dwie kamienne misy: woda spływa z górnej do dolnej, wspartej na ośmiu figurach lwów. W Alhambrze lwów jest dwanaście.",
          "Po wojnie miejsce było zaniedbane, stały tu nawet garaże dla autobusów. Dopiero rewitalizacja przywróciła mu dawny wygląd.",
      ]),
       ("Warto wiedzieć", [
          "Obok stoją rzeźba Magdaleny Abakanowicz „5 Figur” i Pomnik Katyński w Ogrodzie Zamkowym.",
      ])],
      "Dziedziniec Różany Zamku Cesarskiego (od ul. Fredry / al. Niepodległości), 61-809 Poznań",
      ("poznan.pl: Fontanna Lwów", PF + "fontanna-lwow,41213.html"),
      [wiki("Fontanna Lwów w Poznaniu")],
      hours=[("Dostęp", "dziedziniec zamku, godzin nie podano w źródle")]),

    M("pomnik-katynski", "Pomnik Ofiar Katynia i Sybiru",
      "Pomnik Katyński w Ogrodzie Zamkowym",
      "Pomnik Katyński Roberta Sobocińskiego z 1999 roku w Ogrodzie Zamkowym.",
      "Pomnik Ofiar Katynia i Sybiru, zwany Pomnikiem Katyńskim, stoi w Ogrodzie Zamkowym przy Zamku Cesarskim, u zbiegu ulicy Fredry i alei Niepodległości. Odsłonięto go w 1999 roku.",
      [("O pomniku", [
          "Autorem jest poznański rzeźbiarz Robert Sobociński.",
          "Pomnik upamiętnia oficerów Wojska Polskiego i policjantów zamordowanych w 1940 roku w Katyniu, Charkowie i Miednoje, a także ofiary zsyłek na Sybir.",
      ]),
       ("Warto wiedzieć", [
          "Od 2014 roku cały ogród nosi imię Ofiar Katynia i Sybiru. Więcej o nim przeczytasz na stronie Ogrodu Zamkowego.",
      ])],
      "Ogród Zamkowy, ul. Fredry / al. Niepodległości, 61-701 Poznań",
      ("poznan.pl: Pomnik Ofiar Katynia i Sybiru", PM + "ofiar-katynia-i-sybiru,40376.html"),
      img="ogrod-zamkowy", credit="ogrod-zamkowy"),

    M("pomnik-panstwa-podziemnego", "Pomnik Polskiego Państwa Podziemnego",
      "Pomnik Polskiego Państwa Podziemnego z sylwetkami orłów",
      "Nowoczesny pomnik z 2007 roku: symboliczne ruiny, szklana krypta i orły zrywające się do lotu.",
      "Pomnik Polskiego Państwa Podziemnego i Armii Krajowej stoi na tyłach Teatru Wielkiego, na rogu alei Niepodległości i ulicy Libelta, na skraju Parku Wieniawskiego.",
      [("O pomniku", [
          "Zaprojektował go prof. Mariusz Kulpa z gdańskiej ASP, zwycięzca konkursu. Odsłonięto go 26 września 2007 roku w obecności m.in. ostatniego prezydenta RP na uchodźstwie Ryszarda Kaczorowskiego.",
          "Składa się z sześciu słupów pamięci z tablicami, oszklonej krypty symbolizującej zejście do podziemia i unoszących się nad nimi sylwetek orłów. Rdzawą blachę sprowadzono z Finlandii.",
          "Żeliwne tabliczki upamiętniają Wielkopolan, którzy zginęli od 1 września 1939 do 3 lipca 1945 roku.",
      ])],
      "al. Niepodległości / ul. Libelta, 61-714 Poznań",
      ("poznan.pl: Pomnik Polskiego Państwa Podziemnego", PM + "polskiego-panstwa-podziemnego,39373.html"),
      [wiki("Pomnik Polskiego Państwa Podziemnego w Poznaniu")]),

    M("pomnik-armii-poznan", "Pomnik Armii „Poznań”",
      "Pomnik Armii Poznań: strzeliste ostrza naprzeciw pochylonych brył",
      "Monumentalny pomnik z 1982 roku: polskie „bagnety” naprzeciw pancernych brył najeźdźcy.",
      "Pomnik bohaterów Armii „Poznań” z 1939 roku odsłonięto 1 września 1982 roku, w 43. rocznicę wybuchu II wojny światowej. Stoi u stóp Wzgórza św. Wojciecha, przy alei Niepodległości.",
      [("Symbolika", [
          "Pięć smukłych elementów skierowanych w górę symbolizuje polskie bagnety, które opierają się niemieckiej sile pancernej, przedstawionej jako cztery pochylone szare bryły.",
          "Na ścianach wypisano nazwy pól bitewnych i jednostek Armii „Poznań” oraz nazwiska kilkudziesięciu poległych. W środku jest wyrzeźbiony krzyż Virtuti Militari.",
      ]),
       ("Historia", [
          "Projekt Anny Rodzińskiej i architekta Józefa Iwiańskiego wygrał konkurs w 1978 roku, ale budowa latami się przeciągała. Władze proponowały inne lokalizacje, zarzucały też projektowi, że bryły najeźdźcy są za duże. Pomnik powstał dopiero w latach 1981–1982.",
      ])],
      "al. Niepodległości (u stóp Wzgórza św. Wojciecha), 61-747 Poznań",
      ("poznan.pl: Pomnik Armii „Poznań”", PM + "armii-poznan,40367.html"),
      [wiki("Pomnik Armii Poznań")]),

    M("pomnik-powstancow", "Pomnik Powstańców Wielkopolskich",
      "Granitowy obelisk Pomnika Powstańców Wielkopolskich",
      "17-metrowy obelisk z 1965 roku, upamiętniający zwycięskie powstanie z lat 1918–1919.",
      "Pomnik upamiętnia powstanie wielkopolskie, jedyne zwycięskie polskie powstanie, które trwało od 27 grudnia 1918 do 16 lutego 1919 roku. Stoi u zbiegu ulic Królowej Jadwigi i Wierzbięcice, na skraju Parku Drwęskich.",
      [("O pomniku", [
          "Zaprojektował go Alfred Wiśniewski z gdańskiej uczelni plastycznej. Odsłonięto go 19 września 1965 roku.",
          "Obelisk ma 17 metrów wysokości i jest pokryty szarym granitem. Płaskorzeźby przedstawiają orła oraz sceny z walki o polskość: strajk dzieci we Wrześni, wóz Drzymały, Marcina Kasprzaka i śmierć pierwszego powstańca, Franciszka Ratajczaka.",
          "Obok stoją figury dwóch powstańców: oficera z szablą i szeregowca z karabinem. W 1988 roku wokół pomnika urządzono plac apelowy.",
      ]),
       ("Warto wiedzieć", [
          "Powstanie wybuchło dzień po przemówieniu Ignacego Jana Paderewskiego przed Hotelem Bazar. Jego historię opowiada Muzeum Powstania Wielkopolskiego na Starym Rynku.",
          "Stąd jest około 300 metrów do Starego Browaru.",
      ])],
      "ul. Królowej Jadwigi / ul. Wierzbięcice, 61-871 Poznań",
      ("poznan.pl: Pomnik Powstańców Wielkopolskich", PM + "powstancow-wielkopolskich,40373.html"),
      [wiki("Pomnik Powstańców Wielkopolskich")]),

    M("pomnik-15-pulku-ulanow", "Pomnik 15. Pułku Ułanów Poznańskich",
      "Pomnik ułana walczącego ze smokiem przy ulicy Ludgardy",
      "Ułan walczący ze smokiem na wysokiej kolumnie, u stóp Góry Przemysła.",
      "Pomnik przedstawia ułana walczącego ze smokiem na wysokim cokole. Stoi przy ulicy Ludgardy, obok klasztoru franciszkanów, na zboczu Góry Przemysła.",
      [("Historia", [
          "Upamiętnia żołnierzy 15. Pułku Ułanów Poznańskich, który walczył m.in. z bolszewikami w 1920 roku i we wrześniu 1939 roku w składzie Armii „Poznań”.",
          "Rzeźbę Mieczysława Lubelskiego odsłonięto w 1927 roku. Przed wojną smok miał na głowie czapkę z czerwoną gwiazdą, symbol bolszewizmu.",
          "Niemcy zniszczyli pomnik w 1939 roku. Rekonstrukcję wykonali Józef Murlewski i Benedykt Kasznia, a ponowne odsłonięcie odbyło się w 1982 roku.",
      ]),
       ("Warto wiedzieć", [
          "To jedno z głównych miejsc uroczystości patriotycznych w Poznaniu, m.in. podczas Dni Ułana.",
      ])],
      "ul. Ludgardy / ul. Paderewskiego, 61-709 Poznań",
      ("poznan.pl: Pomnik 15. Pułku Ułanów Poznańskich", PM + "15-pulku-ulanow-poznanskich,40374.html"),
      [wiki("Pomnik 15. Pułku Ułanów Poznańskich")]),

    M("fontanna-higiei", "Fontanna Higiei",
      "Fontanna z posągiem bogini Higiei przed Biblioteką Raczyńskich",
      "Posąg bogini zdrowia na placu Wolności, pamiątka po pierwszym poznańskim wodociągu z 1840 roku.",
      "Fontanna Higiei stoi na placu Wolności przed Biblioteką Raczyńskich. Jej historia zaczyna się od wodociągu, który w 1840 roku zbudowano w dużej mierze za pieniądze Edwarda Raczyńskiego.",
      [("Historia", [
          "Po budowie wodociągu w mieście ustawiono cztery studnie. Najważniejszą miała zdobić figura Higiei, greckiej bogini zdrowia. Cokół zaprojektował berliński architekt Christian Gottlieb Cantian.",
          "Siedząca bogini w antycznym stroju ma rysy Konstancji Raczyńskiej, żony fundatora. Woda wypływa z lwiej głowy w cokole.",
          "Fontannę kilka razy przenoszono. Przed Bibliotekę Raczyńskich trafiła w 1971 roku. Na czas budowy parkingu podziemnego zdjęto ją, a po renowacji wróciła na plac w 2009 roku.",
      ]),
       ("Co zobaczyć", [
          "Medalion z wizerunkiem Wincentego Priessnitza, pioniera wodolecznictwa, z napisem po grecku i po polsku „Nic lepszego nad wodę”. W polskim napisie brakuje litery „s”.",
      ])],
      "pl. Wolności (przed Biblioteką Raczyńskich), 61-739 Poznań",
      ("poznan.pl: Fontanna Higiei", PF + "fontanna-higiei,41215.html"),
      [wiki("Fontanna Higiei w Poznaniu")]),

    M("fontanna-z-delfinami", "Fontanna z delfinami (Studzienka Kronthala)",
      "Chłopiec na delfinie, fragment fontanny w Alejach Marcinkowskiego",
      "Fontanna z 1909 roku z miedzianymi chłopcami na delfinach, w Alejach Marcinkowskiego.",
      "Fontanna z delfinami, nazywana też Studzienką Kronthala lub Fontanną Lederera, stoi w Alejach Marcinkowskiego, blisko skrzyżowania z ulicą 23 Lutego.",
      [("Historia", [
          "Wcześniej stała tu miejska studnia ufundowana przez Edwarda Raczyńskiego. W 1909 roku zastąpiła ją fontanna berlińskiego rzeźbiarza Hugona Lederera. Projekt osobiście zatwierdzał cesarz Wilhelm II.",
          "Fundatorem był kupiec Gustaw Kronthal, stąd jedna z nazw fontanny. W 2006 roku przeszła gruntowną renowację.",
      ]),
       ("Co zobaczyć", [
          "Kamienną nieckę z muszlowca i miedziane rzeźby chłopców na delfinach na krańcach balustrady.",
          "Według dziennikarza Adama Pleskaczyńskiego „delfiny” to w rzeczywistości sumy, o czym ma świadczyć budowa ich pysków.",
          "Tuż obok stoją pomnik Karola Marcinkowskiego i rzeźba Golema.",
      ])],
      "al. Marcinkowskiego / ul. 23 Lutego, 61-745 Poznań",
      ("poznan.pl: Fontanna Kronthala (Studzienka z delfinami)", PF + "fontanna-kronthala-studzienka-z-delfinami,41212.html"),
      [wiki("Fontanna z delfinami w Poznaniu")]),

    M("pomnik-marcinkowskiego", "Pomnik Karola Marcinkowskiego",
      "Pomnik Karola Marcinkowskiego w Alejach Marcinkowskiego",
      "Pomnik lekarza i społecznika, twórcy pracy organicznej, odsłonięty w 2005 roku.",
      "Pomnik Karola Marcinkowskiego, lekarza i społecznika, stoi u zbiegu Alej Marcinkowskiego i ulicy 23 Lutego. Odsłonięto go w 2005 roku.",
      [("O pomniku", [
          "Zaprojektował go gdański rzeźbiarz Stanisław Radwański. Marcinkowski stoi w długim płaszczu z epoki, z laską w dłoni, na wysokim cokole z granitu.",
          "Napis na cokole głosi: „Karol Marcinkowski – twórca pracy organicznej”.",
      ]),
       ("Warto wiedzieć", [
          "Marcinkowski był jednym z założycieli Hotelu Bazar, ośrodka polskiego życia w XIX-wiecznym Poznaniu.",
          "Obok są Fontanna z delfinami i gmach poczty. Drugi pomnik Marcinkowskiego stoi przed I Liceum Ogólnokształcącym przy ulicy Bukowskiej.",
      ])],
      "al. Marcinkowskiego / ul. 23 Lutego, 61-745 Poznań",
      ("poznan.pl: Pomnik Karola Marcinkowskiego", PM + "karola-marcinkowskiego,40371.html"),
      [wiki("Pomnik Karola Marcinkowskiego w Poznaniu")]),

    M("pomnik-janickiego", "Pomnik Klemensa Janickiego",
      "Pomnik siedzącego poety Klemensa Janickiego na kolumnie",
      "Renesansowy poeta z piórem w dłoni, na kolumnie przy ulicy 23 Lutego, z napisem „Zapomnianym poetom”.",
      "Pomnik Klemensa Janickiego, renesansowego poety piszącego po łacinie, stoi u zbiegu ulic 23 Lutego i Masztalarskiej, blisko Starego Rynku. Odsłonięto go w grudniu 2015 roku.",
      [("O pomniku", [
          "Janicki, urodzony w 1516 roku, uczył się w poznańskiej Akademii Lubrańskiego i tu powstały jego pierwsze utwory.",
          "Poeta siedzi na kufrze, z piórem i arkuszem w rękach. Figura z brązu stoi na 2,5-metrowej kolumnie z piaskowca, a cały pomnik ma około 4 metrów wysokości.",
          "Autorami są Joanna Buczak i Dariusz Wieczerzak, których projekt wygrał konkurs Towarzystwa Opieki nad Zabytkami. Na cokole widnieje napis „Zapomnianym poetom”.",
      ])],
      "ul. 23 Lutego / ul. Masztalarska, 61-744 Poznań",
      ("poznan.pl: Pomnik Klemensa Janickiego", PM + "klemensa-janickiego,60787.html"),
      [wiki("Pomnik Klemensa Janickiego w Poznaniu")]),

    M("pomnik-jana-pawla-ii", "Pomnik Jana Pawła II",
      "Pomnik Jana Pawła II na Ostrowie Tumskim",
      "Pomnik papieża z 2000 roku przed dawnym probostwem katedralnym na Ostrowie Tumskim.",
      "Pomnik Jana Pawła II stoi na Ostrowie Tumskim, przed dawnym probostwem katedralnym, w pobliżu archikatedry. Odsłonięto go w 2000 roku.",
      [("O pomniku", [
          "Jest dziełem rzeźbiarki Krystyny Fałygi-Solskiej.",
          "Upamiętnia m.in. spotkanie papieża z kapłanami archidiecezji poznańskiej w katedrze w 1983 roku, w czasie jego drugiej pielgrzymki do Polski.",
      ]),
       ("Warto wiedzieć", [
          "Mszę dla około miliona wiernych papież odprawił wtedy na Łęgach Dębińskich, dziś Parku Jana Pawła II.",
      ])],
      "Ostrów Tumski, 61-109 Poznań",
      ("poznan.pl: Pomnik Jana Pawła II", PM + "jana-pawla-ii,40369.html")),

    M("pomnik-kochanowskiego", "Pomnik Jana Kochanowskiego",
      "Obelisk Jana Kochanowskiego z medalionem przed Akademią Lubrańskiego",
      "Obelisk z 1885 roku z medalionem poety, przed Akademią Lubrańskiego na Ostrowie Tumskim.",
      "Pomnik Jana Kochanowskiego ma formę obelisku z medalionem. Stoi na Ostrowie Tumskim, na skwerze przed Akademią Lubrańskiego.",
      [("Historia", [
          "Kamień węgielny wmurowano w 1884 roku, w 300. rocznicę śmierci poety, a pomnik odsłonięto w 1885 roku. Obelisk zaprojektował Antoni Krzyżanowski, a medalion z portretem wykonał Wiktor Brodzki. Pieniądze zebrano w zbiórce publicznej.",
          "Niemcy zniszczyli pomnik w 1940 roku. W 1984 roku odtworzono go według projektu Jerzego Sobocińskiego, a w 2002 roku przeniesiono w obecne miejsce.",
      ]),
       ("Ciekawostka", [
          "W latach 1564–1574 Kochanowski był prepozytem poznańskiej kapituły katedralnej, co dawało mu duże dochody. Według Wikipedii sam nigdy nie przebywał w Poznaniu.",
      ])],
      "ul. Lubrańskiego 1 (przed Akademią Lubrańskiego), 61-108 Poznań",
      ("poznan.pl: Pomnik Jana Kochanowskiego", PM + "jana-kochanowskiego,40368.html"),
      [wiki("Pomnik Jana Kochanowskiego w Poznaniu")]),

    M("pomnik-cegielskiego", "Pomnik Hipolita Cegielskiego",
      "Pomnik Hipolita Cegielskiego opartego o maszynę parową",
      "Przemysłowiec oparty o maszynę parową, przy placu Wiosny Ludów. Pomnik z 2009 roku.",
      "Pomnik Hipolita Cegielskiego, przemysłowca i twórcy polskiego patriotyzmu gospodarczego, stoi na rogu ulic Święty Marcin i Podgórnej, przy placu Wiosny Ludów.",
      [("O pomniku", [
          "Odsłonięto go 19 września 2009 roku. Zaprojektował go poznański rzeźbiarz Krzysztof Jakubik, a fundatorem było Towarzystwo im. Hipolita Cegielskiego.",
          "Cegielski stoi oparty o maszynę parową, symbol swoich zakładów, z których wyrosły słynne Zakłady Cegielskiego (HCP).",
          "Pomysł upamiętnienia Cegielskiego pojawił się już w okresie międzywojennym, ale zrealizowano go dopiero po 2000 roku.",
      ]),
       ("Warto wiedzieć", [
          "Pierwsze zakłady Cegielskiego działały przy pobliskiej ulicy Koziej, a później przy Strzeleckiej.",
      ])],
      "ul. Święty Marcin / ul. Podgórna, 61-829 Poznań",
      ("poznan.pl: Pomnik Hipolita Cegielskiego", PM + "hipolita-cegielskiego,51453.html"),
      [wiki("Pomnik Hipolita Cegielskiego w Poznaniu")]),

    M("pomnik-paderewskiego", "Pomnik Ignacego Jana Paderewskiego",
      "Figura Paderewskiego przed szklaną fasadą Akademii Muzycznej",
      "Pomnik pianisty i męża stanu przed Akademią Muzyczną jego imienia, odsłonięty w 2015 roku.",
      "Figura Ignacego Jana Paderewskiego stoi przed budynkiem Akademii Muzycznej w Poznaniu, której jest patronem. Odsłonięto ją w 2015 roku, w 155. rocznicę urodzin Paderewskiego.",
      [("O pomniku", [
          "Zaprojektował ją poznański rzeźbiarz Rafał Nowak.",
          "Pomnik sfinansowano z darowizn osób prywatnych i firm. W tym samym roku uczelnia świętowała 95-lecie.",
      ]),
       ("Warto wiedzieć", [
          "Paderewski był pianistą, kompozytorem i politykiem. Jego przemówienie przed Hotelem Bazar 26 grudnia 1918 roku poprzedziło wybuch powstania wielkopolskiego.",
      ])],
      "ul. Święty Marcin 87 (przed Akademią Muzyczną), 61-808 Poznań",
      ("poznan.pl: Pomnik Paderewskiego", PM + "pomnik-paderewskiego,65724.html"),
      img=True),

    M("pomnik-ratajskiego", "Pomnik Cyryla Ratajskiego",
      "Siedząca figura Cyryla Ratajskiego przed Poznańskim Centrum Finansowym",
      "Pomnik zasłużonego przedwojennego prezydenta Poznania z 2002 roku, przy placu Andersa.",
      "Pomnik Cyryla Ratajskiego, przedwojennego prezydenta Poznania, stoi na placu Andersa przed Poznańskim Centrum Finansowym, od strony ulicy Półwiejskiej.",
      [("O pomniku", [
          "Odsłonięto go 23 kwietnia 2002 roku w obecności wnuczki Ratajskiego i trzech powojennych prezydentów miasta. Autorem jest warszawski rzeźbiarz Jan Kucz.",
          "Nazwiska sponsorów wpisano do księgi pamiątkowej, przekazanej potem do muzeum historii miasta.",
      ]),
       ("Warto wiedzieć", [
          "To kilka kroków od Starego Browaru i deptaka na Półwiejskiej z pomnikiem Starego Marycha.",
      ])],
      "pl. Andersa 5, 61-894 Poznań",
      ("poznan.pl: Pomnik Cyryla Ratajskiego", PM + "cyryla-ratajskiego,40375.html"),
      [wiki("Pomnik Cyryla Ratajskiego w Poznaniu")]),

    M("pomnik-kosciuszki", "Pomnik Tadeusza Kościuszki",
      "Pomnik Tadeusza Kościuszki na skwerze przy ulicy Grunwaldzkiej",
      "Pomnik odlany z brązu dzwonu Zamku Cesarskiego, na skwerze przy ulicach Grunwaldzkiej i Bukowskiej.",
      "Pomnik Tadeusza Kościuszki stoi na skwerze u zbiegu ulic Grunwaldzkiej i Bukowskiej. To powojenna rekonstrukcja pomnika z 1930 roku.",
      [("Historia", [
          "Pomnik zaprojektowała Zofia Trzcińska-Kamińska na Powszechną Wystawę Krajową w 1929 roku. Po wystawie gipsowy posąg zastąpiono brązowym, odsłoniętym 27 grudnia 1930 roku, w rocznicę wybuchu powstania wielkopolskiego.",
          "Niemcy zniszczyli pomnik w czasie wojny. Autorka sama go odtworzyła, a w 1967 roku stanął w obecnym miejscu.",
          "Według Wikipedii do odlewu użyto dzwonu z wieży zegarowej Zamku Cesarskiego, który spadł w czasie walk w 1945 roku.",
      ])],
      "ul. Grunwaldzka / ul. Bukowska, 60-809 Poznań",
      ("poznan.pl: Pomnik Tadeusza Kościuszki", PM + "tadeusza-kosciuszki,40370.html"),
      [wiki("Pomnik Tadeusza Kościuszki w Poznaniu")]),

    M("pomnik-komedy", "Pomnik Krzysztofa Komedy",
      "Brązowa figura Krzysztofa Komedy oglądającego klatki filmowe",
      "Kompozytor jazzowy z kamertonem przy uchu, przed Uniwersytetem Medycznym, który ukończył.",
      "Pomnik Krzysztofa Komedy-Trzcińskiego, kompozytora jazzu i muzyki filmowej, stoi przed Centrum Kongresowo-Dydaktycznym Uniwersytetu Medycznego. Komeda ukończył poznańską uczelnię medyczną i był laryngologiem.",
      [("O pomniku", [
          "Odsłonięto go 19 listopada 2010 roku, na 90-lecie uczelni. Zaprojektował go Adam Dawczak-Dębicki.",
          "Brązowa figura trzyma kamerton przy uchu i ogląda „pod światło” szklane klatki filmowe ze zdjęciami z filmów, do których Komeda pisał muzykę.",
          "W 2012 roku wandale przewrócili i połamali rzeźbę. Po renowacji wróciła na miejsce w tym samym roku.",
      ])],
      "Uniwersytet Medyczny, ul. Przybyszewskiego 49 / ul. Bukowska, 60-355 Poznań",
      ("poznan.pl: Pomnik Krzysztofa Komedy Trzcińskiego", PM + "krzysztofa-komedy-trzcinskiego,51796.html"),
      [wiki("Pomnik Krzysztofa Komedy-Trzcińskiego w Poznaniu")]),

    M("wiedzma-z-chwaliszewa", "Wiedźma z Chwaliszewa",
      "",
      "Lustrzana rzeźba ze stali w Parku Stare Koryto Warty, upamiętniająca kobietę spaloną na stosie w 1511 roku.",
      "„Wiedźma z Chwaliszewa” to pomnik pierwszej kobiety na ziemiach polskich, która według przekazów została oskarżona o czary i spalona na stosie. Stoi w Parku Stare Koryto Warty na Chwaliszewie.",
      [("Historia", [
          "Według przekazów w 1511 roku na Chwaliszewie, wtedy osobnym miasteczku z browarami, oskarżono znachorkę o zatrucie wody używanej do warzenia piwa i spalono ją na stosie.",
          "Niezależnie od tego, na ile ta historia jest potwierdzona, stała się symbolem prześladowań kobiet oskarżanych o czary.",
      ]),
       ("O rzeźbie", [
          "Rzeźba z polerowanej, trawionej kwasem stali ma około 166 cm, czyli średni wzrost kobiety w Polsce. Przedstawia zarys postaci bez rysów twarzy, a w jej lustrzanej powierzchni można się przejrzeć.",
          "Pomysł wyszedł od Ewy Łowżył, założycielki Chóru Czarownic, a rzeźbę zaprojektowała poznańska artystka Alicja Biała.",
      ])],
      "Park Stare Koryto Warty, 61-124 Poznań",
      ("poznan.pl: Wiedźma z Chwaliszewa", PM + "wiedzma-z-chwaliszewa,86852.html"),
      [("Malta Festival: Wiedźma z Chwaliszewa", "https://malta-festival.pl/wiedzmazchwaliszewa")],
      img=None),

    M("fontanna-park-wilsona", "Fontanna w Parku Wilsona",
      "Fontanna w kształcie ośmioramiennej gwiazdy w Parku Wilsona",
      "Fontanna w kształcie gwiazdy z 1929 roku, zbudowana na Powszechną Wystawę Krajową.",
      "Fontanna w Parku Wilsona stoi w centralnej części parku, między muszlą koncertową, rzeźbą „Perseusz i Andromeda” a Palmiarnią.",
      [("Historia", [
          "Powstała w 1929 roku i została uruchomiona w czasie Powszechnej Wystawy Krajowej (PeWuKa), która pokazywała osiągnięcia odrodzonej Polski. Zaprojektował ją architekt Roger Sławski.",
      ]),
       ("Co zobaczyć", [
          "Fontanna ma kształt ośmioramiennej gwiazdy, a woda tryska z jej środka. Wieczorem jest podświetlana kolorowymi światłami.",
      ])],
      "Park Wilsona, ul. Śniadeckich 30, 61-001 Poznań Poznań",
      ("poznan.pl: Fontanna w Parku Wilsona", PF + "fontanna-w-parku-wilsona,41214.html"),
      hours=[("Park", "codziennie 5:00–22:00")]),

    M("studzienka-taschnera", "Studzienka Taschnera",
      "Rzeźbiona kolumna Studzienki Taschnera na dziedzińcu przy ulicy Mostowej",
      "Bogato rzeźbiona fontanna z 1908 roku, dziś w ogrodzie Muzeum Kultur Świata.",
      "Studzienka Taschnera stoi na dziedzińcu Muzeum Kultur Świata przy ulicy Mostowej 7. To jedna z mniej znanych, ale najbardziej ozdobnych fontann w mieście.",
      [("Historia", [
          "Odsłonięto ją w 1908 roku na dziedzińcu dzisiejszego Urzędu Miasta przy placu Kolegiackim. Zaprojektował ją berliński rzeźbiarz Ignatius Taschner.",
          "W 1965 roku studzienkę rozebrano i złożono w magazynie na Cytadeli. Dzięki zbiórce Towarzystwa Opieki nad Zabytkami odrestaurowano ją i w 1992 roku ustawiono w obecnym miejscu.",
      ]),
       ("Co zobaczyć", [
          "Kolumnę w ośmiokątnym basenie: na dole maszkarony, wyżej dzieci na delfinach, a na szczycie chłopiec obejmujący wielką rybę.",
          "Płaskorzeźby na ścianach basenu, pokazujące różne sposoby wykorzystania wody.",
      ])],
      "ul. Mostowa 7 (dziedziniec Muzeum Bamberskiego), 61-854 Poznań",
      ("poznan.pl: Studzienka Taschnera", PF + "studzienka-taschnera,41216.html"),
      [wiki("Studzienka Taschnera w Poznaniu")],
      hours=[("Dostęp", "dziedziniec muzeum, godzin nie podano w źródle")]),
]
