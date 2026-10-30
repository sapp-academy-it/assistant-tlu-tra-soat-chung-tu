# Key ttp-002

Loại bộ hồ sơ: thuê xe đưa sinh viên đi thực tế (dòng 'SV đi thực tập' của bảng kê).
Phân loại: có lỗi (lệch số tiền hóa đơn).
Chất lượng quét: bình thường.
Case bẫy: không.
Phiên bản áp dụng: quy chế và quy trình trong `inputs/` (đúng bản đã nhận, ghi trong `inputs/README.md`).

**Kết luận mong đợi: `CAN_BO_SUNG`** (quy tắc B7 (2)).

Nguồn trích dẫn gọi tài liệu theo vai trò, như `inputs/README.md`: **quy chế** = quy chế mua sắm và chi tiêu nội bộ (docx); **quy trình** = quy trình tạm ứng, thanh toán, quyết toán của phòng Tài chính Kế toán (docx; `PL01` = Phụ lục 01 hướng dẫn hồ sơ, cột 3.1/3.2/3.3 = hồ sơ tạm ứng / thanh toán tạm ứng / thanh toán); **bảng kê** = bảng kê chứng từ gửi phòng Tài chính Kế toán (xlsx, sheet và ô, ví dụ `TT CTP!C8`). Số điều của quy chế do tự động đánh số nên không có trong văn bản: quy chế được trích theo chương và tiêu đề mục.

## Bảng từng bước

| Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn |
|---|---|---|---|---|
| B3 | Đề nghị thanh toán | có | giấy đề nghị thanh toán (tr.1) | bảng kê, sheet 'SV đi thực tập'!C6; quy trình, PL01 mục I.1 cột 3.3 |
| B3 | Giấy đề xuất/tờ trình/dự trù | có | tờ trình có dự trù kinh phí (tr.2) | bảng kê, sheet 'SV đi thực tập'!C7; quy trình, PL01 mục I.1 cột 3.3 |
| B3 | Phiếu ý kiến của phòng Tài chính - Kế toán | có | phiếu ý kiến phòng tài chính - kế toán (tr.3) | bảng kê, sheet 'SV đi thực tập'!C8; quy trình, PL01 mục I.1 cột 3.3 |
| B3 | Hợp đồng | có | hợp đồng thuê xe (tr.5) | bảng kê, sheet 'SV đi thực tập'!C9; quy trình, PL01 mục I.1 cột 3.3 (từ 20 triệu đồng) |
| B3 | Bảng kiểm soát trình ký hợp đồng | có | bảng kiểm soát trình ký hợp đồng (tr.6) | bảng kê, sheet 'SV đi thực tập'!C10; quy trình, PL01 mục I.1 cột 3.3 |
| B3 | Báo giá | có | báo giá (tr.4) | bảng kê, sheet 'SV đi thực tập'!C11; quy trình, PL01 mục I.1 cột 3.3 |
| B3 | Quyết định cho SV đi thực tập/thực tế kèm danh sách | có | quyết định cho sinh viên đi thực tế (tr.7) | bảng kê, sheet 'SV đi thực tập'!C12 |
| B3 | Biên bản thanh lý hợp đồng/biên bản nghiệm thu | có | biên bản nghiệm thu và thanh lý hợp đồng (tr.8) | bảng kê, sheet 'SV đi thực tập'!C13; quy trình, PL01 mục I.1 cột 3.3 (lần cuối) |
| B3 | Hóa đơn tài chính | có | hóa đơn thuê xe (tr.9) | bảng kê, sheet 'SV đi thực tập'!C14; quy trình, PL01 mục I.1 cột 3.3 |
| B5a | số tiền khớp giữa các chứng từ (đề nghị, danh sách, hóa đơn, quyết định) | sai | đề nghị và hợp đồng 24.200.000 đ, hóa đơn 24.750.000 đ | quy trình, mục 5.1c |
| B5a | số bằng chữ khớp số bằng số | OK | các chứng từ có số bằng chữ đều khớp | quy trình, mục 5.1c |
| B5d | thông tin người nhận tiền đủ, thống nhất giữa các chứng từ | OK | họ tên, số tài khoản và ngân hàng khớp | quy trình, mục 5.2c |
| B5e | hóa đơn lập đúng tên, mã số thuế, địa chỉ đơn vị mua | OK | hóa đơn thuê xe (tr.9) | quy trình, mục 5.2b |
| B5f | khoản mua từ 5 triệu đồng không dùng tiền mặt | OK | thanh toán chuyển khoản | quy trình, mục 5.1d |
| B5g | chữ ký và dấu ở các vai trò cần có (có hay không, không xác thực) | thiếu | báo giá không có dấu nhà cung cấp; hợp đồng thiếu chữ ký bên B | quy trình, mục 2.2.1 và biểu mẫu tương ứng |
| B5i | thời điểm và niên độ | OK | chứng từ lập trong năm 2026, đúng thời điểm giao dịch | quy trình, mục 5.1e |
| B5j | tạm ứng trước đã thanh toán | không áp dụng | không phải bộ tạm ứng | quy trình, mục 5.1f |
| B5k | mẫu biểu đúng loại, có số hiệu | OK | biểu mẫu có số hiệu | quy trình, mục 'Biểu mẫu' |
| B5h | định mức riêng của loại hồ sơ | chưa kiểm | phiên bản đầu chỉ kiểm định mức chi tiết của công tác phí (Q4) | spec, 'Giới hạn đã biết' Q4 |

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn | Việc cần làm và người cấp hoặc ký |
|---|---|---|---|---|---|---|
| F1 | hóa đơn thuê xe (tr.9); giấy đề nghị thanh toán (tr.1); hợp đồng thuê xe (tr.5) | Hóa đơn 24.750.000 đ lớn hơn số tiền đề nghị và giá trị hợp đồng 24.200.000 đ (lệch 550.000 đ). | chặn | sửa được | quy trình, mục 5.1c; quy trình, PL01 mục I.1 cột 3.3 | Nhà cung cấp lập lại hóa đơn đúng giá trị hợp đồng, hoặc đơn vị có phụ lục hợp đồng và đề nghị điều chỉnh; trưởng đơn vị ký. |
| F2 | báo giá (tr.4) | Báo giá của nhà cung cấp có chữ ký nhưng không có dấu đỏ của nhà cung cấp. | chặn | sửa được | bảng mô tả của khách hàng (xlsx 'AI kế toán thanh toán'), sheet 'Gửi SAPP' ô C18 (báo giá có dấu đỏ/chữ ký của nhà cung cấp); bảng kê, sheet 'SV đi thực tập'!C11 | Nhà cung cấp đóng dấu báo giá (nhà cung cấp ký, đóng dấu). |
| F3 | hợp đồng thuê xe (tr.5) | Hợp đồng thuê xe không có chữ ký của đại diện bên B (nhà cung cấp). | chặn | sửa được | bảng kê, sheet 'SV đi thực tập'!C9; quy trình, mục 5.1g | Nhà cung cấp ký hợp đồng. |

## Phần không kiểm tra được

- Không có trường nào không đọc được. Ngoài phạm vi (cần dữ liệu ngoài bộ hồ sơ): đối chiếu ủy nhiệm chi, hạch toán, ngân sách còn lại, thật giả của chữ ký, con dấu và hóa đơn điện tử.

