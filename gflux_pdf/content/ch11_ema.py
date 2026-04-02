from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, bul, H2, callout, formula, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("11", "EMA, Check-Ins & Gewichtsschwankungen")

    s.append(body(
        "Tägliche Gewichtsschwankungen bei einem hochvolumigen, kohlenhydratreichen Athleten sind "
        "dramatisch und vollkommen normal. Ein Athlet, der die Physiologie hinter diesen "
        "Schwankungen nicht versteht, wird auf Basis bedeutungsloser Tagesrauschen falsche "
        "Protokollanpassungen vornehmen. Die tägliche Zahl wird protokolliert — niemals isoliert "
        "bewertet. Die Waage lügt, die Mathematik nicht."
    ))
    s.append(sp(6))

    s.append(H2("Exponentieller gleitender Durchschnitt (EMA)"))
    s.append(body(
        "Alle Gewichtsanalysen nutzen einen 7-tägigen exponentiellen gleitenden Durchschnitt (EMA), "
        "der aktuellen Daten mehr Gewicht gibt als älteren. Der EMA filtert Glykogen-, Wasser- und "
        "Verdauungstraktschwankungen heraus und zeigt den echten Trend von Muskel- und "
        "Fettmassenveränderung. Mindestens 4-Wochen-EMA-Fenster sind erforderlich, bevor "
        "Kalorienkorrekturen vorgenommen werden."
    ))
    s.append(sp(6))

    s.append(H2("Der EMA in der Praxis"))
    s.append(body(
        "Das tägliche Gewicht lügt. Ein kohlenhydratreicher Refeed zieht Wasser. Eine harte "
        "Beinsession verursacht lokale Entzündungen und speichert Flüssigkeit. Wer darauf mit Panik "
        "und Kalorienkürzung reagiert, sabotiert seinen eigenen Fortschritt. Wir nutzen den "
        "7-Tage-EMA, um das Rauschen herauszufiltern. Die Formel gewichtet das heutige Gewicht zu "
        "25% und den bisherigen Trend zu 75%:"
    ))
    s.append(sp(4))
    s.append(formula("EMA_heute = (Gewicht_heute × 0.25) + (EMA_gestern × 0.75)"))
    s.append(sp(4))
    s.append(body(
        "<b>Beispiel:</b> Ein 85 kg schwerer Athlet isst massive Mengen Kohlenhydrate. Sein "
        "EMA_gestern lag bei exakt 85.0 kg. Am nächsten Morgen zeigt die Waage durch Glykogen und "
        "Wasser plötzlich 86.2 kg. Sein Kopf sagt ihm: 'Ich werde fett.' Der EMA sagt die absolute "
        "Wahrheit: (86.2 × 0.25) + (85.0 × 0.75) = 21.55 + 63.75 = 85.3 kg. Der Ausreißer wird "
        "geglättet. Der Trend bleibt stabil."
    ))
    s.append(sp(6))

    s.append(H2("Quellen täglicher Gewichtsschwankungen"))
    s.append(mk_table([
        ["QUELLE", "TYPISCHER BEREICH", "ZEITRAUM"],
        ["Glykogenauffüllung (nach kohlenhydratreichem Tag)", "+0,8-1,5 kg", "12-24 Stunden"],
        ["Intramuskuläres Wasser (an Glykogen gebunden, 1:3)",  "+0,8-1,5 kg", "12-36 Stunden"],
        ["Verdauungstraktinhalt (Nahrung im System)",            "+0,5-1,5 kg", "8-16 Stunden"],
        ["Natriumbedingte extrazelluläre Wassereinlagerung",    "+0,3-0,8 kg", "12-48 Stunden"],
        ["Hormonelle Wasserschwankungen (Frauen: Lutealphase)", "+0,3-2,0 kg", "Variabel - zyklusabhängig"],
        ["GESAMTE MÖGLICHE TAGESSCHWANKUNG",
         "Bis zu 5-6 kg",
         "Kein Fettmassenzuwachs. Vollständig reversibel."],
    ], [CONTENT_W*0.5, CONTENT_W*0.25, CONTENT_W*0.25], accent_rows={5}))
    s.append(sp(6))

    s.append(H2("Morgen-Check-in-Protokoll"))
    for pt in [
        "Rohes Waage-Gewicht — ins Tracking-Sheet eintragen, nicht handeln.",
        "EMA-Aktualisierung — der einzig maßgebliche Wert für Protokollentscheidungen.",
        "HRV aus Nachtdaten.",
        "Ruhepuls.",
        "Schlafpuls.",
        "Morgenphysik-Foto — Vorder-, Seiten- und Rückansicht zur Gewebequalitätsbeurteilung.",
        "Subjektive Erholungsbewertung (1-10) als sekundärer Kontext.",
    ]:
        s.append(bul(pt))
    s.append(sp(6))

    s.append(callout(
        "VISUELLE DATEN HABEN VORRANG VOR WAAGE-DATEN: Zeigt die Waage einen Anstieg, aber das "
        "Morgenfoto zeigt volle Muskeln, sichtbare Trennungen und keine neue Weichheit — die Waage "
        "zeigt Glykogen und Wasser, kein Fett. Ist die Waage stabil, aber die Muskeln sehen flach "
        "und entleert aus, müssen die Kalorien steigen, unabhängig von der Zahl auf dem Display. "
        "Die Kamera und die Biomarker sagen die Wahrheit. Die tägliche Waagenzahl ist Kontext, "
        "kein Urteil."
    ))
    s.append(sp(6))
    s.append(body(
        "Phase 2: Die Optimierung. Diese Mathematik ist mächtig, aber sie erfordert tägliche "
        "Disziplin. In den ersten vier Wochen der Adaptionsphase solltest du sie händisch "
        "durchführen, um die Ursache-Wirkungs-Mechanismen deines Körpers zu begreifen. Du verstehst "
        "nun die Fluktuationen. Wer den administrativen Aufwand eliminieren und die absolute "
        "Präzision will, lagert diese Mathematik im nächsten Schritt an den automatisierten "
        "CbTK-Tracker aus."
    ))

    return s
