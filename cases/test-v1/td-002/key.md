# Key td-002

Loại bộ hồ sơ: tuyển dụng (dòng 'Tuyển dụng' của bảng kê).
Phân loại: có lỗi (thiếu chữ ký).
Chất lượng quét: bình thường.
Case bẫy: không.
Phiên bản áp dụng: quy chế và quy trình trong `inputs/` (đúng bản đã nhận, ghi trong `inputs/README.md`).

**Kết luận mong đợi: `CAN_BO_SUNG`** (quy tắc B7 (2)).

Nguồn trích dẫn gọi tài liệu theo vai trò, như `inputs/README.md`: **quy chế** = quy chế mua sắm và chi tiêu nội bộ (docx); **quy trình** = quy trình tạm ứng, thanh toán, quyết toán của phòng Tài chính Kế toán (docx; `PL01` = Phụ lục 01 hướng dẫn hồ sơ, cột 3.1/3.2/3.3 = hồ sơ tạm ứng / thanh toán tạm ứng / thanh toán); **bảng kê** = bảng kê chứng từ gửi phòng Tài chính Kế toán (xlsx, sheet và ô, ví dụ `TT CTP!C8`). Số điều của quy chế do tự động đánh số nên không có trong văn bản: quy chế được trích theo chương và tiêu đề mục.

## Bảng từng bước

| Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn |
|---|---|---|---|---|
| B3 | Giấy đề nghị thanh toán | có | giấy đề nghị thanh toán (tr.1) | bảng kê, sheet 'Tuyển dụng'!C6 |
| B3 | Danh sách chuyển khoản | có | danh sách chuyển khoản (tr.4) | bảng kê, sheet 'Tuyển dụng'!C7 |
| B3 | Bảng thanh toán tiền chấm thi và hướng dẫn | có | bảng thanh toán tiền chấm thi và hướng dẫn (tr.3) | bảng kê, sheet 'Tuyển dụng'!C8 |
| B3 | Quyết định tuyển dụng | có | quyết định tuyển dụng (tr.2) | bảng kê, sheet 'Tuyển dụng'!C9 |
| B5a | số tiền khớp giữa các chứng từ (đề nghị, danh sách, hóa đơn, quyết định) | OK | mọi con số khớp | quy trình, mục 5.1c |
| B5a | số bằng chữ khớp số bằng số | OK | các chứng từ có số bằng chữ đều khớp | quy trình, mục 5.1c |
| B5d | thông tin người nhận tiền đủ, thống nhất giữa các chứng từ | OK | họ tên, số tài khoản và ngân hàng khớp | quy trình, mục 5.2c |
| B5e | hóa đơn lập đúng tên, mã số thuế, địa chỉ đơn vị mua | không áp dụng | bộ không có hóa đơn | quy trình, mục 5.2b |
| B5f | khoản mua từ 5 triệu đồng không dùng tiền mặt | OK | thanh toán chuyển khoản | quy trình, mục 5.1d |
| B5g | chữ ký và dấu ở các vai trò cần có (có hay không, không xác thực) | thiếu | đề nghị thanh toán thiếu chữ ký trưởng đơn vị | quy trình, mục 5.1g |
| B5i | thời điểm và niên độ | OK | chứng từ lập trong năm 2026, đúng thời điểm giao dịch | quy trình, mục 5.1e |
| B5j | tạm ứng trước đã thanh toán | không áp dụng | không phải bộ tạm ứng | quy trình, mục 5.1f |
| B5k | mẫu biểu đúng loại, có số hiệu | OK | biểu mẫu có số hiệu | quy trình, mục 'Biểu mẫu' |
| B5h | định mức riêng của loại hồ sơ | chưa kiểm | phiên bản đầu chỉ kiểm định mức chi tiết của công tác phí (Q4) | spec, 'Giới hạn đã biết' Q4 |

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn | Việc cần làm và người cấp hoặc ký |
|---|---|---|---|---|---|---|
| F1 | giấy đề nghị thanh toán (tr.1) | Giấy đề nghị thanh toán (Mẫu 05 - TT) không có chữ ký của trưởng đơn vị (ô ký để trống). | chặn | sửa được | quy trình, mục 5.1g; quy trình, mục 'Biểu mẫu' (Mẫu 05 - TT, khối chữ ký) - mức bắt buộc cần chuyên gia xác nhận (Q5) | Trưởng đơn vị ký vào đề nghị thanh toán. |
| F2 | bảng thanh toán tiền chấm thi và hướng dẫn (tr.3) | Bảng thanh toán tiền chấm thi và hướng dẫn không có chữ ký của trưởng đơn vị. | chặn | sửa được | bảng kê, sheet 'Tuyển dụng'!C8; quy trình, mục 5.1g | Trưởng đơn vị ký bảng thanh toán. |

## Phần không kiểm tra được

- Không có trường nào không đọc được. Ngoài phạm vi (cần dữ liệu ngoài bộ hồ sơ): đối chiếu ủy nhiệm chi, hạch toán, ngân sách còn lại, thật giả của chữ ký, con dấu và hóa đơn điện tử.

## Ghi chú cho chuyên gia

- Danh mục chữ ký bắt buộc của từng biểu mẫu là Q5 (chưa nguồn nào quyết định); key lấy khối chữ ký trên Mẫu 05 - TT của quy trình làm căn cứ, chuyên gia xác nhận.

