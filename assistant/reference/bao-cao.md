# Hình dạng báo cáo tra soát

Báo cáo luôn có đúng năm phần sau, theo thứ tự, để người nhận kiểm lại từng bước.

1. **Đầu báo cáo**: loại bộ hồ sơ và lý do (B2); phiên bản quy chế và quy trình đã áp dụng (xem `quy-dinh.md`); danh sách chứng từ đã nhận kèm số trang (B1); yêu cầu ngoài phạm vi đã từ chối (nếu có).
2. **Bảng từng bước**, mỗi dòng một mục đã kiểm: `Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn`. Kết quả là một trong `OK`, `thiếu`, `sai`, `không đọc được`; `chưa kiểm` khi loại bộ chưa xác định (không tính là OK). Bằng chứng: chứng từ, trang, trường, giá trị đọc (dữ liệu cá nhân che bớt). Mọi mục ở B3 và B5 đều có dòng, kể cả OK; dòng chứng từ không áp dụng ghi `không áp dụng` kèm lý do.
3. **Danh sách phát hiện**: `Mã | Chứng từ, trang | Nội dung | Mức | Loại | Nguồn | Việc cần làm và người cấp hoặc ký`. Mức: `chặn` hoặc `cảnh báo`. Loại: `sửa được` hoặc `vi phạm`. Phát hiện không có nguồn thì không đưa ra.
4. **Không kiểm tra được**: các mục `không đọc được`, mục cần dữ liệu ngoài bộ hồ sơ (ngân sách còn lại, ủy nhiệm chi, tỷ giá, ngày nghỉ lễ, thật giả chữ ký), mục chưa có căn cứ (Q1, Q2, Q4, Q5 khi liên quan).
5. **Kết luận**: một mã `DU_DIEU_KIEN` | `CAN_BO_SUNG` | `KHONG_HOP_LE`; quy tắc B7 đã quyết định và các mã phát hiện làm căn cứ; câu "Quyết định duyệt, từ chối, chi tiền thuộc về kế toán thanh toán, kế toán trưởng, Hiệu trưởng theo thẩm quyền; báo cáo này chỉ là tra soát."

## Ví dụ làm mẫu (hư cấu hoàn toàn, số tiền tự đặt)

Bộ: một giảng viên đi công tác trong nước 3 ngày 2 đêm, chín chứng từ trên 11 trang: đề nghị thanh toán tr.1; thư mời tr.2; quyết định cử đi tr.3; tờ trình có dự trù tr.4-5; phiếu ý kiến P.TCKT tr.6; giấy đi đường tr.7 (xoay ngang); hóa đơn tiền phòng tr.8; hóa đơn vé máy bay khứ hồi tr.9; thẻ lên máy bay tr.10-11.

- B2: có quyết định cử đi, giấy đi đường, vé: loại công tác phí.
- B3: đủ, mọi dòng có hoặc không áp dụng (vé tham quan: không áp dụng).
- B4: đề nghị 4.500.000 đ, bằng chữ "bốn triệu năm trăm nghìn đồng", chuyển khoản; hóa đơn phòng 2 đêm 1.100.000 đ, đơn vị mua ghi tên một cá nhân; hóa đơn vé 2.400.000 đ; giấy đi đường 3 ngày, phụ cấp 900.000 đ, ngày ký của trưởng đơn vị `KHÔNG ĐỌC ĐƯỢC`; dự trù 5.000.000 đ.
- B5: tổng 1.100.000 + 2.400.000 + 900.000 = 4.400.000 so với đề nghị 4.500.000: sai, lệch 100.000 đ. Không vượt dự trù. Hóa đơn phòng ghi sai đơn vị mua: sai. Phòng 550.000 đ mỗi đêm không vượt 600.000 đ phòng đơn; phụ cấp 3 ngày x 300.000 đ: OK. Hạn nộp 6 ngày làm việc: OK. Ngày ký trưởng đơn vị: không đọc được, không bắt buộc.
- B6: `F1` chặn, sửa được (số tiền lệch, quy trình 5.1c); `F2` chặn, sửa được (hóa đơn phòng sai đơn vị mua, quy trình 5.2b); `F3` cảnh báo (ngày ký không đọc được, trường không bắt buộc).
- B7: không có chặn loại `vi phạm`, có `F1`, `F2`: `CAN_BO_SUNG` theo quy tắc (2).

| Bước | Mục kiểm | Kết quả | Bằng chứng | Nguồn |
|---|---|---|---|---|
| B3 | đủ chứng từ loại công tác phí | OK | 9 chứng từ | bảng kê TT CTP |
| B5a | đề nghị bằng tổng chứng từ | sai | 4.500.000 so với 4.400.000; đề nghị tr.1, hóa đơn tr.8 và tr.9 | quy trình 5.1c |
| B5a | không vượt dự trù | OK | 4.500.000 so với 5.000.000 | quy trình 5.1b |
| B5c | hạn nộp 15 ngày làm việc | OK | 6 ngày làm việc | quy chế Chương VI, Điều 22 |
| B5e | đơn vị mua trên hóa đơn phòng | sai | tr.8, tên cá nhân | quy trình 5.2b |
| B5g | ngày ký trưởng đơn vị (không bắt buộc) | không đọc được | giấy đi đường tr.7 | quy trình 5.2 |
| B5h | định mức phòng và phụ cấp | OK | 550.000 mỗi đêm; 3 ngày | quy chế Chương VI, Điều 22 |

Phát hiện: `F1` (chặn, sửa được): sửa số tiền hoặc bổ sung chứng từ còn thiếu, người đề nghị. `F2` (chặn, sửa được): xin hóa đơn lập lại đúng đơn vị mua, nhà cung cấp. `F3` (cảnh báo): xem bản gốc, người rà soát. Không kiểm tra được: ngày ký ở `F3`. Kết luận: `CAN_BO_SUNG`, quy tắc (2), căn cứ `F1`, `F2`; quyết định duyệt, từ chối hay chi thuộc về kế toán thanh toán, kế toán trưởng, Hiệu trưởng.
