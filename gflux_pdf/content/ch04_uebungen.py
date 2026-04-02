from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, H2, callout, callout_bold, companion_box, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("04", "Übungsauswahl-Logik")

    s.append(body(
        "Die Übungsauswahl folgt einer verbindlichen Bewegungsmuster-Rotation. Dies ist deine "
        "Versicherungspolice gegen kumulativen Gelenk- und Sehnenverschleiß. Das Muster ist die "
        "nicht verhandelbare Einheit — die spezifische Übung innerhalb des Musters ist flexibel, "
        "abhängig von Geräten, Tagesform und Regenerationsstatus."
    ))
    s.append(sp(6))

    s.append(H2("Bewegungsmuster-Rotation an Extremitäten-Tagen"))
    s.append(body(
        "Extremitäten-Tage rotieren zwischen kniebeuge- und scharnierdominanten Mustern, um zu "
        "verhindern, dass zwei aufeinanderfolgende schwere Sessions dasselbe Muster belasten. "
        "Die Rotation ergibt effektiv eine 4-fache Aufteilung:"
    ))
    s.append(sp(4))

    s.append(mk_table([
        ["SESSION", "HAUPT-GRUNDZUG", "DUP SEKUNDÄR", "BEGRÜNDUNG"],
        ["Extr. A",
         "Schwere Kniebeugung\n(z.B. Kniebeugen, Hack)",
         "Moderates Scharnier\n(z.B. RDL-Variation)",
         "Quadrizepsdominante Session. Hüfte assistiert."],
        ["Extr. B",
         "Schweres Scharnier\n(z.B. Kreuzheben, Trap-Bar)",
         "Moderate Kniebeugung\n(z.B. Beinpresse leicht)",
         "Hüftdominante Session. Knie unterstützt aktiv."],
        ["Extr. C",
         "Schwere Kniebeugung\n(anderer Winkel/Stand als A)",
         "Moderates Scharnier\n(anderer Winkel als B)",
         "Wieder quadrizepsdominiert, Belastungswinkel gezielt verändert."],
        ["(Extr. D)",
         "Schwere Scharniervariation\n(z.B. Einbein, Defizit)",
         "Moderate Kniebeugungs-\nVariation",
         "Optionale 4. Rotation für mehr Volumen oder spezifische Schwachstellen."],
    ], [CONTENT_W * 0.15, CONTENT_W * 0.3, CONTENT_W * 0.25, CONTENT_W * 0.3]))
    s.append(sp(6))
    s.append(body(
        "Das Muster legt die kumulative Gelenkbelastung der Woche fest. Die spezifische Übung "
        "bestimmt nur den Winkel."
    ))
    s.append(sp(6))

    s.append(H2("DUP Sekundär-Auswahl"))
    s.append(body(
        "Die DUP-Sekundärübung soll das Bewegungsmuster des Hauptzuges derselben Session spiegeln, "
        "aber anders ausgeführt werden — z.B. mit konstantem Muskelspannungs-Fokus, anderer "
        "Fußstellung, langsamem Tempo oder einer Maschinen-Variante. Sie darf keine nahezu maximale "
        "Last erfordern. Ihr Zweck ist Volumenakkumulation, nicht absolute Intensität."
    ))
    s.append(sp(4))
    s.append(body(
        "Übungsrotation hält Sehnen und Gelenke gesund. Gesunde Sehnen erlauben progressives "
        "Overloading. Progressives Overloading erzeugt die mechanische Spannung, die G-Flux "
        "erst sinnvoll macht."
    ))
    s.append(sp(6))

    s.append(H2("Isolations-Auswahl"))
    s.append(body(
        "Isolationen werden frei gewählt. Keine Rotationspflicht. Priorisiere Übungen mit starker "
        "Muskel-Geist-Verbindung, geringem Gelenkrisiko und möglicher progressiver Überlastung über "
        "mehrere Sessions. Rest-Pause-Technik wird extrem empfohlen, um Volumen effizient zu "
        "akkumulieren, ohne die Sessiondauer unnötig zu verlängern."
    ))
    s.append(sp(8))
    s.append(callout_bold(
        "HÄUFIGE FEHLER — ÜBUNGSAUSWAHL<br/><br/>"
        "— <b>Gleiche Bewegungsebene in aufeinanderfolgenden Sessions belasten:</b> Kumulativer "
        "Gelenkverschleiß ohne Erholungsfenster. Dies ist der häufigste strukturelle Fehler im "
        "selbst programmierten Training.<br/>"
        "— <b>DUP Sekundär mit maximaler Intensität ausführen:</b> Das ist nicht der Zweck. Die "
        "Intensität gehört in Tier 1. Wer hier zu viel gibt, zerstört den Transfereffekt auf die "
        "Hauptübung.<br/>"
        "— <b>Isolationsübungen zu häufig rotieren:</b> Rotation ist bei Grundzügen Pflicht, bei "
        "Isolationen optional. Wer Isolationen ständig tauscht, verliert den Progressionstrack."
    ))
    s.append(sp(6))
    s.append(callout_bold(
        "EXEKUTION — KAPITEL 04<br/><br/>"
        "— Halte die Bewegungsmuster-Rotation an Extremitäten-Tagen ein. Die Übung ist flexibel — "
        "das Muster nicht.<br/>"
        "— DUP Sekundär nie mit maximaler Intensität ausführen. Volumenarbeit, keine PR-Versuche.<br/>"
        "— Isolationen frei wählen: Priorität auf Muskelfühlung, geringes Gelenkrisiko, klares "
        "Progressionspotenzial.<br/>"
        "— Rest-Pause-Technik für Isolationen in Betracht ziehen — gleiche Adaptation, weniger Zeitaufwand."
    ))
    s.append(sp(8))

    s.append(companion_box(
        "G-Flux Übungsauswahl & Programm-Templates",
        "Dieses Kapitel definiert die strikte Logik. Der Begleitband erweitert sie zu einer "
        "vollständigen Übungsbibliothek nach Muster, Gerät und Trainingsniveau — mit fertigen "
        "8-Wochen-Programm-Templates für die Optimierungsphase. Exekution ohne Rätselraten.",
    ))

    return s
