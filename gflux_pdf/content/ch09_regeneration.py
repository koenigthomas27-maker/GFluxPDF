from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, bul, H2, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("09", "Biomarker-Überwachung & Regeneration")

    s.append(body(
        "Regenerationsentscheidungen werden gnadenlos datenbasiert getroffen. Die folgenden "
        "Biomarker werden täglich verfolgt und steuern Trainingsintensität, Entlastungszeitpunkt "
        "und Kalorienkorrekturen. Die Prioritätsreihenfolge spiegelt Zuverlässigkeit und "
        "Handlungsrelevanz jedes Markers wider."
    ))
    s.append(sp(4))

    s.append(mk_table([
        ["PRIORITÄT", "BIOMARKER", "SIGNAL", "MAßNAHME"],
        ["1 — Kritisch",
         "HRV (Herzfrequenzvariabilität)",
         "Stabil oder steigend von persönlicher Baseline",
         "Abfall > 10% über 2+ Tage: Intensität reduzieren, Kalorien prüfen, frühzeitige "
         "Entlastung erwägen."],
        ["2 — Kritisch",
         "Ruhepuls",
         "Max. 5 Schläge über persönlicher Baseline und stabil",
         "Erhöhter Ruhepuls = systemischer Stress. Erst Kalorien erhöhen. Dann "
         "Sessionintensität reduzieren."],
        ["3 — Hoch",
         "Schlafpuls",
         "Niedrig und stabil",
         "Erhöhter Schlafpuls = autonomer Stress. Schlaf-Stack priorisieren. "
         "Trainingsbelastung reduzieren."],
        ["4 — Hoch",
         "Ermüdungslevel-Trend",
         "Gradueller Aufbau, dann scharfer Abfall in Entlastungswoche",
         "Unkontrollierter Ermüdungsanstieg ohne Plateaubildung = Entlastungssignal unabhängig "
         "von der Zykluswoche."],
        ["5 — Unterstützend",
         "Subjektive Bereitschaft",
         "Sollte mit obigen Markern korrelieren",
         "Nur als Bestätigung nutzen. Daten haben absoluten Vorrang vor dem Gefühl in beide Richtungen."],
        ["Ignorieren",
         "BioCharge / Geräte-Bereitschaft",
         "Häufig durch historische Daten und NEAT-Fehlklassifikation verfälscht",
         "Nicht für Protokollentscheidungen nutzen. HRV und Ruhepuls sind die verlässlichen Signale."],
    ], [CONTENT_W*0.15, CONTENT_W*0.25, CONTENT_W*0.25, CONTENT_W*0.35]))
    s.append(sp(6))

    s.append(H2("Ungeplante Entlastungsauslöser"))
    s.append(body(
        "Sofortige Volumenreduktion — unabhängig von der aktuellen Zyklusposition — bei einem der "
        "folgenden Faktoren:"
    ))
    for pt in [
        "HRV fällt über 3+ aufeinanderfolgende Tage um mehr als 15% unter die persönliche Baseline.",
        "Ruhepuls um mehr als 8 Schläge über Baseline ohne Krankheit.",
        "Schlafpuls konstant über 80 bpm bei einem nicht schlafmangel-geplagten Athleten.",
        "Grundzug-Leistung sinkt über 10% von der jüngsten Baseline ohne erklärliche Ursache.",
        "Sehnen- oder Gelenkempfindlichkeit steigt massiv statt sich zwischen Sessions zu stabilisieren.",
    ]:
        s.append(bul(pt))
    s.append(sp(6))

    s.append(H2("Krankheit & Trainingsausfall"))
    s.append(body(
        "Krankheit ist keine Deload-Woche. Krankheit ist ein Systemausfall. Wenn das Immunsystem "
        "kämpft, wird das Training sofort pausiert. Du reduzierst deine Kalorien auf die sitzende "
        "Untergrenze (Sedentary Baseline). Du erzeugst jedoch KEIN Defizit. Der Körper braucht "
        "Nährstoffe, um sich zu erholen und zellulär zu reparieren. Sich während einer Krankheit "
        "herunterzuhungern, garantiert den katabolen Verlust von hart erarbeitetem Muskelgewebe."
    ))

    return s
