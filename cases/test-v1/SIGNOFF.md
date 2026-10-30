# SIGNOFF test-v1

Bản ghi ký key của test set `test-v1` (phiên bản `v1`, tag `v1`). Cách ký: chuyên gia nghiệp vụ duyệt (approve) PR chứa `cases/test-v1/` trên GitHub; approval của commit cuối là chữ ký. Sau khi ký, `key.md` của mọi case và tệp này không đổi (đổi sẽ làm sai sha256 đã ký).

- Vai trò người ký: chuyên gia nghiệp vụ (chủ sở hữu, người đặt hàng).
- Ngày ký: ngày approve PR trên GitHub (GitHub ghi ngày; tệp này không điền tay để không đổi sau khi ký).
- sha256 của key: `faaa40c8ec9fc4dfd5b1d1f1951a36ec72d58943e45df2a0d8edc0c03179041d` (lệnh: `cat cases/test-v1/*/key.md | sha256sum`, 42 tệp `key.md` theo thứ tự tên thư mục).
- Số case: 42 (công tác phí 20: 6 hợp lệ, 14 có lỗi; 11 loại còn lại mỗi loại 2: 1 hợp lệ, 1 có lỗi; 17 hợp lệ, 8 quét kém, 10 bẫy).
- Số phát hiện mong đợi trong key: 64 (59 mức chặn, 5 mức cảnh báo). Kết luận: CAN_BO_SUNG 19, DU_DIEU_KIEN 17, KHONG_HOP_LE 6.
- Số trường trong các `fields.md`: 5246.

## Chuyên gia kiểm gì, đối chiếu với tài liệu nào

1. Mỗi `key.md`: kết luận mong đợi đúng theo quy tắc B7 của spec; mỗi phát hiện có nguồn. Đối chiếu nguồn với `inputs/`: **quy chế** (Chương VI: điều kiện, định mức thuê phòng 600.000 đ/phòng đơn và phụ cấp 300.000 đ/ngày cho cán bộ, giảng viên, thời hạn 15 ngày làm việc, công tác trong ngày; Chương III nguyên tắc chi; Chương VII học bổng), **quy trình** (mục 5.1b đến 5.1g, 5.2b, 5.2c, 2.2.1, 2.2.3, 'Biểu mẫu', Phụ lục 01 các mục I.1, I.3, V, VI và 'sự kiện'), **bảng kê** (từng sheet và ô được trích), **bảng mô tả 'AI kế toán thanh toán'** (sheet 'Gửi SAPP' ô C18, báo giá có dấu đỏ).
2. Q1 (bảng kê không nói dòng nào bắt buộc): mỗi `key.md` ghi từng dòng bảng kê là 'có', 'thiếu' hoặc 'không áp dụng'. Chuyên gia xác nhận các dòng ghi 'thiếu' (chỉ dùng cho dòng có trong cả bảng kê và Phụ lục 01 cột 3.3) và các dòng 'không áp dụng' (tùy trường hợp).
3. Q5 (chữ ký bắt buộc của từng biểu mẫu): các phát hiện 'thiếu chữ ký' của trưởng đơn vị, chủ tịch hội đồng, bên B, phòng HR, người lập biểu... dựa vào khối chữ ký của biểu mẫu hoặc vai trò hiển nhiên; chuyên gia xác nhận mức chặn của từng phát hiện đó.
4. Chuyên gia xem `fields.md` của vài case để chắc bản chép khớp ảnh (đặc biệt các trường ghi KHÔNG ĐỌC ĐƯỢC ở ctp-015, hnh-002 là cố ý bị mực đè).

## Điểm người dựng test set tự quyết, chuyên gia xác nhận

- Bảng kê trong `inputs/` có 10 sheet, spec ghi 12 loại. Để giữ đúng 11 loại ngoài công tác phí (spec: 22 case), sheet 'TTdạy, chấm thi' được tách thành 3 loại theo Phụ lục 01 mục I (tiền dạy; chấm thi; xây dựng ngân hàng câu hỏi/ra đề): day-, cho-, nhc-.
- Định mức thuê phòng so với số tiền trên hóa đơn đã gồm thuế; ca vi phạm (ctp-011) vượt cả khi chưa tính thuế nên không bị ảnh hưởng. Số ngày phụ cấp tính cả ngày đi và về (3 ngày 2 đêm = 3 ngày phụ cấp), theo ví dụ của spec.
- Phát hiện về tạm ứng chưa thanh toán (hnh-002, quy trình 5.1f) xếp loại 'sửa được' (thanh toán tạm ứng trước rồi nộp lại), không phải 'vi phạm'.
- Quá niên độ (sach-002, 5.1e) xếp loại 'vi phạm' theo B7; đề bài nêu năm tài chính là năm dương lịch (quy trình không định nghĩa).
- Ở các case bẫy, `de-bai.md` có thêm dòng 'Lời người dùng' (yêu cầu của người dùng cố ý thử giới hạn) ngoài loại nghiệp vụ và ngày xét.
- Mẫu giấy đi đường dùng số hiệu 'C16 - HD' hư cấu; Q2 (mẫu theo thông tư cũ) chưa đưa vào key, key không có phát hiện về căn cứ ban hành của mẫu.
- Dữ liệu cá nhân (căn cước, mã số thuế, điện thoại, tài khoản) đều hư cấu, ghi dạng nhóm số có dấu cách hoặc 8 chữ số; mã số thuế nhà cung cấp hư cấu ghi dạng có gạch nối. Mã số thuế và địa chỉ của Trường là dữ liệu pháp nhân công khai (quy trình mục 5.2b).

## Sinh lại ảnh

`python3 -I cases/test-v1/_gen/build.py` dựng lại toàn bộ `cases/test-v1/<mã-case>/` (ảnh, `de-bai.md`, `fields.md`, `key.md`) và tệp này: xác định, không dùng mạng, chỉ ghi dưới `cases/test-v1/`; cần Pillow, numpy và phông Liberation, DejaVu của hệ thống.

## sha256 từng key

| Case | sha256 của key.md |
|---|---|
| cho-001 | `672d4ab9c0fa5c9d17248103b8279b02acbcd4e3888c1ae9b6fdba04ad85cdf8` |
| cho-002 | `9bdf031c888658637a7775d211cd8bbff6fb290518229a9ed31c303bf4b14447` |
| ctp-001 | `74d049844ca30faac25a3a6ff78405921818e2fc43b0e57a33d4eee8f6495da8` |
| ctp-002 | `cb11a8bc5fcd452fc29cb71e815c2a93c347e69033f6583c5590c1d48d2d1bc8` |
| ctp-003 | `e578c4e145f129bb8379025b79f29bc3027495769c5477c6579bbd8221d7cd8e` |
| ctp-004 | `32320109c8fcc22772e1cad75e88fdecd06587bc98de3e053003be705ea09087` |
| ctp-005 | `a08f1679825f5d49ac114a91bd8896f280f81444d92f245da30e41f990b12395` |
| ctp-006 | `49ffb4337208ee78113008de545709556422548cb341f6593442aa0b3f5d9847` |
| ctp-007 | `a6fd34a6da5c9c63f470268471a69a7bbbd8f54cdbbe08c59d111a252ddccb85` |
| ctp-008 | `640a76f75e23e01632a5c5898f7c115e605bf9a5a0f88dcd4cc603bc48fdfd39` |
| ctp-009 | `e1872bd569bc50553f1c9d2245b5149393a71a7ff708408a99824fe29f8eae00` |
| ctp-010 | `2d78ea5478b0bf20050c39928084c39be51730e98fa9ac6adb4a0ce4b1451f0b` |
| ctp-011 | `72558d4eaf747588ce439de1e476063ae69d0906c287ab932b19091585dd9a78` |
| ctp-012 | `483bd53fe068f7d2d97dde913b81a6d36d8c8cd7789357c59360157f5b62eb00` |
| ctp-013 | `4f0e4c57196b9aea9dee4310247aa628189b91209f47a1da22c467f82bd5b1aa` |
| ctp-014 | `d4a9674a615049a0098ed1b68ebf71bb8c1c7242321c720daa667d1c9c9d013f` |
| ctp-015 | `475a342173ed272e2d054772bd86926e4bc66962505b30f18a385b0e0d2f2566` |
| ctp-016 | `cc8f5dcc597446316a365ec117853e7fa0a2ff98f46eb3583d14ae5569cd4c97` |
| ctp-017 | `5eb3b0f5a4fe26221afe35ec59c0876a77105364a2b9c8089d090b2934ac28a1` |
| ctp-018 | `886126d9c7a22f07f8058a538b55ff984d8130d87374af2101a439dd5b2e0f14` |
| ctp-019 | `54b36df46543401340facc9157f7608c9dd105b211bb4f7b9045d798b4918765` |
| ctp-020 | `fc5b50f891096ee65f845ef2f9f7dce88b9a444451f53d64d812509a757a5390` |
| day-001 | `1a541daf36470090581007bf7801b92db0ef5942e260d93b558fb07a5e81f29b` |
| day-002 | `2e56b428d44b29b2d33cb6877ae485fa4a784a4397156513ae7679de802b7b33` |
| dt-001 | `88a1794d9b5099d01d37b689d8d6fd2f4377fb2ea6d9d024397eb147bbb66089` |
| dt-002 | `c23b51eb96ec36a085cd0304bf7c6bc241d602392a786a25072a591df60b172e` |
| hb-001 | `333da04d3ec7397803a28b5ebd22655eeb8dc4ea19990aa80ba5fd6d4f5c0b3f` |
| hb-002 | `9c6f82a388975771467368b5e0b534931d790e1ada252c55a208d9ae5cdb16c7` |
| hnh-001 | `49e0587bc6e6d3e0228d87c2d453203023d95a153b45eb826779e4a315c5425b` |
| hnh-002 | `c9929be0671e948b96a751886fd3df6ebf7fb9c57d6b63993172989a6fd6aec1` |
| mh-001 | `a67ef905a91cd6db2ef5a989107de1fa9fb9405adb022a30ffd1d3bafe81c930` |
| mh-002 | `23ce450eb812032436c4058d9f5a190e441c454d5a2d9e638942c764306b434b` |
| nhc-001 | `279534276fcd85a545023b09dc14b7812f669f1636f553ac217e49fd5ad59ebc` |
| nhc-002 | `f659a709b110bd1e3f36adcb51bf2748b5969c8ce41a7f51613797fda108d165` |
| qtc-001 | `576cc3007f55d485aecbfdcb4408c3556c0a4bfcd8fb12ce78a4f52019f00ede` |
| qtc-002 | `a58e7731ec87a9fffda5cb4465c1019efa6d62f294abeb582ee01c877bf0a55c` |
| sach-001 | `727d24dee87046110980c6b43c05664bd5182f8ecdc853de5287658945b63a75` |
| sach-002 | `c5199e435cc2cd2b46e8cab37028d9525fe3ca8f37db85fd8d24e36b42a8840b` |
| td-001 | `bbc671d30ba88305acd475a5c5c49520c6c1cc3c41df23c26d5263425c6e85d8` |
| td-002 | `8a4fbe2c4c74bdc8dc9d29a00567058d9dffeedd59d70bc6fd2416162dbafea8` |
| ttp-001 | `aff858b9dec52631d8f6d9d69b639863632f60e1c149efa0683f3689d7b20d29` |
| ttp-002 | `f0cd4d26942bbb485d71ae2667987dfe77102fa1d4d9cf04e67aa99f1ec2baf2` |
