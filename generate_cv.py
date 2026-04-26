"""Generate Gauresh Naik CV PDF — one-page, two-column dark techy design."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
import io
import os

# ── Paths ──
BASE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BASE, "Gauresh_Naik_CV.pdf")
PHOTO = os.path.join(BASE, "assets", "images", "GAURESH PROFILE.png")

# ── Colors (matching site's dark techy palette) ──
BG_DARK = HexColor("#080C10")
BG_SURFACE = HexColor("#0F1923")
BG_CARD = HexColor("#111C28")
TEAL = HexColor("#00E5CC")
AMBER = HexColor("#F5A623")
BLUE = HexColor("#0066FF")
TEXT_PRIMARY = HexColor("#F0F4F8")
TEXT_SECONDARY = HexColor("#7A8FA6")
TEXT_MUTED = HexColor("#3D5166")
SIDEBAR_BG = HexColor("#0B1219")

# ── Dimensions ──
W, H = A4  # 595.27, 841.89
MARGIN = 14 * mm
SIDEBAR_W = 200
MAIN_X = SIDEBAR_W + 14
MAIN_W = W - MAIN_X - MARGIN

# ── Helpers ──
def draw_sidebar_bg(c):
    c.setFillColor(SIDEBAR_BG)
    c.rect(0, 0, SIDEBAR_W, H, fill=1, stroke=0)

def draw_main_bg(c):
    c.setFillColor(BG_DARK)
    c.rect(SIDEBAR_W, 0, W - SIDEBAR_W, H, fill=1, stroke=0)

def draw_teal_line(c, x, y, w, color=TEAL, opacity=0.4):
    c.setStrokeColor(color)
    c.setLineWidth(0.5)
    # No alpha on canvas line; use lighter color via opacity in fillAlpha
    c.saveState()
    c.setStrokeColorRGB(0, 229/255, 204/255, alpha=opacity)
    c.line(x, y, x + w, y)
    c.restoreState()

def wrap_text(c, text, font, size, max_w):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        if c.stringWidth(test, font, size) <= max_w:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def draw_wrapped(c, text, x, y, font, size, max_w, color=TEXT_PRIMARY, leading=None):
    if leading is None:
        leading = size + 2.5
    c.setFont(font, size)
    c.setFillColor(color)
    lines = wrap_text(c, text, font, size, max_w)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y

def draw_bullet(c, text, x, y, font, size, max_w, color=TEXT_SECONDARY, bullet_color=TEAL, bullet="◆"):
    leading = size + 2.4
    c.setFillColor(bullet_color)
    c.setFont("Helvetica", size - 1)
    c.drawString(x, y + 0.5, bullet)
    bw = c.stringWidth(bullet + "  ", "Helvetica", size - 1)
    lines = wrap_text(c, text, font, size, max_w - bw)
    c.setFillColor(color)
    c.setFont(font, size)
    for line in lines:
        c.drawString(x + bw, y, line)
        y -= leading
    return y

def draw_section_header(c, text, x, y, color=TEAL, font_size=9):
    """Mono-style section header with // prefix and accent bar."""
    c.setFont("Courier-Bold", font_size)
    c.setFillColor(color)
    c.drawString(x, y, text)
    # Underline accent bar
    c.setStrokeColor(color)
    c.setLineWidth(1.5)
    c.line(x, y - 4, x + 24, y - 4)
    return y

def draw_pill(c, text, x, y, color=TEAL, font_size=6.8):
    """Draw a skill pill, return new x position (right edge + gap)."""
    pad_x = 6
    pad_y = 3
    c.setFont("Courier", font_size)
    tw = c.stringWidth(text, "Courier", font_size)
    pill_w = tw + pad_x * 2
    pill_h = font_size + pad_y * 2
    # Border
    c.setStrokeColor(color)
    c.setLineWidth(0.4)
    c.setFillColor(BG_CARD)
    c.roundRect(x, y - pad_y, pill_w, pill_h, 6, fill=1, stroke=1)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(x + pad_x, y, text)
    return x + pill_w + 4, pill_h

def draw_pills_wrapped(c, pills, x, y, max_w, color=TEAL, font_size=6.8, gap_y=4):
    """Draw pills wrapping to multiple rows. Returns new y."""
    cur_x = x
    pad_x = 6
    pad_y = 3
    pill_h = font_size + pad_y * 2
    c.setFont("Courier", font_size)
    for text in pills:
        tw = c.stringWidth(text, "Courier", font_size)
        pill_w = tw + pad_x * 2
        if cur_x + pill_w > x + max_w:
            cur_x = x
            y -= pill_h + gap_y
        c.setStrokeColor(color)
        c.setLineWidth(0.4)
        c.setFillColor(BG_CARD)
        c.roundRect(cur_x, y - pad_y, pill_w, pill_h, 6, fill=1, stroke=1)
        c.setFillColor(TEXT_PRIMARY)
        c.setFont("Courier", font_size)
        c.drawString(cur_x + pad_x, y, text)
        cur_x += pill_w + 4
    return y - pill_h - gap_y + 2

# ══════════════════════════════════════════════════════════
# BUILD PDF
# ══════════════════════════════════════════════════════════
c = canvas.Canvas(OUTPUT, pagesize=A4)
c.setTitle("Gauresh Naik — CV")
c.setAuthor("Gauresh Naik")

# ── Backgrounds ──
draw_main_bg(c)
draw_sidebar_bg(c)

# ══════════════════════════════════════════════════════════
# LEFT SIDEBAR
# ══════════════════════════════════════════════════════════
sx = 18
sw = SIDEBAR_W - 36
sy = H - 28

# ── Profile Photo (circular, teal ring) — compressed for small PDF size ──
if os.path.exists(PHOTO):
    photo_size = 90
    photo_x = sx + (sw - photo_size) / 2
    photo_y = sy - photo_size

    # Compress photo to ~250x250 JPEG for small embedded size
    img = Image.open(PHOTO).convert("RGB")
    img.thumbnail((300, 300), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=82, optimize=True)
    buf.seek(0)
    photo_reader = ImageReader(buf)

    c.saveState()
    p = c.beginPath()
    cx_photo = photo_x + photo_size / 2
    cy_photo = photo_y + photo_size / 2
    p.circle(cx_photo, cy_photo, photo_size / 2)
    p.close()
    c.clipPath(p, stroke=0, fill=0)
    c.drawImage(photo_reader, photo_x, photo_y, photo_size, photo_size,
                preserveAspectRatio=True, anchor='c')
    c.restoreState()
    # Teal glow ring
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.5)
    c.circle(cx_photo, cy_photo, photo_size / 2 + 2, fill=0, stroke=1)
    sy = photo_y - 18

# ── Name ──
c.setFont("Helvetica-Bold", 17)
c.setFillColor(TEXT_PRIMARY)
name = "GAURESH NAIK"
tw = c.stringWidth(name, "Helvetica-Bold", 17)
c.drawString(sx + (sw - tw) / 2, sy, name)
sy -= 14

# ── Title ──
c.setFont("Helvetica", 8)
c.setFillColor(TEAL)
title = "Marketing & Sales Professional"
tw = c.stringWidth(title, "Helvetica", 8)
c.drawString(sx + (sw - tw) / 2, sy, title)
sy -= 10

# ── Subtitle ──
c.setFont("Courier", 6.5)
c.setFillColor(TEXT_SECONDARY)
sub = "Revenue & Operations Lead"
tw = c.stringWidth(sub, "Courier", 6.5)
c.drawString(sx + (sw - tw) / 2, sy, sub)
sy -= 18

# ── Teal divider ──
c.setStrokeColor(TEAL)
c.setLineWidth(0.5)
c.line(sx + 30, sy, sx + sw - 30, sy)
sy -= 14

# ── Contact ──
c.setFont("Courier-Bold", 8)
c.setFillColor(TEAL)
c.drawString(sx, sy, "// CONTACT")
sy -= 13

c.setFont("Helvetica", 7.5)
c.setFillColor(TEXT_PRIMARY)
c.drawString(sx, sy, "naikg8033@gmail.com")
sy -= 11
c.drawString(sx, sy, "+965 976 94436")
sy -= 10
c.setFont("Courier", 6)
c.setFillColor(TEXT_SECONDARY)
c.drawString(sx, sy, "Phone & WhatsApp")
sy -= 11
c.setFont("Helvetica", 7.5)
c.setFillColor(TEXT_PRIMARY)
c.drawString(sx, sy, "Kuwait")
sy -= 10
c.setFont("Courier", 6)
c.setFillColor(TEXT_SECONDARY)
c.drawString(sx, sy, "Open to relocation")
sy -= 11
c.setFont("Helvetica", 7.5)
c.setFillColor(TEXT_PRIMARY)
c.drawString(sx, sy, "github.com/gaur61201")
sy -= 18

# ── Teal divider ──
c.setStrokeColor(TEAL)
c.setLineWidth(0.5)
c.line(sx + 30, sy, sx + sw - 30, sy)
sy -= 14

# ── Marketing & Content Skills ──
c.setFont("Courier-Bold", 8)
c.setFillColor(TEAL)
c.drawString(sx, sy, "// MARKETING")
sy -= 12
marketing = [
    "Social Media Strategy",
    "Content Creation",
    "Video Editing (Premiere)",
    "Canva · Freepik AI",
    "Meta Ads",
    "Instagram · TikTok",
    "Caption Writing",
    "Content Calendars",
]
for skill in marketing:
    c.setFont("Helvetica", 6.8)
    c.setFillColor(TEAL)
    c.drawString(sx + 4, sy, "◆")
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(sx + 12, sy, skill)
    sy -= 9.5
sy -= 6

# ── Sales & Revenue ──
c.setFont("Courier-Bold", 8)
c.setFillColor(AMBER)
c.drawString(sx, sy, "// SALES")
sy -= 12
sales = [
    "Lead Generation",
    "Cold Outreach & Calling",
    "DM Prospecting",
    "Sales Proposals",
    "Objection Handling",
    "Pipeline Management",
    "CRM (Airtable)",
    "Follow-up Sequences",
    "Deal Closing",
]
for skill in sales:
    c.setFont("Helvetica", 6.8)
    c.setFillColor(AMBER)
    c.drawString(sx + 4, sy, "◆")
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(sx + 12, sy, skill)
    sy -= 9.5
sy -= 6

# ── Operations & Systems ──
c.setFont("Courier-Bold", 8)
c.setFillColor(BLUE)
c.drawString(sx, sy, "// OPERATIONS")
sy -= 12
ops = [
    "n8n Automation",
    "Airtable · Google Sheets",
    "Workflow Design",
    "GitHub · GitHub Pages",
    "Claude Code",
    "Web Dev (HTML/CSS/JS)",
    "Process Documentation",
]
for skill in ops:
    c.setFont("Helvetica", 6.8)
    c.setFillColor(BLUE)
    c.drawString(sx + 4, sy, "◆")
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(sx + 12, sy, skill)
    sy -= 9.5

# ══════════════════════════════════════════════════════════
# RIGHT MAIN AREA
# ══════════════════════════════════════════════════════════
mx = MAIN_X + 8
mw = MAIN_W - 16
my = H - 28

# ── Top tag ──
c.setFont("Courier", 7)
c.setFillColor(TEAL)
c.drawString(mx, my, "// BASED IN KUWAIT · OPEN TO OPPORTUNITIES")
my -= 18

# ── Big name ──
c.setFont("Helvetica-Bold", 26)
c.setFillColor(TEXT_PRIMARY)
c.drawString(mx, my, "GAURESH")
my -= 26
c.drawString(mx, my, "NAIK")
my -= 14

# ── Tagline ──
c.setFont("Helvetica-Bold", 10)
c.setFillColor(TEAL)
c.drawString(mx, my, "Marketing & Sales Professional")
my -= 14

# ── Body ──
c.setFont("Helvetica", 8)
c.setFillColor(TEXT_SECONDARY)
my = draw_wrapped(c,
    "I generate leads, close deals, build content — and automate the systems that hold it all together. Hired for one role. Built three.",
    mx, my, "Helvetica", 8, mw, color=TEXT_SECONDARY, leading=11)
my -= 6

# Divider
c.setStrokeColor(TEAL)
c.setLineWidth(0.5)
c.line(mx, my, mx + 36, my)
my -= 14

# ── About ──
draw_section_header(c, "// 01 — ABOUT", mx, my)
my -= 16
c.setFont("Helvetica-Bold", 11)
c.setFillColor(TEXT_PRIMARY)
c.drawString(mx, my, "An operator who markets. A marketer who closes.")
my -= 13

paras = [
    "Marketing & Sales professional with hands-on experience in content creation, lead generation, and sales — running all three simultaneously at Waves Printing Press in Kuwait.",
    "Beyond my job title, I design CRM workflows, build automation pipelines in n8n, and create client-facing websites. I don’t just execute campaigns — I build the systems that make execution sustainable.",
]
for para in paras:
    my = draw_wrapped(c, para, mx, my, "Helvetica", 7.5, mw, color=TEXT_SECONDARY, leading=10.5)
    my -= 3

# Stats row
my -= 4
stat_w = mw / 3 - 8
stat_x = mx
for label, num, sub in [("3", "Functions Managed", ""), ("1 yr", "Experience Kuwait", ""), ("4", "Live Sites Built", "")]:
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(TEAL)
    c.drawString(stat_x, my, label)
    c.setFont("Courier", 6.5)
    c.setFillColor(TEXT_SECONDARY)
    c.drawString(stat_x, my - 10, num)
    stat_x += stat_w + 12
my -= 22

# ── Experience ──
draw_section_header(c, "// 02 — EXPERIENCE", mx, my)
my -= 16

# Company
c.setFont("Helvetica-Bold", 12)
c.setFillColor(TEXT_PRIMARY)
c.drawString(mx, my, "WAVES PRINTING PRESS")
# Period right-aligned
c.setFont("Courier", 7)
c.setFillColor(TEAL)
period = "2024 — Present"
pw = c.stringWidth(period, "Courier", 7)
c.drawString(mx + mw - pw, my + 1, period)
my -= 12

c.setFont("Helvetica", 8.5)
c.setFillColor(TEAL)
c.drawString(mx, my, "Revenue & Operations Lead")
c.setFont("Courier", 6.5)
c.setFillColor(TEXT_SECONDARY)
loc = "Kuwait"
lw = c.stringWidth(loc, "Courier", 6.5)
c.drawString(mx + mw - lw, my, loc)
my -= 11

c.setFont("Courier", 6.5)
c.setFillColor(TEXT_MUTED)
c.drawString(mx, my, "Hired as Social Media Manager → Marketing · Lead Gen · Sales · Automation")
my -= 12

# Body
my = draw_wrapped(c,
    "Joined to manage Instagram. Ended up building the revenue infrastructure. Took ownership of content strategy, lead generation, sales pipeline, and CRM automation — designing systems the company had never had before.",
    mx, my, "Helvetica", 7.5, mw, color=TEXT_SECONDARY, leading=10.5)
my -= 4

# Achievements
achievements = [
    "Designed full CRM & lead tracking system in Airtable with pipeline stages from New Lead → Closed Won",
    "Built n8n automation workflows for lead capture, follow-up sequencing, and content scheduling",
    "Created bilingual (English + Gulf Arabic) outreach templates for cold DM, email, and call campaigns",
    "Developed social media content strategy targeting corporate clients, event planners, and F&B businesses",
]
for ach in achievements:
    my = draw_bullet(c, ach, mx + 2, my, "Helvetica", 7.3, mw - 4,
                     color=TEXT_SECONDARY, bullet_color=TEAL, bullet="◆")

# Tags
my -= 2
my = draw_pills_wrapped(c,
    ["#Airtable", "#n8n", "#LeadGen", "#ContentStrategy", "#SalesOps", "#MetaAds"],
    mx, my, mw, color=TEAL, font_size=6.3, gap_y=3)
my -= 4

# ── Projects ──
draw_section_header(c, "// 03 — PROJECTS", mx, my)
my -= 14
c.setFont("Courier", 6.5)
c.setFillColor(TEXT_SECONDARY)
c.drawString(mx, my, "Client demo websites built to production standard")
my -= 12

projects = [
    {
        "title": "Healy Gymnastics Academy",
        "tag": "Sports & Fitness · Kuwait",
        "url": "gaur61201.github.io/healy-gymnastics",
        "desc": "Full business website for Kuwait’s #1 gymnastics academy — bilingual copy, program listings, coach profiles, enrollment form, WhatsApp CTA.",
    },
    {
        "title": "Hair Lounge Kuwait",
        "tag": "Beauty & Wellness · Kuwait",
        "url": "gaur61201.github.io/hairlounge-kuwait",
        "desc": "Premium women’s salon site with service menu, video gallery, Google Reviews, FAQ accordion, and multi-step WhatsApp booking flow.",
    },
    {
        "title": "Waves Printing Press",
        "tag": "Live Production Site · Kuwait",
        "url": "gaur61201.github.io/waves-printing-press",
        "desc": "Bilingual business website with service showcases, lead generation CTAs, and WhatsApp integration. Live client deployment.",
    },
    {
        "title": "Lead & CRM Automation System",
        "tag": "Operations & Automation · Internal",
        "url": "Built & Tested Internally",
        "desc": "End-to-end lead management for a Kuwait printing company — Airtable CRM with pipeline stages, n8n workflows, Google Sheets reporting.",
    },
]

# Projects in 2-column grid
col_w = (mw - 14) / 2
col_x = [mx, mx + col_w + 14]
for i, proj in enumerate(projects):
    col = i % 2
    if col == 0 and i > 0:
        my = row_y_after - 6
    row_y_start = my

    cx = col_x[col]
    # Card header
    c.setFont("Courier", 6)
    c.setFillColor(TEAL)
    c.drawString(cx, my, proj["tag"].upper())
    my -= 11
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(cx, my, proj["title"])
    my -= 11
    my = draw_wrapped(c, proj["desc"], cx, my, "Helvetica", 6.8, col_w,
                      color=TEXT_SECONDARY, leading=9.5)
    my -= 1
    c.setFont("Courier", 6)
    c.setFillColor(TEAL)
    c.drawString(cx, my, "→ " + proj["url"])
    my -= 4

    if col == 0:
        # Save y for row, but reset for second column
        col_left_end_y = my
        my = row_y_start
    else:
        # End of row — take the lower y of both cards
        row_y_after = min(my, col_left_end_y)
        my = row_y_after

# ── Save ──
c.save()
print(f"PDF saved to: {OUTPUT}")
