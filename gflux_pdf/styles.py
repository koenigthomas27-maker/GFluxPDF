from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from gflux_pdf.config import CYAN, WHITE, TEXT_LIGHT, TEXT_MID, BLACK, DARK1, DARK2, DARK3


def S(name, **kw):
    """Shorthand for ParagraphStyle."""
    return ParagraphStyle(name, **kw)


# --- HEADINGS ---
H1 = S(
    "H1",
    fontName="Helvetica-Bold",
    fontSize=20,
    textColor=WHITE,
    leading=26,
    spaceBefore=16,
    spaceAfter=4,
)

H2 = S(
    "H2",
    fontName="Helvetica-Bold",
    fontSize=13,
    textColor=CYAN,
    leading=18,
    spaceBefore=12,
    spaceAfter=4,
)

H3 = S(
    "H3",
    fontName="Helvetica-Bold",
    fontSize=10,
    textColor=WHITE,
    leading=14,
    spaceBefore=8,
    spaceAfter=3,
)

# --- BODY TEXT ---
BODY = S(
    "Body",
    fontName="Helvetica",
    fontSize=9.5,
    textColor=TEXT_LIGHT,
    leading=14,
    spaceAfter=6,
    alignment=TA_JUSTIFY,
)

BULLET = S(
    "Bullet",
    fontName="Helvetica",
    fontSize=9.5,
    textColor=TEXT_LIGHT,
    leading=14,
    spaceAfter=3,
    leftIndent=10,
)

NOTE = S(
    "Note",
    fontName="Helvetica-Oblique",
    fontSize=8.5,
    textColor=TEXT_MID,
    leading=12,
)

# --- TOC ---
TOC_ENTRY = S(
    "TOCEntry",
    fontName="Helvetica",
    fontSize=10,
    textColor=TEXT_LIGHT,
    leading=15,
)

TOC_ENTRY_H1 = S(
    "TOCEntryH1",
    fontName="Helvetica-Bold",
    fontSize=11,
    textColor=CYAN,
    leading=17,
    spaceBefore=4,
)

TOC_ENTRY_H2 = S(
    "TOCEntryH2",
    fontName="Helvetica",
    fontSize=9.5,
    textColor=TEXT_LIGHT,
    leading=14,
    leftIndent=14,
)

# --- PULL QUOTE ---
PULL_QUOTE = S(
    "PullQuote",
    fontName="Helvetica-BoldOblique",
    fontSize=13,
    textColor=CYAN,
    leading=20,
    alignment=TA_CENTER,
)

# --- MATH / FORMULA ---
FORMULA = S(
    "Formula",
    fontName="Helvetica-Bold",
    fontSize=12,
    textColor=CYAN,
    leading=18,
    alignment=TA_CENTER,
)
