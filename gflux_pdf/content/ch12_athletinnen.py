from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, H2, female_box, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("12", "Besonderheiten für Athletinnen")

    s.append(body(
        "Das G-Flux Athleten-Protokoll gilt gleichermassen für Athletinnen mit einigen wichtigen "
        "Anpassungen für Hormonphysiologie, Körperzusammensetzungsschwellen und zyklische "
        "Stoffwechselveränderungen. Athletinnen, die mit ihrer Physiologie trainieren statt blind "
        "dagegen, erzielen weit überlegene Output-Werte."
    ))
    s.append(sp(6))

    s.append(H2("Körperfettschwellen"))
    s.append(mk_table([
        ["SCHWELLE", "MANN", "FRAU", "HINWEISE"],
        ["Einstiegsvoraussetzung",
         "Unter 15%", "Unter 22%",
         "Das essentielle Frauenfett (10-13%) ist physiologisch notwendig — kein Überschuss."],
        ["Aufbaudeckel",
         "15%", "22%",
         "Über dem Deckel werden Überschusskalorien bevorzugt gespeichert. Untergrenze zuerst anpassen."],
        ["Optimaler Arbeitsbereich",
         "10-14%", "17-22%",
         "Optimales Partitionierungsfenster für den G-Flux-Ansatz."],
        ["Gefahrenzone (zu mager)",
         "Unter 8%", "Unter 14%",
         "Leistung, Regeneration und Hormonfunktion verschlechtern sich rapide. Nicht von hier aus aufbauen."],
    ], [CONTENT_W*0.3, CONTENT_W*0.15, CONTENT_W*0.15, CONTENT_W*0.4]))
    s.append(sp(6))

    s.append(H2("Ernährungsanpassung nach Zyklusphasen"))
    s.append(body(
        "Der Menstruationszyklus erzeugt vorhersehbare Variationen in Stoffwechselrate, "
        "Brennstoffpräferenz, Regenerationskapazität und Hormonumfeld. Die Ernährung an die "
        "Zyklusphase anzupassen — statt sie zu ignorieren — verbessert Leistung und "
        "Körperzusammensetzung erheblich."
    ))
    s.append(sp(4))

    s.append(mk_table([
        ["ZYKLUSPHASE", "TAGE (ca.)", "ERNÄHRUNGSANPASSUNG", "TRAININGSHINWEISE"],
        ["Follikulärphase\n(nach Menstruation)",
         "Tag 1-13",
         "Standard G-Flux-Protokoll. Kohlenhydratverwertung ist hier absolut optimal. "
         "Geringerer Kalorienbedarf als in der Lutealphase.",
         "Leistung typischerweise am besten. Intensität und Kraft extrem fordern."],
        ["Ovulation",
         "Tag 14",
         "Standard-Protokoll beibehalten.",
         "Höchste Leistungsphase. Ideal für schwere Top-Sätze und PB's."],
        ["Lutealphase",
         "Tag 15-28",
         "Gesamtkalorien um 150-300 kcal erhöhen. Fett auf 35-40% der Nicht-Cardio-Kalorien "
         "steigern. Protein hoch. Kohlenhydrate können hoch bleiben.",
         "Regeneration kann langsamer sein. Gefühlte Anstrengung steigt. Intensität leicht "
         "reduzieren, wenn nötig - nicht durch übermäßige Ermüdung beissen."],
        ["Menstruationsphase",
         "Tag 1-5",
         "Erhöhte Fettaufnahme beibehalten. Omega-3 signifikant steigern. "
         "Kalorien am oberen Ende.",
         "Hochintensives Cardio bei starken Beschwerden reduzieren. Nur Zone 2. "
         "Krafttraining kann bei reduzierter Intensität weiterlaufen."],
    ], [CONTENT_W*0.25, CONTENT_W*0.15, CONTENT_W*0.3, CONTENT_W*0.3]))
    s.append(sp(6))

    # --- NEW CONTENT: Cycle-phase training intensity table ---
    s.append(H2("Trainingsintensität nach Zyklusphase"))
    s.append(body(
        "Die folgende Tabelle gibt konkrete Empfehlungen für Krafttraining, Cardio-Intensität und "
        "Erholung in jeder Zyklusphase. Nutze sie als Orientierung — individuelle Unterschiede "
        "können erheblich sein. Tracking über mehrere Zyklen ist notwendig, um das eigene Muster "
        "zuverlässig zu erkennen."
    ))
    s.append(sp(4))

    s.append(mk_table([
        ["PHASE", "KRAFTTRAINING", "CARDIO", "ERHOLUNG", "BESONDERHEIT"],
        ["Follikulär\n(T.1-13)",
         "Maximale Intensität. Schwere Top-Sätze. PB-Versuche ansetzen.",
         "Zone 2 + Schwelle möglich. Volles Protokoll.",
         "Normal. Kurze Regenerationszeit.",
         "Östrogen fördert Muskelproteinsynthese und Geweberegeneration."],
        ["Ovulation\n(T.14)",
         "Höchste Kraft und Motivation. Ideal für neue Bestleistungen.",
         "Volle Intensität. VO2max-Intervalle möglich.",
         "Sehr gut.",
         "Peak-Östrogen. Bindegewebe etwas anfälliger — auf Aufwärmen achten."],
        ["Luteal\n(T.15-28)",
         "Etwas reduzierte Intensität. RPE-8 statt RPE-9 bei Top-Sätzen.",
         "Zone 2 dominant. Schwelle nur an guten Tagen.",
         "Länger. Mehr Schlaf einplanen.",
         "Progesteron erhöht Körperkerntemperatur. Mehr Pausen. Mehr Wasser trinken."],
        ["Menstruation\n(T.1-5)",
         "Reduziert. Fokus auf Technik und Qualität statt Last.",
         "Nur Zone 2 oder leichtes Cross-Training. Kein Intensitätswork.",
         "Priorität. Schlaf maximieren.",
         "Prostaglandine verursachen Entzündungsreaktion. Omega-3 und Magnesium priorisieren."],
    ], [CONTENT_W*0.18, CONTENT_W*0.24, CONTENT_W*0.2, CONTENT_W*0.18, CONTENT_W*0.2]))
    s.append(sp(6))

    s.append(female_box(
        "PROTEIN-HINWEIS FÜR ATHLETINNEN: Aktuelle Forschung deutet darauf hin, dass Athletinnen "
        "in der Follikulärphase eher den unteren Bereich von 1,8-2,3 g/kg benötigen und in der "
        "Lutealphase eher den oberen — durch höheren Proteinabbau. Der Gesamtbedarf kann 5-10% "
        "höher als bei männlichen Äquivalenten je kg Magermasse liegen, um Hormongesundheit und "
        "Regeneration zu unterstützen."
    ))
    s.append(sp(6))

    s.append(H2("Gewichtsschwankungen bei Athletinnen"))
    s.append(body(
        "Athletinnen können im Laufe des Menstruationszyklus Waagenschwankungen von 1-3 kg erleben "
        "— bedingt durch hormonelle Wassereinlagerung, besonders in der Lutealphase. Das ist normal, "
        "erwartet und definitiv kein Fettmassenzuwachs. Das EMA-Tracking kompensiert dies "
        "automatisch durch Glättung über 7 Tage. Nicht mit Kalorienreduktion auf prämenstruelle "
        "Waageanstiege reagieren — das ist die schlechteste mögliche Reaktion auf eine hormonelle "
        "Wasserschwankung."
    ))

    return s
