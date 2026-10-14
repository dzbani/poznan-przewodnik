# -*- coding: utf-8 -*-
"""Angielskie tłumaczenia, partia 13 (14.10.2026): ostatnie pomniki i fontanny. Zasady: data_en.py."""

FREE = [("Admission", "free")]
OUTSIDE = [("Access", "around the clock, from outside")]

EN_BATCH13 = {
    "pomnik-zygi-latarnika": dict(
        name="Zyga the Lamplighter Monument",
        img_alt="A sculpture of a lamplighter by a historic gas lamp on ul. Grobla",
        short="A bronze lamplighter by a real gas lamp, next to the former gasworks on ul. Grobla.",
        badge="Free",
        status=None,
        lead="Zyga, in Poznań dialect short for Zygmunt, is a fictional lamplighter. His bronze figure stands on the square by ul. Grobla, next to the Old Gasworks.",
        sections=[
            ("About the monument", [
                "The monument was unveiled on 29 May 2003. It came out of the “Let's Save the Lamps” campaign run by “Gazeta Wyborcza” and the gasworks, which was meant to save the historic gas lamps of Poznań.",
                "The sculptor is Robert Sobociński. Part of the composition is an original, restored gas lamp moved from ul. Słowackiego in Jeżyce.",
            ]),
        ],
        address="ul. Grobla (the square by the Old Gasworks), 61-858 Poznań",
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-mickiewicza": dict(
        name="Adam Mickiewicz Monument",
        img_alt="The Adam Mickiewicz Monument on Plac Mickiewicza",
        short="A monument of 1960 by the Poznań Crosses. The first monument to the poet on Polish lands stood in Poznań in 1859.",
        badge="Free",
        status=None,
        lead="The present monument to Adam Mickiewicz, by Bazyli Wojtowicz, was unveiled in 1960 on Plac Mickiewicza. It is a four-metre figure on a two-metre plinth.",
        sections=[
            ("The first Mickiewicz monument", [
                "After the poet's death in 1855 the people of Poznań collected money for a monument and ordered it from Władysław Oleszczyński in Paris. The Prussian authorities long refused to agree to the location, and permission was given only at the end of 1858.",
                "The monument was unveiled on 7 May 1859 in the garden by St Martin's Church. It was the first monument to Mickiewicz on Polish lands. In 1904 it was replaced by a bronze cast, and in 1939 the Germans destroyed both monuments.",
                "The site of the first monument by St Martin's Church is today marked by a plaque.",
            ]),
            ("Good to know", [
                "On the same square stands the Poznań June 1956 Monument, and next to it stretches Mickiewicz Park in front of the Grand Theatre.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "fontanna-lwow": dict(
        name="Lion Fountain",
        img_alt="A fountain supported by eight lions in the courtyard of the Imperial Castle",
        short="A fountain modelled on the Court of the Lions in the Alhambra, hidden in the courtyard of the Imperial Castle.",
        badge="Free",
        status=None,
        lead="The Lion Fountain stands in the Rose Courtyard of the Imperial Castle. Both the courtyard and the fountain are modelled on the famous Court of the Lions in the Alhambra palace in Granada.",
        sections=[
            ("About the fountain", [
                "It was created together with the castle, designed by Franz Schwechten and completed around 1910.",
                "It has two stone basins: water flows from the upper to the lower one, which is supported by eight figures of lions. In the Alhambra there are twelve lions.",
                "After the war the place was neglected, and there were even garages for buses here. Only revitalisation restored its former look.",
            ]),
            ("Good to know", [
                "Next to it stand Magdalena Abakanowicz's sculpture “5 Figures” and the Katyn Monument in the Castle Garden.",
            ]),
        ],
        address="Rose Courtyard of the Imperial Castle (from ul. Fredry / Aleje Niepodległości), 61-809 Poznań",
        hours=[("Access", "castle courtyard, hours not given in the source")],
        tickets=FREE,
    ),
    "pomnik-katynski": dict(
        name="Monument to the Victims of Katyn and Siberia",
        img_alt="The Katyn Monument in the Castle Garden",
        short="The Katyn Monument by Robert Sobociński, 1999, in the Castle Garden.",
        badge="Free",
        status=None,
        lead="The Monument to the Victims of Katyn and Siberia, called the Katyn Monument, stands in the Castle Garden by the Imperial Castle, where ul. Fredry meets Aleje Niepodległości. It was unveiled in 1999.",
        sections=[
            ("About the monument", [
                "The author is the Poznań sculptor Robert Sobociński.",
                "The monument commemorates officers of the Polish Army and policemen murdered in 1940 in Katyn, Kharkiv and Mednoye, as well as victims of deportations to Siberia.",
            ]),
            ("Good to know", [
                "The monument stands in the garden of the Imperial Castle. You can read more about the garden on the Castle Garden page.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-panstwa-podziemnego": dict(
        name="Monument to the Polish Underground State",
        img_alt="The Monument to the Polish Underground State with eagle silhouettes",
        short="A modern monument of 2007: symbolic ruins, a glass crypt and eagles taking flight.",
        badge="Free",
        status=None,
        lead="The Monument to the Polish Underground State and the Home Army stands behind the Grand Theatre, at the corner of Aleje Niepodległości and ul. Libelta, on the edge of Wieniawski Park.",
        sections=[
            ("About the monument", [
                "It was designed by Prof. Mariusz Kulpa of the Academy of Fine Arts in Gdańsk, winner of the competition. It was unveiled on 26 September 2007 in the presence of, among others, the last President of the Republic of Poland in exile, Ryszard Kaczorowski.",
                "It consists of six memorial pillars with plaques, a glazed crypt symbolising the descent into the underground, and the silhouettes of eagles rising above them. The rust-coloured sheet metal was brought from Finland.",
                "Cast-iron plaques commemorate Greater Poland people who died between 1 September 1939 and 3 July 1945.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-armii-poznan": dict(
        name="“Poznań” Army Monument",
        img_alt="The “Poznań” Army Monument: soaring blades facing slanted blocks",
        short="A monumental memorial of 1982: Polish “bayonets” facing the armoured blocks of the invader.",
        badge="Free",
        status=None,
        lead="The monument to the heroes of the “Poznań” Army of 1939 was unveiled on 1 September 1982, on the 43rd anniversary of the outbreak of the Second World War. It stands at the foot of St Adalbert Hill, on Aleje Niepodległości.",
        sections=[
            ("Symbolism", [
                "Five slender elements pointing upwards symbolise Polish bayonets resisting German armoured force, shown as four slanted grey blocks.",
                "The walls bear the names of battlefields and units of the “Poznań” Army and the names of several dozen of the fallen. In the middle is a carved Virtuti Militari cross.",
            ]),
            ("History", [
                "The design by Anna Rodzińska and the architect Józef Iwiański won a competition in 1978, but construction dragged on for years. The authorities proposed other locations and also criticised the design for the invader's blocks being too large. The monument was built only in 1982 and unveiled on 1 September.",
            ]),
        ],
        address="Aleje Niepodległości (at the foot of St Adalbert Hill), 61-747 Poznań",
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-powstancow": dict(
        name="Monument to the Greater Poland Insurgents",
        img_alt="The granite obelisk of the Monument to the Greater Poland Insurgents",
        short="A 17-metre obelisk of 1965, commemorating the victorious uprising of 1918–1919.",
        badge="Free",
        status=None,
        lead="The monument commemorates the Greater Poland Uprising, the only victorious Polish uprising, which lasted from 27 December 1918 to 16 February 1919. It stands where ul. Królowej Jadwigi meets ul. Wierzbięcice, on the edge of Drwęski Park.",
        sections=[
            ("About the monument", [
                "It was designed by Alfred Wiśniewski of the art school in Gdańsk. It was unveiled on 19 September 1965.",
                "The obelisk is 17 metres high and clad in grey granite. Its bas-reliefs show an eagle and scenes from the struggle for Polishness: the children's strike in Września, Drzymała's wagon, Marcin Kasprzak and the death of the first insurgent, Franciszek Ratajczak.",
                "Next to it stand figures of two insurgents: an officer with a sabre and a private with a rifle. In 1988 a parade ground was laid out around the monument.",
            ]),
            ("Good to know", [
                "The uprising broke out the day after Ignacy Jan Paderewski's speech in front of the Hotel Bazar. Its story is told by the Museum of the Greater Poland Uprising on the Old Market Square.",
                "It is about 300 metres from here to Stary Browar.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-15-pulku-ulanow": dict(
        name="Monument to the 15th Poznań Uhlan Regiment",
        img_alt="A monument of an uhlan fighting a dragon on ul. Ludgardy",
        short="An uhlan fighting a dragon on a tall column, at the foot of Przemysł Hill.",
        badge="Free",
        status=None,
        lead="The monument shows an uhlan fighting a dragon on a tall plinth. It stands on ul. Ludgardy, next to the Franciscan monastery, on the slope of Przemysł Hill.",
        sections=[
            ("History", [
                "It commemorates soldiers of the 15th Poznań Uhlan Regiment, which fought, among others, the Bolsheviks in 1920 and in September 1939 as part of the “Poznań” Army.",
                "The sculpture by Mieczysław Lubelski was unveiled in 1927. Before the war the dragon wore a cap with a red star on its head, a symbol of Bolshevism.",
                "The Germans destroyed the monument in 1939. The reconstruction was made by Józef Murlewski and Benedykt Kasznia, and it was unveiled again in 1982.",
            ]),
            ("Good to know", [
                "It is one of the main places for patriotic ceremonies in Poznań, among others during the Uhlan Days.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "fontanna-higiei": dict(
        name="Hygieia Fountain",
        img_alt="A fountain with a statue of the goddess Hygieia in front of the Raczyński Library",
        short="A statue of the goddess of health on Plac Wolności, a reminder of Poznań's first waterworks of 1840.",
        badge="Free",
        status=None,
        lead="The Hygieia Fountain stands on Plac Wolności in front of the Raczyński Library. Its history begins with the waterworks that were built in 1840, largely with money from Edward Raczyński.",
        sections=[
            ("History", [
                "After the waterworks were built, four wells were set up in the city. The most important was to be decorated with a figure of Hygieia, the Greek goddess of health. The plinth was designed by the Berlin architect Christian Gottlieb Cantian.",
                "The seated goddess in ancient dress has the features of Konstancja Raczyńska, the wife of the founder. Water flows from a lion's head in the plinth.",
                "The fountain was moved several times. It came to the front of the Raczyński Library in 1971. For the building of the underground car park it was taken down, and after renovation it returned to the square in 2009.",
            ]),
            ("What to see", [
                "A medallion with the likeness of Vincenz Priessnitz, a pioneer of hydrotherapy, with the inscription in Greek and Polish “Nothing is better than water”. The letter “s” is missing from the Polish inscription.",
            ]),
        ],
        address="Plac Wolności (in front of the Raczyński Library), 61-739 Poznań",
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "fontanna-z-delfinami": dict(
        name="Dolphin Fountain (Kronthal's Well)",
        img_alt="A boy on a dolphin, a detail of the fountain on Aleje Marcinkowskiego",
        short="A fountain of 1909 with copper boys on dolphins, on Aleje Marcinkowskiego.",
        badge="Free",
        status=None,
        lead="The Dolphin Fountain, also called Kronthal's Well or the Lederer Fountain, stands on Aleje Marcinkowskiego, near the junction with ul. 23 Lutego.",
        sections=[
            ("History", [
                "Earlier a municipal well funded by Edward Raczyński stood here. In 1909 it was replaced by a fountain by the Berlin sculptor Hugo Lederer. The design was personally approved by Emperor Wilhelm II.",
                "The donor was the merchant Gustaw Kronthal, hence one of the fountain's names. In 2006 it underwent a thorough renovation.",
            ]),
            ("What to see", [
                "A stone basin of shell limestone and copper sculptures of boys on dolphins at the ends of the balustrade.",
                "According to the journalist Adam Pleskaczyński the “dolphins” are in fact catfish, as the structure of their mouths is said to show.",
                "Right next to it stand the Karol Marcinkowski Monument and a sculpture of the Golem.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-marcinkowskiego": dict(
        name="Karol Marcinkowski Monument",
        img_alt="The Karol Marcinkowski Monument on Aleje Marcinkowskiego",
        short="A monument to the physician and social activist, creator of “organic work”, unveiled in 2005.",
        badge="Free",
        status=None,
        lead="The monument to Karol Marcinkowski, physician and social activist, stands where Aleje Marcinkowskiego meets ul. 23 Lutego. It was unveiled in 2005.",
        sections=[
            ("About the monument", [
                "It was designed by the Gdańsk sculptor Stanisław Radwański. Marcinkowski stands in a long coat of the period, with a cane in his hand, on a tall granite plinth.",
                "The inscription on the plinth reads: “Karol Marcinkowski – creator of organic work”.",
            ]),
            ("Good to know", [
                "Marcinkowski initiated the building of the Hotel Bazar, a centre of Polish life in 19th-century Poznań.",
                "Next to it are the Dolphin Fountain and the post office building. A second monument to Marcinkowski stands in front of the 1st Secondary School on ul. Bukowska.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-janickiego": dict(
        name="Klemens Janicki Monument",
        img_alt="A monument of the seated poet Klemens Janicki on a column",
        short="A Renaissance poet with a pen in his hand, on a column on ul. 23 Lutego, with the inscription “To forgotten poets”.",
        badge="Free",
        status=None,
        lead="The monument to Klemens Janicki, a Renaissance poet who wrote in Latin, stands where ul. 23 Lutego meets ul. Masztalarska, close to the Old Market Square. It was unveiled in December 2015.",
        sections=[
            ("About the monument", [
                "Janicki, born in 1516, studied at the Poznań Lubrański Academy, and his first works were written here.",
                "The poet sits on a chest, with a pen and a sheet of paper in his hands. The bronze figure stands on a 2.5-metre sandstone column, and the whole monument is about 4 metres high.",
                "The authors are Joanna Buczak and Dariusz Wieczerzak, whose design won a competition of the Society for the Care of Monuments. The plinth bears the inscription “To forgotten poets”.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-jana-pawla-ii": dict(
        name="John Paul II Monument",
        img_alt="The John Paul II Monument on Ostrów Tumski",
        short="A monument to the Pope of 2000 in front of the former cathedral parish house on Ostrów Tumski.",
        badge="Free",
        status=None,
        lead="The John Paul II Monument stands on Ostrów Tumski, in front of the former cathedral parish house, near the archcathedral. It was unveiled in 2000.",
        sections=[
            ("About the monument", [
                "It is the work of the sculptor Krystyna Fałyga-Solska.",
                "It commemorates, among other things, the Pope's meeting with the priests of the Poznań archdiocese in the cathedral in 1983, during his second pilgrimage to Poland.",
            ]),
            ("Good to know", [
                "The Pope celebrated Mass for about a million of the faithful on that occasion on Łęgi Dębińskie, today John Paul II Park.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-kochanowskiego": dict(
        name="Jan Kochanowski Monument",
        img_alt="The Jan Kochanowski obelisk with a medallion in front of the Lubrański Academy",
        short="An obelisk of 1885 with a medallion of the poet, in front of the Lubrański Academy on Ostrów Tumski.",
        badge="Free",
        status=None,
        lead="The Jan Kochanowski Monument has the form of an obelisk with a medallion. It stands on Ostrów Tumski, on the square in front of the Lubrański Academy.",
        sections=[
            ("History", [
                "The foundation stone was laid in 1884, on the 300th anniversary of the poet's death, and the monument was unveiled in 1885. The obelisk was designed by Antoni Krzyżanowski, and the medallion with the portrait was made by Wiktor Brodzki. The money was raised in a public collection.",
                "The Germans destroyed the monument in 1940. In 1984 it was recreated to a design by Jerzy Sobociński, and in 2002 it was moved to its present place.",
            ]),
            ("A curiosity", [
                "In 1564–1574 Kochanowski was provost of the Poznań cathedral chapter, which gave him a large income. According to Wikipedia he himself never stayed in Poznań.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-cegielskiego": dict(
        name="Hipolit Cegielski Monument",
        img_alt="The monument to Hipolit Cegielski leaning on a steam engine",
        short="An industrialist leaning on a steam engine, on Plac Wiosny Ludów. A monument of 2009.",
        badge="Free",
        status=None,
        lead="The monument to Hipolit Cegielski, industrialist and creator of Polish economic patriotism, stands at the corner of ul. Święty Marcin and ul. Podgórna, by Plac Wiosny Ludów.",
        sections=[
            ("About the monument", [
                "It was unveiled on 19 September 2009. It was designed by the Poznań sculptor Krzysztof Jakubik, and the donor was the Hipolit Cegielski Society.",
                "Cegielski stands leaning on a steam engine, a symbol of his works, from which the famous Cegielski Works (HCP) grew.",
                "The idea of commemorating Cegielski had already appeared in the interwar period, but the monument was unveiled only on 19 September 2009.",
            ]),
            ("Good to know", [
                "Cegielski's first works operated on nearby ul. Kozia, and later on ul. Strzelecka.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-paderewskiego": dict(
        name="Ignacy Jan Paderewski Monument",
        img_alt="A figure of Paderewski in front of the glass façade of the Academy of Music",
        short="A monument to the pianist and statesman in front of the Academy of Music named after him, unveiled in 2015.",
        badge="Free",
        status=None,
        lead="The figure of Ignacy Jan Paderewski stands in front of the building of the Academy of Music in Poznań, of which he is the patron. It was unveiled in 2015, on the 155th anniversary of Paderewski's birth.",
        sections=[
            ("About the monument", [
                "It was designed by the Poznań sculptor Rafał Nowak.",
                "The monument was financed by donations from private individuals and companies. In the same year the academy celebrated its 95th anniversary.",
            ]),
            ("Good to know", [
                "Paderewski was a pianist, composer and politician. His speech in front of the Hotel Bazar on 26 December 1918 preceded the outbreak of the Greater Poland Uprising.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-ratajskiego": dict(
        name="Cyryl Ratajski Monument",
        img_alt="A seated figure of Cyryl Ratajski in front of the Poznań Financial Centre",
        short="A monument of 2002 to the distinguished pre-war mayor of Poznań, on Plac Andersa.",
        badge="Free",
        status=None,
        lead="The monument to Cyryl Ratajski, the pre-war mayor of Poznań, stands on Plac Andersa in front of the Poznań Financial Centre, on the ul. Półwiejska side.",
        sections=[
            ("About the monument", [
                "It was unveiled on 23 April 2002 in the presence of Ratajski's granddaughter and three post-war mayors of the city. The author is the Warsaw sculptor Jan Kucz.",
                "The names of the sponsors were entered in a commemorative book, later handed to the city history museum.",
            ]),
            ("Good to know", [
                "It is a few steps from Stary Browar and the Półwiejska pedestrian street with the Old Marych Monument.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-kosciuszki": dict(
        name="Tadeusz Kościuszko Monument",
        img_alt="The Tadeusz Kościuszko Monument on the square by ul. Grunwaldzka",
        short="A monument cast from the bronze of the Imperial Castle bell, on a square by ul. Grunwaldzka and ul. Bukowska.",
        badge="Free",
        status=None,
        lead="The Tadeusz Kościuszko Monument stands on the square where ul. Grunwaldzka meets ul. Bukowska. It is a post-war reconstruction of the monument of 1930.",
        sections=[
            ("History", [
                "The monument was designed by Zofia Trzcińska-Kamińska for the General National Exhibition in 1929. After the exhibition the plaster statue was replaced by a bronze one, unveiled on 27 December 1930, on the anniversary of the outbreak of the Greater Poland Uprising.",
                "The Germans destroyed the monument during the war. The artist herself recreated it, and in 1967 it was set up in its present place.",
                "According to Wikipedia the cast used the bell from the clock tower of the Imperial Castle, which fell during the fighting in 1945.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "pomnik-komedy": dict(
        name="Krzysztof Komeda Monument",
        img_alt="A bronze figure of Krzysztof Komeda looking at film frames",
        short="The jazz composer with a tuning fork at his ear, in front of the Medical University he graduated from.",
        badge="Free",
        status=None,
        lead="The monument to Krzysztof Komeda-Trzciński, composer of jazz and film music, stands in front of the Congress and Teaching Centre of the Medical University. Komeda graduated from the Poznań medical university and was an ear, nose and throat specialist.",
        sections=[
            ("About the monument", [
                "It was unveiled on 19 November 2010, for the university's 90th anniversary. It was designed by Adam Dawczak-Dębicki.",
                "The bronze figure holds a tuning fork to his ear and looks “against the light” at glass film frames with stills from the films Komeda wrote music for.",
                "In 2012 vandals knocked over and broke the sculpture. After renovation it returned to its place in the same year.",
            ]),
        ],
        address="Medical University, ul. Przybyszewskiego 49 / ul. Bukowska, 60-355 Poznań",
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "wiedzma-z-chwaliszewa": dict(
        name="The Witch of Chwaliszewo",
        img_alt="",
        short="A mirror-finish steel sculpture in the Old Warta Riverbed Park, commemorating a woman burned at the stake in 1511.",
        badge="Free",
        status=None,
        lead="“The Witch of Chwaliszewo” is a monument to the first woman on Polish lands who, according to tradition, was accused of witchcraft and burned at the stake. It stands in the Old Warta Riverbed Park in Chwaliszewo.",
        sections=[
            ("History", [
                "According to tradition, in 1511 in Chwaliszewo, then a separate small town with breweries, a healer was accused of poisoning the water used for brewing beer and was burned at the stake.",
                "Whatever the extent to which the story is confirmed, it became a symbol of the persecution of women accused of witchcraft.",
            ]),
            ("About the sculpture", [
                "The sculpture of polished, acid-etched steel is about 166 cm tall, the average height of a woman in Poland. It shows the outline of a figure without facial features, and you can see yourself in its mirrored surface.",
                "The idea came from Ewa Łowżył, founder of the Witches' Choir, and the sculpture was designed by the Poznań artist Alicja Biała.",
            ]),
        ],
        hours=OUTSIDE,
        tickets=FREE,
    ),
    "fontanna-park-wilsona": dict(
        name="Fountain in Wilson Park",
        img_alt="A star-shaped fountain with eight arms in Wilson Park",
        short="A star-shaped fountain of 1929, built for the General National Exhibition.",
        badge="Free",
        status=None,
        lead="The fountain in Wilson Park stands in the central part of the park, between the concert shell, the sculpture “Perseus and Andromeda” and the Palm House.",
        sections=[
            ("History", [
                "It was built in 1929 and switched on during the General National Exhibition (PeWuKa), which showed the achievements of reborn Poland. It was designed by the architect Roger Sławski.",
            ]),
            ("What to see", [
                "The fountain has the shape of an eight-armed star, and water spurts from its centre. In the evening it is lit with coloured lights.",
            ]),
        ],
        hours=[("Park", "daily 5:00–22:00")],
        tickets=FREE,
    ),
    "studzienka-taschnera": dict(
        name="Taschner's Well",
        img_alt="The carved column of Taschner's Well in the courtyard on ul. Mostowa",
        short="A richly carved fountain of 1908, today in the garden of the Museum of World Cultures.",
        badge="Free",
        status=None,
        lead="Taschner's Well stands in the courtyard of the Museum of World Cultures at ul. Mostowa 7. It is one of the lesser-known but very original fountains.",
        sections=[
            ("History", [
                "It was unveiled in 1908 in the courtyard of today's City Hall on Kolegiacki Square. It was designed by the Berlin sculptor Ignatius Taschner.",
                "In 1965 the well was dismantled and put into storage at the Citadel. Thanks to a collection by the Society for the Care of Monuments it was restored and in 1992 set up in its present place.",
            ]),
            ("What to see", [
                "A column in an octagonal basin: at the bottom grotesque masks, above them children on dolphins, and at the top a boy hugging a large fish.",
                "Reliefs on the walls of the basin showing different ways of using water.",
            ]),
        ],
        address="ul. Mostowa 7 (courtyard of the Bamber Museum), 61-854 Poznań",
        hours=[("Access", "museum courtyard, hours not given in the source")],
        tickets=FREE,
    ),
    "lasek-katynski": dict(
        name="Katyn Grove (Lasek Katyński)",
        img_alt="",
        short="116 red oaks by Fort VII commemorate people from Greater Poland murdered by the NKVD in 1940.",
        badge="Free",
        status=None,
        lead="The Katyn Grove was created next to Fort VII, which houses the Museum of the Martyrdom of Greater Poland People. It symbolically recalls more than 22,000 Polish officers, policemen, scholars, clergy and other people murdered in 1940.",
        sections=[
            ("Oaks of Remembrance", [
                "116 red oaks were planted in the grove, one for each of the 116 people from Poznań and Greater Poland murdered in Katyn, Kharkiv and Mednoye. That is how many families of the “Katyń” Association in Poznań were waiting for their loved ones to be commemorated.",
                "The oaks were planted in 2020 at the request of the “Katyń” Association in Poznań, with city money. The trees stand in a chessboard layout that symbolises military order. In autumn the leaves of red oaks turn shades of red, brown and gold.",
            ]),
            ("Plaques", [
                "By the road to Fort VII stands an information board funded by the Poznań Branch of the Institute of National Remembrance.",
                "On 18 September 2026 granite slabs appeared next to the oaks, bearing the victim's first name and surname, date of birth and place of death, and where the documentation allowed also military rank. QR codes lead to the “Katyń 1940” service with biographies.",
            ]),
            ("Good to know", [
                "The grove lies right next to Fort VII, a former German camp that is today the Museum of the Martyrdom of Greater Poland People. The two places are easy to combine in one visit.",
            ]),
        ],
        address="ul. Polska (next to Fort VII), 60-595 Poznań",
        hours=[("Grounds", "open to everyone")],
        tickets=FREE,
    ),
}
