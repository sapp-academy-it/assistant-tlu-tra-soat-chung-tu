# Key qtc-002

Loại bộ hồ sơ: quyết toán chương trình, sự kiện (dòng 'QT CT' của bảng kê).
Phân loại: có lỗi (lệch số tiền quyết toán).
Chất lượng quét: bình thường.
Case bẫy: không.
Phiên bản áp dụng: quy chế và quy trình trong `inputs/` (đúng bản đã nhận, ghi trong `inputs/README.md`).

**Kết luận mong đợi: `CAN_BO_SUNG`** (quy tắc B7 (2)).

Nguồn trích dẫn gọi tài liệu theo vai trò, như `inputs/README.md`: **quy chế** = quy chế mua sắm và chi tiêu nội bộ (docx); **quy trình** = quy trình tạm ứng, thanh toán, quyết toán của phòng Tài chính Kế toán (docx; `PL01` = Phụ lục 01 hướng dẫn hồ sơ, cột 3.1/3.2/3.3 = hồ sơ tạm ứng / thanh toán tạm ứng / thanh toán); **bảng kê** = bảng kê chứng từ gửi phòng Tài chính Kế toán (xlsx, sheet và ô, ví dụ `TT CTP!C8`). Số điều của quy chế do tự động đánh số nên không có trong văn bản: quy chế được trích theo chương và tiêu đề mục.

## Bảng từng bước

| Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn |
|---|---|---|---|---|
| B3 | Giấy đề nghị thanh toán | có | giấy đề nghị thanh toán (tr.1) | bảng kê, sheet 'QT CT'!C6; quy trình, PL01 mục (sự kiện) cột 3.3 |
| B3 | Quyết toán chương trình | có | quyết toán chương trình (tr.8) | bảng kê, sheet 'QT CT'!C7; quy trình, PL01 mục (sự kiện) cột 3.3 (bảng tổng hợp quyết toán) |
| B3 | Giấy đề xuất/tờ trình/dự trù | có | tờ trình có dự trù kinh phí (tr.2) | bảng kê, sheet 'QT CT'!C8 |
| B3 | Phiếu ý kiến của phòng Tài chính - Kế toán | có | phiếu ý kiến phòng tài chính - kế toán (tr.3) | bảng kê, sheet 'QT CT'!C9 |
| B3 | Hóa đơn tài chính | có | hóa đơn dịch vụ sự kiện (tr.7) | bảng kê, sheet 'QT CT'!C10; quy trình, PL01 mục (sự kiện) cột 3.3 |
| B3 | Hợp đồng | có | hợp đồng dịch vụ tổ chức sự kiện (tr.5) | bảng kê, sheet 'QT CT'!C11; quy trình, PL01 mục (sự kiện) cột 3.3 (từ 20 triệu đồng) |
| B3 | Báo giá | có | báo giá (tr.4) | bảng kê, sheet 'QT CT'!C12 |
| B3 | BB bàn giao và nghiệm thu | có | biên bản bàn giao và nghiệm thu (tr.6) | bảng kê, sheet 'QT CT'!C13; quy trình, PL01 mục (sự kiện) cột 3.3 (biên bản nghiệm thu) |
| B3 | Danh sách sinh viên nhận tiền | có | danh sách sinh viên nhận tiền (tr.9) | bảng kê, sheet 'QT CT'!C14; quy trình, PL01 mục (sự kiện) cột 3.3 (danh sách nhận tiền) |
| B5a | số tiền khớp giữa các chứng từ (đề nghị, danh sách, hóa đơn, quyết định) | sai | quyết toán 27.000.000 đ; hợp đồng và hóa đơn 22.000.000 đ; đề nghị 25.000.000 đ | quy trình, mục 5.1c |
| B5a | số bằng chữ khớp số bằng số | OK | các chứng từ có số bằng chữ đều khớp | quy trình, mục 5.1c |
| B5d | thông tin người nhận tiền đủ, thống nhất giữa các chứng từ | OK | họ tên, số tài khoản và ngân hàng khớp | quy trình, mục 5.2c |
| B5e | hóa đơn lập đúng tên, mã số thuế, địa chỉ đơn vị mua | sai | hóa đơn ghi mã số thuế sai | quy trình, mục 5.2b |
| B5f | khoản mua từ 5 triệu đồng không dùng tiền mặt | OK | thanh toán chuyển khoản | quy trình, mục 5.1d |
| B5g | chữ ký và dấu ở các vai trò cần có (có hay không, không xác thực) | thiếu | biên bản bàn giao và nghiệm thu thiếu chữ ký bên B | quy trình, mục 2.2.1 và biểu mẫu tương ứng |
| B5i | thời điểm và niên độ | OK | chứng từ lập trong năm 2026, đúng thời điểm giao dịch | quy trình, mục 5.1e |
| B5j | tạm ứng trước đã thanh toán | không áp dụng | không phải bộ tạm ứng | quy trình, mục 5.1f |
| B5k | mẫu biểu đúng loại, có số hiệu | OK | biểu mẫu có số hiệu | quy trình, mục 'Biểu mẫu' |
| B5h | định mức riêng của loại hồ sơ | chưa kiểm | phiên bản đầu chỉ kiểm định mức chi tiết của công tác phí (Q4) | spec, 'Giới hạn đã biết' Q4 |

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn | Việc cần làm và người cấp hoặc ký |
|---|---|---|---|---|---|---|
| F1 | quyết toán chương trình (tr.8); hóa đơn dịch vụ sự kiện (tr.7); hợp đồng dịch vụ tổ chức sự kiện (tr.5); giấy đề nghị thanh toán (tr.1) | Quyết toán ghi dịch vụ tổ chức sự kiện 24.000.000 đ (tổng 27.000.000 đ) trong khi hợp đồng, hóa đơn và báo giá là 22.000.000 đ và đề nghị thanh toán là 25.000.000 đ. | chặn | sửa được | quy trình, mục 5.1c; quy trình, PL01 mục (sự kiện) cột 3.3 | Đơn vị sửa bảng quyết toán cho khớp hợp đồng và hóa đơn; trưởng đơn vị ký. |
| F2 | biên bản bàn giao và nghiệm thu (tr.6) | Biên bản bàn giao và nghiệm thu không có chữ ký của bên B (nhà cung cấp). | chặn | sửa được | bảng kê, sheet 'QT CT'!C13; quy trình, mục 5.1g | Nhà cung cấp ký biên bản. |
| F3 | hóa đơn dịch vụ sự kiện (tr.7) | Mã số thuế đơn vị mua trên hóa đơn ghi 0101825721, không đúng mã số thuế của Trường (0101825712). | chặn | sửa được | quy trình, mục 5.2b | Nhà cung cấp lập lại hóa đơn đúng mã số thuế. |

## Phần không kiểm tra được

- Không có trường nào không đọc được. Ngoài phạm vi (cần dữ liệu ngoài bộ hồ sơ): đối chiếu ủy nhiệm chi, hạch toán, ngân sách còn lại, thật giả của chữ ký, con dấu và hóa đơn điện tử.

