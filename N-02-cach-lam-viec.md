# N-02 · Cách làm việc

Cập nhật ngày 05/10/2026. **Mỗi người tự làm và chịu trách nhiệm phần mình; không có bước bắt buộc Hưng duyệt hoặc merge.**

## 1. Làm và đưa lên bản chung

1. Lấy bản mới nhất, đọc 01–04, hướng dẫn N và nội dung bài giảng liên quan. Hiểu các phần trước đủ để dùng đúng đầu vào cho phần mình.
2. Viết phần được giao; giữ nguồn bảng tính, công thức và hình có thể chỉnh sửa.
3. Tự kiểm và dùng **ít nhất một lượt Agent ad-review phần đã làm**. Xử lý góp ý có căn cứ, rồi kiểm lại phần đã sửa.
4. Commit và đưa lên bản chung bằng PR hoặc commit trực tiếp theo quyền truy cập. **PR là cách khuyến khích, không bắt buộc.** Báo trên nhóm phần đã cập nhật và ảnh hưởng đến người khác.

PR hoặc commit ghi ngắn nội dung thay đổi. Phần chưa hoàn thiện ghi rõ là nháp. Lịch nội bộ, thời điểm bàn giao và việc tiếp theo trao đổi trên nhóm, không lập bảng deadline hay danh sách việc trong repo.

## 2. Giữ đúng dữ liệu gốc và sửa hồi quy

- Đối chiếu đủ [01](01-mo-ta-de-tai.md), [02](02-du-toan-kinh-phi.md), [03](03-ton-chi-du-an.md), [04](04-ton-chi-du-an-day-du.md). Tên vai trò, chức năng, thiết bị, nhân sự, mốc và ngân sách phải thống nhất giữa các chương.
- Người và Agent đều phải giữ đúng dữ liệu nguồn, phân biệt yêu cầu đã có với giả định/gợi ý. Không bỏ yêu cầu hoặc thêm cam kết chỉ để bài dễ làm; không gắn lời của AI thành yêu cầu của giảng viên.
- Khi phát hiện sai hoặc thiếu, có thể sửa ngược tài liệu trước và thông báo trên nhóm: sai ở đâu, căn cứ sửa và phần nào bị ảnh hưởng. Thay đổi quyết định chung về phạm vi, ngân sách hoặc ràng buộc cần nhóm thống nhất; sửa lỗi đối chiếu có nguồn không cần một cổng duyệt riêng của Hưng.
- Nếu các nguồn gốc mâu thuẫn mà chưa có căn cứ phân xử, nêu rõ vấn đề và giả định đang dùng để nhóm giải quyết; chưa kết luận phần phụ thuộc đã hoàn chỉnh.
- Giữ mã WBS ổn định. Nếu đổi mã/cấu trúc, chỉ rõ ánh xạ cũ–mới và cập nhật các bảng tiến độ, nhân lực, chi phí liên quan.

## 3. Lượt Agent ad-review tối thiểu

Cung cấp cho Agent **bản vừa làm, 01–04, N-01–N-04, các phần trước có liên quan và nội dung học của chương**; PMBOK 6 dùng thêm khi cần. Nếu tài liệu dài, cho Agent truy cập phần nguồn cần thiết và yêu cầu chỉ rõ giới hạn đã đọc.

Yêu cầu Agent kiểm: đúng yêu cầu môn, đúng dữ liệu gốc, logic, độ phủ phạm vi, phép tính, quan hệ với phần khác và chi tiết có căn cứ. Góp ý cần nêu vị trí, nguồn đối chiếu, ảnh hưởng và hướng xử lý; không yêu cầu đủ một số lỗi định trước.

Người làm xem xét và sửa các góp ý hợp lý; có thể bác góp ý sai bằng nguồn. Ghi ngắn bản/phần đã review và kết quả xử lý trong PR, thông tin commit hoặc thông báo nhóm. Một chữ PASS không thay trách nhiệm của người làm; không cần mỗi lần lại ad-review toàn bộ phần đã có.

AI dùng để phản biện bản nháp theo xác nhận của giảng viên được ghi ở [N-01](N-01-khung-btl.md), không viết thay bài nộp.

## 4. Kiểm trước khi gửi/nộp

- Nội dung đúng nguồn, không mâu thuẫn các phần liên quan; giả định và điểm chưa chốt được ghi rõ.
- Bảng có đơn vị, cách tính và số tổng đúng; hình có chú thích và nguồn. Không dùng ảnh chụp thay file nguồn của bảng cần tính lại.
- Markdown UTF-8, tiêu đề rõ, thuật ngữ được giải thích; link dùng được. Khi đổi tên/di chuyển file, cập nhật các tham chiếu.
- Bản chung mới nhất được giữ; không ghi đè công việc đang làm của người khác hoặc xóa lịch sử chung.
- Khi ghép nộp: đủ chín chương, đóng góp rõ, PDF và slide thống nhất; bảng, hình, công thức và mục lục đọc được. Người ghép và người gửi do nhóm thống nhất, không mặc định Hưng.

Các file `N-` và ghi chú review là tài liệu làm việc, không tự ghép vào quyển nộp. Chưa kiểm bản xuất hoặc hệ thống thực tế thì ghi đúng giới hạn đã kiểm.
