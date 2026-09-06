# Khung BTL và bản đồ đầu ra — Nhóm 16

**Loại tài liệu:** Điều phối nội bộ, không phải chương báo cáo để nộp.

**Ngày thiết lập:** 06/09/2026. Các nguyên tắc tổ chức đã được Hưng đồng ý trong phiên tư vấn; các tên người, thời hạn và yêu cầu chi tiết chưa có xác nhận được giữ ở trạng thái mở trong [quyết định và phân công](06-quyet-dinh-va-phan-cong.md). Việc tài liệu được commit không thay thế xác nhận của thành viên hoặc yêu cầu mới từ giảng viên.

## 1. Đọc từ đâu và tài liệu nào là nguồn gốc?

1. Đọc tài liệu này để hiểu BTL cần tạo ra gì và các phần liên quan thế nào.
2. Đọc ba tài liệu gốc dưới đây để hiểu dự án kho trà đã được nhóm thống nhất.
3. Đọc [quy cách cộng tác](05-quy-cach-cong-tac.md) trước khi nhận và bàn giao việc.
4. Xem [quyết định và phân công](06-quyet-dinh-va-phan-cong.md) để biết điều đã chốt, việc đang mở và phần mình phụ trách.

| Tài liệu gốc đã được nhóm thống nhất | Vai trò |
| --- | --- |
| [01 — Mô tả đề tài](01-mo-ta-de-tai.md) | Bối cảnh, nhu cầu và phạm vi chức năng ban đầu |
| [02 — Dự toán kinh phí](02-du-toan-kinh-phi.md) | Nguồn gốc bảng lương, lịch tham gia, ngân sách và thiết bị; mục V theo dõi phân bổ chi phí |
| [03 — Tôn chỉ dự án](03-ton-chi-du-an.md) | Mục tiêu, bên liên quan, sản phẩm bàn giao, mốc và ràng buộc |

Repository này là nơi quản lý bản gốc của nhóm. Hưng quản lý lưu trữ và duyệt thay đổi. Không duy trì một bản có thể sửa độc lập trong kho học cá nhân rồi coi cả hai là bản chính. Các bản đã nộp hoặc xuất ra là snapshot: phải ghi phiên bản nguồn, không tự đồng bộ ngược vào bản gốc.

Việc đổi số file chỉ là đổi tổ chức lưu trữ: `00-mo-ta-de-tai.md` → `01-mo-ta-de-tai.md`; `01-du-toan-kinh-phi.md` → `02-du-toan-kinh-phi.md`; `03-ton-chi-du-an.md` giữ tên. Số file gốc không phải số chương báo cáo: file `02` cung cấp dữ liệu cho nhiều chương, đặc biệt chương 4 và 6.

## 2. Nguồn yêu cầu và mức độ xác nhận

Các ký hiệu nguồn dưới đây dùng trong toàn bộ ba tài liệu điều phối. Tên PDF là tên nguồn, không phải liên kết tải xuống trong repo.

| Mã | Nguồn đã đối chiếu | Nội dung dùng |
| --- | --- | --- |
| GV-01 | `0-intro.pdf`, trang 12–14 | Đầu ra, chín chương, quy định phân công, nộp bài, đổi lịch và AI |
| GV-02 | `0-intro.pdf`, trang 4–5, 16 | Nội dung môn, chuẩn đầu ra, tài liệu tham khảo PMBOK 6 và bài giảng PTIT |
| GV-03 | `1-overview.pdf`, trang 9, 11, 25–26, 29 | Ràng buộc dự án, hoạt động quản lý, trách nhiệm PM, bài tập dự toán sơ bộ |
| GV-04 | `2-process.pdf`, trang 13–15, 24, 32–36 | Nhóm tiến trình, quan hệ phụ thuộc, lập kế hoạch, ánh xạ miền kiến thức và bài tập tôn chỉ |
| LICH-01 | Ảnh lịch nhóm do Hưng cung cấp | Nhóm 16; Dũng, Công, Phú, Hưng; báo cáo 23/11 |
| NOTE-01 | Ghi chú môn `02-self-note.txt` do Hưng quản lý | Không code/prototype; dùng thuật ngữ “Người quản lý dự án”, “Tôn chỉ dự án” |
| OWNER-01 | Xác nhận của Hưng trong phiên điều phối ngày 06/09/2026 | Ba tài liệu gốc đã được nhóm thống nhất; quyết định tổ chức tại file 06 |

Các PDF và ảnh lịch chưa được đưa vào repo. Hưng cần cung cấp cách truy cập tài liệu môn cho thành viên trước khi họ tự đối chiếu nguồn; đây là việc mở tại file 06. Không đưa đường dẫn máy cá nhân hoặc một link chưa chia sẻ vào quy trình như thể cả nhóm đã truy cập được.

### 2.1. Yêu cầu bắt buộc của BTL

- Nhóm 3–4 thành viên; nhóm 16 hiện có 4 thành viên.
- Lập kế hoạch quản lý cho một dự án phần mềm cụ thể, báo cáo theo chín chương tại mục 4.
- Nộp quyển **PDF qua email trước ngày báo cáo**, và chuẩn bị **slide để thuyết trình theo lịch giảng viên**. Lịch hiện được cung cấp là **23/11**. Chưa có giờ nộp cụ thể hoặc thời lượng thuyết trình BTL được xác nhận trong các nguồn đã đọc.
- Nộp không đúng hạn bị trừ điểm. Không coi ngày 23/11 là hạn được phép gửi PDF trong ngày.
- Muốn đổi lịch BTL: tự thỏa thuận với một nhóm khác, có sự đồng ý rồi báo giảng viên **ít nhất 3 ngày trước ngày báo cáo**. Không dùng quy định một ngày của phần thuyết trình chuyên đề để thay thế.
- Báo cáo ghi rõ công việc của từng thành viên. Mỗi người phụ trách tối thiểu một nội dung trong **phạm vi, thời gian, chi phí, nguồn nhân lực**; các phần còn lại phân công để bảo đảm thống nhất và đồng bộ. Mỗi người tự trình bày phần mình đã làm.
- GV-01 nêu: **“Nếu phát hiện hành vi sao chép bài hoặc sử dụng công cụ AI để làm báo cáo: 3 điểm.”** Không diễn giải thành việc dùng AI viết hộ rồi sửa câu chữ là được phép. Các tài liệu điều phối có hỗ trợ AI không tự tạo ngoại lệ đối với quy định này; không tự đưa chúng vào quyển nộp. Nhóm tự thực hiện nội dung học thuật và chịu trách nhiệm giải thích sản phẩm của mình; phạm vi sử dụng công cụ còn chưa rõ phải được làm rõ với giảng viên khi cần.

### 2.2. Điều gì chưa phải yêu cầu của giảng viên?

GitHub, Markdown, review chéo, cách chia file và mốc nội bộ là quy ước tổ chức của nhóm. Danh sách biểu mẫu ở mục 4 là khung làm việc để chuẩn bị, không phải rubric chi tiết đã được thầy xác nhận. Khi có bài giảng/yêu cầu mới, người phụ trách cập nhật ảnh hưởng qua quy trình ở file 05.

Chiến lược học riêng, tài liệu PMBOK khác hoặc hướng thử nghiệm công nghệ/AI của một thành viên không tự trở thành phạm vi BTL. Nguồn tham khảo môn hiện xác nhận PMBOK 6 và bài giảng PTIT; không tự thêm chức năng để làm bài “đổi mới”.

## 3. Hiểu khung môn trước khi chia chương

| Khái niệm | Câu hỏi | Cách dùng trong BTL |
| --- | --- | --- |
| Vòng đời dự án | Công việc dự án đi qua các giai đoạn nào? | Khảo sát, phát triển, triển khai, bàn giao theo mô hình nhóm chọn và giải thích |
| Nhóm tiến trình | Cần thực hiện loại hoạt động quản lý nào? | Khởi tạo; lập kế hoạch; thực hiện; giám sát và kiểm soát; kết thúc |
| Miền kiến thức | Đang quản lý khía cạnh nào? | Phạm vi, thời gian, chi phí, nhân lực, mua sắm, giao tiếp, rủi ro, chất lượng và sự tích hợp |

Nhóm tiến trình không đồng nhất với các pha của vòng đời; có thể lặp trong từng pha (GV-04). Chương báo cáo không phải chuỗi công việc phải làm xong tuần tự từ 1 đến 9. Tích hợp và các bên liên quan vẫn phải được xử lý xuyên suốt, dù khung thầy không yêu cầu thêm chương 10 hoặc 11.

Phân biệt **bốn sinh viên làm BTL** với **đội dự án phần mềm giả định trong file 02**. Phân công sinh viên ở file 06; bảng tổ chức, lương và huy động của dự án giả định dùng cho chương nhân lực/chi phí. Không lấy thời gian rảnh của sinh viên làm lịch làm việc của kỹ sư trong dự toán, hoặc lấy vai PM giả định làm bằng chứng một sinh viên đã làm tất cả các chương.

Mỗi chương cần chỉ rõ quyết định cho dự án kho trà, căn cứ/biểu mẫu để giải thích, cách kiểm soát và xử lý thay đổi. BTL lập kế hoạch cho cả việc thực hiện, theo dõi và nghiệm thu; không yêu cầu tạo kết quả thực thi giả. Dữ liệu ví dụ phải ghi là tình huống giả định, không ghi thành kết quả thực tế.

## 4. Bản đồ chín chương và đầu ra làm việc

Các thuật ngữ dùng trong bảng:

- **WBS — Work Breakdown Structure:** cấu trúc phân rã công việc theo sản phẩm bàn giao và gói công việc; cung cấp cấu trúc chung để các phần lập kế hoạch liên kết với nhau.
- **CPM — Critical Path Method:** phương pháp đường găng, phân tích mạng công việc để xác định chuỗi chi phối thời gian hoàn thành dự án theo các giả định của lịch.
- **EVM — Earned Value Management:** quản lý giá trị thu được, đối chiếu giá trị công việc theo kế hoạch, giá trị công việc đã hoàn thành và chi phí thực tế; cần đủ dữ liệu, không tính chỉ từ bảng ngân sách tổng.
- **RACI — Responsible, Accountable, Consulted, Informed:** ma trận phân công người thực hiện, người chịu trách nhiệm cuối cùng, người được tham vấn và người được thông báo. Việc lập ma trận không thay thế xác nhận nhận việc của thành viên.

| Chương theo GV-01 | Câu hỏi quản lý | Đầu ra dự kiến cần chuẩn bị | Quan hệ đầu vào/đầu ra |
| --- | --- | --- | --- |
| 1. Tôn chỉ dự án | Vì sao thực hiện, mục tiêu và ràng buộc gì, ai liên quan? | Tôn chỉ dựa trên file 03; đối chiếu file 01 và 02 | Là nền cho toàn bộ kế hoạch; không chép số liệu khác bản gốc |
| 2. Quản lý phạm vi | Bàn giao gì, giới hạn đến đâu, gồm những gói công việc nào? | Mô tả phạm vi, danh mục bàn giao, WBS, mô tả gói công việc, cách xác nhận và kiểm soát phạm vi | Cấp mã và nội dung công việc cho tiến độ, nhân lực, chi phí, chất lượng |
| 3. Quản lý thời gian | Công việc phụ thuộc nhau ra sao, cần bao lâu, có đạt mốc không? | Danh sách hoạt động, quan hệ trước/sau, căn cứ thời lượng, lịch trình; sơ đồ mạng/CPM theo hướng dẫn học phần | Nhận WBS; đối chiếu nhân lực, mua sắm và rủi ro trước khi chốt |
| 4. Quản lý chi phí | Tiền được tính từ đâu và phân bổ cho công việc thế nào? | Bảng tính có căn cứ, ngân sách theo thời gian, cách theo dõi chi phí; EVM khi xác định đủ đầu vào/yêu cầu | Nhận WBS, nguồn lực, tiến độ, mua sắm, rủi ro; tuân thủ ràng buộc file 02 |
| 5. Quản lý mua sắm | Mua/thuê gì, cần có lúc nào, chọn và nghiệm thu ra sao? | Danh mục, yêu cầu, kế hoạch đặt/nhận hàng, tiêu chí nhà cung cấp và nghiệm thu | Cấp thời gian chờ, điều kiện và chi phí cho tiến độ/chi phí |
| 6. Quản lý nguồn nhân lực | Vai trò nào làm việc gì, tham gia lúc nào? | Cơ cấu tổ chức, trách nhiệm/RACI, lịch huy động, cách điều phối và phát triển đội | Nhận WBS; dùng bảng nhân lực đã chốt; kiểm tra khả năng bố trí theo lịch |
| 7. Quản lý giao tiếp | Ai cần thông tin gì, khi nào, ai cung cấp và xử lý vấn đề? | Ma trận giao tiếp, hình thức/nhịp báo cáo, cách chuyển vấn đề cần quyết định | Bao quát bên liên quan của dự án giả định; phân biệt quy cách sinh viên ở file 05 |
| 8. Quản lý rủi ro | Điều gì ảnh hưởng mục tiêu, ai theo dõi, xử lý thế nào? | Danh mục, đánh giá ưu tiên, phương án ứng phó và người theo dõi | Nhận giả định của mọi phần; trả tác động về phạm vi, thời gian, chi phí |
| 9. Quản lý chất lượng | Thế nào là đạt, kiểm tra thế nào và ai xác nhận? | Tiêu chí, hoạt động bảo đảm/kiểm soát chất lượng, phương pháp nghiệm thu | Liên hệ từng sản phẩm bàn giao và nguồn lực/thời gian thực hiện kiểm tra |

Độ chi tiết của các đầu ra được cập nhật theo môn học; không tự biến mọi ví dụ trong bảng thành một biểu mẫu bắt buộc. Không đánh dấu một chương hoàn tất chỉ vì có số trang hoặc có đủ tiêu đề.

## 5. Luồng thực hiện và phụ thuộc

**Đợt mở đầu:** Hưng cung cấp khung phạm vi/WBS đủ bao quát; ba bạn còn lại có thể đồng thời đọc nguồn, chuẩn bị cấu trúc hoạt động, đối chiếu bảng nhân lực và kiểm tra căn cứ chi phí. Không phải đợi chương 2 viết xong toàn bộ.

**Đợt lập kế hoạch liên kết:** khi có mã WBS và mô tả bàn giao đủ dùng, người thời gian lập hoạt động, người nhân lực gắn vai trò và người chi phí gắn căn cứ. Các bên trả lại điểm thiếu hoặc không khả thi; chưa tự sửa ràng buộc đã chốt. Mua sắm, rủi ro và chất lượng cung cấp đầu vào ngay khi chúng ảnh hưởng kế hoạch, dù chương đầy đủ sẽ làm sau.

**Đợt hoàn thiện và tích hợp:** đối chiếu mã, số liệu, giả định, bảng nguồn và cách kiểm soát; sau đó mới khóa nội dung và hoàn thiện trình bày.

| Bàn giao cho ai? | Đầu vào đủ để bắt đầu | Chưa cần chờ |
| --- | --- | --- |
| Thời gian | Mã WBS, nội dung gói, bàn giao, mốc đã chốt, câu hỏi mở | Phần dẫn nhập/format hoàn thiện của chương 2 |
| Nhân lực | WBS sơ bộ và bảng vai trò/lịch tham gia ở file 02 | Toàn bộ sơ đồ mạng tiến độ đã chốt |
| Chi phí | Các bảng ngân sách, lương, thiết bị gốc; WBS và nguồn lực sơ bộ | Văn xuôi hoàn thiện của chương 3/6 |
| Mua sắm | Nhu cầu thiết bị/dịch vụ và thời điểm cần sử dụng | Toàn bộ chương nhân lực |
| Rủi ro/chất lượng | Sản phẩm bàn giao, ràng buộc và giả định đang có | Kế hoạch hoàn chỉnh của tất cả các chương |

Hưng bàn giao phạm vi theo hai mức: **đủ để phối hợp** rồi **hoàn thiện**. Mã đã cấp giữ ổn định; khi đổi cấu trúc phải có ánh xạ mã và danh sách phần bị tác động. Phạm vi cần bao quát công việc quản lý, chuyển dữ liệu, kiểm thử, triển khai, đào tạo và bàn giao phù hợp với tài liệu gốc, không chỉ liệt kê tính năng phần mềm.

Không cần làm xong chương 5 trước chương 6. Nhân lực tham gia từ đầu vì quyết định khả năng lập lịch và chi phí; mua sắm cần cung cấp thời gian chờ và điều kiện tiếp nhận trước các mốc tích hợp/triển khai.

## 6. Điều kiện đủ để giao và đóng một phần việc

Trước khi giao: có đầu ra cụ thể, nguồn đầu vào/phiên bản, người chủ trì, người đọc chéo, tiêu chí hoàn tất và ba mốc thời gian theo file 05. Người nhận xác nhận khả năng đáp ứng; phần chưa biết ghi rõ thay vì biến thành cam kết.

Trước khi đóng: đầu ra có trong repo; người viết giải thích được căn cứ; liên kết và số liệu đã kiểm; phản hồi liên quan được xử lý; người đọc chéo có kết luận; Hưng duyệt phần thay đổi thuộc quyền của mình. Kết quả review tài liệu không phải xác nhận giảng viên chấp nhận bài hoặc xác nhận dự án phần mềm đã thực thi.

Các điểm dữ liệu gốc chưa thống nhất hoàn toàn và các điều kiện chưa đủ kiểm chứng được theo dõi trong file 06. Không che chúng bằng một dấu “hoàn tất” chung.
