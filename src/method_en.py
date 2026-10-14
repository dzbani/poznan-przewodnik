# -*- coding: utf-8 -*-
"""Angielska strona „How we verify information” (/en/how-we-verify). Odpowiada build.build_method().
Po zmianie polskiej strony: zaktualizuj ten plik i uruchom: python src/check_en.py --stamp-method"""
from build import CONTACT_EMAIL


def body(n_attractions, first_date, last_date, practical_date, links_date):
    mail = f'<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>'
    return f"""
<header class="wrap page-head">
  <p class="kicker">About the site</p>
  <h1>How we verify information</h1>
  <p class="lead">In a guide it matters more that information is true than that there is a lot of it. Below we describe where we get our data, what we do when sources disagree, and what we do not promise.</p>
  <nav class="toc" aria-label="Contents">
    <a href="#sources">Where we get our data</a><a href="#conflicts">When sources disagree</a><a href="#dates">Check dates</a>
    <a href="#not-do">What we do not do</a><a href="#photos">Photographs</a><a href="#errors">Found a mistake?</a>
  </nav>
</header>

<div class="wrap prose">
<section id="sources">
  <h2>Where we get our data</h2>
  <ul>
    <li><strong>Opening hours, prices, addresses and phone numbers</strong> come from the venue's own website or from official portals: the city's poznan.pl, the tourist portal visitpoznan.pl and organisers' sites, for example those of museums. Search engines and aggregators often show old data. An example: the Croissant Museum showed pre-increase prices in search results, while according to the museum's website a ticket has cost PLN 41 and PLN 47 since 2 January 2026.</li>
    <li><strong>Historical descriptions</strong> are based on official portals and on Wikipedia. We do not take hours or prices from Wikipedia.</li>
    <li><strong>Each of the {n_attractions} attractions</strong> has a list of sources with links under its description, so you can check where a piece of information comes from.</li>
    <li><strong>The climate of Poznań</strong> was calculated from raw IMGW data for 1991–2020 (Poznań-Ławica station), not copied from other sites.</li>
    <li><strong>The events calendar</strong> contains only what the organiser's website or an official portal confirms. We enter the date of the next edition only when the organiser has announced it, not on the basis of estimates.</li>
  </ul>
</section>

<section id="conflicts">
  <h2>When sources disagree</h2>
  <p>We do not choose by eye. In such a situation we do one of two things: we give only what all the sources confirm and describe the discrepancy with the names of the sources, or we leave the information out and refer you to the venue.</p>
  <ul>
    <li><a href="attractions/fort-iii.html">Fort III</a>: two official portals give different days and entry times. We wrote what is certain and described the discrepancy openly.</li>
    <li><a href="attractions/muzeum-czerwca-1956.html">Museum of the Poznań June 1956</a>: we could not confirm the hours in any current source, so we do not give them and ask you to contact the museum.</li>
    <li><a href="attractions/niewidzialna-ulica.html">Invisible Street</a>: sources give different prices, so we refer you to the venue's website instead of entering one of them.</li>
  </ul>
</section>

<section id="dates">
  <h2>Check dates</h2>
  <p>Under every attraction you can see a “Checked” date. It is the day on which we last compared the data with the sources. At present all attractions were checked between {first_date} and {last_date}, and the “Practical information” section on {practical_date}.</p>
  <p>Hours and prices change, and the date is not a guarantee that things are the same today. Before your visit, confirm them on the venue's website. We do not promise to refresh the data at a fixed rhythm, but changes we learn about we check and enter.</p>
  <p>We check the links to sources automatically (last check: {links_date}), and when a source ceases to exist we remove it together with information that rested only on it.</p>
</section>

<section id="not-do">
  <h2>What we do not do</h2>
  <ul>
    <li>We do not give phone numbers, hours or prices if we do not have them from a reliable source.</li>
    <li>We do not give lines or stops for getting to attractions without checking. Instead there is a link to a public-transport route in Google Maps.</li>
    <li>We do not write reviews or ratings and do not accept paid entries. There are no ads on the site.</li>
    <li>We rely on public sources, not on our own accounts of visits to every place.</li>
  </ul>
  <p>This guide is a private, non-commercial website, not affiliated with the City of Poznań Office (<a href="privacy.html#who">more</a>).</p>
</section>

<section id="photos">
  <h2>Photographs</h2>
  <p>Most photographs come from Wikimedia Commons under open licences. You will find the author and the licence of a photograph by clicking the “i” icon in its corner, and all of them together on the page <a href="../zdjecia.html" hreflang="pl" lang="pl">Photo credits</a> (in Polish). When Commons has no photograph with a named author, we show a placard with the name of the place instead.</p>
</section>

<section id="errors">
  <h2>Found a mistake?</h2>
  <p>Next to every attraction there is a “Report outdated information” link that opens a ready email with the name of the place. You can also write to {mail}. We check a report against the sources before we change the data.</p>
</section>
</div>
"""
