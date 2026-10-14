# -*- coding: utf-8 -*-
"""Angielska strona „Practical information” (/en/practical). Odpowiada wybranym sekcjom polskiej strony
Informacje praktyczne (build.build_info): przyjazd, bagaż, nocleg, komunikacja, karta turystyczna, informacja
turystyczna, lokalne smaki, numery alarmowe, zdrowie, taksówki, parkowanie, rowery, przewodnicy, pogoda.
Pominięte (na razie): lista muzeów wg dni, lista miejsc bezpłatnych, toalety, dostępność.
Po zmianie polskiej strony: zaktualizuj ten plik i uruchom: python src/check_en.py --stamp-practical"""
from build import CONTACT_EMAIL


def body(checked):
    ext = lambda url, text: f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'
    return f"""
<header class="wrap page-head">
  <p class="kicker">Planning your visit</p>
  <h1>Practical information</h1>
  <p class="lead">How to get to Poznań and move around the city, where to find medical help, parking and more. Information checked {checked}.</p>
  <nav class="toc" aria-label="Contents">
    <a href="#arrival">Arriving</a><a href="#luggage">Luggage</a><a href="#stay">Where to stay</a><a href="#transport">Public transport</a><a href="#card">Tourist Card</a>
    <a href="#info">Tourist information</a><a href="#food">Local food</a><a href="#emergency">Emergency numbers</a><a href="#health">Health</a>
    <a href="#taxis">Taxis</a><a href="#parking">Parking</a><a href="#cycling">Cycling</a><a href="#guides">Guided tours</a><a href="#weather">Weather</a>
  </nav>
</header>

<div class="wrap prose">
<section id="arrival">
  <h2>Arriving</h2>
  <h3>Poznań-Ławica Airport</h3>
  <p>The airport is at ul. Bukowska 285. Buses <strong>148</strong> and <strong>159</strong> run between the terminal and the Poznań Główny railway station. Since 18 April 2026 they run alternately, so from the stops Poznań Główny, Rondo Kaponiera and Bałtyk and from the terminal they leave every 7–8 minutes at peak times, and every 10 minutes off-peak and at weekends. Line 177 runs every 30 minutes at peak times and every 40 minutes otherwise.</p>
  <p>You can buy a ticket with a payment card at the terminal on the bus. There is a tourist information point at the airport.</p>
  <p class="muted">Source (in Polish): {ext("https://www.ztm.poznan.pl/aktualnosci/komunikaty/linie-nr-148-159-oraz-177-zmiany-w-komunikacji-na-trasie-poznan-glowny-port-lotniczy-lawica-od-18-kwietnia/", "ZTM Poznań: lines 148, 159 and 177 from 18 April 2026")}</p>
  <h3>Poznań Główny railway station</h3>
  <p>The station building is connected to the Avenida shopping centre. Buses to the airport (148 and 159) leave from the Poznań Główny stop.</p>
</section>

<section id="luggage">
  <h2>Luggage storage</h2>
  <p>At Poznań Główny station (ul. Dworcowa 2) there are luggage lockers which, according to PKP, are available around the clock. The PKP website gives neither their location nor their prices, so check the daily rate on the spot at the lockers. There are also lockers at the {ext("https://dworzecautobusowy.poznan.pl/", "Poznań Główny bus station")}. Prices are set by the station regulations (new from 1 March 2026), which you will find on its website. We did not check the prices there.</p>
  <p>We could not confirm whether luggage storage operates at Ławica airport, so ask at the airport information desk. There are also private luggage-storage points in the city that you can book online. Check prices and addresses on their websites, because they change.</p>
  <p class="muted">Sources (in Polish): {ext("https://www.pkp.pl/pl/dworce/poznan-glowny-informacje-dla-podroznych", "PKP: Poznań Główny, passenger information")}, {ext("https://dworzecautobusowy.poznan.pl/", "Poznań Główny bus station")}.</p>
</section>

<section id="stay">
  <h2>Where to stay</h2>
  <p>Poznań is compact, and most attractions in this guide are in the centre or a few tram stops from it. Choosing a district therefore depends mainly on how long you are willing to commute and whether you arrive by train.</p>
  <ul>
    <li><strong>Old Town (Stare Miasto):</strong> closest to the Old Market Square, the Parish Church (Fara), the Croissant Museum and the Royal Castle. There are many restaurants and cafés around the square.</li>
    <li><strong>Around Poznań Główny station:</strong> convenient if you arrive by train or are going to the airport on buses 148 and 159. You can reach the Old Market Square by tram.</li>
    <li><strong>Jeżyce:</strong> a district of Art Nouveau townhouses, close to the Poznań International Fair. A good choice if you are going to a trade fair.</li>
    <li><strong>Łazarz and Wilda:</strong> residential districts south of the centre. From here you can get to the centre by public transport.</li>
  </ul>
  <p>Prices depend on the date, so we do not quote rates. On the days of major events at the Poznań International Fair (for example Pyrkon or Poznań Game Arena), and during fairs and the marathon, it is worth booking accommodation in advance. See the events calendar (in Polish) for dates: <a href="../kalendarz.html" hreflang="pl" lang="pl">Kalendarz wydarzeń</a>.</p>
  <p>You choose and book accommodation on booking sites or directly with the property. We do not recommend specific hotels.</p>
</section>

<section id="transport">
  <h2>Public transport</h2>
  <p>Trams and buses are run by the Public Transport Authority (ZTM). The fare list has applied since 1 September 2025. Time tickets are valid in all zones and allow changes between vehicles.</p>
  <div class="table-wrap"><table class="grid grid-fit">
    <thead><tr><th scope="col">Ticket</th><th scope="col">Standard</th><th scope="col">Reduced</th></tr></thead>
    <tbody>
      <tr><th scope="row">up to 15 minutes</th><td>PLN 5</td><td>PLN 2.50</td></tr>
      <tr><th scope="row">up to 45 minutes</th><td>PLN 7</td><td>PLN 3.50</td></tr>
      <tr><th scope="row">up to 90 minutes</th><td>PLN 9</td><td>PLN 4.50</td></tr>
      <tr><th scope="row">24 hours, zone A</th><td>PLN 18</td><td>PLN 9</td></tr>
      <tr><th scope="row">24 hours, zones A+B+C+D</th><td>PLN 24</td><td>PLN 12</td></tr>
      <tr><th scope="row">7 days, zone A</th><td>PLN 59</td><td>PLN 29.50</td></tr>
      <tr><th scope="row">7 days, zones A+B+C+D</th><td>PLN 94</td><td>PLN 47</td></tr>
    </tbody>
  </table></div>
  <h3>How to buy a ticket</h3>
  <p>Trams and buses have contactless payment terminals. You can buy time tickets and 24-hour tickets in them: choose a ticket on the screen and tap your payment card or phone. The terminal does not print a ticket, and at an inspection it is enough to show the card you paid with. You can also buy tickets in the apps moBILET, SkyCash, GoPay, jakdojade.pl and zBiletem, and at ticket machines at stops.</p>
  <p>The “Family 24 h” offer is good value: two standard 24-hour tickets validated at the same time cover 2 adults and up to 3 children aged up to 18. A 24-hour ticket validated between Friday 20:00 and Saturday 24:00 is valid until Sunday 24:00 (“Weekend 24 h”).</p>
  <p class="muted">Sources (in Polish): {ext("https://www.ztm.poznan.pl/wszystko-o-biletach/cennik-biletow/", "ZTM Poznań: fare list")}, {ext("https://www.ztm.poznan.pl/wszystko-o-biletach/rodzaje-i-formy-biletow/", "ZTM: types and forms of tickets")}.</p>
</section>

<section id="card">
  <h2>Poznań Tourist Card</h2>
  <p>The card gives free admission to most Poznań museums and discounts in restaurants, sports facilities and on tickets to the New Zoo, among others. The Poznań package is available for 24, 48 or 72 hours, in a standard or reduced version, with or without public transport. There is also an “Around Poznań” package with attractions in Poznań County.</p>
  <p>You can buy it online, in the app and at the tourist information points on the Old Market Square, on Kolegiacki Square (seasonal) and at the airport, as well as in the souvenir shop in the Gate of Poznań. Current package prices are on {ext("https://karta.visitpoznan.pl/", "karta.visitpoznan.pl")}.</p>
</section>

<section id="info">
  <h2>Tourist information</h2>
  <p>The points are run by the Poznań Local Tourist Organisation, which also publishes the official portal {ext("https://visitpoznan.pl/en/", "visitpoznan.pl")}.</p>
  <div class="table-wrap"><table class="grid">
    <thead><tr><th scope="col">Point</th><th scope="col">Address</th><th scope="col">Hours</th><th scope="col">Contact</th></tr></thead>
    <tbody>
      <tr><th scope="row">Old Market Square</th><td>Stary Rynek 59/60</td><td>Mon–Sat 9:30–18:00, Sun 9:00–17:00</td><td class="sel">+48 61 852 61 56</td></tr>
      <tr><th scope="row">Kolegiacki Square</th><td>pl. Kolegiacki 17</td><td>seasonal, 1 May–30 Sep: Mon–Sat 10:00–18:00, Sun 9:00–17:00</td><td class="sel">+48 883 400 034</td></tr>
      <tr><th scope="row">Ławica Airport</th><td>ul. Bukowska 285</td><td>daily (sources give different hours: 7:00–19:00 or 8:00–20:00)</td><td class="sel">info@airport-poznan.com.pl</td></tr>
      <tr><th scope="row">Gate of Poznań</th><td>ul. Gdańska 2</td><td>Tue–Fri 9:00–18:00, Sat–Sun 10:00–19:00</td><td class="sel">+48 61 647 76 34</td></tr>
    </tbody>
  </table></div>
  <p class="muted">Source: {ext("https://visitpoznan.pl/it", "visitpoznan.pl: Tourist Information")}</p>
</section>

<section id="food">
  <h2>Local food</h2>
  <p>The symbol of Poznań is the <i>rogal świętomarciński</i> (St Martin's croissant): a semi-French pastry filled with white poppy seed. Since 2008 it has had the EU Protected Geographical Indication. Only bakeries from the Greater Poland region that hold a certificate from the Chapter of the Poznań Traditional St Martin's Croissant may use the name. Most are eaten on 11 November.</p>
  <p>The restaurant Muga has held a Michelin star for the fourth year in a row. The Michelin Guide 2026 lists 25 venues from Poznań and the surrounding area.</p>
</section>

<section id="emergency">
  <h2>Emergency numbers</h2>
  <div class="table-wrap"><table class="grid grid-fit">
    <tbody>
      <tr><th scope="row">Emergency number (all services)</th><td class="sel big">112</td></tr>
      <tr><th scope="row">Ambulance</th><td class="sel big">999</td></tr>
      <tr><th scope="row">Fire brigade</th><td class="sel big">998</td></tr>
      <tr><th scope="row">Police</th><td class="sel big">997</td></tr>
      <tr><th scope="row">Municipal guard</th><td class="sel big">986</td></tr>
    </tbody>
  </table></div>
  <p>Calls to emergency numbers are free.</p>
</section>

<section id="health">
  <h2>Health and medical help</h2>
  <p>In a life-threatening emergency call 112 or 999. The call is free.</p>
  <h3>Hospital emergency departments</h3>
  <p>Emergency departments operate in these hospitals, among others:</p>
  <ul>
    <li>Provincial Hospital in Poznań (Szpital Wojewódzki), ul. Juraszów 7/19</li>
    <li>Józef Struś Multispecialty City Hospital, ul. Szwajcarska 3</li>
  </ul>
  <p>Go to an emergency department only in urgent cases. For less urgent problems in the evening, at night and at weekends, the night and holiday healthcare service can help.</p>
  <h3>Night and holiday healthcare</h3>
  <p>It operates Monday to Friday 18:00–8:00 and around the clock on Saturdays, Sundays and public holidays. You do not have to live in Poznań to use it. Selected points from the list published by the city (poznan.pl, December 2025):</p>
  <div class="table-wrap"><table class="grid grid-fit">
    <thead><tr><th scope="col">Facility</th><th scope="col">Address</th><th scope="col">Phone</th></tr></thead>
    <tbody>
      <tr><th scope="row">Centrum Medyczne HCP</th><td>ul. 28 Czerwca 1956 r. 194</td><td class="sel">61 227 41 88</td></tr>
      <tr><th scope="row">Poznań Centre of Specialist Medical Services (POSUM)</th><td>al. Solidarności 36</td><td class="sel">61 647 77 15</td></tr>
      <tr><th scope="row">Specialist Healthcare Team for Mother and Child</th><td>ul. Adama Wrzoska 1</td><td class="sel">61 616 20 20</td></tr>
    </tbody>
  </table></div>
  <p>The full list of points, and information on where to get help nearest to you, is available from the National Health Fund's Patient Information Line (in Polish): 800 190 590.</p>
  <h3>Dentist at night and on holidays</h3>
  <p>Emergency dental care is provided by Pozdent Stomatologia, ul. Czajcza 1a (Wilda), tel. 61 835 18 01.</p>
  <h3>Pharmacies</h3>
  <p>A list of pharmacies open at night and on holidays is published by the {ext("https://www.woia.pl/", "Greater Poland Regional Chamber of Pharmacists")} (in Polish).</p>
  <p class="muted">Source (in Polish): {ext("https://www.poznan.pl/mim/info/news/gdzie-do-lekarza-w-swieta,269048.html", "poznan.pl: where to see a doctor on public holidays")}.</p>
</section>

<section id="taxis">
  <h2>Taxis and ride-hailing</h2>
  <p>You can order a taxi by phone or in an app, for example iTaxi, tel. 737 737 737. Ride-hailing services such as Uber and Bolt also operate in Poznań.</p>
  <p>Ask for the price before the ride or check it in the app.</p>
</section>

<section id="parking">
  <h2>Driving: parking</h2>
  <p>The city centre is covered by a paid parking zone. The entrance to the zone is marked by a “P – paid parking” sign. There are three areas with different prices:</p>
  <div class="table-wrap"><table class="grid">
    <thead><tr><th scope="col">Zone</th><th scope="col">Area</th><th scope="col">When paid</th><th scope="col">1st hour</th><th scope="col">2nd hour</th><th scope="col">3rd hour</th><th scope="col">next hours</th></tr></thead>
    <tbody>
      <tr><th scope="row">SPP (blue)</th><td>Wilda, Łazarz, part of Jeżyce, Ostrów Tumski, Śródka and surroundings</td><td>Mon–Fri 8:00–20:00, Saturday free</td><td>PLN 5.00</td><td>PLN 6.00</td><td>PLN 7.00</td><td>PLN 5.00</td></tr>
      <tr><th scope="row">ŚSPP Jeżyce (red)</th><td>from ul. Roosevelta to ul. Polna and Kościelna, ul. św. Floriana</td><td>Mon–Sat 8:00–20:00</td><td>PLN 7.50</td><td>PLN 9.00</td><td>PLN 10.00</td><td>PLN 7.50</td></tr>
      <tr><th scope="row">ŚSPP Centrum (red)</th><td>Old Town</td><td>Mon–Sat 8:00–20:00</td><td>PLN 9.50</td><td>PLN 11.00</td><td>PLN 13.00</td><td>PLN 9.50</td></tr>
    </tbody>
  </table></div>
  <p>The prices are for drivers from outside Poznań. You pay at a parking meter; other ways of paying are described on the ZDM website. On Sundays parking is free in all zones, and in the blue zone also on Saturdays.</p>
  <p>It is more convenient to leave your car at a Park&amp;Ride car park and travel to the centre by public transport. The city's P&amp;R car parks are: Szymanowskiego (at PST), św. Michała, Biskupińska (at Poznań Strzeszyn station), Rondo Starołęka and Junikowo PKM (Plewiska, at Poznań Junikowo station). With a ZTM season ticket on a PEKA card, parking is free.</p>
  <p class="muted">Sources (in Polish): {ext("https://zdm.poznan.pl/oplaty-za-postoj", "ZDM Poznań: parking charges (price list from 1 Sep 2025)")}, {ext("https://zdm.poznan.pl/parkowanie-parkingi-park-ride-1", "ZDM: Park&amp;Ride car parks")}.</p>
</section>

<section id="cycling">
  <h2>Cycling</h2>
  <p>Poznań has a network of cycle paths. The Wartostrada runs along the Warta, a pedestrian and cycle path beside the river.</p>
  <p>You will find the Poznań Cycling Map 2026 at {ext("https://www.poznan.pl/rowery/", "poznan.pl/rowery")} (in Polish).</p>
  <h3>Renting bicycles and scooters</h3>
  <p>The city bike-share system, Poznański Rower Miejski, closed on 30 November 2022. The city justified this by, among other things, a fall in the number of rentals and costs, and by the fact that about 5,500 shared scooters and bicycles from three private operators were then on the streets. Old guides to the “city bike in Poznań” are therefore out of date.</p>
  <p>Today you can rent scooters and bicycles by the minute in the apps of private operators. In 2023 the city described the rules for the centre: in the paid parking zone a vehicle must be left at a designated “hop&amp;go” mobility point, and the app should not let you end the rental anywhere else. We have not checked which operators are active now, how much rides cost, or whether bans apply in the Old Town and on the Old Market Square. Check the rules on returning and riding in the centre in the operator's app and on the {ext("https://zdm.poznan.pl/", "Municipal Roads Authority (ZDM) website")} before you rent.</p>
  <p class="muted">Sources (in Polish): {ext("https://www.poznan.pl/mim/smartcity/news/ostatnie-dni-poznanskiego-roweru-miejskiego,192653.html", "poznan.pl: The last days of the Poznań City Bike (25 Nov 2022)")}, {ext("https://www.poznan.pl/mim/info/news/hulajnogi-w-strefach-mikromobilnosci,200071.html", "poznan.pl: Scooters in micromobility zones (23 Mar 2023)")}.</p>
</section>

<section id="guides">
  <h2>Guided tours</h2>
  <p>Guided tours are organised by, among others, the {ext("https://www.przewodnicy-pttk.org/pl/strona-glowna/", "Marceli Motty PTTK Guides' Circle")} (pl. Kolegiacki 16). You can also order a guide at the tourist information points.</p>
  <p>For a self-guided walk, the {ext("https://visitpoznan.pl/audioprzewodniki-po-poznaniu", "Visit Poznań audio guides")} and the marked Royal-Imperial Route (Trakt Królewsko-Cesarski) will come in handy.</p>
</section>

<section id="weather">
  <h2>Weather and seasons</h2>
  <p>Poznań has a temperate climate. July is the warmest month (19.5 °C on average) and January the coldest (−0.4 °C on average). July is also the rainiest month, so it is worth having an umbrella in summer.</p>
  <p>The current forecast is published by {ext("https://meteo.imgw.pl/", "IMGW")}, the Polish meteorological institute (in Polish).</p>
</section>
</div>
"""
