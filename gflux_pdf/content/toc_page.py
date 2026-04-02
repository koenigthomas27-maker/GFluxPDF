"""
Table of Contents page — static visual TOC rendered before the
auto-generated TOC flowable (which fills in page numbers).
"""

from reportlab.platypus import PageBreak, Paragraph
from gflux_pdf.components import sp, section_break, toc_table
from gflux_pdf.toc_template import GFluxDocTemplate

TOC_ITEMS = [
    ("01", "Philosophie, Voraussetzungen & Onboarding"),
    ("02", "Das G-Flux-Prinzip"),
    ("03", "Trainingsarchitektur: Der 9-Tage-Zyklus"),
    ("04", "Übungsauswahl-Logik"),
    ("05", "Cardio & Cross-Training-Protokoll"),
    ("06", "Ernährungsrahmen"),
    ("07", "Insulinsensitivität & Supplementierung"),
    ("08", "Der 8-Wochen-Volumenzyklus"),
    ("09", "Biomarker-Überwachung & Regeneration"),
    ("10", "Mini-Cut-Protokoll"),
    ("11", "EMA, Check-Ins & Gewichtsschwankungen"),
    ("12", "Besonderheiten für Athletinnen"),
    ("13", "Dem Prozess vertrauen"),
    ("—",  "Anhang: Das G-Flux Kompendium"),
]


def build(toc_flowable) -> list:
    """
    toc_flowable: the TableOfContents instance returned by
                  GFluxDocTemplate.make_toc() — it will auto-fill page numbers.
    """
    s = [PageBreak()]
    s += section_break("—", "Inhaltsverzeichnis")

    # Auto-populated TOC with real page numbers
    s.append(toc_flowable)
    s.append(sp(16))

    return s
