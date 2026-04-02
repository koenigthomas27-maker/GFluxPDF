from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, H2, callout, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("07", "Insulinsensitivität & Supplementierung")

    s.append(body(
        "Insulinsensitivität ist der metabolische Schlüsselmechanismus des G-Flux-Protokolls. "
        "Bei hoher Sensitivität fließen Kohlenhydrate bevorzugt ins Muskelglykogen und in anabole "
        "Signalwege statt ins Fettgewebe. Die Kombination aus hohem Ausdauervolumen und gezielter "
        "Supplementierung erzeugt eine kraftvolle, nachhaltige Verbesserung der Insulinsensitivität, "
        "die den kohlenhydratreichen Ansatz dieses Protokolls erst effektiv macht. Das ist die "
        "biochemische Infrastruktur deines Erfolgs."
    ))
    s.append(sp(4))

    s.append(H2("Wie Ausdauertraining die Insulinsensitivität verbessert"))
    s.append(body(
        "Aerobes Training erhöht direkt die Dichte der GLUT4-Glukosetransporter in der "
        "Skelettmuskulatur — die Proteine, die Glukose aus dem Blut in die Muskelzellen ziehen. "
        "Höhere GLUT4-Dichte bedeutet: Mehr Kohlenhydrate werden mit weniger Insulin ins "
        "Muskelgewebe aufgenommen. Dieser Effekt ist akut (hält 24-72 Stunden nach jeder Session "
        "an) und chronisch (strukturelle Anpassung über Wochen). Deshalb ist der Cardio-Anteil "
        "metabolische Infrastruktur, kein optionales Konditionswork."
    ))
    s.append(sp(6))

    s.append(H2("Tägliches Supplement-Protokoll"))
    s.append(body(
        "Timing ist entscheidend. Die Interaktion der Wirkstoffe mit Nährstoffen (insbesondere Fett "
        "und Kohlenhydraten) bestimmt die Absorptionsrate und die Insulinsensibilisierung."
    ))
    s.append(sp(4))

    s.append(mk_table([
        ["SUPPLEMENT", "DOSIS", "ZEITPUNKT", "FUNKTION / FOKUS"],
        ["Berberin",
         "500 mg × 3",
         "Mit jeder KH-reichen Mahlzeit",
         "AMPK-Aktivierung — ähnlich wie Metformin. Leitet Glukose ins Muskelgewebe, verbessert Lipidprofil."],
        ["R-Liponsäure (Na-RALA)",
         "200 mg × 2",
         "Frühstück + Abendessen mit Essen",
         "Synergistischer Insulinsensibilisator. Starkes Antioxidans, reduziert trainingsbedingten oxidativen Stress."],
        ["NAC (N-Acetylcystein)",
         "600 mg",
         "Frühstück mit Essen",
         "Glutathion-Vorläufer. Leberschutz, oxidativer Stress, Unterstützung der Atemwege."],
        ["CoQ10 (+ BioPerine)",
         "200 mg",
         "Größte Mahlzeit (Fett vorhanden)",
         "Mitochondriale ATP-Produktion, Herzgesundheit. BioPerine erhöht die Aufnahme erheblich."],
        ["Omega-3 (EPA+DHA)",
         "1,5-2 g EPA/DHA täglich",
         "Aufgeteilt auf 2-3 Mahlzeiten",
         "Entzündungshemmend, Herzgesundheit, Muskelproteinsynthese-Unterstützung."],
        ["Zink-Picolinat",
         "25-30 mg",
         "Frühstück mit Essen",
         "Hormonelle Unterstützung, Immunfunktion, Regenerations-Kofaktor."],
        ["Magnesium-Glycinat",
         "400 mg",
         "30-60 Min. vor dem Schlafen",
         "GABA-Aktivierung, Tiefschlafqualität, Kortisol-Reduktion."],
        ["Apigenin",
         "50 mg",
         "30-60 Min. vor dem Schlafen",
         "GABA-A-Rezeptor-Bindung, Einschlaf-Tempo, entzündungshemmend."],
        ["L-Theanin",
         "200 mg",
         "30-60 Min. vor dem Schlafen",
         "Alpha-Wellen-Induktion, ZNS-Beruhigung, Schlafpuls-Senkung."],
        ["Selen (Macadamia)",
         "1-2 Nüsse täglich",
         "Jederzeit",
         "Schilddrüse, Antioxidans, Immunsystem. Nahrungsquelle ist hierbei ausreichend."],
    ], [CONTENT_W * 0.22, CONTENT_W * 0.18, CONTENT_W * 0.25, CONTENT_W * 0.35]))
    s.append(sp(6))

    s.append(callout(
        "SYNERGIE: Berberin + R-Liponsäure zusammen zu kohlenhydratreichen Mahlzeiten aktivieren "
        "das Glukosemanagement gleichzeitig über zwei verschiedene Signalwege. Kombiniert mit "
        "GLUT4-Hochregulation durch Ausdauertraining wird die Kohlenhydrat-Verteilung ins "
        "Muskelgewebe deutlich effizienter als durch jede einzelne Maßnahme allein."
    ))

    return s
