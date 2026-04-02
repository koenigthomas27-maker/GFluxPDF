"""
Reusable ReportLab flowable builders for the G-Flux PDF.
All functions return Flowable instances or lists of Flowables.
"""

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, Flowable,
)
from reportlab.lib.enums import TA_CENTER

import gflux_pdf.styles as st
from gflux_pdf.config import (
    CYAN, BLACK, DARK1, DARK2, DARK3, WHITE,
    TEXT_LIGHT, TEXT_MID, RULE, FEMALE, CONTENT_W, W, H, L_MARGIN,
)


# ---------------------------------------------------------------------------
# Primitive helpers
# ---------------------------------------------------------------------------

def sp(h: float = 8) -> Spacer:
    return Spacer(1, h)


def body(text: str) -> Paragraph:
    return Paragraph(text, st.BODY)


def bul(text: str) -> Paragraph:
    return Paragraph(f"<font color='#00E5FF'>&#x2014;</font> {text}", st.BULLET)


def note(text: str) -> Paragraph:
    return Paragraph(text, st.NOTE)


def H2(text: str) -> Paragraph:
    """Section sub-heading (cyan)."""
    return Paragraph(text, st.H2)


def H3(text: str) -> Paragraph:
    """Sub-sub-heading (white)."""
    return Paragraph(text, st.H3)


def formula(text: str) -> Paragraph:
    return Paragraph(f"<font color='#00E5FF'><b>{text}</b></font>", st.FORMULA)


def pull_quote(text: str) -> Paragraph:
    return Paragraph(text, st.PULL_QUOTE)


# ---------------------------------------------------------------------------
# Section break — chapter title block with cyan accent
# ---------------------------------------------------------------------------

class ChapterSplash(Flowable):
    """
    Full-width chapter title block drawn directly on canvas.
    Renders a dark background rect, large faded chapter number,
    a cyan left-accent bar, and the chapter title.
    """

    def __init__(self, number: str, title: str, anchor: str = ""):
        super().__init__()
        self.number = number   # e.g. "01"
        self.title  = title    # e.g. "Philosophie & Onboarding"
        self.anchor = anchor   # PDF bookmark key
        self._height = 60

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return availWidth, self._height

    def draw(self):
        c = self.canv
        c.saveState()

        w = self.width
        h = self._height

        # Background
        c.setFillColor(DARK3)
        c.rect(0, 0, w, h, fill=1, stroke=0)

        # Cyan left accent bar
        c.setFillColor(CYAN)
        c.rect(0, 0, 4, h, fill=1, stroke=0)

        # Large faded chapter number (watermark style)
        c.setFillColor(DARK1)  # nearly invisible against DARK3
        c.setFont("Helvetica-Bold", 72)
        c.drawString(w - 58, -4, self.number)

        # Chapter number label (small, cyan)
        c.setFillColor(CYAN)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(14, h - 14, f"KAPITEL {self.number}")

        # Chapter title (white, large)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 22)
        c.drawString(14, 14, self.title)

        # Bottom rule
        c.setStrokeColor(CYAN)
        c.setLineWidth(0.8)
        c.line(0, 0, w, 0)

        # PDF bookmark anchor
        if self.anchor:
            c.bookmarkPage(self.anchor)
            c.addOutlineEntry(f"{self.number} {self.title}", self.anchor, level=0)

        c.restoreState()


def section_break(number: str, title: str) -> list:
    """Returns a list of flowables: spacer + ChapterSplash + spacer."""
    anchor = f"ch_{number}"
    return [
        sp(8),
        ChapterSplash(number, title, anchor=anchor),
        sp(14),
    ]


# ---------------------------------------------------------------------------
# Tables
# ---------------------------------------------------------------------------

def mk_table(
    data: list[list[str]],
    widths: list[float],
    accent_rows: set[int] | None = None,
    female_rows: set[int] | None = None,
) -> Table:
    """
    Build a styled dark-theme table.
    Row 0 is treated as header (bold, cyan).
    accent_rows: additional rows to render bold/cyan (e.g. summary rows).
    female_rows: rows rendered in FEMALE color.
    """
    para_data = []
    for ri, row in enumerate(data):
        para_row = []
        for ci, cell in enumerate(row):
            is_header  = ri == 0
            is_accent  = accent_rows and ri in accent_rows
            is_female  = female_rows and ri in female_rows
            font_name  = "Helvetica-Bold" if (is_header or is_accent) else "Helvetica"
            text_color = (
                CYAN   if (is_header or is_accent) else
                FEMALE if is_female else
                TEXT_LIGHT
            )
            style = ParagraphStyle(
                f"tc_{ri}_{ci}",
                fontName=font_name,
                fontSize=8.5,
                textColor=text_color,
                leading=11,
            )
            para_row.append(Paragraph(str(cell), style))
        para_data.append(para_row)

    t = Table(para_data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1,  0), DARK3),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [DARK1, DARK2]),
        ("GRID",         (0, 0), (-1, -1), 0.3, RULE),
        ("VALIGN",       (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",  (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING",   (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 6),
    ]))
    return t


# ---------------------------------------------------------------------------
# Callout boxes
# ---------------------------------------------------------------------------

def callout(text: str, border_color=None, bg=DARK2, text_color=TEXT_LIGHT) -> Table:
    if border_color is None:
        border_color = CYAN
    cell_style = ParagraphStyle(
        "cb",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=text_color,
        leading=14,
    )
    t = Table([[Paragraph(text, cell_style)]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, -1), bg),
        ("LINEBEFORE",   (0, 0), (0,  -1), 3, border_color),
        ("BOX",          (0, 0), (-1, -1), 0.3, RULE),
        ("LEFTPADDING",  (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING",   (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 10),
    ]))
    return t


def callout_bold(text: str) -> Table:
    cell_style = ParagraphStyle(
        "cbb",
        fontName="Helvetica-Bold",
        fontSize=10,
        textColor=CYAN,
        leading=14,
    )
    t = Table([[Paragraph(text, cell_style)]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, -1), DARK3),
        ("BOX",          (0, 0), (-1, -1), 1, CYAN),
        ("LEFTPADDING",  (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING",   (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 10),
    ]))
    return t


def female_box(text: str) -> Table:
    return callout(text, border_color=FEMALE, bg=DARK2, text_color=FEMALE)


def companion_box(vol_title: str, teaser: str) -> Table:
    title_style = ParagraphStyle(
        "cpt",
        fontName="Helvetica-Bold",
        fontSize=9,
        textColor=CYAN,
        leading=13,
    )
    body_style = ParagraphStyle(
        "cpb",
        fontName="Helvetica",
        fontSize=9,
        textColor=TEXT_LIGHT,
        leading=13,
    )
    from reportlab.lib import colors
    inner_title = Paragraph(
        f'<font color="#00E5FF"><b>&#x25BA; Begleitband: {vol_title}</b></font>',
        title_style,
    )
    inner_body = Paragraph(teaser, body_style)
    t = Table([[inner_title], [inner_body]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, -1), colors.HexColor("#0D1A1F")),
        ("BOX",          (0, 0), (-1, -1), 0.8, CYAN),
        ("LINEBEFORE",   (0, 0), (0,  -1), 3, CYAN),
        ("LEFTPADDING",  (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING",   (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 8),
    ]))
    return t


# ---------------------------------------------------------------------------
# TOC table (static visual, used before real TOC)
# ---------------------------------------------------------------------------

def toc_table(items: list[tuple[str, str]]) -> Table:
    data = [
        [
            Paragraph(f'<font color="#00E5FF"><b>{n}</b></font>', st.TOC_ENTRY),
            Paragraph(f'<font color="#E0E0E0">{t}</font>', st.TOC_ENTRY),
        ]
        for n, t in items
    ]
    t = Table(data, colWidths=[15 * 2.8346, CONTENT_W - 15 * 2.8346], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN",       (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 4),
    ]))
    return t
