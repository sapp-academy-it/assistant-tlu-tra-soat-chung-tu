"""Voucher templates (all data fictional). Each builder draws one voucher into a Doc and returns it."""
import datetime as dt
import random

from engine import Doc, W, H, MARGIN, vn, words, noaccent

SCHOOL = "Trường Đại học Thăng Long"
SCHOOL_MST = "0101825712"
SCHOOL_ADDR = "Đường Nghiêm Xuân Yêm, Phường Định Công, Thành phố Hà Nội"
SCHOOL_UP = "TRƯỜNG ĐẠI HỌC THĂNG LONG"
HT = "Phan Văn Q"      # Hiệu trưởng (fictional)
KTT = "Trịnh Thị R"    # Kế toán trưởng
TPTC = "Đinh Văn S"    # Trưởng phòng TCKT


def D(d):
    return d.strftime("%d/%m/%Y")


def date_line(d, place="Hà Nội"):
    return "%s, ngày %02d tháng %02d năm %d" % (place, d.day, d.month, d.year)


class Ctx:
    def __init__(self, seed):
        self.seed = seed
        self.docs = []

    def doc(self, key, name):
        rng = random.Random("%s/%s" % (self.seed, key))
        d = Doc(key, name, rng)
        self.docs.append(d)
        return d


# ---------------------------------------------------------------- forms

def dntt(ctx, key="dntt", name="Giấy đề nghị thanh toán", don_vi="", ngay=None, nguoi="", bo_phan="", noi_dung="", amount=0,
         amount_words=None, httt="CK", tk=("", "", ""), kem="", signed=(True, True, True, True), ill=(), names=None, so_ma="Mẫu số 05 - TT", tamung_cu=None):
    """names: dict role->printed name. ill: set of field labels to smear (amount, words)."""
    d = ctx.doc(key, name)
    names = names or {}
    d.text(MARGIN, d.y, SCHOOL_UP, "serifb", 20)
    d.text(W - MARGIN, d.y, so_ma, "serifb", 20, anchor="ra")
    d.y += 30
    d.kv("Đơn vị:", don_vi, x=MARGIN, hand=True)
    d.gap(6)
    d.center("GIẤY ĐỀ NGHỊ THANH TOÁN", "serifb", 30, 6)
    d.center("Ngày %02d tháng %02d năm %d" % (ngay.day, ngay.month, ngay.year), "serifi", 21, 14)
    d.rec("Ngày lập", D(ngay))
    d.line("Kính gửi: Ban Giám hiệu; Phòng Tài chính - Kế toán", "serif", 22)
    d.kv("Họ và tên người đề nghị thanh toán:", nguoi, hand=True)
    d.kv("Bộ phận (hoặc địa chỉ):", bo_phan, hand=True)
    d.kv("Nội dung thanh toán:", noi_dung, hand=True)
    d.kv("Số tiền (bằng số):", vn(amount) + " đ" if amount is not None else "", hand=True, ill=("amount" in ill))
    d.kv("Số tiền (bằng chữ):", amount_words if amount_words is not None else words(amount), hand=True, ill=("words" in ill))
    d.kv("Kèm theo:", kem, hand=True)
    d.gap(6)
    d.line("Hình thức thanh toán:", "serifb", 22)
    chk = lambda b: "☒" if b else "☐"
    d.room(34)
    d.text(MARGIN + 20, d.y, "%s Tiền mặt        %s Chuyển khoản" % (chk(httt == "TM"), chk(httt == "CK")), "sans", 21)
    d.rec("Hình thức thanh toán", "Tiền mặt" if httt == "TM" else "Chuyển khoản")
    d.y += 38
    if httt == "CK":
        d.kv("Số tài khoản thụ hưởng:", tk[0], hand=True)
        d.kv("Ngân hàng:", tk[1], hand=True)
        d.kv("Chủ tài khoản:", tk[2], hand=True)
    if tamung_cu:
        d.kv("Số tạm ứng kỳ trước chưa thanh toán:", tamung_cu, hand=True)
    d.gap(8)
    d.sig_block([("Hiệu trưởng", names.get("HT", HT), signed[0]), ("Kế toán trưởng", names.get("KTT", KTT), signed[1]),
                 ("Trưởng đơn vị", names.get("TDV", ""), signed[2]), ("Người đề nghị", nguoi, signed[3])])
    return d


def tamung(ctx, key="dntu", name="Giấy đề nghị tạm ứng", don_vi="", ngay=None, nguoi="", bo_phan="", ly_do="", amount=0, thoi_han="",
           cu="", signed=(True, True, True, True)):
    d = ctx.doc(key, name)
    d.text(MARGIN, d.y, SCHOOL_UP, "serifb", 20)
    d.text(W - MARGIN, d.y, "Mẫu số 03 - TU", "serifb", 20, anchor="ra")
    d.y += 30
    d.kv("Đơn vị:", don_vi, hand=True)
    d.center("GIẤY ĐỀ NGHỊ TẠM ỨNG", "serifb", 30, 6)
    d.center("Ngày %02d tháng %02d năm %d" % (ngay.day, ngay.month, ngay.year), "serifi", 21, 14)
    d.rec("Ngày lập", D(ngay))
    d.line("Kính gửi: Ban Giám hiệu; Phòng Tài chính - Kế toán", "serif", 22)
    d.kv("Họ và tên người đề nghị tạm ứng:", nguoi, hand=True)
    d.kv("Bộ phận:", bo_phan, hand=True)
    d.kv("Lý do tạm ứng:", ly_do, hand=True)
    d.kv("Số tiền tạm ứng (bằng số):", vn(amount) + " đ", hand=True)
    d.kv("Số tiền tạm ứng (bằng chữ):", words(amount), hand=True)
    d.kv("Thời hạn thanh toán:", thoi_han, hand=True)
    d.kv("Các khoản tạm ứng kỳ trước chưa thanh toán:", cu, hand=True)
    d.gap(10)
    d.sig_block([("Hiệu trưởng", HT, signed[0]), ("Kế toán trưởng", KTT, signed[1]), ("Trưởng đơn vị", "", signed[2]), ("Người đề nghị", nguoi, signed[3])])
    return d


def vanban(ctx, key, name, title, org_top="BỘ GIÁO DỤC VÀ ĐÀO TẠO", org="TRƯỜNG ĐẠI HỌC THĂNG LONG", so="", ngay=None, subtitle=None,
           paras=(), kv=(), table=None, sigs=(), stamp=None, ill=(), table_label=None, hand_kv=False, extra=None, table2=None):
    """Generic administrative document: national header, title, key/value lines, paragraphs, optional tables, signatures, stamp."""
    d = ctx.doc(key, name)
    d.header2(org_top, org)
    d.text(MARGIN + 190, d.y - 8, "Số: %s" % so, "serif", 19, anchor="ma")
    d.text(W - MARGIN - 230, d.y - 8, date_line(ngay), "serifi", 19, anchor="ma")
    d.rec("Số văn bản", so)
    d.rec("Ngày văn bản", D(ngay))
    d.y += 30
    d.center(title, "serifb", 28, 6)
    if subtitle:
        d.center(subtitle, "serifb", 21, 10)
    d.gap(6)
    for lbl, val in kv:
        d.kv(lbl, val, hand=hand_kv, ill=(lbl in ill))
    for p in paras:
        d.para(p, size=21)
    if table:
        hd, rows, cw = table[:3]
        kw = table[3] if len(table) > 3 else {}
        d.gap(6)
        d.table(hd, rows, cw, label=table_label or "bảng", **kw)
    if table2:
        hd, rows, cw = table2[:3]
        kw = table2[3] if len(table2) > 3 else {}
        d.table(hd, rows, cw, label="bảng 2", **kw)
    if extra:
        extra(d)
    if sigs:
        d.sig_block(list(sigs))
    if stamp:
        cx, cy, l1, l2 = stamp
        d.stamp(cx, d.y - 110, l1, l2, rec_label=l1 + (" " + l2 if l2 else ""))
    return d


def giay_di_duong(ctx, key="gdd", name="Giấy đi đường", nguoi="", chuc_vu="", don_vi="", qd_so="", qd_ngay=None, di=None, ve=None, noi_den="",
                  phuong_tien="", so_ngay=0, phu_cap=0, nguoi_ky=True, tdv_ky=True, kt_ky=True, tdv_ngay_ill=False, tdv_ngay=None,
                  xacnhan=True, xacnhan_ngay=None, rate=300000, names=None, ill=()):
    d = ctx.doc(key, name)
    names = names or {}
    d.text(MARGIN, d.y, SCHOOL_UP, "serifb", 20)
    d.text(W - MARGIN, d.y, "Mẫu số C16 - HD", "serifb", 20, anchor="ra")
    d.y += 34
    d.center("GIẤY ĐI ĐƯỜNG", "serifb", 32, 4)
    d.center("Số: %s" % qd_so.replace("QĐ", "GĐĐ"), "serifi", 20, 12)
    d.rec("Số giấy đi đường", qd_so.replace("QĐ", "GĐĐ"))
    d.kv("Cấp cho ông/bà:", nguoi, hand=True)
    d.kv("Chức vụ:", chuc_vu, hand=True)
    d.kv("Đơn vị công tác:", don_vi, hand=True)
    d.kv("Được cử đi công tác tại:", noi_den, hand=True)
    d.kv("Theo quyết định số:", "%s ngày %s" % (qd_so, D(qd_ngay)), hand=True)
    d.kv("Ngày đi:", D(di), hand=True)
    d.kv("Ngày về:", D(ve), hand=True)
    d.kv("Phương tiện đi lại:", phuong_tien, hand=True)
    d.kv("Số ngày công tác:", "%d ngày" % so_ngay, hand=True)
    d.kv("Phụ cấp lưu trú (%s đ/ngày):" % vn(rate), vn(phu_cap) + " đ", hand=True, ill=("phu_cap" in ill))
    d.gap(8)
    d.line("Xác nhận của cơ quan, đơn vị nơi đến công tác:", "serifb", 21)
    d.room(60)
    if xacnhan:
        d.text(MARGIN + 20, d.y, "Đã đến làm việc từ ngày %s đến ngày %s." % (D(di), D(ve)), "serif", 21)
        d.rec("Xác nhận nơi đến", "Đã đến làm việc từ ngày %s đến ngày %s" % (D(di), D(ve)))
        d.stamp(W - MARGIN - 130, d.y + 20, "ĐƠN VỊ MỜI", "NƠI ĐẾN", rec_label="xác nhận nơi đến")
        d.rec("Ngày xác nhận", D(xacnhan_ngay or ve))
    else:
        d.text(MARGIN + 20, d.y, "(chưa có xác nhận)", "serifi", 21)
        d.rec("Xác nhận nơi đến", "(để trống)")
    d.y += 80
    d.sig_block([("Người đi công tác", nguoi, nguoi_ky), ("Trưởng đơn vị", names.get("TDV", ""), tdv_ky), ("Kế toán", names.get("KT", ""), kt_ky)], gap_after=6)
    d.kv("Ngày ký của trưởng đơn vị:", D(tdv_ngay) if tdv_ngay else "", hand=True, ill=tdv_ngay_ill, rec=True)
    return d


def phieu_y_kien(ctx, key="phieu", name="Phiếu ý kiến phòng Tài chính - Kế toán", ngay=None, don_vi="", noi_dung="", ma_ns="", trong_ns=True,
                 du_tru=0, con_lai=0, y_kien="Đồng ý", signed=True, tp=TPTC, ill_conlai=False):
    d = ctx.doc(key, name)
    d.header2("TRƯỜNG ĐẠI HỌC THĂNG LONG", "PHÒNG TÀI CHÍNH - KẾ TOÁN")
    d.center("PHIẾU Ý KIẾN CỦA PHÒNG TÀI CHÍNH - KẾ TOÁN", "serifb", 27, 8)
    d.center("Ngày %02d tháng %02d năm %d" % (ngay.day, ngay.month, ngay.year), "serifi", 21, 12)
    d.rec("Ngày", D(ngay))
    d.kv("Đơn vị đề nghị:", don_vi)
    d.kv("Nội dung xin ý kiến:", noi_dung)
    d.kv("Mã ngân sách:", ma_ns, hand=True)
    d.kv("Dự trù kinh phí đề nghị:", vn(du_tru) + " đ")
    d.room(34)
    d.text(MARGIN, d.y, "Khoản chi nằm trong ngân sách:   %s Có     %s Không" % ("☒" if trong_ns else "☐", "☐" if trong_ns else "☒"), "sans", 21)
    d.rec("Khoản chi nằm trong ngân sách", "Có" if trong_ns else "Không")
    d.y += 40
    d.kv("Ngân sách còn lại của mã trên:", vn(con_lai) + " đ", hand=True, ill=ill_conlai)
    d.kv("Ý kiến của phòng Tài chính - Kế toán:", y_kien, hand=True)
    d.gap(14)
    d.sig_block([("Trưởng phòng Tài chính - Kế toán", tp, signed)])
    return d


def hoadon(ctx, key, name, seller, seller_mst, seller_addr, seller_tk, so, kyhieu, ngay, items, vat=10, buyer_person="", buyer_name=SCHOOL,
           buyer_mst=SCHOOL_MST, buyer_addr=SCHOOL_ADDR, httt="CK", layout=1, ill=(), note=None, signed=True, rate_label=None, cat=None):
    """Electronic VAT invoice. items: list of (desc, unit, qty, price_before_vat). Returns (doc, totals dict)."""
    d = ctx.doc(key, name)
    ink = d.ink
    d.y = 50
    if layout == 1:
        d.text(W // 2, d.y, "HÓA ĐƠN GIÁ TRỊ GIA TĂNG", "sansb", 30, anchor="ma")
        d.text(W // 2, d.y + 40, "(Bản thể hiện của hóa đơn điện tử)", "sans", 16, anchor="ma")
        d.y += 70
        d.text(W // 2, d.y, "Ngày %02d tháng %02d năm %d" % (ngay.day, ngay.month, ngay.year), "sans", 19, anchor="ma")
        d.text(W - MARGIN, d.y - 70, "Ký hiệu: %s" % kyhieu, "sans", 18, anchor="ra")
        d.text(W - MARGIN, d.y - 44, "Số: %s" % so, "sansb", 20, anchor="ra")
    else:
        d.text(MARGIN, d.y, "HÓA ĐƠN ĐIỆN TỬ - VAT INVOICE", "sansb", 26)
        d.text(W - MARGIN, d.y, "Số (No.): %s" % so, "sansb", 20, anchor="ra")
        d.y += 36
        d.text(MARGIN, d.y, "Ký hiệu (Serial): %s" % kyhieu, "sans", 18)
        d.text(W - MARGIN, d.y, "Ngày (Date): %s" % D(ngay), "sans", 18, anchor="ra")
        d.y += 40
    d.rec("Số hóa đơn", so)
    d.rec("Ký hiệu", kyhieu)
    d.rec("Ngày lập hóa đơn", D(ngay))
    d.y += 34
    d.rule()
    sz = 19
    d.kv("Đơn vị bán hàng:", seller, kind="sans", size=sz, dots=False)
    d.kv("Mã số thuế:", seller_mst, kind="sans", size=sz, dots=False)
    d.kv("Địa chỉ:", seller_addr, kind="sans", size=sz, dots=False)
    d.kv("Số tài khoản:", seller_tk, kind="sans", size=sz, dots=False)
    d.rule()
    d.kv("Họ tên người mua hàng:", buyer_person, kind="sans", size=sz, dots=False)
    d.kv("Tên đơn vị:", buyer_name, kind="sans", size=sz, dots=False, ill=("buyer_name" in ill))
    d.kv("Mã số thuế:", buyer_mst, kind="sans", size=sz, dots=False, ill=("buyer_mst" in ill))
    d.kv("Địa chỉ:", buyer_addr, kind="sans", size=sz, dots=False, ill=("buyer_addr" in ill))
    d.kv("Hình thức thanh toán:", {"CK": "CK", "TM": "TM", "TM/CK": "TM/CK"}[httt], kind="sans", size=sz, dots=False)
    d.rule()
    rows = []
    sub = 0
    for i, (desc, unit, qty, price) in enumerate(items):
        amt = qty * price
        sub += amt
        rows.append([str(i + 1), desc, unit, str(qty), vn(price), vn(amt)])
    taxv = int(round(sub * vat / 100.0))
    total = sub + taxv
    d.table(["STT", "Tên hàng hóa, dịch vụ", "ĐVT", "SL", "Đơn giá", "Thành tiền"], rows, [0.6, 4.2, 1, 0.8, 1.6, 1.8], size=18, label="hàng hóa",
            aligns=["c", "l", "c", "c", "r", "r"])
    d.kv("Cộng tiền hàng:", vn(sub), kind="sans", size=sz, dots=False)
    d.kv("Thuế suất GTGT: %d%%  - Tiền thuế GTGT:" % vat, vn(taxv), kind="sans", size=sz, dots=False)
    d.kv("Tổng cộng tiền thanh toán:", vn(total), kind="sansb", size=sz + 1, dots=False, ill=("total" in ill))
    d.kv("Số tiền viết bằng chữ:", words(total), kind="sans", size=sz - 1, dots=False)
    if note:
        d.kv("Ghi chú:", note, kind="sans", size=sz - 1, dots=False)
    d.gap(14)
    d.room(130)
    d.text(MARGIN, d.y, "Người mua hàng", "sansb", 18)
    d.text(W - MARGIN - 330, d.y, "Người bán hàng", "sansb", 18)
    d.y += 30
    d.box(W - MARGIN - 380, d.y, W - MARGIN, d.y + 96, 2)
    if signed:
        d.text(W - MARGIN - 370, d.y + 8, "Signature Valid", "sansb", 16, fill=(30, 110, 40))
        d.text(W - MARGIN - 370, d.y + 32, "Ký bởi: %s" % seller.upper()[:34], "sans", 14)
        d.text(W - MARGIN - 370, d.y + 54, "Ký ngày: %s" % D(ngay), "sans", 14)
    d.rec("Chữ ký số người bán", "có" if signed else "không có")
    d.y += 120
    return d, dict(sub=sub, tax=taxv, total=total)


def the_bay(ctx, key, name, hanh_khach, legs, kind="air", hang="VNA", ma="", rec_ill=()):
    """legs: list of (flight, from, to, date, time). Boarding pass / e-ticket confirmation (kind air) or bus/train ticket."""
    d = ctx.doc(key, name)
    d.y = 60
    if kind == "air":
        d.center("XÁC NHẬN VÉ ĐIỆN TỬ / THẺ LÊN MÁY BAY", "sansb", 24, 8)
        d.kv("Mã đặt chỗ:", ma, kind="mono", size=22, dots=False)
        d.kv("Hành khách:", noaccent(hanh_khach).upper(), kind="sansb", size=20, dots=False)
        for i, (fl, a, b, dd, tm) in enumerate(legs):
            d.gap(10)
            d.line("CHẶNG %d" % (i + 1), "sansb", 19)
            d.box(MARGIN, d.y, W - MARGIN, d.y + 150, 2)
            y = d.y + 12
            d.text(MARGIN + 18, y, "Chuyến bay: %s" % fl, "sansb", 20)
            d.text(MARGIN + 18, y + 38, "Từ: %s" % a, "sans", 20)
            d.text(MARGIN + 18, y + 72, "Đến: %s" % b, "sans", 20)
            d.text(W // 2 + 40, y + 38, "Ngày bay: %s" % D(dd), "sansb", 20)
            d.text(W // 2 + 40, y + 72, "Giờ khởi hành: %s" % tm, "sans", 20)
            d.text(W - MARGIN - 20, y + 104, "ECONOMY   |   GHẾ %s" % ("%02d%s" % (10 + i * 7, "AB"[i % 2])), "sans", 16, anchor="ra")
            d.rec("Chặng %d, chuyến bay" % (i + 1), fl)
            d.rec("Chặng %d, từ - đến" % (i + 1), "%s - %s" % (a, b))
            d.rec("Chặng %d, ngày bay" % (i + 1), D(dd))
            d.rec("Chặng %d, giờ khởi hành" % (i + 1), tm)
            d.y += 170
        d.rec("Hành khách", noaccent(hanh_khach).upper())
        d.rec("Mã đặt chỗ", ma)
    else:
        d.center("VÉ %s" % ("TÀU HỎA" if kind == "train" else "XE KHÁCH"), "sansb", 26, 10)
        d.kv("Hành khách:", hanh_khach, kind="sans", size=20, dots=False)
        for i, (fl, a, b, dd, tm) in enumerate(legs):
            d.gap(10)
            d.box(MARGIN, d.y, W - MARGIN, d.y + 120, 2)
            y = d.y + 12
            d.text(MARGIN + 18, y, "%s %s" % ("Tàu" if kind == "train" else "Nhà xe", fl), "sansb", 20)
            d.text(MARGIN + 18, y + 38, "Tuyến: %s - %s" % (a, b), "sans", 20)
            d.text(MARGIN + 18, y + 74, "Ngày đi: %s   Giờ: %s" % (D(dd), tm), "sans", 20)
            d.rec("Vé %d, đơn vị vận chuyển" % (i + 1), fl)
            d.rec("Vé %d, tuyến" % (i + 1), "%s - %s" % (a, b))
            d.rec("Vé %d, ngày đi" % (i + 1), D(dd))
            d.rec("Vé %d, giờ" % (i + 1), tm)
            d.y += 140
        d.rec("Hành khách", hanh_khach)
    return d


def bang(ctx, key, name, title, org_left="TRƯỜNG ĐẠI HỌC THĂNG LONG", mau="", kv=(), table=None, total_line=None, words_line=None, sigs=(), ill_kv=(), hand_kv=False,
         note=None, stamp=None, landscape_note=None):
    """List-type vouchers (payment lists, details tables) with a form code at the top right."""
    d = ctx.doc(key, name)
    d.text(MARGIN, d.y, org_left, "serifb", 20)
    if mau:
        d.text(W - MARGIN, d.y, mau, "serifb", 20, anchor="ra")
    d.y += 36
    d.center(title, "serifb", 27, 8)
    for lbl, val in kv:
        d.kv(lbl, val, hand=hand_kv, ill=(lbl in ill_kv))
    d.gap(4)
    if table:
        hd, rows, cw = table[:3]
        kw = table[3] if len(table) > 3 else {}
        d.table(hd, rows, cw, label=name, **kw)
    if total_line:
        d.kv(total_line[0], total_line[1], hand=hand_kv, ill=(total_line[0] in ill_kv))
    if words_line:
        d.kv("Số tiền bằng chữ:", words_line)
    if note:
        d.para(note, "serifi", 19)
    if sigs:
        d.sig_block(list(sigs))
    if stamp:
        cx, cy, l1, l2 = stamp
        d.stamp(cx, d.y - 110, l1, l2, rec_label=l1 + (" " + l2 if l2 else ""))
    return d
