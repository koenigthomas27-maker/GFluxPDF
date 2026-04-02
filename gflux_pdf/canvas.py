"""
Canvas background functions applied to each PDF page.
cover_canvas  — applied to page 1 only
main_canvas   — applied to all subsequent pages
"""

from gflux_pdf.config import (
    W, H, CYAN, BLACK, DARK2, WHITE, TEXT_MID, RULE,
)


def cover_canvas(c, doc):
    c.saveState()

    # Full black background
    c.setFillColor(BLACK)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Top-right decorative corner triangle
    p = c.beginPath()
    p.moveTo(W - 80 * 2.8346, H)
    p.lineTo(W, H)
    p.lineTo(W, H - 80 * 2.8346)
    p.close()
    c.setFillColor(DARK2)
    c.drawPath(p, fill=1, stroke=0)

    # Left accent bar (cyan)
    c.setFillColor(CYAN)
    c.rect(0, 0, 5, H, fill=1, stroke=0)

    # Bottom accent bar (cyan)
    c.setFillColor(CYAN)
    c.rect(0, 0, W, 5, fill=1, stroke=0)

    # Logo / brand
    c.setFillColor(CYAN)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(16 * 2.8346, H - 16 * 2.8346, "CbTK")
    c.setFillColor(TEXT_MID)
    c.setFont("Helvetica", 10)
    c.drawString(16 * 2.8346 + 36, H - 16 * 2.8346, "COACHING BY TK")

    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.line(16 * 2.8346, H - 20 * 2.8346, W - 16 * 2.8346, H - 20 * 2.8346)

    # Large title block
    title_y = H / 2 + 30
    c.setFillColor(CYAN)
    c.setFont("Helvetica-Bold", 52)
    c.drawString(16 * 2.8346, title_y + 52, "G-FLUX")

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 52)
    c.drawString(16 * 2.8346, title_y, "ATHLETE")

    c.setFillColor(TEXT_MID)
    c.setFont("Helvetica-Bold", 52)
    c.drawString(16 * 2.8346, title_y - 56, "PROTOCOL")

    c.setFillColor(TEXT_MID)
    c.setFont("Helvetica", 12)
    c.drawString(16 * 2.8346, title_y - 84, "Das Hybrid-Kraft & Ausdauer-Handbuch")

    # Bottom rule + edition info
    c.setStrokeColor(CYAN)
    c.setLineWidth(0.6)
    c.line(16 * 2.8346, 24 * 2.8346, W - 16 * 2.8346, 24 * 2.8346)

    c.setFillColor(CYAN)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(16 * 2.8346, 18 * 2.8346, "TRAININGSHANDBUCH")

    c.setFillColor(TEXT_MID)
    c.setFont("Helvetica", 9)
    c.drawRightString(W - 16 * 2.8346, 18 * 2.8346, "AUSGABE 2026")

    c.restoreState()


def main_canvas(c, doc):
    c.saveState()

    # Full black background
    c.setFillColor(BLACK)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Left accent bar (cyan, thinner than cover)
    c.setFillColor(CYAN)
    c.rect(0, 0, 3, H, fill=1, stroke=0)

    # Top rule
    c.setStrokeColor(RULE)
    c.setLineWidth(0.4)
    c.line(12 * 2.8346, H - 13 * 2.8346, W - 12 * 2.8346, H - 13 * 2.8346)

    # Header: brand + doc title
    c.setFillColor(CYAN)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(14 * 2.8346, H - 10 * 2.8346, "CbTK")

    c.setFillColor(WHITE)
    c.setFont("Helvetica", 8)
    c.drawString(14 * 2.8346 + 24, H - 10 * 2.8346, "G-FLUX ATHLETEN-PROTOKOLL")
    c.drawRightString(W - 12 * 2.8346, H - 10 * 2.8346, "TRAININGSHANDBUCH")

    # Bottom rule + page number
    c.line(12 * 2.8346, 12 * 2.8346, W - 12 * 2.8346, 12 * 2.8346)

    page_num = doc.page
    if page_num > 1:
        c.setFillColor(WHITE)
        c.setFont("Helvetica", 8)
        c.drawCentredString(W / 2, 8 * 2.8346, str(page_num - 1))

    c.restoreState()
