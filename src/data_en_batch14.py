# -*- coding: utf-8 -*-
"""Angielskie tłumaczenia, partia 14 (19.10.2026): Lodowisko Malta. Zasady: data_en.py.
Etykiety see_also bez dopisku „(in Polish)”: build_en dodaje go sam, gdy cel nie ma angielskiej strony."""

EN_BATCH14 = {
    "lodowisko-malta": dict(
        name="Malta Ice Rink",
        img_alt="Skaters on the ice inside the tent of the Malta Ice Rink (photo from 2016)",
        short="A seasonal ice rink in a tent by the Malta Regatta Course. The 2026/27 season opened on 10 October.",
        badge="Seasonal, paid",
        status=None,
        lead="The Malta Ice Rink is a seasonal rink run by Poznańskie Ośrodki Sportu i Rekreacji (POSiR, the city's sport and recreation centres) in a tent at the start of the Malta Regatta Course. The new skating season began here on Saturday 10 October 2026.",
        sections=[
            ("What is here", [
                "An ice rink under a tent roof, open every day, including in the evening. You can hire skates, helmets and skating aids for beginners (supports shaped like a penguin, a teddy bear or a seal). There is also a skate-sharpening point.",
                "During the season there are Ice Party events with a DJ. POSiR announces the date of the first one on social media and on its website.",
                "The rink's website also has a subpage with information about learning to skate.",
            ]),
            ("Good to know", [
                "A ticket covers 60 minutes of skating. If you stay longer, you pay a surcharge for each started minute (the ticket price divided by 60). If you leave earlier, the money is not refunded.",
                "The ice is cleaned three times a day, for 30 minutes each: at 12:30, 15:30 and 18:30. You cannot skate during that time, so on weekdays the “after 15:30” ticket applies from 16:00.",
                "Families with the Poznań Large Family Card pay 75% of the ticket price. Holders of the OK Poznań card can enter for PLN 1 within an annual quota of entries to POSiR facilities. MultiSport, FitProfit and similar cards give entry but do not cover the skate hire. Discounts cannot be combined.",
                "POSiR's other seasonal rink is in the Wilda Sports Hall (ul. o. Mariana Żelazka 1a), open daily 7:00–21:45, with the same ticket prices according to the POSiR announcement.",
                "The photograph on this page dates from 2016 and the rink stands in a tent, so it may look slightly different today.",
            ]),
        ],
        hours=[("Sunday–Thursday", "8:00–22:00"), ("Friday–Saturday", "8:00–23:00"),
               ("Ice-cleaning breaks", "12:30–13:00, 15:30–16:00, 18:30–19:00")],
        tickets=[("Standard, Mon–Fri until 15:30 (60 min)", "PLN 16"), ("Reduced, Mon–Fri until 15:30 (60 min)", "PLN 11"),
                 ("Standard, after 15:30 and on Sat, Sun and public holidays (60 min)", "PLN 24"), ("Reduced, after 15:30 and on Sat, Sun and public holidays (60 min)", "PLN 19"),
                 ("Family ticket (3 people)", "PLN 46 on weekdays, PLN 54 at weekends"),
                 ("Senior, Mondays", "PLN 5 per hour"),
                 ("Skate hire", "PLN 18"), ("Helmet hire", "PLN 9"), ("Skating aid for beginners", "PLN 20"),
                 ("Skate sharpening", "PLN 24"), ("Locker", "PLN 6")],
        see_also=["Lake Malta", "Malta Ski: slope, summer toboggan run, roller coaster", "Malta Thermal Baths"],
    ),
}
