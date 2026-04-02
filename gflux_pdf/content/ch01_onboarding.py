from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, bul, H2, callout, callout_bold, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("01", "Philosophie & Onboarding")

    s.append(body(
        "Das G-Flux Athleten-Protokoll ist kein Standard-Bulk-, Cut- oder Erhaltungsplan. Es ist "
        "ein leistungsorientiertes physiologisches Betriebssystem. Die zentrale Überzeugung: Der "
        "menschliche Körper adaptiert am effizientesten, wenn der gesamte Energiefluss massiv hoch "
        "ist — wenn riesige Mengen an Kalorien aufgenommen und gleichzeitig durch systematischen "
        "Workload verbraucht werden. Das Ergebnis bei konsequenter Umsetzung: gleichzeitiger "
        "Muskelaufbau, souveränes Fettmanagement und eine erstklassige Ausdauerkapazität."
    ))
    s.append(body(
        "Dieses Protokoll ist kein Einstieg für absolute Anfänger. Es erfordert eine klare Grundlage "
        "aus Kraft, Bewegungskompetenz und metabolischer Belastbarkeit. Die folgenden Voraussetzungen "
        "sind nicht verhandelbar."
    ))
    s.append(sp(6))

    s.append(H2("Voraussetzungen"))
    s.append(mk_table([
        ["VORAUSSETZUNG", "MINDESTSTANDARD", "WARUM ES WICHTIG IST"],
        ["Körperfettanteil",
         "Unter 15% (männlich)\nUnter 22% (weiblich)",
         "Über dem Grenzwert werden Überschusskalorien bevorzugt in Fett umgewandelt. "
         "Der Partitionierungsvorteil kollabiert vollständig."],
        ["Kraftniveau",
         "Frühes bis mittleres Niveau bei Grundzügen",
         "Schwere Grundzüge sind das mechanische Fundament. Unzureichende Kraft minimiert "
         "den systemischen Trainingsreiz."],
        ["Laufbasis",
         "10 km am Stück durchlaufen können",
         "Das Laufvolumen beginnt bei 10 km. Null aerobe Grundlage bedeutet ein unakzeptabel "
         "hohes strukturelles Verletzungsrisiko."],
        ["Ernährungswissen",
         "Makro-Tracking blind beherrschen",
         "Kalorien-Wiederauffüllung und Untergrenzenverwaltung erfordern absolute Präzision. "
         "Schätzen reicht hier nicht."],
        ["Regenerationswissen",
         "HRV und Ruhepuls kennen",
         "Biomarker-gesteuertes Training erfordert, dass der Athlet die eigenen Daten "
         "interpretieren und logisch handeln kann."],
    ], [CONTENT_W * 0.25, CONTENT_W * 0.3, CONTENT_W * 0.45]))
    s.append(sp(6))

    s.append(callout_bold(
        "KÖRPERFETT-DECKELREGEL: Die Aufbauphase erlaubt niemals einen Körperfettanteil über 15% "
        "(männlich) bzw. 22% (weiblich). Wenn das Tracking oder die visuelle Beurteilung eine "
        "Annäherung an diese Grenze anzeigt, wird zwingend zuerst die Kalorienuntergrenze angepasst. "
        "Das ist der primäre, kompromisslose Kontrollmechanismus."
    ))
    s.append(sp(6))

    s.append(H2("Tag 1: Die Adaptionsphase (Pipeline Stufe 1)"))
    s.append(body(
        "Das G-Flux Protokoll ist kein 30-Tage-Quick-Fix. Die ersten vier Wochen bilden deine "
        "fundamentale Adaptionsphase. Das System entwickelt sich in Stufen. In Phase 1 muss noch "
        "nicht alles perfekt sein, aber die Struktur muss stehen. So startest du an Tag 1:"
    ))
    for pt in [
        "Frequenz wählen: Entscheide dich realistisch für den 9-Tage-Zyklus oder einen 3- bzw. "
        "4-Tage-Split. Dies diktiert deinen gesamten wöchentlichen Workload.",
        "Start-Kilometer festlegen: Beginne bei 10 km. Nicht mehr. Dies etabliert deine minimale "
        "aerobe Basis und schützt die Sehnen vor dem ansteigenden Workload.",
        "Feste Cardio-Termine im Kalender: Betrachte sie als unverschiebbare Meetings mit deiner "
        "Leistungsfähigkeit. Empfehlung: Morgens, vor oder direkt nach einem leichten Frühstück.",
        "Hauptübungen fixieren: Wähle die Grundzüge für den ersten Block und bleibe dabei. "
        "Konstante mechanische Reize erzwingen konstante Adaption.",
    ]:
        s.append(bul(pt))
    s.append(sp(8))

    s.append(callout(
        "DIY-FILTER: Wir sind keine Grifter, die dir an Tag 1 ein Abonnement andrehen. Führe die "
        "ersten 4 Wochen in absoluter Eigenregie durch. Tracke händisch, rechne deinen EMA, lerne "
        "das Feedback deines ZNS kennen. Erst wenn du die Adaption auf zellulärer Ebene verstanden "
        "hast, macht die Optimierungsphase durch das CbTK 1-on-1 Coaching oder den automatisierten "
        "Tracker Sinn. Verdien dir das Upgrade."
    ))

    return s
