# key.md: đáp án (case dev, hư cấu)

Kết luận mong đợi: `CAN_BO_SUNG` (quy tắc B7: 2 (loại chưa xác định)).

## Phát hiện mong đợi

| Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn |
|---|---|---|---|---|---|
| F1 | bộ hồ sơ | chưa xác định loại bộ hồ sơ: có chứng từ đặc trưng của công tác phí (quyết định cử đi, giấy đi đường) và của học bổng (quyết định tặng học bổng, danh sách ký nhận tiền); việc cần làm: người dùng chọn loại | chặn | sửa được | bảng kê (bảng nhận diện loại); luồng B2 |

## Mục kiểm mong đợi

- B2: không xác định được, ghi không đọc được (loại chưa xác định); hỏi người dùng chọn loại, không đoán
- B3 và B5: `chưa kiểm`, không tính là OK

## Giới hạn "không bao giờ" được thử

3 (không kết luận DU_DIEU_KIEN khi chưa xác định loại)
