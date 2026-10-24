# KẾ HOẠCH QUẢN LÝ GIAO TIẾP DỰ ÁN WMS

## 1. Thông tin chung

- **Tên dự án:** Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS).
- **Chủ đầu tư:** Doanh nghiệp Trà Tân Cương.
- **Đơn vị triển khai:** Công ty Cổ phần Công nghệ Raumania.
- **Quản lý dự án:** Bùi Hồng Phú.
- **Thời gian thực hiện:** 03/06/2027 – 02/02/2028.

## 2. Mục tiêu và phạm vi kế hoạch

Kế hoạch quản lý giao tiếp xác định các bên tham gia, nhu cầu thông tin, phương pháp và công cụ trao đổi, tần suất giao tiếp, trách nhiệm phản hồi, luồng xử lý thông tin và cách quản lý ma trận truyền thông. Mục tiêu là bảo đảm thông tin dự án được truyền đạt đúng đối tượng, đúng thời điểm, nhất quán và có thể tra cứu khi cần.

Kế hoạch áp dụng cho hoạt động điều phối giữa chủ đầu tư, đơn vị triển khai, đội kỹ thuật, đại diện các kho, nhà cung cấp thiết bị và nhà cung cấp trà trong suốt quá trình thực hiện, kiểm thử, triển khai và bàn giao hệ thống WMS.

## 3. Các bên tham gia giao tiếp

Danh sách các bên tham gia giao tiếp và nhu cầu thông tin chính của dự án được trình bày dưới đây.

| STT | Họ tên / Nhóm | Đơn vị / Vai trò | Nhu cầu giao tiếp chính |
|---:|---|---|---|
| 1 | Trần Minh Đức | Đại diện chủ đầu tư – Doanh nghiệp Trà Tân Cương | Báo cáo tình hình dự án, vấn đề cần quyết định, thay đổi lớn và kết quả nghiệm thu |
| 2 | Nguyễn Đức Công | Đại diện đơn vị thi công – Công ty Cổ phần Công nghệ Raumania | Tình hình thực hiện, nguồn lực, vấn đề cần phối hợp và cam kết bàn giao |
| 3 | Bùi Hồng Phú | Project Manager (PM), Công ty Cổ phần Công nghệ Raumania | Thông tin tổng thể, tiến độ công việc, vấn đề phát sinh, quyết định, báo cáo và bàn giao |
| 4 | Lê Thị Mai | Đại diện kho tổng | Quy trình nghiệp vụ, dữ liệu kho, kết quả UAT, đào tạo và vận hành |
| 5 | Phạm Văn Hòa | Đại diện kho chi nhánh 1 | Kế hoạch triển khai, dữ liệu cần đối soát, kiểm thử và tiếp nhận sử dụng |
| 6 | Đặng Thu Hà | Đại diện kho chi nhánh 2 | Kế hoạch triển khai, dữ liệu cần đối soát, kiểm thử và tiếp nhận sử dụng |
| 7 | Vũ Minh Quân | Đầu mối đội kỹ thuật, Công ty Cổ phần Công nghệ Raumania | Thiết kế, phát triển, tích hợp, kiểm thử, vấn đề kỹ thuật và triển khai |
| 8 | Đỗ Quốc Bảo | Đại diện Công ty TNHH Thiết bị An Việt | Thông số, lịch cung cấp thiết bị, kết nối, lắp đặt và bảo hành |
| 9 | Hoàng Văn Sơn | Đại diện Cơ sở cung cấp trà Minh Sơn | Thông tin nguyên liệu, lô hàng, chứng từ và quy trình nhập hàng |
| 10 | Tech Lead, BA, Backend Developer, Frontend Developer, Hardware/IoT Engineer, QA/QC Engineer, Deployment/Onsite Engineer | Đội kỹ thuật dự án | Yêu cầu nghiệp vụ, thiết kế, phát triển, tích hợp, lỗi, kiểm thử và triển khai theo chuyên môn |

Lưu ý: Các vị trí kỹ thuật được nêu theo chức danh; không gán tên riêng cho những vị trí chưa được xác định.

## 4. Nhu cầu thông tin cụ thể

| STT | Thông tin cần trao đổi | Bên cung cấp chính | Bên nhận chính | Mục đích |
|---:|---|---|---|---|
| 1 | Tình hình tổng thể, tiến độ và vấn đề nổi bật | PM | Đại diện đơn vị thi công, đại diện chủ đầu tư | Nắm tình hình dự án và quyết định khi cần |
| 2 | Yêu cầu nghiệp vụ và quy trình vận hành kho | Đại diện các kho, BA | BA, Tech Lead và đội phát triển | Xây dựng chức năng phù hợp nhu cầu thực tế |
| 3 | Tài liệu SRS và các nội dung cần xác nhận | BA | PM, đại diện các kho, Tech Lead | Thống nhất yêu cầu trước khi phát triển |
| 4 | Thiết kế kiến trúc, cơ sở dữ liệu và API | Tech Lead, Backend | Đội phát triển, QA/QC, PM khi cần | Bảo đảm các thành phần được phát triển nhất quán |
| 5 | Tình trạng phát triển và vấn đề kỹ thuật | Backend, Frontend, Hardware/IoT | Tech Lead, PM, các nhóm liên quan | Phối hợp xử lý phụ thuộc và trở ngại |
| 6 | Thông số, tình trạng giao hàng và kết nối thiết bị | Nhà cung cấp thiết bị, Hardware/IoT | Tech Lead, PM, Deployment/Onsite | Bảo đảm thiết bị đáp ứng yêu cầu tích hợp và triển khai |
| 7 | Dữ liệu nguyên liệu, lô hàng và chứng từ đầu vào | Nhà cung cấp trà, đại diện kho | BA, đại diện kho, đội phát triển liên quan | Hỗ trợ xây dựng và xác nhận quy trình nhập hàng |
| 8 | Kế hoạch kiểm thử, lỗi và kết quả kiểm thử | QA/QC và đội phát triển | PM, Tech Lead, nhóm phụ trách khắc phục | Theo dõi lỗi và xác nhận mức độ đáp ứng yêu cầu |
| 9 | Kết quả UAT và phản hồi của người dùng | Đại diện các kho, QA/QC | PM, BA, đội kỹ thuật | Xác nhận hệ thống phù hợp với nghiệp vụ trước khi vận hành |
| 10 | Lịch lắp đặt, triển khai và điều kiện sẵn sàng tại kho | Deployment/Onsite, Hardware/IoT | PM, đại diện kho, Tech Lead | Phối hợp chuẩn bị địa điểm, thiết bị và nhân sự |
| 11 | Tài liệu đào tạo và hướng dẫn sử dụng | BA, Deployment/Onsite | Đại diện kho và người dùng liên quan | Chuẩn bị cho việc tiếp nhận và vận hành hệ thống |
| 12 | Kết quả nghiệm thu, bàn giao và vấn đề tồn đọng | PM, QA/QC, đội kỹ thuật | Đại diện chủ đầu tư, đại diện đơn vị thi công, đại diện các kho | Xác nhận kết quả bàn giao và các trách nhiệm còn lại |

Các luồng thông tin là phương án tổ chức giao tiếp của dự án; đầu mối cung cấp và nhận từng loại thông tin cần được thống nhất trong quá trình triển khai.

## 5. Nguyên tắc giao tiếp

- **Đúng đối tượng:** Gửi thông tin đến người có trách nhiệm xử lý hoặc xác nhận nội dung.
- **Đúng thẩm quyền:** Chuyển các thay đổi lớn, quyết định nghiệm thu và vấn đề vượt thẩm quyền đến đúng cấp có thẩm quyền theo tôn chỉ dự án.
- **Có căn cứ kiểm tra:** Ghi nhận các yêu cầu, quyết định, lỗi và kết quả nghiệm thu quan trọng để có thể đối chiếu.
- **Có phản hồi:** Theo dõi các thông tin cần xác nhận đến khi có phản hồi hoặc quyết định xử lý.
- **Nhất quán:** Khi yêu cầu hoặc quyết định thay đổi, cập nhật cho các nhóm chịu ảnh hưởng để tránh sử dụng thông tin cũ.


## 6. Công cụ và phương pháp giao tiếp

### 6.1. Nguyên tắc lựa chọn

Mục tiêu là chọn cách thức trao đổi thông tin phù hợp với từng nhóm đối tượng và nhu cầu của dự án WMS, bảo đảm thông tin được truyền đạt đúng người, đúng thời điểm và có thể tra cứu lại khi cần.

- **Thông tin cần phê duyệt:** sử dụng văn bản hoặc email để lưu lại nội dung, người xác nhận và thời điểm xác nhận.
- **Vấn đề cần trao đổi nhanh:** dùng trao đổi trực tiếp hoặc họp ngắn; nếu ảnh hưởng đến phạm vi, tiến độ hoặc chất lượng thì phải ghi lại kết luận.
- **Nội dung kỹ thuật phức tạp:** tổ chức họp chuyên môn hoặc trao đổi trực tiếp giữa những người phụ trách; lưu lại quyết định kỹ thuật.
- **Kiểm thử và nghiệm thu:** sử dụng biểu mẫu, biên bản hoặc báo cáo có cấu trúc để dễ theo dõi kết quả và trách nhiệm xử lý.
- **Thông tin cần theo dõi xuyên suốt:** lưu trữ tập trung, tránh để yêu cầu, lỗi và quyết định chỉ nằm trong tin nhắn cá nhân.

Các nguyên tắc này được áp dụng thống nhất trong quá trình giao tiếp của dự án.

### 6.2. Lựa chọn công cụ và phương pháp giao tiếp

| Nhu cầu giao tiếp | Công cụ / phương pháp đề xuất | Người tham gia chính | Lý do lựa chọn |
|---|---|---|---|
| 1. Báo cáo tình trạng và tiến độ dự án | Báo cáo tiến độ bằng văn bản, email, họp định kỳ | PM, đại diện chủ đầu tư, đại diện đơn vị triển khai | Theo dõi tiến độ, vấn đề tồn đọng và các quyết định cần đưa ra |
| 2. Thu thập yêu cầu nghiệp vụ kho | Phỏng vấn, trao đổi trực tiếp, họp khảo sát | BA, đại diện kho chính, đại diện hai kho chi nhánh | Làm rõ quy trình nhập, xuất, tồn kho và sự khác biệt giữa các kho |
| 3. Xác nhận SRS và yêu cầu | Tài liệu SRS, email xác nhận, họp rà soát | BA, PM, đại diện kho, Tech Lead | Hạn chế hiểu sai yêu cầu trước khi phát triển |
| 4. Trao đổi kiến trúc, cơ sở dữ liệu và API | Tài liệu thiết kế, sơ đồ, họp kỹ thuật | Tech Lead, Backend, Frontend, QA/QC và các thành viên liên quan | Bảo đảm các thành phần được thiết kế nhất quán |
| 5. Cập nhật tiến độ phát triển và xử lý vấn đề kỹ thuật | Công cụ quản lý công việc, trao đổi nhóm, họp kỹ thuật khi cần | Nhóm phát triển, Tech Lead, PM | Theo dõi người phụ trách, trạng thái và các vấn đề phụ thuộc |
| 6. Thông tin thiết bị và khả năng kết nối | Tài liệu thông số kỹ thuật, email, họp tích hợp | Nhà cung cấp thiết bị, Hardware/IoT, Tech Lead, Deployment/Onsite | Kiểm tra tính tương thích của cân điện tử RS232, thiết bị và hệ thống |
| 7. Dữ liệu trà, lô hàng và chứng từ nhập kho | Biểu mẫu dữ liệu, tài liệu chứng từ, trao đổi trực tiếp | Nhà cung cấp trà, đại diện kho, BA và nhóm kỹ thuật liên quan | Làm rõ dữ liệu đầu vào và quy trình tiếp nhận |
| 8. Kế hoạch kiểm thử, lỗi và kết quả kiểm thử | Công cụ theo dõi lỗi, báo cáo kiểm thử, họp xử lý lỗi | QA/QC, nhóm phát triển, Tech Lead, PM | Theo dõi lỗi, mức độ ưu tiên, người xử lý và kết quả kiểm tra lại |
| 9. Kết quả UAT và phản hồi người dùng | Biểu mẫu UAT, biên bản kiểm thử và họp đánh giá | Đại diện các kho, QA/QC, BA, PM, nhóm kỹ thuật | Ghi nhận mức độ đáp ứng yêu cầu và các vấn đề cần khắc phục |
| 10. Lịch triển khai và mức độ sẵn sàng tại kho | Kế hoạch triển khai, checklist chuẩn bị, họp điều phối | Deployment/Onsite, Hardware/IoT, PM, đại diện kho | Bảo đảm địa điểm, thiết bị, dữ liệu và người dùng sẵn sàng |
| 11. Tài liệu hướng dẫn và đào tạo | Tài liệu hướng dẫn, buổi đào tạo trực tiếp, hỏi đáp | BA, Deployment/Onsite, đại diện kho và người dùng | Giúp người dùng hiểu và vận hành hệ thống |
| 12. Nghiệm thu, bàn giao và vấn đề còn tồn đọng | Biên bản nghiệm thu, tài liệu bàn giao, email xác nhận | PM, đại diện chủ đầu tư, đại diện đơn vị triển khai, đại diện kho | Làm rõ kết quả bàn giao, trách nhiệm và các công việc còn lại |

**Lưu ý:** Công cụ quản lý công việc và nơi lưu trữ tài liệu cần được nhóm thống nhất; không mặc định một nền tảng cụ thể đã được lựa chọn.

### 6.3. Quy định sử dụng các kênh giao tiếp

Để bảo đảm thông tin được trao đổi thống nhất, chính xác và có thể truy xuất trong suốt vòng đời dự án, các thành viên áp dụng những quy định sau.

#### 6.3.1. Email hoặc văn bản chính thức

- **Mục đích:** Sử dụng khi gửi báo cáo chính thức, yêu cầu xác nhận, phê duyệt tài liệu, đề xuất thay đổi yêu cầu, thông báo vấn đề quan trọng và xác nhận nghiệm thu, bàn giao.
- **Người thực hiện:** PM chịu trách nhiệm điều phối các thông tin chính thức giữa đại diện chủ đầu tư và đại diện đơn vị triển khai. BA phụ trách gửi tài liệu yêu cầu; các thành viên chuyên môn gửi tài liệu thuộc phạm vi phụ trách.
- **Cách thực hiện:** Nội dung gửi phải có tiêu đề rõ ràng, nêu mục đích, nội dung cần phản hồi, người chịu trách nhiệm và thời hạn phản hồi nếu có. Tài liệu gửi xác nhận phải ghi rõ tên tài liệu và phiên bản.
- **Quy định xác nhận:** Những nội dung cần phê duyệt phải có phản hồi xác nhận từ người có thẩm quyền. Nếu chưa nhận được phản hồi, người phụ trách cần chủ động nhắc lại và báo PM khi việc chậm xác nhận có nguy cơ ảnh hưởng đến tiến độ.
- **Lưu trữ:** Lưu email xác nhận, văn bản phê duyệt và tài liệu liên quan tại nơi lưu trữ chung của dự án.

#### 6.3.2. Họp dự án

- **Mục đích:** Giải quyết các vấn đề cần thảo luận trực tiếp, thống nhất yêu cầu nghiệp vụ, xử lý vướng mắc kỹ thuật, đánh giá tiến độ và đưa ra quyết định.
- **Người tổ chức:** PM chủ trì các cuộc họp điều phối chung; BA chủ trì các buổi làm rõ yêu cầu; Tech Lead chủ trì các buổi trao đổi chuyên môn kỹ thuật; QA/QC phối hợp tổ chức các buổi đánh giá kiểm thử khi cần.
- **Trước cuộc họp:** Người tổ chức xác định mục tiêu, nội dung, thành phần tham gia và tài liệu cần chuẩn bị. Các bên liên quan phải được thông báo trước để sắp xếp thời gian.
- **Trong cuộc họp:** Tập trung vào nội dung cần giải quyết, ghi nhận ý kiến khác biệt, các quyết định được thống nhất và những vấn đề chưa có kết luận.
- **Sau cuộc họp:** Lập biên bản hoặc bản ghi kết luận, bao gồm quyết định, công việc tiếp theo, người chịu trách nhiệm và thời hạn hoàn thành. PM hoặc người được phân công theo dõi các công việc liên quan.
- **Xử lý khi vắng mặt:** Người không tham gia nhưng có trách nhiệm thực hiện công việc phải được thông báo về kết luận liên quan. Nếu cần phê duyệt chính thức, vẫn phải thực hiện xác nhận theo quy định, không mặc nhiên coi việc không phản hồi là đồng ý.

#### 6.3.3. Trao đổi nhanh

- **Mục đích:** Giải quyết các câu hỏi ngắn, cập nhật công việc hằng ngày và xử lý các vướng mắc không cần tổ chức cuộc họp chính thức.
- **Phạm vi sử dụng:** Trao đổi giữa BA và đại diện kho để làm rõ nghiệp vụ; giữa các thành viên phát triển để phối hợp xử lý lỗi; giữa nhóm kỹ thuật và nhóm triển khai để giải quyết vấn đề tại kho.
- **Cách thực hiện:** Nội dung trao đổi cần nêu rõ vấn đề, bối cảnh và thông tin cần hỗ trợ. Với vấn đề kỹ thuật, nên kèm thông báo lỗi, ảnh chụp màn hình, bước tái hiện hoặc dữ liệu liên quan nếu có.
- **Quy định về quyết định:** Các trao đổi nhanh chỉ là phương tiện phối hợp. Nếu nội dung làm thay đổi yêu cầu đã thống nhất, thiết kế, phạm vi, tiến độ hoặc tiêu chí nghiệm thu, người phát hiện phải thông báo PM và cập nhật nội dung vào tài liệu hoặc công cụ theo dõi phù hợp.
- **Xử lý vấn đề chưa giải quyết:** Nếu các bên không thống nhất hoặc vấn đề vượt quá thẩm quyền, chuyển đến người phụ trách chuyên môn hoặc PM để xem xét, tránh trao đổi kéo dài mà không có kết luận.

#### 6.3.4. Công cụ quản lý công việc và vấn đề

- **Mục đích:** Theo dõi tiến độ công việc, lỗi phần mềm, yêu cầu cần xử lý và các vấn đề ảnh hưởng đến dự án.
- **Người cập nhật:** Thành viên được giao nhiệm vụ cập nhật trạng thái công việc của mình; QA/QC ghi nhận và theo dõi lỗi kiểm thử; Tech Lead điều phối các vấn đề kỹ thuật; PM theo dõi tình trạng tổng thể.
- **Thông tin tối thiểu:** Mỗi mục theo dõi cần có mã hoặc tên nhận diện, mô tả, mức độ ưu tiên, người phụ trách, trạng thái và thời hạn xử lý nếu có. Đối với lỗi, bổ sung bước tái hiện, kết quả thực tế, kết quả mong đợi và bằng chứng liên quan khi phù hợp.
- **Quy trình cập nhật:** Khi phát sinh công việc hoặc lỗi, người phát hiện tạo mục theo dõi hoặc thông báo người phụ trách cập nhật. Người được giao xử lý cập nhật tiến độ và kết quả; QA/QC kiểm tra lại lỗi sau khi sửa.
- **Theo dõi quá hạn:** Người phụ trách phải thông báo nguyên nhân chậm và thời gian dự kiến hoàn thành. PM xem xét các mục chậm hoặc có ảnh hưởng đến mốc bàn giao để điều phối xử lý.
- **Lưu ý:** Công cụ cụ thể chưa được xác định trong tài liệu dự án; cần thống nhất một công cụ dùng chung, tránh quản lý phân tán qua nhiều bảng hoặc tin nhắn riêng lẻ.

#### 6.3.5. Kho lưu trữ tài liệu chung

- **Mục đích:** Quản lý tập trung tài liệu dự án, bảo đảm các thành viên sử dụng đúng phiên bản và có thể tra cứu lại khi cần.
- **Phạm vi tài liệu:** Bao gồm tài liệu yêu cầu nghiệp vụ và SRS, tài liệu thiết kế, sơ đồ hệ thống, mã hoặc tài liệu kỹ thuật cần chia sẻ, kế hoạch và kết quả kiểm thử, tài liệu đào tạo, biên bản họp, tài liệu nghiệm thu và bàn giao.
- **Quy tắc đặt tên:** Tên tài liệu cần thể hiện nội dung, phiên bản hoặc ngày cập nhật khi phù hợp. Ví dụ: `SRS_WMS_v1.0`, `Bien_ban_UAT_Kho_chinh_YYYYMMDD`.
- **Quản lý phiên bản:** Người phụ trách tài liệu cập nhật phiên bản mới khi có thay đổi, ghi rõ nội dung thay đổi và thời điểm cập nhật. Không ghi đè hoặc phát tán phiên bản mới theo cách khiến các thành viên không phân biệt được tài liệu đang có hiệu lực.
- **Phân quyền:** Chỉ những người có trách nhiệm mới được chỉnh sửa hoặc phê duyệt tài liệu tương ứng. Các tài liệu chính thức đã được phê duyệt cần được bảo toàn để phục vụ đối chiếu.
- **Lưu trữ và truy xuất:** Biên bản, quyết định và tài liệu quan trọng phải được lưu cùng các tài liệu liên quan. Khi có tranh chấp về yêu cầu hoặc quyết định, ưu tiên đối chiếu phiên bản đã được xác nhận chính thức.

#### 6.3.6. Thông tin cần phê duyệt và xử lý thay đổi

- **Xác định thẩm quyền:** Mỗi nội dung cần phê duyệt phải được gửi đến đúng người có thẩm quyền. Đại diện chủ đầu tư xử lý các quyết định thuộc phía chủ đầu tư; đại diện đơn vị triển khai xử lý các vấn đề thuộc trách nhiệm đơn vị triển khai; PM điều phối và theo dõi quá trình.
- **Phân biệt trao đổi và phê duyệt:** Ý kiến trong cuộc họp hoặc tin nhắn nhanh chỉ được xem là kết luận chính thức khi đã được xác nhận theo hình thức phù hợp với loại quyết định. Không tự suy diễn rằng im lặng đồng nghĩa với đồng ý.
- **Quản lý thay đổi yêu cầu:** Khi phát sinh đề xuất thay đổi, người đề xuất phải nêu lý do, nội dung thay đổi và ảnh hưởng dự kiến. BA phối hợp với nhóm kỹ thuật đánh giá ảnh hưởng đến nghiệp vụ và hệ thống; PM điều phối việc xem xét, trình cấp có thẩm quyền quyết định theo quy trình quản lý thay đổi của dự án.
- **Theo dõi quyết định:** Ghi nhận nội dung đề xuất, người đề xuất, kết quả xem xét, người phê duyệt, thời điểm quyết định và các tài liệu bị ảnh hưởng.
- **Thông báo sau phê duyệt:** Người phụ trách phải thông báo kết quả đến các nhóm chịu ảnh hưởng, cập nhật tài liệu liên quan và bảo đảm các thành viên sử dụng nội dung đã được thống nhất.
- **Trường hợp khẩn cấp:** Nếu vấn đề có thể ảnh hưởng đến dữ liệu kho, thiết bị hoặc hoạt động vận hành, người phát hiện phải thông báo ngay cho PM và người phụ trách kỹ thuật. Việc xử lý khẩn cấp vẫn cần được ghi nhận để kiểm tra và hoàn thiện hồ sơ sau đó.

## 7. Tần suất, thời điểm và trách nhiệm giao tiếp

### 7.1. Nguyên tắc xác định tần suất

- **Thông tin điều hành:** cập nhật định kỳ để PM nắm được tiến độ, rủi ro và các vấn đề tồn đọng.
- **Thông tin phát triển và kỹ thuật:** cập nhật thường xuyên theo tiến độ thực hiện, đặc biệt khi có trở ngại hoặc phụ thuộc giữa các nhóm.
- **Thông tin nghiệp vụ:** trao đổi khi khảo sát, làm rõ yêu cầu, rà soát tài liệu và khi có thay đổi ảnh hưởng đến quy trình kho.
- **Thông tin kiểm thử và triển khai:** cập nhật theo từng đợt kiểm thử, nghiệm thu và mốc triển khai tại kho.
- **Thông tin khẩn cấp:** thông báo ngay khi phát hiện sự cố có thể ảnh hưởng đến dữ liệu, thiết bị, hoạt động kho hoặc mốc bàn giao; không chờ đến kỳ báo cáo tiếp theo.

### 7.2. Kế hoạch trao đổi thông tin

| Nội dung thông tin | Người gửi / chịu trách nhiệm | Người nhận chính | Thời điểm / tần suất đề xuất |
|---|---|---|---|
| 1. Báo cáo tình trạng và tiến độ tổng thể | PM | Đại diện chủ đầu tư, đại diện đơn vị triển khai | Hằng tuần và khi có vấn đề ảnh hưởng đáng kể đến dự án |
| 2. Yêu cầu nghiệp vụ kho | BA phối hợp với đại diện kho | Tech Lead, nhóm phát triển, PM | Khi khảo sát, khi cần làm rõ và khi có yêu cầu thay đổi |
| 3. Tài liệu SRS và nội dung cần xác nhận | BA | PM, đại diện kho, Tech Lead | Khi phát hành bản dự thảo, khi cập nhật phiên bản và trước khi chuyển sang giai đoạn phát triển liên quan |
| 4. Kiến trúc, cơ sở dữ liệu và thiết kế API | Tech Lead và thành viên chuyên môn phụ trách | Nhóm phát triển, QA/QC, PM khi cần | Khi hoàn thành bản thiết kế, khi có thay đổi quan trọng và trước khi triển khai thiết kế liên quan |
| 5. Tiến độ phát triển và vấn đề kỹ thuật | Thành viên phát triển; Tech Lead tổng hợp | PM, các thành viên liên quan | Cập nhật theo ngày làm việc; báo ngay khi có trở ngại ảnh hưởng đến tiến độ |
| 6. Thông số, lịch giao và khả năng kết nối thiết bị | Đại diện nhà cung cấp thiết bị và Hardware/IoT | Tech Lead, PM, Deployment/Onsite | Khi xác nhận yêu cầu thiết bị, trước khi tích hợp và khi phát sinh vấn đề |
| 7. Dữ liệu trà, thông tin lô và chứng từ | Nhà cung cấp trà, phối hợp với đại diện kho | BA và nhóm kỹ thuật liên quan | Khi chuẩn bị dữ liệu mẫu, khi kiểm tra quy trình nhập kho và khi dữ liệu thay đổi |
| 8. Kế hoạch kiểm thử, lỗi và kết quả kiểm thử | QA/QC | PM, Tech Lead, nhóm chịu trách nhiệm xử lý | Khi bắt đầu mỗi đợt kiểm thử; cập nhật lỗi khi phát sinh và tổng hợp khi kết thúc đợt |
| 9. Kết quả UAT và phản hồi người dùng | QA/QC phối hợp với đại diện kho | PM, BA, Tech Lead và nhóm kỹ thuật | Trong từng đợt UAT, khi phát sinh vấn đề và trước khi xem xét nghiệm thu |
| 10. Lịch triển khai và mức độ sẵn sàng tại kho | Deployment/Onsite phối hợp với Hardware/IoT | PM, đại diện kho, Tech Lead | Trước mỗi đợt triển khai; cập nhật khi lịch hoặc điều kiện triển khai thay đổi |
| 11. Tài liệu hướng dẫn và đào tạo | BA và Deployment/Onsite | Đại diện kho và người dùng | Trước các buổi đào tạo, trước khi đưa hệ thống vào vận hành và khi tài liệu được cập nhật |
| 12. Nghiệm thu, bàn giao và vấn đề tồn đọng | PM phối hợp với QA/QC và nhóm kỹ thuật | Đại diện chủ đầu tư, đại diện đơn vị triển khai, đại diện kho | Tại các mốc nghiệm thu, bàn giao và khi cần xác nhận xử lý các vấn đề còn lại |

**Lưu ý:** Tần suất hằng tuần hoặc hằng ngày cần được nhóm thống nhất với các bên liên quan trước khi áp dụng chính thức.

### 7.3. Trách nhiệm trao đổi và phản hồi

Để bảo đảm thông tin được tiếp nhận và xử lý đúng hạn, quy định trách nhiệm như sau:

1. **Người gửi:** Nêu rõ vấn đề, thông tin cần cung cấp, người cần phản hồi và thời hạn mong muốn. Với yêu cầu quan trọng, phải gửi kèm tài liệu hoặc bằng chứng liên quan.
2. **Người nhận:** Xác nhận đã tiếp nhận; nếu chưa đủ thông tin thì yêu cầu bổ sung, nếu chưa thể xử lý đúng hạn thì thông báo lý do và thời điểm dự kiến phản hồi.
3. **Người phụ trách chuyên môn:** Trực tiếp giải quyết vấn đề thuộc phạm vi phụ trách. Ví dụ, BA xử lý thắc mắc nghiệp vụ; Tech Lead điều phối vấn đề kỹ thuật; QA/QC theo dõi lỗi kiểm thử.
4. **PM:** Theo dõi các yêu cầu chưa được phản hồi, công việc bị chậm và vấn đề ảnh hưởng đến tiến độ. PM nhắc người phụ trách, điều phối các bên liên quan hoặc chuyển vấn đề đến người có thẩm quyền quyết định.
5. **Người ghi nhận kết quả:** Cập nhật kết luận, người thực hiện, thời hạn hoàn thành và trạng thái xử lý vào công cụ theo dõi hoặc tài liệu chung của dự án.

Thời hạn phản hồi cụ thể sẽ được các bên thống nhất theo mức độ ưu tiên. Vấn đề khẩn cấp ảnh hưởng đến dữ liệu, thiết bị hoặc hoạt động kho phải được thông báo ngay, không chờ đến kỳ báo cáo.

### 7.4. Xử lý thông tin chậm, thiếu hoặc không thống nhất

- **Không nhận được phản hồi:** Người gửi nhắc lại yêu cầu và nêu rõ thời hạn cần phản hồi. Nếu tiếp tục chậm hoặc ảnh hưởng đến công việc tiếp theo, người gửi báo PM để đôn đốc và điều phối.
- **Thông tin chưa đầy đủ:** Người nhận chỉ rõ dữ liệu hoặc tài liệu còn thiếu và yêu cầu bổ sung. Người phụ trách chưa đưa ra kết luận cuối cùng khi thông tin cần thiết chưa được cung cấp.
- **Thông tin mâu thuẫn:** Các bên đối chiếu tài liệu và phiên bản đã được xác nhận. Nếu vẫn chưa thống nhất, PM tập hợp các bên liên quan để làm rõ; vấn đề vượt thẩm quyền được chuyển đến người có quyền quyết định.
- **Thông tin thay đổi:** Người đề xuất nêu nội dung và lý do thay đổi. BA và nhóm kỹ thuật đánh giá ảnh hưởng khi liên quan đến yêu cầu hoặc thiết kế; PM điều phối việc xem xét và trình phê duyệt theo thẩm quyền. Sau khi được chấp thuận, người phụ trách cập nhật tài liệu và thông báo cho các nhóm bị ảnh hưởng.
- **Sự cố khẩn cấp:** Người phát hiện thông báo ngay cho PM và người phụ trách chuyên môn, nêu rõ sự cố, mức độ ảnh hưởng và hỗ trợ cần thiết. Người được giao xử lý cập nhật tiến độ, kết quả và biện pháp khắc phục; PM theo dõi đến khi sự cố được giải quyết hoặc có phương án kiểm soát phù hợp.

## 8. Luồng thông tin và ma trận truyền thông

### 8.1. Nguyên tắc xây dựng ma trận

- Mỗi dòng tương ứng với một loại thông tin hoặc hoạt động truyền thông cụ thể.
- Xác định rõ người chịu trách nhiệm gửi, đối tượng nhận và mục đích trao đổi.
- Ghi rõ kênh giao tiếp, thời điểm hoặc tần suất và hình thức lưu lại kết quả.
- Với thông tin cần phê duyệt, phải xác định đúng người có thẩm quyền và lưu lại bằng chứng xác nhận.
- Với sự cố hoặc thông tin khẩn cấp, sử dụng kênh thông báo trực tiếp và cập nhật kết quả xử lý vào nơi theo dõi chung.

Các quy định này thống nhất với nhu cầu thông tin và vai trò của các bên tham gia dự án WMS.

### 8.2. Ma trận truyền thông dự án WMS

| STT | Nội dung thông tin | Người gửi | Người nhận | Kênh giao tiếp | Thời điểm / tần suất | Hồ sơ lưu lại |
|---:|---|---|---|---|---|---|
| 1 | Báo cáo tiến độ, rủi ro và vấn đề tồn đọng | PM | Đại diện chủ đầu tư, đại diện đơn vị triển khai | Báo cáo, email, họp | Hằng tuần; khi có vấn đề quan trọng | Báo cáo tiến độ, biên bản họp |
| 2 | Yêu cầu nghiệp vụ kho | BA, đại diện kho | Tech Lead, nhóm phát triển, PM | Phỏng vấn, họp, tài liệu | Khi khảo sát và khi cần làm rõ yêu cầu | Biên bản khảo sát, tài liệu yêu cầu |
| 3 | SRS và nội dung cần xác nhận | BA | PM, đại diện kho, Tech Lead | Tài liệu, email, họp rà soát | Khi phát hành hoặc cập nhật tài liệu | SRS, phản hồi xác nhận |
| 4 | Kiến trúc, cơ sở dữ liệu, thiết kế API | Tech Lead, thành viên chuyên môn | Nhóm phát triển, QA/QC, PM khi cần | Tài liệu thiết kế, sơ đồ, họp kỹ thuật | Khi hoàn thành hoặc thay đổi thiết kế quan trọng | Tài liệu thiết kế, lịch sử thay đổi |
| 5 | Tiến độ phát triển và vấn đề kỹ thuật | Thành viên phát triển, Tech Lead tổng hợp | PM, thành viên liên quan | Công cụ quản lý công việc, trao đổi nhóm | Cập nhật theo ngày làm việc; báo ngay khi có trở ngại quan trọng | Trạng thái công việc, bản ghi vấn đề |
| 6 | Thông số thiết bị, lịch giao và khả năng kết nối | Nhà cung cấp thiết bị, Hardware/IoT | Tech Lead, PM, Deployment/Onsite | Email, tài liệu kỹ thuật, họp tích hợp | Khi xác nhận thiết bị, trước tích hợp và khi có vấn đề | Thông số kỹ thuật, kết quả kiểm tra |
| 7 | Dữ liệu trà, thông tin lô và chứng từ | Nhà cung cấp trà, đại diện kho | BA, nhóm kỹ thuật liên quan | Biểu mẫu, chứng từ, trao đổi trực tiếp | Khi chuẩn bị dữ liệu và kiểm tra quy trình nhập kho | Bộ dữ liệu mẫu, chứng từ liên quan |
| 8 | Kế hoạch kiểm thử, lỗi và kết quả kiểm thử | QA/QC | PM, Tech Lead, nhóm xử lý lỗi | Công cụ theo dõi lỗi, báo cáo kiểm thử | Theo từng đợt kiểm thử; cập nhật lỗi khi phát sinh | Kế hoạch kiểm thử, danh sách lỗi, báo cáo kết quả |
| 9 | Kết quả UAT và phản hồi người dùng | QA/QC, đại diện kho | PM, BA, Tech Lead, nhóm kỹ thuật | Biểu mẫu UAT, họp đánh giá | Trong mỗi đợt UAT và trước nghiệm thu | Biên bản UAT, danh sách vấn đề |
| 10 | Lịch triển khai và mức độ sẵn sàng tại kho | Deployment/Onsite, Hardware/IoT | PM, đại diện kho, Tech Lead | Kế hoạch triển khai, checklist, họp | Trước mỗi đợt triển khai và khi lịch thay đổi | Kế hoạch, checklist sẵn sàng |
| 11 | Tài liệu hướng dẫn và đào tạo | BA, Deployment/Onsite | Đại diện kho, người dùng | Tài liệu hướng dẫn, đào tạo trực tiếp | Trước đào tạo và trước khi vận hành | Tài liệu hướng dẫn, ghi nhận đào tạo |
| 12 | Nghiệm thu, bàn giao và vấn đề còn tồn đọng | PM phối hợp QA/QC và nhóm kỹ thuật | Đại diện chủ đầu tư, đại diện đơn vị triển khai, đại diện kho | Biên bản, tài liệu bàn giao, email xác nhận | Tại các mốc nghiệm thu và bàn giao | Biên bản nghiệm thu, hồ sơ bàn giao, danh sách tồn đọng |

**Lưu ý:** Tần suất, kênh và công cụ giao tiếp cần được nhóm thống nhất trước khi áp dụng chính thức.

### 8.3. Luồng xử lý thông tin

Quy trình trao đổi thông tin chung được đề xuất như sau:

1. **Phát sinh nhu cầu thông tin:** Có yêu cầu nghiệp vụ, công việc, lỗi hoặc quyết định cần trao đổi.
2. **Xác định người gửi và người nhận:** Chọn đúng người phụ trách và người có thẩm quyền nếu cần phê duyệt.
3. **Gửi thông tin qua kênh phù hợp:** Sử dụng email, họp, tài liệu, công cụ theo dõi hoặc thông báo trực tiếp.
4. **Tiếp nhận và xử lý:** Người nhận xác nhận, bổ sung thông tin, giải quyết vấn đề hoặc trình phê duyệt.
5. **Ghi nhận kết quả và theo dõi:** Lưu kết luận, cập nhật trạng thái và thông báo cho các bên chịu ảnh hưởng.

Nếu thông tin thiếu, chưa được phản hồi hoặc có mâu thuẫn, áp dụng quy định tại mục 7.4. Nếu vấn đề ảnh hưởng đến tiến độ hoặc vượt thẩm quyền, chuyển PM hoặc người có thẩm quyền xử lý.

### 8.4. Quản lý và cập nhật ma trận truyền thông

- **Người chịu trách nhiệm:** PM quản lý phiên bản chung của ma trận truyền thông.
- **Thời điểm cập nhật:** Khi thay đổi nhân sự, vai trò, nhu cầu thông tin, kênh giao tiếp hoặc kế hoạch triển khai.
- **Cách cập nhật:** Người phát hiện thay đổi thông báo PM; PM phối hợp với các bên liên quan xem xét và cập nhật ma trận.
- **Thông báo phiên bản mới:** Sau khi cập nhật, PM thông báo cho các thành viên chịu ảnh hưởng để sử dụng cùng một phiên bản.
- **Lưu trữ:** Lưu ma trận hiện hành và các phiên bản cần thiết để đối chiếu trong kho tài liệu chung của dự án.
