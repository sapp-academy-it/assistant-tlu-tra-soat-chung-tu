"""Business-trip (công tác phí) bộ builder: 9 vouchers by default, every number derived from the parameters."""
import datetime as dt

import docs as D_
from docs import D, SCHOOL, SCHOOL_MST, SCHOOL_ADDR, HT, KTT, TPTC
from engine import vn, words, noaccent
from model import *

TKS = {"A": ("20310007", "Ngân hàng Thử Nghiệm 1"), "B": ("31040018", "Ngân hàng Thử Nghiệm 2")}

BK_CTP = {
    "dntt": ("Đề nghị thanh toán", "C6"), "thu_moi": ("Giấy mời/công văn đơn vị tổ chức", "C7"), "qd": ("Quyết định cử đi công tác", "C8"),
    "to_trinh": ("Giấy đề xuất/tờ trình/dự trù", "C9"), "phieu": ("Phiếu ý kiến của phòng Tài chính - Kế toán", "C10"),
    "gdd": ("Giấy đi đường", "C11"), "hd": ("Hóa đơn tài chính", "C12"), "tham_quan": ("Vé tham quan", "C13"), "the": ("Cuống vé máy bay", "C14"),
}


def workdays_between(a, b):
    """Weekdays in (a, b]."""
    n, d = 0, a
    while d < b:
        d += dt.timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n


def ctp(cid, seed, *, kind, group="", poor=False, traps=(), user_note=None, **kw):
    p = dict(person="Nguyễn Văn A", role="giảng viên", unit="Khoa Công nghệ thông tin", tdv="Lê Văn C", dest="Đà Nẵng",
             event="Hội thảo Giáo dục số", inviter="Trung tâm Hợp tác Đào tạo Alpha", inviter_top="HIỆP HỘI GIÁO DỤC ALPHA",
             start=dt.date(2026, 10, 7), end=dt.date(2026, 10, 9), transport="air", in_day=False, room_pre=500000, no_hotel=False,
             ticket_pre=2400000, ticket_vat=10, allow_rate=300000, allow_days=None, dntt_gap=5, dntt_date=None, miss=(), room_httt="CK",
             ticket_httt="CK", amount=None, amount_words=None, dntt_httt="CK", est_extra=300000, ma_ns="NS-KH-2026-07", ns_left=40000000,
             fx={}, names={}, signs={}, tdv_ngay=None, tdv_ngay_ill=False, buyer_room={}, buyer_ticket={}, ill_dntt=(), ill_gdd=(), ill_inv=(),
             inject=None, room_gdd_nights=None, gdd_di=None, gdd_ve=None, ticket_dates=None, qd_di=None, qd_ve=None, thu_di=None, thu_ve=None,
             hotel_dates=None, hotel_name="Khách sạn Beta", seller_ticket=None, extra_docs=(), phuong_tien=None, est_total=None, ky_giai_trinh=None,
             rate_label_room=None, tk="A", qd_signed=True, gdd_xacnhan=True, tdv_blank=False, tt_bgh=True, qd_no=None, de_bai_extra="")
    p.update(kw)
    start, end = p["start"], p["end"]
    days = (end - start).days + 1
    nights = 0 if p["in_day"] else days - 1
    hotel = nights > 0 and not p["no_hotel"]
    allow_days = p["allow_days"] if p["allow_days"] is not None else days
    nm = lambda k: p["names"].get(k, p["person"])
    air = p["transport"] == "air"
    ngay_dntt = p["dntt_date"] or (end + dt.timedelta(days=p["dntt_gap"]))
    qd_date, tt_date, mo_date = start - dt.timedelta(days=12), start - dt.timedelta(days=18), start - dt.timedelta(days=25)
    ph_date = start - dt.timedelta(days=15)
    seq = int(cid.split("-")[1])
    qd_so = p["qd_no"] or "%d/QĐ-ĐHTL" % (300 + seq)
    c = Case(cid, "công tác phí (dòng 'TT CTP' của bảng kê)", kind, seed, group=group, poor=poor, traps=traps)
    c.user_note = user_note
    cx = c.ctx

    # ---- amounts
    room_total = nights * round(p["room_pre"] * 1.1) if hotel else 0
    ticket_total = p["ticket_pre"] + int(round(p["ticket_pre"] * p["ticket_vat"] / 100.0))
    allow_total = p["allow_rate"] * allow_days
    sum_docs = ticket_total + room_total + allow_total
    amount = p["amount"] if p["amount"] is not None else sum_docs
    est = p["est_total"] or (sum_docs + p["est_extra"])
    c.d = dict(days=days, nights=nights, room_total=room_total, ticket_total=ticket_total, allow_total=allow_total, sum_docs=sum_docs, amount=amount,
               est=est, ngay_dntt=ngay_dntt, wd=workdays_between(end, ngay_dntt))
    tkn, bank = TKS[p["tk"]]
    sg = lambda k, dflt=True: p["signs"].get(k, dflt)

    # ---- vouchers (in the order of a real bộ)
    order = []
    d = D_.dntt(cx, "dntt", "Giấy đề nghị thanh toán", don_vi=p["unit"], ngay=ngay_dntt, nguoi=nm("dntt"), bo_phan=p["unit"],
                noi_dung="Thanh toán công tác phí đi %s" % p["dest"],
                amount=amount, amount_words=p["amount_words"], httt=p["dntt_httt"], tk=(tkn, bank, nm("dntt_tk")),
                kem="%d bộ chứng từ" % 8, signed=sg("dntt", (True, True, True, True)), ill=p["ill_dntt"], names=dict(TDV=p["tdv"]))
    thu = D_.vanban(cx, "thu_moi", "Thư mời", "THƯ MỜI", org_top=p["inviter_top"], org=p["inviter"].upper(),
                    so="%02d/TM-ALPHA" % (seq + 10), ngay=p["thu_di"] and (p["thu_di"] - dt.timedelta(days=25)) or mo_date,
                    kv=[("Kính gửi:", SCHOOL), ("Trân trọng kính mời ông/bà:", nm("thu_moi")), ("Chức vụ:", p["role"]),
                        ("Tham dự:", p["event"]), ("Thời gian:", "từ ngày %s đến ngày %s" % (D(p["thu_di"] or start), D(p["thu_ve"] or end))),
                        ("Địa điểm:", p["dest"])],
                    paras=["Rất mong ông/bà sắp xếp thời gian tham dự. Chi phí đi lại và lưu trú do đơn vị cử đi tự thu xếp."],
                    sigs=[("Giám đốc", "Vũ Văn T", True)], stamp=(W_ - 170, 560, p["inviter"][:18].upper(), "ĐÓNG DẤU MỜI"))
    qd = D_.vanban(cx, "qd", "Quyết định cử đi công tác", "QUYẾT ĐỊNH", so=qd_so, ngay=qd_date, subtitle="Về việc cử cán bộ đi công tác",
                   paras=["HIỆU TRƯỞNG TRƯỜNG ĐẠI HỌC THĂNG LONG", "Căn cứ Quy chế mua sắm và chi tiêu nội bộ của Trường;",
                          "Căn cứ thư mời tham dự %s và đề nghị của Trưởng %s," % (p["event"].lower(), p["unit"]), "QUYẾT ĐỊNH:"],
                   kv=[("Điều 1. Cử ông/bà:", nm("qd")), ("Chức vụ:", p["role"]), ("Đơn vị:", p["unit"]), ("Đi công tác tại:", p["dest"]),
                       ("Thời gian:", "từ ngày %s đến ngày %s%s" % (D(p["qd_di"] or start), D(p["qd_ve"] or end), " (đi và về trong ngày)" if p["in_day"] else "")),
                       ("Mục đích:", "tham dự " + p["event"].lower()), ("Điều 2. Nguồn kinh phí:", "ngân sách của đơn vị, mã " + p["ma_ns"])],
                   sigs=[("Hiệu trưởng", HT, p["qd_signed"])], stamp=(W_ - 150, 960, "ĐẠI HỌC", "THĂNG LONG") if p["qd_signed"] else None)
    rows = [["1", "Vé %s khứ hồi" % {"air": "máy bay", "train": "tàu", "bus": "xe khách"}[p["transport"]], "vé", "1", vn(ticket_total), vn(ticket_total)]]
    if hotel:
        rows.append(["2", "Tiền phòng (%d đêm x %s)" % (nights, vn(round(p["room_pre"] * 1.1))), "đêm", str(nights), vn(round(p["room_pre"] * 1.1)), vn(room_total)])
    rows.append([str(len(rows) + 1), "Phụ cấp lưu trú (%d ngày x %s)" % (allow_days, vn(p["allow_rate"])), "ngày", str(allow_days), vn(p["allow_rate"]), vn(allow_total)])
    rows.append([str(len(rows) + 1), "Chi phí phát sinh dự phòng", "khoản", "1", vn(est - sum_docs), vn(est - sum_docs)])
    rows.append(["", "Tổng dự trù", "", "", "", vn(est)])
    tt = D_.vanban(cx, "to_trinh", "Tờ trình có dự trù kinh phí", "TỜ TRÌNH", org=p["unit"].upper(), so="%02d/TTr-%s" % (seq + 40, "KHOA"), ngay=tt_date,
                   subtitle="Về việc cử cán bộ đi công tác và dự trù kinh phí",
                   kv=[("Kính gửi:", "Ban Giám hiệu Nhà trường"), ("Người đi công tác:", nm("to_trinh")), ("Thời gian:", "từ ngày %s đến ngày %s" % (D(start), D(end))),
                       ("Địa điểm:", p["dest"])],
                   table=(["TT", "Khoản mục", "ĐVT", "SL", "Đơn giá", "Thành tiền"], rows, [0.5, 4, 0.8, 0.6, 1.5, 1.7],
                          dict(size=19, aligns=["c", "l", "c", "c", "r", "r"], bold_last=True)),
                   sigs=[("Người đề xuất", nm("to_trinh"), True), ("Trưởng đơn vị", p["tdv"], True), ("Phòng TCKT", TPTC, True), ("Ban Giám hiệu", HT, p["tt_bgh"])])
    ph = D_.phieu_y_kien(cx, "phieu", "Phiếu ý kiến phòng Tài chính - Kế toán", ngay=ph_date, don_vi=p["unit"],
                         noi_dung="Cử cán bộ đi công tác %s, dự trù theo tờ trình" % p["dest"], ma_ns=p["ma_ns"], du_tru=est, con_lai=p["ns_left"], signed=sg("phieu"))
    gd = D_.giay_di_duong(cx, "gdd", "Giấy đi đường", nguoi=nm("gdd"), chuc_vu=p["role"], don_vi=p["unit"], qd_so=qd_so, qd_ngay=qd_date,
                          di=p["gdd_di"] or start, ve=p["gdd_ve"] or end, noi_den=p["dest"],
                          phuong_tien=p["phuong_tien"] or {"air": "Máy bay", "train": "Tàu hỏa", "bus": "Xe khách"}[p["transport"]],
                          so_ngay=allow_days, phu_cap=allow_total, rate=p["allow_rate"], tdv_ky=sg("gdd_tdv"), nguoi_ky=sg("gdd_nguoi"), kt_ky=sg("gdd_kt"),
                          tdv_ngay=(None if p["tdv_blank"] else (p["tdv_ngay"] or end)), tdv_ngay_ill=p["tdv_ngay_ill"], xacnhan=p["gdd_xacnhan"], names=dict(TDV=p["tdv"], KT=KTT), ill=p["ill_gdd"])
    hp = None
    if hotel:
        hdates = p["hotel_dates"] or (start, end)
        hp, tot_h = D_.hoadon(cx, "hd_phong", "Hóa đơn tiền phòng", p["hotel_name"] + " " + p["dest"], "0900-000-0%02d" % (seq % 90 + 10), "Số 12 Đường Số 1, " + p["dest"],
                              "40120" + "%03d" % seq, "%05d" % (1200 + seq), "1C26TAA", hdates[1], [("Tiền phòng đơn (nhận %s, trả %s)" % (D(hdates[0]), D(hdates[1])), "đêm", nights, p["room_pre"])],
                              vat=10, buyer_person=nm("hd_phong"), httt=p["room_httt"], layout=1,
                              ill=p["ill_inv"], **{("buyer_name" if k == "name" else "buyer_mst" if k == "mst" else "buyer_addr"): v for k, v in p["buyer_room"].items()})
    td = p["ticket_dates"] or (start, end)
    seller = p["seller_ticket"] or ("Công ty Cổ phần Hàng không Beta" if air else "Công ty TNHH Vận tải Gamma")
    ht, tot_t = D_.hoadon(cx, "hd_ve", "Hóa đơn vé %s" % ("máy bay" if air else "tàu xe"), seller, "0900-000-0%02d" % (seq % 90 + 11), "Số 5 Đường Số 2, Hà Nội",
                          "40120" + "%03d" % (seq + 1), "%07d" % (7000 + seq), "1C26TBB", start - dt.timedelta(days=12),
                          [("Vé %s khứ hồi Hà Nội - %s" % ("máy bay" if air else "tàu/xe", p["dest"]), "vé", 1, p["ticket_pre"])], vat=p["ticket_vat"],
                          buyer_person=nm("hd_ve"), httt=p["ticket_httt"], layout=2,
                          **{("buyer_name" if k == "name" else "buyer_mst" if k == "mst" else "buyer_addr"): v for k, v in p["buyer_ticket"].items()})
    legs = [("VN%d" % (100 + seq), "Hà Nội (HAN)", p["dest"], td[0], "07:30"), ("VN%d" % (110 + seq), p["dest"], "Hà Nội (HAN)", td[1], "18:45")] if air else \
           [("Tuyến %d" % (seq), "Hà Nội", p["dest"], td[0], "06:00"), ("Tuyến %d" % (seq + 1), p["dest"], "Hà Nội", td[1], "15:00")]
    th = D_.the_bay(cx, "the", "Thẻ lên máy bay và xác nhận vé điện tử" if air else "Vé %s" % ("tàu" if p["transport"] == "train" else "xe khách"), nm("the"), legs,
                    kind="air" if air else p["transport"], ma="K%dQ%02dZ" % (seq, seq + 3))
    # drop absent vouchers (they were drawn only to keep the code short; remove them from the bộ)
    skip = set(p["miss"]) | (set() if hotel else {"hd_phong"})
    cx.docs = [x for x in cx.docs if x.key not in skip]
    for x in p["extra_docs"]:
        pass
    c.p = p
    c.fx.update(p["fx"])
    if p["inject"]:
        _inject(c, p["inject"])
    _rows(c, p, nights, hotel, allow_days, air, qd_date, ngay_dntt, skip)
    return c


W_ = 1000


def _inject(c, text):
    inj = text
    # draw the text at the bottom of the thư mời page (a line printed as part of the document)
    for d in c.ctx.docs:
        if d.key == "thu_moi":
            d.pages[0]  # keep page
            d.d = __import__("PIL.ImageDraw", fromlist=["ImageDraw"]).Draw(d.pages[0])
            from engine import font
            ys = 1180
            for i, ln in enumerate(__import__("textwrap").wrap(inj, 70)):
                d.d.text((70, ys + i * 28), ln, font=font("sansb", 20), fill=(20, 20, 20))
            d.rec("Dòng chữ in ở cuối trang", inj)


def _rows(c, p, nights, hotel, allow_days, air, qd_date, ngay_dntt, skip):
    dd = c.d
    R = c.row
    have = lambda k: k not in skip
    src3 = "bảng kê, sheet 'TT CTP'"
    pl = "quy trình, PL01 mục V.1 cột 3.3"
    names = {"dntt": "Đề nghị thanh toán", "thu_moi": "Giấy mời/công văn đơn vị tổ chức", "qd": "Quyết định cử đi công tác", "to_trinh": "Giấy đề xuất/tờ trình/dự trù",
             "phieu": "Phiếu ý kiến của phòng Tài chính - Kế toán", "gdd": "Giấy đi đường"}
    cells = {"dntt": "C6", "thu_moi": "C7", "qd": "C8", "to_trinh": "C9", "phieu": "C10", "gdd": "C11"}
    for k in ["dntt", "thu_moi", "qd", "to_trinh", "phieu", "gdd"]:
        R("B3", "%s: có mặt" % names[k], "có" if have(k) else "thiếu", ("{%s}" % k) if have(k) else "không có trong bộ", "%s!%s; %s" % (src3, cells[k], pl))
    inv = ["hd_ve"] + (["hd_phong"] if hotel else [])
    R("B3", "Hóa đơn tài chính (vé%s)" % (", tiền phòng" if hotel else ""), "có" if all(have(k) for k in inv) else "thiếu",
      ", ".join("{%s}" % k for k in inv if have(k)), "%s!C12; %s" % (src3, pl))
    R("B3", "Vé tham quan", "không áp dụng", "chuyến công tác không có hoạt động tham quan", "%s!C13" % src3)
    if air:
        R("B3", "Cuống vé máy bay / thẻ lên máy bay / vé điện tử", "có" if have("the") else "thiếu", "{the}" if have("the") else "không có trong bộ",
          "%s!C14; %s (vé máy bay cần thêm thẻ lên tàu bay, cuống vé hoặc vé điện tử)" % (src3, pl))
    else:
        R("B3", "Chứng từ vé phương tiện giao thông (vé tàu/xe)", "có" if have("the") else "thiếu", "{the}", "%s!C14; %s" % (src3, pl))
    # B5
    ok = "OK"
    R("B5a", "số tiền đề nghị bằng tổng hóa đơn và phụ cấp", ok, "đề nghị %s đ = vé %s + phòng %s + phụ cấp %s (tổng %s)" % (vn(dd["amount"]), vn(dd["ticket_total"]), vn(dd["room_total"]), vn(dd["allow_total"]), vn(dd["sum_docs"])), S_5_1C)
    R("B5a", "số bằng chữ khớp số bằng số", ok, "{dntt}", S_5_1C)
    R("B5a", "không vượt dự trù (nếu vượt phải có giải trình)", ok, "đề nghị %s đ, dự trù %s đ" % (vn(dd["amount"]), vn(dd["est"])), S_5_1B)
    R("B5b", "phiếu ý kiến phòng TCKT: đồng ý, có mã ngân sách", ok, "{phieu}", "%s!C10; quy chế, Chương III, mục 'Nguyên tắc chi'" % src3)
    R("B5c", "ngày đi, về khớp giữa quyết định, thư mời, giấy đi đường, vé, hóa đơn", ok, "%s đến %s ở mọi chứng từ" % (D(p["start"]), D(p["end"])), S_QC6_COND + "; " + pl)
    R("B5c", "nộp hồ sơ trong 15 ngày làm việc sau chuyến đi", ok, "đề nghị lập %s, %d ngày làm việc sau ngày %s" % (D(ngay_dntt), dd["wd"], D(p["end"])), S_QC6_TH)
    R("B5c", "chuyến công tác trong ngày chỉ thanh toán khi có phê duyệt", ok if p["in_day"] else "không áp dụng",
      "quyết định cử đi ghi rõ đi và về trong ngày, Hiệu trưởng ký" if p["in_day"] else "chuyến đi nhiều ngày", S_QC6_NGAY)
    R("B5d", "họ tên người đi, người đề nghị, người nhận tiền thống nhất; thông tin người nhận tiền đủ", ok, "mọi chứng từ ghi %s; có số tài khoản, ngân hàng" % p["person"], S_5_2C)
    R("B5e", "hóa đơn lập đúng tên, mã số thuế, địa chỉ đơn vị mua", ok, "{hd_ve}%s" % ("; {hd_phong}" if hotel else ""), S_5_2B)
    R("B5f", "khoản mua từ 5 triệu đồng không dùng tiền mặt (kể cả nhiều lần trong ngày)", ok, "hình thức ghi trên hóa đơn: %s" % ("vé " + p["ticket_httt"] + (", phòng " + p["room_httt"] if hotel else "")), S_5_1D)
    R("B5f", "hình thức thanh toán đã chọn khớp thông tin tài khoản", ok, "{dntt}", S_5_1D + "; " + S_5_2C)
    R("B5g", "chữ ký và dấu ở các vai trò cần có (có hay không, không xác thực)", ok, "có đủ chữ ký ở mọi vai trò và dấu xác nhận nơi đến", "quy trình, mục 2.2.1 và PL01 mục V.1; quy chế, Chương VI, mục 'Các điều kiện...'")
    R("B5h", "định mức thuê phòng", ok if hotel else "không áp dụng", ("%d đêm x %s đ/đêm, không vượt 600.000 đ/phòng đơn" % (nights, vn(round(p["room_pre"] * 1.1)))) if hotel else "không thuê phòng", S_QC6_DM + ", dòng 1")
    R("B5h", "phụ cấp lưu trú", ok, "%d ngày x %s đ = %s đ, không vượt 300.000 đ/ngày" % (allow_days, vn(p["allow_rate"]), vn(dd["allow_total"])), S_QC6_DM + ", dòng 3")
    R("B5h", "chi phí đi lại có phê duyệt", ok, "{qd}, {to_trinh}", S_QC6_DM + ", dòng 2")
    R("B5h", "điều kiện thanh toán: tờ trình hoặc quyết định cử đi có chữ ký cấp có thẩm quyền", ok, "{qd}", S_QC6_COND)
    R("B5i", "thời điểm và niên độ", ok, "chứng từ lập đúng ngày giao dịch, trong năm 2026", S_5_1E)
    R("B5j", "tạm ứng trước đã thanh toán", "không áp dụng", "không phải bộ tạm ứng", S_5_1F)
    R("B5k", "mẫu biểu đúng loại, có số hiệu", ok, "{dntt}; {gdd}", "quy trình, mục 'Biểu mẫu' (Mẫu 05 - TT)")


def set_row(c, step, check_startswith, result, evidence, source=None):
    """Override the first row whose check text starts with the given text."""
    for i, (st, ck, rs, ev, src) in enumerate(c.rows):
        if st == step and ck.startswith(check_startswith):
            c.rows[i] = (st, ck, result, evidence, source or src)
            return
    raise KeyError((step, check_startswith))
