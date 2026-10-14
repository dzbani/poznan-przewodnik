# -*- coding: utf-8 -*-
"""Angielskie tłumaczenia, partia 12 (14.10.2026): ostatnie muzea, las i pomniki Starego Rynku. Zasady: data_en.py."""

FREE = [("Admission", "free")]
OUTSIDE = [("Access", "around the clock, from outside")]

EN_BATCH12 = {
    "lasek-marcelinski": dict(
        name="Lasek Marceliński (Marcelin Wood)",
        img_alt="Lasek Marceliński in autumn",
        short="More than 200 hectares of city forest in western Poznań: a nature trail, a sledging hill and cycle routes.",
        badge="Free",
        status=None,
        lead="Lasek Marceliński, called Uroczysko Marcelin by naturalists, is a city forest in the western part of Poznań, between the Bajkowe estate and the cemetery in Junikowo. It was created after the Second World War on former farmland and covers more than 200 hectares.",
        sections=[
            ("What to do", [
                "Walk and cycle: the forest has a dozen or so kilometres of roads and dirt paths. A bridle path also runs through it.",
                "Follow the nature and forest trail with two loops, 2.9 and 2.1 km long. It starts by the Marcelin forester's lodge and the seat of the Municipal Greenery Authority on ul. Strzegomska.",
                "Climb the sledging and cycling hill, heaped up from former industrial waste. In winter children slide down it on sledges, in summer cyclists ride it.",
            ]),
            ("Good to know", [
                "By the clearing with the hill grows an imposing English elm, transplanted here in 2002 from the centre of Poznań.",
                "By the trail there is a pond in the forest with a clearing and benches. There are also playgrounds in the forest.",
                "The car park is on ul. Strzegomska. You can get here by bike along cycle routes, among others from the stadium side.",
            ]),
        ],
        hours=[("Forest", "open to everyone")],
        tickets=FREE,
    ),
    "muzeum-komunikacji-mpk": dict(
        name="MPK Urban Transport Museum",
        img_alt="The tram depot on ul. Głogowska",
        short="The history of Poznań's trams in the Głogowska depot. Currently closed.",
        badge="Closed",
        status="The Memory and Tradition Room of MPK Poznań is closed for technical reasons until further notice (announcement by MPK Poznań).",
        lead="The museum, officially called the Memory and Tradition Room of MPK Poznań, opened on 31 January 2007. It is housed in the oldest building of the depot on ul. Głogowska, a former transformer substation of 1928–1929.",
        sections=[
            ("What to see", [
                "Mementoes from the history of Poznań's public transport, among others from the building and opening of the Poznań Fast Tram.",
                "Archive recordings from local television.",
            ]),
            ("Good to know", [
                "When the museum is open, it is visited in groups of up to 20 people after booking by phone.",
                "Previous prices: standard PLN 10, children up to 16 PLN 7, family (up to 5 people) PLN 30.",
            ]),
        ],
        hours=[("Currently", "closed until further notice")],
        tickets=[("Currently", "no visits")],
    ),
    "muzeum-ump": dict(
        name="Poznań University of Medical Sciences Museum",
        img_alt="",
        short="The history of medicine and of the university in open exhibitions on the UMP campus. Free entry.",
        badge="Free entry",
        status=None,
        lead="The Karol Marcinkowski Museum of Poznań University of Medical Sciences shows its collections in open space, in the buildings of the university campus at the junction of ul. Przybyszewskiego and ul. Bukowska.",
        sections=[
            ("What to see", [
                "In the Centre for Medical Biology (1st floor, right-hand side): exhibits connected with dentistry, internal medicine, surgery, paediatrics, radiology, ophthalmology and laboratory diagnostics.",
                "In the Congress and Teaching Centre (level 1, by lecture rooms A and B, up the stairs from the main entrance): the history of the university, its patron Karol Marcinkowski, pharmacy, surgery and anaesthesiology.",
            ]),
            ("Good to know", [
                "Both exhibitions are free and accessible during the opening hours of the buildings.",
            ]),
        ],
        address="UMP campus, ul. Bukowska 70, 60-812 Poznań",
        hours=[("Exhibitions", "during the opening hours of the university buildings")],
        tickets=FREE,
    ),
    "muzeum-ziemi": dict(
        name="Earth Museum of Adam Mickiewicz University",
        img_alt="A fragment of the Morasko meteorite weighing 261.8 kg",
        short="Morasko meteorites, including a specimen weighing 261 kg, minerals and fossils. Free entry.",
        badge="Free entry",
        status=None,
        lead="The Earth Museum of the Faculty of Geographical and Geological Sciences of AMU collects minerals, rocks, fossils and Polish meteorites. The meteorite collection includes two large specimens of the Morasko meteorite (261 and 160 kg).",
        sections=[
            ("What to see", [
                "Two large fragments of the Morasko meteorite: one weighing 261 kg, found in 2012, and one weighing 160 kg.",
                "About one and a half thousand specimens of minerals, rocks and fossils from Poland and the world, including a collection of Lower Silesian agates.",
                "Replicas of skulls of early australopithecines, teeth of extinct fish and reptiles, and a lapidarium, that is, a rock garden.",
            ]),
            ("Good to know", [
                "Opening hours change every semester. The current calendar is on the museum's website, where you also book a visit.",
                "Up to 20 people can be in the museum at a time, so larger groups must split up. About 30 minutes is enough for a visit.",
            ]),
        ],
        hours=[("Hours", "variable, calendar at muzeumziemi.amu.edu.pl")],
        tickets=FREE,
    ),
    "izba-prl-w7": dict(
        name="PRL Room in the former Hall W7",
        img_alt="",
        short="A private collection of mementoes of communist Poland in a historic hall of the Cegielski works. Free entry.",
        badge="Free entry",
        status=None,
        lead="The PRL Room on ul. Hetmańska shows part of a collection of mementoes from the time of the Polish People's Republic, gathered by the collector and social activist Marcin Kentzer-Nowakowski. It is housed in the former Hall W7 of the HCP works.",
        sections=[
            ("What to see", [
                "Everyday objects, shop equipment, mementoes of the H. Cegielski works and of the Solidarity period, and Polish motoring of the era.",
            ]),
            ("About Hall W7", [
                "The hall was built during the First World War. Ambulance vehicles were made in it, and later armoured trains. After the Second World War, until the end of the Cold War, rifles and machine guns for the army were made here.",
            ]),
            ("Good to know", [
                "You must arrange the visit in advance with the keeper of the collection, by phone or through social media. He tells the story of the exhibits.",
            ]),
        ],
        hours=[("Visits", "by prior appointment")],
        tickets=FREE,
    ),
    "muzeum-kultury-cyfrowej": dict(
        name="Poznań Museum of Digital Culture",
        img_alt="",
        short="Commodore 64, Amiga and Atari to switch on and play. Currently closed because of a move.",
        badge="Closed",
        status="The museum is closed during the renovation of a new, larger seat (more than 200 m²). It will announce the reopening on social media.",
        lead="The Poznań Museum of Digital Culture combines the history of technology with play. On classic microcomputers you can start games and programs yourself.",
        sections=[
            ("What to see", [
                "Microcomputers such as the Commodore 64, the Amiga and the Atari.",
                "An exhibition on the demoscene, a phenomenon of the late 1980s.",
                "Old electronics: telephones, cameras and portable players, as well as computer components and data carriers.",
            ]),
        ],
        address="ul. Błękitna 1/7 (entrance from ul. Turkusowa), 60-656 Poznań",
        hours=[("Currently", "closed")],
        tickets=[("Currently", "no visits")],
    ),
    "mieszkanie-illakowiczowny": dict(
        name="Kazimiera Iłłakowiczówna Apartment-Studio",
        img_alt="Ul. Gajowa, where the poet's apartment is",
        short="The authentic apartment of the poet and secretary to Piłsudski. Visits by registration.",
        badge="Registration",
        status=None,
        lead="The museum was arranged in the apartment of the poet Kazimiera Iłłakowiczówna on the first anniversary of her death, 16 February 1984. It is a branch of the Raczyński Library and has kept its authentic furnishings, books and personal belongings.",
        sections=[
            ("What to see", [
                "The poet's Oxford language certificate, her debut volume “Ikarowe loty” of 1911 and medals for her service as a nurse in the First World War.",
                "Documents from her work in Polish ministries, decorations, correspondence with well-known people, a death mask made by Józefa Petruka and a portrait painted by Jadwiga Łubowska.",
            ]),
            ("How to visit", [
                "Individual visitors can come on the second and last Wednesday of the month at 12:30, after registering in advance.",
                "Organised groups are received after booking. There are also themed tours, among others on the poet's political views and her journeys as secretary to Marshal Piłsudski.",
            ]),
        ],
        hours=[("Individual visitors", "2nd and last Wednesday of the month, 12:30"), ("Groups", "by reservation")],
        tickets=[("Registration and information", "tel. 61 855 12 44")],
    ),
    "pomnik-koziolkow": dict(
        name="Goats Monument (Pomnik Koziołków)",
        img_alt="A sculpture of two goats butting heads on Kolegiacki Square",
        short="Two bronze goats butting heads on Kolegiacki Square. You can sit on them for a photo.",
        badge="Free",
        status=None,
        lead="The monument shows two goats butting heads, referring to one of the symbols of Poznań: the goats that come out on the town hall tower at noon.",
        sections=[
            ("About the monument", [
                "It was designed by Robert Sobociński and was set up in 2002 on Kolegiacki Square, not far from the main entrance of the City Hall in the former Jesuit College.",
                "In 2019, for the duration of the square's reconstruction, the sculpture was moved to Chopin Park. It returned to its place when the work was finished.",
            ]),
            ("Good to know", [
                "The sculpture stands low, and you can sit on the goats' backs, so it is a popular place for souvenir photos.",
                "The real goats butt heads every day at 12:00 on the town hall tower, a few minutes' walk from here.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "fontanna-prozerpiny": dict(
        name="Proserpina Fountain",
        img_alt="The Baroque Proserpina Fountain in front of the town hall in the evening",
        short="The only surviving historic fountain of the Old Market Square, from 1766, in front of the town hall.",
        badge="Free",
        status=None,
        lead="The Proserpina Fountain stands in front of the town hall on the Old Market Square. It is a Baroque work by Augustyn Schöps, completed in 1766, and the only one of the square's four historic fountains to survive to this day.",
        sections=[
            ("History", [
                "Wells on the square were already mentioned in 1568, when wooden figures of a lion and a deer were ordered for them. In 1615 they were replaced by statues of Apollo, Jupiter, Mars and Neptune.",
                "In 1758 the councillors commissioned a new fountain from Augustyn Schöps. The work lasted until 1766.",
                "In 2010 Lech Poznań fans celebrating the Polish championship damaged the fountain. It was repaired after a month, with money collected by the fans themselves.",
            ]),
            ("What to see", [
                "The scene of the abduction of Proserpina by Pluto, ruler of the underworld, carved in sandstone.",
                "Bas-reliefs of the four elements on the walls of the basin (fire, water, air and earth) and the coat of arms of Poznań.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "fontanna-apolla": dict(
        name="Apollo Fountain",
        img_alt="The Apollo Fountain on the Old Market Square, with townhouses and the town hall in the background",
        short="A modern fountain of 2002 with a statue of Apollo, in the south-east corner of the square.",
        badge="Free",
        status=None,
        lead="The Apollo Fountain stands in the south-east corner of the Old Market Square, where ul. Wodna and ul. Świętosławska meet it. It was unveiled in 2002, and its author is Marian Konieczny.",
        sections=[
            ("History", [
                "As early as the 17th century one of the square's four fountains stood here, from which residents drew water until the end of the 19th century. The modern fountain refers to this tradition.",
                "The statue aroused emotions from the start: the proportions of the figure and its nudity were criticised, and the conservator of monuments also raised objections.",
            ]),
            ("Good to know", [
                "It is one of the square's four fountains. The others are Proserpina, Neptune and Mars, so it is easy to see them all on one walk.",
            ]),
        ],
        address="Stary Rynek (corner of ul. Wodna and ul. Świętosławska), 61-772 Poznań",
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "fontanna-neptuna": dict(
        name="Neptune Fountain",
        img_alt="The statue of Neptune on a fountain on the Old Market Square",
        short="A fountain of 2004 on the site of the old fish market, where ul. Paderewskiego and ul. Szkolna meet the square.",
        badge="Free",
        status=None,
        lead="The Neptune Fountain stands in the south-western part of the Old Market Square, where ul. Paderewskiego and ul. Szkolna meet it. It was designed by Marcin Sobczak and unveiled in 2004.",
        sections=[
            ("History of the place", [
                "For centuries a fish market operated here. Poznań was closely tied to the Warta and its branches: many residents worked as fishermen, raftsmen and sand-diggers. Street names such as Wodna, Mostowa, Grobla and Rybaki recall this.",
                "The fountain stands on the site of an old well of the 17th century. Like the Apollo and Mars fountains, it is a modern reference to the old wells of the square.",
            ]),
        ],
        address="Stary Rynek (where ul. Paderewskiego meets the square), 61-772 Poznań",
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "fontanna-marsa": dict(
        name="Mars Fountain",
        img_alt="The Mars Fountain on the Old Market Square, with the town hall in the background",
        short="The youngest of the four fountains of the Old Market Square, unveiled in 2005.",
        badge="Free",
        status=None,
        lead="The Mars Fountain stands in the north-western part of the Old Market Square. It was unveiled in 2005. The sculpture is by Rafał Nowak, and the donors were Wanda and Romuald Szperliński.",
        sections=[
            ("History", [
                "In the 17th century one of the square's fountains stood here, which supplied residents with water until the end of the 19th century. The new fountain restored this historic place.",
                "The fountain is named after Mars, the Roman god of war, and is one of the four fountains standing on the square.",
            ]),
        ],
        address="Stary Rynek (north-western part), 61-772 Poznań",
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-starego-marycha": dict(
        name="Old Marych Monument",
        img_alt="A sculpture of Old Marych with a bicycle on ul. Półwiejska",
        short="A bronze Poznań man with a bicycle, hero of radio talks in dialect. A popular photo spot.",
        badge="Free",
        status=None,
        lead="Old Marych (Stary Marych) is a fictional character of a typical Poznań man speaking in dialect, the hero of the radio programmes “Blubry Starego Marycha” by Juliusz Kubel. The monument stands at the northern end of the pedestrian zone on ul. Półwiejska.",
        sections=[
            ("About the monument", [
                "The idea came from the Poznań office of “Gazeta Wyborcza”, which in 1998 announced a poll “A Poznań man on the plinth!”. Readers chose Old Marych, the only fictional character among the candidates.",
                "The sculpture was designed by Robert Sobociński. Marych has the face of Marian Pogasz, who read the programmes on the radio. He wheels a bicycle with a traditional briefcase hung over the handlebars.",
                "The monument was unveiled on 21 March 2001, on the 90th anniversary of the birth of Stanisław Strugarek, a populariser of the Poznań dialect.",
            ]),
            ("Good to know", [
                "You can read about the Poznań dialect and its most important words on the About Poznań page.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-kryptologow": dict(
        name="Cryptologists' Monument (Enigma Breakers)",
        img_alt="The three-sided cryptologists' monument in front of the Imperial Castle",
        short="An obelisk of strings of digits in front of the Imperial Castle, devoted to the three Poznań mathematicians who broke Enigma.",
        badge="Free",
        status=None,
        lead="The monument in front of the main entrance to the Imperial Castle commemorates Marian Rejewski, Jerzy Różycki and Henryk Zygalski, mathematicians connected with the University of Poznań who broke the cipher of the German Enigma machine.",
        sections=[
            ("About the monument", [
                "It was unveiled in 2007. It was designed by Grażyna Bielska-Kozakiewicz and Mariusz Kozakiewicz.",
                "It has the form of a metal prism with a triangular base. The walls are covered with strings of digits into which the names of the cryptologists are inscribed, as a tribute to mathematics and human thought.",
                "At the bottom are inscriptions in Polish and English with biographies of the three mathematicians.",
            ]),
            ("Good to know", [
                "Before the war rooms of the university were housed in the castle. A few steps away is the Enigma Cipher Centre with a multimedia exhibition on this history.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "studzienka-bamberki": dict(
        name="Bamberka Well",
        img_alt="The well with the figure of the Bamberka by the town hall",
        short="A bronze figure of a girl in Bamber costume by the west wall of the town hall, from 1915.",
        badge="Free",
        status=None,
        lead="The Bamberka Well stands by the west wall of the town hall. Its decoration is a bronze figure of a woman in Bamber costume, with a yoke and jugs. It commemorates the Bambers, settlers from around Bamberg who in the 18th century settled the villages near Poznań.",
        sections=[
            ("History", [
                "The well was unveiled in 1915. It was funded by the Poznań merchant and wine dealer Leopold Goldenring. The plinth was designed by the builder Stahl, and the figure was sculpted by Józef Wackerle.",
                "The sculptor's model was Jadwiga Gadziemska, an employee of Goldenring's wine shop, who herself did not come from a Bamber family.",
                "The basin once served as a drinking trough for horses, and residents also used it. After the war the well was moved several times, and in 1977 it returned to the Old Market Square.",
            ]),
            ("Good to know", [
                "Kazimiera Iłłakowiczówna wrote a poem about her, “Bambereczka”.",
                "You can learn more about the Bambers at the Museum of the Poznań Bambers on ul. Mostowa.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
}
