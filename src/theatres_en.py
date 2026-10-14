# -*- coding: utf-8 -*-
"""Angielska strona „Theatres and concerts” (/en/theatres). Klucz = id sceny z data_theatres.THEATRES.
Adresy, zdjęcia i adresy linków bierzemy z polskich danych; tu teksty i etykiety linków (w tej samej kolejności).
Po zmianie polskiej strony: zaktualizuj ten plik i uruchom: python src/check_en.py --stamp-theatres"""

INTRO = ("The main stages of Poznań: opera, philharmonic, drama theatres, dance and puppet theatre. For each venue we say "
         "what it stages, how to buy tickets and whether a visitor who does not speak Polish can follow the performance. "
         "Current repertoire and prices are on the theatres' websites.")

LANG_OK = "No Polish needed"
LANG_PL = "Performances in Polish"

# Drugi akapit „Good to know” (z odsyłaczami do Zamku Cesarskiego i kalendarza) jest w build_en.build_theatres_en.
MORE = [
    "Tickets for many events are sold by the Cultural Information Centre at ul. Ratajczaka 44.",
]

VENUES_EN = {
    "teatr-wielki": dict(
        name="Grand Theatre named after Stanisław Moniuszko (Opera)",
        kind="Opera, operetta, ballet, concerts",
        desc=["The Poznań opera performs in a building from 1910 with Pegasus on the roof, one of the symbols of the city. You can also tour the building behind the scenes.",
              "The box office is open Tuesday to Saturday 13:00–19:00, and on Sundays 2 hours before the performance (only if tickets are still available). Tickets are also sold by the Cultural Information Centre at ul. Ratajczaka 44."],
        links=["Repertoire", "Tickets online"],
    ),
    "filharmonia": dict(
        name="Poznań Philharmonic (University Aula)",
        kind="Symphonic and chamber concerts",
        desc=["The Philharmonic has operated since 1947 and gives its concerts in the Neo-Renaissance University Aula in the Collegium Minus building of 1910, on Plac Mickiewicza. The Aula is famous for its excellent acoustics.",
              "The Philharmonic also includes the boys' and men's choir Poznańskie Słowiki (the Poznań Nightingales). Other performers also play in the Aula, and tickets for their concerts are sold by the organisers.",
              "The box office is at the entrance to the Aula. From October to June it is open Tuesday to Friday 13:00–17:00, and on days of Philharmonic concerts also from an hour before the concert."],
        links=["Repertoire and tickets", "Box office"],
    ),
    "teatr-polski": dict(
        name="Polish Theatre (Teatr Polski)",
        kind="Drama theatre",
        desc=["The oldest theatre in Poznań, opened in 1875. It was built from contributions by Poles living under Prussian rule, which is commemorated by the inscription “Naród sobie” (“The Nation to Itself”) on the façade.",
              "The box office is open Tuesday to Friday 10:00–18:00 (or until the performance begins), and on Saturdays and Sundays an hour before the performance."],
        links=["Repertoire", "Theatre tours"],
    ),
    "teatr-nowy": dict(
        name="Teatr Nowy named after Izabella Cywińska",
        kind="Drama theatre",
        desc=["The theatre became a legend under the directorship of Izabella Cywińska, from 1973. Many productions of 1973–1989 are important events in the history of Polish theatre.",
              "In 1992 Tadeusz Łomnicki died on the stage of the Teatr Nowy, during a rehearsal of “King Lear”."],
        links=["Repertoire", "Prices and ticket purchase"],
    ),
    "teatr-muzyczny": dict(
        name="Musical Theatre (Teatr Muzyczny)",
        kind="Musicals and musical comedies",
        desc=["The theatre began operating in 1956 as the State Poznań Operetta. Today it mainly stages musicals.",
              "A new seat for the theatre is being built on Święty Marcin Street. Before your visit, check on the theatre's website where the performance takes place."],
        links=["Repertoire and tickets"],
    ),
    "ptt": dict(
        name="Polish Dance Theatre (Polski Teatr Tańca)",
        kind="Contemporary dance",
        desc=["A company founded in 1973, whose first director was the choreographer Conrad Drzewiecki. In its first years it was already counted among the best companies in Europe and was invited to international festivals. Choreographers from all over the world worked with it, among them Mats Ek and Ohad Naharin."],
        links=["Repertoire and tickets"],
    ),
    "teatr-animacji": dict(
        name="Animation Theatre (Teatr Animacji)",
        kind="Puppet theatre, performances for children and adults",
        desc=["A puppet theatre has operated in Poznań since 1945, and since 1989 under the name Teatr Animacji. It performs in the Zamek Culture Centre building, that is, the former Imperial Castle (main entrance).",
              "The box office is open from an hour before a performance and every Friday 15:00–18:00. A ticket for a children's performance costs PLN 55 (reduced PLN 50)."],
        links=["Repertoire", "Ticket prices"],
    ),
    "teatr-osmego-dnia": dict(
        name="Teatr Ósmego Dnia (Eighth Day Theatre)",
        kind="Alternative theatre",
        desc=["A legendary alternative theatre, founded in 1964 as a student theatre. In communist times its productions sharply commented on reality, and in 1986–1989 the company worked only abroad, performing street shows across Europe, among other things.",
              "The seat is on the second floor. The theatre opens an hour before an event, and there is a lift and a platform at the entrance."],
        links=["Repertoire"],
    ),
}
