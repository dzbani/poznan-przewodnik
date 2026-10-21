# -*- coding: utf-8 -*-
"""Angielskie tłumaczenia, partia 10 (14.10.2026): kościoły i małe muzea. Zasady: data_en.py."""

CHURCH_NOTE = "This is a working church. It cannot be visited during Mass and services, and you are asked to dress modestly and keep quiet."
CH_HOURS = [("Visiting", "outside services"), ("Mass times", "in the parish notices")]

EN_BATCH10 = {
    "kosciol-wspomozenia-wiernych": dict(
        name="Church of Our Lady Help of Christians (Salesian Church)",
        img_alt="The church of Our Lady Help of Christians on ul. Wroniecka",
        short="A Gothic church of former Dominican nuns, commemorating the martyrs of the Poznań Five.",
        badge="Free entry",
        status=None,
        lead="The church and the Dominican nuns' convent were built in the 1280s. After the Prussians dissolved the convent in 1822 the church fell into ruin. In 1926 the Salesians rebuilt it and restored its function.",
        sections=[
            ("History", [
                "The chancel was built first, the nave in the 14th century and the side aisle in the 16th century.",
                "During the rebuilding a Neo-Baroque façade was added to a design by Lucjan Michałowski.",
            ]),
            ("What to see", [
                "A rib vault of about 1440 in the chancel, the only one of its kind in Poznań.",
                "The high altar of 1928 with a painting of Our Lady Help of Christians.",
                "An altar with portraits of the Poznań Five: Czesław Jóźwiak, Edward Kaźmierski, Franciszek Kęsy, Edward Klinik and Jarogniew Wojciechowski. They were boys from the Salesian oratory who worked in the resistance and were murdered by the Germans. In 1999 John Paul II beatified them.",
                "A tower in the 13th-century defensive wall of the city, preserved from the former monastery buildings.",
            ]),
            ("Good to know", [
                "The church stands on ul. Wroniecka, where fragments of the medieval city walls also survive.",
                CHURCH_NOTE,
            ]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "kosciol-mb-bolesnej": dict(
        name="Church of Our Lady of Sorrows",
        img_alt="The Neo-Romanesque Church of Our Lady of Sorrows",
        short="A Neo-Romanesque red-brick church with a marble copy of Michelangelo's Pietà.",
        badge="Free entry",
        status=None,
        lead="The church was built in 1899–1901 in the Neo-Romanesque style of red brick. It stands out for its tall tower with a slender metal spire.",
        sections=[
            ("History", [
                "The church has three aisles with a transept and cross vaults.",
            ]),
            ("What to see", [
                "A marble copy of Michelangelo's Pietà in the Vatican, from about 1900, in the high altar.",
                "A stone font with a sculpture of the baptism of Christ and a pulpit with figures of the evangelists.",
                "A symbolic grave with a monument to Fr Jerzy Popiełuszko by the gate.",
            ]),
            ("Good to know", [CHURCH_NOTE]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "kosciol-maryi-krolowej": dict(
        name="Church of Mary Queen",
        img_alt="The Church of Mary Queen on Rynek Wildecki",
        short="A Neo-Renaissance church on Rynek Wildecki with a 45-metre tower.",
        badge="Free entry",
        status=None,
        lead="The church was built in 1904–1907 in the Neo-Renaissance style. Until the end of the Second World War it belonged to the Protestant congregation as the church of St Matthew. Since 1945 it has been Catholic.",
        sections=[
            ("History", [
                "After it was taken over by the Catholic parish its dedication was changed to the present one.",
            ]),
            ("What to see", [
                "A tower 45 metres high with an entrance portal, on the axis of the building.",
                "An interior with a barrel vault, stained glass, wall paintings and sculptures.",
                "A monument to the Archangel Michael in front of the church.",
            ]),
            ("Good to know", [CHURCH_NOTE]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "kosciol-jana-vianneya": dict(
        name="St John Vianney's Church",
        img_alt="The rotunda of St John Vianney's Church in Sołacz seen from the steps",
        short="An interwar rotunda with a columned portico on a hill in Sołacz.",
        badge="Free entry",
        status=None,
        lead="The church in Sołacz is a neoclassical rotunda on a circular plan, built in 1928–1930. It is a monument of Polish interwar architecture.",
        sections=[
            ("History", [
                "The church stands on a rise, and monumental, wide steps lead up to it.",
            ]),
            ("What to see", [
                "A central columned portico, two side porticoes and a dome over the chancel.",
                "A bright, spacious interior with a crucifix in the high altar and stained glass referring to St John Vianney, St Adalbert and the Last Supper.",
            ]),
            ("Good to know", [
                "The church lies near Sołacki Park, so the two places are easy to combine.",
                CHURCH_NOTE,
            ]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "muzeum-sienkiewicza": dict(
        name="Henryk Sienkiewicz Literary Museum",
        img_alt="The sgraffito-decorated townhouse at Stary Rynek 84, home of the Henryk Sienkiewicz Literary Museum, with a sculpture in a niche and a fountain in the foreground",
        short="Mementoes of the Nobel laureate in a 16th-century townhouse on the square. Free admission on Saturdays.",
        badge="Sat free",
        status=None,
        lead="The Henryk Sienkiewicz Literary Museum is a branch of the Raczyński Library in a 16th-century townhouse at Stary Rynek 84. It is the youngest museum devoted to the writer in Poland.",
        sections=[
            ("About the museum", [
                "The author of the “Trilogy” rarely visited Greater Poland and never set foot in this townhouse. It was Ignacy Moś, a charismatic collector, who linked him with Poznań: he devoted most of his life to gathering mementoes of the writer and gave the collection to the Raczyński Library.",
                "The museum is housed in a historic townhouse whose former owners included Jan Baptysta Quadro, the builder of the Renaissance Town Hall, and the city's president Cyryl Ratajski.",
            ]),
            ("What to see", [
                "The writer's death mask and a cast of his right hand, works by the sculptor Franciszek Black.",
                "A personal copy of “Quo vadis” on Japanese paper, with heliogravures by Piotr Stachiewicz, from the writer's private library. Sienkiewicz's son gave it to Moś.",
                "A replica of the Nobel Prize medal of 1905.",
                "The sculpture “Ursus Fighting the Aurochs” by Marcin Rożek.",
                "First editions of almost all of Sienkiewicz's novels and their translations into languages from all over the world, including such rare ones as Chinese, Japanese, Georgian, Arabic and Hebrew.",
            ]),
        ],
        hours=[("Tuesday, Friday, Saturday", "9:00–16:00"), ("Wednesday, Thursday", "12:00–19:00"),
               ("Monday, Sunday, public holidays", "closed")],
        tickets=[("Standard", "PLN 10"), ("Reduced", "PLN 5"), ("Saturday", "free admission")],
    ),
    "muzeum-bambrow": dict(
        name="Museum of the Poznań Bambers",
        img_alt="The Bamberka well, a symbol of the Poznań Bambers (illustrative photograph)",
        short="The history of the settlers from around Bamberg who in the 18th century settled villages near Poznań.",
        badge="Fri–Sat",
        status=None,
        lead="The museum is run by the Society of Poznań Bambers. It tells the story of the settlers from the Bamberg area in Franconia who in 1719–1753 came to the villages around Poznań, devastated by the Great Northern War and the plague.",
        sections=[
            ("Who the Bambers were", [
                "The first settlers came to Luboń in 1719. Others settled in Dębiec and Bonin (1730), in Rataje and Wilda (1746–1747) and in Jeżyce and Górczyn (1750–1753).",
                "They were farmers and supplied the city with food. They were given favourable terms: a lease of land, building materials, seed grain and several years' exemption from taxes.",
                "In the 19th century a characteristic women's costume took shape, with a flowered bonnet that could weigh as much as 3 kg. By the end of the 19th century most of the Bambers had become Polonised.",
            ]),
            ("Good to know", [
                "The guided tour of the museum is free of charge. Organised groups should register their visit in advance.",
                "The museum is accessible to people with disabilities.",
            ]),
        ],
        hours=[("Friday and Saturday", "10:00–14:00")],
        tickets=[("Guided tour", "free, by appointment")],
    ),
    "muzeum-wojskowe": dict(
        name="Greater Poland Military Museum",
        img_alt="An exhibition of the Greater Poland Military Museum",
        short="Weapons from the 11th century and a fragment of Wojciech Kossak's panorama “The Battle of the Pyramids”.",
        badge="Closed Mon",
        status=None,
        lead="The Greater Poland Military Museum, a branch of the National Museum, is housed in a post-war pavilion on the Old Market Square. It shows Polish and foreign weapons and mementoes of the national uprisings, especially the Greater Poland Uprising.",
        sections=[
            ("What to see", [
                "A fragment of Wojciech Kossak's panorama “The Battle of the Pyramids” of 1901, one of the few exhibits that survived from the pre-war collections.",
                "A 16th-century rapier with a blade forged in Milan.",
                "A bechter, that is, a suit of armour of 1580, belonging to the city's cavalry captain and decorated with the coat of arms of Poznań.",
                "Edged and firearms, protective armour, uniforms and military badges.",
            ]),
            ("Good to know", [
                "With the Poznań Tourist Card admission is free.",
            ]),
        ],
        hours=[("Monday", "closed"), ("Tuesday–Wednesday", "10:00–16:00"), ("Thursday", "10:00–18:00"),
               ("Friday", "10:00–20:00"), ("Saturday–Sunday", "10:00–17:00")],
        tickets=[("Standard", "PLN 15"), ("Reduced", "PLN 10"), ("Children and young people aged 8–26", "PLN 1"),
                 ("Tuesday", "free admission"), ("With the Poznań Tourist Card", "free")],
    ),
    "muzeum-pyry": dict(
        name="Poznań Potato Museum (Muzeum Pyry)",
        img_alt="A street in central Poznań with the Poznań Potato Museum sign on a wrought-iron bracket",
        short="An hour with humour about potatoes, with digging and baking your own potato. Booking required.",
        badge="Booking",
        status=None,
        lead="“Pyra” is the Poznań word for a potato. The Potato Museum is an interactive, humorous one-hour route for children and adults, led by a guide.",
        sections=[
            ("What happens here", [
                "Participants find out how potatoes reached Europe and Poland, what potatoes have to do with washing, how people fought the Colorado beetle and which potato dishes reign in Poland and the world.",
                "The programme includes a simulated potato harvest and baking your own potato.",
            ]),
            ("Good to know", [
                "The visit lasts about 60 minutes. You must book a place in advance in the booking system on the museum's website, where the available times are also shown.",
                "The entrance is from ul. Mokra.",
                "The price includes the guided tour and workshops.",
            ]),
        ],
        address="ul. Wroniecka 18 (entrance from ul. Mokra), 61-763 Poznań",
        hours=[("Tuesday–Sunday", "hours in the booking system"), ("Monday", "closed")],
        tickets=[("Standard", "PLN 31"), ("Reduced", "PLN 29"), ("Family (3 or more people)", "PLN 28 per person"),
                 ("In English", "PLN 35"), ("Children under 4", "free")],
    ),
    "akademia-lubranskiego": dict(
        name="Archdiocesan Museum – Lubrański Academy",
        img_alt="The Lubrański Academy building on Ostrów Tumski",
        short="Sacred art in a building of 1520: the sword of St Peter and King Jagiełło's monstrance.",
        badge="Closed Mon",
        status=None,
        lead="The Archdiocesan Museum was founded in 1894–1898 by Archbishop Florian Stablewski. It is the oldest museum institution in Poznań and one of the oldest museums of its kind in Poland. It is housed on Ostrów Tumski, in the building of the former Lubrański Academy of 1520.",
        sections=[
            ("What to see", [
                "Sacred art from the Middle Ages to the present, including the richest collection of sculpture and painting of the 14th and 15th centuries in this part of Poland.",
                "The sword of St Peter, the monstrance of King Władysław Jagiełło, the golden chalice of Bishop Tolibowski and a crosier from Limoges.",
                "Galleries of portraits, Polish and European painting, textiles and goldsmiths' work.",
            ]),
            ("Good to know", [
                "The museum is part of the ticket for three places on Ostrów Tumski (the Gate of Poznań, Genius Loci and the Lubrański Academy), which costs PLN 49.",
            ]),
        ],
        hours=[("Tuesday–Friday", "11:00–17:00"), ("Saturday", "11:00–16:00"), ("Sunday", "11:00–15:00")],
        tickets=[("Ticket prices", "at akademialubranskiego.pl"), ("Ticket for 3 places on the island", "PLN 49")],
    ),
    "muzeum-farmacji": dict(
        name="Museum of Pharmacy",
        img_alt="An exhibition of the Museum of Pharmacy in Poznań",
        short="A former pharmacy from Miłosław, apothecary vessels and old prints. Open on Thursdays, free entry.",
        badge="Free entry",
        status=None,
        lead="The Museum of Pharmacy was founded in June 1989 on the initiative of the Section for the History of Pharmacy of the Polish Pharmaceutical Society. Since 1992 it has been looked after by the Greater Poland Regional Chamber of Pharmacists.",
        sections=[
            ("What to see", [
                "A pharmacy dispensary from the turn of the 19th and 20th centuries, moved from the pharmacy in Miłosław.",
                "Apothecary vessels of wood, glass, stoneware and porcelain, cast-iron mortars and laboratory equipment.",
                "A library of about 1,200 volumes, including several early printed books.",
            ]),
            ("Good to know", [
                "The museum first operated in a townhouse on the Old Market Square. It was moved to its present seat in 1996 and officially opened in January 2000.",
                "Before your visit it is worth phoning the museum's curator.",
            ]),
        ],
        hours=[("Thursday", "10:00–17:00"), ("Other days", "closed")],
        tickets=[("Admission", "free")],
    ),
    "muzeum-historii-ubioru": dict(
        name="Museum of the History of Clothing",
        img_alt="The exhibition “Fashion Likes to Repeat Itself” at the Museum of the History of Clothing",
        short="The history of fashion and clothing in a private foundation museum, 15 minutes on foot from the station.",
        badge="Closed Sun–Mon",
        status=None,
        lead="The Museum of the History of Clothing is run by the Museum of the History of Clothing Foundation, which uses the ticket income for its statutory activity. The museum is in the centre, about 15 minutes on foot from Poznań Główny station.",
        sections=[
            ("Good to know", [
                "The last entry is 30 minutes before closing.",
                "Groups of 10 to 21 people can order a guided tour: PLN 120 in Polish or PLN 150 in English, plus tickets.",
                "With the Poznań Tourist Card the ticket is cheaper.",
                "Getting there by tram (according to the ZTM timetable of 10 October 2026): 3, 4, 5, 8, 13, 15, 16 and 17 to the stop Wrocławska, or 2, 9 and 19 to the stop Pl. Wiosny Ludów.",
            ]),
        ],
        hours=[("Tuesday, Wednesday, Friday", "10:00–15:00"), ("Thursday", "15:00–19:00"), ("Saturday", "11:00–16:00"),
               ("Sunday–Monday", "closed")],
        tickets=[("Standard", "PLN 20"), ("Reduced", "PLN 15"), ("Children under 7", "free")],
    ),
    "schron-przeciwatomowy": dict(
        name="Nuclear Shelter and Poster Gallery",
        img_alt="Greenery by the above-ground buildings of the shelter on ul. Słupska 62",
        short="A secret shelter for the city authorities with original equipment from communist times and posters from the socialist era.",
        badge="Wed–Fri 10–16",
        status=None,
        lead="On ul. Słupska, in Krzyżowniki near Lake Kierskie, there is a secret nuclear shelter built for the mayor of Poznań and the city's top authorities.",
        sections=[
            ("What to see", [
                "The interiors of the shelter with the original, unchanged equipment from communist times.",
                "A Poster Gallery from the socialist period, divided into three themed parts.",
            ]),
            ("Good to know", [
                "The last entry (for the tour) is at 15:30, 30 minutes before closing.",
                "Individual visitors enter without booking. Booking applies only to organised groups, who reserve a visit by phone.",
                "The shelter is underground and is not accessible to wheelchair users.",
                "We confirmed the hours, prices and admission rules by phone with the site on 20 October 2026. The city's page about the shelter is undated and the website of the Museum of Independence in Greater Poland does not list it among its branches, so it is worth phoning before you visit: +48 887 222 465.",
                "During the Night of Museums on 16 May 2026 the shelter was open from 16:00 to midnight, with the last entry 30 minutes before closing, free admission and no booking.",
            ]),
        ],
        hours=[("Wednesday–Friday", "10:00–16:00, last entry 15:30"), ("Last Saturday of the month", "10:00–16:00, last entry 15:30")],
        tickets=[("Standard", "PLN 15"), ("Reduced", "PLN 10")],
    ),
    "gaspar": dict(
        name="GASPAR Museum of Old Tools and Machines",
        img_alt="",
        short="A private technology museum with mementoes of Hipolit Cegielski and a narrow-gauge railway.",
        badge="By appointment",
        status=None,
        lead="GASPAR is a private technology museum whose patron is Hipolit Cegielski, the founder of the famous Poznań HCP works.",
        sections=[
            ("What to see", [
                "Hand, carpentry and locksmith's tools and old machines.",
                "Mementoes connected with Hipolit Cegielski and the H. Cegielski – Poznań works.",
                "Buildings put up from salvaged materials in the half-timbered technique, and an original narrow-gauge railway.",
            ]),
            ("Good to know", [
                "The museum is open on selected weekends, and on other days by prior appointment.",
                "It is visited with a guide. The museum also runs themed workshops.",
                "Current dates and prices are on the museum's website.",
            ]),
        ],
        hours=[("Selected weekends", "dates at gaspar.org.pl"), ("Other days", "by appointment")],
        tickets=[("Ticket prices", "at gaspar.org.pl")],
    ),
    "muzeum-bizuterii-moja": dict(
        name="MoJA Jewellery Museum",
        img_alt="The entrance and the jewellery display window of the MoJA Jewellery Museum on ul. 27 Grudnia",
        short="Jewellery in permanent and temporary exhibitions, next to the Okrąglak and the Teatr Polski.",
        badge="Closed Tue",
        status=None,
        lead="The MoJA Jewellery Museum is on ul. 27 Grudnia, next to the Okrąglak and the Teatr Polski, a few minutes' walk from Plac Wolności.",
        sections=[
            ("What to see", [
                "Permanent and temporary exhibitions of jewellery and a shop with artistic jewellery.",
            ]),
            ("Good to know", [
                "The reduced ticket applies to pupils, students, teachers and seniors from the age of 60.",
                "Groups of 10 or more can order a tour by a curator and workshops (PLN 25–40 per person).",
                "Tickets can be bought online at tobilet.pl.",
            ]),
        ],
        hours=[("Tuesday", "closed"), ("Other days", "10:00–18:00")],
        tickets=[("Standard", "PLN 35"), ("Reduced", "PLN 15"), ("Children under 6", "free")],
    ),
    "salon-nowowiejskiego": dict(
        name="Feliks Nowowiejski Music Salon",
        img_alt="The villa of Feliks Nowowiejski in Poznań",
        short="The villa of the composer of the “Rota”, with its original interior, instruments and chamber concerts.",
        badge="Tue–Sat",
        status=None,
        lead="The Music Salon opened on 7 February 2008 in the villa in which Feliks Nowowiejski, the composer of the melody of the “Rota”, lived and worked in 1929–1939 and where he died in 1946. It is run by the Feliks Nowowiejski Society.",
        sections=[
            ("What to see", [
                "The original layout of the interiors, works of art, instruments and the composer's everyday objects.",
            ]),
            ("Good to know", [
                "Chamber concerts are held in the salon, recalling the tradition of the Nowowiejski home in the interwar and post-war period, as well as workshops for children.",
                "Organised groups should book a guided visit in advance.",
            ]),
        ],
        hours=[("Tuesday–Saturday", "10:00–16:00"), ("Sunday–Monday", "closed")],
        tickets=[("Standard", "PLN 15"), ("Reduced", "PLN 13")],
    ),
}
