from reportlab.platypus import PageBreak
from gflux_pdf.components import (
    sp, body, H2, callout_bold, mk_table, section_break,
)
from gflux_pdf.config import CONTENT_W


def build() -> list:
    s = [PageBreak()]
    s += section_break("02", "Das G-Flux-Prinzip")

    s.append(body(
        "G-Flux — Energiefluss — beschreibt das gesamte Energievolumen, das täglich durch das "
        "System fließt. Hoher Fluss bedeutet: Der Athlet nimmt riesige Kalorienmengen auf UND "
        "verbraucht massive Mengen durch Training, NEAT und Thermogenese. Das unterscheidet sich "
        "fundamental von einem traditionellen 'Bulk'."
    ))
    s.append(sp(6))

    s.append(H2("Warum hoher Fluss funktioniert"))
    s.append(body(
        "Bei hohem Energiefluss steigert der Körper seine anabolen Mechanismen und erzwingt eine "
        "überlegene Nährstoff-Partitionierung — ein massiver Anteil der aufgenommenen Kalorien wird "
        "bevorzugt direkt ins Muskelgewebe und in die Glykogenspeicher geleitet statt ins Fettgewebe. "
        "Das kombinierte Ergebnis aus mechanischem Reiz (Krafttraining), hohem Glykogenbedarf "
        "(Ausdauertraining) und einem konsistenten Kalorienüberschuss schafft ein metabolisches "
        "Umfeld, das Muskelwachstum extrem begünstigt, ohne begleitende Fettansammlung."
    ))
    s.append(sp(6))

    s.append(H2("Traditioneller Masseaufbau vs. G-Flux"))
    s.append(mk_table([
        ["METRIK", "TRADITIONELLER AUFBAU", "G-FLUX PROTOKOLL"],
        ["Kalorienüberschuss",
         "Fester, moderater Überschuss",
         "Großer Überschuss, dynamisch an Output gekoppelt"],
        ["Cardio",
         "Minimiert oder vermieden",
         "Motor-Aufbau — rechtfertigt massives Essen, nie als Defizit-Werkzeug"],
        ["Körperfett-Verlauf",
         "Steigt signifikant im Aufbauzyklus",
         "Kontrolliert strikt unter der Deckelgrenze"],
        ["Athletische Kapazität",
         "Nimmt beim Aufbau massiv ab",
         "Verbessert sich parallel zum Muskelaufbau"],
        ["Nährstoffverteilung",
         "Durchschnittlich bis schlecht",
         "Optimiert durch hohen Fluss und maximale Insulinsensitivität"],
        ["Ganzjährige Machbarkeit",
         "Erfordert zwingend Diätphasen",
         "Schlanker Aufbau ganzjährig problemlos möglich"],
    ], [CONTENT_W * 0.25, CONTENT_W * 0.35, CONTENT_W * 0.4]))
    s.append(sp(6))
    s.append(body(
        "Der Unterschied zwischen traditionellem Masseaufbau und G-Flux ist nicht graduell. "
        "Er ist strukturell."
    ))
    s.append(sp(4))
    s.append(body(
        "Hohe Kalorien ermöglichen schweres Training. Schweres Training fordert hohe Kalorien. "
        "G-Flux verstärkt sich selbst — oder kollabiert, wenn eine Seite wegfällt."
    ))
    s.append(sp(4))
    s.append(body(
        "Wer den Kalorienboden nicht manuell berechnen will: Der CbTK-Tracker übernimmt die "
        "Berechnung für alle drei NEAT-Kategorien automatisch."
    ))
    s.append(sp(6))

    s.append(callout_bold(
        "DIE KERNREGEL: Cardio wird niemals genutzt, um ein Kaloriendefizit zu erzeugen. Jede durch "
        "dediziertes Cardio-Training verbrannte Kalorie wird zusätzlich zur Kalorienuntergrenze "
        "gegessen. Cardio erweitert den Motor, verbessert die Insulinsensitivität und erhöht die "
        "gesamte Workload-Kapazität. Es verbrennt kein Fett — das Ernährungsprotokoll steuert die "
        "Körperkomposition. Wer diese Regel bricht, scheitert."
    ))
    s.append(sp(8))
    s.append(callout_bold(
        "HÄUFIGE FEHLER — G-FLUX-PRINZIP<br/><br/>"
        "— <b>Cardio als Kaloriendefizit einplanen:</b> Du trainierst deinen Körper in Sparsamkeit "
        "statt Kapazität. Muskelaufbau stagniert. Das ist der teuerste Fehler im Protokoll.<br/>"
        "— <b>Kalorienboden zu niedrig ansetzen:</b> Das System braucht Fluss. Zu wenig Energie "
        "bedeutet zu wenig Adaptationsressource — egal wie hart trainiert wird.<br/>"
        "— <b>G-Flux mit unrestriktiertem Bulk verwechseln:</b> Kein Überschuss ohne Funktion. "
        "Jede Kalorie hat eine Rolle. Der Überschuss entsteht durch Trainingsvolumen, nicht durch "
        "Essen ohne Limit.<br/>"
        "— <b>Die Kernregel einmalig brechen und ignorieren:</b> Wer Cardio-Kalorien nicht "
        "zurückisst, zerstört den Mechanismus. Das Protokoll funktioniert nur als vollständiges System."
    ))
    s.append(sp(6))
    s.append(callout_bold(
        "EXEKUTION — KAPITEL 02<br/><br/>"
        "— Berechne deinen Kalorienboden: 35 kcal/kg Magergewicht (Training + hoher NEAT), "
        "32 kcal/kg (Bürojob + Training), 27–28 kcal/kg (Ruhetag, sitzend).<br/>"
        "— Jede Cardio-Kalorie wird zusätzlich zur Untergrenze gegessen. Keine Ausnahmen.<br/>"
        "— Cardio ist kein Defizit-Werkzeug. Es ist ein Kapazitätswerkzeug.<br/>"
        "— Verstehe die Kernregel vollständig, bevor du das erste Training beginnst."
    ))

    return s
