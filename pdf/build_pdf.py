"""Reusable PDF builder for SBTE Bihar Civil 3rd Sem practical files."""

import io
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, PageTemplate, Paragraph, Spacer, Table,
    TableStyle, PageBreak, Flowable,
)

NAVY = colors.HexColor("#12355B")
ACCENT = colors.HexColor("#B03A2E")
GREY = colors.HexColor("#5A6570")
LIGHT = colors.HexColor("#EDF1F7")
LINE = colors.HexColor("#9AA6B2")
INCLUDE_REF = False

PAGE_W, PAGE_H = A4
M_LEFT = 16 * mm
M_RIGHT = 15 * mm
M_TOP = 13 * mm
M_BOT = 12 * mm

BODY = 8.5
LEAD = 10.9


def styles():
    ss = getSampleStyleSheet()
    s = {}
    s["body"] = ParagraphStyle(
        "body", parent=ss["BodyText"], fontName="Helvetica", fontSize=BODY,
        leading=LEAD, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1B1B1B"),
        spaceAfter=1.0,
    )
    s["small"] = ParagraphStyle(
        "small", parent=s["body"], fontSize=8, leading=10.5, textColor=GREY,
    )
    s["h1"] = ParagraphStyle(
        "h1", parent=s["body"], fontName="Helvetica-Bold", fontSize=15.5, leading=19,
        textColor=NAVY, alignment=TA_LEFT, spaceAfter=4,
    )
    s["subject"] = ParagraphStyle(
        "subject", parent=s["body"], fontName="Helvetica-Bold", fontSize=12, leading=15,
        textColor=colors.white, alignment=TA_LEFT,
    )
    s["label"] = ParagraphStyle(
        "label", parent=s["body"], fontName="Helvetica-Bold", fontSize=8.7, leading=10.8,
        textColor=NAVY, spaceBefore=1.9, spaceAfter=0.4, alignment=TA_LEFT,
    )
    s["cell"] = ParagraphStyle(
        "cell", parent=s["body"], fontSize=7.6, leading=9.4, alignment=TA_LEFT,
        spaceAfter=0,
    )
    s["cellc"] = ParagraphStyle(
        "cellc", parent=s["cell"], alignment=TA_CENTER,
    )
    s["cellh"] = ParagraphStyle(
        "cellh", parent=s["cell"], fontName="Helvetica-Bold", textColor=colors.white,
    )
    s["cellhc"] = ParagraphStyle(
        "cellhc", parent=s["cellh"], alignment=TA_CENTER,
    )
    s["bullet"] = ParagraphStyle(
        "bullet", parent=s["body"], leftIndent=10, bulletIndent=2, spaceAfter=0.6,
    )
    s["num"] = ParagraphStyle(
        "num", parent=s["body"], leftIndent=13, bulletIndent=2, spaceAfter=0.6,
    )
    s["cover_title"] = ParagraphStyle(
        "ct", parent=s["body"], fontName="Helvetica-Bold", fontSize=27, leading=32,
        textColor=NAVY, alignment=TA_CENTER,
    )
    s["cover_sub"] = ParagraphStyle(
        "cs", parent=s["body"], fontSize=11.5, leading=15, textColor=GREY,
        alignment=TA_CENTER,
    )
    return s


S = styles()


class PracHeading(Flowable):
    """Coloured banner that carries the practical number heading."""

    def __init__(self, num, title, subtitle="", label="PRACTICAL  NO."):
        self.label = label
        Flowable.__init__(self)
        self.num = num
        self.title = title
        self.subtitle = subtitle
        self._prac_num = num
        self.height = 0
        self.width = PAGE_W - M_LEFT - M_RIGHT

    def wrap(self, aw, ah):
        self.width = aw
        t = Paragraph(self.title, S["subject"])
        tw, th = t.wrap(aw - 26 * mm, ah)
        self._t = t
        self._tw, self._th = tw, th
        self.height = max(12.5 * mm, th + 7.2 * mm)
        return (aw, self.height)

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(NAVY)
        c.rect(0, 0, w, h, stroke=0, fill=1)
        c.setFillColor(ACCENT)
        c.rect(0, 0, 3.2 * mm, h, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 7.6)
        c.drawString(6.5 * mm, h - 5.4 * mm, "%s  %02d" % (self.label, self.num))
        c.setStrokeColor(colors.HexColor("#7FA0C4"))
        c.setLineWidth(0.5)
        c.line(6.5 * mm, h - 7.4 * mm, w - 6 * mm, h - 7.4 * mm)
        self._t.drawOn(c, 6.5 * mm, h - 8.0 * mm - self._th + 1.2 * mm)


class Rule(Flowable):
    def __init__(self, w=None, color=LINE, thickness=0.6, space=2):
        Flowable.__init__(self)
        self._w = w
        self.color = color
        self.thickness = thickness
        self.space = space
        self.height = space * 2 + thickness

    def wrap(self, aw, ah):
        self.width = self._w or aw
        return (self.width, self.height)

    def draw(self):
        c = self.canv
        c.setStrokeColor(self.color)
        c.setLineWidth(self.thickness)
        c.line(0, self.space, self.width, self.space)


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *a, **kw):
        canvas.Canvas.__init__(self, *a, **kw)
        self._states = []

    def showPage(self):
        self._states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._states)
        for st in self._states:
            self.__dict__.update(st)
            if self._pageNumber > 1:
                self._footer(total)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def _footer(self, total):
        self.setStrokeColor(LINE)
        self.setLineWidth(0.5)
        self.line(M_LEFT, M_BOT - 4 * mm, PAGE_W - M_RIGHT, M_BOT - 4 * mm)
        self.setFont("Helvetica", 7.6)
        self.setFillColor(GREY)
        self.drawString(M_LEFT, M_BOT - 8 * mm, self._subj)
        self.drawRightString(PAGE_W - M_RIGHT, M_BOT - 8 * mm, "Page %d of %d" % (self._pageNumber, total))


class SubjectDoc(BaseDocTemplate):
    def __init__(self, target, meta, page_map=None, **kw):
        BaseDocTemplate.__init__(
            self, target, pagesize=A4, leftMargin=M_LEFT, rightMargin=M_RIGHT,
            topMargin=M_TOP, bottomMargin=M_BOT, title=meta["title"],
            author=meta.get("author", "Civil Engineering Department"),
            subject=meta["title"], **kw,
        )
        self.meta = meta
        self.page_map = page_map if page_map is not None else {}
        frame = Frame(M_LEFT, M_BOT, PAGE_W - M_LEFT - M_RIGHT,
                      PAGE_H - M_TOP - M_BOT, id="body",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=self._deco)])

    def _deco(self, canv, doc):
        canv._subj = self.meta["footer"]

    def afterFlowable(self, flowable):
        n = getattr(flowable, "_prac_num", None)
        if n:
            self.page_map[n] = self.page


def header_block(meta, s):
    """Running header printed on content pages."""
    subj = meta["subject"]
    code = meta["code"]
    line = Table(
        [[Paragraph(f"<b>{subj}</b>", ParagraphStyle(
            "hh", parent=s["body"], fontSize=8.2, textColor=NAVY, alignment=TA_LEFT)),
          Paragraph(f"Course Code: {code} &nbsp;|&nbsp; Semester III &nbsp;|&nbsp; SBTE, Bihar",
                    ParagraphStyle("hh2", parent=s["body"], fontSize=7.4, textColor=GREY,
                                   alignment=2))]],
        colWidths=[78 * mm, (PAGE_W - M_LEFT - M_RIGHT) - 78 * mm],
    )
    line.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 0),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                              ("TOPPADDING", (0, 0), (-1, -1), 0)]))
    return line


def bullets(items, style="bullet", bullet="\u2022"):
    return [Paragraph(t, S[style], bulletText=bullet) for t in items]


def numbered(items):
    out = []
    for i, t in enumerate(items, 1):
        out.append(Paragraph(t, S["num"], bulletText="%d." % i))
    return out


def obs_table(header, rows=None, widths=None, note=None):
    header = header or []
    rows = rows or []
    data = [[Paragraph(h, S["cellhc" if i else "cellh"]) for i, h in enumerate(header)]]
    for r in rows:
        data.append([Paragraph(str(c), S["cellc"]) for c in r])
    if not rows:
        for _ in range(4):
            data.append([Paragraph("&nbsp;", S["cellc"]) for _ in header])
    ncol = len(header)
    avail = PAGE_W - M_LEFT - M_RIGHT
    if widths:
        total = sum(widths)
        colw = [avail * w / total for w in widths]
    else:
        colw = [avail / ncol] * ncol
    t = Table(data, colWidths=colw, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 1.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F9FC")]),
    ]))
    out = [Spacer(1, 2.5), t]
    if note:
        out += [Spacer(1, 2), Paragraph(note, S["small"])]
    return out


def two_col_bullets(items):
    """Place short bullet items in two columns to save vertical space."""
    half = (len(items) + 1) // 2
    left, right = items[:half], items[half:]
    bw = ParagraphStyle("bt", parent=S["body"], leftIndent=9, bulletIndent=1, spaceAfter=0.4)
    cells = []
    for col in (left, right):
        cells.append([Paragraph(t, bw, bulletText="\u2022") for t in col] or [Paragraph("", bw)])
    avail = PAGE_W - M_LEFT - M_RIGHT
    t = Table([[cells[0], cells[1]]], colWidths=[avail / 2.0 - 2 * mm, avail / 2.0 + 2 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


def cover(meta):
    """Student-fillable cover page."""
    out = []
    out.append(Spacer(1, 12 * mm))
    band = Table([[Paragraph("STATE BOARD OF TECHNICAL EDUCATION, BIHAR", ParagraphStyle(
        "b1", parent=S["body"], fontName="Helvetica-Bold", fontSize=9.5,
        textColor=colors.white, alignment=TA_CENTER))]],
        colWidths=[PAGE_W - M_LEFT - M_RIGHT], rowHeights=[9 * mm])
    band.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY),
                              ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    out.append(band)
    out.append(Spacer(1, 14 * mm))
    out.append(Paragraph("LABORATORY", S["cover_sub"]))
    out.append(Paragraph("PRACTICAL FILE", S["cover_title"]))
    out.append(Spacer(1, 3 * mm))
    out.append(Rule(color=ACCENT, thickness=1.4, space=1))
    out.append(Spacer(1, 6 * mm))
    out.append(Paragraph(meta["subject"].upper(), ParagraphStyle(
        "cn", parent=S["body"], fontName="Helvetica-Bold", fontSize=16, leading=20,
        textColor=ACCENT, alignment=TA_CENTER)))
    out.append(Spacer(1, 2.5 * mm))
    out.append(Paragraph(f"Course Code: {meta['code']}", S["cover_sub"]))
    out.append(Spacer(1, 2 * mm))
    out.append(Paragraph("Diploma in Civil Engineering &nbsp;&bull;&nbsp; Semester III",
                         S["cover_sub"]))
    out.append(Spacer(1, 16 * mm))

    rows = [["Student's Name", ""], ["Enrollment No.", ""], ["Roll No.", ""],
            ["Branch", "Civil Engineering"], ["Semester", "III"],
            ["Session", "20____ &ndash; 20____"], ["Name of Institute", ""]]
    data = []
    for k, v in rows:
        data.append([Paragraph(k, ParagraphStyle("ck", parent=S["cell"], fontName="Helvetica-Bold",
                                                 textColor=NAVY, fontSize=9.5)),
                     Paragraph(v or "", ParagraphStyle("cv", parent=S["cell"], fontSize=9.5))])
    t = Table(data, colWidths=[52 * mm, 88 * mm], rowHeights=[10.5 * mm] * len(data), hAlign="CENTER")
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.6, LINE),
        ("BACKGROUND", (0, 0), (0, -1), LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ]))
    out.append(t)
    out.append(Spacer(1, 26 * mm))
    out.append(Paragraph("Department of Civil Engineering", ParagraphStyle(
        "dep", parent=S["body"], fontName="Helvetica-Bold", fontSize=10.5,
        alignment=TA_CENTER, textColor=NAVY)))
    out.append(Spacer(1, 2 * mm))
    out.append(Paragraph("(Name &amp; address of the institute)", ParagraphStyle("sml", parent=S["small"], alignment=TA_CENTER)))
    out.append(PageBreak())
    return out


def instructions(meta, notes):
    out = [header_block(meta, S), Spacer(1, 6), Rule(), Spacer(1, 8)]
    out.append(Paragraph("How to write this file", S["h1"]))
    out.append(Paragraph(
        "Is file ke har practical ko nimn likhit format mein likha gaya hai. "
        "Apne college ke lab manual se practical ki sankhya aur readings confirm karke "
        "observation table mein apni actual readings bharein — yahan di gayi readings "
        "sample hain, sirf samajhne ke liye.", S["body"]))
    out.append(Spacer(1, 3))
    items = [
        "<b>Aim</b> — practical ka uddeshya ek line mein.",
        "<b>Apparatus</b> — naam aur specification (capacity, IS code).",
        "<b>Theory / Formula</b> — principle aur formula jo calculation mein use hua.",
        "<b>Procedure</b> — step-wise, past tense mein, chhote vakya.",
        "<b>Observation table</b> — readings, units ke saath; IS code ka reference.",
        "<b>Calculation</b> — formula lagakar steps dikhayein.",
        "<b>Result</b> — answer with unit aur IS permissible limit ke saath.",
        "<b>Precautions</b> — 3 se 4 points.",
    ]
    out += bullets(items)
    out.append(Spacer(1, 6))
    out.append(Paragraph("General instructions", S["label"]))
    out += bullets([
        "Har practical ke baad date aur teacher ke signature zaroor lein.",
        "Diagram pencil se, scale se banayein; likhai blue/black pen se.",
        "Index page mein page number bharna na bhoolein — file check ke waqt yahi dekha jata hai.",
        "Practical exam (ELA) mein viva hota hai — aim, formula aur result yaad rakhein.",
    ])
    if notes:
        out.append(Spacer(1, 6))
        out.append(Paragraph("Subject specific note", S["label"]))
        out += [Paragraph(n, S["body"]) for n in notes]
    out.append(PageBreak())
    return out


def index_page(meta, practicals, page_map):
    out = [header_block(meta, S), Spacer(1, 6), Rule(), Spacer(1, 8)]
    out.append(Paragraph("Index", S["h1"]))
    out.append(Paragraph(meta["index_note"], S["small"]))
    out.append(Spacer(1, 5))
    avail = PAGE_W - M_LEFT - M_RIGHT
    head = ["S. No.", "Title of the Practical", "Page No.", "Date", "Signature"]
    data = [[Paragraph(h, S["cellhc"]) for h in head]]
    for p in practicals:
        pg = page_map.get(p["num"], "")
        data.append([
            Paragraph("%02d" % p["num"], S["cellc"]),
            Paragraph(p["title"].replace("&", "&amp;"), S["cell"]),
            Paragraph(str(pg), S["cellc"]),
            Paragraph("", S["cellc"]),
            Paragraph("", S["cellc"]),
        ])
    colw = [avail * w for w in (0.075, 0.60, 0.105, 0.10, 0.12)]
    t = Table(data, colWidths=colw, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F9FC")]),
    ]))
    out.append(t)
    out.append(PageBreak())
    return out


def practical_page(p, meta):
    out = [header_block(meta, S), Spacer(1, 5)]
    out.append(PracHeading(p["num"], p["title"], label=meta.get("item_label", "PRACTICAL  NO.")))
    out.append(Spacer(1, 5))

    if p.get("aim"):
        out.append(Paragraph("Aim", S["label"]))
        out.append(Paragraph(p["aim"], S["body"]))

    if p.get("apparatus"):
        out.append(Paragraph("Apparatus / Equipment Required", S["label"]))
        out.append(Paragraph("; ".join(a.rstrip(".") for a in p["apparatus"]) + ".", S["body"]))

    if p.get("theory"):
        out.append(Paragraph("Theory", S["label"]))
        out += [Paragraph(t, S["body"]) for t in p["theory"]]

    if p.get("formula"):
        out.append(Paragraph("Formulae Used", S["label"]))
        out += bullets(p["formula"])

    if p.get("procedure"):
        out.append(Paragraph("Procedure", S["label"]))
        out += numbered(p["procedure"])

    if p.get("observation"):
        out.append(Paragraph("Observation", S["label"]))
        o = p["observation"]
        if isinstance(o, dict):
            out += obs_table(o.get("header"), o.get("rows"), o.get("widths"), o.get("note"))
        else:
            out.append(Paragraph(o, S["body"]))

    if p.get("calculation"):
        out.append(Paragraph("Calculation", S["label"]))
        out += [Paragraph(t, S["body"]) for t in p["calculation"]]

    if p.get("result"):
        out.append(Paragraph("Result", S["label"]))
        out.append(Paragraph(p["result"], S["body"]))

    if p.get("precautions"):
        out.append(Paragraph("Precautions", S["label"]))
        out.append(two_col_bullets(p["precautions"]))

    if p.get("code") and INCLUDE_REF:
        out.append(Paragraph("Reference: " + p["code"], S["small"]))

    sig = Table([[Paragraph("Date: ____________________", S["cell"]),
                  Paragraph("Teacher's Signature: ____________________",
                            ParagraphStyle("sg", parent=S["cell"], alignment=2))]],
                colWidths=[(PAGE_W - M_LEFT - M_RIGHT) * 0.40,
                           (PAGE_W - M_LEFT - M_RIGHT) * 0.60])
    sig.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 0.5, LINE),
                             ("TOPPADDING", (0, 0), (-1, -1), 2),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                             ("LEFTPADDING", (0, 0), (-1, -1), 0),
                             ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    out.append(KeepTogether([Spacer(1, 2), sig]))
    out.append(PageBreak())
    return out


def references_page(meta, practicals):
    out = [header_block(meta, S), Spacer(1, 5), Rule(), Spacer(1, 7)]
    out.append(Paragraph("References and Useful Standards", S["h1"]))
    out.append(Paragraph(
        "Practical file likhne ke liye nimnlikhit textbooks, IS codes aur curriculum outcomes ka "
        "sahayata liya gaya hai. Viva mein IS code number poochhe jaate hain, isliye inhe ek baar "
        "zaroor padh lein.", S["body"]))
    out.append(Spacer(1, 4))

    refs = list(meta.get("references") or [])
    if not refs:
        seen = set()
        for pr in practicals:
            code = (pr.get("code") or "").strip()
            if code and code not in seen:
                seen.add(code)
                refs.append("Practical %02d — %s" % (pr["num"], code))

    data = [[Paragraph("S. No.", S["cellhc"]), Paragraph("Reference / Standard", S["cellh"])]]
    for i, r in enumerate(refs, 1):
        data.append([Paragraph(str(i), S["cellc"]), Paragraph(r, S["cell"])])
    avail = PAGE_W - M_LEFT - M_RIGHT
    t = Table(data, colWidths=[avail * 0.09, avail * 0.91], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F9FC")]),
    ]))
    out.append(t)
    out.append(Spacer(1, 8))
    out.append(Paragraph(
        "<b>Note:</b> Is file mein di gayi observation readings sample hain — samajhne aur format ke liye. "
        "Apne practical class mein actual readings le kar observation table dobara bharein aur result "
        "calculate karein. Practical ki sankhya apne college ke lab manual ke anusaar ho sakti hai.", S["small"]))
    return out


def build(meta, practicals, out_path, notes=None):
    """Two-pass build so that the index gets real page numbers."""

    def story(page_map):
        st = []
        st += cover(meta)
        st += instructions(meta, notes)
        st += index_page(meta, practicals, page_map)
        for p in practicals:
            st += practical_page(p, meta)
        st += references_page(meta, practicals)
        return st

    buf = io.BytesIO()
    d1 = SubjectDoc(buf, meta)
    d1.build(story({}))
    page_map = dict(d1.page_map)

    d2 = SubjectDoc(out_path, meta, page_map=page_map)
    d2.build(story(page_map))
    return page_map


def generic_page(item, meta):
    """Page for term-work items built from a list of content blocks."""
    out = [header_block(meta, S), Spacer(1, 5)]
    out.append(PracHeading(item["num"], item["title"], label=meta.get("item_label", "PRACTICAL  NO.")))
    out.append(Spacer(1, 5))
    for b in item["blocks"]:
        if "h" in b:
            out.append(Paragraph(b["h"], S["label"]))
        if "p" in b:
            out += [Paragraph(t, S["body"]) for t in b["p"]]
        if "ul" in b:
            out += bullets(b["ul"])
        if "ol" in b:
            out += numbered(b["ol"])
        if "table" in b:
            t = b["table"]
            out += obs_table(t.get("header"), t.get("rows"), t.get("widths"), t.get("note"))
    out.append(Spacer(1, 6))
    sig = Table([[Paragraph("Date: ____________________", S["cell"]),
                  Paragraph("Teacher's Signature: ____________________",
                            ParagraphStyle("sg2", parent=S["cell"], alignment=2))]],
                colWidths=[(PAGE_W - M_LEFT - M_RIGHT) * 0.40,
                           (PAGE_W - M_LEFT - M_RIGHT) * 0.60])
    sig.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 0.5, LINE),
                             ("TOPPADDING", (0, 0), (-1, -1), 2),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                             ("LEFTPADDING", (0, 0), (-1, -1), 0),
                             ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    out.append(sig)
    out.append(PageBreak())
    return out


def build_generic(meta, items, out_path, notes=None):
    """Two-pass build for term-work style files."""

    def story(page_map):
        st = []
        st += cover(meta)
        st += instructions(meta, notes)
        st += index_page(meta, items, page_map)
        for it in items:
            st += generic_page(it, meta)
        st += references_page(meta, items)
        return st

    buf = io.BytesIO()
    d1 = SubjectDoc(buf, meta)
    d1.build(story({}))
    page_map = dict(d1.page_map)
    d2 = SubjectDoc(out_path, meta, page_map=page_map)
    d2.build(story(page_map))
    return page_map
