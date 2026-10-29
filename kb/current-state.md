# Hiện trạng — repo này

Chỉ ghi trạng thái hiện hành, viết đè khi repo đổi. Không lịch sử, không cách làm: chi tiết ở `kb/specs/` và `kb/decisions/`.

## Đang chạy

- Repo công khai của một trợ lý AI tra soát chứng từ thanh toán; tài liệu của khách hàng chỉ nằm trên máy chủ sở hữu, không vào git (`.gitignore`, `inputs/README.md`).
- Spec của trợ lý đã được chủ sở hữu duyệt, ngưỡng chấm điểm đã đóng băng: `kb/specs/2026-10-29-tra-soat-chung-tu.md`.
- Năm cổng quy trình chạy trên runner GitHub-hosted: commit-discipline, pr-sensitive, pr-title, pr-body, dead-branches.
- Workflow đọc biến `CI_GATE_RUNNER`, rồi `CI_RUNNER`, dự phòng `ubuntu-latest`.
- Mã cổng ở `.vibemaestro/gates/`.

## Chưa có / đang tắt

- Chưa có `assistant/` (bản dựng), chưa có test case, chưa có tag phiên bản, chưa có điểm chấm.
- Bốn câu hỏi mở cho chuyên gia nghiệp vụ còn mở, ghi trong spec.
