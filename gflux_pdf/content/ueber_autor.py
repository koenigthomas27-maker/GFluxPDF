from reportlab.platypus import PageBreak
from gflux_pdf.components import sp, body, H2, callout, section_break


def build() -> list:
    s = [PageBreak()]
    s += section_break("—", "Über den Autor")

    s.append(H2("Thomas König — CbTK"))
    s.append(body(
        "Thomas König hat mehr als fünfzehn Jahre in Krafträumen, auf Laufbahnen und in "
        "Reha-Kliniken verbracht — oft gleichzeitig. Sein Hintergrund umfasst Powerlifting, "
        "Mannschaftssport, Ringen und Bodybuilding. Er hat Crashdiäten, Protein-Sparende "
        "Modifizierte Fastenprotokolle (PSMF), ketogene Protokolle, pflanzliche Ansätze und "
        "absurde Zuckermanipulationsstrategien am eigenen Leib durchgeführt. Nicht als "
        "theoretische akademische Experimente — sondern als gelebte, blutige Erfahrung, gnadenlos "
        "dokumentiert und an realen, messbaren Ergebnissen validiert."
    ))
    s.append(body(
        "Er hat durch Verletzungen trainiert, für die die meisten Trainer vollständige Ruhe "
        "verordnet hätten. Er hat Bewegungsmuster von Grund auf neu aufgebaut, nachdem jahrelanges, "
        "blindes Hochvolumentraining, das Optik über Langlebigkeit stellte, massive Gelenkschäden "
        "hinterlassen hatte. Er hat die besten Prinzipien aus Powerlifting-Programmierung, "
        "Hypertrophiemethodik, Ausdauercoaching und Kraft-Konditions-Praxis extrahiert — und "
        "ausnahmslos alles verworfen, was den Kontakt mit der Realität nicht überlebt hat."
    ))
    s.append(body(
        "Das G-Flux Athleten-Protokoll ist das direkte Destillat dieses Prozesses. Es ist keine "
        "akademische Labor-Theorie. Es ist im Schützengraben getestet, iteriert und durch "
        "gnadenlose persönliche Anwendung und hunderten von Coaching-Stunden kontinuierlich "
        "verfeinert. Es ist die ungeschönte Antwort auf die Frage: Wie sieht intelligentes, "
        "nachhaltiges, hochleistungsfähiges Training für einen Menschen mit einem echten Leben "
        "und einem langen Zeithorizont wirklich aus?"
    ))
    s.append(callout(
        "Dieses Handbuch ist ein lebendes Dokument. Es wird aktualisiert, wenn neue Erkenntnisse, "
        "neue Leistungsdaten und neue Coaching-Anwendungen den Ansatz verfeinern. Die Version, die "
        "du gerade liest, spiegelt den messerscharfen aktuellen Stand der Praxis wider. Die nächste "
        "Version wird besser sein. Das ist der Maßstab."
    ))

    return s
