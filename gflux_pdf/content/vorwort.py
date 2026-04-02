from reportlab.platypus import PageBreak, Paragraph
from gflux_pdf.components import (
    sp, body, bul, H2, callout, callout_bold, section_break, pull_quote,
)
import gflux_pdf.styles as st


def build() -> list:
    s = []
    s += section_break("—", "Vorwort")

    s.append(pull_quote(
        '"Das Aussehen folgt der Leistung. Wir jagen der Illusion nicht nach — sie folgt uns."'
    ))
    s.append(sp(12))

    s.append(H2("Ist das Hyrox? Nein — aber du wirst jeden Hyrox-Athleten in die Tasche stecken"))
    s.append(body(
        "Eines vorweg: Das hier ist kein Hyrox-Programm, keine Hindernislauf-Methodik und kein "
        "sportartspezifischer Vorbereitungsplan. Wer dieses Handbuch konsequent umsetzt, wird jedoch "
        "feststellen, dass er die meisten Hyrox-Athleten an ihre physischen Grenzen bringt. Warum? Weil "
        "dieses Protokoll exakt jenen aeroben Motor und jene strukturelle Kraftbasis aufbaut, die "
        "Hochleistung in absolut jeder Disziplin diktiert. Wir bauen die biochemische und mechanische "
        "Infrastruktur. Der spezifische Sport ist danach nur noch die Anwendung."
    ))

    s.append(H2("Was ist ein Hybrid-Athlet — wirklich?"))
    s.append(body(
        "Der Begriff 'Hybrid-Athlet' wurde durch Social Media zu etwas aufgeblasen, das neu, exklusiv "
        "und erstrebenswert klingt. Nichts davon trifft zu. Hybrid-Athleten hat es immer gegeben. "
        "Triathleten, Langläufer, Ruderer, Rugby-Spieler, Zehnkämpfer und Siebenkämpferinnen — das "
        "sind die Originale. Profis, die seit jeher außergewöhnliche Kraft, massive Ausdauerkapazität "
        "und Bewegungskompetenz in einem einzigen, funktionalen Körper vereinen."
    ))
    s.append(body(
        "Was du mit diesem Protokoll werden kannst, ist etwas ebenso Wertvolles und für den Alltag "
        "vielleicht sogar Relevanteres: ein vielseitiger, extrem leistungsfähiger Mensch — Mann oder "
        "Frau —, der echte Kraft, einen unermüdlichen Motor und eine erstklassige "
        "Körperzusammensetzung in jeden Bereich des Lebens mitbringt. Das Ziel ist keine "
        "Social-Media-Identität. Es ist ein Körper, der massiven Stress absorbiert, extrem schnell "
        "regeneriert und Jahrzehnte hält."
    ))

    s.append(H2("Warum dieses System entwickelt wurde: Pilzzucht vs. Schmetterlinge"))
    s.append(body(
        "Dieses Handbuch existiert, weil ich die Fitnesskultur im DACH-Raum satt hatte. Der hiesige "
        "Markt hinkt der Weltspitze — USA, Australien, Skandinavien — strukturell ein Jahrzehnt "
        "hinterher. Er wird von Konzernen dominiert, die den Konsumenten wie eine Pilzkultur behandeln: "
        "Im Dunkeln halten, mit Informationsfetzen besprühen und isolieren. Dieses Drop-Feeding ohne "
        "Kontext erzeugt Abhängigkeit, keine athletische Evolution. Wir stecken in einer "
        "Kettenhemd-Mentalität des veralteten Bodybuildings fest."
    ))
    s.append(body(
        "Das Kernproblem ist nicht Doping an sich. Das Problem ist, dass ein ganzer Markt "
        "Trainingsvolumina und Methoden blind kopiert, die ausschließlich unter chemisch modifizierten "
        "Bedingungen funktionieren. Diese Praktiken werden unbewusst normalisiert, bis kaum ein "
        "Freizeitsportler noch weiß, wie physiologisch fundiertes, natürliches Training eigentlich "
        "aussieht."
    ))
    s.append(body(
        "Mein Ziel mit CbTK sind Schmetterlinge: Athleten, die die Systematik tiefgreifend verstehen "
        "und autonom exekutieren. Wir importieren hier echte Sportwissenschaft — Kraft- & "
        "Konditionsforschung (S&C), olympische Periodisierung, skandinavische Ausdauermodelle —, um "
        "den Status quo zu durchbrechen. Ohne die Grifter-Umwege über Dubai."
    ))

    s.append(H2("Was wir stattdessen aufbauen"))
    s.append(body(
        "Das G-Flux Athleten-Protokoll baut das exakte Gegenteil der Mainstream-Illusion auf. Dichtes, "
        "metabolisch aktives, mitochondrienreiches Muskelgewebe — kein Ödem, keine Plasmaflüssigkeit, "
        "keine pharmakologisch induzierte temporäre Größe, die Wochen nach dem Aufhören in sich "
        "zusammenfällt. Das Gewebe, das durch diesen Ansatz aufgebaut wird, ist reif, strukturell "
        "solide und wirklich deins. Nimm drei Monate komplett vom Training frei — ein erheblicher Teil "
        "bleibt, weil die zellulären Mechanismen fundamental anders sind."
    ))
    s.append(body(
        "Die Kollagensynthese bleibt intakt. Die Sehnen bleiben flexibel und extrem reaktionsfähig. "
        "Die inneren Organe werden nicht chronisch vergrößert. Haut und Bindegewebe verhalten sich so, "
        "wie sie es über Jahre hartem Training hinweg sollten. Das ist der Unterschied zwischen einem "
        "Körper, der über Jahrzehnte performt, und einem, der ständiges medizinisches Management "
        "benötigt."
    ))
    s.append(callout(
        "Wir bauen griechische Statuen. Nicht die Illusion, die entsteht, wenn man bestimmte "
        "Muskelgruppen vermeidet, weil sie den V-Taper ruinieren. Wir bauen Herakles — funktional, "
        "kraftvoll, schlank und dominant in jeder Umgebung. Das Aussehen folgt der Leistung. Immer. "
        "Das ist nicht verhandelbar."
    ))

    s.append(H2("Das metabolische Umfeld, das wir schaffen"))
    s.append(body(
        "So zu essen wie ein Akteur der modernen Fitnessbranche — der Masse-First-Verfechter, der "
        "Influencer mit verdeckter Unterstützung — wird deine Stoffwechselgesundheit schleichend "
        "zerstören. Die Insulinsensitivität kollabiert. Der Körper lernt, Fett maximal effizient zu "
        "speichern. Schlafbezogene Atemstörungen werden zum Managementproblem. Das CPAP-Gerät hat "
        "seinen Weg in die Schlafzimmer von Amateuren gefunden. Das ist kein Zufall."
    ))
    s.append(body(
        "Wir erschaffen bewusst das Gegenteil. Ein Körper mit hoher Insulinsensitivität funktioniert "
        "wie ein Nährstoffschwamm — Kohlenhydrate fließen bevorzugt ins Muskelgewebe und in die "
        "Glykogenspeicher, während die Fettansammlung ein ausgesprochen ungünstiges Umfeld vorfindet. "
        "Einmal aufgebaut, sind diese Anpassungen strukturell, zellulär und dauerhaft."
    ))

    s.append(H2("Für wen ist das gedacht?"))
    s.append(body(
        "Dieses Protokoll ist für Männer und Frauen gleichermassen geschrieben. Die physiologischen "
        "Prinzipien sind universell. Spezifische Anpassungen für Athletinnen — Körperfettschwellen, "
        "zyklusphasenabhängige Ernährung, Fettaufnahme-Periodisierung — werden in einem eigenen "
        "Kapitel tiefgreifend und ohne Herablassung behandelt."
    ))
    s.append(body(
        "Das hier ist für jeden, der Freude daran hat, von einer Position echter Stärke und Kapazität "
        "zwischen verschiedenen Herausforderungen zu wechseln. Den Läufer, der extrem schwer hebt. Den "
        "Heber, der laufen möchte. Den Berufstätigen, der sich weigert zu akzeptieren, dass Gesundheit "
        "entweder Kraft oder Ausdauer erfordert — aber nicht beides."
    ))
    s.append(body(
        "Das Ziel ist ein Leben lang dominant auszusehen und sich makellos zu bewegen. Nicht so lange, "
        "wie der aktuelle Block andauert. Starke Gewohnheiten. Flexibles Programm. Eine eiserne Mentalität."
    ))

    return s
