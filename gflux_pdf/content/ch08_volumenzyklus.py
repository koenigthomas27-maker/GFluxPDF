from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, bul, H2, callout_bold, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("08", "Der 8-Wochen-Volumenzyklus")

    s.append(body(
        "Das Training ist in 8-wöchige Mesozyklen mit ansteigendem Volumen organisiert. Progressive "
        "Überlastung gilt nicht nur für die Last, sondern für den gesamten Trainingsreiz — Sätze, "
        "Übungen und Cardio-Volumen steigen progressiv, wenn die Athleten ausreichende "
        "Regenerationskapazität zeigen. Das Volumen steigt nie schneller, als der Körper es zellulär "
        "verarbeiten kann."
    ))
    s.append(body(
        "Woche 8 ist die Höhepunktwoche des Blocks ('Peak / Overreaching' - KEINE 'Death Week'). "
        "Wir bauen kontinuierlich darauf auf. Die Entlastungswoche ist ein separater 1-wöchiger "
        "Überbrückungsblock."
    ))
    s.append(sp(4))

    s.append(H2("Phasenstruktur"))
    s.append(mk_table([
        ["PHASE", "DAUER", "VOLUMEN", "INTENSITÄT", "FOKUS"],
        ["Aufbau: Baseline",
         "Woche 1-4",
         "Start am Minimum aller Stufenspannen. Alle 1-2 Wochen 1 Satz hinzufügen, wenn "
         "Regeneration es zulässt.",
         "Konservativ-methodisch aufbauen. Max. RPE 7-8.",
         "Arbeitskapazitätsaufbau. Baseline-Leistung für den Block etablieren."],
        ["Bump: Grundzüge",
         "Woche 5-7",
         "Sätze bei Grundzügen erhöhen. Sekundär und Isolation nahe Maximum.",
         "Top-Satz-Last um 2,5-5% steigern.",
         "Kraftschwerpunkt Grundzüge. Biomarker eng beobachten. Ermüdung akkumuliert hier massiv."],
        ["Peak / Overreach",
         "Woche 8",
         "Maximales Volumen des Zyklus. Alle Stufen am absoluten Limit.",
         "Schwerste Lasten des gesamten Zyklus.",
         "Funktionelle Überbelastung. ZNS und Muskel auf Maximum. Hier ist das Anpassungssignal "
         "am größten."],
        ["ENTLASTUNGSWOCHE",
         "1 Woche (separat)",
         "Auf 50-60% des Peak-Volumens reduzieren. Nur Grundzüge — keine Isolationen.",
         "Last um 20-30% reduzieren. Bewegungsqualität im Fokus.",
         "Superkompensations-Fenster. HIER wächst der Muskel und passt sich die Kraft an. "
         "Nicht verhandelbar."],
    ], [CONTENT_W*0.15, CONTENT_W*0.15, CONTENT_W*0.25, CONTENT_W*0.2, CONTENT_W*0.25],
        accent_rows={4}))
    s.append(sp(6))

    s.append(H2("Zwischen den Zyklen — Volumen-Reset"))
    s.append(body(
        "Zu Beginn jedes neuen 8-Wochen-Blocks werden Satz- und Wdhlg.-Zahlen auf das Minimum "
        "zurückgesetzt. Die Stangenlast wird übernommen und kann steigen. Das Peak-Volumen wird nie "
        "in den nächsten Zyklus mitgenommen. Diese bewusste Reduktion um 10-20% vom Peak ermöglicht "
        "vollständige Adaptionsverarbeitung und schafft das Fundament für den nächsten Überlastungsblock."
    ))
    s.append(sp(6))

    s.append(H2("Block-Zielanpassung"))
    s.append(body(
        "Jeder neue Trainingsblock wird gegen die aktuellen Ziele des Athleten abgeglichen. "
        "Anpassungen erfolgen auf Block-Ebene, nicht von Session zu Session."
    ))
    s.append(mk_table([
        ["BLOCK-ZIEL", "KRAFTTRAINING-ANPASSUNG", "CARDIO-ANPASSUNG"],
        ["Reiner Muskel- / Kraftaufbau",
         "Volles Protokoll. Grundzüge priorisiert.",
         "30-45 km/Woche. Zone 2 dominant."],
        ["Wettkampfvorbereitung\n(5k, 10k, Halbmarathon)",
         "Kraftintensität beibehalten. Volumen um 1 Satz je Stufe reduzieren. Grundzüge schwer lassen.",
         "Schwellentraining und Renntempo erhöhen. Wettkampfspezifische Einheiten hinzufügen. "
         "Gesamtvolumen kann 50 km übersteigen."],
        ["Rekomposition / Fettdeckel erreicht",
         "Volles Kraftprotokoll beibehalten.",
         "Zone 2 dominant, Schwellentraining reduzieren. Siehe Mini-Cut-Protokoll."],
        ["Regeneration / Entlastungsblock",
         "50-60% Volumen. Nur Grundzüge.",
         "Nur Zone 2, max. 15-20 km. Kein Intensitätswork."],
    ], [CONTENT_W*0.25, CONTENT_W*0.35, CONTENT_W*0.4]))
    s.append(sp(6))

    s.append(H2("Übertraining vs. Under-Recovery & Der Perpetual Intermediate"))
    s.append(body(
        "Lass uns ein populäres Konzept beerdigen: Die Angst vor 'Übertraining' produziert den "
        "'Perpetual Intermediate' – den Athleten, der sich jahrelang weder optisch noch "
        "leistungstechnisch verändert. Übertraining existiert für den Nicht-Profisportler faktisch "
        "nicht. Wenn du nicht gerade 25 Stunden die Woche wie ein Elite-Triathlet trainierst, bist "
        "du nicht im Übertraining. Was du erlebst, ist Under-Recovery: schlechte Ernährung, "
        "unzureichende Kalorienuntergrenzen, mieser Schlaf und toxischer Alltagsstress."
    ))
    s.append(body(
        "Die sportwissenschaftliche Forschung zur Superkompensation (Functional Overreaching) belegt "
        "klar: Ein temporärer, akuter Leistungsabfall durch akkumulierte Ermüdung ist zwingend "
        "notwendig, um eine Anpassung des zentralen Nervensystems (ZNS) und des Gewebes zu erzwingen. "
        "Wer beim ersten Anflug von Müdigkeit das Training abricht, überschreitet niemals diese Schwelle."
    ))
    s.append(body(
        "Es ist kritisch, genau dann durchzupushen, wenn alle objektiven Metriken (dein EMA stimmt, "
        "du isst im G-Flux-Überschuss, du schläfst 8 Stunden) im grünen Bereich sind, aber dein "
        "subjektives Gefühl im absoluten Keller ist. Das trennt den Athleten vom Touristen."
    ))
    s.append(sp(4))

    s.append(callout_bold(
        "DAS PRAXIS-BEISPIEL: Du wachst auf, die Beine sind schwer, der Kopf ist träge. Dein Gefühl "
        "sagt dir: 'Bleib auf der Couch, du bist im Übertraining.' Aber deine HRV ist stabil und die "
        "Kalorien sind gedeckt. Du gehst ins Gym. Du wärmst dich auf. Und exakt an diesem "
        "'verschissensten Tag' durchbrichst du dein Gewichts-Plateau beim Kniebeugen oder läufst "
        "einen 10k-PR. Warum? Weil der Körper sich anpasst. Die Stresstoleranz deines ZNS wurde "
        "zellulär erweitert. Du hast dem Körper bewiesen, dass die vorherige Grenze eine Illusion war."
    ))

    return s
