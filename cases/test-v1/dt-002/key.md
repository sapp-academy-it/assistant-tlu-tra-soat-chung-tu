# Key dt-002

Loại bộ hồ sơ: đề tài nghiên cứu khoa học (dòng 'Đề tài NCKH' của bảng kê).
Phân loại: có lỗi (thiếu chứng từ).
Chất lượng quét: bình thường.
Case bẫy: không.
Phiên bản áp dụng: quy chế và quy trình trong `inputs/` (đúng bản đã nhận, ghi trong `inputs/README.md`).

**Kết luận mong đợi: `CAN_BO_SUNG`** (quy tắc B7 (2)).

Nguồn trích dẫn gọi tài liệu theo vai trò, như `inputs/README.md`: **quy chế** = quy chế mua sắm và chi tiêu nội bộ (docx); **quy trình** = quy trình tạm ứng, thanh toán, quyết toán của phòng Tài chính Kế toán (docx; `PL01` = Phụ lục 01 hướng dẫn hồ sơ, cột 3.1/3.2/3.3 = hồ sơ tạm ứng / thanh toán tạm ứng / thanh toán); **bảng kê** = bảng kê chứng từ gửi phòng Tài chính Kế toán (xlsx, sheet và ô, ví dụ `TT CTP!C8`). Số điều của quy chế do tự động đánh số nên không có trong văn bản: quy chế được trích theo chương và tiêu đề mục.

## Bảng từng bước

| Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn |
|---|---|---|---|---|
| B3 | Danh sách chuyển khoản mẫu 09 | có | danh sách chuyển khoản (mẫu 09) (tr.9) | bảng kê, sheet 'Đề tài NCKH'!C6; quy trình, PL01 mục VI cột 3.3 |
| B3 | Quyết định phê duyệt và giao đề tài | có | quyết định phê duyệt và giao đề tài (tr.2) | bảng kê, sheet 'Đề tài NCKH'!C7; quy trình, PL01 mục VI cột 3.3 |
| B3 | Quyết định HĐ nghiệm thu | có | quyết định hội đồng nghiệm thu (tr.6) | bảng kê, sheet 'Đề tài NCKH'!C8 |
| B3 | Biên bản họp nghiệm thu | có | biên bản họp nghiệm thu (tr.7) | bảng kê, sheet 'Đề tài NCKH'!C9 |
| B3 | Quyết định HĐ bảo vệ đề cương | có | quyết định hội đồng bảo vệ đề cương (tr.3) | bảng kê, sheet 'Đề tài NCKH'!C10 |
| B3 | Đề cương thuyết minh | có | đề cương thuyết minh đề tài (tr.4) | bảng kê, sheet 'Đề tài NCKH'!C11; quy trình, PL01 mục VI cột 3.3 |
| B3 | Giấy chứng nhận nộp sản phẩm cho phòng SĐH&QLKH | thiếu | không có trong bộ | bảng kê, sheet 'Đề tài NCKH'!C12; quy trình, PL01 mục VI cột 3.3 |
| B3 | Hợp đồng | có | hợp đồng thực hiện đề tài (tr.5) | bảng kê, sheet 'Đề tài NCKH'!C13; quy trình, PL01 mục VI cột 3.3 |
| B3 | Biên bản nghiệm thu thanh lý hợp đồng | có | biên bản nghiệm thu thanh lý hợp đồng (tr.8) | bảng kê, sheet 'Đề tài NCKH'!C14 |
| B3 | Hóa đơn tài chính, các chứng từ liên quan | không áp dụng | tùy trường hợp (Q1): bộ không có và đề bài không đòi hỏi | bảng kê, sheet 'Đề tài NCKH'!C15 |
| B5a | số tiền khớp giữa các chứng từ (đề nghị, danh sách, hóa đơn, quyết định) | OK | mọi con số khớp | quy trình, mục 5.1c |
| B5a | số bằng chữ khớp số bằng số | OK | các chứng từ có số bằng chữ đều khớp | quy trình, mục 5.1c |
| B5d | thông tin người nhận tiền đủ, thống nhất giữa các chứng từ | OK | họ tên, số tài khoản và ngân hàng khớp | quy trình, mục 5.2c |
| B5e | hóa đơn lập đúng tên, mã số thuế, địa chỉ đơn vị mua | không áp dụng | bộ không có hóa đơn | quy trình, mục 5.2b |
| B5f | khoản mua từ 5 triệu đồng không dùng tiền mặt | OK | thanh toán chuyển khoản | quy trình, mục 5.1d |
| B5g | chữ ký và dấu ở các vai trò cần có (có hay không, không xác thực) | thiếu | biên bản họp nghiệm thu thiếu chữ ký chủ tịch hội đồng | quy trình, mục 2.2.1 và biểu mẫu tương ứng |
| B5i | thời điểm và niên độ | OK | chứng từ lập trong năm 2026, đúng thời điểm giao dịch | quy trình, mục 5.1e |
| B5j | tạm ứng trước đã thanh toán | không áp dụng | không phải bộ tạm ứng | quy trình, mục 5.1f |
| B5k | mẫu biểu đúng loại, có số hiệu | OK | biểu mẫu có số hiệu | quy trình, mục 'Biểu mẫu' |
| B5h | định mức riêng của loại hồ sơ | chưa kiểm | phiên bản đầu chỉ kiểm định mức chi tiết của công tác phí (Q4) | spec, 'Giới hạn đã biết' Q4 |

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn | Việc cần làm và người cấp hoặc ký |
|---|---|---|---|---|---|---|
| F1 | bộ hồ sơ (không có giấy chứng nhận nộp sản phẩm) | Thiếu giấy chứng nhận nộp sản phẩm cho phòng SĐH&QLKH. | chặn | sửa được | bảng kê, sheet 'Đề tài NCKH'!C12; quy trình, PL01 mục VI cột 3.3 | Chủ nhiệm đề tài nộp sản phẩm và xin giấy chứng nhận của phòng Sau đại học và Quản lý khoa học (phòng SĐH&QLKH ký, đóng dấu). |
| F2 | hợp đồng thực hiện đề tài (tr.5) | Hợp đồng thực hiện đề tài không có chữ ký của bên B (chủ nhiệm đề tài). | chặn | sửa được | bảng kê, sheet 'Đề tài NCKH'!C13; quy trình, mục 5.1g | Chủ nhiệm đề tài ký hợp đồng. |
| F3 | biên bản họp nghiệm thu (tr.7) | Biên bản họp nghiệm thu không có chữ ký của chủ tịch hội đồng. | chặn | sửa được | bảng kê, sheet 'Đề tài NCKH'!C9; quy trình, mục 5.1g | Chủ tịch hội đồng nghiệm thu ký biên bản. |

## Phần không kiểm tra được

- Không có trường nào không đọc được. Ngoài phạm vi (cần dữ liệu ngoài bộ hồ sơ): đối chiếu ủy nhiệm chi, hạch toán, ngân sách còn lại, thật giả của chữ ký, con dấu và hóa đơn điện tử.

