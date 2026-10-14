# -*- coding: utf-8 -*-
"""Angielska strona „About Poznań” (/en/about). Kolejność i liczba pozycji muszą być takie same jak w
data_guide (HISTORY, LEGENDS, DIALECT, CUISINE, CLIMATE); kontroluje to check_en.py.
Po zmianie polskiej strony: zaktualizuj ten plik i uruchom: python src/check_en.py --stamp-about"""

# Tokeny liczbowe PL -> EN, gdy zapis liczby różni się z natury („w latach 70.” XVI w. = „the 1570s”)
NUMBER_EXCEPTIONS = {"70": "1570"}

INTRO = "A short history, legends, words from the local dialect and tastes worth knowing before you arrive."

HISTORY = [
    ("9th century", "A stronghold is built on Ostrów Tumski, between the Warta and the Cybina."),
    ("10th century", "The stronghold is one of the main seats of Duke Mieszko I."),
    ("968", "The first bishopric on Polish lands is founded in Poznań."),
    ("11th century", "The cathedral holds the tombs of Poland's first rulers, including Bolesław the Brave. In 1038 the stronghold is destroyed by the invasion of the Czech duke Bretislav I."),
    ("1253", "Przemysł I grants Poznań a municipal charter. The Old Market Square is laid out on the left bank of the Warta."),
    ("16th century", "The city's golden age. In 1519 Bishop Jan Lubrański founds the Lubrański Academy, in 1550–1560 Giovanni Battista di Quadro gives the town hall its Renaissance look, and in the 1570s the Jesuits open a college, a secondary school with academic courses."),
    ("1793", "In the Second Partition of Poland, Poznań is annexed by Prussia."),
    ("1806", "In November Napoleon arrives in Poznań. For almost three weeks he lives in the former Jesuit College."),
    ("1815", "After the Congress of Vienna, Poznań becomes the seat of the authorities of the Grand Duchy of Posen, part of Prussia. The governor is Prince Antoni Radziwiłł."),
    ("1828–1842", "The Prussians build a mighty fort in Winiary, today's Citadel. Poznań turns into a fortress city surrounded by fortifications."),
    ("1848", "During the Spring of Nations, a National Committee is formed in Poznań on 20 March, and an uprising against the Prussians breaks out in Greater Poland. In May the insurgents surrender."),
    ("1905–1910", "The Imperial Castle is built for Emperor Wilhelm II, the heart of the new Imperial Quarter."),
    ("1918–1919", "On 26 December 1918 Ignacy Paderewski speaks to the people of Poznań in front of the Hotel Bazar, and the next day the Greater Poland Uprising breaks out. The victorious uprising returns Poznań to Poland. In 1919 the University of Poznań is founded, today Adam Mickiewicz University."),
    ("1921", "The first Poznań Fair is held. From 1925 it is an international fair, and Poznań becomes a city of trade fairs."),
    ("1929", "From 16 May to 30 September the General National Exhibition (PeWuKa) takes place, a showcase of the achievements of ten years of independent Poland."),
    ("1932", "Marian Rejewski, a mathematics graduate of the University of Poznań, breaks the cipher of the German Enigma. He is joined by Jerzy Różycki and Henryk Zygalski, also graduates of the Poznań university."),
    ("1939–1945", "On 10 September 1939 the Germans occupy Poznań and incorporate it into the Reich as the capital of the Warthegau. Part of the inhabitants are expelled. After heavy fighting the city is captured on 23 February 1945, about 55% destroyed."),
    ("1956", "On 28 June workers go out onto the streets. The Poznań June is the first mass protest against communist rule in the People's Republic of Poland. On the 25th anniversary, 28 June 1981, the Poznań June Monument, the Poznań Crosses, was unveiled."),
    ("1983 and 1997", "Pope John Paul II visits Poznań. On 20 June 1983 he beatifies Urszula Ledóchowska during Mass on Łęgi Dębińskie, and on 3 June 1997 he meets young people on Plac Mickiewicza."),
    ("2012", "Three group-stage matches of Euro 2012 are played at the rebuilt City Stadium."),
]

LEGENDS = [
    ("The founding of Poznań", "After a long separation, the three brothers Lech, Czech and Rus met where the Cybina flows into the Warta. They recognised one another at once and cried: “Poznaję!” (“I recognise you!”). To commemorate the meeting they built a stronghold on this spot and called it Poznań."),
    ("The Poznań goats", "When the clockmaker Bartłomiej of Gubin was about to show the councillors the new town hall clock, a feast was being prepared in the kitchen for the voivode. A kitchen boy burned the roast venison, so he stole two billy goats from a meadow to roast them. The animals escaped to the tower and began to butt each other above the clock. The amused voivode forgave the boy and ordered a mechanism with goats to be added to the clock."),
    ("The town hall bugle call", "Przemek, the son of a guard in the town hall tower, saved a wounded raven. The bird turned out to be the king of ravens and gave him a silver trumpet for a time of danger. When an enemy surrounded the city, Przemek sounded the trumpet to the four corners of the world. Thousands of birds flew in and drove the invaders away. In memory of this it was decided that the town trumpeter would play the bugle call from the tower every day to the four corners of the world."),
    ("The Proserpina fountain", "In the 17th century a rich widow, Petronela, married a young stonemason's journeyman. When he fell in love with another woman, she accused him of attempting to poison her. The court punished him only with a fine and ordered him to build a fountain in front of the town hall at his own expense. This is how the fountain with the abduction of Proserpina by Pluto came about."),
    ("The sword of St Peter", "The Roman sword in the Archdiocesan Museum is said to be the one with which St Peter cut off the ear of the high priest's servant in the Garden of Gethsemane. According to Jan Długosz, the pope gave it to Poznań's first bishop, Jordan."),
    ("The St Martin's croissants", "According to a popular legend, in November 1891 the parish priest of St Martin's, Fr Jan Lewicki, appealed to the faithful to help the poor, following the example of their patron. The confectioner Józef Melzer persuaded his employer to bake croissants. Wealthy Poznań residents bought them, and the poor received them for free. The croissant's shape is supposed to resemble a horseshoe lost by the saint's horse. In reality croissants were baked in Poznań for 11 November earlier: the oldest known advertisement dates from 1860."),
    ("Duchess Ludgarda", "Ludgarda, the first wife of Przemysł II, did not give him an heir. According to legend, in 1283 she died because of this in a bathhouse at the foot of Poznań castle. Historical sources, however, say that she died in Gniezno and was buried there."),
]

DIALECT = [
    ("pyra", "potato"), ("bimba", "tram"), ("szneka", "a snail-shaped yeast pastry"),
    ("tej", "you (a call: “Tej, chodź tu!”, “Hey, come here!”)"), ("laczki", "backless house slippers"),
    ("tytka", "a paper bag"), ("ancug", "suit"), ("sznytka", "a slice of bread, a sandwich"),
    ("gzik", "quark with cream and chives or onion"), ("galoty", "underpants"), ("szczun", "boy"),
    ("korbol", "pumpkin"), ("ryczka", "a low stool"), ("wuchta", "a lot"), ("fyrtel", "district, neighbourhood"),
    ("jupka", "jacket"), ("bana", "train"), ("ino", "only"), ("szagą", "diagonally, at an angle"),
    ("rajzefiber", "excitement or anxiety before a journey"), ("mantel", "coat"), ("antrejka", "hallway"),
    ("kejter", "dog, mongrel"), ("ćmik", "cigarette"), ("glanc", "shine (hence “szneka z glancem”)"),
]

CUISINE = [
    ("Rogal świętomarciński (St Martin's croissant)", "A semi-French pastry filled with white poppy seed. Since 2008 it has had the EU Protected Geographical Indication. Most are eaten on 11 November."),
    ("Pyry z gzikiem (potatoes with quark)", "Potatoes with quark mixed with cream, chives or onion."),
    ("Szare kluski (grey dumplings)", "Dumplings made of raw potatoes, served with cabbage, bigos or fried onion."),
    ("Czernina (duck blood soup)", "A soup made from duck blood (formerly goose blood)."),
    ("Plyndze (potato pancakes)", "Potato pancakes (in the dialect plyndz, plendz or plindz)."),
    ("Pieczona kaczka z jabłkami (roast duck with apples)", "Served with red cabbage and pyzy (potato dumplings)."),
    ("Szneka z glancem (iced snail pastry)", "A snail-shaped yeast pastry covered with icing."),
    ("Ślepe ryby (“blind fish” soup)", "A thick potato soup. There are no fish in it, hence the name."),
]

CLIMATE = [
    ("−0.4 °C", "average temperature in January"), ("19.5 °C", "average temperature in July"),
    ("539 mm", "annual precipitation"), ("July", "the rainiest month (84 mm)"),
]

LABELS = dict(
    kicker="Get to know the city", title="About Poznań",
    h_history="History in brief", h_legends="Legends", h_dialect="Do you speak Poznań?",
    dialect_intro="Poznań people still use words from the local dialect. These are the ones you will hear most often:",
    h_food="What to eat in Poznań", h_climate="Climate",
    food_p1="Only bakeries from the Greater Poland region that hold a certificate from the Chapter of the Poznań Traditional St Martin's Croissant may use the name “rogal świętomarciński”. You can learn the history of the croissant at the {rogal}, and of the potato at the {pyry}.",
    food_p2="The restaurant Muga has held a Michelin star for the fourth year in a row. The Michelin Guide 2026 lists 25 venues from Poznań and the surrounding area.",
    climate_p="Summers are warm but there can be downpours. In winter the temperature often drops below zero. Late spring and early autumn are the most pleasant seasons for sightseeing.",
    climate_src="Averages for 1991–2020, Poznań-Ławica station. Calculations based on {imgw_data}. Forecast: {imgw}.",
)
