# -*- coding: utf-8 -*-
"""Angielska strona „Museums” (/en/museums). Tabela jest liczona z polskich danych atrakcji (museums_table.derive),
a nazwy, godziny i ceny bierzemy z angielskich tłumaczeń: dla muzeów przetłumaczonych w pełni z data_en.EN,
dla pozostałych stąd (MUSEUMS_EN: tylko nazwa, godziny i ceny, w tej samej kolejności wierszy co po polsku).
Po zmianie polskich danych muzeów: zaktualizuj ten plik i uruchom: python src/check_en.py --stamp-museums"""

DAY_EN = {"pn": "Monday", "wt": "Tuesday", "sr": "Wednesday", "cz": "Thursday", "pt": "Friday", "sb": "Saturday", "nd": "Sunday"}

MUSEUMS_EN = {
    "muzeum-kultur-swiata": dict(
        name="Museum of World Cultures",
        hours=[("Monday", "closed"), ("Tuesday–Wednesday", "10:00–16:00"), ("Thursday", "10:00–18:00"),
               ("Friday", "10:00–20:00"), ("Saturday–Sunday", "10:00–17:00")],
        tickets=[("Standard", "PLN 20"), ("Reduced", "PLN 13"), ("Children and young people aged 8–26", "PLN 1"),
                 ("Tuesday", "free admission")],
    ),
    "muzeum-sienkiewicza": dict(
        name="Henryk Sienkiewicz Literary Museum",
        hours=[("Tuesday, Friday, Saturday", "9:00–16:00"), ("Wednesday, Thursday", "12:00–19:00"),
               ("Monday, Sunday, public holidays", "closed")],
        tickets=[("Standard", "PLN 10"), ("Reduced", "PLN 5"), ("Saturday", "free admission")],
    ),
    "muzeum-bambrow": dict(
        name="Museum of the Poznań Bambers",
        hours=[("Friday and Saturday", "10:00–14:00")],
        tickets=[("Guided tour", "free, by appointment")],
    ),
    "muzeum-wojskowe": dict(
        name="Greater Poland Military Museum",
        hours=[("Monday", "closed"), ("Tuesday–Wednesday", "10:00–16:00"), ("Thursday", "10:00–18:00"),
               ("Friday", "10:00–20:00"), ("Saturday–Sunday", "10:00–17:00")],
        tickets=[("Standard", "PLN 15"), ("Reduced", "PLN 10"), ("Children and young people aged 8–26", "PLN 1"),
                 ("Tuesday", "free admission"), ("With the Poznań Tourist Card", "free")],
    ),
    "muzeum-pyry": dict(
        name="Poznań Potato Museum (Muzeum Pyry)",
        hours=[("Tuesday–Sunday", "hours in the booking system"), ("Monday", "closed")],
        tickets=[("Standard", "PLN 31"), ("Reduced", "PLN 29"), ("Family (3 or more people)", "PLN 28 per person"),
                 ("In English", "PLN 35"), ("Children under 4", "free")],
    ),
    "akademia-lubranskiego": dict(
        name="Archdiocesan Museum – Lubrański Academy",
        hours=[("Tuesday–Friday", "11:00–17:00"), ("Saturday", "11:00–16:00"), ("Sunday", "11:00–15:00")],
        tickets=[("Ticket prices", "at akademialubranskiego.pl"), ("Ticket for 3 places on the island", "PLN 49")],
    ),
    "muzeum-farmacji": dict(
        name="Museum of Pharmacy",
        hours=[("Thursday", "10:00–17:00"), ("Other days", "closed")],
        tickets=[("Admission", "free")],
    ),
    "muzeum-historii-ubioru": dict(
        name="Museum of the History of Clothing",
        hours=[("Tuesday, Wednesday, Friday", "10:00–15:00"), ("Thursday", "15:00–19:00"), ("Saturday", "11:00–16:00"),
               ("Sunday–Monday", "closed")],
        tickets=[("Standard", "PLN 20"), ("Reduced", "PLN 15"), ("Children under 7", "free")],
    ),
    "muzeum-iluzji": dict(
        name="Museum of Illusions, Science and Art",
        hours=[("Monday", "closed"), ("Tuesday–Sunday", "10:00–19:00")],
        tickets=[("Ticket prices", "at muzeumins.pl")],
    ),
    "muzeum-komunikacji-mpk": dict(
        name="MPK Urban Transport Museum",
        hours=[("Currently", "closed until further notice")],
        tickets=[("Currently", "no visits")],
    ),
    "muzeum-prl": dict(
        name="Museum of the Polish People's Republic (PRL Museum)",
        hours=[("Monday", "closed"), ("Tuesday–Sunday", "10:00–18:00")],
        tickets=[("Standard", "PLN 35"), ("Reduced", "PLN 31"), ("Family (min. 2 adults + child)", "PLN 27 per person"),
                 ("Children under 3", "free")],
    ),
    "schron-przeciwatomowy": dict(
        name="Nuclear Shelter and Poster Gallery",
        hours=[("Wednesday–Friday", "10:00–16:00"), ("Last Saturday of the month", "10:00–16:00")],
        tickets=[("Standard", "PLN 15"), ("Reduced", "PLN 10")],
    ),
    "gaspar": dict(
        name="GASPAR Museum of Old Tools and Machines",
        hours=[("Selected weekends", "dates at gaspar.org.pl"), ("Other days", "by appointment")],
        tickets=[("Ticket prices", "at gaspar.org.pl")],
    ),
    "muzeum-czekolady": dict(
        name="Chocolate Museum",
        hours=[("Daily", "10:00–18:00"), ("Saturday", "until 19:00"), ("Sunday", "from 11:00")],
        tickets=[("Visit with a workshop", "PLN 65 per person (children and adults)")],
    ),
    "izba-prl-w7": dict(
        name="PRL Room in the former Hall W7",
        hours=[("Visits", "by prior appointment")],
        tickets=[("Admission", "free")],
    ),
    "muzeum-ump": dict(
        name="Poznań University of Medical Sciences Museum",
        hours=[("Exhibitions", "during the opening hours of the university buildings")],
        tickets=[("Admission", "free")],
    ),
    "muzeum-ziemi": dict(
        name="Earth Museum of Adam Mickiewicz University",
        hours=[("Hours", "variable, calendar at muzeumziemi.amu.edu.pl")],
        tickets=[("Admission", "free")],
    ),
    "salon-nowowiejskiego": dict(
        name="Feliks Nowowiejski Music Salon",
        hours=[("Tuesday–Saturday", "10:00–16:00"), ("Sunday–Monday", "closed")],
        tickets=[("Standard", "PLN 15"), ("Reduced", "PLN 13")],
    ),
    "muzeum-kultury-cyfrowej": dict(
        name="Poznań Museum of Digital Culture",
        hours=[("Currently", "closed")],
        tickets=[("Currently", "no visits")],
    ),
    "muzeum-bizuterii-moja": dict(
        name="MoJA Jewellery Museum",
        hours=[("Tuesday", "closed"), ("Other days", "10:00–18:00")],
        tickets=[("Standard", "PLN 35"), ("Reduced", "PLN 15"), ("Children under 6", "free")],
    ),
    "mieszkanie-illakowiczowny": dict(
        name="Kazimiera Iłłakowiczówna Apartment-Studio",
        hours=[("Individual visitors", "2nd and last Wednesday of the month, 12:30"), ("Groups", "by reservation")],
        tickets=[("Registration and information", "tel. 61 855 12 44")],
    ),
    "niewidzialna-ulica": dict(
        name="Invisible Street (Niewidzialna Ulica)",
        hours=[("Monday", "closed to individual visitors"), ("Tuesday–Saturday", "12:00–18:00"), ("Sunday", "12:00–17:00")],
        tickets=[("Ticket prices", "at niewidzialnaulica.pl")],
    ),
    "muzeum-uzbrojenia": dict(
        name="Armament Museum",
        hours=[("Monday", "closed"), ("Tuesday–Saturday (Mar–Oct)", "10:00–17:00"), ("Sunday (Mar–Oct)", "10:00–16:00"),
               ("Tuesday–Sunday (Nov–Feb)", "10:00–16:00")],
        tickets=[("Standard", "PLN 15"), ("Reduced", "PLN 10"), ("Combined ticket with the “Poznań” Army Museum", "PLN 20, reduced PLN 12"),
                 ("Children under 7", "free"), ("Tuesday", "free admission")],
    ),
    "muzeum-armii-poznan": dict(
        name="“Poznań” Army Museum",
        hours=[("Monday", "closed"), ("Tuesday–Sunday", "10:00–16:00"), ("Last entry", "15:30")],
        tickets=[("Standard", "PLN 10"), ("Reduced", "PLN 6"), ("Combined ticket with the Armament Museum", "PLN 20, reduced PLN 12"),
                 ("Tuesday", "free admission")],
    ),
    "muzeum-sztuk-uzytkowych": dict(
        name="Museum of Decorative Arts",
        hours=[("Monday", "closed"), ("Tuesday–Wednesday", "10:00–16:00"), ("Thursday", "10:00–18:00"),
               ("Friday", "10:00–20:00"), ("Saturday–Sunday", "10:00–17:00")],
        tickets=[("Standard", "PLN 20"), ("Reduced", "PLN 13"), ("Children and young people aged 8–26", "PLN 1"),
                 ("Tuesday", "free admission")],
    ),
}
