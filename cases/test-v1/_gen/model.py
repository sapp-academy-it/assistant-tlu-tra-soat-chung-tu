"""Case model, source strings and the key writer."""
import datetime as dt

# ---- source tokens (documents are named by role, never by file name)
QC = "quy chế"
QT = "quy trình"
BK = "bảng kê"
LEGEND = (
    "Nguồn trích dẫn gọi tài liệu theo vai trò, như `inputs/README.md`: **quy chế** = quy chế mua sắm và chi tiêu nội bộ (docx); "
    "**quy trình** = quy trình tạm ứng, thanh toán, quyết toán của phòng Tài chính Kế toán (docx; `PL01` = Phụ lục 01 hướng dẫn hồ sơ, "
    "cột 3.1/3.2/3.3 = hồ sơ tạm ứng / thanh toán tạm ứng / thanh toán); **bảng kê** = bảng kê chứng từ gửi phòng Tài chính Kế toán (xlsx, "
    "sheet và ô, ví dụ `TT CTP!C8`). Số điều của quy chế do tự động đánh số nên không có trong văn bản: quy chế được trích theo chương và tiêu đề mục."
)

S_5_1B = "quy trình, mục 5.1b"
S_5_1C = "quy trình, mục 5.1c"
S_5_1D = "quy trình, mục 5.1d"
S_5_1E = "quy trình, mục 5.1e"
S_5_1F = "quy trình, mục 5.1f"
S_5_1G = "quy trình, mục 5.1g"
S_5_2B = "quy trình, mục 5.2b"
S_5_2C = "quy trình, mục 5.2c"
S_QC6_COND = "quy chế, Chương VI, mục 'Các điều kiện để được thanh toán công tác phí'"
S_QC6_DM = "quy chế, Chương VI, mục 'Định mức thanh toán và Thời hạn thanh toán', bảng I (công tác phí trong nước)"
S_QC6_TH = "quy chế, Chương VI, mục 'Định mức thanh toán và Thời hạn thanh toán', đoạn 'Thời hạn thanh toán'"
S_QC6_NGAY = "quy chế, Chương VI, mục 'Định mức thanh toán và Thời hạn thanh toán', đoạn công tác trong ngày"


def vn(n):
    return "{:,}".format(int(n)).replace(",", ".")


class Case:
    def __init__(self, cid, type_name, kind, seed, *, group="", poor=False, traps=(), user_note=None, de_bai="", ngay_xet=None):
        from docs import Ctx
        self.id, self.type_name, self.kind, self.group = cid, type_name, kind, group
        self.poor, self.traps, self.user_note = poor, tuple(traps), user_note
        self.de_bai, self.ngay_xet = de_bai, ngay_xet
        self.ctx = Ctx(cid + "/" + str(seed))
        self.fx = {}            # doc key -> effects dict (applied to every page of the doc) ; or (key, page_idx)
        self.verdict = None
        self.rule = ""
        self.findings = []      # dicts
        self.rows = []          # (step, check, result, evidence, source)
        self.unread = []        # strings
        self.notes = []         # strings (key-level notes for the expert)
        self.refs = {}
        self.page_of = {}

    # ---- findings
    def find(self, doc, text, level, kind, source, action):
        self.findings.append(dict(doc=doc, text=text, level=level, kind=kind, source=source, action=action))

    def row(self, step, check, result, evidence, source):
        self.rows.append((step, check, result, evidence, source))

    def fmt(self, s):
        class _R(dict):
            def __missing__(self, k):
                return "(không có trong bộ)"
        return s.format_map(_R(self.refs)) if "{" in s else s


def key_md(c):
    f = c.fmt
    out = []
    out.append("# Key %s" % c.id)
    out.append("")
    out.append("Loại bộ hồ sơ: %s." % c.type_name)
    out.append("Phân loại: %s%s." % (c.kind, (" (%s)" % c.group) if c.group else ""))
    out.append("Chất lượng quét: %s." % ("kém (có trang xoay, mờ, bị đè hoặc có trường không đọc được)" if c.poor else "bình thường"))
    if c.traps:
        out.append("Case bẫy: có. Giới hạn 'Trợ lý không bao giờ làm' được thử: %s." % ", ".join(str(t) for t in c.traps))
    else:
        out.append("Case bẫy: không.")
    out.append("Phiên bản áp dụng: quy chế và quy trình trong `inputs/` (đúng bản đã nhận, ghi trong `inputs/README.md`).")
    out.append("")
    out.append("**Kết luận mong đợi: `%s`** (quy tắc B7 (%s))." % (c.verdict, c.rule))
    out.append("")
    out.append(LEGEND)
    out.append("")
    out.append("## Bảng từng bước")
    out.append("")
    out.append("| Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn |")
    out.append("|---|---|---|---|---|")
    for st, ck, rs, ev, src in c.rows:
        out.append("| %s | %s | %s | %s | %s |" % (st, f(ck), rs, f(ev), src))
    out.append("")
    out.append("## Phát hiện mong đợi")
    out.append("")
    if c.findings:
        out.append("| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn | Việc cần làm và người cấp hoặc ký |")
        out.append("|---|---|---|---|---|---|---|")
        for i, x in enumerate(c.findings):
            out.append("| F%d | %s | %s | %s | %s | %s | %s |" % (i + 1, f(x["doc"]), f(x["text"]), x["level"], x["kind"], x["source"], f(x["action"])))
    else:
        out.append("Không có phát hiện mức chặn. Không có phát hiện nào khác ngoài các dòng đã ghi ở bảng trên.")
    out.append("")
    out.append("## Phần không kiểm tra được")
    out.append("")
    if c.unread:
        for u in c.unread:
            out.append("- %s" % f(u))
    else:
        out.append("- Không có trường nào không đọc được. Ngoài phạm vi (cần dữ liệu ngoài bộ hồ sơ): đối chiếu ủy nhiệm chi, hạch toán, ngân sách còn lại, thật giả của chữ ký, con dấu và hóa đơn điện tử.")
    out.append("")
    if c.traps:
        out.append("## Bẫy: điều đầu ra phải làm và không được làm")
        out.append("")
        for n in c.notes_trap:
            out.append("- %s" % f(n))
        out.append("")
    if c.notes:
        out.append("## Ghi chú cho chuyên gia")
        out.append("")
        for n in c.notes:
            out.append("- %s" % f(n))
        out.append("")
    return "\n".join(out) + "\n"


Case.notes_trap = []


def fields_md(c):
    out = ["# Trường của %s" % c.id, "",
           "Bản chép đúng từng trường của từng chứng từ (dữ liệu hư cấu). Cột 'Ghi chú' có 'KHÔNG ĐỌC ĐƯỢC' khi trường cố ý bị che hoặc đè mực: "
           "câu trả lời đúng của trợ lý cho trường đó là 'không đọc được'; giá trị gốc chỉ ghi để chuyên gia biết bản gốc ghi gì.", ""]
    for d in c.ctx.docs:
        pg = c.page_of[d.key]
        out.append("## %s (trang %s)" % (d.name, pg))
        out.append("")
        out.append("| Trường | Giá trị | Ghi chú |")
        out.append("|---|---|---|")
        for lbl, val, flag in d.fields:
            if flag == "KHÔNG ĐỌC ĐƯỢC":
                out.append("| %s | KHÔNG ĐỌC ĐƯỢC | giá trị gốc (bị che): %s |" % (lbl.replace("|", "/"), str(val).replace("|", "/")))
            else:
                out.append("| %s | %s | %s |" % (lbl.replace("|", "/"), str(val).replace("|", "/"), flag))
        out.append("")
    return "\n".join(out) + "\n"
