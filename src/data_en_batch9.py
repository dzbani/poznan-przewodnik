# -*- coding: utf-8 -*-
"""Angielskie tłumaczenia, partia 9 (14.10.2026): kościoły, forty, Śródka, cmentarz. Zasady: data_en.py."""

CHURCH_NOTE = "This is a working church. It cannot be visited during Mass and services, and you are asked to dress modestly and keep quiet."
CH_HOURS = [("Visiting", "outside services"), ("Mass times", "in the parish notices")]

EN_BATCH9 = {
    "kosciol-nmp-in-summo": dict(
        name="Church of Our Lady in Summo",
        img_alt="The Gothic church of Our Lady in Summo against the background of the cathedral",
        short="A 15th-century Gothic church on the site of a chapel from the time of Mieszko I and Dobrawa.",
        badge="Free",
        status=None,
        lead="The Gothic church of Our Lady in Summo stands on Ostrów Tumski, next to the cathedral. It was consecrated on 2 July 1448. In the 10th century the chapel of Mieszko I's palace stood on this site.",
        sections=[
            ("History", [
                "According to tradition a pre-Romanesque chapel was raised around 965 by Dobrawa, the wife of Mieszko I, who was a Christian before his baptism. It was the oldest church in the Poznań stronghold and probably in the whole Piast state.",
                "Around 1430 the old church was demolished and a new, Gothic one began to be built. It was consecrated by Bishop Andrzej of Bnin.",
                "Since 1999 archaeological research under Prof. Hanna Kóčka-Krenz has been going on around the church, uncovering remains of the palace complex of Mieszko I.",
            ]),
            ("What to see", [
                "Polychrome painting, stained glass and a high altar designed by Prof. Wacław Taranczewski after 1954.",
                "Next to the church lies the Genius Loci Archaeological Reserve, which organises visits to the church and its surroundings.",
            ]),
        ],
        hours=[("Church", "open to visitors, outside services")],
        tickets=[("Admission", "free")],
    ),
    "kosciol-bozego-ciala": dict(
        name="Corpus Christi Church",
        img_alt="The Gothic façade of Corpus Christi Church with its gate",
        short="A Gothic church founded by Władysław Jagiełło on a site connected with the miracle of the Host.",
        badge="Free entry",
        status=None,
        lead="The church stands on a site connected with the tradition of the miraculous finding of a Host in 1399. In 1406 King Władysław Jagiełło founded a church and a Carmelite monastery here.",
        sections=[
            ("History", [
                "The brick church was completed at the turn of the 15th and 16th centuries. Around 1570 a chapel was added, which Pompeo Ferrari rebuilt around 1726.",
                "Destroyed during the Swedish Deluge, it was rebuilt in the Baroque style by 1664. After the dissolution of the order in 1823 it fell into decline and was saved by a renovation in 1856. Since 1899 it has been a parish church.",
            ]),
            ("What to see", [
                "A three-aisled Gothic interior with star vaults of the 15th century in the side aisles and 17th-century paintings in the nave.",
                "The high altar of about 1740 with the painting “The Last Supper”.",
                "Portraits of King Władysław Jagiełło and St Hedwig in the chancel, and heraldic plaques of Greater Poland nobility.",
                "The Chapel of Our Lady of the Scapular and a Baroque choir loft of the 17th century.",
            ]),
            ("Good to know", [
                "The nearby church of the Most Holy Blood of Jesus on ul. Żydowska is connected with the same tradition of 1399.",
                CHURCH_NOTE,
            ]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "kosciol-sw-jozefa": dict(
        name="St Joseph's Church (Discalced Carmelites)",
        img_alt="The Baroque church of the Discalced Carmelites of St Joseph",
        short="A Baroque Carmelite church where the prototype of Jan Skrzetuski from “With Fire and Sword” is buried.",
        badge="Free entry",
        status=None,
        lead="The Baroque church was built in 1644–1678 to a design by Krzysztof Bonadura the Elder and Jerzy Catenazzi. Since its rebuilding after 1945 it has been looked after by the Discalced Carmelites.",
        sections=[
            ("History", [
                "After the dissolution of the monastery the Prussians gave the church to the army. After 1840 the interior was rebuilt to a design by Karl Friedrich Schinkel as a Protestant garrison church.",
                "After Poland regained independence it was a Catholic garrison church. The monastery, damaged in the war, was rebuilt until 1966.",
            ]),
            ("What to see", [
                "A three-aisled interior with fittings from 1984–1988 and paintings by Albert Tschautsch of 1878 in the transept.",
                "In the porch a fragment of the tombstone of the convent's benefactor Wojciech Konarzewski, and a plaque commemorating Mikołaj Skrzetuski, the prototype of Jan Skrzetuski from Sienkiewicz's “With Fire and Sword”, who is buried in the crypt.",
                "The hermitage of St Raphael Kalinowski in the crypt, arranged in 1987, and his monument in front of the church.",
            ]),
            ("Good to know", [CHURCH_NOTE]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "kosciol-sw-malgorzaty": dict(
        name="St Margaret's Church in Śródka",
        img_alt="St Margaret's Church in Śródka",
        short="A 14th-century Gothic church on Śródka Market Square, right next to the mural.",
        badge="Free entry",
        status=None,
        lead="The first church in Śródka was probably built before 1231. The present church was raised in the 14th century. In 1671–1805 it belonged to the Philippines (Oratorians).",
        sections=[
            ("History", [
                "In the 15th century the Chapel of St Barbara was added, and around 1652 the Chapel of St Philip Neri.",
                "The church, burned during the Swedish Deluge, was rebuilt in 1658 and at that time partly lost its medieval character.",
            ]),
            ("What to see", [
                "A single-aisled interior with a late Gothic star vault.",
                "The high altar with an image of Our Lady in a silver dress from the end of the 17th century.",
                "A painting of Our Lady with the Child on a crescent from the early 17th century and a painting with music-making angels from about 1603 in the Chapel of St Barbara.",
                "The former house of the Congregation of the Philippines of 1746–1777 next to the church.",
            ]),
            ("Good to know", [
                "The church stands in Śródka, a few steps from the three-dimensional mural and the Gate of Poznań.",
                CHURCH_NOTE,
            ]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "kosciol-dominikanow": dict(
        name="Dominican Church (Most Sacred Heart of Jesus and Our Lady of Consolation)",
        img_alt="The Dominican church on ul. Szewska",
        short="A Dominican church of 1244 with a shrine of Our Lady of the Rosary.",
        badge="Free entry",
        status=None,
        lead="The first Dominican church was founded in 1244 by the Greater Poland dukes Przemysł I and Bolesław the Pious. The church received its present form at the beginning of the 18th century to a design by Jan Catenazzi. It is a shrine of Our Lady of the Rosary.",
        sections=[
            ("History", [
                "Parts of the early Gothic walls of the 13th century survive, with a portal in the west façade uncovered in 1923.",
                "The Chapel of Our Lady of the Rosary from the 15th century probably stands on the site of the former church of St Gothard. It received its present form in 1900–1901.",
            ]),
            ("What to see", [
                "Baroque fittings of the 18th century, including the high altar of 1760 with a painting of Our Lady of the Rosary with St Dominic.",
                "Mannerist choir stalls of 1620–1630 with scenes from the lives of St Dominic and St Hyacinth, and a Baroque pulpit of 1714–1716.",
                "In the Chapel of Our Lady of the Rosary, a venerated painting of Our Lady with the Child of 1631, crowned in 1968, and a Gothic bronze tomb slab from the Vischer workshop of Nuremberg.",
            ]),
            ("Good to know", [CHURCH_NOTE]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "kosciol-zbawiciela": dict(
        name="Church of the Most Holy Saviour",
        img_alt="The Neo-Gothic Church of the Most Holy Saviour",
        short="A Neo-Gothic church with a soaring tower, built in 1866–1869 for Protestants.",
        badge="Free entry",
        status=None,
        lead="The Neo-Gothic church was built in 1866–1869 to a design by August Stüler and Juliusz Hochberger for the Protestant parish of St Paul. It has been Catholic since 1945.",
        sections=[
            ("History", [
                "The Catholic parish was established here in 1950.",
            ]),
            ("What to see", [
                "The soaring tower and a tondo with a sculpted head of Christ above the main portal.",
                "A three-aisled interior with star and cross vaults and surviving wooden galleries.",
                "A Passion sculpture by Lech Czuba of 2000, a Neo-Gothic font of 1867–1869 and an organ of 1912.",
            ]),
            ("Good to know", [CHURCH_NOTE]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "kosciol-sw-anny": dict(
        name="St Anne's Church",
        img_alt="The Neo-Gothic church of St Anne in Łazarz",
        short="A Neo-Gothic church in Łazarz with a clock tower and original stained glass.",
        badge="Free entry",
        status=None,
        lead="The Neo-Gothic church in Łazarz was built in 1904–1907. At first it belonged to the Protestant church, and since 1945 it has been Catholic.",
        sections=[
            ("History", [
                "The church has three aisles and is built on the plan of a Greek cross.",
            ]),
            ("What to see", [
                "A clock tower, three decorated portals and Neo-Gothic gables.",
                "Crystal and cross-rib vaults, polychrome painting and original stained glass.",
                "An 18th-century painting of the Suffering Christ, a copy of a painting by Leonardo da Vinci with the face of St Anne and bas-reliefs by the 19th-century Italian artist Cirillo dell'Antonio.",
            ]),
            ("Good to know", [CHURCH_NOTE]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "kosciol-najsw-krwi": dict(
        name="Church of the Most Holy Blood of Jesus",
        img_alt="The façade of the Church of the Most Holy Blood of Jesus on ul. Żydowska",
        short="A church in a former townhouse connected with the tradition of the miracle of the three Hosts of 1399.",
        badge="Free entry",
        status=None,
        lead="The church stands on the site of a townhouse connected with the tradition of the so-called miracle of the three Hosts of 1399. In the 17th century the Carmelites rebuilt it into a church, using the Gothic walls and a cellar with a small well.",
        sections=[
            ("History", [
                "The building took its present appearance at the beginning of the 20th century. Fragments of the old walls can be seen on the façade.",
            ]),
            ("What to see", [
                "A sculpture of Our Lady with the Child from the turn of the 15th and 16th centuries above the entrance, moved from the Old Market Square.",
                "A late Baroque interior with a high altar of 1733 and paintings on the vault of 1735.",
                "A sculpture “Lamentation of Christ” from the early 16th century.",
                "A chapel in the crypt with a small well. According to tradition its water helped especially with eye diseases.",
            ]),
            ("Good to know", [
                "Corpus Christi Church on ul. Strzelecka is connected with the same tradition.",
                CHURCH_NOTE,
            ]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "kosciol-zmartwychwstania": dict(
        name="Church of the Resurrection of the Lord",
        img_alt="The neoclassical façade of the Church of the Resurrection of the Lord in Wilda",
        short="A neoclassical votive church for independence, with a portico like a Greek temple.",
        badge="Free entry",
        status=None,
        lead="The church was built in 1923–1926. Its neoclassical form was meant to express gratitude for the regaining of independence in 1918 and to commemorate the 950th anniversary of the baptism of Poland. It has been run by the Resurrectionists from the beginning.",
        sections=[
            ("History", [
                "The architecture and decoration refer to the symbolism of rebirth and victory.",
            ]),
            ("What to see", [
                "A monumental portico with Ionic columns, recalling a Greek temple.",
                "A single-aisled hall interior with a coffered ceiling and a statue of the victorious Christ in the chancel.",
                "A tower with figures of Polish saints: Andrew Bobola, Casimir, Stanislaus of Szczepanów and John Cantius.",
            ]),
            ("Good to know", [CHURCH_NOTE]),
        ],
        hours=CH_HOURS,
        tickets=[("Admission", "free")],
    ),
    "fort-iii": dict(
        name="Fort III",
        img_alt="Fort III on the grounds of the New Zoo, the barracks and the bridge over the moat",
        short="A Prussian main fort of 1881 on the grounds of the New Zoo. Guided visits in season, including the underground.",
        badge="May–September",
        status=None,
        lead="Fort III was built by the Prussian army in 1877–1881. It is one of the 18 artillery forts of the Poznań Fortress and one of nine forts of the main type. It lies on the grounds of the New Zoo on ul. Krańcowa.",
        sections=[
            ("What to see", [
                "The fort is surrounded by a dry moat 850 m long, 5.5 m deep and 9 m wide. Its access is guarded by five caponiers. Along the whole length of the front and shoulders runs an artillery rampart with emplacements for 21 guns of 15 and 12 cm calibre.",
                "The entrance was defended by a blockhouse and a drawbridge. In the central part there are two courtyards separated by the embankment of a poterne, which links the two-storey barracks with the lower floor.",
                "The route includes an underground and an above-ground part. A permanent exhibition tells the history of the Poznań Fortress, in the barracks you can see how the soldiers lived, and on the rampart stand an armoured observation dome and a position with traces of the carriage of the fortress's largest gun, with a range of 7,700 m.",
                "In the underground the temperature is a constant 12 °C. There is a large powder magazine for 35 tonnes of black powder and a shoulder caponier with walls more than 2.5 m thick. The corridors are lit by paraffin lamps.",
            ]),
            ("History", [
                "In 1889 the fort was strengthened by adding batteries for extra guns on the shoulders. Later modernisations brought armoured infantry and artillery observation posts.",
            ]),
            ("Good to know", [
                "The fort lies within the New Zoo, so besides a ticket to the fort you need a ticket to the Zoo. Guides wait at the gate from ul. Krańcowa 81. Visiting without a Zoo ticket is possible by arrangement with the organiser in advance.",
                "The route lasts about an hour. No booking is required. The fort was prepared for visitors by the Poznań Society of Friends of Fortifications.",
                "Tickets for the fort are sold at the fort's entrance, 200 m from the Zoo ticket offices, on visiting days from 10:30.",
                "The city portal gives visits from May to September on Saturdays, Sundays and public holidays, with entries at 11:00, 12:30, 14:00, 15:30 and 17:00. Organised groups can also arrange other hours and weekdays. It is worth checking the dates for the next season by phone before your visit.",
            ]),
        ],
        address="ul. Krańcowa 81, 61-070 Poznań (on the grounds of the New Zoo)",
        hours=[("Season", "May–September (the 2026 season ended in September; outside the season the sources do not give regular entries)"),
               ("Saturdays, Sundays and public holidays", "guided visits, entries according to poznan.pl at 11:00, 12:30, 14:00, 15:30 and 17:00; check by phone")],
        tickets=[("Fort, standard", "PLN 8"), ("Fort, reduced", "PLN 6"), ("With the Poznań Tourist Card", "50% discount"),
                 ("Zoo ticket", "required separately")],
    ),
    "fort-iva": dict(
        name="Fort IVa",
        img_alt="Fort IVa in Poznań",
        short="A Prussian fort of 1881, today a winter roost for bats. Open on the first Sunday of the month.",
        badge="1st Sunday of the month",
        status=None,
        lead="Fort IVa in Wilczy Młyn was built by the Prussian army in 1878–1881. It is one of the 18 forts of the second ring of the Poznań Fortress and one of six intermediate forts of the new type.",
        sections=[
            ("History", [
                "In 1888 the fort was modernised and strengthened, among other things by adding reverse caponiers and walls protecting against blast.",
                "In the interwar period the Polish Army kept stores here. Signatures of soldiers survive in the barracks.",
                "During the fighting for Poznań in 1945 the fort defended itself for only two hours. Traces of the fighting can be seen on the walls in the underground. In 1952–1965 the fort was blown up and partly demolished.",
            ]),
            ("Today", [
                "In 1997 the fort was taken over by scouts, who together with the Polish Society for the Protection of Nature “Salamandra” secured the underground.",
                "The underground is a winter roost for several species of bats, among them the greater mouse-eared bat, Natterer's bat and the common serotine.",
            ]),
            ("Good to know", [
                "You must register your visit in advance by phone. Another date can also be arranged.",
            ]),
        ],
        address="Wilczy Młyn, 61-602 Poznań",
        hours=[("Visiting", "1st Sunday of the month, 10:00–14:00"), ("Registration", "in advance, by phone")],
        tickets=[("Admission", "free")],
    ),
    "fort-va": dict(
        name="Fort Va Bonin",
        img_alt="Fort Va Bonin in Poznań",
        short="A Prussian fort with a guide in a historic uniform. From May to September, on the last Saturdays.",
        badge="Seasonal",
        status=None,
        lead="Fort Va was built by the Prussian army in 1887–1890 and named Bonin. It belongs to the second ring of the Poznań Fortress. The tourist route leads through the most important parts of the fort, above and below ground.",
        sections=[
            ("Visiting", [
                "The fort is visited only with a guide dressed in a historic uniform. The route lasts about an hour.",
                "The fort is looked after, and the route is led, by the Kernwerk Society of Friends of Fortifications.",
                "Organised groups (of 15 or more) can visit the fort on other days after contacting the society in advance.",
            ]),
        ],
        hours=[("May–September", "last Saturday of the month"), ("Entries", "12:00 and 15:00"),
               ("October–April", "the sources do not give regular visits (the 2026 season ended in September)")],
        tickets=[("Standard", "PLN 15"), ("Reduced", "PLN 10")],
    ),
    "rynek-srodecki": dict(
        name="Śródka Market Square (Rynek Śródecki)",
        img_alt="Śródka Market Square and ul. Filipińska in Śródka",
        short="The former main square of Śródka with St Margaret's Church, the Philippines' monastery and a 3D mural.",
        badge="Free",
        status=None,
        lead="Śródka Market Square was the central square of Śródka, a former separate town that is now a district of Poznań. Centuries ago it had its own town hall, and until the 1960s the square had a larger area than the Old Market Square.",
        sections=[
            ("History", [
                "The town hall stood on the site of today's townhouse with the post office. The square shrank when the Chwaliszewska route (ul. Wyszyńskiego) was built and some townhouses were demolished: the southern frontage and one townhouse of the eastern frontage. A large part of the buildings had been destroyed earlier by the war.",
                "Until 2010 the Malta cinema stood by the square.",
            ]),
            ("What to see", [
                "St Margaret's Church and the Philippines' monastery by the square.",
                "The three-dimensional mural “A Śródka Tale with a Trumpeter on the Roof and a Cat in the Background”, unveiled on 1 October 2015 on the townhouse at ul. Śródka 3. It was based on a photograph from the 1920s.",
                "A plaque unveiled on 27 December 1998, on the 80th anniversary of the Greater Poland Uprising, on the building at no. 15.",
            ]),
            ("Good to know", [
                "The streets Bydgoska, Filipińska, Śródka and Wyszyńskiego lead off the square. From here you can walk to the Bishop Jordan Bridge and Ostrów Tumski.",
            ]),
        ],
        hours=[("Square", "open 24 hours")],
        tickets=[("Admission", "free")],
    ),
    "most-biskupa-jordana": dict(
        name="Bishop Jordan Bridge",
        img_alt="The Bishop Jordan Bridge with a view of Poznań Cathedral",
        short="A pedestrian and cycle footbridge over the Cybina between Śródka and Ostrów Tumski, on the site of a crossing a thousand years old.",
        badge="Free",
        status=None,
        lead="The Bishop Jordan Bridge, also called the Cybina or Śródka Bridge, is a pedestrian and cycle footbridge over the Cybina river. It links Śródka (ul. Ostrówek) with Ostrów Tumski and leads straight towards a view of the cathedral.",
        sections=[
            ("History of the crossing", [
                "A crossing at this place existed from the early Middle Ages. In 2007 the remains of a 10th-century bridge (37 oak elements) were discovered, and the oldest mention of bridges dates from 1146.",
                "In 1905 a steel truss bridge with tram tracks was opened, and on 13 November 1913 a newer one. It was blown up on 5 September 1939 by retreating units of the Polish Army. A temporary post-war crossing existed until the end of the 1960s. This broke a route that had been in use for almost a thousand years.",
            ]),
            ("The new bridge", [
                "The new bridge was officially opened on 7 December 2007. It uses the steel main span from the dismantled Roch Bridge. The 70-metre span was moved over the Mieszko I Bridge on 29 September 2007.",
                "It is a pedestrian and cycle footbridge. The name commemorates Jordan, the first bishop of Poznań and of Poland.",
            ]),
            ("Good to know", [
                "From the bridge you can see Poznań Cathedral.",
            ]),
        ],
        address="ul. Ostrówek, 61-125 Poznań (Śródka – Ostrów Tumski)",
        hours=[("Bridge", "open 24 hours")],
        tickets=[("Crossing", "free")],
    ),
    "cmentarz-zasluzonych-wielkopolan": dict(
        name="Cemetery of Distinguished Greater Poland People",
        img_alt="A historic tombstone in the Cemetery of Distinguished Greater Poland People",
        short="Poznań's oldest necropolis on St Adalbert Hill. The graves of Gen. Taczak, city mayors and Prime Minister Mikołajczyk.",
        badge="Free",
        status=None,
        lead="The cemetery on the northern slope of St Adalbert Hill is the oldest necropolis in Poznań. It was founded at the beginning of the 19th century as the cemetery of the Fara parish, and since 1948 it has been the resting place of distinguished Greater Poland people.",
        sections=[
            ("History", [
                "The site for the cemetery was designated in 1808, and the oldest surviving tombstone is dated 1813. From the end of the 19th century, when the parish received a new cemetery, it was called the old Fara cemetery.",
                "In 1948 it was decided that the old cemetery would become a necropolis of distinguished Greater Poland people. In 1959 the remains of 79 people from the cemetery on ul. Towarowa, which was being closed, were moved here. On 11 January 1971 the parish handed the necropolis to the secular authorities.",
            ]),
            ("What to see", [
                "A Baroque figure of Our Lady of 1771, moved from the Reformed Franciscan monastery in Śródka.",
                "The tombstone of Aniela Dembińska, née Liszkowska, who died aged 20, carved in 1889 in Paris by Władysław Marcinkowski.",
                "The graves of, among others, Gen. Stanisław Taczak, the first commander of the Greater Poland Uprising, Prime Minister Stanisław Mikołajczyk, the city mayors Szymon Wroniecki, Jarogniew Drwęski and Cyryl Ratajski, and the pianist Raul Koczalski. Hipolit Cegielski is commemorated by a symbolic grave.",
                "A stone dedicated to “the Greater Poland people who did not return from the mountains”, set up in 1994 by the Polish Tatra Society.",
            ]),
            ("Good to know", [
                "The seemingly grave-free clearing at the foot of the hill is a mass grave of victims of the cholera epidemics of 1831–1873.",
                "The visiting hours are given by the poznan.pl portal. The same page has a grave search engine. This is a working cemetery, so the behaviour appropriate to such a place applies.",
            ]),
        ],
        hours=[("Entry", "daily 10:00–18:00")],
        tickets=[("Admission", "free")],
    ),
}
