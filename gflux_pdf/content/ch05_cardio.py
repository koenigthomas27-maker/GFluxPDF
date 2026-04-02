from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, note, H2, callout_bold, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("05", "Cardio & Cross-Training-Protokoll")

    s.append(H2("Wöchentliches Laufvolumen"))
    s.append(body(
        "Das Laufvolumen beginnt für neue Athleten oder nach einer Pause bei strikt 10 km pro Woche. "
        "Dies etabliert die aerobe Basis. Es wird progressiv gesteigert — maximal 10% pro Woche. "
        "Der Zielkorridor für gut angepasste G-Flux-Athleten liegt bei 30–45 km."
    ))
    s.append(body(
        "Es gibt kein hartes Limit nach oben, solange die Regeneration stimmt. In speziellen "
        "Wettkampfblöcken kann dies massiv gesteigert werden. Das Laufvolumen ist immer den "
        "Regenerationsdaten untergeordnet — Biomarker-Signale haben absoluten Vorrang vor "
        "Volumenzielen. Cardio ist dein Motor, nicht dein Fettkiller."
    ))
    s.append(sp(6))

    s.append(mk_table([
        ["CARDIO-TYP", "INTENSITÄT", "PLATZIERUNG", "ZWECK"],
        ["Lockerer Lauf — Zone 2",
         "55–75 % max. HF\nKonversationstempo",
         "An beliebigen Nicht-Extr.- oder Ruhetagen",
         "Aerobe Grundlagenentwicklung. GLUT4-Hochregulation. Gros des Volumens."],
        ["Schwellentraining / Tempo",
         "85–92 % max. HF\nKomfortabel hart",
         "An Extremitäten-Tagen stapeln (vor Ruhetag)",
         "Verbesserung der Laktatschwelle. Laufeffizienz."],
        ["Intervalle / VO2max",
         "93–100 % max. HF\nMaximale Belastung",
         "Nur an Extremitäten-Tagen (max 1x/Woche)",
         "VO2max-Decke anheben. Anaerobe Kapazität. Sparsam einsetzen."],
        ["Wettkampf- / Tempoläufe",
         "Spez. Renntempo\n(je nach Wettkampf)",
         "An Extremitäten-Tagen stapeln",
         "Erforderlich im Wettkampfblock. Kraftintensität bleibt hoch; Volumen reduziert."],
    ], [CONTENT_W * 0.25, CONTENT_W * 0.25, CONTENT_W * 0.25, CONTENT_W * 0.25]))
    s.append(sp(6))

    s.append(callout_bold(
        "80/20-REGEL: 80% des wöchentlichen Cardio-Volumens bleibt zwingend in Zone-2-Intensität "
        "(locker). Nur 20% auf Höhe der Schwelle oder darüber. Eine Verletzung dieses Verhältnisses "
        "akkumuliert toxische ZNS-Ermüdung, zerstört die Krafttrainingsqualität und blockiert die "
        "Superkompensation ohne verhältnismäßigen aeroben Nutzen."
    ))
    s.append(sp(4))
    s.append(body(
        "Hier entscheidet sich, ob du Kapazität aufbaust oder Ermüdung akkumulierst."
    ))
    s.append(sp(6))

    s.append(H2("Cross-Training — Mehr als nur Elliptical"))
    s.append(body(
        "Cardio außerhalb des Laufens beschränkt sich nicht auf stetes Maschinentraining. "
        "Cross-Training-Sessions können je nach Regenerationszustand und Ziel als "
        "Konditionsschaltkreise strukturiert werden. Leistungsstarke Athleten finden kurze, intensive "
        "Konditionsschaltkreise oft zeiteffizienter als 45 Minuten Zone-2-Elliptical."
    ))
    s.append(sp(4))

    s.append(mk_table([
        ["CROSS-TRAINING-ART", "FORMAT", "REGENERATIONSKONTEXT", "DAUER"],
        ["Gleichmäßiges Cardio\n(Elliptical / Rudern / Rad)",
         "Kontinuierliche Zone-2-Belastung",
         "Optimal bei mittlerer bis niedriger Regeneration. Geringer ZNS-Aufwand. Rein aerob.",
         "30-60 Min."],
        ["Konditionsschaltkreis\n(Carries / Swings / Seile)",
         "Arbeits-/Pausenintervalle z.B. 40s/20s\n3-5 Stationen rotieren",
         "Wenn Energie hoch und ein Kraft-Cardio-Mix gewünscht ist. Höherer ZNS-Aufwand.",
         "15-25 Min."],
        ["Plyometrisches Konditionieren\n(Box-Jumps / Bounds)",
         "Geringes Volumen, explosiv.\nMax. 3 Sätze à 3-5 Wdhlg.",
         "Nur bei starken Biomarkern (HRV hoch). ZNS-Primer vor Grundzügen. Erhöht motorische Rekrutierung.",
         "10-20 Min."],
        ["Kettlebell / Barbell-Komplex",
         "Fließende Sequenzen. Mittlere Last, geringe Pause",
         "Exzellentes Stoffwechsel-Konditionieren. Nicht am Tag vor schwerem Unterkörper.",
         "15-30 Min."],
    ], [CONTENT_W * 0.25, CONTENT_W * 0.25, CONTENT_W * 0.35, CONTENT_W * 0.15]))
    s.append(sp(6))

    s.append(H2("Kalorien-Wiederauffüllung (Cardio Re-Eat)"))
    s.append(body(
        "Jede durch Cardio verbrannte Kalorie wird zusätzlich zur Untergrenze gegessen. Die "
        "Berechnung nutzt das Körpergewicht in kg als primäre, unverfälschte Variable."
    ))
    s.append(sp(4))

    s.append(mk_table([
        ["METHODE", "FORMEL", "BEISPIEL MANN (104 kg)", "BEISPIEL FRAU (68 kg)"],
        ["Laufen",
         "1 kcal × Gewicht (kg) × km",
         "104 × 10 km = 1.040 kcal ZUSÄTZLICH",
         "68 × 10 km = 680 kcal ZUSÄTZLICH"],
        ["Höhenkorrektur",
         "+10-15% pro 150 m Aufstieg",
         "1.040 + 156 = ca. 1.200 kcal",
         "680 + 102 = ca. 780 kcal"],
        ["Elliptical / Maschinen",
         "Geräte-Output × 0,85",
         "800 kcal Gerät = ca. 680 kcal effektiv",
         "500 kcal Gerät = ca. 425 kcal effektiv"],
        ["Krafttraining",
         "Abgedeckt durch Untergrenze",
         "Nicht separat wiederauffüllen",
         "Nicht separat wiederauffüllen"],
    ], [CONTENT_W * 0.2, CONTENT_W * 0.25, CONTENT_W * 0.3, CONTENT_W * 0.25]))
    s.append(sp(4))
    s.append(note(
        "Geräte-Algorithmen unterschätzen den Kalorienverbrauch schwererer Athleten systematisch. "
        "Die 1-kcal/kg/km-Methode ist durch Leistungsdaten validiert und weitaus genauer als "
        "handgelenkbasierte Schätzungen."
    ))
    s.append(sp(4))
    s.append(body(
        "Wer den Calorie Re-Eat nicht täglich manuell tracken will: Der CbTK-Tracker berechnet "
        "die Wiederauffüllung automatisch nach Aktivität, Gewicht und Cardio-Art."
    ))
    s.append(sp(4))
    s.append(body(
        "Cardio verbessert Insulinsensitivität. Insulinsensitivität macht Kohlenhydrate anaboler. "
        "Das ist keine Empfehlung — das ist Mechanismus."
    ))
    s.append(sp(8))
    s.append(callout_bold(
        "HÄUFIGE FEHLER — CARDIO<br/><br/>"
        "— <b>Zu oft Intervalle einbauen:</b> Das ZNS akkumuliert toxische Ermüdung. "
        "Kraftqualität kollabiert. Das 80/20-Verhältnis existiert aus einem Grund.<br/>"
        "— <b>Cardio-Kalorien nicht zurückessen:</b> Du trainierst deinen Körper, Energie zu sparen, "
        "nicht zu nutzen. Der Muskelaufbau stoppt.<br/>"
        "— <b>Volumen zu schnell steigern:</b> Sehnen adaptieren langsamer als Muskulatur. "
        "Das Ergebnis sind strukturelle Verletzungen, kein Fortschritt.<br/>"
        "— <b>Hartes Cardio an Rumpf-Tagen stapeln:</b> Die Regeneration für den nächsten "
        "schweren Tag ist damit zerstört."
    ))
    s.append(sp(6))
    s.append(callout_bold(
        "EXEKUTION — KAPITEL 05<br/><br/>"
        "— Starte bei 10 km/Woche. Nicht mehr.<br/>"
        "— Steigere maximal 10% pro Woche.<br/>"
        "— 80% des Volumens bleibt Zone 2. Kein Verhandeln.<br/>"
        "— Hartes Cardio ausschließlich an Extremitäten-Tagen stapeln.<br/>"
        "— Jede Cardio-Kalorie wird zur Untergrenze hinzugegessen. Keine Ausnahmen."
    ))

    return s
