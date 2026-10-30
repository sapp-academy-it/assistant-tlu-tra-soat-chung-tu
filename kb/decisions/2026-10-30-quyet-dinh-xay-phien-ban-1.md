---
description: "Hai chỗ bản 1 của skill khác chữ của spec, để chuyên gia xem lại: 10 sheet so với 12 loại, và tách cốt lõi / tùy trường hợp cho Q1"
status: live
---

# Hai quyết định khi xây phiên bản 1

Spec đã duyệt không đổi. Hai chỗ khi xây phải chọn khác chữ của spec, cộng một quy tắc tạm cho quy trình 5.2c; chuyên gia nghiệp vụ xem lại và ký hoặc sửa.

## 1. Mười sheet, không phải mười hai loại

- Spec (nhiệm vụ 1) nói 12 loại của bảng kê; file bảng kê có 10 sheet.
- Chọn: skill nhận 10 loại theo 10 sheet (`assistant/reference/bang-ke.md`). Bộ thuộc nghiệp vụ của Phụ lục 01 của quy trình mà không có sheet (quảng cáo mạng xã hội, tổ chức sự kiện, học phần thực hành, thuê khoán) được ghi là "loại chưa có sheet": B3 là không kiểm tra được, kết luận tối đa `CAN_BO_SUNG`, không bao giờ `DU_DIEU_KIEN` (cùng nguyên tắc với loại chưa xác định ở spec B2 và quy tắc 3 của B7).
- Loại bị loại: tự đặt thêm hai loại cho đủ 12 (nguồn không nêu chúng, sẽ là bịa); gộp nghiệp vụ của Phụ lục 01 vào "mua hàng hóa" (sai danh sách chứng từ).
- Cần chuyên gia: hai loại còn lại là loại nào, và danh sách chứng từ của chúng.

## 2. Tách cốt lõi và tùy trường hợp cho Q1

- Spec (Giới hạn đã biết, Q1) viết: đến khi chuyên gia xác nhận thì "đủ chứng từ" theo key của chuyên gia. Chưa có key, skill vẫn phải kiểm đủ chứng từ.
- Chọn (quy tắc tạm ở `bang-ke.md`): mỗi dòng bảng kê là `Cốt lõi` (thiếu thì phát hiện chặn, sửa được) hoặc `Tùy trường hợp` (vắng thì `không áp dụng`, hoặc cảnh báo khi không rõ, không chặn). Phân loại dựa vào tên sheet và Phụ lục 01. Danh sách `Cốt lõi` của mỗi loại là đầy đủ, không cộng chứng từ từ loại khác.
- Loại bị loại: coi mọi dòng `x` là bắt buộc (hồ sơ mua hàng bị đòi hơn 30 chứng từ); coi mọi dòng là tùy trường hợp (không phát hiện được thiếu).
- Cần chuyên gia: ký phân loại này, hoặc cho phân loại khác; khi đó `bang-ke.md` đổi theo và key của test set theo nó.

## 3. Quy tắc tạm cho quy trình 5.2c (thông tin người nhận tiền)

- Quy trình 5.2c đòi thông tin người nhận (mã cán bộ hoặc Mẫu 07-TCKT, họ tên, mã số thuế cá nhân, CCCD, điện thoại) nhưng không nói mỗi người trên một danh sách nhiều người nhận phải có đủ ngay trên chứng từ hay nộp riêng. Đây thuộc B5(d) và 5.2c, không thuộc Q5 (Q5 là trường bắt buộc của biểu mẫu).
- Chọn (B5(d) của `SKILL.md`): giấy đề nghị thanh toán chuyển cho một người nhận mà thiếu thông tin 5.2c: phát hiện chặn, sửa được. Danh sách nhiều người nhận (Mẫu 08, 09, danh sách ký nhận) thiếu thông tin của từng người: chỉ cảnh báo, nguồn quy trình 5.2c, không chặn. Bốn key (sach-001, td-001, hb-001, qt-001) và nckh-001 theo quy tắc này.
- Loại bị loại: chặn cho mọi chỗ thiếu (mỗi danh sách Mẫu 09 thật chỉ có tên và tài khoản, mọi hồ sơ sẽ bị chặn); bỏ qua 5.2c hoàn toàn (mất kiểm tra cho người nhận đơn lẻ).
- Cần chuyên gia: xác nhận mức độ này, hoặc cho mức khác.
