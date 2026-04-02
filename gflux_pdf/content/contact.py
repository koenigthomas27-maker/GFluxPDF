from reportlab.platypus import PageBreak, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, TableStyle
from gflux_pdf.components import sp, body, H2, section_break
from gflux_pdf.config import (
    CONTENT_W, CYAN, DARK2, DARK3, TEXT_LIGHT, RULE,
)


# ---------------------------------------------------------------------------
# CONTACT PAGE CONFIGURATION
# To activate a field: uncomment the line and fill in the value.
# To hide a field:     comment it out or leave it commented.
# ---------------------------------------------------------------------------

CONTACT_ROWS = {
    "Direktkontakt": [
        ("E-Mail",            "koenigthomas27@gmail.com"),
        # ("Telefon / WhatsApp", ""),           # uncomment when ready
    ],
    "Social Media": [
         ("Instagram",        "https://www.instagram.com/thomas__koenigz/"),               
        # ("YouTube",        ""),               # uncomment when ready
         ("FaceBook",         "https://www.facebook.com/thomas.koenig.129"),               
        # ("LinkedIn",       ""),               # uncomment when ready
    ],
    "Website & Blog": [
        # ("Website / Blog", ""),               # uncomment when ready
    ],
    "Podcast": [
        # ("Podcast",        ""),               # uncomment when ready
        # ("Verfügbar auf",  ""),               # uncomment when ready
    ],
    "Produkte & Links": [
        # ("CbTK-Tracker",    ""),              # uncomment when ready
        # ("1-on-1 Coaching", ""),              # uncomment when ready
        # ("Weitere Produkte",""),              # uncomment when ready
    ],
}

# Section order — controls display sequence
SECTION_ORDER = [
    "Direktkontakt",
    "Social Media",
    "Website & Blog",
    "Podcast",
    "Produkte & Links",
]


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------

def _contact_table(rows: list) -> Table:
    label_style = ParagraphStyle(
        "ct_label",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        textColor=CYAN,
        leading=14,
    )
    value_style = ParagraphStyle(
        "ct_value",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=TEXT_LIGHT,
        leading=14,
    )
    para_rows = [
        [Paragraph(label, label_style), Paragraph(value, value_style)]
        for label, value in rows
    ]
    col_w = [CONTENT_W * 0.3, CONTENT_W * 0.7]
    t = Table(para_rows, colWidths=col_w)
    t.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [DARK3, DARK2]),
        ("LINEBEFORE",     (0, 0), (0,  -1), 3, CYAN),
        ("LINEBELOW",      (0, 0), (-1, -1), 0.3, RULE),
        ("VALIGN",         (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING",    (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",   (0, 0), (-1, -1), 12),
        ("TOPPADDING",     (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 10),
    ]))
    return t


def build() -> list:
    s = [PageBreak()]
    s += section_break("CK", "Kontakt & Community")

    s.append(body(
        "Du hast das Protokoll verstanden. Jetzt geht es um Umsetzung. "
        "Fragen, Feedback, Coaching-Anfragen oder der direkte Kanal zu Thomas:"
    ))
    s.append(sp(10))

    # Only render sections that have at least one active (uncommented) row
    for section_name in SECTION_ORDER:
        rows = CONTACT_ROWS.get(section_name, [])
        if not rows:
            continue  # section is entirely commented out — skip silently
        s.append(H2(section_name))
        s.append(_contact_table(rows))
        s.append(sp(12))

    return s
