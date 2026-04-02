"""
G-Flux Athleten-Protokoll — PDF Generator
==========================================
Entry point. Assembles all chapter modules into a single story
and builds the PDF via GFluxDocTemplate.multiBuild() so that
the table of contents receives real page numbers on the second pass.

Usage:
    pip install reportlab
    python -m gflux_pdf.generate
    # or from the repo root:
    python gflux_pdf/generate.py
"""

import sys
import os

# Allow running as a script from any working directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.platypus import PageBreak

from reportlab.platypus import NextPageTemplate

from gflux_pdf.config import OUTPUT_FILE
from gflux_pdf.canvas import cover_canvas, main_canvas
from gflux_pdf.toc_template import GFluxDocTemplate
from gflux_pdf.components import section_break, sp

# Chapter modules
from gflux_pdf.content import (
    vorwort,
    ueber_autor,
    toc_page,
    ch01_onboarding,
    ch02_gflux,
    ch03_architektur,
    ch04_uebungen,
    ch05_cardio,
    ch06_ernaehrung,
    ch07_insulin,
    ch08_volumenzyklus,
    ch09_regeneration,
    ch10_minicut,
    ch11_ema,
    ch12_athletinnen,
    ch13_prozess,
    appendix,
    contact,
)


def build_story(toc_flowable) -> list:
    story = []

    # Page 1: cover template, then switch to main template for all other pages
    story.append(NextPageTemplate("main"))
    story.append(PageBreak())
    
    

    # Front matter
    story += vorwort.build()
    story += ueber_autor.build()
    story += toc_page.build(toc_flowable)

    # Main chapters
    story += ch01_onboarding.build()
    story += ch02_gflux.build()
    story += ch03_architektur.build()
    story += ch04_uebungen.build()
    story += ch05_cardio.build()
    story += ch06_ernaehrung.build()
    story += ch07_insulin.build()
    story += ch08_volumenzyklus.build()
    story += ch09_regeneration.build()
    story += ch10_minicut.build()
    story += ch11_ema.build()
    story += ch12_athletinnen.build()
    story += ch13_prozess.build()

    # Appendix
    story += appendix.build()

    # Contact page
    story += contact.build()

    return story


def main():
    toc = GFluxDocTemplate.make_toc()

    doc = GFluxDocTemplate(
        OUTPUT_FILE,
        cover_canvas_fn=cover_canvas,
        main_canvas_fn=main_canvas,
    )

    story = build_story(toc)

    # multiBuild runs two passes:
    #   Pass 1 — lays out pages and collects TOC entries
    #   Pass 2 — re-renders with real page numbers in the TOC
    doc.multiBuild(story)

    print(f"PDF generiert: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
