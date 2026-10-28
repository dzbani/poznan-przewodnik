# -*- coding: utf-8 -*-
"""Angielskie tłumaczenia, partia 5 (14.10.2026): atrakcje punktów widokowych. Zasady: data_en.py.
Etykiety see_also bez dopisku „(in Polish)”: build_en dodaje go sam, gdy cel nie ma angielskiej strony."""

EN_BATCH5 = {
    "taras-widokowy-collegium-altum": dict(
        name="Collegium Altum Viewing Terrace (UEP)",
        img_alt="The red Collegium Altum tower block of the University of Economics among autumn trees",
        short="A panorama of Poznań in all four directions from the 18th floor of the red tower block of the University of Economics.",
        badge="Daily 9–19",
        status=None,
        lead="The viewing terrace on the 18th floor of the Collegium Altum of the University of Economics shows Poznań in all four directions. After many years it was reopened to visitors on 16 June 2025.",
        sections=[
            ("About the place", [
                "The Collegium Altum is a red tower block with a façade of red metal panels and a steel structure. It is a distinctive element of the city's skyline. Construction began in 1976.",
                "The terrace is on the 18th floor, next to the lift hall. It operated until 2004, after which the floor was turned into computer laboratories and the terrace was closed to visitors for many years. The idea of reopening it came from the then president of SARP (the Association of Polish Architects), Piotr Kostka. The official opening took place on 11 June 2025, and the terrace opened to visitors on 16 June.",
            ]),
            ("On site", [
                "Binoculars are included in the price of the ticket. On the terrace there is the SkyCoffee café (coffee, tea, cold drinks, croissants and tarts), and on Wednesday, Thursday, Friday and Saturday evenings it also hosts SkyPong, which is ping pong with a bar menu.",
                "Children get platforms for looking at the panorama, plus rebuses and puzzles. For everyone there is a relaxation zone with sofas, a photo frame against the panorama, cards describing the places you can see and QR codes on the windows. The Fly Radar screen shows aircraft in real time, including those on approach to land at Ławica.",
            ]),
            ("What to see", [
                "From above you can see, among other things, the Old Market Square, Ostrów Tumski with the cathedral, the Royal Castle and the Imperial Castle, Plac Wolności, the Okrąglak, Stary Browar, the Grand Theatre, Poznań Główny station, the Poznań International Fair, the City Stadium, the Citadel and Lake Malta.",
                "The official list on the terrace's website covers more than 30 places, including the Warta, the Town Hall and Ławica Airport.",
            ]),
            ("Good to know", [
                "Individual visitors can use the terrace every day from 9:00 to 19:00, according to the “Basic information” and “Price list” pages. The FAQ tab on the same site is out of date and gives older hours (Mon–Fri 12:00–20:00, Sat–Sun 9:00–20:00), so it is worth phoning before your visit.",
                "Individual tickets are bought from ticket machines in the lift hall on the 18th floor (you can pay by card and contactless), and no reservation is needed. A ticket entitles you to one uninterrupted entry. Keep it until you leave and tap it on the reader.",
                "On weekdays between 9:00 and 12:00 everyone pays the reduced price. The reduced price also applies to, among others, children over 3 and young people with an ID card, people with disabilities (with one carer), pensioners and holders of the Large Family Card. On Tuesdays students of other universities pay PLN 10, and UEP students enter free of charge. According to the FAQ on the terrace's website, Poznań City Card holders also enter free of charge, but it is worth confirming this by phone.",
                "Organised groups (at least 10 people) book a visit online at least 3 days in advance. For every 10 people the group leader enters free of charge. A group visit lasts 45 minutes and takes place on weekdays 9:00–12:00. Guided tours are for groups only.",
                "The building has a ramp and a lift, and the whole terrace is accessible to wheelchair users. There is an intercom on the terrace for contacting staff, and an alarm system in the toilet for calling for help. The website does not say whether the toilet is adapted for wheelchair users.",
                "Dogs are not allowed, except marked assistance dogs. Children must be supervised by adults. Taking photographs is permitted, and commercial shoots require contacting the terrace staff beforehand (taras@ue.poznan.pl).",
                "UEP car park: ul. Towarowa 55. There are few spaces, and there is also a paid parking zone in the area. From September to June the car park is open on weekdays 16:00–24:00 and at weekends 6:00–24:00, and in July and August every day 6:00–24:00.",
            ]),
        ],
        hours=[("Daily", "9:00–19:00"), ("Groups (Mon–Fri)", "9:00–12:00, after online booking")],
        tickets=[("Standard", "PLN 20"), ("Reduced", "PLN 15"), ("Mon–Fri 9:00–12:00", "everyone pays the reduced price"),
                 ("Group of 10 or more (online only)", "PLN 15 per person"), ("Students (Tuesday)", "PLN 10")],
        see_also=["Viewpoints in Poznań: all towers and terraces", "Royal Castle and its viewing tower",
                  "Okrąglak, visible from the terrace"],
    ),
    "szachty": dict(
        name="Szachty",
        img_alt="The view from the top of the viewing tower over the ponds at Szachty",
        short="Ponds in former clay pits, a 25-metre viewing tower and a nature trail. Free entry.",
        badge="Free entry",
        status=None,
        lead="Szachty is the site of former clay pits, where a centre of the brick industry once operated. Today it is a place for walks, bike rides and watching wildlife.",
        sections=[
            ("What to see", [
                "A viewing tower 25 metres high, on the ul. Mieleszyńska side. After 120 steps you see a panorama of Poznań: the tower blocks, the stadium and the office buildings in the centre.",
                "Edy's Pond (Staw Edy) with viewpoints, and the Spreading Pond (Staw Rozlany) with a jetty from which you can see tern nesting platforms, ducks and swans.",
                "Kindler's House from about 1910, built of brick made here, at the entrance from ul. Leszczyńska.",
                "Educational boards about plants and animals along the paths.",
            ]),
            ("Good to know", [
                "There is a playground by the tower.",
                "By Edy's Pond you can use a campfire place free of charge after registering by email with the Municipal Greenery Authority.",
                "Getting there by bus to the stops Kowalewicka n/ż (lines 180, 610 and 702) or Glinianki n/ż (180, 250, 610, 616, 702, 703, 704 and 707), according to the ZTM timetable of 10 October 2026. Car parks are on ul. Mieleszyńska and ul. Witaszka.",
            ]),
        ],
        hours=[("Grounds and tower", "open to everyone")],
        tickets=[("Entry and viewing tower", "free")],
        see_also=["Viewpoints in Poznań: all towers and terraces"],
    ),
    "czmoniec-bobrowy-szlak": dict(
        name="Viewing Tower and Beaver Trail in Czmoniec",
        img_alt="The wooden viewing tower on the Beaver Trail in Czmoniec",
        short="A wooden viewing tower above the meadows and oxbow lakes of the Warta, and a short nature trail. No tickets, in Kórnik municipality.",
        badge="Free",
        status=None,
        lead="In Czmoniec, in Kórnik municipality, on the edge of wide meadows in the Warta valley, stands a wooden viewing tower. It stands on the Beaver Trail (Bobrowy Szlak), a nature trail through the oxbow lakes of the Warta.",
        sections=[
            ("What to see", [
                "A wooden viewing tower about 14 m high, opened in 2010. It was built on the initiative of the village head of Czmoniec, and the platform at the top holds up to 20 people at a time. From it you see meadows, oxbow lakes of the Warta and clumps of trees. Other sources give the height of the tower as 14–15 m.",
                "The Beaver Trail, a nature trail in the Warta valley, through meadows and oxbow lakes. You can reach it from the north, and the trail leads to the tower.",
            ]),
            ("Good to know", [
                "According to the Visit Poznań portal, you can reach the tower by car along ul. Malwowa (a dirt road). An unmarked car park is a few hundred metres from the tower. You can also walk along the Beaver Trail from the north.",
                "The area is open, with no ticket offices or set hours. Before you set out, check the current rules for access and parking, because access along the dirt road may be difficult. Information about the area is also on kornik.travel.",
                "The trip can be combined with a visit to Kórnik or Rogalin.",
            ]),
        ],
        address="Czmoniec, ul. Malwowa (tower west of the village), Kórnik municipality",
        hours=[("Tower and trail", "open area, no set hours")],
        tickets=[("Admission", "free")],
        getting=[("Car", "Along ul. Malwowa (a dirt road) to an unmarked car park a few hundred metres from the tower."),
                 ("Public transport", "Check the connection from Poznań in the route planner (link above).")],
        see_also=["Viewpoints in Poznań: all towers and terraces"],
    ),
}
