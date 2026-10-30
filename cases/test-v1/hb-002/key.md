# Key hb-002

Loại bộ hồ sơ: học bổng (dòng 'Hoc bổng' của bảng kê).
Phân loại: có lỗi (lệch số tiền giữa quyết định và danh sách).
Chất lượng quét: bình thường.
Case bẫy: không.
Phiên bản áp dụng: quy chế và quy trình trong `inputs/` (đúng bản đã nhận, ghi trong `inputs/README.md`).

**Kết luận mong đợi: `CAN_BO_SUNG`** (quy tắc B7 (2)).

Nguồn trích dẫn gọi tài liệu theo vai trò, như `inputs/README.md`: **quy chế** = quy chế mua sắm và chi tiêu nội bộ (docx); **quy trình** = quy trình tạm ứng, thanh toán, quyết toán của phòng Tài chính Kế toán (docx; `PL01` = Phụ lục 01 hướng dẫn hồ sơ, cột 3.1/3.2/3.3 = hồ sơ tạm ứng / thanh toán tạm ứng / thanh toán); **bảng kê** = bảng kê chứng từ gửi phòng Tài chính Kế toán (xlsx, sheet và ô, ví dụ `TT CTP!C8`). Số điều của quy chế do tự động đánh số nên không có trong văn bản: quy chế được trích theo chương và tiêu đề mục.

## Bảng từng bước

| Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn |
|---|---|---|---|---|
| B3 | Giấy đề nghị thanh toán | có | giấy đề nghị thanh toán (tr.1) | bảng kê, sheet 'Hoc bổng'!C6 |
| B3 | Danh sách chuyển khoản mẫu 09 | có | danh sách chuyển khoản (mẫu 09) (tr.5) | bảng kê, sheet 'Hoc bổng'!C7; quy trình, PL01 mục II (khoản chi cho cá nhân) cột 3.3 |
| B3 | Giấy đề xuất/tờ trình/dự trù | có | tờ trình có dự trù kinh phí (tr.2) | bảng kê, sheet 'Hoc bổng'!C8 |
| B3 | Phiếu ý kiến của phòng Tài chính - Kế toán | có | phiếu ý kiến phòng tài chính - kế toán (tr.3) | bảng kê, sheet 'Hoc bổng'!C9 |
| B3 | Quyết định tặng học bổng | có | quyết định tặng học bổng (tr.4) | bảng kê, sheet 'Hoc bổng'!C10 |
| B3 | Danh sách ký nhận tiền | có | danh sách ký nhận tiền (tr.6) | bảng kê, sheet 'Hoc bổng'!C11 |
| B5a | số tiền khớp giữa các chứng từ (đề nghị, danh sách, hóa đơn, quyết định) | sai | danh sách 48.000.000 đ so với quyết định và đề nghị 42.000.000 đ | quy trình, mục 5.1c |
| B5a | số bằng chữ khớp số bằng số | OK | các chứng từ có số bằng chữ đều khớp | quy trình, mục 5.1c |
| B5d | thông tin người nhận tiền đủ, thống nhất giữa các chứng từ | OK | họ tên, số tài khoản và ngân hàng khớp | quy trình, mục 5.2c |
| B5e | hóa đơn lập đúng tên, mã số thuế, địa chỉ đơn vị mua | không áp dụng | bộ không có hóa đơn | quy trình, mục 5.2b |
| B5f | khoản mua từ 5 triệu đồng không dùng tiền mặt | OK | thanh toán chuyển khoản | quy trình, mục 5.1d |
| B5g | chữ ký và dấu ở các vai trò cần có (có hay không, không xác thực) | thiếu | danh sách ký nhận: dòng 6 chưa có chữ ký nhận | quy trình, mục 2.2.1 và biểu mẫu tương ứng |
| B5i | thời điểm và niên độ | OK | chứng từ lập trong năm 2026, đúng thời điểm giao dịch | quy trình, mục 5.1e |
| B5j | tạm ứng trước đã thanh toán | không áp dụng | không phải bộ tạm ứng | quy trình, mục 5.1f |
| B5k | mẫu biểu đúng loại, có số hiệu | OK | biểu mẫu có số hiệu | quy trình, mục 'Biểu mẫu' |
| B5h | định mức riêng của loại hồ sơ | chưa kiểm | phiên bản đầu chỉ kiểm định mức chi tiết của công tác phí (Q4) | spec, 'Giới hạn đã biết' Q4 |

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn | Việc cần làm và người cấp hoặc ký |
|---|---|---|---|---|---|---|
| F1 | danh sách chuyển khoản (mẫu 09) (tr.5); danh sách ký nhận tiền (tr.6); quyết định tặng học bổng (tr.4) | Dòng 4 (Mai Đức Dũng) ghi 12.000.000 đ trong khi quyết định cho 6.000.000 đ/sinh viên; tổng danh sách 48.000.000 đ so với quyết định và đề nghị 42.000.000 đ. | chặn | sửa được | quy trình, mục 5.1c; bảng kê, sheet 'Hoc bổng'!C7, C10 | Đơn vị sửa danh sách cho khớp quyết định (hoặc xin quyết định điều chỉnh); trưởng đơn vị ký. |
| F2 | danh sách ký nhận tiền (tr.6) | Dòng 6 (Tạ Hoài Phúc) trong danh sách ký nhận không có chữ ký nhận tiền. | chặn | sửa được | bảng kê, sheet 'Hoc bổng'!C11; quy trình, mục 5.1g | Sinh viên nhận tiền ký nhận; đơn vị lập danh sách xác nhận. |

## Phần không kiểm tra được

- Không có trường nào không đọc được. Ngoài phạm vi (cần dữ liệu ngoài bộ hồ sơ): đối chiếu ủy nhiệm chi, hạch toán, ngân sách còn lại, thật giả của chữ ký, con dấu và hóa đơn điện tử.

