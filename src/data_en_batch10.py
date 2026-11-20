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
        short="Weapons, uniforms and mementoes of the national uprisings, and a fragment of Wojciech Kossak's panorama “The Battle of the Pyramids”.",
        badge="Closed Mon",
        status=None,
        lead="The Greater Poland Military Museum, a branch of the National Museum in Poznań, is housed in one of the two pavilions built on the Old Market Square after the wartime destruction. It shows Polish and foreign weapons and mementoes of the national uprisings, especially the Greater Poland Uprising of 1918–1919.",
        sections=[
            ("What to see", [
                "The permanent exhibition shows edged and firearms, protective armour, military insignia, uniforms and equipment. According to the museum's website it covers the period from the 10th to the 21st century, and according to poznan.pl Polish and foreign weapons and protective armour from the 11th to the 18th century and mementoes of the national uprisings.",
                "The largest and most spectacular fragment of Wojciech Kossak's panorama “The Battle of the Pyramids” of 1901, one of the few objects that survived from the museum's pre-war collections.",
                "A bechter, that is, the armour of the city's cavalry captain of 1580, decorated on the neck guard with the coat of arms of Poznań.",
                "A 16th-century sword-rapier with a blade forged in Milan, one of the most valuable gifts to museums.",
                "A collection of mementoes of the Greater Poland Uprising of 1918–1919 and the Greater Poland Army, from which the museum traces its origins.",
                "Temporary exhibitions are held in the first part of the ground floor, and occasional shows in the hall.",
            ]),
            ("History", [
                "The museum came into being after the Greater Poland Uprising. General Józef Dowbor-Muśnicki entrusted the creation of a historical-military museum to the Scientific Section of the High Command, which in March 1919 took over the collections of the former Hindenburg Museum. The museum was opened by Józef Piłsudski on 27 October 1919 and made available to the public in December 1920.",
                "From 1923 the museum had its own seat at ul. Artyleryjska 1. In September 1939 the most valuable exhibits were evacuated, and the German occupation authorities liquidated the museum. In December 1956 the painter Stefan Pajączkowski took the initiative to re-establish a military museum.",
                "In July 1962 a building in the middle of the Old Market Square was acquired, and the exhibition was opened on 22 February 1963 as the Army Museum. In 1966 the museum was confirmed as a branch of the National Museum in Poznań and its historic name, the Greater Poland Military Museum, was restored.",
            ]),
            ("Good to know", [
                "The ticket office closes 30 minutes before the museum closes. On Tuesdays admission is free, and children and young people aged 8 to 26 pay PLN 1. Next to the price list the museum's website shows the symbols of the Large Family Card and the Poznań Tourist Card but does not give the terms of the concessions, so check them at the ticket office.",
                "The museum is closed on 1 January, Good Friday, Holy Saturday, Easter Sunday and Easter Monday, on Corpus Christi, and on 1 November, 24, 25, 26 and 31 December. It is open (hours as on Sunday) on 6 January, 1 and 3 May, 15 August and 11 November.",
                "In 2026 “quiet hours” between 15:00 and 17:00 apply on the first Sunday of the month. The next one is 6 December.",
                "The building has two storeys and a winding staircase to the first floor, and there is no lift. The ground floor is architecturally accessible. There is no toilet for people with disabilities in the building.",
            ]),
        ],
        hours=[("Monday", "closed"), ("Tuesday–Wednesday", "10:00–16:00"), ("Thursday", "10:00–18:00"),
               ("Friday", "10:00–20:00"), ("Saturday–Sunday", "10:00–17:00")],
        tickets=[("Standard", "PLN 15"), ("Reduced", "PLN 10"), ("Children and young people aged 8–26", "PLN 1"),
                 ("Tuesday", "free admission")],
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
        img_alt="The brick façade of the Lubrański Academy with the name above the entrance and exhibition boards in the courtyard",
        short="Sacred art in a Renaissance building of the 16th century: the sword of St Peter and King Jagiełło's monstrance.",
        badge="Closed Mon",
        status=None,
        lead="The Archdiocesan Museum was founded in 1894–1898 by Archbishop Florian Stablewski. It is one of the first museums in Poznań (Visit Poznań calls it the oldest) and one of the oldest museums of its kind in Poland. It is housed on Ostrów Tumski, in the building of the former Lubrański Academy, about 100 m from the cathedral.",
        sections=[
            ("What to see", [
                "Sacred art from the Middle Ages to the present, including the richest collection of sculpture and painting of the 14th and 15th centuries in this part of Poland.",
                "The sword of St Peter, the monstrance of King Władysław Jagiełło, the golden chalice of Bishop Tolibowski and a crosier from Limoges.",
                "Galleries of portraits, Polish and European painting, textiles and goldsmiths' work.",
            ]),
            ("History of the building and the museum", [
                "The Lubrański Academy was founded in 1518 by Bishop Jan Lubrański. Its four-wing brick building with a courtyard was built in 1518–1530, using a stretch of the wall around Ostrów Tumski. Visit Poznań gives the year 1520.",
                "The museum was founded in 1898 and its collections first went to a former Carmelite convent on ul. Wieżowa. They were moved to the Academy building after a renovation and the arrangement of a new exhibition, and the ceremonial opening took place in September 2007.",
            ]),
            ("Good to know", [
                "The last visitors are admitted half an hour before closing. The museum is adapted for people with disabilities.",
                "With the Poznań Tourist Card admission is free (according to Visit Poznań).",
                "An audio guide can be borrowed free of charge with every ticket.",
                "Educational activities: edukacja@muzeum.poznan.pl, tel. +48 605 988 300.",
            ]),
        ],
        hours=[("Tuesday–Friday", "11:00–17:00"), ("Saturday", "11:00–16:00"), ("Sunday–Monday", "closed")],
        tickets=[("Standard", "PLN 40"), ("Reduced", "PLN 30"), ("Family", "PLN 80"), ("Special", "PLN 15"), ("Guide", "PLN 100"), ("Workshops", "PLN 100")],
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
        short="The history of clothing in temporary exhibitions and the largest private collection of complete 19th-century dresses in Poland.",
        badge="Closed Sun–Mon",
        status=None,
        lead="The Museum of the History of Clothing is a non-public institution and funds its activity on its own. Its mission is to bring historical clothing closer to people as a field of applied art and a witness to history. Its organisational and administrative work is run by the Museum of the History of Clothing Foundation, a non-profit organisation. The museum is in the centre, at ul. Kwiatowa 14/2, about 15 minutes on foot from the Main Station.",
        sections=[
            ("What to see", [
                "Temporary exhibitions. The museum is small but has a huge collection, so each exhibition shows a different part of it. Historic clothes, accessories and objects connected with crafts tell of everyday life, work, customs and social and technological change. The exhibitions often combine a historical perspective with current challenges, for example the impact of the clothing industry on the environment.",
                "The permanent exhibition: a collection of historic clothing and fashion accessories coming mainly from the 19th century, created by Anna Moryto. It is the largest private collection in Poland of complete 19th-century dresses, regularly made available to the public. The steadily growing collection contains more than 50 historic exhibits.",
                "The museum also runs educational activities: it organises workshops, lectures and meetings with experts.",
            ]),
            ("Good to know", [
                "The last entry is 30 minutes before closing. People who want to visit the museum on other days or at other times, and organised groups, are asked to contact it by phone or e-mail.",
                "Organised groups (more than 10 people, at most 21) can order a guided tour: PLN 120 in Polish or PLN 150 in English, plus tickets.",
                "A reduced ticket is available to pupils, students up to 26, seniors over 65, people with disabilities and pensioners. Tickets are bought at the museum's ticket office or on the ToBilet platform. The money from ticket sales goes entirely to the statutory activity of the Foundation.",
                "With the Ok Poznań card the ticket costs PLN 17 (reduced PLN 12.75), and with the Poznań Tourist Card PLN 14 (reduced PLN 10.50).",
                "Getting there according to the museum's website: trams 2, 3, 6, 9, 12, 13, 16 and 18 to the stops Wrocławska, Plac Wiosny Ludów or Królowej Jadwigi. Current timetables are on the ZTM Poznań website.",
            ]),
        ],
        hours=[("Tuesday, Wednesday, Friday", "10:00–15:00"), ("Thursday", "15:00–19:00"), ("Saturday", "11:00–16:00"),
               ("Sunday–Monday", "closed"), ("Last entry", "30 minutes before closing")],
        tickets=[("Standard", "PLN 20"), ("Reduced", "PLN 15"), ("With the Ok Poznań card", "PLN 17 / reduced PLN 12.75"),
                 ("With the Poznań Tourist Card", "PLN 14 / reduced PLN 10.50"), ("Children under 7", "free")],
    ),
    "schron-przeciwatomowy": dict(
        name="Nuclear Shelter and Poster Gallery",
        img_alt="The above-ground building of the shelter at ul. Słupska 62, with a red roof, behind a fence and arborvitae trees",
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
        img_alt="The courtyard of the GASPAR museum with brick and half-timbered buildings and a well",
        short="A private technology museum with mementoes of Hipolit Cegielski and a narrow-gauge railway.",
        badge="Weekends",
        status=None,
        lead="GASPAR is a private technology museum whose patron is Hipolit Cegielski, the founder of the famous Poznań HCP works.",
        sections=[
            ("What to see", [
                "Hand, carpentry and locksmith's tools and old machines.",
                "Mementoes connected with Hipolit Cegielski and the H. Cegielski – Poznań works.",
                "Buildings put up from salvaged materials in the half-timbered technique, and an original narrow-gauge railway.",
            ]),
            ("Good to know", [
                "The museum is open on Saturdays and Sundays from 12:00 to 17:00, and on other days by prior appointment.",
                "It is visited with a guide, who is included in the ticket price (in Polish and English). The museum also runs themed workshops.",
                "The museum has no separate website: the address gaspar.org.pl leads to its profile on the Turturi service, where dates and prices are listed. According to that profile the museum is closed on 11 November and 24–26 December in 2026.",
                "A visit takes about an hour, and an organised group can have at most about 15 people. Contact by e-mail: muzeum@gaspar.org.pl.",
            ]),
        ],
        hours=[("Saturday and Sunday", "12:00–17:00"), ("Other days", "by appointment")],
        tickets=[("Standard", "PLN 30"), ("Reduced (under 18)", "PLN 25"), ("Family (1–2 adults + 1–3 children over 5)", "PLN 75"),
                 ("Group (more than 10 people)", "PLN 25 per person"), ("Children under 5", "free")],
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
