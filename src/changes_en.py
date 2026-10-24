"""Angielskie teksty strony „What has changed” (odpowiednik zmiany.html).

Zamknięcia, remonty i sezonowe ograniczenia bierze build_en z angielskich kart atrakcji (pole status),
więc tu są tylko tłumaczenia wpisów z data_changes.RULES (klucz = pole sort wpisu).
Po zmianie polskiej strony: przejrzeć ten plik, potem python src/check_en.py --stamp-changes.
"""

KIND = {"Termin": "Date", "Zasady": "Rule", "Ceny": "Prices", "Nazwa": "Name"}

RULES_EN = {
    "2026-10-05": dict(
        when="as of 5 October 2026",
        title="Betlejem Poznańskie 2026/27: known dates",
        text="The fair on Plac Wolności opens on 20 November 2026 and the one on the Old Market Square on 21 November 2026. Both run until 6 January 2027. It is the only Christmas fair the city allows on the Old Market Square.",
        page=("calendar.html#betlejem", "Events calendar"),
        src="Betlejem Poznańskie (organiser)"),
    "2026-02-01": dict(
        when="from 1 February 2026",
        title="Museum of the Poznań June 1956: new organisation",
        text="Since 1 January 2026 the museum has been an independent cultural institution, and after a break it reopened on 1 February 2026. The free-entry day was moved from Tuesday to Sunday. Ticket prices have not changed (PLN 15 and 10).",
        page=("attractions/muzeum-czerwca-1956.html", None),
        src="Museum: announcement of the reopening"),
    "2026-01-02": dict(
        when="from 2 January 2026",
        title="St Martin's Croissant Museum: new price list",
        text="For individual visitors the croissant show costs PLN 41 (reduced PLN 37), and the croissant-and-goats show PLN 47 (reduced PLN 43). Search engines often still show the old, lower prices.",
        page=("attractions/rogalowe-muzeum.html", None),
        src="Croissant Museum: for individual visitors"),
    "2025-11-11": dict(
        when="from 2025",
        title="St Martin Street Name Day: no parade in its old form",
        text="In 2025 a fenced “name-day town” with four gates and an entry check was set up on the street (free admission, luggage left at the gate). For 2026 the organiser has so far announced only that the St Martin's Fair on 11 November (11:00–21:00) will take place in a changed format, within a mass-event area. Check the entry rules on the Zamek Culture Centre website.",
        page=("calendar.html#imieniny-sw-marcin", "Events calendar"),
        src="Zamek Culture Centre: St Martin Street Name Day"),
    "2025-01-01": dict(
        when="from 2025",
        title="The Ethnographic Museum is now the Museum of World Cultures",
        text="This branch of the National Museum changed its name in 2025. It is in the same building of the former Masonic lodge. Under the old name it is still described in many places.",
        page=("attractions/muzeum-kultur-swiata.html", None),
        src="poznan.pl: Museum of World Cultures"),
}
