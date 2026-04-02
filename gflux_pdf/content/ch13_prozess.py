from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, bul, callout_bold, section_break,
)


def build() -> list:
    s = [PageBreak()]
    s += section_break("13", "Dem Prozess vertrauen")

    s.append(body(
        "Das G-Flux Athleten-Protokoll arbeitet langsam und sichtbar gleichzeitig. Woche für Woche "
        "erscheinen die Veränderungen subtil. Monat für Monat werden sie unverkennbar. Dieses "
        "Protokoll belohnt keine Touristen. Wer nach drei Wochen in den Spiegel schaut und eine "
        "komplette Metamorphose erwartet, hat die Physiologie des menschlichen Körpers nicht "
        "verstanden. Wahre Adaptation — das Einbauen von dichten, neuen Mitochondrien, das "
        "Verdicken von Sehnen, der Aufbau von echtem, kontraktilem Gewebe — braucht Zeit."
    ))
    s.append(body(
        "Der Athlet, der kurzfristigen Signalen nachjagt — täglichen Waagenschwankungen, einer "
        "schlechten Session, einer Woche erhöhter Ermüdung — wird ständig ein System überschreiben, "
        "das Geduld und Konsistenz braucht, um sein volles Ergebnis zu liefern. Athleten scheitern "
        "nicht an schlechten Plänen. Sie scheitern, weil sie bei der ersten täglichen "
        "Waagenschwankung in Panik geraten. Weil sie das Programm wechseln, genau an dem Punkt, an "
        "dem die zelluläre Anpassung eigentlich stattfinden würde."
    ))
    s.append(body(
        "Jede Komponente stärkt jede andere. Hohe Kalorien unterstützen schweres Training. Schweres "
        "Training fordert hohe Kalorien. Cardio verbessert Insulinsensitivität. Hohe "
        "Insulinsensitivität macht Kohlenhydrate anaboler. Qualitätsschlaf pusht die HRV. Bessere "
        "HRV erlaubt qualitativ hochwertigere Trainingseinheiten. Bessere Einheiten erzeugen "
        "massiveren Output und mehr Anpassung. Mehr Anpassung rechtfertigt mehr Volumen. Mehr "
        "Volumen erfordert mehr Kalorien. Das System verstärkt sich selbst physiologisch."
    ))
    s.append(sp(6))

    s.append(bul("Zu wenig essen an hochleistungsfähigen Tagen. Die Wiederauffüllungsregel ist absolut nicht optional."))
    s.append(bul("Zu oft zu hart laufen. Zone-2-Disziplin ist das eiserne Fundament des Cardio-Blocks."))
    s.append(bul("Volumen schneller steigern als Regenerationsdaten es autorisieren."))
    s.append(bul("Auf tägliches Waagensrauschen reagieren. Dem EMA über mindestens 4 Wochen vertrauen."))
    s.append(bul("Die Entlastungswoche überspringen. Hier findet Anpassung wirklich statt."))
    s.append(bul("Biomarker-Signale ignorieren. Daten existieren genau dazu, das Rätselraten zu eliminieren."))
    s.append(bul("Muskelkater als Fortschrittsindikator verwechseln. Muskelkater zeigt Neuheit, keine Anpassung."))
    s.append(bul("Das Programm alle paar Wochen wechseln. Das System braucht Zeit, um seine Ergebnisse zu zementieren."))
    s.append(sp(8))

    s.append(callout_bold(
        "ABSCHLUSSPRINZIP: Dieses Protokoll funktioniert nur im Kalorienüberschuss. Der Überschuss "
        "treibt die Anpassung an. Das Cardio kontrolliert den Überschuss. Das Training verwandelt "
        "den Überschuss in Muskel. Die Daten halten das System ehrlich. Die Entlastungswoche "
        "realisiert die Anpassung. Entferne eine einzige Komponente und das System kollabiert. "
        "Führe alle Komponenten aus, und das Resultat ist unausweichlich."
    ))

    return s
