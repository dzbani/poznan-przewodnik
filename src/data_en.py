# -*- coding: utf-8 -*-
"""Angielska wersja przewodnika (strony pod /en/). Polskie dane w site_data.py pozostają jedynym
źródłem faktów; tu są tylko przetłumaczone teksty, kluczowane po slug atrakcji.

Zasady tłumaczenia:
- nazwy własne zostają po polsku, z krótkim wyjaśnieniem przy pierwszym użyciu;
- ceny „PLN 35”, ulgowy = „reduced”, rodzinny = „family”;
- godziny w formacie 24-godzinnym (9:00–16:00), daty „1 Mar–15 Nov”;
- brytyjska pisownia, krótkie zdania.

Po zmianie polskiej atrakcji uruchom: python src/check_en.py  (pokaże, które tłumaczenia są nieaktualne).
Po zaktualizowaniu tłumaczenia: python src/check_en.py --stamp <slug>
"""

# Kategorie: slug -> (nazwa, opis)
CATEGORIES_EN = {
    "zabytki": ("Sights and history", "A thousand years of history: from Mieszko I's stronghold to the emperor's castle."),
    "pomniki": ("Monuments and fountains", "From the Baroque fountain outside the town hall to Old Marych with his bicycle."),
    "koscioly": ("Churches", "From the Romanesque Hospitaller church to interwar rotundas."),
    "muzea": ("Museums", "Art, archaeology, the history of Greater Poland and croissants."),
    "przyroda": ("Parks and nature", "A lake, gardens and greenery within the city limits."),
    "rodzina": ("Family and active", "A zoo, a park railway, swimming pools and a ski slope all year round."),
    "wspolczesny": ("Contemporary Poznań", "Street art and an old brewery turned into an arts centre."),
    "wycieczki": ("Day trips", "Castles, palaces and the cradle of Poland within a day's reach."),
}

EN = {
    "stary-rynek": dict(
        name="Old Market Square and Town Hall",
        img_alt="Colourful townhouses and the town hall on the Old Market Square in Poznań",
        short="The heart of the city since the 13th century. A Renaissance town hall and two goats butting heads at noon.",
        badge="Free",
        status="The museum inside the Town Hall (Poznań City Museum) is closed from 1 July 2026 to 30 November 2027 for renovation. Part of the building is under scaffolding. The goats still appear, but the mechanism has occasionally stopped during the works.",
        lead="Stary Rynek (Old Market Square) was laid out around 1253, when the city was chartered. It is a square measuring 141 metres on each side, and the Renaissance-style town hall stands at its centre.",
        sections=[
            ("About the place", [
                "The square was the centre of the chartered town, founded between the castle and the Warta river. Townhouses surround the open space, and a block of buildings fills its middle.",
                "The town hall has medieval origins. Between 1550 and 1560 it was rebuilt by Giovanni Battista di Quadro, an architect from Lugano in Ticino. He added a storey, extended the building to the west, and gave it an attic parapet and a three-storey loggia, which created its Renaissance look.",
            ]),
            ("What to see", [
                "The Poznań Goats on the town hall tower: every day at 12:00 they emerge above the clock and butt heads. The clock was ordered from Bartłomiej Wolff of Gubin during the rebuilding and installed in 1551. A crowd gathers below at noon, so arrive a few minutes early.",
                "The central block of buildings: besides the town hall, it holds the Weigh House, the neoclassical Guardhouse (now the Museum of the Greater Poland Uprising) and the little merchants' houses (domki budnicze), former trading stalls.",
                "Four fountains: Proserpina, Apollo, Neptune and Mars. The Proserpina fountain dates from 1766 and is the only one that survived. The other three were rebuilt between 2002 and 2005.",
            ]),
            ("Good to know", [
                "The Tourist Information Point is at Stary Rynek 59/60. You can pick up maps and buy the Poznań Tourist Card there.",
                "Within a few hundred metres you will find the Croissant Museum, the Parish Church (Fara), the Archaeological Museum and the Museum of the Greater Poland Uprising.",
            ]),
        ],
        hours=[("Square", "open 24 hours"), ("Poznań Goats", "daily at 12:00"), ("Museum in the Town Hall", "closed until 30 Nov 2027")],
        tickets=[("Square and goats", "free")],
    ),
    "ostrow-tumski": dict(
        name="Ostrów Tumski and the Archcathedral",
        img_alt="The Archcathedral on Ostrów Tumski",
        short="The oldest cathedral in Poland. The tombs of the first rulers and the Golden Chapel.",
        badge="Cathedral free",
        status=None,
        lead="Ostrów Tumski (Cathedral Island) lies between the Warta and the Cybina rivers. In the 10th century it was the site of a stronghold of the first Piast rulers. A bishopric has existed here since 968, and the Archcathedral of St Peter and St Paul is the oldest cathedral in Poland.",
        sections=[
            ("About the place", [
                "The first cathedral was built in the 980s. The present building is Gothic, from the 14th and 15th centuries. After the destruction of the Second World War it was partly rebuilt and its Gothic character was restored.",
                "Poland's first rulers are buried in the cathedral, among them Bolesław the Brave, Mieszko II and Casimir the Restorer.",
            ]),
            ("What to see", [
                "The Golden Chapel (Chapel of the Polish Kings), built in 1836–1837: an octagonal mausoleum in the Byzantine style, dedicated to Mieszko I and Bolesław the Brave. It stands exactly on the axis of the church.",
                "The cathedral crypts: remains of earlier buildings, the tombs of the Piast dynasty and a 10th-century baptismal font.",
                "The viewing tower, open seasonally (in 2026 from 1 June).",
            ]),
            ("Good to know", [
                "The cathedral is a working church. It cannot be visited during Mass, services or concerts, and you are asked to dress modestly and keep quiet.",
                "Across the Cybina, connected by a footbridge, stands the Gate of Poznań (Brama Poznania). It offers a combined ticket for visiting Ostrów Tumski.",
            ]),
        ],
        hours=[
            ("Sightseeing (1 Mar–15 Nov)", "weekdays 9:00–16:00"),
            ("Sightseeing (16 Nov–end of Feb)", "weekdays 9:00–16:00"),
            ("Crypts", "1 Mar–15 Nov: weekdays 9:00–16:00, Sundays 14:00–18:00"),
            ("Viewing tower", "from 1 Jun 2026; during the season (1 Mar–15 Nov) same as the crypts: weekdays 9:00–16:00, Sundays 14:00–18:00"),
            ("Crypts and tower after 15 Nov", "the archdiocese publishes hours only for 1 Mar–15 Nov; there are no sightseeing hours in winter"),
        ],
        tickets=[("Cathedral entry", "free"), ("Crypts", "PLN 10, reduced PLN 8, family PLN 25"),
                 ("Viewing tower", "PLN 14, reduced PLN 12, family PLN 40")],
        see_also=["Viewpoints in Poznań: all towers and terraces (in Polish)"],
    ),
    "centrum-szyfrow-enigma": dict(
        name="Enigma Cipher Centre",
        img_alt="Inside the Enigma Cipher Centre exhibition: a chandelier of glowing letters and visitors at the interactive stations",
        short="How three mathematicians from Poznań broke the Enigma code. A multimedia exhibition with an audio guide.",
        badge="Closed Mon",
        status=None,
        lead="The Enigma Cipher Centre, opened in 2021, tells how three Polish mathematicians, Marian Rejewski, Henryk Zygalski and Jerzy Różycki, broke the ciphers of the German Enigma machine. It is run by the Poznań Heritage Centre.",
        sections=[
            ("What to see", [
                "A modern, multimedia exhibition about the breaking of Enigma, about the fate of the three mathematicians in exile, and about how their work changed the course of the war and influenced the development of digital technology.",
                "The exhibition also traces the history of ciphers from antiquity to the present day, and describes the secret cryptology course held in Poznań that the Polish mathematicians attended.",
            ]),
            ("How to visit", [
                "Tickets are for a specific time slot. Groups of up to 15 people enter every 15 minutes. The last entry is one hour before closing.",
                "Allow about 2 hours for your visit.",
                "An audio guide is included in the ticket price, in five languages. Versions are also available with Polish Sign Language interpretation, with audio description, and in Easy Read text.",
            ]),
        ],
        hours=[("Monday", "closed"), ("Tuesday–Friday", "9:00–18:00"), ("Saturday–Sunday", "10:00–19:00")],
        tickets=[("Standard", "PLN 35"), ("Reduced", "PLN 29"), ("Family", "PLN 75"), ("Children under 6", "free")],
    ),
    "rogalowe-muzeum": dict(
        name="St Martin's Croissant Museum",
        img_alt="St Martin's croissants and ingredients (almonds, raisins, candied peel) around a heart drawn in flour with the words ROGA-LOVE",
        short="A live show about the St Martin's croissant, just off the Old Market Square. Buy tickets in advance.",
        badge="Book ahead",
        status=None,
        lead="The Croissant Museum (Rogalowe Muzeum Poznania) is an interactive show near the Old Market Square. Visitors learn the history of the rogal świętomarciński (St Martin's croissant) and see how it is made following the traditional recipe.",
        sections=[
            ("About the croissant", [
                "Since 2008 the name “rogal świętomarciński” has been a Protected Geographical Indication of the European Union (Commission Regulation (EC) No 1070/2008 of 30 October 2008). Only a bakery in the Greater Poland region that holds a certificate from the Chapter of the Poznań Traditional St Martin's Croissant may use the name.",
                "Poznań residents eat these croissants above all on 11 November, the St Martin Street Name Day.",
            ]),
            ("The shows", [
                "The croissant show lasts 55–60 minutes; the croissant-and-goats show lasts 65 minutes. In the croissant-and-goats show, besides everything in the standard show, you watch the Poznań goats (koziołki) from the museum windows (at 12:00 for the show starting at 11:00 and at 15:00 for the show starting at 14:00) and learn the history of their mechanism.",
                "Shows in English take place on Saturdays and Sundays at 14:00, and every day at 14:00 in July and August.",
                "Shows often sell out, so it is best to buy a ticket in advance. Online booking is possible up to 30 minutes before the show.",
            ]),
        ],
        address="Stary Rynek 41/2 (entrance from ul. Klasztorna 23), 61-772 Poznań",
        hours=[("Shows every day", "11:00 (with the goats), 12:30, 14:00 (with the goats), 15:30"),
               ("Extra show on Saturdays", "17:00"), ("In English", "Sat–Sun 14:00; daily in July and August")],
        tickets=[("Croissant show", "PLN 41, reduced PLN 37"), ("Croissant-and-goats show", "PLN 47, reduced PLN 43"), ("Show in English", "PLN 47, reduced ticket at the same price"),
                 ("Family ticket (2 adults and 2 children aged 3–18)", "PLN 37 per person for the croissant show, PLN 43 for the croissant-and-goats show"), ("Children under 3", "PLN 1")],
    ),
    "jezioro-maltanskie": dict(
        name="Lake Malta",
        img_alt="A sculpture by Lake Malta",
        short="An artificial lake with a regatta course. Walks, cycling and things to do all year round.",
        badge="Free",
        status=None,
        lead="Lake Malta (Jezioro Maltańskie) is an artificial reservoir opened in 1952. It is 2.2 km long and covers about 64 hectares. A popular walking and cycling route runs all the way around it.",
        sections=[
            ("What to see", [
                "The regatta course, built in 1987–1990 for the canoe sprint World Championships, which were held in Poznań in 1990.",
                "On the lake shore you will also find the Malta Thermal Baths, the year-round Malta Ski slope, the Maltanka narrow-gauge park railway and the New Zoo.",
            ]),
            ("Good to know", [
                "In June the Malta Festival takes place on the lake and across the city. In 2026 it featured 108 events at 27 venues.",
            ]),
        ],
        hours=[("Area around the lake", "open 24 hours")],
        tickets=[("Admission", "free")],
        see_also=["Malta Ice Rink: the seasonal rink", "Malta Ski: slope, summer toboggan run, roller coaster",
                  "Malta Thermal Baths", "Maltanka Park Railway"],
    ),
}


from data_en_batch2 import EN_BATCH2  # noqa: E402  (partia 2, 14.10.2026)
EN.update(EN_BATCH2)

from data_en_batch3 import EN_BATCH3  # noqa: E402  (partia 3, 15.10.2026)
EN.update(EN_BATCH3)

from data_en_batch4 import EN_BATCH4  # noqa: E402  (partia 4, 15.10.2026)
EN.update(EN_BATCH4)

from data_en_batch5 import EN_BATCH5  # noqa: E402  (partia 5, 14.10.2026)
EN.update(EN_BATCH5)


from data_en_batch6 import EN_BATCH6  # noqa: E402  (partia 6, 14.10.2026)
EN.update(EN_BATCH6)


from data_en_batch7 import EN_BATCH7  # noqa: E402  (partia 7, 14.10.2026)
EN.update(EN_BATCH7)


from data_en_batch8 import EN_BATCH8  # noqa: E402  (partia 8, 14.10.2026)
EN.update(EN_BATCH8)


from data_en_batch9 import EN_BATCH9  # noqa: E402  (partia 9, 14.10.2026)
EN.update(EN_BATCH9)


from data_en_batch10 import EN_BATCH10  # noqa: E402  (partia 10, 14.10.2026)
EN.update(EN_BATCH10)


from data_en_batch11 import EN_BATCH11  # noqa: E402  (partia 11, 14.10.2026)
EN.update(EN_BATCH11)


from data_en_batch12 import EN_BATCH12  # noqa: E402  (partia 12, 14.10.2026)
EN.update(EN_BATCH12)


from data_en_batch13 import EN_BATCH13  # noqa: E402  (partia 13, 14.10.2026; ostatnia)
EN.update(EN_BATCH13)


from data_en_batch14 import EN_BATCH14  # noqa: E402  (partia 14, 19.10.2026: Lodowisko Malta)
EN.update(EN_BATCH14)
