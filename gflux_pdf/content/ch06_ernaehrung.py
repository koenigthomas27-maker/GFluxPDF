from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, H2, callout_bold, female_box, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("06", "Ernährungsrahmen")

    s.append(H2("Die Kalorienuntergrenze"))
    s.append(body(
        "Die Kalorienuntergrenze ist die tägliche Mindestaufnahme vor jeder Cardio-Wiederauffüllung. "
        "Sie deckt Grundumsatz, berufliches NEAT, den thermischen Effekt der Nahrung und den massiven "
        "Stoffwechselaufwand schweren Krafttrainings ab. Ein grober Ausgangspunkt: 35 kcal pro kg "
        "Magermasse für Athleten mit hoher täglicher Aktivität."
    ))
    s.append(sp(4))

    s.append(mk_table([
        ["SZENARIO", "UNTERGRENZE MANN (104 kg)", "UNTERGRENZE FRAU (68 kg)",
         "GESAMT BEISPIEL (+ 10 km Lauf)"],
        ["Hohes NEAT — aktiver Beruf, Trainingstag",
         "ca. 3.600 kcal", "ca. 2.380 kcal",
         "M: ca. 4.700 kcal / F: ca. 3.060 kcal"],
        ["Mittleres NEAT — Trainingstag",
         "ca. 3.400 kcal", "ca. 2.200 kcal",
         "M: ca. 4.500 kcal / F: ca. 2.880 kcal"],
        ["Geringe Aktivität — sitzender Ruhetag",
         "ca. 3.000-3.200 kcal", "ca. 1.900-2.100 kcal",
         "Nur Untergrenze — keine Wiederauffüllung"],
    ], [CONTENT_W * 0.3, CONTENT_W * 0.25, CONTENT_W * 0.2, CONTENT_W * 0.25]))
    s.append(sp(6))
    s.append(body(
        "Wer die Untergrenze unterschreitet, zerstört den Mechanismus, bevor das erste schwere "
        "Training beginnt."
    ))
    s.append(sp(6))

    s.append(H2("Makronährstoff-Rahmen"))
    s.append(body(
        "Protein und Kohlenhydrate sind die primären Stellschrauben. Fett folgt sekundär, sobald "
        "Protein- und Kohlenhydratziele kompromisslos erfüllt sind."
    ))
    s.append(sp(4))

    s.append(mk_table([
        ["MAKRO", "ZIEL MANN", "ZIEL FRAU", "HINWEISE"],
        ["Protein",
         "1,8-2,3 g/kg Magermasse\n(z.B. 104 kg = 187-239 g)",
         "1,8-2,3 g/kg Magermasse\n(z.B. 68 kg = 122-156 g)",
         "Höheres Ende bei hohem Trainingsvolumen. Über 2,3 g/kg ist meist unnötig und teuer "
         "ohne Zusatznutzen."],
        ["Kohlenhydrate",
         "Primärer Kalorienträger\nKeine feste Obergrenze",
         "Primärer Kalorienträger\nKeine feste Obergrenze",
         "Rund ums Training vorziehen. Schnellverdauliche Quellen vor der Session. Größte "
         "KH-Mahlzeiten direkt nach dem Training für maximale Glykogensynthese."],
        ["Fett",
         "Moderat — folgt Protein und KH\nca. 25-35 % der Restkalorien",
         "Etwas höher — ca. 30-40 %\nBes. in der Menstruationsphase",
         "Fett-Timing: Ausschließlich abends, nach dem Training oder kohlenhydratarme Mahlzeiten."],
    ], [CONTENT_W * 0.15, CONTENT_W * 0.25, CONTENT_W * 0.25, CONTENT_W * 0.35]))
    s.append(sp(6))

    s.append(callout_bold(
        "TRENNUNGS-REGEL: Kombiniere niemals massive Fettmengen mit massiven Kohlenhydraten in "
        "derselben Mahlzeit. Insulin öffnet die zellulären Tore; Fett nutzt diesen Weg zur "
        "gnadenlosen Speicherung. Trenne Fett rigoros von deinen Pre-/Post-Workout-Meals. Das ist "
        "für die Körperkomposition nicht verhandelbar."
    ))
    s.append(sp(6))

    s.append(female_box(
        "HINWEIS FÜR ATHLETINNEN — FETTAUFNAHME: Frauen benötigen proportional mehr Fett als Männer "
        "für die Hormongesundheit — besonders in der Lutealphase (Tag 15-28) und der "
        "Menstruationsphase. Fett sollte in diesen Phasen zwingend auf 35-40% der "
        "Nicht-Cardio-Kalorien erhöht werden. Die Omega-3-Aufnahme maximieren. Kohlenhydrate können "
        "hoch bleiben — dies ist keine Fett-oder-KH-Entscheidung, sondern eine strategische Erhöhung "
        "der Gesamtkalorien zur Unterstützung des erhöhten Stoffwechselbedarfs des Hormonzyklus."
    ))
    s.append(sp(6))
    s.append(body(
        "Die Kalorienuntergrenze schafft die Voraussetzung für schweres Training. Schweres Training "
        "rechtfertigt die Untergrenze. Die Makros steuern, wohin die Energie fließt. Jede "
        "Komponente stützt die andere."
    ))
    s.append(sp(8))
    s.append(callout_bold(
        "HÄUFIGE FEHLER — ERNÄHRUNGSRAHMEN<br/><br/>"
        "— <b>Protein über 2,3 g/kg ansetzen:</b> Unnötiger Kostenaufwand ohne Nutzenzuwachs. "
        "Verdrängt Kohlenhydrate aus dem Kalorienbudget — genau das Gegenteil des Ziels.<br/>"
        "— <b>Fett und Kohlenhydrate in einer Mahlzeit massiv kombinieren:</b> Insulin öffnet die "
        "zellulären Tore. Fett nutzt sie zur Speicherung. Das ist Mechanismus, kein Theorie.<br/>"
        "— <b>Kohlenhydrate nach dem Training meiden:</b> Genau jetzt ist die Glykogensyntheserate "
        "am höchsten. Wer hier spart, spart am teuersten Ende.<br/>"
        "— <b>Kalorienuntergrenze an Ruhetagen ignorieren:</b> Kein Training bedeutet nicht kein "
        "Bedarf. Muskelproteinreparatur findet am Ruhetag statt — sie braucht Substrate."
    ))
    s.append(sp(6))
    s.append(callout_bold(
        "EXEKUTION — KAPITEL 06<br/><br/>"
        "— Kalorienboden täglich einhalten — unabhängig vom Trainingstag.<br/>"
        "— Protein auf 1,8–2,3 g/kg Magermasse. Oberes Ende bei hohem Trainingsvolumen.<br/>"
        "— Größte Kohlenhydrat-Mahlzeit direkt nach dem Training.<br/>"
        "— Fett strikt von Pre-/Post-Workout-Meals trennen.<br/>"
        "— Cardio-Kalorien immer zusätzlich zur Untergrenze essen — nie als Teil davon."
    ))

    return s
