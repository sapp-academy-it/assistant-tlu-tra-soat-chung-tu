# Key hnh-002

Loại bộ hồ sơ: hội nghị, hội thảo, bộ hồ sơ tạm ứng (quy trình PL01 mục V cột 3.1; bảng kê chỉ liệt kê hồ sơ thanh toán).
Phân loại: có lỗi (tạm ứng khi chưa thanh toán tạm ứng trước).
Chất lượng quét: kém (có trang xoay, mờ, bị đè hoặc có trường không đọc được).
Case bẫy: không.
Phiên bản áp dụng: quy chế và quy trình trong `inputs/` (đúng bản đã nhận, ghi trong `inputs/README.md`).

**Kết luận mong đợi: `CAN_BO_SUNG`** (quy tắc B7 (2)).

Nguồn trích dẫn gọi tài liệu theo vai trò, như `inputs/README.md`: **quy chế** = quy chế mua sắm và chi tiêu nội bộ (docx); **quy trình** = quy trình tạm ứng, thanh toán, quyết toán của phòng Tài chính Kế toán (docx; `PL01` = Phụ lục 01 hướng dẫn hồ sơ, cột 3.1/3.2/3.3 = hồ sơ tạm ứng / thanh toán tạm ứng / thanh toán); **bảng kê** = bảng kê chứng từ gửi phòng Tài chính Kế toán (xlsx, sheet và ô, ví dụ `TT CTP!C8`). Số điều của quy chế do tự động đánh số nên không có trong văn bản: quy chế được trích theo chương và tiêu đề mục.

## Bảng từng bước

| Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn |
|---|---|---|---|---|
| B3 | Giấy đề nghị tạm ứng (Mẫu 03 - TU) | có | giấy đề nghị tạm ứng (tr.1) | bảng kê, sheet 'Hội nghị hội thảo'!-; quy trình, PL01 mục V (hội thảo) cột 3.1 |
| B3 | Tờ trình dự trù kinh phí được phê duyệt | có | tờ trình có dự trù kinh phí (tr.2) | bảng kê, sheet 'Hội nghị hội thảo'!-; quy trình, PL01 mục V cột 3.1 |
| B3 | Ý kiến phòng Tài chính - Kế toán | có | phiếu ý kiến phòng tài chính - kế toán (tr.3) | bảng kê, sheet 'Hội nghị hội thảo'!-; quy trình, PL01 mục V cột 3.1 |
| B3 | Báo giá và chứng từ liên quan đến dự trù | có | báo giá (tr.4) | bảng kê, sheet 'Hội nghị hội thảo'!-; quy trình, PL01 mục V cột 3.1 |
| B3 | Quyết định tổ chức/cử đi đào tạo | có | quyết định tổ chức hội thảo (tr.5) | bảng kê, sheet 'Hội nghị hội thảo'!-; quy trình, PL01 mục V cột 3.1 |
| B5a | số tiền khớp giữa các chứng từ (đề nghị, danh sách, hóa đơn, quyết định) | OK | mọi con số khớp | quy trình, mục 5.1c |
| B5a | số bằng chữ khớp số bằng số | OK | các chứng từ có số bằng chữ đều khớp | quy trình, mục 5.1c |
| B5d | thông tin người nhận tiền đủ, thống nhất giữa các chứng từ | OK | họ tên, số tài khoản và ngân hàng khớp | quy trình, mục 5.2c |
| B5e | hóa đơn lập đúng tên, mã số thuế, địa chỉ đơn vị mua | không áp dụng | bộ tạm ứng chưa có hóa đơn | quy trình, mục 5.2b |
| B5f | khoản mua từ 5 triệu đồng không dùng tiền mặt | OK | thanh toán chuyển khoản | quy trình, mục 5.1d |
| B5g | chữ ký và dấu ở các vai trò cần có (có hay không, không xác thực) | OK | có đủ chữ ký ở các vai trò | quy trình, mục 2.2.1 và biểu mẫu tương ứng |
| B5i | thời điểm và niên độ | OK | chứng từ lập trong năm 2026, đúng thời điểm giao dịch | quy trình, mục 5.1e |
| B5j | tạm ứng trước đã thanh toán | sai | ghi tạm ứng kỳ trước 20.000.000 đ chưa thanh toán | quy trình, mục 5.1f |
| B5k | mẫu biểu đúng loại, có số hiệu | OK | biểu mẫu có số hiệu | quy trình, mục 'Biểu mẫu' |
| B5h | định mức riêng của loại hồ sơ | chưa kiểm | phiên bản đầu chỉ kiểm định mức chi tiết của công tác phí (Q4) | spec, 'Giới hạn đã biết' Q4 |

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn | Việc cần làm và người cấp hoặc ký |
|---|---|---|---|---|---|---|
| F1 | giấy đề nghị tạm ứng (tr.1) | Đề nghị tạm ứng tiếp 15.000.000 đ trong khi khoản tạm ứng kỳ trước 20.000.000 đ (02/09/2026) chưa thanh toán và hoạt động này không diễn ra đồng thời hoặc nối tiếp với hoạt động đã tạm ứng (đề bài không nêu). | chặn | sửa được | quy trình, mục 5.1f | Người đề nghị thanh toán hết khoản tạm ứng trước (giấy thanh toán tạm ứng Mẫu 04-TTTU) rồi nộp lại đề nghị tạm ứng; kế toán thanh toán xác nhận. |
| F2 | báo giá (tr.4) | Báo giá của nhà cung cấp có chữ ký nhưng không có dấu đỏ của nhà cung cấp. | chặn | sửa được | bảng mô tả của khách hàng (xlsx 'AI kế toán thanh toán'), sheet 'Gửi SAPP' ô C18 (báo giá có dấu đỏ/chữ ký của nhà cung cấp); quy trình, PL01 mục V cột 3.1 (báo giá) | Nhà cung cấp đóng dấu báo giá. |
| F3 | phiếu ý kiến phòng tài chính - kế toán (tr.3) | Dòng 'Ngân sách còn lại' của phiếu ý kiến không đọc được (không kiểm tra nào của B5 dùng trường này). | cảnh báo | - | quy trình, PL01 mục V cột 3.1 (ý kiến phòng TCKT) | Người rà soát xem bản gốc; người ký là trưởng phòng TCKT. |

## Phần không kiểm tra được

- phiếu ý kiến phòng tài chính - kế toán (tr.3): dòng 'Ngân sách còn lại của mã trên' bị mực đè (trường không bắt buộc); ngoài phạm vi: kiểm tra ngân sách còn lại.

## Ghi chú cho chuyên gia

- Bảng kê liệt kê hồ sơ thanh toán; bộ này là hồ sơ tạm ứng nên B3 đối chiếu quy trình PL01 mục V cột 3.1. Trợ lý nên nêu rõ điều này.

