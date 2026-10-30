# -*- coding: utf-8 -*-
"""Angielskie tłumaczenia, partia 7 (14.10.2026): zabytki Starego Miasta i Ostrowa, nowoczesność, parki. Zasady: data_en.py."""

EN_BATCH7 = {
    "genius-loci": dict(
        name="Genius Loci Archaeological Reserve",
        img_alt="A wooden model made of logs and stones in the exhibition of the Genius Loci Archaeological Reserve, beside a glass staircase",
        short="The original defensive rampart of a 10th-century stronghold on Ostrów Tumski.",
        badge="Sun free",
        status=None,
        lead="The Genius Loci reserve on Ostrów Tumski shows the excellently preserved structures of the defensive rampart of the Poznań stronghold from the 10th century. It is run by the Archaeological Museum and opened in 2012.",
        sections=[
            ("What to see", [
                "Wooden structures of the stronghold's rampart from the time of the first Piasts, preserved in the ground for more than a thousand years.",
                "Exhibitions and multimedia presentations that show how fortifications were built in the early Middle Ages.",
            ]),
            ("Good to know", [
                "Getting there (according to the ZTM timetable of 10 October 2026): the stop Katedra is served by buses 167, 213, 223 and 911 and line T7, and trams 5, 6, 7 and 8 stop at Rondo Śródka. The reserve's website gives older line numbers, which do not match the current timetable.",
                "The site is adapted for people with disabilities.",
                "There is a ticket for three places on Ostrów Tumski (the Gate of Poznań, Genius Loci and the Lubrański Academy) at PLN 49.",
                "The last entry is half an hour before closing.",
            ]),
        ],
        hours=[("Monday", "closed"), ("Tuesday–Thursday", "10:00–16:00"), ("Friday–Saturday", "10:00–18:00"), ("Sunday", "10:00–15:00")],
        tickets=[("Standard", "PLN 20"), ("Reduced", "PLN 15"), ("Family (2 adults + 4 children)", "PLN 50"),
                 ("Sunday", "free admission to the exhibitions"),
                 ("Joint with the Górka Palace (Archaeological Museum)", "PLN 30, reduced PLN 25, family PLN 80")],
    ),
    "podziemia-katedry": dict(
        name="Poznań Cathedral Crypts",
        img_alt="Remains of earlier buildings in the crypts of Poznań Cathedral",
        short="Remains of the pre-Romanesque and Romanesque cathedrals, the remnants of the tombs of Mieszko I and Chrobry, and a 10th-century basin.",
        badge="Seasonal, paid",
        status=None,
        lead="Beneath Poznań Cathedral survive fragments of earlier buildings, discovered during archaeological research carried out when the church was rebuilt after the Second World War. You can see traces of earlier cathedrals here, including the one from the time of the first Piasts.",
        sections=[
            ("What to see", [
                "Fragments of the pre-Romanesque and Romanesque cathedral: walls of rubble stone and pre-Romanesque column bases.",
                "Remains of tombs, most probably of Poland's first rulers: Mieszko I and Bolesław the Brave.",
                "The remains of a 10th-century basin, perhaps a baptismal font from which Mieszko I may have been baptised together with his subjects. According to another hypothesis the basin was used for mixing lime.",
                "A lapidarium with fragments of tombstones, slabs and epitaphs, and the crypt in which the archbishops and auxiliary bishops of Poznań are buried.",
                "At the entrance hang boards by Prof. Zofia Kurnatowska on the history of the cathedral and Ostrów Tumski, and a film is shown during the visit.",
            ]),
            ("History of the discoveries", [
                "The main discoveries come from research carried out alongside the rebuilding of the cathedral (1946–1956). They revealed earlier phases of the church's construction, older than the Gothic.",
            ]),
            ("Good to know", [
                "You buy a ticket at the tourist service point on the cathedral grounds or in the sacristy. The cathedral is a working church: it cannot be visited during Mass, services and concerts, and you are asked to dress modestly and keep quiet.",
                "Besides the crypts you can climb the cathedral's viewing tower. More about the cathedral itself and Ostrów Tumski is on a separate page.",
            ]),
        ],
        hours=[("Season (1 Mar–15 Nov), weekdays", "9:00–16:00"), ("Season (1 Mar–15 Nov), Sundays", "14:00–18:00"),
               ("Winter", "crypts closed (poznan.pl)")],
        tickets=[("Standard", "PLN 10"), ("Reduced", "PLN 8"), ("Family", "PLN 25")],
    ),
    "domki-budnicze": dict(
        name="Domki Budnicze (Merchants' Houses)",
        img_alt="Colourful merchants' houses on the Old Market Square in Poznań",
        short="Narrow Renaissance townhouses with arcades on the south side of the town hall, former fish stalls and shops.",
        badge="Free",
        status=None,
        lead="The Domki Budnicze stand on the south side of the town hall, in the central block of buildings. They are a relic of the old trading buildings: in the Middle Ages wooden stalls stood here, where herrings, salt, candles and torches were sold.",
        sections=[
            ("History", [
                "In 1418 the city authorities established 17 fish stalls here. In the 16th century narrow townhouses with Renaissance arcades were built in their place, their arches resting on sandstone columns. Shops occupied the lower parts, and living rooms the upper ones.",
                "On the capital of the column of house no. 11 you can read the date 1535. The row is closed on the south by a townhouse of 1538 called the City Chancellery or the Scribes' House, today the seat of the Society of Friends of the City of Poznań, founded in 1922 by the mayor Cyryl Ratajski.",
                "During the Second World War the buildings were almost completely destroyed. They were rebuilt in 1953–1961 with polychrome decoration designed by Zbigniew Bednarowicz.",
            ]),
            ("What to see", [
                "The emblem of the merchants' guild on house no. 17: a herring and three palms. On the capital of the column of house no. 24 is the house mark of its former owners.",
                "Under the arcades Poznań artists sell their work, most often views of the Old Town. There are also souvenir shops.",
                "Behind the houses runs ul. Kurzanoga, which probably recalls an old townhouse of that name.",
            ]),
        ],
        address="Stary Rynek, 61-772 Poznań (on the south side of the town hall)",
        hours=[("Arcades", "open around the clock"), ("Shops and galleries", "according to the hours of individual venues")],
        tickets=[("Admission", "free")],
    ),
    "plac-wolnosci": dict(
        name="Plac Wolności (Freedom Square)",
        img_alt="The Freedom Fountain on Plac Wolności in Poznań",
        short="A showpiece square with the Freedom Fountain, surrounded by the Bazar, the National Museum and the Raczyński Library.",
        badge="Free",
        status=None,
        lead="Plac Wolności is a rectangular square measuring 85 by 205 m, west of the medieval centre. Poznań people call it “Plajta” in dialect. Today it is the city's drawing room, and in winter the site of the Poznań Bethlehem Christmas Market.",
        sections=[
            ("History", [
                "In 1798 the city bought the land for 2,500 thalers and levelled a hill called Mucha Góra (Fly Hill) to create the square. It was named Wilhelmsplatz, after the Prussian king Frederick William III.",
                "On 26 January 1919 Greater Poland soldiers and Gen. Józef Dowbor-Muśnicki took a solemn oath here. In April 1919 German monuments were removed from the square, and in June the square received its present name.",
            ]),
            ("What to see", [
                "The Freedom Fountain, switched on in 2012 at the eastern end of the square.",
                "The Hygieia Fountain on the north side, next to the Raczyński Library.",
                "Monuments around the square: the National Museum, the Hotel Bazar and the Raczyński Library, as well as historic townhouses and department stores.",
                "Four maple-leaved plane trees, which in 2023 were protected as natural monuments.",
                "In the townhouse of the Union Insurance Company of 1910–1911 (Plac Wolności 14) operates one of the oldest working lifts in Poland.",
            ]),
            ("Good to know", [
                "Under the square's surface is a three-level car park for more than 500 cars, opened in 2006.",
                "The square hosts fairs and seasonal events, among them the Poznań Bethlehem Christmas Market (in the 2026/27 season from 20 November to 6 January) and the Easter Fair. Current dates are in the events calendar.",
            ]),
        ],
        hours=[("Square", "open 24 hours")],
        tickets=[("Admission", "free")],
    ),
    "kolegium-jezuickie": dict(
        name="Former Jesuit College",
        img_alt="The Baroque building of the former Jesuit College",
        short="A Baroque building where Napoleon stayed. Today the seat of the Poznań City Hall.",
        badge="Free",
        status=None,
        lead="The Jesuit College operated in 1572–1773 as a secondary school with academic courses, the second in the city after the Lubrański Academy. The present Baroque building was built in 1701–1733 to a design by Giovanni Catenazzi. Today it houses the Poznań City Hall.",
        sections=[
            ("History", [
                "The college taught classical languages, mathematics, physics, philosophy and the natural sciences. At the beginning there were 16 professors and about 300 pupils. Adam Mickiewicz University and the St Mary Magdalene Secondary School continue its tradition.",
                "In November 1806 Napoleon Bonaparte lived here for almost three weeks. On 23 October 1805 Tsar Alexander I was a guest, and in 1815–1830 the governor of the Grand Duchy of Posen, Prince Antoni Radziwiłł, resided here.",
            ]),
            ("What to see", [
                "A three-storey, horseshoe-shaped building around an inner courtyard.",
                "Right next to it stands the Poznań Parish Church (Fara). In the season, from May to September, a tourist information point operates at pl. Kolegiacki 17.",
            ]),
        ],
        hours=[("Building seen from the square", "visible around the clock")],
        tickets=[("Viewing the building", "free")],
    ),
    "collegium-minus": dict(
        name="Collegium Minus",
        img_alt="Collegium Minus, the seat of the authorities of Adam Mickiewicz University",
        short="A Neo-Renaissance building of 1910, the seat of the rector of AMU. Concerts of the Poznań Philharmonic are held in the Aula.",
        badge="Outside free",
        status=None,
        lead="Collegium Minus is a building erected for the German Royal Academy, and since 1919 the seat of the authorities of Adam Mickiewicz University. Its front faces ul. Wieniawskiego, and it adjoins ul. Święty Marcin.",
        sections=[
            ("History", [
                "Edward Fürstenau's design was made in 1905–1906. Construction work lasted from spring 1907: the teaching part was handed over on 1 November 1909, and the Aula was solemnly opened on 18 January 1910.",
                "The building was a demonstration of the German presence in the face of Poznań's Polish community. It served the Academy for a little over four years, because during the First World War it housed a military hospital.",
                "In April 1919 the Polish authorities handed the building to the university being created. The name Collegium Minus was proposed on 5 April 1919 by Prof. Michał Sobeski, and on 7 May 1919 the University of Poznań was solemnly opened.",
            ]),
            ("What to see", [
                "The Neo-Renaissance façade with porticoes and tall gables on the ul. Wieniawskiego side.",
                "The University Aula: the hall is about 580 m², 33 m long and 17.5 m wide, and 14 m high above the stage. It is famous for its acoustics. Originally it was dominated by a 35-stop organ by Völkner of Bydgoszcz.",
                "The Lubrański Hall, called the Small Aula, with a copy of Jan Matejko's painting “The Founding of the Lubrański Academy” (the original is from 1886).",
            ]),
            ("Good to know", [
                "This is a working university building, so its interiors are not visited like a museum. The easiest way into the Aula is to attend a Poznań Philharmonic concert or another event. The repertoire is on the “Theatres and concerts” page.",
            ]),
        ],
        hours=[("From outside", "open 24 hours"), ("Aula", "during concerts and events")],
        tickets=[("Viewing from outside", "free"), ("Concerts in the Aula", "tickets sold by the organiser")],
    ),
    "palac-dzialynskich": dict(
        name="Działyński Palace",
        img_alt="The façade of the Działyński Palace with a pelican on the attic",
        short="A palace on the Old Market Square with a pelican on the attic, in the 19th century a centre of Polishness.",
        badge="Free",
        status=None,
        lead="The palace on the Old Market Square was built in 1773–1776 by the architect Antoni Höhne for the Grand Marshal of Lithuania Władysław Roch Gurowski.",
        sections=[
            ("What to see", [
                "The imposing east façade divided by pilasters in the Corinthian order.",
                "The pelican on the obelisk at the top of the attic. In heraldry it symbolises sacrifice, and in the time of the partitions it became a symbol of Polish resistance.",
            ]),
            ("History", [
                "In the 19th century the palace was a centre of the cultural and political life of Poles. In the Red Room there were meetings connected with the uprisings of 1830, 1848 and 1863, as well as exhibitions, concerts and lectures, including by the philosopher August Cieszkowski.",
                "Today it houses institutes of the Polish Academy of Sciences and a branch of the Kórnik Library.",
            ]),
        ],
        hours=[("Façade", "visible around the clock")],
        tickets=[("Viewing the façade", "free")],
    ),
    "wzgorze-sw-wojciecha": dict(
        name="St Adalbert Hill",
        img_alt="St Adalbert's Church in Poznań",
        short="The Crypt of Distinguished Greater Poland People: the tomb of Józef Wybicki and the heart of Gen. Dąbrowski.",
        badge="By appointment",
        status=None,
        lead="By St Adalbert's Church is the Crypt of Distinguished Greater Poland People, founded in 1923 on the initiative of the parish priest Fr Bogusław Kościelski. It was modelled on the Skałka in Kraków.",
        sections=[
            ("Who is buried here", [
                "Józef Wybicki, author of the words of “Dąbrowski's Mazurka”, and Antoni Kosiński, co-creator of Dąbrowski's Legions.",
                "Heliodor Święcicki, founder and first rector of the University of Poznań.",
                "The composers Feliks Nowowiejski, author of the melody of the “Rota”, and Tadeusz Szeligowski.",
                "The crypt also holds the heart of Gen. Jan Henryk Dąbrowski and the remains of Gen. Ignacy Prądzyński. In the south aisle of the church lies Karol Marcinkowski, a physician and social activist.",
            ]),
            ("Good to know", [
                "In 1997 a new part of the crypt was opened by the south aisle of the church.",
                "The crypt can be visited only after arranging a visit with the parish by phone. It is closed during Masses and ceremonies.",
            ]),
        ],
        hours=[("Crypt", "by arrangement by phone"), ("During Mass", "closed")],
        tickets=[("Visit", "by arrangement with the parish")],
    ),
    "okraglak": dict(
        name="Okrąglak",
        img_alt="The Okrąglak department store on ul. Mielżyńskiego",
        short="A cylindrical department store of 1954, a symbol of Poznań modernism.",
        badge="Free",
        status=None,
        lead="The Okrąglak department store, designed by Prof. Marek Leykam, is a symbol of Poznań modernism. It was opened on 29 January 1954 at the corner of ul. 27 Grudnia and ul. Mielżyńskiego, on the site of the pre-war Sugar Industry Bank.",
        sections=[
            ("What to see", [
                "A cylinder-shaped building, recognisable from afar.",
                "Inside, the centre of the building is taken by a cylindrical space open to the full height, with three flights of winding stairs leading to every floor.",
            ]),
            ("Good to know", [
                "Right next to it are the MoJA Jewellery Museum and the Teatr Polski.",
            ]),
        ],
        hours=[("Building from outside", "visible around the clock")],
        tickets=[("Viewing the building", "free")],
    ),
    "stadion": dict(
        name="Enea Stadium and the Lech Museum",
        img_alt="A steam locomotive in front of the city stadium in Poznań",
        short="A tour of the Euro 2012 stadium: the dressing room, the tunnel, the dugout and the club museum.",
        badge="Mon–Sat",
        status=None,
        lead="The City Stadium on ul. Bułgarska is the home of Lech Poznań. The rebuilt venue opened on 20 September 2010, and in 2012 it hosted three group-stage matches of Euro 2012. According to Wikipedia it holds 43,269 spectators (after an enlargement in 2012).",
        sections=[
            ("The tour", [
                "The stadium can be visited only with a guide; independent entry is not possible. The tour lasts about an hour, for groups of up to 35 people, in Polish or English. It includes the visitors' dressing room (the route does not lead to the home dressing room), the tunnel through which the players walk out onto the pitch, the dugouts and the multimedia Lech Poznań Museum.",
                "The times in the table are a pattern. The timetable for the whole week appears on the ticket website at the weekend before, because it depends on events at the stadium, so some days have no tours: in the week of 19–25 October 2026 there were none on Wednesday, Thursday and Sunday, and on Monday and Friday they ran at 14:00 and 16:00. Check the current calendar before your visit in the “Calendar of Tours with the Museum” on bilety.lechpoznan.pl.",
            ]),
            ("How to get in", [
                "The tour starts from the Stacja Kolejorz shop (Mon–Fri 10:00–19:00, Saturday 10:00–15:00). You can buy a ticket online (no need to print it; just give the guide the number) or from the guide on the spot, but there are no reservations and tickets may run out. A ticket for a given day can be used on another date after a message to wycieczki@lechpoznan.pl.",
                "Car park A1 for visitors is on ul. Ptasia, opposite the Mercedes showroom, next to the white tent.",
                "The stadium is adapted for wheelchair users. You can enter with a pram, but the website advises leaving it in the car or at the Stacja Kolejorz shop.",
            ]),
            ("Good to know", [
                "The reduced ticket applies to children and young people up to the age of 18, people in education up to the age of 26, seniors over 65 and people with disabilities (their carers enter free). Children up to the age of 4 enter free.",
                "Families get a discount on the final price, calculated in the transaction summary: 10% for 2 standard tickets and 1 reduced, 15% for 2 standard and 2 reduced, 20% for 2 standard and 3 or more reduced.",
                "Season-ticket holders in the Lechici programme get the tour ticket 50% cheaper (once a season, from their own account). On presenting the ticket, a 20% discount applies on the same day in the MasterLech restaurant.",
                "The helpline for individual tours (tel. 660 423 851) is open Monday to Friday 11:00–16:00, excluding holidays, days off and match days. Groups and other questions: wycieczki@lechpoznan.pl.",
                "There are also other tours: for organised groups (Monday–Friday, from PLN 20 per person plus PLN 90 per group for the guide), a pre-match tour (it starts 2.5 hours before a league match, and the price depends on the match and includes a match ticket and parking) and an exclusive tour with lunch at MasterLech (voucher PLN 200, reduced PLN 150, date agreed 10–14 days ahead, not at weekends, on match days or on holidays).",
            ]),
        ],
        hours=[("May–Sep, Mon–Fri", "12:00, 14:00, 16:00, 17:30"), ("Oct–Apr, Mon–Fri", "12:00, 14:00, 16:00"),
               ("Saturday (all year)", "10:00, 11:30, 12:45, 14:00")],
        tickets=[("Standard", "PLN 35"), ("Reduced", "PLN 25"), ("Children under 4", "free")],
    ),
    "linie-turystyczne": dict(
        name="Historic Trams and Buses (Tourist Lines)",
        img_alt="A historic Konstal 105N tram on tourist line 0",
        short="A ride on a historic tram or the “Ogórek” bus. They run in season, at weekends and on public holidays.",
        badge="Seasonal",
        status="The 2026 season ended on the weekend of 26–27 September (MPK still announced occasional special runs). The lines return in summer; the 2027 season timetable will be announced by MPK Poznań.",
        lead="In the summer season historic MPK trams and buses go out onto the streets of Poznań. The tram tourist line 0 has run since 1999, and the bus line since 2005.",
        sections=[
            ("Lines in the 2026 season", [
                "Tram 0 (Sundays and selected public holidays): historic cars between the University Library and the stop 27 Grudnia-Teatr Polski. Departures at 12:30, 13:30, 14:30, 16:00 and 17:00.",
                "Tram 20 (Saturdays): the same route, run by faster historic trams, at the same times.",
                "Bus 100 (weekends and public holidays): from Poznań Główny station to the New Zoo, every 40 minutes between 9:40 and 17:40.",
                "Bus 102 (Saturdays): from Poznań Główny station to the Museum of Armoured Weapons, departures at 10:00 and 12:00.",
                "On selected days the historic lines H (tram) and A (bus) also run. MPK announces the dates separately.",
            ]),
            ("Tickets", [
                "Tickets are sold by the conductor on the vehicle. You can pay in cash or by card.",
            ]),
        ],
        address="stop Biblioteka Uniwersytecka (ul. Ratajczaka: 61-815) / Poznań Główny station, 61-896 Poznań",
        hours=[("Season", "summer, weekends and public holidays"), ("Timetable", "at mpk.poznan.pl")],
        tickets=[("Single", "PLN 7, reduced PLN 5"), ("Day ticket", "PLN 12, reduced PLN 9")],
    ),
    "park-wilsona": dict(
        name="Wilson Park",
        img_alt="The Wilson Monument and flowers in Wilson Park",
        short="The former first botanical garden of Poznań, with the Wilson Monument, a concert shell and the Palm House.",
        badge="Free",
        status=None,
        lead="Wilson Park in Łazarz began as Poznań's first botanical garden. It was founded in 1902 and completed in 1904 to a design by Hermann Kube. It covers 7.2 hectares.",
        sections=[
            ("History", [
                "As early as 1834 the City Beautification Society set up a tree nursery here. The botanical garden operated until 1925.",
                "In 1951–1990 the park bore the name of Marcin Kasprzak. In 1990 it returned to the name of the US president Woodrow Wilson, who helped Poland regain independence in 1918.",
                "In 1931 the Wilson Monument was unveiled here, carved by Gutzon Borglum, the creator of the sculptures on Mount Rushmore.",
            ]),
            ("What to see", [
                "A concrete concert shell from 1936.",
                "The sculpture “Perseus and Andromeda” of 1891, moved to the park in 1956.",
                "The Poznań Palm House, currently closed for rebuilding.",
            ]),
        ],
        hours=[("Park", "daily 5:00–22:00")],
        tickets=[("Admission", "free")],
    ),
    "legi-debinskie": dict(
        name="Łęgi Dębińskie (John Paul II Park)",
        img_alt="The Pyra Monument in John Paul II Park",
        short="Poznań's third-largest park, with the Potato (Pyra) Monument and the site of the papal Mass of 1983.",
        badge="Free",
        status=None,
        lead="John Paul II Park, known as Łęgi Dębińskie, is the third-largest park in Poznań, after the Citadel and Millennium Park. It covers a little over 18.5 hectares.",
        sections=[
            ("History", [
                "The name commemorates John Paul II's visit to Poznań. On 20 June 1983 the Pope celebrated Mass here for about a million of the faithful. It was the largest gathering in the city's history, commemorated by the Papal Cross on ul. Ojca Mariana Żelazka.",
            ]),
            ("What to see", [
                "The Pyra Monument: a five-tonne erratic boulder in the shape of a potato, brought from near Stęszew and unveiled in September 2007 during the Pyrlandia Days.",
                "Wide meadows, paths with benches, an outdoor gym, street workout equipment and a fitness trail.",
            ]),
            ("For families", [
                "Two playgrounds, including an inclusive carousel for children with mobility disabilities, and a dog run.",
                "Getting there by bus 176 (stop Żelazka n/ż) or 603 (stop Droga Dębińska), according to the ZTM timetable of 10 October 2026. The poznan.pl website also mentions trams 2, 9, 18 and 19, but does not name a stop, so check the route in the timetable.",
            ]),
        ],
        hours=[("Park", "open to everyone")],
        tickets=[("Admission", "free")],
    ),
    "morasko": dict(
        name="Morasko Meteorite Nature Reserve",
        img_alt="Forest in the Morasko Meteorite reserve",
        short="Craters left by a meteorite shower about 5,000 years ago and Morasko Hill, Poznań's highest elevation.",
        badge="Free",
        status=None,
        lead="The Morasko Meteorite nature reserve, established in 1976, lies on the northern edge of Poznań, by the border with Suchy Las. It protects craters that, according to most researchers, were formed by the fall of iron meteorites about 5,000 years ago, and a fragment of oak-hornbeam forest.",
        sections=[
            ("Craters and meteorites", [
                "There are six craters in the reserve. The largest is about 90 metres across and 11.5 metres deep, and some of them are filled with water.",
                "The first meteorite was found here in 1914. More are found to this day. In 2012 a meteorite of about 261 kg was dug up, the largest known in Poland.",
                "Poznań is one of the few cities in the world that have meteorite craters within their boundaries.",
            ]),
            ("Nature", [
                "Most of the reserve is covered by grąd, that is, oak-hornbeam forest. In spring martagon lily, asarabacca and lily of the valley, among others, bloom here.",
                "In the water-filled craters amphibians gather in spring, including newts and the yellow-bellied toad. Among birds, the black woodpecker and the raven live here.",
                "In the reserve stands Morasko Hill, the highest elevation in Poznań, and the small lake Zimna Woda.",
            ]),
            ("Good to know", [
                "A tourist trail and an educational path with boards, prepared by the Astronomical Observatory of AMU and the Salamandra Society, lead through the reserve.",
                "In the reserve you may walk only along marked trails. You must not pick plants or search for meteorites.",
                "Bring comfortable shoes: this is a walk along forest paths, with no park infrastructure.",
            ]),
        ],
        address="Morasko, northern border of Poznań 61-680",
        hours=[("Reserve", "accessible, only along marked trails")],
        tickets=[("Admission", "free")],
    ),
    "rusalka": dict(
        name="Lake Rusałka",
        img_alt="Lake Rusałka in Poznań",
        short="A forest lake with a beach and a guarded bathing area in the west of the city.",
        badge="Free",
        status=None,
        lead="Rusałka is a lake of 36.7 hectares in the Golęcin green wedge, in the western part of Poznań. In summer a sandy beach with a municipal bathing area operates here.",
        sections=[
            ("The bathing area", [
                "The bathing area has 96 metres of shoreline. In the season it is guarded by lifeguards.",
                "There are two zones: one for non-swimmers, up to 1.2 metres deep (red buoys), and one for swimmers, up to 4 metres (yellow buoys).",
                "In 2026 the bathing season lasted from 20 June to 6 September.",
            ]),
            ("What else is by the lake", [
                "A playground, an outdoor gym, beach volleyball and boules courts, a cycle path, the Frajda amusement park and food outlets.",
                "At the bathing area there is an amphibious beach wheelchair for people with disabilities. Ask the lifeguards about availability.",
            ]),
        ],
        hours=[("Area around the lake", "open around the clock"), ("Guarded bathing area", "in the summer season")],
        tickets=[("Admission", "free")],
    ),
}
