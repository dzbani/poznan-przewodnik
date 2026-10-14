# -*- coding: utf-8 -*-
"""Angielska strona „Museums” (/en/museums). Tabela jest liczona z polskich danych atrakcji (museums_table.derive),
a nazwy, godziny i ceny bierzemy z angielskich tłumaczeń: dla muzeów przetłumaczonych w pełni z data_en.EN,
dla pozostałych stąd (MUSEUMS_EN: tylko nazwa, godziny i ceny, w tej samej kolejności wierszy co po polsku).
Po zmianie polskich danych muzeów: zaktualizuj ten plik i uruchom: python src/check_en.py --stamp-museums"""

DAY_EN = {"pn": "Monday", "wt": "Tuesday", "sr": "Wednesday", "cz": "Thursday", "pt": "Friday", "sb": "Saturday", "nd": "Sunday"}

MUSEUMS_EN = {
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
    "muzeum-komunikacji-mpk": dict(
        name="MPK Urban Transport Museum",
        hours=[("Currently", "closed until further notice")],
        tickets=[("Currently", "no visits")],
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
}
