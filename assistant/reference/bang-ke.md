# Bảng kê chứng từ gửi P.TCKT, theo loại hồ sơ

Nguồn: bảng kê chứng từ gửi P.TCKT, 12 loại hồ sơ (xlsx, sha256 bắt đầu `ff0d1d6d`) (file Checklist_Mau_12_BKCT_TCKT; mỗi sheet một loại); trong file mọi dòng đều đánh `x`, cột Có và Nợ để trống, nên chưa nói chứng từ nào bắt buộc (câu hỏi mở Q1). Mã nguồn dùng trong báo cáo: "bảng kê <tên sheet>, dòng <tên chứng từ>". File có 10 sheet; spec nói 12 loại (xem mục "Loại chưa có sheet" ở cuối).

## Quy tắc tạm thời cho Q1 (đến khi chuyên gia ký key)

- `Cốt lõi`: chứng từ đặc trưng của loại, chắc chắn có trong mọi bộ của loại đó (theo tên sheet và Phụ lục 01). Thiếu = thiếu chứng từ bắt buộc: phát hiện chặn, loại sửa được, kết luận ít nhất `CAN_BO_SUNG`.
- `Tùy trường hợp`: dòng gộp nhiều lựa chọn hoặc chỉ cần khi có tình huống (hợp đồng từ 20 triệu đồng, tạm ứng, hàng nhập khẩu...). Vắng mặt: ghi `không áp dụng` nếu bộ hồ sơ cho thấy tình huống không xảy ra; nếu không rõ, ghi cảnh báo "chưa xác định có cần không (Q1)", không chặn.
- Mọi dòng ghi một trong: có, thiếu, không áp dụng.

## Nhận diện loại (tên sheet; chứng từ đặc trưng)

| Loại | Tên sheet | Nhận diện bằng |
|---|---|---|
| Công tác phí | TT CTP | quyết định cử đi công tác, giấy đi đường, vé hoặc hóa đơn đi lại, lưu trú |
| Hội nghị, hội thảo, tọa đàm | Hội nghị hội thảo | quyết định tổ chức, quyết toán chương trình, danh sách ký nhận tiền |
| Thuê xe, đưa sinh viên đi thực tập, thực tế | SV đi thực tập | quyết định cho sinh viên đi thực tập kèm danh sách, hợp đồng thuê xe, biên bản thanh lý |
| Tiền dạy, chấm thi | TTdạy, chấm thi | bảng kê chi tiết tiền dạy hoặc chấm thi, quyết định hội đồng, danh sách chuyển khoản mẫu 09 |
| Học bổng | Hoc bổng | quyết định tặng học bổng, danh sách ký nhận tiền |
| Đề tài NCKH | Đề tài NCKH | quyết định phê duyệt giao đề tài, biên bản nghiệm thu, giấy chứng nhận nộp sản phẩm |
| Sách, giáo trình | Đề tài sách, GT | quyết định giao nhiệm vụ biên soạn, hợp đồng biên soạn |
| Mua hàng hóa, dịch vụ | Mua hàng hóa dịch vụ | hợp đồng, báo giá, biên bản nghiệm thu, phiếu nhập xuất kho, hóa đơn |
| Quyết toán chương trình | QT CT | bảng quyết toán chương trình, danh sách sinh viên nhận tiền |
| Tuyển dụng | Tuyển dụng | quyết định tuyển dụng, bảng thanh toán tiền chấm thi và hướng dẫn |

Hai loại ngang nhau hoặc không có chứng từ đặc trưng: hỏi người dùng chọn loại (B2).

## Danh sách theo loại

Danh sách `Cốt lõi` của từng loại dưới đây là đầy đủ: không cộng thêm chứng từ nào từ loại khác hay từ danh sách chung. Loại nào không ghi giấy đề nghị thanh toán, tờ trình, phiếu ý kiến P.TCKT hay hóa đơn thì không đòi các chứng từ đó (ví dụ tiền dạy, đề tài, sách, tuyển dụng).

### Công tác phí (TT CTP)
Cốt lõi: đề nghị thanh toán; quyết định cử đi công tác; giấy đề xuất, tờ trình, dự trù; phiếu ý kiến P.TCKT; giấy đi đường; hóa đơn tài chính hoặc chứng từ hợp pháp cho đi lại và lưu trú (lưu trú theo mức khoán thì không cần hóa đơn).
Tùy trường hợp: giấy mời hoặc công văn của đơn vị tổ chức (khi có đơn vị mời); vé tham quan (khi có tham quan); cuống vé máy bay (khi đi máy bay, kèm thẻ lên tàu bay hoặc vé điện tử).

### Hội nghị, hội thảo, tọa đàm (Hội nghị hội thảo)
Cốt lõi: đề nghị thanh toán; giấy đề xuất, tờ trình, dự trù; phiếu ý kiến P.TCKT; quyết định tổ chức; hóa đơn tài chính; quyết toán chương trình; danh sách ký nhận tiền (mẫu 06) hoặc danh sách chuyển khoản (mẫu 09, 2 bản) tùy hình thức chi.
Tùy trường hợp: cuống vé máy bay; các chứng từ khác.

### Thực tập, thực tế của sinh viên (SV đi thực tập)
Cốt lõi: đề nghị thanh toán; giấy đề xuất, tờ trình, dự trù; phiếu ý kiến P.TCKT; quyết định cho sinh viên đi thực tập, thực tế kèm danh sách; hóa đơn tài chính.
Tùy trường hợp: hợp đồng (bắt buộc từ 20 triệu đồng trở lên), bảng kiểm soát trình ký hợp đồng, báo giá (01 đến 03 đơn vị), biên bản thanh lý hợp đồng hoặc biên bản nghiệm thu.

### Tiền dạy, chấm thi (TTdạy, chấm thi)
Cốt lõi: danh sách chuyển khoản mẫu 09 (hoặc danh sách ký nhận mẫu 06 nếu tiền mặt); bảng kê chi tiết tiền dạy hoặc tiền chấm thi; bảng kê chi tiết tính tiền; giấy đề xuất, tờ trình, dự trù; phiếu ý kiến P.TCKT.
Tùy trường hợp (theo từng việc): quyết định thành lập Hội đồng KLTN; biên bản nghiệm thu công việc; hợp đồng cộng tác viên; hợp đồng chuyên gia; bảng tính tiền xây dựng ngân hàng câu hỏi; quyết định thành lập hội đồng nghiệm thu và biên bản bàn giao ngân hàng câu hỏi; bảng tính tiền lương nhân sự.

### Học bổng (Hoc bổng)
Cốt lõi: giấy đề nghị thanh toán; danh sách chuyển khoản mẫu 09; giấy đề xuất, tờ trình, dự trù; phiếu ý kiến P.TCKT; quyết định tặng học bổng; danh sách ký nhận tiền (khi chi tiền mặt; khi chuyển khoản thì danh sách chuyển khoản thay thế, ghi không áp dụng).

### Đề tài NCKH (Đề tài NCKH)
Cốt lõi: danh sách chuyển khoản mẫu 09; quyết định phê duyệt và giao đề tài; quyết định hội đồng nghiệm thu; biên bản họp nghiệm thu; đề cương thuyết minh; giấy chứng nhận nộp sản phẩm cho phòng SĐH và QLKH; hợp đồng; biên bản nghiệm thu thanh lý hợp đồng; hóa đơn tài chính hoặc chứng từ liên quan.
Tùy trường hợp: quyết định hội đồng bảo vệ đề cương.

### Sách, giáo trình (Đề tài sách, GT)
Cốt lõi: danh sách chuyển khoản mẫu 09; quyết định phê duyệt và giao nhiệm vụ biên soạn; quyết định hội đồng nghiệm thu; đề cương biên soạn; giấy chứng nhận nộp sản phẩm; hợp đồng biên soạn; biên bản nghiệm thu thanh lý hợp đồng; hóa đơn tài chính hoặc chứng từ liên quan.
Tùy trường hợp: quyết định hội đồng thẩm định đề cương; đề cương thuyết minh.

### Mua hàng hóa, dịch vụ (Mua hàng hóa dịch vụ)
Cốt lõi: giấy đề nghị thanh toán (hoặc đề nghị tạm ứng, thanh toán tạm ứng nếu bộ tạm ứng); giấy đề xuất, tờ trình, dự trù; phiếu ý kiến P.TCKT (khoản chi không thường xuyên); hóa đơn tài chính; biên bản nghiệm thu hoặc biên bản bàn giao và nghiệm thu; báo giá.
Tùy trường hợp: hợp đồng, bản photo hợp đồng và bảng kiểm soát trình ký hợp đồng (từ 20 triệu đồng); biên bản thanh lý hợp đồng; đơn đặt hàng, đơn hàng mua bán; giấy ủy quyền (thanh toán trên 5 triệu qua cá nhân) kèm sao kê hoặc ảnh giao dịch; phiếu nhập kho, phiếu xuất kho (vật tư, thiết bị); phiếu giao hàng, phiếu bảo hành; chứng nhận chất lượng, xuất xứ (hàng nhập khẩu); biên bản bàn giao nội bộ; báo cáo chi phí đồ uống; danh sách lớp; giao dịch chuyển tiền; phiếu giải trình (khi vượt hoặc ngoài dự toán); danh sách nhân sự ký nhận; biên bản giao hàng; bảng kê chi tiết; các chứng từ khác.

### Quyết toán chương trình (QT CT)
Cốt lõi: giấy đề nghị thanh toán; quyết toán chương trình; giấy đề xuất, tờ trình, dự trù; phiếu ý kiến P.TCKT; hóa đơn tài chính.
Tùy trường hợp: hợp đồng; báo giá; biên bản bàn giao và nghiệm thu; danh sách sinh viên nhận tiền (khi có chi cho sinh viên).

### Tuyển dụng (Tuyển dụng)
Cốt lõi: giấy đề nghị thanh toán; danh sách chuyển khoản; bảng thanh toán tiền chấm thi và hướng dẫn; quyết định tuyển dụng.

## Loại chưa có sheet

Phụ lục 01 của quy trình (`quy-dinh.md`) còn nghiệp vụ không có sheet trong bảng kê, ví dụ quảng cáo trên nền tảng mạng xã hội, hoạt động tổ chức sự kiện, học phần thực hành hoặc mô hình thực hành cho sinh viên, tiền nhân công thuê khoán. Nhận diện: bộ có chứng từ đặc trưng của các nghiệp vụ đó (bảng phân bổ chi phí quảng cáo; bảng tổng hợp quyết toán chương trình hoặc sự kiện; định mức nguyên vật liệu, nhân công cho thực hành; hợp đồng giao khoán) và không khớp rõ với 10 loại ở trên. Với loại này không có bảng kê để đối chiếu nên B3 là `không kiểm tra được`, kết luận tối đa `CAN_BO_SUNG`, không bao giờ `DU_DIEU_KIEN`; B4 đến B6 vẫn làm. Hai loại còn lại trong "12 loại" của spec chưa xác định (nguồn không nêu).
