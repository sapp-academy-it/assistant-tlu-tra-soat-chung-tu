# Hiện trạng — repo này

Chỉ ghi trạng thái hiện hành, viết đè khi repo đổi. Không lịch sử, không cách làm: chi tiết ở `kb/specs/` và `kb/decisions/`.

## Đang chạy

- Repo công khai của một trợ lý AI tra soát chứng từ thanh toán; tài liệu của khách hàng chỉ nằm trên máy của chủ sở hữu, không vào git (`.gitignore`, `inputs/README.md`).
- Spec của trợ lý đã được chủ sở hữu duyệt, ngưỡng chấm điểm đã đóng băng: `kb/specs/2026-10-29-tra-soat-chung-tu.md`.
- Năm cổng quy trình chạy trên runner GitHub-hosted: commit-discipline, pr-sensitive, pr-title, pr-body, dead-branches.
- Workflow đọc biến `CI_GATE_RUNNER`, rồi `CI_RUNNER`, dự phòng `ubuntu-latest`.
- Mã cổng ở `.vibemaestro/gates/`.
- `assistant/` có skill `tra-soat-chung-tu` bản 1 (tám bước B1 đến B8, 11 giới hạn, `reference/` ghi quy chế, quy trình, bảng kê) và `plugin.json`.
- `cases/dev/` có 21 case hư cấu thử trên skill, kết quả ở `kb/decisions/2026-10-30-case-dev-phien-ban-1.md`.

## Chưa có / đang tắt

- Chưa có tag phiên bản, chưa có `cases/test-v1`, chưa có điểm chấm.
- Năm câu hỏi mở cho chuyên gia nghiệp vụ (Q1 đến Q5) còn mở, ghi trong spec; hai chỗ bản xây khác chữ spec ghi ở `kb/decisions/2026-10-30-quyet-dinh-xay-phien-ban-1.md`.
