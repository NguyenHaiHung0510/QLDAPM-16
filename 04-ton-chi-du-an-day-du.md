# TÔN CHỈ DỰ ÁN

**Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS)**

> Bài tập Nhóm 16. Biên soạn: Codex theo chỉ dẫn của người quản lý tài liệu ngày 07/09/2026; đọc chéo: các subagent T3. Trạng thái: bản đề xuất hoàn chỉnh, chờ nhóm duyệt. Căn cứ: ba ảnh viết tay đã nộp, mẫu 7 mục của giảng viên và tài liệu [01](01-mo-ta-de-tai.md), [02](02-du-toan-kinh-phi.md), [03](03-ton-chi-du-an.md). Tên công ty, địa chỉ và thông tin liên hệ được xây dựng cho tình huống giả định của bài tập, không xác nhận danh tính hay trụ sở thực tế.

## 1. Thông tin chung

| Nội dung | Thông tin |
| --- | --- |
| Tên dự án | Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS) |
| Ngày bắt đầu | 03/06/2027 |
| Ngày kết thúc | 02/02/2028 |
| Tổng kinh phí | **2.000.000.000 VNĐ** (Hai tỷ đồng chẵn) |
| Nguồn | Ngân sách đầu tư của Doanh nghiệp Trà Tân Cương |
| Chủ đầu tư | Doanh nghiệp Trà Tân Cương |
| Đơn vị thụ hưởng | Kho tổng chế biến/đóng gói tại Thái Nguyên và 02 kho chi nhánh phân phối của Doanh nghiệp Trà Tân Cương |
| Đơn vị thi công | Công ty Cổ phần Công nghệ Raumania |
| Địa chỉ | Số 128 đường Trần Phú, phường Hà Đông, thành phố Hà Nội |
| Người đại diện | Nguyễn Đức Công |
| Người quản lý dự án (PM) | Bùi Hồng Phú |
| Điện thoại | 036 181 3636 |
| Email | phu.bui@raumania.example |

## 2. Mục tiêu của dự án

Xây dựng hệ thống quản lý thống nhất cho 03 kho của Doanh nghiệp Trà Tân Cương, số hóa quá trình nhập nguyên liệu, chế biến/đóng gói, bảo quản, xuất hàng và điều chuyển giữa các kho.

- Quản lý nhập–xuất–tồn theo mã lô, vị trí lưu trữ và hạn sử dụng; ghi nhận chất lượng, nhiệt độ/độ ẩm bảo quản; cảnh báo hàng cận hạn và tồn kho dưới ngưỡng.
- Quản lý định mức nguyên vật liệu (BOM), chuyển đổi theo độ ẩm và hao hụt trong chế biến; ưu tiên xuất lô còn hạn sử dụng có ngày hết hạn gần nhất (FEFO).
- Quản lý nhà cung cấp, đơn hàng xuất, nhân sự và phân quyền, tài chính kho, cơ sở vật chất và vật tư; cung cấp báo cáo phục vụ điều hành.
- Triển khai ứng dụng web trên máy trạm Windows, kết nối cân điện tử RS232, máy in tem/phiếu, máy quét mã vạch/QR và máy chấm công; đồng bộ dữ liệu giữa 03 kho.
- Đưa kho tổng vào vận hành thực tế chậm nhất cuối tháng thứ 6; hoàn thành triển khai và bàn giao toàn bộ trong 08 tháng, với tổng kinh phí không vượt 02 tỷ đồng.

Hệ thống phục vụ ban lãnh đạo, quản lý kho, thủ kho, công nhân chế biến/đóng gói, kế toán kho và nhân sự logistics/tài xế theo vai trò được phân công.

## 3. Sản phẩm bàn giao và mốc thời gian quan trọng

Thời gian dự án tính theo tháng kể từ ngày 03/06/2027: tháng thứ nhất từ 03/06 đến hết 02/07/2027; các tháng sau tính tương tự. **Mốc trong bảng là hạn hoàn thành/bàn giao, không phải ngày bắt đầu công việc.** Toàn dự án kết thúc hết ngày 02/02/2028, trước khi bước sang tháng thứ 9 vào ngày 03/02/2028.

| TT | Sản phẩm bàn giao | Hạn hoàn thành/bàn giao |
| ---: | --- | --- |
| 1 | Tài liệu đặc tả yêu cầu (SRS), bao gồm kết quả khảo sát và yêu cầu nghiệp vụ | 02/07/2027 — cuối tháng 1 |
| 2 | Tài liệu thiết kế kiến trúc hệ thống và cơ sở dữ liệu | 02/07/2027 — cuối tháng 1 |
| 3 | Phiên bản phần mềm hoàn thành các chức năng lõi quản lý kho, đọc cân RS232, in tem QR và xử lý BOM/FEFO, phục vụ kiểm thử tích hợp | 02/10/2027 — cuối tháng 4 |
| 4 | Hệ thống và thiết bị được lắp đặt tại kho tổng, hoàn thành chạy thử và kiểm thử chấp nhận của người dùng (UAT), kèm kết quả kiểm thử | 02/11/2027 — cuối tháng 5 |
| 5 | Hệ thống chính thức vận hành tại kho tổng; người dùng kho tổng được hướng dẫn, đào tạo trước khi sử dụng | **02/12/2027 — cuối tháng 6** |
| 6 | Hệ thống và thiết bị được triển khai tại 02 kho chi nhánh, kèm hướng dẫn và đào tạo sử dụng | 02/01/2028 — cuối tháng 7 |
| 7 | Phần mềm hoàn chỉnh, dịch vụ kết nối phần cứng, cơ sở dữ liệu đồng bộ 03 kho; hạ tầng và thiết bị; bộ tài liệu kỹ thuật, quy trình thao tác, hướng dẫn sử dụng; kết quả đào tạo bổ sung và biên bản nghiệm thu tổng thể, bàn giao | **02/02/2028 — cuối tháng 8** |

## 4. Tiêu chuẩn đánh giá sự thành công

| Tiêu chuẩn | Kết quả cần đạt |
| --- | --- |
| Tiến độ | Kho tổng vận hành thực tế chậm nhất ngày 02/12/2027; hoàn thành nghiệm thu, bàn giao toàn bộ chậm nhất ngày 02/02/2028 |
| Kinh phí | Tổng chi phí không vượt 2.000.000.000 VNĐ, bao gồm dự phòng rủi ro |
| Nghiệp vụ | Các chức năng trong phạm vi được kiểm thử chấp nhận; áp dụng đúng FEFO và định mức, hao hụt BOM; số liệu nhập–xuất–tồn khớp dữ liệu đối soát |
| Vận hành và thiết bị | Hệ thống hoạt động ổn định tại 03 kho trên máy trạm Windows; đọc dữ liệu cân liên tục qua RS232, không gây chậm thao tác nghiệp vụ; các thiết bị tích hợp hoạt động theo yêu cầu |
| Độ chính xác và tốc độ | Sai số cân tự động **< 0,1%**; thời gian in tem **< 2 giây/sản phẩm** |
| Bàn giao | Người dùng được đào tạo; tài liệu và sản phẩm bàn giao đầy đủ; có biên bản nghiệm thu được đại diện chủ đầu tư, đại diện các kho và PM xác nhận |

Cách đo sai số cân và thời gian in tem được thống nhất trong kế hoạch kiểm thử, giữ nguyên các ngưỡng trên.

## 5. Vai trò, trách nhiệm của các bên liên quan chính

| TT | Họ tên / Đơn vị | Vai trò | Trách nhiệm | Thông tin liên lạc |
| ---: | --- | --- | --- | --- |
| 1 | Trần Minh Đức — Doanh nghiệp Trà Tân Cương | Đại diện chủ đầu tư | Phê duyệt tôn chỉ, ngân sách và thay đổi lớn; bố trí đầu mối nghiệp vụ; quyết định nghiệm thu | 033 996 8288 |
| 2 | Nguyễn Đức Công — Công ty Cổ phần Công nghệ Raumania | Đại diện đơn vị thi công | Bố trí nguồn lực, phối hợp chủ đầu tư và chịu trách nhiệm về cam kết bàn giao của công ty | 035 682 4179 |
| 3 | Bùi Hồng Phú — Công ty Cổ phần Công nghệ Raumania | Người quản lý dự án (PM) | Lập kế hoạch, điều phối công việc; quản lý tiến độ, chi phí, chất lượng và rủi ro; tổ chức bàn giao | 036 181 3636 |
| 4 | Lê Thị Mai — Kho tổng | Đại diện kho tổng và người dùng nghiệp vụ | Cung cấp quy trình, dữ liệu; phối hợp thủ kho, công nhân và kế toán tham gia UAT; tiếp nhận vận hành | 038 724 6159 |
| 5 | Phạm Văn Hòa — Kho chi nhánh 1 | Đại diện kho chi nhánh 1 | Phối hợp triển khai, đối soát dữ liệu, kiểm thử và tiếp nhận sử dụng | 037 853 2649 |
| 6 | Đặng Thu Hà — Kho chi nhánh 2 | Đại diện kho chi nhánh 2 | Phối hợp triển khai, đối soát dữ liệu, kiểm thử và tiếp nhận sử dụng | 039 462 8751 |
| 7 | Vũ Minh Quân — Công ty Cổ phần Công nghệ Raumania | Đầu mối đội kỹ thuật | Phối hợp phân tích, thiết kế, phát triển, kiểm thử và triển khai; xử lý vấn đề kỹ thuật | 034 675 9281 |
| 8 | Đỗ Quốc Bảo — Công ty TNHH Thiết bị An Việt | Đại diện nhà cung cấp thiết bị | Cung cấp thiết bị đúng yêu cầu; hỗ trợ kết nối, lắp đặt và bảo hành | 032 847 5961 |
| 9 | Hoàng Văn Sơn — Cơ sở cung cấp trà Minh Sơn | Đại diện nhà cung cấp trà | Cung cấp thông tin nguyên liệu, lô hàng và chứng từ; phối hợp xác nhận quy trình nhập hàng | 033 758 4269 |

## 6. Một số rủi ro chính

| TT | Rủi ro | Hướng xử lý |
| ---: | --- | --- |
| 1 | Thiết bị không tương thích hoặc không đạt yêu cầu đọc cân, in tem | Kiểm tra trên thiết bị mẫu từ sớm; phối hợp nhà cung cấp xử lý trước khi triển khai |
| 2 | Yêu cầu giữa các kho chưa thống nhất hoặc thay đổi trong quá trình thực hiện | Xác nhận phạm vi với các đầu mối; đánh giá ảnh hưởng trước khi duyệt thay đổi |
| 3 | Dữ liệu cũ thiếu hoặc sai, gây chậm chuyển đổi | Thống nhất mẫu bảng tính Excel; kiểm tra và đối soát dữ liệu với doanh nghiệp trước khi chạy thử |
| 4 | Giao thiết bị chậm hoặc điện, Internet tại kho chưa sẵn sàng | Theo dõi lịch cung cấp thiết bị; kiểm tra điều kiện tại kho trước khi lắp đặt |
| 5 | Người dùng không tham gia kiểm thử, đào tạo đúng lịch | Thống nhất lịch với quản lý kho; bố trí đầu mối tham gia và hướng dẫn trước khi vận hành |

Giả định thực hiện: doanh nghiệp bố trí công nhân và thủ kho tham gia UAT đúng tiến độ; điện và Internet tại 03 kho ổn định; cân điện tử và máy in tem mua mới đạt chuẩn kết nối; dữ liệu cũ được cung cấp dưới dạng bảng tính Excel. Các điều kiện này được kiểm tra trong quá trình lập kế hoạch và triển khai.

## 7. Ký phê duyệt của chủ đầu tư

Đại diện chủ đầu tư phê duyệt.
