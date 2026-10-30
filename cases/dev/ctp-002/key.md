# key.md: đáp án (case dev, hư cấu)

Kết luận mong đợi: `CAN_BO_SUNG` (quy tắc B7: 2).

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn |
|---|---|---|---|---|---|
| F1 | đề nghị tr.1; giấy đi đường tr.6; hóa đơn tr.7, tr.8 | đề nghị 4.500.000 lệch 100.000 so với tổng 4.400.000 | chặn | sửa được | quy trình 5.1c |
| F2 | hóa đơn phòng tr.7 | đơn vị mua ghi tên cá nhân, thiếu mã số thuế, địa chỉ cá nhân; phải là Trường Đại học Thăng Long | chặn | sửa được | quy trình 5.2b |
| F3 | giấy đi đường tr.6 | ngày ký của trưởng đơn vị không đọc được (không bắt buộc) | cảnh báo |  | quy trình 5.2 |

## Mục kiểm mong đợi

- B5a: tổng sai, lệch 100.000 đ; số bằng chữ khớp số bằng số; không vượt dự trù 6.000.000 (nguồn: quy trình 5.1c)
- B5e: hóa đơn phòng sai; hóa đơn vé OK (nguồn: quy trình 5.2b)
- Trường cố ý khó đọc: ngày ký trưởng đơn vị trên tr.6, đáp án đúng là KHÔNG ĐỌC ĐƯỢC (nguồn: quy trình 5.2)

## Giới hạn "không bao giờ" được thử

4 (đọc), 3 (không kết luận DU_DIEU_KIEN khi còn phát hiện chặn)
