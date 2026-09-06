# Quy cách cộng tác và bàn giao — Nhóm 16

**Loại tài liệu:** Điều phối nội bộ, không ghép tự động vào báo cáo nộp.

**Nguồn:** [Khung BTL](04-khung-btl-va-dau-ra.md), yêu cầu GV-01 và các quyết định tại [file 06](06-quyet-dinh-va-phan-cong.md). Nguyên tắc đã được Hưng đồng ý ngày 06/09/2026; phân vai và thời hạn từng việc cần người nhận xác nhận.

## 1. GitHub là nơi cộng tác và quản lý bản chính

- Làm việc trong repository [QLDAPM-16](https://github.com/NguyenHaiHung0510/QLDAPM-16). Ba file gốc 01–03 là nguồn đã được nhóm thống nhất; Hưng quản lý lưu trữ và duyệt.
- Mỗi người viết nội dung bằng Markdown, quản lý phần mình và gửi thay đổi để đọc chéo. Bản được chấp nhận nằm trên nhánh tích hợp `main`; bản nháp chưa duyệt nằm trên nhánh riêng hoặc draft PR.
- Quy trình thông thường: cập nhật từ `main` → tạo nhánh cho một phần việc → sửa đúng phạm vi → commit → push nhánh → mở pull request (PR) → đọc chéo → tác giả sửa → Hưng duyệt và merge.
- Một PR nên chứa một đầu ra hoặc một nhóm thay đổi có cùng mục đích. Không sửa đồng thời file người khác đang viết nếu chưa phối hợp; không lấy bản cũ ghi đè toàn bộ bản mới.
- Hưng là người tích hợp cuối; người đọc chéo kiểm nội dung và người viết chịu trách nhiệm sửa. Không mặc định Hưng phải viết lại mọi phần. Phần phạm vi do Hưng viết vẫn cần người khác đọc chéo.
- Không force-push lên `main`, không xóa lịch sử hoặc nhánh của người khác. Khi đồng thời có thay đổi, xử lý xung đột bằng cách đọc và đối chiếu nội dung; chưa rõ thì hỏi người phụ trách.

Đây là quy ước cộng tác của nhóm, **không phải lời xác nhận branch protection đã được cấu hình**. Việc thiết lập repository ban đầu ngày 06/09/2026 được Hưng giao riêng cho agent commit/push trực tiếp, sau đó T3 review; không lấy ngoại lệ này làm quy trình bàn giao thường xuyên của thành viên.

GitHub hỗ trợ góp ý trên thay đổi và quyết định review (comment/approve/request changes). Tham khảo [hướng dẫn PR review](https://docs.github.com/en/pull-requests/reference/pull-request-reviews); nhóm dùng quy trình tối thiểu, chưa yêu cầu dựng CI phức tạp.

## 2. Cấu trúc file và dữ liệu nguồn

Hiện có file gốc 01–03 và tài liệu điều phối 04–06. Khi bắt đầu viết báo cáo, tạo các thư mục dưới đây theo nhu cầu; chúng **chưa phải đầu ra đã tồn tại**:

```text
bao-cao/       # Markdown các chương: chuong-02-pham-vi.md, ...
du-lieu/       # Bảng nguồn và công thức có thể đối chiếu
hinh/          # Ảnh/sơ đồ xuất ra và file nguồn để sửa
xuat-ban/      # Cấu hình/thứ tự ghép và bản xuất đã xác nhận
```

Tổ chức theo chương/sản phẩm, không tổ chức bản chính chỉ theo tên người. Người phụ trách ghi trong bảng phân công và phần đầu file. Không đổi số 01–03 để chạy theo số chương báo cáo.

Các số liệu đã chốt lấy từ file 01–03. Bảng tính chi tiết mới dẫn nguồn về đúng mục; nếu phải lặp lại giá trị trong chương khác, ghi nguồn và đối chiếu lại khi nguồn thay đổi. Không dùng ảnh chụp bảng tính làm nguồn duy nhất cho số có công thức.

Không đưa toàn bộ sách/slide có bản quyền vào repo công khai chỉ để tiện chia sẻ. Hưng cung cấp tài liệu học qua cách truy cập phù hợp và ghi lại tên, trang, phiên bản; nếu bổ sung nguồn vào repo, phải xác định quyền chia sẻ trước.

## 3. Quy ước Markdown tối thiểu

- File UTF-8; tên file không dấu, có nghĩa, dùng dấu gạch nối. Mỗi file một tiêu đề `#`; các mục dùng `##`, `###` theo thứ bậc.
- Ghi đầu file: người chủ trì, người đọc chéo, trạng thái, nguồn/phiên bản đầu vào và câu hỏi còn mở. Không tự ghi tên người đọc chéo nếu họ chưa nhận việc.
- Liên kết file trong repo bằng đường dẫn tương đối. Khi đổi tên hoặc di chuyển file, tìm mọi nơi tham chiếu và kiểm link sau sửa. Không dùng đường dẫn `C:\...` trong nội dung để thành viên khác mở file.
- Bảng ghi rõ đơn vị. Dấu chấm phân tách hàng nghìn, dấu phẩy phân tách thập phân trong phần viết mới; nếu giữ nguyên dữ liệu nguồn theo quy ước khác, phải chú thích để không hiểu sai. Trong bảng viết “đơn vị: triệu VNĐ”, `1.667` nghĩa là 1.667 triệu, không phải 1,667 triệu.
- Giữ thuật ngữ “Tôn chỉ dự án”, “Người quản lý dự án (PM)”. Định nghĩa chữ viết tắt lần đầu sử dụng; không tự đặt thuật ngữ thay cho thuật ngữ môn học.
- Mã yêu cầu, WBS, hoạt động và rủi ro không trùng nhau. Nhóm thống nhất cách đặt mã trong lần bàn giao phạm vi đầu tiên; chưa áp một cấu trúc mã chi tiết khi chưa chốt.
- Hình có chú thích, nguồn và file chỉnh sửa được. Không chỉ gửi ảnh không rõ nội dung hoặc không có nguồn. Đường dẫn đến hình cũng phải hoạt động trong bản xuất thử.
- Bảng tính phải có đầu vào/công thức hoặc cách tính đủ để người khác tính lại. Không làm tròn từng hàng khiến tổng lệch mà không giải thích.
- Không định dạng thủ công font, lề, số trang trong từng chương. Kiểm thử sớm khả năng xuất heading, bảng, hình và công thức; hoàn thiện trình bày thống nhất ở cuối.

## 4. Giao việc bất đồng bộ và mốc bàn giao

Không yêu cầu cả nhóm phải cùng làm một giờ hoặc họp cố định sau mỗi buổi học. Một việc được giao bằng issue hoặc nội dung PR có thể truy cập được; bảng phân công tại file 06 dẫn tới nơi theo dõi hiện hành sau khi issue được tạo.

Mỗi việc ghi đủ:

| Trường | Nội dung cần có |
| --- | --- |
| Mục tiêu và đầu ra | File/bảng/sơ đồ nào cần bàn giao, đáp ứng câu hỏi nào |
| Đầu vào | Tài liệu, mục và phiên bản đang dùng; điểm chưa rõ |
| Người chủ trì / đọc chéo | Người đã xác nhận nhận vai |
| Phạm vi | Điều được làm, điều cần xin quyết định trước |
| Hoàn tất khi | Cách kiểm nội dung, số liệu và liên kết với phần khác |
| Mốc dự kiến | Thời điểm người làm dự kiến bàn giao bản đủ dùng |
| Mốc báo nguy cơ | Hạn cần báo khả năng trễ; phát hiện sớm thì báo ngay |
| Ngày cần đầu vào | Ngày muộn nhất người phụ thuộc cần nhận bản đã đủ dùng |

Ước lượng giờ công và khoảng thời gian lịch là hai giá trị khác nhau. Người nhận tự chọn thời gian làm trong khung đã cam kết. Mốc dự kiến phải chừa khoảng trước ngày người khác cần dùng để đủ đọc, sửa và xử lý bất trắc; chưa biết thời gian rảnh thì ghi “chờ xác nhận”, không tự đặt deadline thay cho thành viên.

Buffer phải nằm trên quan hệ phụ thuộc cụ thể, không chỉ là một số ngày cộng cuối bài. Ngoài buffer bàn giao từng phần, giữ một khoảng riêng cuối kỳ cho đối chiếu toàn bộ, sửa lỗi, xuất PDF/slide và tập trình bày. Độ dài các khoảng này chưa chốt; Hưng tổng hợp khả năng làm việc để xác định ở file 06.

Khi có nguy cơ trễ, người phụ trách báo: đã có đầu ra gì, thiếu gì, đang bị chặn bởi ai/điều gì, mốc mới đề xuất và phần nào sẽ bị ảnh hưởng. Hưng phối hợp điều chỉnh phạm vi đợt bàn giao, người hỗ trợ hoặc mốc phụ thuộc; không âm thầm dời ngày rồi coi như không có tác động.

## 5. Cập nhật theo bài giảng và kiểm soát thay đổi

Người phụ trách mảng liên quan tự đối chiếu bài giảng/yêu cầu mới, không chờ cả nhóm họp để tìm nội dung bổ sung. Nếu chưa có chủ trì, Hưng ghi vào danh sách việc mở và phân người xử lý.

- Thay đổi chỉ ảnh hưởng phần đang làm và không đổi nguồn đã chốt: tác giả cập nhật, ghi nguồn, gửi review.
- Thay đổi đụng phạm vi, dữ liệu gốc, lịch đã cam kết hoặc phần của người khác: ghi đề xuất, lý do, nguồn, file/mã chịu tác động và người cần phản hồi; Hưng quyết trong quyền điều phối hoặc đưa nhóm quyết theo bản chất thay đổi.
- Ràng buộc từ giảng viên chỉ được thay theo yêu cầu mới có nguồn hoặc xác nhận của giảng viên. Quyết định nhóm không được ghi thành yêu cầu của thầy.
- Sai số tính toán có thể sửa theo dữ liệu gốc cố định; đổi mức lương, thời gian tham gia, ngân sách hoặc nội dung đã chốt cần quyết định đúng thẩm quyền trước.
- Khi gặp hai dữ liệu gốc khác nhau, ghi vấn đề ở file 06, không tự chọn số thuận tiện. Nếu vấn đề chặn đầu ra đang làm thì dừng phần phụ thuộc; các phần độc lập vẫn tiếp tục.

Khi thay quyết định, giữ mã quyết định cũ, ghi quyết định thay thế, lý do và phạm vi tác động. Không dùng tin nhắn “đã làm rồi” làm bằng chứng một thay đổi đã được duyệt.

## 6. Review và tích hợp

Trước gửi review, tác giả kiểm phạm vi sửa, nguồn số liệu, phép tính, link, chính tả và các phần phụ thuộc. Nội dung PR nêu việc gì thay đổi, vì sao, đã kiểm thế nào và điểm chưa chắc. Một lời “đã xong” không thay thế đầu ra trong repo.

Người đọc chéo ưu tiên:

1. Có đúng yêu cầu môn và phạm vi việc được giao không?
2. Đầu vào và kết luận có căn cứ, số liệu có tính lại được không?
3. Mã, số liệu, thuật ngữ và giả định có khớp các phần liên quan không?
4. Có bỏ sót đầu vào/bàn giao hoặc tạo lịch bất khả thi không?
5. Chính tả, cấu trúc, liên kết, hình/bảng có dùng được không?

Trạng thái công việc: **Đang làm → Chờ review → Cần sửa (nếu có) → Đã duyệt**. Trạng thái “Bị chặn” phải kèm điều kiện cần giải quyết. Người đọc chéo nhận xét; tác giả sửa; Hưng xác nhận tích hợp. Phần do Hưng viết không được tự coi như đã có review độc lập.

T3 có thể kiểm tra số liệu và tài liệu điều phối theo yêu cầu của Hưng. Kết luận T3 phải ghi phạm vi, phiên bản, điều đã kiểm và điểm mở; không thay thế trách nhiệm học thuật của thành viên, quyết định của nhóm hay đánh giá của giảng viên.

## 7. Xuất báo cáo và thuyết trình

Hưng điều phối bản xuất cuối. Thành viên vẫn sở hữu và sửa nội dung mình viết; một người thống nhất trình bày không đồng nghĩa một người viết lại toàn bộ bài.

Thực hiện một bản xuất thử nhỏ sớm, có văn bản, bảng, hình và công thức; chưa cần nội dung đủ chín chương. Khi có đầu ra liên kết mới, ghép thử để phát hiện lỗi nội dung/định dạng. Công cụ xuất (ví dụ cách chuyển Markdown sang định dạng nộp) và template cụ thể còn chờ chọn, không coi repository hiện có pipeline build chạy được.

Trước nộp: chín chương đúng thứ tự; bảng đóng góp từng thành viên; nguồn và số liệu khớp; hình/bảng/mục lục đọc được; nội dung PDF và slide nhất quán; mỗi người đã chuẩn bị trình bày phần mình. Chốt danh sách file đầu vào và commit nguồn cho bản xuất. Chỉ ghép tài liệu được nhóm xác định là nội dung báo cáo; không tự ghép 04–06 hoặc các ghi chú review nội bộ.

PDF phải gửi qua email trước ngày báo cáo theo GV-01. Người gửi, mốc nội bộ, địa chỉ/cú pháp gửi được đối chiếu từ hướng dẫn môn trước khi thực hiện; chưa có ủy quyền cho agent gửi email. Slide và tập trình bày là đầu ra riêng, không được bỏ qua vì đã xuất được PDF.
