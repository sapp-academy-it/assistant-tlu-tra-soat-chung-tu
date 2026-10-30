"""Render every case under cases/test-v1/<id>/ : input/trang-NN.jpg, de-bai.md, fields.md, key.md. Deterministic, offline."""
import os
import shutil
from PIL import Image
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.dirname(HERE)  # cases/test-v1

from engine import apply_effects
from model import key_md, fields_md

BASE_FX = {"base": "scan"}


def finalize(c):
    n = 0
    pages = []
    for d in c.ctx.docs:
        first = n + 1
        for i, im in enumerate(d.pages):
            fx = dict(BASE_FX)
            fx.update(c.fx.get("*", {}))
            fx.update(c.fx.get(d.key, {}))
            fx.update(d.effects[i])
            n += 1
            pages.append((n, d, i, apply_effects(im, fx, hash_seed(c.id, n)), fx))
        c.page_of[d.key] = str(first) if n == first else "%d-%d" % (first, n)
        c.refs[d.key] = "%s, tr.%s" % (d.name.lower(), c.page_of[d.key].replace("-", "-")) 
        c.refs[d.key] = "%s (tr.%s)" % (d.name.lower(), c.page_of[d.key])
    c.pages = pages
    c.npages = n
    return c


def hash_seed(cid, n):
    h = 0
    for ch in "%s/%d" % (cid, n):
        h = (h * 131 + ord(ch)) % (2 ** 31)
    return h


def write(c):
    root = os.path.join(OUT, c.id)
    if os.path.isdir(root):
        shutil.rmtree(root)
    os.makedirs(os.path.join(root, "input"))
    for n, d, i, im, fx in c.pages:
        im = im.resize((int(im.width * 0.88), int(im.height * 0.88)), Image.LANCZOS)
        im.save(os.path.join(root, "input", "trang-%02d.jpg" % n), "JPEG", quality=52, optimize=False, progressive=False)
    de = ["# Đề bài %s" % c.id, "", "Loại nghiệp vụ: %s." % c.type_name, "Ngày xét: %s." % c.ngay_xet, "Bộ chứng từ: %d trang ảnh quét trong `input/` (thứ tự trang như bộ nộp)." % c.npages]
    if c.de_bai:
        de += ["", c.de_bai]
    if c.user_note:
        de += ["", "Lời người dùng: " + c.user_note]
    open(os.path.join(root, "de-bai.md"), "w", encoding="utf-8").write("\n".join(de) + "\n")
    open(os.path.join(root, "fields.md"), "w", encoding="utf-8").write(fields_md(c))
    open(os.path.join(root, "key.md"), "w", encoding="utf-8").write(key_md(c))


def main(only=None):
    import cases_def
    cs = cases_def.all_cases()
    for c in cs:
        if only and c.id not in only:
            continue
        finalize(c)
        write(c)
        print(c.id, c.npages, "pages", c.verdict, len(c.findings), "findings")
    if not only:
        signoff(cs)
    return cs




def signoff(cs):
    import hashlib
    keys = sorted(cs, key=lambda c: c.id)
    allk = b"".join(open(os.path.join(OUT, c.id, "key.md"), "rb").read() for c in keys)
    h = hashlib.sha256(allk).hexdigest()
    nf = sum(len(c.findings) for c in cs)
    nb = sum(1 for c in cs for f in c.findings if f["level"] == "chặn")
    from collections import Counter
    vc = Counter(c.verdict for c in cs)
    L = ["# SIGNOFF test-v1", "",
         "Bản ghi ký key của test set `test-v1` (phiên bản `v1`, tag `v1`). Cách ký: chuyên gia nghiệp vụ duyệt (approve) PR chứa `cases/test-v1/` trên GitHub; "
         "approval của commit cuối là chữ ký. Sau khi ký, `key.md` của mọi case và tệp này không đổi (đổi sẽ làm sai sha256 đã ký).", "",
         "- Vai trò người ký: chuyên gia nghiệp vụ (chủ sở hữu, người đặt hàng).",
         "- Ngày ký: ngày approve PR trên GitHub (GitHub ghi ngày; tệp này không điền tay để không đổi sau khi ký).",
         "- sha256 của key: `%s` (lệnh: `cat cases/test-v1/*/key.md | sha256sum`, 42 tệp `key.md` theo thứ tự tên thư mục)." % h,
         "- Số case: %d (công tác phí 20: 6 hợp lệ, 14 có lỗi; 11 loại còn lại mỗi loại 2: 1 hợp lệ, 1 có lỗi; 17 hợp lệ, 8 quét kém, 10 bẫy)." % len(cs),
         "- Số phát hiện mong đợi trong key: %d (%d mức chặn, %d mức cảnh báo). Kết luận: %s." % (nf, nb, nf - nb, ", ".join("%s %d" % (k, v) for k, v in sorted(vc.items()))),
         "- Số trường trong các `fields.md`: %d." % sum(len(d.fields) for c in cs for d in c.ctx.docs), "",
         "## Chuyên gia kiểm gì, đối chiếu với tài liệu nào", "",
         "1. Mỗi `key.md`: kết luận mong đợi đúng theo quy tắc B7 của spec; mỗi phát hiện có nguồn. Đối chiếu nguồn với `inputs/`: **quy chế** (Chương VI: điều kiện, định mức thuê phòng 600.000 đ/phòng đơn và phụ cấp 300.000 đ/ngày cho cán bộ, giảng viên, thời hạn 15 ngày làm việc, công tác trong ngày; Chương III nguyên tắc chi; Chương VII học bổng), "
         "**quy trình** (mục 5.1b đến 5.1g, 5.2b, 5.2c, 2.2.1, 2.2.3, 'Biểu mẫu', Phụ lục 01 các mục I.1, I.3, V, VI và 'sự kiện'), **bảng kê** (từng sheet và ô được trích), **bảng mô tả 'AI kế toán thanh toán'** (sheet 'Gửi SAPP' ô C18, báo giá có dấu đỏ).",
         "2. Q1 (bảng kê không nói dòng nào bắt buộc): mỗi `key.md` ghi từng dòng bảng kê là 'có', 'thiếu' hoặc 'không áp dụng'. Chuyên gia xác nhận các dòng ghi 'thiếu' (chỉ dùng cho dòng có trong cả bảng kê và Phụ lục 01 cột 3.3) và các dòng 'không áp dụng' (tùy trường hợp).",
         "3. Q5 (chữ ký bắt buộc của từng biểu mẫu): các phát hiện 'thiếu chữ ký' của trưởng đơn vị, chủ tịch hội đồng, bên B, phòng HR, người lập biểu... dựa vào khối chữ ký của biểu mẫu hoặc vai trò hiển nhiên; chuyên gia xác nhận mức chặn của từng phát hiện đó.",
         "4. Chuyên gia xem `fields.md` của vài case để chắc bản chép khớp ảnh (đặc biệt các trường ghi KHÔNG ĐỌC ĐƯỢC ở ctp-015, hnh-002 là cố ý bị mực đè).", "",
         "## Điểm người dựng test set tự quyết, chuyên gia xác nhận", "",
         "- Bảng kê trong `inputs/` có 10 sheet, spec ghi 12 loại. Để giữ đúng 11 loại ngoài công tác phí (spec: 22 case), sheet 'TTdạy, chấm thi' được tách thành 3 loại theo Phụ lục 01 mục I (tiền dạy; chấm thi; xây dựng ngân hàng câu hỏi/ra đề): day-, cho-, nhc-.",
         "- Định mức thuê phòng so với số tiền trên hóa đơn đã gồm thuế; ca vi phạm (ctp-011) vượt cả khi chưa tính thuế nên không bị ảnh hưởng. Số ngày phụ cấp tính cả ngày đi và về (3 ngày 2 đêm = 3 ngày phụ cấp), theo ví dụ của spec.",
         "- Phát hiện về tạm ứng chưa thanh toán (hnh-002, quy trình 5.1f) xếp loại 'sửa được' (thanh toán tạm ứng trước rồi nộp lại), không phải 'vi phạm'.",
         "- Quá niên độ (sach-002, 5.1e) xếp loại 'vi phạm' theo B7; đề bài nêu năm tài chính là năm dương lịch (quy trình không định nghĩa).",
         "- Ở các case bẫy, `de-bai.md` có thêm dòng 'Lời người dùng' (yêu cầu của người dùng cố ý thử giới hạn) ngoài loại nghiệp vụ và ngày xét.",
         "- Mẫu giấy đi đường dùng số hiệu 'C16 - HD' hư cấu; Q2 (mẫu theo thông tư cũ) chưa đưa vào key, key không có phát hiện về căn cứ ban hành của mẫu.",
         "- Dữ liệu cá nhân (căn cước, mã số thuế, điện thoại, tài khoản) đều hư cấu, ghi dạng nhóm số có dấu cách hoặc 8 chữ số; mã số thuế nhà cung cấp hư cấu ghi dạng có gạch nối. Mã số thuế và địa chỉ của Trường là dữ liệu pháp nhân công khai (quy trình mục 5.2b).", "",
         "## Sinh lại ảnh", "",
         "`python3 -I cases/test-v1/_gen/build.py` dựng lại toàn bộ `cases/test-v1/<mã-case>/` (ảnh, `de-bai.md`, `fields.md`, `key.md`) và tệp này: xác định, không dùng mạng, chỉ ghi dưới `cases/test-v1/`; cần Pillow, numpy và phông Liberation, DejaVu của hệ thống.", "",
         "## sha256 từng key", "", "| Case | sha256 của key.md |", "|---|---|"]
    for c in keys:
        L.append("| %s | `%s` |" % (c.id, hashlib.sha256(open(os.path.join(OUT, c.id, "key.md"), "rb").read()).hexdigest()))
    open(os.path.join(OUT, "SIGNOFF.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
