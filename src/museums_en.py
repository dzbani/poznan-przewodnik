# -*- coding: utf-8 -*-
"""Angielska strona „Museums” (/en/museums). Tabela jest liczona z polskich danych atrakcji (museums_table.derive),
a nazwy, godziny i ceny bierzemy z angielskich tłumaczeń: dla muzeów przetłumaczonych w pełni z data_en.EN,
dla pozostałych stąd (MUSEUMS_EN: tylko nazwa, godziny i ceny, w tej samej kolejności wierszy co po polsku).
Po zmianie polskich danych muzeów: zaktualizuj ten plik i uruchom: python src/check_en.py --stamp-museums"""

DAY_EN = {"pn": "Monday", "wt": "Tuesday", "sr": "Wednesday", "cz": "Thursday", "pt": "Friday", "sb": "Saturday", "nd": "Sunday"}

MUSEUMS_EN = {
    "muzeum-komunikacji-mpk": dict(
        name="MPK Urban Transport Museum",
        hours=[("Currently", "closed until further notice")],
        tickets=[("Currently", "no visits")],
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
    "muzeum-kultury-cyfrowej": dict(
        name="Poznań Museum of Digital Culture",
        hours=[("Currently", "closed")],
        tickets=[("Currently", "no visits")],
    ),
    "mieszkanie-illakowiczowny": dict(
        name="Kazimiera Iłłakowiczówna Apartment-Studio",
        hours=[("Individual visitors", "2nd and last Wednesday of the month, 12:30"), ("Groups", "by reservation")],
        tickets=[("Registration and information", "tel. 61 855 12 44")],
    ),
}
