# key.md: đáp án (case dev, hư cấu)

Kết luận mong đợi: `CAN_BO_SUNG` (quy tắc B7: 2).

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn |
|---|---|---|---|---|---|
| F1 | bộ hồ sơ | thiếu quyết định cho sinh viên đi thực tập, thực tế kèm danh sách; người cấp: Hiệu trưởng hoặc đơn vị đào tạo | chặn | sửa được | bảng kê SV đi thực tập, dòng Quyết định cho SV đi thực tập/ thực tế kèm danh sách |
| F2 | hóa đơn tr.5 | mã số thuế đơn vị mua không đúng (ghi 0100000000), phải là mã số thuế của Trường | chặn | sửa được | quy trình 5.2b |

## Mục kiểm mong đợi

- Loại: thuê xe đưa sinh viên đi thực tế (bảng kê SV đi thực tập) (đầu vào: tr.2, tr.4)
- B5a: 28.000.000 khớp ở đề nghị, tờ trình, hợp đồng, hóa đơn (đầu vào: tr.1, tr.2, tr.4, tr.5)
- Hợp đồng từ 20 triệu đồng: có (tr.4); biên bản thanh lý: có (tr.6) (đầu vào: tr.4, tr.6)
