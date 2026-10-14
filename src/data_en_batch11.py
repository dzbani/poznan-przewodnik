# -*- coding: utf-8 -*-
"""Angielskie tłumaczenia, partia 11 (14.10.2026): parki, jeziora i bulwary. Zasady: data_en.py."""

PARK_HOURS = [("Park", "open to everyone")]
FREE = [("Admission", "free")]

EN_BATCH11 = {
    "bulwary-warta": dict(
        name="Warta Boulevards (Wartostrada)",
        img_alt="The city beach on the Warta at Szeląg",
        short="The Wartostrada: 13.6 km of pedestrian and cycle paths along the river, with city beaches in summer.",
        badge="Free",
        status=None,
        lead="The Wartostrada is a system of pedestrian and cycle paths along the Warta. Two routes on both banks of the river are 13.6 km long in total and run from the Przemysł I Bridge in the south to the Lech Bridge in the north.",
        sections=[
            ("About the route", [
                "Construction of the Wartostrada began in 2011, and the route was extended in 2015–2020 and 2020–2022. The paths are intended for pedestrians and cyclists of every level.",
                "The route links, among others, the Queen Jadwiga Bridge, the St Roch Bridge and the Bolesław the Brave Bridge. It passes the Gate of Poznań and runs through the parks Szeląg Park and Park nad Wartą.",
                "Along the route are viewpoints, bicycle repair stations and Bike&Ride car parks.",
            ]),
            ("City beaches", [
                "In summer city beaches operate on the Warta, among others in Chwaliszewo and at Szeląg. The city announces the season dates and attractions every year.",
            ]),
            ("Good to know", [
                "From the Wartostrada it is easy to walk to Ostrów Tumski, the Gate of Poznań and Śródka, so a walk by the river can be combined with visiting them.",
            ]),
        ],
        address="Wartostrada (city-centre section), 61-124 Poznań",
        hours=[("Paths", "open around the clock"), ("City beaches", "in the summer season")],
        tickets=FREE,
    ),
    "park-solacki": dict(
        name="Sołacki Park",
        img_alt="A pond in Sołacki Park",
        short="A hundred-year-old landscape park with ponds on the Bogdanka, among the villas of Sołacz.",
        badge="Free",
        status=None,
        lead="Sołacki Park was laid out in 1908–1911 to a design by Hermann Kube, then director of the Poznań Municipal Gardens. It covers almost 15 hectares and was created on the marshy land of the Bogdanka valley.",
        sections=[
            ("About the park", [
                "It is a park in the English style. About 3,000 trees and 12,000 shrubs grow here, alongside native species also exotic ones, among them the Canadian hemlock, the bald cypress and the Douglas fir.",
                "The dammed Bogdanka forms the Sołacz Ponds with irregular shores.",
                "Since 1983 the park has been entered in the register of monuments together with the villa district of Sołacz.",
            ]),
            ("What to see", [
                "Ponds, little bridges and a waterfall on the Bogdanka.",
                "A green tram shelter on ul. Małopolska from 1913, when the tram reached Sołacz.",
                "The sculpture “Two Women” by Sylwester Ambroziak of 2008.",
                "A building of 1912 in which, after renovation in 2022, a hotel with the Port Sołacz restaurant operates.",
            ]),
            ("Good to know", [
                "The park has playgrounds and walking paths. You may meet, among others, mandarin ducks and woodpeckers.",
            ]),
        ],
        address="Sołacki Park, 60-631 Poznań",
        hours=PARK_HOURS,
        tickets=FREE,
    ),
    "jezioro-kierskie": dict(
        name="Lake Kierskie",
        img_alt="Lake Kierskie",
        short="Poznań's largest lake: sailing, bathing areas and 12 km of shore for walks.",
        badge="Free",
        status=None,
        lead="Lake Kierskie is an elongated channel stretching from Krzyżowniki to Kiekrz, about 4.5 km long and several hundred metres wide. It covers 285 hectares and is 37.6 metres deep.",
        sections=[
            ("What to do here", [
                "Sail. The Greater Poland Yacht Club was founded in Kiekrz in 1933, and today a dozen or so sailing clubs have marinas here.",
                "Walk and cycle along more than 12 km of shoreline.",
                "In summer swim at the guarded bathing areas in Krzyżowniki and Kiekrz. In winter ice boats sail on the lake.",
                "Fish, for example for vendace, eel, zander and pike. The lake is open to anglers all year round.",
            ]),
            ("Good to know", [
                "Not far away, in Krzyżowniki, is the Nuclear Shelter and Poster Gallery.",
                "Sources give different dimensions of the lake. The city portal writes of a length of 4.8 km and a width of 2.1 km, while Wikipedia gives a length of about 4.3–4.5 km and a width of up to 0.8 km. A width of 2.1 km does not fit an area of 285 ha, so in this description we have used the Wikipedia data.",
            ]),
        ],
        address="Lake Kierskie, Poznań-Kiekrz 60-480",
        hours=[("Area around the lake", "open around the clock"), ("Guarded bathing areas", "in the summer season")],
        tickets=FREE,
    ),
    "jezioro-strzeszynskie": dict(
        name="Lake Strzeszyńskie",
        img_alt="Lake Strzeszyńskie among forests",
        short="The cleanest of Poznań's large lakes, among forests, with a bathing area and a campsite.",
        badge="Free",
        status=None,
        lead="Lake Strzeszyńskie is a natural reservoir among forests on the north-western edge of Poznań, about 10 km from the centre. It is the cleanest of the large lakes in the city.",
        sections=[
            ("About the lake", [
                "It covers 34.9 hectares and is 17.8 metres deep. It is surrounded by deciduous and pine forests.",
                "Fish living here include vendace, whitefish, eel, pike and perch.",
            ]),
            ("Good to know", [
                "By the lake there is a centre with a bathing area, accommodation, a year-round restaurant, cabins and a campsite.",
            ]),
        ],
        address="Lake Strzeszyńskie, Poznań-Strzeszyn 60-479",
        hours=[("Area around the lake", "open around the clock")],
        tickets=FREE,
    ),
    "park-chopina": dict(
        name="Chopin Park",
        img_alt="Chopin Park in Poznań",
        short="An intimate park behind the Jesuit College, with a bust of Chopin, two steps from the Old Market Square.",
        badge="Free",
        status=None,
        lead="Chopin Park lies on ul. Podgórna, behind the former Jesuit College, right next to the Old Market Square. It covers 1.8 hectares.",
        sections=[
            ("History", [
                "At the beginning of the 18th century the Jesuits laid out a garden here, which also served as a botanical garden for nature lessons.",
                "From 1815 the garden belonged to the residence of the governor Antoni Radziwiłł, who turned it into a park. In 1961 the park was opened to the public and named after Chopin.",
            ]),
            ("What to see", [
                "A marble bust of Fryderyk Chopin by Marcin Rożek.",
                "Old trees, among them a small-leaved lime with a girth of about 3 metres, a sycamore, an oak and a plane tree.",
            ]),
            ("Good to know", [
                "Getting there by tram (according to the ZTM timetable of 10 October 2026): 3, 4, 5, 8, 13, 15, 16 and 17 to the stop Wrocławska, or 2, 9 and 19 to the stop Pl. Wiosny Ludów.",
            ]),
        ],
        address="ul. Podgórna, 61-829 Poznań",
        hours=PARK_HOURS,
        tickets=FREE,
    ),
    "park-marcinkowskiego": dict(
        name="Marcinkowski Park",
        img_alt="Marcinkowski Park in Poznań",
        short="A park of 1906 by the station, with a bust of Słowacki that survived the war buried in the ground.",
        badge="Free",
        status=None,
        lead="Marcinkowski Park began to be built in 1905 on former fortress land and was opened in 1906. It covers 9.5 hectares and lies not far from Poznań Główny station.",
        sections=[
            ("History", [
                "At first the park was named after Friedrich Schiller. It received its present name, in honour of the physician and social activist Karol Marcinkowski, in 1919.",
                "After the Second World War the park was enlarged with the grounds of former cemeteries. On the cemetery of the parish of St Martin, closed in 1959, the grave of Karol Marcinkowski lay until 1923.",
            ]),
            ("What to see", [
                "A bust of Juliusz Słowacki of white marble by Władysław Marcinkowski, unveiled in 1923. During the occupation it was buried by workers of the municipal gardens, and it returned to its place in 1950.",
                "A sculpture of a peacock with a girl by Anna Krzymańska above the pond.",
                "A Turkish hazel with a trunk girth of 200 cm, protected as a natural monument.",
            ]),
            ("For families", [
                "Two playgrounds, a sports pitch, an outdoor gym and a skate park.",
                "Getting there by trams 5, 6, 12 and 17 to the stop Poznań Główny.",
            ]),
        ],
        address="al. Niepodległości / ul. Stanisława Matyi, 61-874 Poznań",
        hours=PARK_HOURS,
        tickets=FREE,
    ),
    "park-tysiaclecia": dict(
        name="Millennium Park",
        img_alt="Memorial boulders in Millennium Park in autumn",
        short="A forest park in Nowe Miasto with 28 memorial boulders, an amphitheatre and a children's traffic town.",
        badge="Free",
        status=None,
        lead="Millennium Park covers 26.3 hectares. It was laid out on forest land, on the site of a former military firing range and an old cemetery on ul. Świętojańska.",
        sections=[
            ("History", [
                "The first plans for the park appeared in 1928, and in 1931 a competition was announced for developing the so-called Cybina Green Wedge. Work began only after the city had been rebuilt from wartime destruction.",
                "The park was opened on 16 July 1966 as the first of five newly designed city parks. Finishing work lasted until 1970.",
            ]),
            ("What to see", [
                "28 monuments made of erratic boulders placed along the paths.",
                "A small amphitheatre and wide walking avenues with bays in which benches stand.",
            ]),
            ("For families", [
                "In the northern part of the park there is a traffic town where children learn the rules as pedestrians and cyclists. It is also useful before a cycling-licence exam.",
                "A large playground, trampolines, an outdoor gym and a dog-walking area.",
            ]),
        ],
        address="ul. Termalna / ul. Komandoria, 61-028 Poznań",
        hours=PARK_HOURS,
        tickets=FREE,
    ),
    "park-rataje": dict(
        name="Rataje Park and the Railway Open-Air Museum",
        img_alt="A steam locomotive in the Środa County Railway open-air museum in Rataje Park",
        short="Poznań's second-largest park: a garden of the senses and a railway open-air museum with a locomotive that puffs steam at noon.",
        badge="Free",
        status=None,
        lead="Rataje Park, opened in 2018 on the border of Rataje and Żegrze, is the second-largest park in Poznań, after the Citadel. It is divided into nine themed zones: recreational, educational and historical.",
        sections=[
            ("Środa County Railway open-air museum", [
                "In the central part of the park, not far from the church of the Visitation of Our Lady, stand two locomotives: the narrow-gauge Dn2t “Baziel” and the Tkt48-130 with a dining car of the former WARS company. Nearby are a stretch of track, level-crossing gates, a mechanical semaphore, a water crane, a buffer stop and a historic station clock.",
                "Every day at 12:00, and in summer also at 14:00 and 16:00, the narrow-gauge locomotive lets off steam and whistles.",
                "The open-air museum commemorates the railway built from 1898. The narrow-gauge main line ran from Kobylepole to Środa Wielkopolska and Zaniemyśl and carried mainly sugar beet. After it was taken over by PKP in 1949 the railway was gradually closed down. To this day only the Środa Wielkopolska – Zaniemyśl section still runs.",
            ]),
            ("What else to see", [
                "A garden of the senses, that is, themed gardens appealing to sight, hearing, smell, taste and touch, with a sensory trail.",
                "An avenue of memorial trees, walking and cycling paths and a picnic clearing.",
            ]),
            ("For families", [
                "A playground with a large colourful toy train next to the open-air museum, a parkour track, a pumptrack, an outdoor gym, a sports pitch and a dog run.",
            ]),
        ],
        address="os. Rzeczypospolitej / os. Polan, 61-239 Poznań",
        hours=[("Park", "open to everyone"), ("Locomotive show", "daily 12:00; in summer also 14:00 and 16:00")],
        tickets=FREE,
    ),
    "stare-koryto-warty": dict(
        name="Old Warta Riverbed Park",
        img_alt="The amphitheatre in the Old Warta Riverbed Park",
        short="A park on the filled-in bed of the Warta, between the Old Town and Ostrów Tumski. An amphitheatre, a fountain and a playground.",
        badge="Free",
        status=None,
        lead="The Old Warta Riverbed Park in Chwaliszewo was created on the site of the old river bed, filled in during the 1960s. It opened in 2016. It covers almost 3 hectares.",
        sections=[
            ("The idea for the park", [
                "The design by the 1050 studio refers to the meanders of the river and the vegetation of river valleys. Trees were deliberately not planted along the axis of the old bed, so that you can see where the Warta flowed. Trees grow only at the edges.",
                "More than 100 trees, 16,000 shrubs and about 10,000 perennials and ornamental grasses were planted, chosen so that the park also looks good in winter.",
            ]),
            ("What to see", [
                "An amphitheatre, a square with a fountain and walking paths.",
                "The pavilion of the former “New Gasworks” on ul. Ewangelicka. Since 2018 it has housed “Pawilon”, a cultural venue run by the Arsenał City Gallery.",
                "A plaque of 2021 commemorating Poznań recipients of the Order of the Smile.",
            ]),
            ("For families", [
                "A playground of 2017 with a separate “Labyrinth” zone for children aged 1–3. The equipment is also adapted for children with disabilities. There are trampolines, a climbing wall, a zip line and musical platforms.",
                "There are two automatic toilets in the park.",
            ]),
        ],
        address="pl. Międzymoście / ul. Ewangelicka, 61-111 Poznań",
        hours=PARK_HOURS,
        tickets=FREE,
    ),
    "park-szelagowski": dict(
        name="Szeląg Park",
        img_alt="The ruins of old steps in Szeląg Park",
        short="A historic park on the Warta escarpment, next to the Citadel: views over the river valley, ruined steps and a chalybeate spring.",
        badge="Free",
        status=None,
        lead="Szeląg Park lies on the escarpment of the Warta valley, at Szeląg, and adjoins Cytadela Park. From its slope views stretch over the river valley.",
        sections=[
            ("History", [
                "The name comes from the merchant family Szyling. The best known of them, Mayor Mikołaj Szyling, founded a gunpowder factory here in the 16th century. From the beginning of the 19th century the area was a favourite destination for outings of Poznań people.",
                "In 1922 the land was bought by the Fowler Brotherhood (the Marksmen's Guild), which laid out the Shooting Garden with the largest covered shooting range in Poland and restaurant terraces for several thousand guests.",
                "In June 1945 the first post-war Wianki (midsummer wreath festival) took place here. After the war the area fell into decline, and in 2009 the park was tidied up.",
            ]),
            ("What to see", [
                "The ruins of monumental steps leading towards the river.",
                "A small spring of chalybeate water, which stains the ground rust-coloured.",
                "Magnificent black poplars with a girth of up to six metres, a maple-leaved plane tree and an avenue of horse chestnuts.",
                "The Fowler Brotherhood monument of 2017 and the Veteran's House, an example of late modernism.",
            ]),
            ("Good to know", [
                "The Wartostrada runs along the park, so it is easy to combine a walk with the Citadel and the Warta boulevards.",
            ]),
        ],
        address="ul. Szelągowska, 61-626 Poznań",
        hours=PARK_HOURS,
        tickets=FREE,
    ),
    "park-kasprowicza": dict(
        name="Kasprowicz Park",
        img_alt="",
        short="A park in Łazarz by the Arena hall, with an obelisk to the poet, playgrounds and chess tables.",
        badge="Free",
        status=None,
        lead="Kasprowicz Park lies in Łazarz, between ul. Reymonta, ul. Wyspiańskiego, ul. Jarochowskiego and ul. Chociszewskiego. It covers 9.3 hectares and was laid out in 1936–1939.",
        sections=[
            ("History", [
                "During the occupation the Germans devastated the park, because they planned to move the Poznań zoo here. In the early 1960s the area was tidied up and new trees and shrubs were planted.",
            ]),
            ("What to see", [
                "The Arena sports and entertainment hall, standing on the park's grounds.",
                "A stone obelisk with a bas-relief of the face of Jan Kasprowicz by Edward Haupt of 1967, at the corner of ul. Jarochowskiego and ul. Niegolewskich.",
            ]),
            ("For families", [
                "Two playgrounds, an outdoor gym, street workout equipment, tables for chess and draughts, a ping-pong table and a dog run.",
            ]),
        ],
        address="ul. Reymonta / ul. Jarochowskiego, 60-791 Poznań",
        hours=PARK_HOURS,
        tickets=FREE,
    ),
    "park-nad-warta": dict(
        name="Park nad Wartą (Park by the Warta)",
        img_alt="An avenue in Park nad Wartą in winter",
        short="One of Poznań's largest parks: 17 hectares of riverside woodland, a pond and canoe marinas.",
        badge="Free",
        status=None,
        lead="Park nad Wartą covers a little over 17 hectares. It stretches along the eastern bank of the Warta, from ul. Krzywoustego to ul. Hetmańska, next to the Piastowskie housing estate in Rataje.",
        sections=[
            ("What to see", [
                "The park has a natural, woodland character: horse chestnuts, willows and poplars grow here. In the central part there is a pond.",
                "On the river stand the canoe marinas of rowing and canoeing clubs, among them KS Posnania, Polonia, Warta, Energetyk and AZS.",
            ]),
            ("Sport and family", [
                "Three playgrounds, a pitch for football and beach volleyball, a skate park, street workout equipment, tennis courts and a bowling alley.",
            ]),
        ],
        address="along the Warta, by the Piastowskie estate, 61-155 Poznań",
        hours=PARK_HOURS,
        tickets=FREE,
    ),
    "park-wieniawskiego": dict(
        name="Wieniawski Park",
        img_alt="Lawns and paths of Wieniawski Park",
        short="A historic park next to the Grand Theatre, formerly called “Teatralka”, with a sledging hill.",
        badge="Free",
        status=None,
        lead="Wieniawski Park, in the interwar period called “Teatralka”, lies in the centre of Poznań, in the northern part of the Imperial District, right next to the Grand Theatre. It was laid out in 1907–1910.",
        sections=[
            ("What to see", [
                "A sledging hill in the southern part of the park, on whose top elements of former small architecture have survived.",
                "A catering pavilion traditionally called Pegasus's Stable, which refers to its neighbour the theatre.",
                "About 260 trees of 34 species. The most valuable are the Russian olive and the hackberry.",
                "In the western part of the park stands a disused, historic railway signal box.",
            ]),
            ("Neighbourhood", [
                "From ul. Fredry the park borders the former Mortgage Bank and the villa of Adolf Landsberg, and on the south the monument to the Polish Underground State.",
            ]),
        ],
        address="ul. Wieniawskiego / ul. Fredry, 61-712 Poznań",
        hours=PARK_HOURS,
        tickets=FREE,
    ),
    "park-moniuszki": dict(
        name="Moniuszko Park",
        img_alt="Trees in Moniuszko Park",
        short="One of Poznań's oldest city parks, intimate, right in the centre, with a bust of the composer.",
        badge="Free",
        status=None,
        lead="Moniuszko Park is a historic park of 2.2 hectares in the centre of Poznań, between ul. Libelta, ul. Noskowskiego, ul. Chopina and Aleje Niepodległości.",
        sections=[
            ("History", [
                "It was created around 1870 as a private garden. In 1906 the city bought the land and turned the garden into a public park.",
                "It was named after Goethe, in 1919 it became the City Park, and since 1921 it has been the Stanisław Moniuszko Park. The old stand of trees suffered badly in 1945 during the fighting for the nearby Citadel.",
            ]),
            ("What to see", [
                "A bust of Moniuszko of 1924, funded by the choirs of the Greater Poland Union of Singing Circles. Destroyed during the occupation, it was recreated after the war by Edward Haupt.",
                "Hornbeams and oaks. It is a quiet place to rest in the city centre, a few minutes from the Imperial Castle.",
            ]),
        ],
        address="ul. Libelta / ul. Chopina, 61-706 Poznań",
        hours=PARK_HOURS,
        tickets=FREE,
    ),
    "ogrod-zamkowy": dict(
        name="Castle Garden (Ogród Zamkowy)",
        img_alt="The Katyn Monument in the Castle Garden",
        short="The former private garden of Emperor Wilhelm II by the Imperial Castle, with the Katyn Monument and a sculpture by Abakanowicz.",
        badge="Free",
        status=None,
        lead="The Castle Garden of the Victims of Katyn and Siberia is the former private garden of Emperor Wilhelm II's residence, by the north wall of the Imperial Castle, at the corner of Aleje Niepodległości and ul. Fredry.",
        sections=[
            ("History", [
                "Part of the garden was the Rose Garden with the Lion Fountain. The main part served as an intimate “salon” with a semicircular square and an avenue of limes. The garden was a symmetrical reflection of Mickiewicz Park on the other side of Aleje Niepodległości.",
                "In 2001–2004 the garden was renovated and the wrought-iron fences were recreated. It has borne its present name since 2014.",
            ]),
            ("What to see", [
                "The Monument to the Victims of Katyn and Siberia (the Katyn Monument) by Robert Sobociński.",
                "Magdalena Abakanowicz's sculpture “5 Figures” in the Rose Courtyard.",
                "A bench with the archaeologist Józef Kostrzewski.",
                "A maple-leaved plane tree with a girth of 411 cm, protected since 2024.",
            ]),
        ],
        hours=[("Garden", "fenced area; opening hours are not given in the source")],
        tickets=FREE,
    ),
}
