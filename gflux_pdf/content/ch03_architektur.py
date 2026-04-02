from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, H2, H3, callout, callout_bold, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("03", "Trainingsarchitektur: Der 9-Tage-Zyklus")

    s.append(body(
        "In der Exekutionsphase läuft das Protokoll auf einem 9-tägigen Rotationszyklus statt nach "
        "einem festen 7-Tage-Wochenplan. Damit wird die Trainingsfrequenz vom Kalender entkoppelt. "
        "Die tatsächliche ZNS-Regeneration bestimmt wirklich die Sessionplanung. Die Struktur folgt "
        "einem Rumpf/Extremitäten-Split über drei Variationen (A, B, C) mit einem dedizierten "
        "Ruhe-/Arm-/Bauch-Tag als Regenerationssession zwischen je zwei Trainingstagen."
    ))
    s.append(sp(6))

    s.append(mk_table([
        ["TAG", "SESSION", "CARDIO-OPTIONEN", "HINWEISE"],
        ["Tag 1", "Rumpf A",            "Lockerer Lauf / Elliptical",    "Drücken-Ziehen Fokus A"],
        ["Tag 2", "Extremitäten A",     "Hartes Cardio hier stapelbar",  "Kniebeugedominante Grundzüge"],
        ["Tag 3", "Ruhe / Arme / Bauch","Nur leichtes Cross-Training",   "ZNS-schonendes Training. Aktive Erholung."],
        ["Tag 4", "Rumpf B",            "Lockerer Lauf / Elliptical",    "Drücken-Ziehen Fokus B"],
        ["Tag 5", "Extremitäten B",     "Hartes Cardio hier stapelbar",  "Scharnierbewegung dominante Grundzüge"],
        ["Tag 6", "Ruhe / Arme / Bauch","Nur leichtes Cross-Training",   "ZNS-schonendes Training. Aktive Erholung."],
        ["Tag 7", "Rumpf C",            "Lockerer Lauf / Elliptical",    "Drücken-Ziehen Fokus C"],
        ["Tag 8", "Extremitäten C",     "Hartes Cardio hier stapelbar",  "Kniebeugedominant (anderer Winkel)"],
        ["Tag 9", "Ruhe / Arme / Bauch","Nur leichtes Cross-Training",   "Zyklus wird mit Tag 1 neu gestartet"],
    ], [CONTENT_W * 0.12, CONTENT_W * 0.25, CONTENT_W * 0.33, CONTENT_W * 0.3]))
    s.append(sp(6))

    s.append(callout_bold(
        "STAPELREGEL: Hartes Cardio — Intervalle, VO2max-Einheiten, Tempoläufe, "
        "Konditionsschaltkreise — wird immer an Extremitäten-Tagen platziert, unmittelbar vor dem "
        "vollständigen Ruhetag. Dies konzentriert die maximale physiologische Anpassung auf einen "
        "Tag und garantiert ein vollständiges Regenerationsfenster vor der nächsten schweren Einheit."
    ))
    s.append(sp(6))

    s.append(H2("Alternative Strukturen"))
    s.append(body(
        "Dieselbe Bewegungsmuster-Logik gilt bei einem 3-Tage-Ganzkörper- oder "
        "4-Tage-Ober-/Unterkörper-Split. Weniger Trainingstage bedeuten nur, dass Rumpf- und "
        "Extremitätenmuster auf weniger Sessions verteilt werden — das Prinzip, dass keine zwei "
        "aufeinanderfolgenden Sessions dieselbe Bewegungsebene gleich intensiv belasten, bleibt "
        "unumstößlich."
    ))
    s.append(sp(6))

    s.append(H2("Satz- und Wiederholungsschema"))
    s.append(body(
        "Das Volumen ist in drei Stufen organisiert. Jeder neue Zyklus beginnt am untersten Ende "
        "jeder Stufenspanne. Volumen wird nur erhöht, wenn die Regenerationsdaten das bedingungslos "
        "unterstützen. Das Volumen steigt nie schneller, als der Körper es zellulär verarbeiten kann. "
        "Wer hier das Ego nicht kontrolliert und zu früh eskaliert, sabotiert die langfristige Adaption."
    ))
    s.append(sp(4))

    s.append(mk_table([
        ["STUFE", "ÜBUNGSTYP", "SÄTZE", "WDHLG.", "PAUSE", "ZIEL"],
        ["1 — Grundzüge",
         "1-2 Hauptbewegungen",
         "1-2 Top-Sätze\n+ 2-4 Rücksätze",
         "TS: 5-8\nRS: 8-12",
         "3-4 Min.",
         "Maximaler Kraftreiz. Top-Satz ist das Tageshoch."],
        ["2 — DUP Sekundär",
         "1-3 sekundäre Bewegungen",
         "2-3 Sätze",
         "8-12",
         "2,5-3 Min.",
         "Volumenakkumulation. Spiegelt Muster bei sub-maximaler Last."],
        ["3 — Isolation",
         "1-4 frei gewählte Übungen",
         "2-4 Sätze",
         "8-15 / 10-20",
         "1,5-2 Min.",
         "Metabolischer Stress, Gewebequalität. Rest-Pause möglich."],
    ], [CONTENT_W * 0.15, CONTENT_W * 0.2, CONTENT_W * 0.15, CONTENT_W * 0.1,
        CONTENT_W * 0.1, CONTENT_W * 0.3]))
    s.append(sp(6))

    # --- NEW CONTENT: Sample Session Templates ---
    s.append(H2("Beispiel-Session-Templates"))
    s.append(body(
        "Die folgenden Templates zeigen, wie ein konkreter Trainingstag im 9-Tage-Zyklus strukturiert "
        "ist. Übungen sind austauschbar innerhalb des Bewegungsmusters — die Struktur aus Grundzug, "
        "DUP-Sekundär und Isolationen bleibt immer erhalten."
    ))
    s.append(sp(4))

    s.append(H3("Rumpf A — Drücken/Ziehen Fokus (Beispiel)"))
    s.append(mk_table([
        ["STUFE", "ÜBUNG", "SÄTZE × WDHLG.", "PAUSE", "HINWEIS"],
        ["1 — Grundzug Drücken", "Langhantel Bankdrücken", "1 TS × 5-6 + 3 RS × 8", "3-4 Min.", "Top-Satz: RPE 8-9. Rücksätze: -15% Last."],
        ["1 — Grundzug Ziehen",  "Langhantel Rudern (Pendlay)", "1 TS × 5 + 3 RS × 8", "3 Min.", "Volle Streckung, kontrolliertes Senken."],
        ["2 — DUP Drücken",      "Schrägbankdrücken (Maschine)", "3 × 10-12", "2,5 Min.", "Konstantspannung, kein Lockout."],
        ["2 — DUP Ziehen",       "Seilzug-Rudern eng", "3 × 10-12", "2,5 Min.", "Ellbogen eng am Körper führen."],
        ["3 — Isolation A",      "Seitheben (Kabel)", "3 × 15-20", "1,5 Min.", "Rest-Pause in letztem Satz möglich."],
        ["3 — Isolation B",      "Face Pulls", "3 × 15", "1,5 Min.", "Schulterstabilisierung. Nie weglassen."],
    ], [CONTENT_W*0.2, CONTENT_W*0.28, CONTENT_W*0.2, CONTENT_W*0.12, CONTENT_W*0.2]))
    s.append(sp(6))

    s.append(H3("Extremitäten A — Kniebeugedominant (Beispiel)"))
    s.append(mk_table([
        ["STUFE", "ÜBUNG", "SÄTZE × WDHLG.", "PAUSE", "HINWEIS"],
        ["1 — Grundzug Kniebeuge", "Langhantel Kniebeugen", "1 TS × 5 + 3 RS × 8", "4 Min.", "Top-Satz: wöchentliche Progression. Full depth."],
        ["2 — DUP Scharnier",      "RDL (Romanian Deadlift)", "3 × 10", "3 Min.", "Hüftscharnierend, Knie leicht gebeugt."],
        ["3 — Isolation A",         "Beinstrecker", "3 × 12-15", "2 Min.", "Maximale Kontraktion am Top halten."],
        ["3 — Isolation B",         "Beinbeuger liegend", "3 × 12-15", "2 Min.", "Langsam senken (3 Sek. Exzentrik)."],
        ["3 — Isolation C",         "Wadenheben stehend", "4 × 15-20", "1,5 Min.", "Volles ROM. Keine Hüpftechnik."],
    ], [CONTENT_W*0.2, CONTENT_W*0.28, CONTENT_W*0.2, CONTENT_W*0.12, CONTENT_W*0.2]))
    s.append(sp(6))

    s.append(H3("Ruhe / Arme / Bauch — Aktive Regeneration (Beispiel)"))
    s.append(mk_table([
        ["BEREICH", "ÜBUNG", "SÄTZE × WDHLG.", "PAUSE", "HINWEIS"],
        ["Bizeps",  "Kurzhantel Curls (Wechsel)", "3 × 12-15", "90 Sek.", "Keine Kompensation durch Rücken."],
        ["Trizeps", "Seil-Pushdowns",             "3 × 15",    "90 Sek.", "Ellbogen fixiert, volle Streckung."],
        ["Bizeps",  "Hammer Curls",               "2 × 12",    "90 Sek.", "Brachialis-Fokus."],
        ["Bauch",   "Kabelrotationen",            "3 × 12",    "60 Sek.", "Kontrolliert, kein Schwung."],
        ["Bauch",   "Ab-Wheel Rollout",           "3 × 8-10",  "90 Sek.", "Nur wenn Lendenwirbelkontrolle stabil."],
        ["Cardio",  "Leichtes Cardio (Zone 2)",   "20-30 Min.","—",       "Elliptical oder Fahrrad. Kein Laufen."],
    ], [CONTENT_W*0.15, CONTENT_W*0.3, CONTENT_W*0.2, CONTENT_W*0.12, CONTENT_W*0.23]))

    return s
