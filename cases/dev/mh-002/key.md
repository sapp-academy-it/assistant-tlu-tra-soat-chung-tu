# key.md: đáp án (case dev, hư cấu)

Kết luận mong đợi: `KHONG_HOP_LE` (quy tắc B7: 1).

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn |
|---|---|---|---|---|---|
| F1 | hóa đơn tr.6, tr.7, tr.8; đề nghị tr.1 | ba hóa đơn cùng nhà cung cấp cùng ngày 14/08/2026 (2.100.000, 1.900.000, 2.000.000), mỗi hóa đơn dưới 5 triệu nhưng tổng 6.000.000 thanh toán tiền mặt | chặn | vi phạm | quy trình 5.1d (mua nhiều lần trong cùng một ngày) |

## Mục kiểm mong đợi

- B5f: gộp theo nhà cung cấp và ngày: tổng 6.000.000, tiền mặt: sai (đầu vào: tr.1, tr.6 đến tr.8)
- B5a: 6.000.000 khớp (đầu vào: tr.1, tr.2, tr.6 đến tr.8)
