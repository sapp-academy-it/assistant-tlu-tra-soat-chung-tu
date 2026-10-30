# Key day-002

Loại bộ hồ sơ: tiền dạy học kỳ (dòng 'TTdạy, chấm thi' của bảng kê, phần tiền dạy).
Phân loại: có lỗi (lệch số tiền giữa các danh sách).
Chất lượng quét: bình thường.
Case bẫy: không.
Phiên bản áp dụng: quy chế và quy trình trong `inputs/` (đúng bản đã nhận, ghi trong `inputs/README.md`).

**Kết luận mong đợi: `CAN_BO_SUNG`** (quy tắc B7 (2)).

Nguồn trích dẫn gọi tài liệu theo vai trò, như `inputs/README.md`: **quy chế** = quy chế mua sắm và chi tiêu nội bộ (docx); **quy trình** = quy trình tạm ứng, thanh toán, quyết toán của phòng Tài chính Kế toán (docx; `PL01` = Phụ lục 01 hướng dẫn hồ sơ, cột 3.1/3.2/3.3 = hồ sơ tạm ứng / thanh toán tạm ứng / thanh toán); **bảng kê** = bảng kê chứng từ gửi phòng Tài chính Kế toán (xlsx, sheet và ô, ví dụ `TT CTP!C8`). Số điều của quy chế do tự động đánh số nên không có trong văn bản: quy chế được trích theo chương và tiêu đề mục.

## Bảng từng bước

| Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn |
|---|---|---|---|---|
| B3 | Danh sách chuyển khoản mẫu 09 | có | danh sách chuyển khoản mềm (mẫu 09) (tr.3) | bảng kê, sheet 'TTdạy, chấm thi '!C6; quy trình, PL01 mục I.1/I.2 cột 3.3 (danh sách nhận tiền, mẫu 08 và 09) |
| B3 | Bảng kê chi tiết tiền dạy (cuối kỳ) | có | bảng chi tiết thanh toán tiền dạy (phòng hr) (tr.1) | bảng kê, sheet 'TTdạy, chấm thi '!C7; quy trình, PL01 mục I.1/I.2 cột 3.3 (bảng chi tiết thanh toán tiền dạy, phòng HR) |
| B3 | Danh sách thanh toán chuyển khoản (Mẫu 08) | có | danh sách chuyển khoản (mẫu 08) (tr.2) | bảng kê, sheet 'TTdạy, chấm thi '!-; quy trình, PL01 mục I.1/I.2 cột 3.3 |
| B3 | Bảng thông tin giảng viên mời (Mẫu 07) | có | bảng thông tin giảng viên mời (mẫu 07) (tr.4) | bảng kê, sheet 'TTdạy, chấm thi '!-; quy trình, mục 5.2c và biểu mẫu Mẫu 07 - TCKT |
| B3 | Bảng tính tiền lương nhân sự | không áp dụng | tùy trường hợp (Q1): bộ không có và đề bài không đòi hỏi | bảng kê, sheet 'TTdạy, chấm thi '!C20 |
| B5a | số tiền khớp giữa các chứng từ (đề nghị, danh sách, hóa đơn, quyết định) | sai | Phạm Thị D: Mẫu 08 4.200.000 đ, bảng HR 4.000.000 đ | quy trình, mục 5.1c |
| B5a | số bằng chữ khớp số bằng số | OK | các chứng từ có số bằng chữ đều khớp | quy trình, mục 5.1c |
| B5d | thông tin người nhận tiền đủ, thống nhất giữa các chứng từ | OK | họ tên, số tài khoản và ngân hàng khớp | quy trình, mục 5.2c |
| B5e | hóa đơn lập đúng tên, mã số thuế, địa chỉ đơn vị mua | không áp dụng | bộ không có hóa đơn | quy trình, mục 5.2b |
| B5f | khoản mua từ 5 triệu đồng không dùng tiền mặt | OK | thanh toán chuyển khoản | quy trình, mục 5.1d |
| B5g | chữ ký và dấu ở các vai trò cần có (có hay không, không xác thực) | thiếu | Mẫu 07 thiếu chữ ký người lập biểu | quy trình, mục 2.2.1 và biểu mẫu tương ứng |
| B5i | thời điểm và niên độ | OK | chứng từ lập trong năm 2026, đúng thời điểm giao dịch | quy trình, mục 5.1e |
| B5j | tạm ứng trước đã thanh toán | không áp dụng | không phải bộ tạm ứng | quy trình, mục 5.1f |
| B5k | mẫu biểu đúng loại, có số hiệu | OK | biểu mẫu có số hiệu | quy trình, mục 'Biểu mẫu' |
| B5h | định mức riêng của loại hồ sơ | chưa kiểm | phiên bản đầu chỉ kiểm định mức chi tiết của công tác phí (Q4) | spec, 'Giới hạn đã biết' Q4 |

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn | Việc cần làm và người cấp hoặc ký |
|---|---|---|---|---|---|---|
| F1 | danh sách chuyển khoản (mẫu 08) (tr.2); bảng chi tiết thanh toán tiền dạy (phòng hr) (tr.1); danh sách chuyển khoản mềm (mẫu 09) (tr.3) | Dòng 2 (Phạm Thị D): Mẫu 08 ghi 4.200.000 đ, bảng HR ghi 4.000.000 đ; tổng Mẫu 08 16.700.000 đ so với bảng HR 16.500.000 đ (lệch 200.000 đ), Mẫu 09 theo Mẫu 08. | chặn | sửa được | quy trình, mục 5.1c; quy trình, PL01 mục I.1 cột 3.3 | Đơn vị sửa Mẫu 08 và Mẫu 09 theo bảng HR (hoặc phòng HR xác nhận lại); trưởng đơn vị và người lập biểu ký. |
| F2 | bảng chi tiết thanh toán tiền dạy (phòng hr) (tr.1) | Bảng chi tiết thanh toán tiền dạy không có chữ ký của phòng HR. | chặn | sửa được | quy trình, PL01 mục I.1/I.2 cột 3.3 (bảng chi tiết do phòng HR lập); quy trình, mục 5.1g | Phòng HR ký bảng chi tiết. |
| F3 | bảng thông tin giảng viên mời (mẫu 07) (tr.4) | Bảng thông tin giảng viên mời (Mẫu 07) không có chữ ký của người lập biểu. | chặn | sửa được | quy trình, mục 5.2c; quy trình, mục 'Biểu mẫu' (Mẫu 07 - TCKT) | Người lập biểu ký Mẫu 07. |

## Phần không kiểm tra được

- Không có trường nào không đọc được. Ngoài phạm vi (cần dữ liệu ngoài bộ hồ sơ): đối chiếu ủy nhiệm chi, hạch toán, ngân sách còn lại, thật giả của chữ ký, con dấu và hóa đơn điện tử.

