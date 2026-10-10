"""Dziennik zmian: co wpływa na plany zwiedzających.

Zamknięcia, remonty i sezonowe ograniczenia NIE są tu przepisywane: strona bierze je z pola status kart atrakcji
(site_data i pliki data_*), więc zmiana na karcie od razu zmienia dziennik. Tu są tylko wpisy, które nie mają
swojej karty ze statusem: zmiany cen, nazw i zasad oraz ogłoszone terminy.
Każdy wpis ma źródło; fakty muszą zgadzać się z tym, co jest na karcie atrakcji lub w kalendarzu.
"""

# slug karty -> sekcja
CLOSED = ["palmiarnia", "stary-rynek", "muzeum-komunikacji-mpk", "muzeum-kultury-cyfrowej"]
SEASONAL = ["zamek-kornik", "ostrow-lednicki", "wpe-dziekanowice", "szreniawa", "grod-pobiedziska", "linie-turystyczne"]

# Zmiany cen, nazw, zasad i terminy. when = tekst widoczny, sort = ISO do sortowania (najnowsze na górze).
RULES = [
    dict(sort="2026-10-05", when="stan na 5.10.2026", kind="Termin",
         title="Betlejem Poznańskie 2026/27: znane terminy",
         text="Jarmark na Placu Wolności rusza 20 listopada 2026, na Starym Rynku 21 listopada 2026. Oba trwają do 6 stycznia 2027. To jedyny jarmark, który miasto dopuszcza na Starym Rynku.",
         page=("kalendarz.html#betlejem", "Kalendarz wydarzeń"),
         src=("Betlejem Poznańskie (organizator)", "https://betlejempoznanskie.pl/")),
    dict(sort="2026-02-01", when="od 1.02.2026", kind="Zasady",
         title="Muzeum Poznańskiego Czerwca 1956: nowa organizacja",
         text="Od 1 stycznia 2026 muzeum jest samodzielną instytucją kultury, a po przerwie otworzyło się ponownie 1 lutego 2026. Dzień wstępu wolnego przeniesiono z wtorku na niedzielę. Ceny biletów się nie zmieniły (15 i 10 zł).",
         page=("atrakcje/muzeum-czerwca-1956.html", "Muzeum Poznańskiego Czerwca 1956"),
         src=("Muzeum: komunikat o ponownym otwarciu", "https://www.wmn.poznan.pl/moje-aktualnosci/muzeum-powstania-poznanskiego-czerwiec-1956-w-poznaniu-ponownie-otwiera-sie-dla-zwiedzajacych/")),
    dict(sort="2026-01-02", when="od 2.01.2026", kind="Ceny",
         title="Rogalowe Muzeum Poznania: nowy cennik",
         text="Dla zwiedzających indywidualnych pokaz rogalowy kosztuje 41 zł (ulgowy 37 zł), a pokaz z herbami 47 zł (ulgowy 43 zł). Wyszukiwarki często pokazują jeszcze stare, niższe ceny.",
         page=("atrakcje/rogalowe-muzeum.html", "Rogalowe Muzeum Poznania"),
         src=("Rogalowe Muzeum: dla indywidualnych", "https://rogalowemuzeum.pl/indywidualni/")),
    dict(sort="2025-11-11", when="od 2025", kind="Zasady",
         title="Imieniny Ulicy Święty Marcin: bez korowodu w dawnej formie",
         text="W 2025 roku na ulicy powstało ogrodzone „imieninowe miasteczko” z czterema bramami i kontrolą przy wejściu (wstęp bezpłatny, bagaże w depozycie przy bramie). Na 2026 rok organizator podał na razie tylko, że Kiermasz Świętomarciński 11 listopada (11:00–21:00) odbędzie się w zmienionej formule, na terenie imprezy masowej. Zasady wejścia sprawdź na stronie CK Zamek.",
         page=("kalendarz.html#imieniny-sw-marcin", "Kalendarz wydarzeń"),
         src=("Centrum Kultury Zamek: Imieniny Ulicy Święty Marcin", "https://ckzamek.pl/podstrony/71-imieniny-ulicy-swiety-marcin/")),
    dict(sort="2025-01-01", when="od 2025", kind="Nazwa",
         title="Muzeum Etnograficzne to teraz Muzeum Kultur Świata",
         text="Oddział Muzeum Narodowego zmienił nazwę w 2025 roku. Mieści się w tym samym budynku dawnej loży masońskiej. Przy starej nazwie nadal bywa opisywany w wielu miejscach.",
         page=("atrakcje/muzeum-kultur-swiata.html", "Muzeum Kultur Świata"),
         src=("poznan.pl: Muzeum Kultur Świata", "https://www.poznan.pl/mim/turystyka/muzea-w-poznaniu,poi,202,12/muzeum-etnograficzne-oddzial-muzeum-narodowego,15728.html")),
]
