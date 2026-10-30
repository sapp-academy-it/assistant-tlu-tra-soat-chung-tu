# Key nhc-002

Loại bộ hồ sơ: xây dựng ngân hàng câu hỏi (dòng 'TTdạy, chấm thi' của bảng kê, phần ra đề).
Phân loại: có lỗi (thiếu chứng từ).
Chất lượng quét: bình thường.
Case bẫy: không.
Phiên bản áp dụng: quy chế và quy trình trong `inputs/` (đúng bản đã nhận, ghi trong `inputs/README.md`).

**Kết luận mong đợi: `CAN_BO_SUNG`** (quy tắc B7 (2)).

Nguồn trích dẫn gọi tài liệu theo vai trò, như `inputs/README.md`: **quy chế** = quy chế mua sắm và chi tiêu nội bộ (docx); **quy trình** = quy trình tạm ứng, thanh toán, quyết toán của phòng Tài chính Kế toán (docx; `PL01` = Phụ lục 01 hướng dẫn hồ sơ, cột 3.1/3.2/3.3 = hồ sơ tạm ứng / thanh toán tạm ứng / thanh toán); **bảng kê** = bảng kê chứng từ gửi phòng Tài chính Kế toán (xlsx, sheet và ô, ví dụ `TT CTP!C8`). Số điều của quy chế do tự động đánh số nên không có trong văn bản: quy chế được trích theo chương và tiêu đề mục.

## Bảng từng bước

| Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn |
|---|---|---|---|---|
| B3 | Danh sách chuyển khoản mẫu 09 | thiếu | không có trong bộ | bảng kê, sheet 'TTdạy, chấm thi '!C6; quy trình, PL01 mục I.3 cột 3.3 (danh sách nhận tiền, mẫu 08 và 09) |
| B3 | Giấy đề xuất/tờ trình/dự trù | có | tờ trình có dự trù kinh phí (tr.1) | bảng kê, sheet 'TTdạy, chấm thi '!C13 |
| B3 | Phiếu ý kiến của phòng Tài chính - Kế toán | có | phiếu ý kiến phòng tài chính - kế toán (tr.2) | bảng kê, sheet 'TTdạy, chấm thi '!C14 |
| B3 | Bảng tính tiền xây dựng ngân hàng câu hỏi | có | bảng tính tiền xây dựng ngân hàng câu hỏi (tr.4) | bảng kê, sheet 'TTdạy, chấm thi '!C15; quy trình, PL01 mục I.3 cột 3.3 |
| B3 | Quyết định thành lập HĐ nghiệm thu | có | quyết định thành lập hội đồng nghiệm thu (tr.3) | bảng kê, sheet 'TTdạy, chấm thi '!C16 |
| B3 | Biên bản bàn giao ngân hàng câu hỏi | có | biên bản bàn giao ngân hàng câu hỏi (tr.5) | bảng kê, sheet 'TTdạy, chấm thi '!C17 |
| B5a | số tiền khớp giữa các chứng từ (đề nghị, danh sách, hóa đơn, quyết định) | OK | mọi con số khớp | quy trình, mục 5.1c |
| B5a | số bằng chữ khớp số bằng số | OK | các chứng từ có số bằng chữ đều khớp | quy trình, mục 5.1c |
| B5d | thông tin người nhận tiền đủ, thống nhất giữa các chứng từ | chưa kiểm | không có danh sách chuyển khoản | quy trình, mục 5.2c |
| B5e | hóa đơn lập đúng tên, mã số thuế, địa chỉ đơn vị mua | không áp dụng | bộ không có hóa đơn | quy trình, mục 5.2b |
| B5f | khoản mua từ 5 triệu đồng không dùng tiền mặt | OK | thanh toán chuyển khoản | quy trình, mục 5.1d |
| B5g | chữ ký và dấu ở các vai trò cần có (có hay không, không xác thực) | thiếu | bảng tính tiền thiếu chữ ký trưởng đơn vị | quy trình, mục 2.2.1 và biểu mẫu tương ứng |
| B5i | thời điểm và niên độ | OK | chứng từ lập trong năm 2026, đúng thời điểm giao dịch | quy trình, mục 5.1e |
| B5j | tạm ứng trước đã thanh toán | không áp dụng | không phải bộ tạm ứng | quy trình, mục 5.1f |
| B5k | mẫu biểu đúng loại, có số hiệu | OK | biểu mẫu có số hiệu | quy trình, mục 'Biểu mẫu' |
| B5h | định mức riêng của loại hồ sơ | chưa kiểm | phiên bản đầu chỉ kiểm định mức chi tiết của công tác phí (Q4) | spec, 'Giới hạn đã biết' Q4 |

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn | Việc cần làm và người cấp hoặc ký |
|---|---|---|---|---|---|---|
| F1 | bộ hồ sơ (không có danh sách chuyển khoản) | Thiếu danh sách chuyển khoản (Mẫu 08 và Mẫu 09) của người nhận thù lao; không có thông tin tài khoản người nhận. | chặn | sửa được | bảng kê, sheet 'TTdạy, chấm thi '!C6; quy trình, PL01 mục I.3 cột 3.3; quy trình, mục 5.2c | Đơn vị lập Mẫu 08 (bản cứng) và Mẫu 09 (bản mềm); trưởng đơn vị, trưởng phòng TCKT và Hiệu trưởng ký theo mẫu. |
| F2 | biên bản bàn giao ngân hàng câu hỏi (tr.5) | Biên bản bàn giao ngân hàng câu hỏi không có chữ ký của bên nhận. | chặn | sửa được | bảng kê, sheet 'TTdạy, chấm thi '!C17; quy trình, mục 5.1g | Bên nhận ký biên bản bàn giao. |
| F3 | bảng tính tiền xây dựng ngân hàng câu hỏi (tr.4) | Bảng tính tiền xây dựng ngân hàng câu hỏi không có chữ ký của trưởng đơn vị. | chặn | sửa được | bảng kê, sheet 'TTdạy, chấm thi '!C15; quy trình, mục 5.1g | Trưởng đơn vị ký bảng tính tiền. |

## Phần không kiểm tra được

- Không có trường nào không đọc được. Ngoài phạm vi (cần dữ liệu ngoài bộ hồ sơ): đối chiếu ủy nhiệm chi, hạch toán, ngân sách còn lại, thật giả của chữ ký, con dấu và hóa đơn điện tử.

