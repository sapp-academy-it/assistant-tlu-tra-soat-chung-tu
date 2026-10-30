# Key mh-002

Loại bộ hồ sơ: mua dịch vụ in ấn (dòng 'Mua hàng hóa dịch vụ' của bảng kê).
Phân loại: có lỗi (thanh toán tiền mặt từ 5 triệu đồng).
Chất lượng quét: bình thường.
Case bẫy: không.
Phiên bản áp dụng: quy chế và quy trình trong `inputs/` (đúng bản đã nhận, ghi trong `inputs/README.md`).

**Kết luận mong đợi: `KHONG_HOP_LE`** (quy tắc B7 (1)).

Nguồn trích dẫn gọi tài liệu theo vai trò, như `inputs/README.md`: **quy chế** = quy chế mua sắm và chi tiêu nội bộ (docx); **quy trình** = quy trình tạm ứng, thanh toán, quyết toán của phòng Tài chính Kế toán (docx; `PL01` = Phụ lục 01 hướng dẫn hồ sơ, cột 3.1/3.2/3.3 = hồ sơ tạm ứng / thanh toán tạm ứng / thanh toán); **bảng kê** = bảng kê chứng từ gửi phòng Tài chính Kế toán (xlsx, sheet và ô, ví dụ `TT CTP!C8`). Số điều của quy chế do tự động đánh số nên không có trong văn bản: quy chế được trích theo chương và tiêu đề mục.

## Bảng từng bước

| Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn |
|---|---|---|---|---|
| B3 | Giấy đề nghị thanh toán | có | giấy đề nghị thanh toán (tr.1) | bảng kê, sheet 'Mua hàng hóa dịch vụ'!C6 |
| B3 | Giấy đề xuất/tờ trình/dự trù | có | tờ trình có dự trù kinh phí (tr.2) | bảng kê, sheet 'Mua hàng hóa dịch vụ'!C9; quy trình, PL01 mục I.1 cột 3.3 (chi không thường xuyên) |
| B3 | Phiếu ý kiến của phòng Tài chính - Kế toán | có | phiếu ý kiến phòng tài chính - kế toán (tr.3) | bảng kê, sheet 'Mua hàng hóa dịch vụ'!C10; quy trình, PL01 mục I.1 cột 3.3 |
| B3 | Hóa đơn tài chính | có | hóa đơn in ấn (tr.6) | bảng kê, sheet 'Mua hàng hóa dịch vụ'!C11; quy trình, PL01 mục I.1 cột 3.3 |
| B3 | BB nghiệm thu | có | biên bản nghiệm thu dịch vụ (tr.5) | bảng kê, sheet 'Mua hàng hóa dịch vụ'!C12; quy trình, PL01 mục I.1 cột 3.3 (biên bản nghiệm thu dịch vụ hoàn thành) |
| B3 | Hợp đồng | không áp dụng | tùy trường hợp (Q1): bộ không có và đề bài không đòi hỏi | bảng kê, sheet 'Mua hàng hóa dịch vụ'!C16 |
| B3 | Báo giá | có | báo giá (tr.4) | bảng kê, sheet 'Mua hàng hóa dịch vụ'!C17; quy trình, PL01 mục I.1 cột 3.3 |
| B3 | Bảng kiểm soát trình ký hợp đồng | không áp dụng | tùy trường hợp (Q1): bộ không có và đề bài không đòi hỏi | bảng kê, sheet 'Mua hàng hóa dịch vụ'!C20 |
| B5a | số tiền khớp giữa các chứng từ (đề nghị, danh sách, hóa đơn, quyết định) | OK | mọi con số khớp | quy trình, mục 5.1c |
| B5a | số bằng chữ khớp số bằng số | OK | các chứng từ có số bằng chữ đều khớp | quy trình, mục 5.1c |
| B5d | thông tin người nhận tiền đủ, thống nhất giữa các chứng từ | OK | họ tên, số tài khoản và ngân hàng khớp | quy trình, mục 5.2c |
| B5e | hóa đơn lập đúng tên, mã số thuế, địa chỉ đơn vị mua | OK | hóa đơn in ấn (tr.6) | quy trình, mục 5.2b |
| B5f | khoản mua từ 5 triệu đồng không dùng tiền mặt | sai | hóa đơn và đề nghị: tiền mặt | quy trình, mục 5.1d |
| B5g | chữ ký và dấu ở các vai trò cần có (có hay không, không xác thực) | thiếu | biên bản nghiệm thu thiếu chữ ký và dấu nhà cung cấp | quy trình, mục 2.2.1 và biểu mẫu tương ứng |
| B5i | thời điểm và niên độ | OK | chứng từ lập trong năm 2026, đúng thời điểm giao dịch | quy trình, mục 5.1e |
| B5j | tạm ứng trước đã thanh toán | không áp dụng | không phải bộ tạm ứng | quy trình, mục 5.1f |
| B5k | mẫu biểu đúng loại, có số hiệu | OK | biểu mẫu có số hiệu | quy trình, mục 'Biểu mẫu' |
| B5h | định mức riêng của loại hồ sơ | chưa kiểm | phiên bản đầu chỉ kiểm định mức chi tiết của công tác phí (Q4) | spec, 'Giới hạn đã biết' Q4 |

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn | Việc cần làm và người cấp hoặc ký |
|---|---|---|---|---|---|---|
| F1 | hóa đơn in ấn (tr.6); giấy đề nghị thanh toán (tr.1) | Hóa đơn 7.150.000 đ (đã gồm thuế, từ 5 triệu đồng) và đề nghị đều chọn thanh toán tiền mặt. | chặn | vi phạm | quy trình, mục 5.1d | Đơn vị phải chuyển sang chuyển khoản (có chứng từ chuyển tiền qua ngân hàng); phần đã trả tiền mặt cần phê duyệt riêng của cấp có thẩm quyền. |
| F2 | biên bản nghiệm thu dịch vụ (tr.5) | Biên bản nghiệm thu dịch vụ không có chữ ký và dấu của nhà cung cấp. | chặn | sửa được | bảng kê, sheet 'Mua hàng hóa dịch vụ'!C12; quy trình, mục 5.1g | Nhà cung cấp ký, đóng dấu biên bản nghiệm thu. |

## Phần không kiểm tra được

- Không có trường nào không đọc được. Ngoài phạm vi (cần dữ liệu ngoài bộ hồ sơ): đối chiếu ủy nhiệm chi, hạch toán, ngân sách còn lại, thật giả của chữ ký, con dấu và hóa đơn điện tử.

