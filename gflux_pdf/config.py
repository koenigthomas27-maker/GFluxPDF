from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# --- PAGE SIZE ---
W, H = A4  # 210 x 297 mm

# --- MARGINS ---
L_MARGIN = 18 * mm
R_MARGIN = 18 * mm
T_MARGIN = 18 * mm
B_MARGIN = 18 * mm
CONTENT_W = W - L_MARGIN - R_MARGIN

# --- BRAND COLORS ---
CYAN    = colors.HexColor("#00E5FF")
BLACK   = colors.HexColor("#0A0A0A")
DARK1   = colors.HexColor("#141414")
DARK2   = colors.HexColor("#1C1C1C")
DARK3   = colors.HexColor("#242424")
WHITE   = colors.HexColor("#FFFFFF")
TEXT_LIGHT = colors.HexColor("#E0E0E0")
TEXT_MID   = colors.HexColor("#AAAAAA")
RULE       = colors.HexColor("#3A3A3A")
FEMALE     = colors.HexColor("#FF6B9D")

# --- PDF OUTPUT ---
OUTPUT_FILE = "GFlux_DE_2026_V1_Full.pdf"
