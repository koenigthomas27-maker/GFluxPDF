from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, H2, callout_bold, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("10", "Mini-Cut-Protokoll")

    s.append(body(
        "Wenn der Körperfettanteil sich dem Deckelwert nähert (15% männlich / 22% weiblich), wird "
        "eine Mini-Cut-Phase eingeleitet, bevor der Überschuss fortgesetzt wird. Priorität ist die "
        "Erhaltung athletischer Leistungsfähigkeit und Schutz von metabolisch aktivem Gewebe — nicht "
        "die Geschwindigkeit des Fettabbaus. Ein Mini-Cut ist eine temporäre, kontrollierte Reduktion "
        "über Wiederauffüllungsprozentsätze — niemals aggressive Kalorienrestriktion."
    ))
    s.append(sp(6))

    s.append(mk_table([
        ["VARIABLE", "AUFBAU-EINSTELLUNG", "MINI-CUT-ANPASSUNG"],
        ["Cardio-Wiederauffüllung",
         "100% der verbrannten Kalorien",
         "60-70% der Cardio-Kalorien aufnehmen. Zwingt den Körper ans Fett."],
        ["Cardio-Volumen",
         "Volles Protokoll (30-45 km+)",
         "Um 10-20% reduzieren. Bei erhaltener Leistung kann es höher bleiben."],
        ["Cardio-Intensität",
         "Zone 2 dominant + Schwelle an Extremitäten-Tagen",
         "Nur Zone 2 während Defizit. Keine Intervalle oder Tempoarbeit — bes. bei "
         "hochkapazitätsgewohnten Athleten (schützt das ZNS)."],
        ["Trainingsvolumen",
         "Volle 8-Wochen-Zyklusprogression",
         "Um 1 Satz je Stufe reduzieren. Isolationen zuerst entfernen. Grundzüge bedingungslos schützen."],
        ["Minimales Defizit",
         "Entfällt",
         "Niemals mehr als 500 kcal unter den täglichen Gesamtverbrauch (TDEE)."],
        ["Protein",
         "1,8-2,3 g/kg Magermasse",
         "Beibehalten. Bei starkem Hungergefühl am oberen Ende orientieren, um Muskulatur zu "
         "schützen. Kein massiver Überschuss nötig."],
        ["Dauer",
         "Entfällt",
         "Maximal 2-4 Wochen vor Rückkehr zum Überschuss."],
    ], [CONTENT_W*0.25, CONTENT_W*0.35, CONTENT_W*0.4]))
    s.append(sp(6))

    s.append(callout_bold(
        "LEISTUNG IST DER REGULATOR: Wenn die Cardio-Leistung — Tempo, Leistungsoutput, gefühlte "
        "Anstrengung bei gegebenem Tempo — im Mini-Cut signifikant sinkt, wird das Cardio-Volumen "
        "sofort reduziert. Laufvolumen im Defizit auf Kosten der Output-Qualität zu jagen ist "
        "extrem destruktiv. Ein Athlet mit hoher aerober Basiskapazität schützt diese am besten, "
        "indem er lockerer und kürzer läuft, nicht härter."
    ))

    return s
