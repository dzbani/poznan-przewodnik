# -*- coding: utf-8 -*-
"""Angielska wersja strony Prywatność (/en/privacy). Treść odpowiada build.build_privacy();
po zmianie polskiej wersji zaktualizuj ten plik i uruchom: python src/check_en.py --stamp-privacy"""
from build import CONTACT_EMAIL, PRIVACY_UPDATED


def body(en_date):
    mail = f'<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>'
    ext = lambda url, text: f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'
    return f"""
<header class="wrap page-head">
  <p class="kicker">Legal information</p>
  <h1>Privacy</h1>
  <p class="lead">In short: there are no ads, forms or accounts here. The only thing we ask for is your consent to anonymous visit statistics in Google Analytics. Without your consent the site does not store cookies and does not connect to Google.</p>
  <nav class="toc" aria-label="Contents">
    <a href="#who">Who runs the site</a><a href="#cookies">Cookies and statistics</a><a href="#geolocation">Geolocation</a><a href="#hosting">Server</a>
    <a href="#external">External services</a><a href="#rights">Your rights</a>
  </nav>
</header>

<div class="wrap prose">
<section id="who">
  <h2>Who runs the site</h2>
  <p>The guide “Odkrywaj Poznań” (odkrywajpoznan.pl) is a private, non-commercial website, not affiliated with the City of Poznań Office. The controller of the statistics data described below is “Odkrywaj Poznań”. For matters concerning the site and privacy, write to {mail}.</p>
</section>

<section id="cookies">
  <h2>Cookies and statistics</h2>
  <p>On your first visit we ask whether we may count visits with <strong>Google Analytics 4</strong>. This tells us which pages are read and what is worth developing. The two buttons, “Accept” and “Decline”, are equal, and declining blocks nothing.</p>
  <ul>
    <li><strong>If you decline or make no choice:</strong> the Google script is not loaded, no cookies are created and nothing is sent to Google.</li>
    <li><strong>If you accept:</strong> your browser downloads a script from googletagmanager.com and sends information about the visit to Google Analytics: the pages you open, the address of the page you came from, your approximate location (city and country determined from the IP address, which Google Analytics 4 does not store), the device type, system and browser, screen resolution and language. Google stores the cookies <code>_ga</code> and <code>_ga_S4K8EW3YGQ</code>, which make it possible to tell a returning browser from a new one. They expire after 2 years.</li>
  </ul>
  <p>We do not use Google's advertising features or Google signals (consent for them is switched off), we do not combine the statistics with other data and we do not try to find out who you are. We only see aggregate reports.</p>
  <p><strong>Legal basis:</strong> your consent (Article 6(1)(a) GDPR, Article 399 of the Polish Electronic Communications Law). You can withdraw it at any time with the <button type="button" class="linkish" data-consent-open>Cookie settings</button> button (it is also in the footer of every page). After you withdraw consent we delete the Google Analytics cookies from your browser. Withdrawal does not affect the lawfulness of the statistics collected earlier.</p>
  <p><strong>Recipient and transfer outside the EEA:</strong> the data goes to Google Ireland Limited. It may also be processed by Google LLC in the USA, which participates in the EU-U.S. Data Privacy Framework (a European Commission decision finding an adequate level of protection). Terms: {ext("https://policies.google.com/privacy?hl=en", "Google Privacy Policy")}, {ext("https://business.safety.google/adsprocessorterms/", "data processing terms")}.</p>
  <p><strong>How long:</strong> data about visits is kept in Google Analytics for 14 months, after which Google deletes it.</p>
  <p><strong>Your choice</strong> is saved in your browser's storage (localStorage, the entry <code>op-zgoda-statystyki</code>) so that we do not ask on every page. It is not a cookie, it is not sent anywhere and it disappears when you clear the site's data in your browser.</p>
  <p>If you add the site to your phone's home screen, the browser may keep its files in ordinary cache. This is not data about you.</p>
</section>

<section id="geolocation">
  <h2>Geolocation</h2>
  <p>On the Map page there is a <strong>“Where am I”</strong> button. If you click it, your browser will ask for permission to access your GPS location. This is entirely optional.</p>
  <ul>
    <li><strong>If you do not click the button:</strong> no location is collected. You can browse the map normally by clicking names and filtering attractions.</li>
    <li><strong>If you give permission:</strong> you allow the browser to use GPS (or an approximate position from Wi-Fi or the mobile network). Your location <strong>stays only in your browser</strong> and is never sent to us. We use it only to:
      <ul>
        <li>show your marker on the map,</li>
        <li>sort the list of attractions from the nearest, with distances in kilometres.</li>
      </ul>
    </li>
    <li><strong>If you refuse:</strong> the button stays available for another try. You can withdraw permission in your browser settings.</li>
  </ul>
  <p><strong>Support:</strong> geolocation works in browsers that support <code>navigator.geolocation</code> (Chrome, Firefox, Safari, Edge). The data does not leave your browser.</p>
</section>

<section id="hosting">
  <h2>Server</h2>
  <p>The site is served by GitHub Pages (GitHub, Inc.). Like any server, GitHub records technical connection data in its logs, including the IP address, date and time and the address of the page opened, to ensure the security and functionality of the service. We do not have access to these logs. Terms: {ext("https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement", "GitHub privacy statement")}.</p>
  <p>The domain is registered with OVH.</p>
</section>

<section id="external">
  <h2>External services</h2>
  <p>The site's fonts, photographs and scripts are on our own server. The exceptions are:</p>
  <ul>
    <li><strong>Google Analytics</strong> (googletagmanager.com, google-analytics.com), only with your consent, described above;</li>
    <li><strong>the attractions map</strong> (the Map page only): its base layer comes from OpenStreetMap servers, so your browser passes them your IP address ({ext("https://osmfoundation.org/wiki/Privacy_Policy", "OSMF policy")}).</li>
  </ul>
  <p>The “Show on map” and directions links open Google Maps, and the other links lead to the websites of museums, organisers and other services. Once you follow them, their own privacy policies apply.</p>
</section>

<section id="rights">
  <h2>Your rights</h2>
  <p>With regard to the statistics you have the right to withdraw consent, and to access, rectify, erase, restrict the processing of and transfer your data. However, the statistics do not allow us to tell which data concerns you, so the simplest way is to withdraw consent, which removes the identifier from your browser. For other matters write to {mail}.</p>
  <p>You have the same rights under the GDPR with regard to GitHub, OpenStreetMap and Google. You can also lodge a complaint with the President of the Personal Data Protection Office, UODO ({ext("https://uodo.gov.pl/en", "uodo.gov.pl")}).</p>
  <p class="muted">Last updated: {en_date(PRIVACY_UPDATED)}. This is a translation of the Polish privacy page; in case of doubt the <a href="../prywatnosc.html" hreflang="pl" lang="pl">Polish version</a> prevails.</p>
</section>
</div>
"""
