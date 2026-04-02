from reportlab.platypus import PageBreak, HRFlowable, Paragraph
from gflux_pdf.components import (
    sp, body, bul, H2, H3, callout, callout_bold, mk_table,
    section_break, formula,
)
from gflux_pdf.config import CONTENT_W, RULE


def _hr():
    return HRFlowable(width="100%", thickness=0.4, color=RULE, spaceAfter=8)


# ---------------------------------------------------------------------------
# Quick Reference Appendix (new content)
# ---------------------------------------------------------------------------

def _quick_reference() -> list:
    s = []
    s.append(H2("Schnellreferenz — Schlüsselformeln"))
    s.append(_hr())

    s.append(H3("EMA-Formel (Exponentieller Gleitender Durchschnitt)"))
    s.append(formula("EMA_heute = (Gewicht_heute × 0.25) + (EMA_gestern × 0.75)"))
    s.append(sp(4))
    s.append(body(
        "Starte den EMA mit dem tatsächlichen Gewicht am ersten Messtag. Führe die Berechnung "
        "täglich durch, immer morgens nüchtern nach dem Toilettengang. Erste aussagekräftige "
        "Tendenzaussage nach 7-10 Tagen, zuverlässige Protokollentscheidung nach 4 Wochen."
    ))
    s.append(sp(8))

    s.append(H3("Kalorienuntergrenze — Ausgangspunkt"))
    s.append(mk_table([
        ["VARIABLE", "FORMEL", "BEISPIEL"],
        ["Trainingstag (aktiver Beruf)",
         "Magermasse (kg) × 35 kcal",
         "88 kg Magermasse × 35 = 3.080 kcal Untergrenze"],
        ["Trainingstag (Bürojob)",
         "Magermasse (kg) × 32 kcal",
         "88 kg × 32 = 2.816 kcal Untergrenze"],
        ["Ruhetag (sitzend)",
         "Magermasse (kg) × 27-28 kcal",
         "88 kg × 27 = 2.376 kcal Untergrenze"],
    ], [CONTENT_W*0.3, CONTENT_W*0.4, CONTENT_W*0.3]))
    s.append(sp(8))

    s.append(H3("Cardio-Wiederauffüllung"))
    s.append(mk_table([
        ["AKTIVITÄT", "FORMEL", "BEISPIEL (80 kg Athlet)"],
        ["Laufen (eben)",      "1,0 kcal × kg × km",          "1,0 × 80 × 12 km = 960 kcal"],
        ["Laufen (mit Höhe)",  "+12% pro 150 m Aufstieg",      "960 + 115 = 1.075 kcal"],
        ["Elliptical/Rudern",  "Geräteanzeige × 0,85",         "700 kcal × 0,85 = 595 kcal"],
        ["Radfahren (drinnen)","Geräteanzeige × 0,75",         "600 kcal × 0,75 = 450 kcal"],
        ["Konditionsschaltkreis","Geräteanzeige × 0,90",       "300 kcal × 0,90 = 270 kcal"],
    ], [CONTENT_W*0.3, CONTENT_W*0.35, CONTENT_W*0.35]))
    s.append(sp(8))

    s.append(H3("Herzfrequenz-Zonen nach maximaler HF"))
    s.append(mk_table([
        ["ZONE", "% MAX. HF", "EMPFUNDENE ANSTRENGUNG", "G-FLUX EINSATZ"],
        ["Zone 1 — Sehr locker", "50-60%", "Problemlos sprechen, Erholung", "Aufwärmen, Cool-Down, aktive Pause"],
        ["Zone 2 — Locker",      "61-70%", "Komfortables Gespräch möglich", "Gros aller Cardio-Sessions (80%)"],
        ["Zone 3 — Moderat",     "71-80%", "Kurze Sätze möglich",           "Schwelle-Einstieg. Sparsam einsetzen."],
        ["Zone 4 — Hart",        "81-90%", "Einzelne Wörter nur",           "Schwellentraining, Tempoläufe (max. 20%)"],
        ["Zone 5 — Maximum",     "91-100%", "Nicht sprechen möglich",       "VO2max-Intervalle. Max. 1× / Woche."],
    ], [CONTENT_W*0.22, CONTENT_W*0.15, CONTENT_W*0.25, CONTENT_W*0.38]))
    s.append(sp(8))

    s.append(H3("Supplement-Timing Cheatsheet"))
    s.append(mk_table([
        ["ZEITPUNKT", "SUPPLEMENT", "DOSIS"],
        ["Frühstück (mit Essen)",
         "Berberin + R-Liponsäure + NAC + Zink-Picolinat",
         "500 / 200 / 600 / 25-30 mg"],
        ["Mittagessen / KH-Mahlzeit",
         "Berberin + CoQ10",
         "500 / 200 mg"],
        ["Größte Mahlzeit (Fett vorhanden)",
         "Omega-3 (Teil)",
         "0,5-1 g EPA/DHA"],
        ["Abendessen mit Essen",
         "Berberin + R-Liponsäure + Omega-3 (Rest)",
         "500 / 200 mg / Rest-Omega-3"],
        ["30-60 Min. vor Schlafen",
         "Magnesium-Glycinat + Apigenin + L-Theanin",
         "400 / 50 / 200 mg"],
        ["Täglich (beliebig)",
         "Selen (Macadamia-Nüsse)",
         "1-2 Nüsse"],
    ], [CONTENT_W*0.25, CONTENT_W*0.45, CONTENT_W*0.3]))

    return s


# ---------------------------------------------------------------------------
# Appendix A, B, C (companion volume teasers)
# ---------------------------------------------------------------------------

def _appendix_a() -> list:
    s = []
    s.append(H2("Anhang A — G-Flux Ernährung Band I"))
    s.append(_hr())
    s.append(body(
        "Ernährung ist die Variable, die bestimmt, ob das G-Flux System zu deinen Gunsten wirkt "
        "oder ins Stocken gerät. Das Trainingshandbuch gibt dir die Regeln. Dieser Band gibt dir "
        "die Werkzeuge zur präzisen Umsetzung — bei jedem Körpergewicht, über jeden Trainingsblock, "
        "für männliche und weibliche Athleten."
    ))
    s.append(sp(4))
    s.append(H3("Was enthalten ist"))
    for pt in [
        "Kalorienuntergrenze-Rechner: Bestimme deine exakte tägliche Kalorienuntergrenze basierend "
        "auf Körpergewicht, Magermasse, beruflichem NEAT und Aktivitätsniveau. Ausgearbeitete "
        "Beispiele für Athleten von 60 kg bis 120 kg, männlich und weiblich.",
        "Cardio-Wiederauffüllungstabellen: Vorberechnete Wiederauffüllungsziele für Laufdistanzen "
        "von 5 km bis 42 km, Elliptical, Rudern und Konditionsschaltkreise — nach Körpergewicht in "
        "5-kg-Schritten organisiert. Kein Kopfrechnen während des Trainingstags.",
        "Makro-Periodisierung über den 8-Wochen-Block: Protein-, Kohlenhydrat- und Fettzielanpassungen "
        "Woche für Woche bei steigendem Trainingsvolumen — inkl. Entlastungswoche-Ernährungsstrategie.",
        "Kohlenhydrat-Zyklusprotokolle: Wann hohe, mittlere und niedrigere Kohlenhydrattage innerhalb "
        "der Wochenstruktur einzusetzen sind.",
        "Mini-Cut-Ausführungsanleitung: Schritt-für-Schritt-Protokoll für die kontrollierte "
        "Defizitphase — Kalorienreduktionsplan und Austrittskriterien.",
        "Zyklusbasiertes Ernährungskapitel für Athletinnen: Vollständige Phasen-Ernährungsplanung "
        "für alle vier Zyklusphasen.",
        "Supplement-Zeitplan-Referenz: Vollständiger täglicher Zeitplan mit Dosierungsbegründung.",
    ]:
        s.append(bul(pt))
    s.append(sp(6))
    s.append(callout(
        "FÜR WEN DIESER BAND GEDACHT IST: Jeden Athleten, der über Schätzungen hinausgehen und in "
        "präzise, blockspezifische Ernährungsausführung einsteigen möchte. Besonders wertvoll für "
        "Athletinnen, Athleten im 80–120-kg-Bereich und alle, die zum ersten Mal einen Mini-Cut "
        "ohne Muskelverlust durchführen wollen."
    ))
    return s


def _appendix_b() -> list:
    s = []
    s.append(PageBreak())
    s.append(H2("Anhang B — G-Flux Übungsauswahl & Programm-Templates"))
    s.append(_hr())
    s.append(body(
        "Kapitel 04 dieses Handbuchs definiert die Bewegungsmuster-Logik. Dieser Band übersetzt "
        "diese Logik in vollständig ausgearbeitete Trainingspläne — Übung für Übung, Session für "
        "Session, Woche für Woche über den 8-Wochen-Block. Der Unterschied zwischen dem Verstehen "
        "des Systems und dem fertigen Plan vor dir."
    ))
    s.append(sp(4))
    s.append(H3("Was enthalten ist"))
    for pt in [
        "Übungsbibliothek nach Bewegungsmuster: Vollständiger Katalog nach Muster unterteilt nach "
        "Gerätebedarf, Gelenkstress-Profil und Könnensstand.",
        "Übungsrotationstabellen: Vorgefertigte A/B/C-Rotationssequenzen für Rumpf- und "
        "Extremitäten-Tage in verschiedenen Gerätekonfigurationen.",
        "9-Tage-Zyklus-Programm-Templates: Vollständige 8-Wochen-Programme mit Übungsauswahl, "
        "Satz-Zahlen, Wiederholungszielen und Last-Progressionsleitlinien.",
        "4-Tage-Ober-/Unterkörper-Templates: Dieselbe Blockstruktur auf 4-Tage-Wochenplan angepasst.",
        "3-Tage-Ganzkörper-Templates: Das Drei-Stufen-Schema in 3-Session-Woche komprimiert.",
        "Entlastungswoche-Templates: Session-für-Session-Entlastungspläne für alle drei Programmstrukturen.",
        "Gelenk- und Sehnen-Schutzanhang: Modifizierte Übungsauswahl für gängige Beschwerden.",
    ]:
        s.append(bul(pt))
    s.append(sp(6))
    s.append(callout(
        "FÜR WEN DIESER BAND GEDACHT IST: Athleten, die im Gym keine Zeit mehr mit Überlegen "
        "verschwenden wollen und Pläne brauchen, die sofort funktionieren. Unverzichtbar für "
        "Trainer, die das Protokoll mit Klienten anwenden."
    ))
    return s


def _appendix_c() -> list:
    s = []
    s.append(PageBreak())
    s.append(H2("Anhang C — G-Flux Konditionshandbuch"))
    s.append(_hr())
    s.append(body(
        "Kapitel 05 etabliert den Cardio-Rahmen. Das Konditionshandbuch geht mehrere Ebenen tiefer "
        "und verwandelt den Rahmen in ein strukturiertes, periodisiertes Konditionsprogramm, das "
        "parallel zum Krafttrainingsblock läuft."
    ))
    s.append(sp(4))
    s.append(H3("Was enthalten ist"))
    for pt in [
        "Zone-2-Kalibrierungsprotokoll: Wie du deine persönliche Zone-2-Grenze präzise ermittelst "
        "mittels Tempo, Herzfrequenz und Leistungsdaten.",
        "Laufleistungs-Zieltabellen: Zone-2-, Zone-3- und Schwellen-Leistungsziele in Watt nach "
        "Athleten-Körpergewicht organisiert.",
        "Wöchentliche Cardio-Struktur-Templates: Vorgefertigte Laufpläne für 30 km, 35 km, 40 km "
        "und 45 km Gesamtvolumen-Ziele.",
        "Cross-Training-Schaltkreisprogramme: Sechs sofort einsetzbare Konditionsschaltkreise nach "
        "Regenerationsbedarf kategorisiert.",
        "Plyometrisches Integrations-Protokoll: Strukturierter 4-wöchiger Einstieg für Athleten "
        "ohne Vorerfahrung im Explosivtraining.",
        "Wettkampfblock-Periodisierung: Vollständige 8-Wochen-Blockanpassungen für 5k, 10k oder "
        "Halbmarathon mit 2-wöchigem Taper-Protokoll.",
        "Wettkampftag-Ernährung: Kohlenhydrat-Ladeprotokoll, Mahlzeiten-Timing und "
        "Wiederauffüllungsprotokoll nach dem Wettkampf.",
        "Langstrecken-Vorbereitungsanleitung: Für Athleten, die über 15 km ausdehnen — "
        "Glykogenmanagement und Wiederauffüllungsberechnung für Distanzen über 20 km.",
    ]:
        s.append(bul(pt))
    s.append(sp(6))
    s.append(callout(
        "FÜR WEN DIESER BAND GEDACHT IST: Jeden Athleten, für den der Lauf- und Konditionsanteil "
        "genauso wichtig ist wie das Heben — insbesondere Athleten, die auf einen Wettkampf "
        "trainieren."
    ))
    return s


def _next_steps() -> list:
    s = [PageBreak()]
    s += section_break("—", "Nächste Schritte: Exekution")
    s.append(body(
        "Du hast nun die Blaupause, um das G-Flux-Protokoll auszuführen. Ausführung trennt "
        "Resultate von wertloser Theorie. Wer nur liest, stagniert."
    ))
    s.append(sp(6))
    s.append(callout_bold(
        "Wenn du die vollständige Automatisierung im Alltag möchtest (EMA-Tracking, präzise "
        "Kalorienberechnungen und strukturierte Templates): Nutze den CbTK G-Flux Tracker."
    ))
    s.append(sp(6))
    s.append(body(
        "Für 1-on-1 Coaching-Anfragen oder den direkten Zugang zum vollständigen System, nutze "
        "die offiziellen CbTK-Kanäle."
    ))
    return s


def build() -> list:
    s = [PageBreak()]
    s += section_break("—", "Anhang — Das G-Flux Kompendium")

    s.append(body(
        "Das Trainingshandbuch, das du gerade gelesen hast, liefert die unumstößliche Philosophie, "
        "die Architektur und die Regeln. Es überlädt dich absichtlich nicht mit hunderten Seiten an "
        "Templates und Makro-Rechnern, denn du musst zuerst verstehen, WARUM wir tun, was wir tun. "
        "Phase 3: Automatisierung & Skalierung."
    ))
    s.append(sp(6))

    s.append(H3("Weg 1: DIY (Do It Yourself)"))
    s.append(body(
        "Du nimmst die Regeln aus diesem Handbuch und baust dir deine 8-Wochen-Blöcke, deine "
        "Ernährungsperiodisierung und deine Cardio-Schaltkreise selbst zusammen. Das ist der harte, "
        "lehrreichste, aber auch zeitintensivste Weg."
    ))
    s.append(sp(4))

    s.append(H3("Weg 2: Die Paper Coaches (Anhänge A, B, C)"))
    s.append(body(
        "Die drei folgenden Kompendium-Bände fungieren als deine 'Paper Coaches'. Sie sind für "
        "Athleten, die kein 1-on-1 Coaching wollen, aber fertige, synergierende Systeme brauchen."
    ))
    s.append(sp(4))

    s.append(H3("Weg 3: CbTK 1-on-1 Online-Coaching"))
    s.append(body(
        "Totale Automatisierung und Eskalation für Athleten, die die Adaption hinter sich haben und "
        "ab jetzt maximale Output-Werte fordern, ohne sich um die Steuerung zu kümmern. Wir "
        "übernehmen die wöchentliche EMA-Analyse, die Kalorien-Eskalation, die Anpassung der "
        "Biomarker und die Modifikation der Templates an deinen Terminkalender."
    ))
    s.append(sp(8))

    # Quick Reference (new content)
    s += _quick_reference()
    s.append(sp(6))

    # Companion volume teasers
    s += _appendix_a()
    s += _appendix_b()
    s += _appendix_c()

    # Final page
    s += _next_steps()

    return s
