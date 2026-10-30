"""Page-drawing engine of the test set (all data fictional). Deterministic: every random choice comes from a seeded RNG.

Needs only Pillow and numpy and the system fonts listed in FONT_PATHS. No network. Writes nothing by itself.
"""
import os
import random
import textwrap

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1000, 1414
MARGIN = 70

FONT_PATHS = {
    "serif": ["/usr/share/fonts/liberation/LiberationSerif-Regular.ttf", "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"],
    "serifb": ["/usr/share/fonts/liberation/LiberationSerif-Bold.ttf", "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"],
    "serifi": ["/usr/share/fonts/liberation/LiberationSerif-Italic.ttf", "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"],
    "sans": ["/usr/share/fonts/TTF/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"],
    "sansb": ["/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
    "hand": ["/usr/share/fonts/TTF/DejaVuSerif-Italic.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"],
    "mono": ["/usr/share/fonts/liberation/LiberationMono-Regular.ttf", "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"],
}
_FC = {}


def font(kind, size):
    k = (kind, size)
    if k not in _FC:
        for p in FONT_PATHS[kind]:
            if os.path.exists(p):
                _FC[k] = ImageFont.truetype(p, size)
                break
        else:
            raise SystemExit("font not found for %s: install the Liberation and DejaVu fonts" % kind)
    return _FC[k]


def vn(n):
    return "{:,}".format(int(n)).replace(",", ".")


_D = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]


def _grp(n, first):
    h, t, u = n // 100, (n // 10) % 10, n % 10
    out = []
    if h > 0 or not first:
        out.append(_D[h] + " trăm")
    if t == 0:
        if u > 0 and (h > 0 or not first):
            out.append("linh")
        if u > 0:
            out.append(_D[u])
    elif t == 1:
        out.append("mười")
        if u == 5:
            out.append("lăm")
        elif u > 0:
            out.append(_D[u])
    else:
        out.append(_D[t] + " mươi")
        if u == 1:
            out.append("mốt")
        elif u == 5:
            out.append("lăm")
        elif u > 0:
            out.append(_D[u])
    return " ".join(out)


def words(n):
    """Vietnamese amount in words, e.g. 4500000 -> 'Bốn triệu năm trăm nghìn đồng'."""
    n = int(n)
    parts = []
    units = ["", " nghìn", " triệu", " tỷ"]
    groups = []
    while n > 0:
        groups.append(n % 1000)
        n //= 1000
    for i in range(len(groups) - 1, -1, -1):
        g = groups[i]
        if g == 0:
            continue
        parts.append(_grp(g, i == len(groups) - 1) + units[i])
    s = " ".join(parts) if parts else "không"
    return s[0].upper() + s[1:] + " đồng"


def noaccent(s):
    import unicodedata
    s = s.replace("Đ", "D").replace("đ", "d")
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


class Doc:
    """One voucher. Draws on one or more pages and records every field it draws (for fields.md)."""

    def __init__(self, key, name, rng, ink=(15, 15, 15)):
        self.key, self.name, self.rng = key, name, rng
        self.pages = []
        self.effects = []          # one dict per page
        self.fields = []           # (label, value, flag)
        self.ink = ink
        self.new_page()

    # ---- page handling
    def new_page(self, **effects):
        im = Image.new("RGB", (W, H), (255, 255, 255))
        self.pages.append(im)
        self.effects.append(effects)
        self.d = ImageDraw.Draw(im)
        self.y = MARGIN
        self.foot()

    def foot(self):
        self.d.text((W // 2, H - 34), "Dữ liệu hư cấu, chỉ dùng để kiểm thử", font=font("sans", 12), fill=(165, 165, 165), anchor="mm")

    def set_effect(self, **e):
        self.effects[-1].update(e)

    def room(self, h):
        if self.y + h > H - 70:
            fx = dict(self.effects[-1])
            self.new_page(**fx)

    # ---- text
    def text(self, x, y, s, kind="serif", size=22, fill=None, anchor="la"):
        self.d.text((x, y), s, font=font(kind, size), fill=fill or self.ink, anchor=anchor)

    def width(self, s, kind="serif", size=22):
        return self.d.textlength(s, font=font(kind, size))

    def center(self, s, kind="serifb", size=26, gap=8):
        self.room(size + gap)
        self.text(W // 2, self.y, s, kind, size, anchor="ma")
        self.y += size + gap

    def line(self, s, kind="serif", size=22, x=MARGIN, gap=6):
        self.room(size + gap)
        self.text(x, self.y, s, kind, size)
        self.y += size + gap

    def para(self, s, kind="serif", size=22, x=MARGIN, gap=8, indent=0):
        maxw = W - x - MARGIN
        chars = max(10, int(maxw / (size * 0.5)))
        first = True
        for ln in textwrap.wrap(s, chars):
            self.room(size + gap)
            self.text(x + (indent if first else 0), self.y, ln, kind, size)
            self.y += size + gap
            first = False
        self.y += 4

    def gap(self, h=12):
        self.y += h

    def rule(self, x0=MARGIN, x1=W - MARGIN, w=2):
        self.d.line([(x0, self.y), (x1, self.y)], fill=self.ink, width=w)
        self.y += 8

    def header2(self, left_top, left_bot, right_top="CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", right_bot="Độc lập - Tự do - Hạnh phúc"):
        y = self.y
        self.text(MARGIN + 190, y, left_top, "serif", 19, anchor="ma")
        self.text(MARGIN + 190, y + 24, left_bot, "serifb", 20, anchor="ma")
        self.text(W - MARGIN - 230, y, right_top, "serifb", 17, anchor="ma")
        self.text(W - MARGIN - 230, y + 24, right_bot, "serifb", 19, anchor="ma")
        self.d.line([(W - MARGIN - 330, y + 52), (W - MARGIN - 130, y + 52)], fill=self.ink, width=2)
        self.y = y + 70

    # ---- fields
    def rec(self, label, value, flag=""):
        self.fields.append((label, value, flag))

    def hand_text(self, x, y, s, size=24, color=(25, 35, 140)):
        cx = x
        for ch in s:
            dy = self.rng.randint(-2, 2)
            f = font("hand", size)
            self.d.text((cx, y + dy), ch, font=f, fill=color)
            cx += self.d.textlength(ch, font=f) + self.rng.choice([0, 0, 1])
        return cx

    def smear(self, x0, y0, x1, y1):
        """Cover a region with an ink scribble so the text under it cannot be read."""
        for _ in range(int((x1 - x0) / 4) + 6):
            a = (self.rng.randint(int(x0), int(x1)), self.rng.randint(int(y0), int(y1)))
            b = (a[0] + self.rng.randint(-25, 25), self.rng.randint(int(y0), int(y1)))
            self.d.line([a, b], fill=(30, 30, 30), width=self.rng.randint(5, 9))

    def kv(self, label, value, x=MARGIN, hand=False, ill=False, size=22, kind="serif", maxx=None, rec=True, dots=True, flag=""):
        """label ........ value on one line; records the field."""
        self.room(size + 14)
        y = self.y
        self.text(x, y, label, kind, size)
        vx = x + self.width(label + " ", kind, size) + 4
        maxx = maxx or (W - MARGIN)
        if dots:
            dx = vx
            while dx < maxx:
                self.d.text((dx, y + 4), ".", font=font("serif", size), fill=(120, 120, 120))
                dx += 9
        value = "" if value is None else str(value)
        if value:
            if hand:
                ex = self.hand_text(vx + 4, y - 2, value, size=size + 2)
            else:
                self.text(vx + 4, y, value, kind if kind != "serif" else "serif", size)
                ex = vx + 4 + self.width(value, kind, size)
            if ill:
                self.smear(vx, y - 2, ex + 6, y + size + 4)
        if rec:
            self.rec(label.rstrip(": ").rstrip(), value if value else "(để trống)", "KHÔNG ĐỌC ĐƯỢC" if ill else flag)
        self.y += size + 12

    def box(self, x0, y0, x1, y1, w=2):
        self.d.rectangle([x0, y0, x1, y1], outline=self.ink, width=w)

    def table(self, headers, rows, colw, size=20, label=None, hand_cols=(), ill_cells=(), aligns=None, rowh=None, rec=True, bold_last=False):
        """colw: relative widths. rows: list of list of str. ill_cells: set of (row, col) smeared. Records every cell."""
        total = W - 2 * MARGIN
        sc = total / float(sum(colw))
        xs = [MARGIN]
        for c in colw:
            xs.append(xs[-1] + c * sc)
        rh = rowh or (size + 18)
        aligns = aligns or ["l"] * len(headers)
        self.room(rh * 2)
        y0 = self.y
        # header
        for i, h in enumerate(headers):
            self.text((xs[i] + xs[i + 1]) / 2, y0 + 8, h, "serifb", size - 1, anchor="ma")
        self.d.line([(MARGIN, y0), (W - MARGIN, y0)], fill=self.ink, width=2)
        y = y0 + rh
        self.d.line([(MARGIN, y), (W - MARGIN, y)], fill=self.ink, width=2)
        for ri, row in enumerate(rows):
            self.room(rh + 4)
            for ci, cell in enumerate(row):
                cell = "" if cell is None else str(cell)
                cx0, cx1 = xs[ci] + 6, xs[ci + 1] - 6
                lines = [cell] if self.width(cell, "serif", size) <= (cx1 - cx0) else textwrap.wrap(cell, max(6, int((cx1 - cx0) / (size * 0.5))))[:2]
                for li, ln in enumerate(lines):
                    ty = y + 7 + li * (size + 2)
                    if aligns[ci] == "r":
                        tx = cx1 - self.width(ln, "serif", size)
                    elif aligns[ci] == "c":
                        tx = (cx0 + cx1) / 2 - self.width(ln, "serif", size) / 2
                    else:
                        tx = cx0
                    kind = "serifb" if (bold_last and ri == len(rows) - 1) else "serif"
                    if ci in hand_cols and ln:
                        self.hand_text(tx, ty - 2, ln, size=size)
                    else:
                        self.text(tx, ty, ln, kind, size)
                    if (ri, ci) in ill_cells and ln:
                        self.smear(tx - 2, ty - 2, tx + self.width(ln, "serif", size) + 4, ty + size + 4)
                if rec:
                    nm = "%s, dòng %d, %s" % (label or "bảng", ri + 1, headers[ci])
                    self.rec(nm, cell if cell else "(để trống)", "KHÔNG ĐỌC ĐƯỢC" if (ri, ci) in ill_cells else "")
            y += rh
            self.d.line([(MARGIN, y), (W - MARGIN, y)], fill=self.ink, width=1)
        for x in xs:
            self.d.line([(x, y0), (x, y)], fill=self.ink, width=1)
        self.y = y + 14

    # ---- signatures and stamps
    def squiggle(self, cx, cy, scale=1.0):
        pts = []
        n = self.rng.randint(7, 10)
        x = cx - 55 * scale
        for i in range(n):
            x += self.rng.uniform(8, 17) * scale
            pts.append((x, cy + self.rng.uniform(-22, 22) * scale))
        col = (18, 28, 120)
        for i in range(len(pts) - 1):
            self.d.line([pts[i], pts[i + 1]], fill=col, width=3)
        self.d.line([(pts[0][0] - 10, pts[0][1] + 24 * scale), (pts[-1][0] + 20, pts[-1][1] - 6 * scale)], fill=col, width=2)

    def sig_block(self, sigs, title_size=19, gap_after=20, rec=True):
        """sigs: list of (role, printed_name, signed). Draws roles in a row, with a signature squiggle when signed."""
        self.room(150)
        n = len(sigs)
        cw = (W - 2 * MARGIN) / float(n)
        y = self.y
        for i, (role, nm, signed) in enumerate(sigs):
            cx = MARGIN + cw * i + cw / 2
            self.text(cx, y, role, "serifb", title_size, anchor="ma")
            self.text(cx, y + 24, "(Ký, họ tên)", "serifi", 16, anchor="ma")
            if signed:
                self.squiggle(cx, y + 76)
            if nm:
                self.text(cx, y + 118, nm, "serifb", 19, anchor="ma")
            if rec:
                self.rec("Chữ ký: " + role, "có" if signed else "không có (để trống)", "")
        self.y = y + 150 + gap_after

    def stamp(self, cx, cy, l1, l2="", r=62, color=(200, 30, 30), alpha=170, rec_label=None, tilt=None):
        lay = Image.new("RGBA", (r * 2 + 20, r * 2 + 20), (0, 0, 0, 0))
        ld = ImageDraw.Draw(lay)
        c = r + 10
        ld.ellipse([c - r, c - r, c + r, c + r], outline=color + (alpha,), width=4)
        ld.ellipse([c - r + 9, c - r + 9, c + r - 9, c + r - 9], outline=color + (alpha,), width=1)
        f1, f2 = font("sansb", 13), font("sans", 12)
        ld.text((c, c - 8), l1, font=f1, fill=color + (alpha,), anchor="mm")
        if l2:
            ld.text((c, c + 12), l2, font=f2, fill=color + (alpha,), anchor="mm")
        lay = lay.rotate(tilt if tilt is not None else self.rng.uniform(-14, 14), resample=Image.BICUBIC)
        self.pages[-1].paste(lay, (int(cx - c), int(cy - c)), lay)
        if rec_label:
            self.rec("Dấu: " + rec_label, "có", "")

    def finish_page_text(self):
        pass


# ---------- scan effects (applied to a finished page) ----------

def apply_effects(im, fx, seed):
    rng = np.random.RandomState(seed)
    if not fx:
        fx = {}
    base = fx.get("base", "ok")  # ok | scan | poor
    g = im.convert("L")
    if fx.get("blur"):
        g = g.filter(ImageFilter.GaussianBlur(fx["blur"]))
    if fx.get("lowres"):
        s = fx["lowres"]
        g = g.resize((int(g.width * s), int(g.height * s)), Image.BILINEAR).resize((g.width, g.height), Image.BILINEAR)
    a = np.asarray(g, dtype=np.float32)
    # a mild scanner look on every page: slight tone and light noise
    noise = fx.get("noise", 1.5)
    a = a * (1 - 0.04) + 8 + rng.normal(0, noise, a.shape)
    if fx.get("shadow"):
        grad = np.linspace(0, fx["shadow"], a.shape[1], dtype=np.float32)[None, :]
        a = a - grad
    if fx.get("contrast"):
        a = 128 + (a - 128) * fx["contrast"] + (255 - 128) * (1 - fx["contrast"]) * 0.6
    a = np.clip(a, 0, 255).astype(np.uint8)
    out = Image.fromarray(a, "L")
    if fx.get("skew"):
        out = out.rotate(fx["skew"], resample=Image.BICUBIC, fillcolor=235, expand=False)
    if fx.get("rot"):
        out = out.rotate(fx["rot"], expand=True, fillcolor=235)
    return out
