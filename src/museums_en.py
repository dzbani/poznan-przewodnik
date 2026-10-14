# -*- coding: utf-8 -*-
"""Angielska strona „Museums” (/en/museums). Tabela jest liczona z polskich danych atrakcji (museums_table.derive),
a nazwy, godziny i ceny bierzemy z angielskich tłumaczeń: dla muzeów przetłumaczonych w pełni z data_en.EN,
dla pozostałych stąd (MUSEUMS_EN: tylko nazwa, godziny i ceny, w tej samej kolejności wierszy co po polsku).
Po zmianie polskich danych muzeów: zaktualizuj ten plik i uruchom: python src/check_en.py --stamp-museums"""

DAY_EN = {"pn": "Monday", "wt": "Tuesday", "sr": "Wednesday", "cz": "Thursday", "pt": "Friday", "sb": "Saturday", "nd": "Sunday"}

MUSEUMS_EN = {
}
