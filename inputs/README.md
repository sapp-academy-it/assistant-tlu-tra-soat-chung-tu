# inputs/

The customer's documents (rules, checklists, process descriptions, a request letter), exactly as received: one file per
document, the name it came with. They are never edited here; a document that changes comes in again as a new file.

The test-set session (stage 4) is given this folder alone, and every expected result it writes names its source here.
The coordinating session never reads these files.

## This assistant's documents (not in git)

The customer's documents stay on the owner's machine and are never pushed (owner 2026-10-29): `.gitignore` ignores
everything in this folder except this file. A session that needs them reads them from the owner's local clone; the
documents below are identified by role and sha256, never by their original file names.

| Role | sha256 |
|---|---|
| Internal purchasing and spending regulation (quy chế mua sắm và chi tiêu nội bộ), docx | `7de1c815a5f36c5a1a414531115422ce5f6f96be6f432474cbb0bc77fd84fd05` |
| Payment process of the finance-accounting office (quy trình tạm ứng, thanh toán, quyết toán), docx | `10be97ea95bbd2e7d52ba05a244f22649c1662f38b961dbbd25458d626b847e9` |
| Checklist of 12 voucher-set templates (bảng kê chứng từ gửi phòng tài chính kế toán), xlsx | `ff0d1d6db1a06f783878f446b18f4d0aeca7d14c9903d8e0ad99f85bf6ec8f34` |
| "AI kế toán thanh toán" sheet: the customer's description of the process, its problems and the expected AI help, xlsx | `47ea625f8735ca8d1e02fdafc9c61cee35921865cbeb40019fb6b4cf9fdb7178` |
| One real sample voucher set for a business trip (scanned pdf, 16 pages; holds personal data), pdf | `9f41802ac6e559c029e4bb058e51f4d687fadd8f7f54bc167c1ce67a99e5d28c` |
