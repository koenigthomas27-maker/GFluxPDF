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

    s.append(callout_bold(
        "DIE KERNREGEL: Cardio wird niemals genutzt, um ein Kaloriendefizit zu erzeugen. Jede durch "
        "dediziertes Cardio-Training verbrannte Kalorie wird zusätzlich zur Kalorienuntergrenze "
        "gegessen. Cardio erweitert den Motor, verbessert die Insulinsensitivität und erhöht die "
        "gesamte Workload-Kapazität. Es verbrennt kein Fett — das Ernährungsprotokoll steuert die "
        "Körperkomposition. Wer diese Regel bricht, scheitert."
    ))

    return s
