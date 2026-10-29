# -*- coding: utf-8 -*-
"""Angielskie tłumaczenia, partia 4 (15.10.2026): atrakcje z planów zwiedzania. Zasady: data_en.py."""

EN_BATCH4 = {
    "bazar": dict(
        name="Hotel Bazar",
        img_alt="The Hotel Bazar building in Poznań",
        short="A building from 1838, founded by Karol Marcinkowski among others as a centre of Polish life.",
        badge="Free",
        status=None,
        lead="The Bazar grew out of a joint-stock company founded on 24 June 1838. Its committee included the physician and social activist Karol Marcinkowski. The building stands at the junction of Aleje Marcinkowskiego and ul. Paderewskiego, on the edge of the Old Town.",
        sections=[
            ("History", [
                "Shareholders gave up profits in favour of social goals, and the shops in the Bazar were rented only to Poles.",
                "A luxury hotel with a famous restaurant operated here, as did many Polish organisations, newspaper offices (including the “Dziennik Poznański”) and cultural institutions.",
                "The hotel burned down in 1945 and was rebuilt by 1950. From 1950 to 1990 it was managed by Orbis, and in 1990 the building was recovered by the pre-war company Bazar Poznański.",
            ]),
        ],
        hours=[("Façade", "visible around the clock")],
        tickets=[("Viewing the building", "free")],
    ),
    "biblioteka-raczynskich": dict(
        name="Raczyński Library",
        img_alt="The Raczyński Library building on Freedom Square",
        short="A neoclassical building from 1829 with a façade modelled on the Louvre, on Freedom Square.",
        badge="Free",
        status=None,
        lead="The library was founded by Count Edward Raczyński. It opened on 5 May 1829 as the first public library in the Polish lands under Prussian rule.",
        sections=[
            ("The building", [
                "The neoclassical building on Plac Wolności (Freedom Square) was built in 1822–1828. Its façade echoes the Louvre in Paris and has twelve pairs of cast-iron Corinthian columns.",
                "On 1 July 2013 a new wing of the library, designed by the JEMS Architekci studio, was opened.",
            ]),
            ("Good to know", [
                "The library has about 1.8 million items and 35 branches in Poznań. It also runs literary museums, including the Henryk Sienkiewicz Literary Museum on the Old Market Square.",
            ]),
        ],
        hours=[("Building from the square side", "visible around the clock")],
        tickets=[("Viewing the building", "free")],
    ),
    "jezyce": dict(
        name="Jeżyce",
        img_alt="Townhouses on Rynek Jeżycki",
        short="Art Nouveau townhouses, a market on Rynek Jeżycki and the Jeżycjada trail of Małgorzata Musierowicz.",
        badge="Free",
        status=None,
        lead="Jeżyce is one of the best-loved districts of Poznań. A former village, already mentioned in 1253, it was incorporated into the city in 1900 and quickly filled with townhouses, many with Art Nouveau decoration.",
        sections=[
            ("About the district", [
                "The first written mention of Jeżyce appears in the charter of Poznań of 1253. For centuries it was an agricultural village. In the 18th century the Bambers, settlers from around Bamberg, settled here.",
                "In 1848 Poznań's first railway station was opened in Jeżyce. After the district was incorporated into the city in 1900, village buildings were replaced by multi-storey rental townhouses. The old village layout survives in the oval shape of ul. Kościelna.",
            ]),
            ("What to see", [
                "Rynek Jeżycki, the heart of the district. One of the oldest markets in Poznań operates on it: vegetables, fruit, flowers, bread, cheese, honey and second-hand books.",
                "Art Nouveau townhouses on ul. Dąbrowskiego, ul. Mickiewicza, ul. Słowackiego and ul. Prusa, as well as villas on ul. Roosevelta and ul. Zacisze.",
                "The Teatr Nowy on ul. Dąbrowskiego and the church of the Sacred Heart of Jesus and St Florian from 1906.",
            ]),
            ("The Jeżycjada trail", [
                "Jeżyce is the setting of the “Jeżycjada”, a series of novels by Małgorzata Musierowicz. The Poznań Local Tourist Organisation created the Poznań Jeżycjada Trail together with the author: about 7 km (a shortened 3 km variant) through Jeżyce and the Imperial Quarter, with quotations and recordings read by the writer.",
            ]),
            ("Good to know", [
                "Jeżyce is also home to the Old Zoo and the Botanical Garden of Adam Mickiewicz University. Both are described on separate pages.",
            ]),
        ],
        hours=[("District", "open around the clock"), ("Market on Rynek Jeżycki", "Mon–Sat 6:00–20:00, Sunday closed")],
        tickets=[("Walk", "free")],
    ),
    "makiety-dawnego-poznania": dict(
        name="Models of Old Poznań",
        img_alt="A panorama of the model of old Poznań with the market square, the Town Hall, churches and city walls",
        short="Poznań in 1618 at a scale of 1:150, with a light and sound show in the church crypt.",
        badge="Shows daily",
        status=None,
        lead="In the crypt of the Franciscan church on ul. Ludgardy stand detailed models of historic Poznań, presented with commentary, light and sound.",
        sections=[
            ("What to see", [
                "A model of old Poznań at a scale of 1:150, reconstructed from an engraving of 1618. It has more than 2,300 objects and was the first such detailed historical model in Poland.",
                "A model of the Stronghold of the First Piasts and a model of the Old Market Square.",
                "One of the models, at a scale of 1:100, has tactile elements and Braille descriptions for blind visitors.",
            ]),
            ("Good to know", [
                "A show lasts 27 minutes. Shows start at 11:00, 11:45, 12:30, 13:15, 14:00, 14:45, 15:30, 16:15 and 17:00. From 1 October to 30 April the last show starts at 15:30. Shows at other times are possible by prior arrangement.",
                "You can buy tickets up to 15 minutes before a show, or in advance. Payment is by cash or BLIK. Tickets are for a specific day and time and are non-refundable.",
                "With the Poznań Tourist Card a ticket is 25% cheaper.",
                "The commentary is in Polish, German, English, Spanish, French, Italian and Russian. For one show you can order two language versions (Polish and one of six foreign languages, except the English–German and French–English pairs): the first language is played in the room, the second through headphones (up to 8 people).",
                "Groups of more than 20 people (Polish version) must book a show by phone or e-mail (makieta@makieta.poznan.pl). In groups of children and young people up to 19 years old, one carer per 15 people enters free of charge.",
            ]),
        ],
        hours=[("Shows, 1 Oct–30 Apr", "11:00–15:30, starting every 45 minutes"),
               ("Shows, other months", "11:00–17:00, starting every 45 minutes"),
               ("Closed", "1 Jan, Good Friday, Holy Saturday, Easter, Corpus Christi, 31 Oct, 1 Nov, 23–25 Dec, 31 Dec")],
        tickets=[("Standard", "PLN 35"), ("Foreign-language versions", "PLN 35"),
                 ("Children under 10 (Polish version)", "PLN 25"),
                 ("With the Poznań City Card or Piast Card", "PLN 25"),
                 ("With the Poznań Tourist Card", "25% cheaper"),
                 ("Groups of more than 20 (Polish version)", "PLN 25 per person, booking required")],
    ),
    "malta-ski": dict(
        name="Malta Ski",
        img_alt="The Malta Ski slope in winter",
        short="An artificial ski slope, a summer toboggan run and a roller coaster above the lake.",
        badge="Weather permitting",
        status=None,
        lead="Malta Ski is a year-round centre on Lake Malta. In winter an artificial ski slope operates, and in summer a toboggan run and other attractions.",
        sections=[
            ("What is here", [
                "An artificial ski slope about 150 metres long.",
                "A summer toboggan run 560 metres long.",
                "The year-round Adrenaline roller coaster, mini golf and a playground.",
            ]),
            ("Good to know", [
                "Opening hours depend on the weather and change during the year. Current hours and prices are given on maltaski.pl.",
                "The roller coaster and the toboggan run are partners of the Poznań Tourist Card.",
            ]),
        ],
        hours=[("Hours", "depend on the weather, see maltaski.pl"), ("Seasons according to maltaski.pl", "winter 17 Oct–31 Mar, summer 1 Apr–31 Oct")],
        tickets=[("Price list", "on maltaski.pl")],
        see_also=["Malta Ice Rink: the seasonal rink", "Lake Malta", "Malta Thermal Baths"],
    ),
    "mury-miejskie": dict(
        name="Medieval City Walls",
        img_alt="A fragment of the city walls on ul. Wroniecka",
        short="Remains of walls from the 13th–15th centuries, Catherine's Tower and a tourist path by the Wronki Gate.",
        badge="Free",
        status=None,
        lead="Defensive walls surrounded Poznań from the 13th to the 15th century. They were about 1,725 metres long and 7 metres high, and the inner towers reached 11 metres.",
        sections=[
            ("History", [
                "Timber-and-earth fortifications were begun soon after the city was chartered in 1253, and were later replaced by a wall with 32 projecting turrets (bartizans).",
                "After 1431 a second, outer wall was added with semicircular towers adapted for firearms. In the 17th century, with the development of artillery, the walls lost their defensive significance.",
            ]),
            ("What to see", [
                "Catherine's Tower (Baszta Katarzynek), the only tower of the former walls to survive to this day.",
                "The remains of an artillery bastion on ul. 23 Lutego.",
                "Fragments of the outer wall with the Castle Postern (Furta Zamkowa) by the Royal Castle, and western sections on ul. Ludgardy.",
                "A tourist path between the bastion and the remains of the Wronki Gate.",
            ]),
            ("Good to know", [
                "Since August 2013 the course of the former walls has been marked by 17 plaques set into the pavements of the Old Town.",
            ]),
        ],
        hours=[("Remains of the walls", "open around the clock")],
        tickets=[("Admission", "free")],
    ),
    "park-mickiewicza": dict(
        name="Mickiewicz Park",
        img_alt="Mickiewicz Park with the fountain in front of the Grand Theatre",
        short="A showpiece park in front of the Grand Theatre, with a fountain and plane trees, next to the Poznań Crosses.",
        badge="Free",
        status=None,
        lead="Mickiewicz Park was created in 1907–1910 on the site of former fortifications, as part of the Imperial Quarter designed by Joseph Stübben. Its layout is closely linked with the Grand Theatre building.",
        sections=[
            ("What to see", [
                "A long pool with a high-jetting fountain and the ceremonial steps in front of the Stanisław Moniuszko Grand Theatre.",
                "Avenues of plane trees, protected as a natural monument since 2023.",
                "The southern part of the park, which leads into Adam Mickiewicz Square with the monument to Adam Mickiewicz and the Poznań June 1956 Monument.",
            ]),
            ("Good to know", [
                "The park lies opposite the Imperial Castle, so it is easy to combine with a tour of the Imperial Quarter.",
                "Trams 2, 3, 4, 5, 8, 9, 13, 15, 16, 17 and 19 run to the stop Zamek (according to the ZTM timetable of 10 October 2026).",
            ]),
        ],
        hours=[("Park", "open to everyone")],
        tickets=[("Admission", "free")],
    ),
    "pomnik-czerwca-1956": dict(
        name="Poznań June 1956 Monument",
        img_alt="The two joined crosses of the Poznań June 1956 Monument",
        short="The Poznań Crosses, commemorating the first mass protest against communist rule.",
        badge="Free",
        status=None,
        lead="The monument on Adam Mickiewicz Square, known as the Poznań Crosses, commemorates the workers' revolt of 28 June 1956, the first mass protest against communist rule in Poland.",
        sections=[
            ("About the monument", [
                "The monument was unveiled on 28 June 1981, on the 25th anniversary of the events. It was designed by the sculptor Adam Graczyk and the architect Włodzimierz Wojciechowski.",
                "It consists of two joined steel crosses 19.5 and 21 metres high. At their base stands a sculpture of an eagle.",
                "The left cross bears the date 1956. On the right are the dates of later protests in communist Poland: 1968, 1970, 1976, 1980 and 1981. The inscription refers to the workers' slogans: “For freedom, law and bread”.",
            ]),
            ("Good to know", [
                "The monument stands in the Imperial Quarter, opposite the Imperial Castle. The castle houses the Museum of the Poznań Uprising – June 1956.",
            ]),
        ],
        hours=[("Monument", "open around the clock")],
        tickets=[("Admission", "free")],
    ),
    "trakt-krolewsko-cesarski": dict(
        name="Royal-Imperial Route",
        img_alt="Royal-Imperial Route marker with a crown by the Gate of Poznań",
        short="Poznań's main tourist trail: from the Gate of Poznań via Ostrów Tumski and the Old Market Square to the Castle.",
        badge="Free",
        status=None,
        lead="The Royal-Imperial Route (Trakt Królewsko-Cesarski) is Poznań's main tourist and cultural trail. It links the most interesting parts of the city and tells the story of Poznań and of forty generations of its inhabitants.",
        sections=[
            ("The route", [
                "The main axis is about 3 km long and leads west from the Gate of Poznań through Ostrów Tumski with its cathedral, the Old Market Square with the town hall and the Old Town, to the city centre with its museums and theatres, and the Imperial Castle.",
                "The trail was originally laid out from the church of St John of Jerusalem Outside the Walls to the church of the Sacred Heart of Jesus and St Florian in Jeżyce. Additional trails run around the main axis.",
                "Along the way are the cathedral, the Royal Castle, the town hall, the former Jesuit College, the Raczyński Library and the Imperial Castle, among others.",
            ]),
            ("How to visit", [
                "The route is marked by maroon plates with a cut-out crown, the logo of the route, mounted on elements of city infrastructure.",
                "You can walk the trail, or travel it by bicycle and public transport. Visiting is free, and the route's website has free leaflets and a map.",
                "Free guided walks are held every year.",
            ]),
            ("About the trail", [
                "The route was created in 2006–2013 according to a concept of 2004, and its course was modified in 2015. It is managed by the Poznań Heritage Centre, a municipal cultural institution.",
            ]),
        ],
        hours=[("Trail", "open around the clock")],
        tickets=[("Visiting", "free")],
    ),
}
