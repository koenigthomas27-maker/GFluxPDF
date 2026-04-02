"""
GFluxDocTemplate — BaseDocTemplate subclass that:
  - collects H1/H2 headings for automatic TOC page numbers
  - adds PDF bookmarks (outline entries) for H1 sections
  - registers page frames with correct margins
"""

from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle

from gflux_pdf.config import (
    W, H, L_MARGIN, R_MARGIN, T_MARGIN, B_MARGIN,
    CONTENT_W, CYAN, TEXT_LIGHT, DARK1, DARK2, DARK3,
)
import gflux_pdf.styles as st


class GFluxDocTemplate(BaseDocTemplate):
    """
    Two-pass doc template that populates a TableOfContents automatically.
    Usage:
        toc  = GFluxDocTemplate.make_toc()
        doc  = GFluxDocTemplate(filename)
        doc.multiBuild([toc, ...rest_of_story])
    """

    def __init__(self, filename: str, cover_canvas_fn=None, main_canvas_fn=None, **kwargs):
        kwargs.setdefault("pagesize", (W, H))
        kwargs.setdefault("rightMargin",  R_MARGIN)
        kwargs.setdefault("leftMargin",   L_MARGIN)
        kwargs.setdefault("topMargin",    T_MARGIN)
        kwargs.setdefault("bottomMargin", B_MARGIN)
        super().__init__(filename, **kwargs)

        # Content frame (same for all pages; canvas functions handle background)
        frame = Frame(
            L_MARGIN,
            B_MARGIN,
            CONTENT_W,
            H - T_MARGIN - B_MARGIN,
            id="main",
        )

        cover_fn = cover_canvas_fn if cover_canvas_fn else lambda c, d: None
        main_fn  = main_canvas_fn  if main_canvas_fn  else lambda c, d: None

        self.addPageTemplates([
            PageTemplate(id="cover", frames=[frame], onPage=cover_fn),
            PageTemplate(id="main",  frames=[frame], onPage=main_fn),
        ])

    # ------------------------------------------------------------------
    # Automatic TOC collection
    # ------------------------------------------------------------------

    def afterFlowable(self, flowable):
        """Fires after each flowable is placed; collects H1/H2 for TOC."""
        if not hasattr(flowable, "style"):
            return

        style_name = flowable.style.name
        text = flowable.getPlainText()

        if style_name == "H1":
            key = f"toc_{self.page}_{text[:20]}"
            self.canv.bookmarkPage(key)
            self.notify("TOCEntry", (0, text, self.page, key))

        elif style_name == "H2":
            self.notify("TOCEntry", (1, text, self.page))

    # ------------------------------------------------------------------
    # Factory: build a pre-styled TableOfContents flowable
    # ------------------------------------------------------------------

    @staticmethod
    def make_toc() -> TableOfContents:
        toc = TableOfContents()

        # Level 0 — chapter titles (H1)
        toc.levelStyles = [
            ParagraphStyle(
                "TOCLevel0",
                fontName="Helvetica-Bold",
                fontSize=11,
                textColor=CYAN,
                leading=17,
                spaceBefore=4,
                leftIndent=0,
            ),
            # Level 1 — sub-headings (H2)
            ParagraphStyle(
                "TOCLevel1",
                fontName="Helvetica",
                fontSize=9.5,
                textColor=TEXT_LIGHT,
                leading=14,
                leftIndent=14,
            ),
        ]
        return toc
