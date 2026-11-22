# CHƯƠNG 4. QUẢN LÝ CHI PHÍ DỰ ÁN

**Dự án:** Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS).  
**Nhóm 16. Người phụ trách chương:** Nguyễn Tuấn Dũng.  
**PM dự án giả định:** Bùi Hồng Phú. **Đơn vị thực hiện:** Công ty Cổ phần Công nghệ Raumania.  
**Phiên bản:** 22/11/2026, đối chiếu repo tại commit `bc0593ccee1778c269bc924496b839e8bf28a74c`.

Chương này trình bày kế hoạch quản lý chi phí, cơ sở ước lượng, phân bổ ngân sách và cách kiểm soát cho dự án một kho tổng và hai kho chi nhánh. Kết quả là **phương án kế hoạch**, chưa phải đường cơ sở đã được chủ đầu tư phê duyệt. Bảng tính kèm theo giữ nguyên tổng kinh phí 2 tỷ đồng của bộ tài liệu gốc và làm rõ phần chi phí chưa thể gán đủ vào hoạt động trong lịch hiện hành.

## 4.1. Căn cứ và giới hạn

### 4.1.1. Nguồn đối chiếu

| Nguồn | Dữ liệu sử dụng |
| --- | --- |
| [01. Mô tả đề tài](01-mo-ta-de-tai.md), [02. Dự toán kinh phí](02-du-toan-kinh-phi.md), [03. Tôn chỉ](03-ton-chi-du-an.md), [04. Tôn chỉ đầy đủ](04-ton-chi-du-an-day-du.md) | Phạm vi ba kho, ngân sách, lương, thiết bị, thời hạn và thẩm quyền. |
| [Báo cáo quản lý phạm vi](BÁO%20CÁO%20QUẢN%20LÝ%20PHẠM%20VI%20DỰ%20ÁN.md) | 45 gói WBS lá, đầu ra, yêu cầu và kiểm soát thay đổi. |
| [Chương 3. Quản lý thời gian](CHUONG-3-QUAN-LY-THOI-GIAN.md), [dữ liệu lịch](chuong-3/du-lieu-lich.json), [kết quả lịch](chuong-3/ket-qua-lich.json) | Hoạt động, vai trò, tải, kỳ và ngày thực hiện đề xuất. |
| [Kế hoạch quản lý nhân lực](Kế%20hoạch%20quản%20lý%20nhân%20lực.md) | Tám vị trí, 50 người-tháng (MM), lịch huy động và bàn giao trách nhiệm. |
| [Bài giảng Quản lý chi phí](tai-lieu/6-cost.pdf), ThS. Ngô Tiến Đức | Trang 9: nội dung kế hoạch; trang 11, 19-21: cơ sở ước lượng; trang 22-24: ngân sách; trang 25-30: kiểm soát; trang 31: bài tập. |

Slide thuyết trình *Quản lý Chi phí Dự án Phần mềm - Nhóm 3* được dùng để tham khảo phương pháp, không thay số liệu của dự án kho trà hoặc yêu cầu trực tiếp của giảng viên. Không có dòng lợi ích kinh tế, mức chiết khấu hoặc dữ liệu định cỡ phần mềm đã xác nhận để tính NPV, ROI, LOC hay Function Points cho dự án này.

Bốn thành viên làm bài tập được phân công theo [N-03](N-03-phan-cong-va-quyet-dinh.md). Đây là phân công học tập, khác với tám vị trí của đội triển khai giả định. Phạm vi, thời gian, chi phí và nhân lực là bốn nội dung quản lý liên quan với nhau, không phải bốn pha tuần tự.

### 4.1.2. Khoản thuộc ngân sách

Ngân sách bao gồm lương theo kỳ huy động, thiết bị mua mới, môi trường phát triển/kiểm thử/vận hành trong tám tháng, công tác hiện trường và 143 triệu đồng dự phòng rủi ro. Công quản lý, tài liệu, đào tạo và kiểm thử thuộc đội nhân sự đã dự toán, không được cộng thêm một lần lương khác.

Máy chấm công và thiết bị đo do doanh nghiệp cung cấp phải được kiểm tra khi khảo sát. Không ghi chúng thành khoản mua mới trong 130 triệu đồng. Phương án đo không dây hoặc chức năng ngoài phạm vi cần được thẩm định bằng yêu cầu thay đổi. Phí duy trì sau bàn giao và bảo trì dài hạn được tiếp nhận/thỏa thuận riêng theo tôn chỉ.

## 4.2. Kế hoạch quản lý chi phí

### 4.2.1. Sáu quy định của kế hoạch

Các quy định dưới đây cụ thể hóa nội dung tại trang 9 của bài giảng. Các ngưỡng quản trị là đề xuất của kế hoạch này, cần được phê duyệt cùng đường cơ sở.

| Nội dung | Quy định áp dụng |
| --- | --- |
| Đơn vị đo | Ngân sách và chi phí: VNĐ. Bảng trình bày có thể dùng triệu VNĐ và ghi rõ đơn vị. Huy động nhân sự: MM. Nỗ lực lịch: ngày công theo lịch tám giờ/ngày đã nêu ở chương 3. |
| Độ chính xác và làm tròn | Tính trên số gốc, giữ phần thập phân trong phân bổ; trình bày tiền đến 1 VNĐ, MM đến 4 chữ số nếu cần. Sai lệch tổng do làm tròn hiển thị phải được giải thích. Độ chính xác trình bày không chứng minh sai số ước lượng. |
| Tài khoản kiểm soát | CA-11 đến CA-16 tương ứng nhóm WBS 1.1 đến 1.6. Mỗi khoản có mã gói, loại chi và kỳ. Lương huy động chưa gán hoạt động được đối chiếu riêng, không tạo thêm WBS để làm đầy ngân sách. |
| Ngưỡng kiểm soát | Xem xét mọi chênh lệch bất lợi; ưu tiên xử lý khi CPI hoặc SPI <0,95 trong một kỳ hoặc <1 trong hai kỳ liên tiếp. Báo ngay khi EAC vượt ngân sách tương ứng, cam kết chưa được phép hoặc có nguy cơ trễ mốc kho tổng. |
| Quy tắc đo | PV theo ngân sách công việc được duyệt; EV theo đầu ra có bằng chứng; AC theo chi phí đã phát sinh có căn cứ, kể cả chưa trả tiền. Gói ngắn có thể dùng 0/100; gói dài dùng mốc có trọng số chốt trước; công định kỳ dùng mức nỗ lực của kỳ. |
| Hình thức báo cáo | Cập nhật công việc, chi phí và cam kết hàng tuần. Báo cáo chủ đầu tư cuối tháng lịch theo WBS 1.1.2.3; chốt bổ sung ngày 02 để đối chiếu tháng dự án. Báo cáo nêu ngày trạng thái, phiên bản, PV/EV/AC, dự báo, quỹ dự phòng, nguyên nhân và hành động. |

Không dùng số tiền giải ngân, thời gian đã trôi qua hoặc giờ đã làm thay cho tỷ lệ hoàn thành đầu ra. Việc trả tiền mua hàng không tự làm cho gói lắp đặt và nghiệm thu hoàn thành.

### 4.2.2. Trách nhiệm và phê duyệt

PM tổng hợp dự toán, kiểm tra kỳ huy động và lịch, theo dõi phát sinh, dự báo phần còn lại và trình thay đổi. Tech Lead cùng người phụ trách chuyên môn kiểm tra khối lượng, giả định phân bổ và ước lượng lại. QA và đầu mối nghiệm thu cung cấp bằng chứng đầu ra. Onsite/đầu mối mua sắm cung cấp hồ sơ thiết bị, công tác và nghĩa vụ thanh toán. Chủ đầu tư phê duyệt đường cơ sở và thay đổi trong thẩm quyền tôn chỉ; chưa có hạn mức ủy quyền riêng thì sử dụng dự phòng phải được trình xác nhận.

## 4.3. Phương pháp và cơ sở ước lượng

### 4.3.1. Các phương pháp và cách lựa chọn

| Phương pháp | Cách dùng trong dự án |
| --- | --- |
| Theo nguồn lực/định mức | Phương pháp chính: MM huy động × lương tháng; số lượng thiết bị × đơn giá; dịch vụ/công tác theo hạn mức ở tài liệu 02. |
| Từ dưới lên | Tổng hợp khoản chi đã truy vết tới hoạt động/WBS, đối chiếu ngược ngân sách gốc. Phần lương chưa gán cho hoạt động vẫn để rõ; việc chia sẵn ngân sách không phải một kiểm chứng bottom-up độc lập về tính đủ. |
| Tương tự | Chỉ áp dụng khi có dự án so sánh, mức điều chỉnh và nguồn kiểm chứng; hiện chưa có dữ liệu này. |
| Theo tham số, LOC, FP, COCOMO | Cần kích thước và năng suất/đơn giá có căn cứ; chưa dùng để tạo thêm một tổng dự toán cho WMS. |
| Ba điểm/PERT | Có thể dùng khi ước lượng lại khoản bất định và có ba điểm phù hợp. Không lấy PERT thời lượng ở chương 3 nhân thành chi phí mà bỏ qua kỳ huy động cố định. |
| Từ trên xuống | Tổng 2 tỷ là ràng buộc cần đối chiếu, không chứng minh chi phí từng gói đã được ước lượng đủ. |

### 4.3.2. Lương huy động và nỗ lực của lịch

| Vai trò | Lương/tháng (triệu VNĐ) | Kỳ huy động | MM | Tổng lương (triệu VNĐ) |
| --- | ---: | --- | ---: | ---: |
| PM | 50 | T1-T8 | 8 | 400 |
| Tech Lead | 50 | T1-T8 | 8 | 400 |
| Kỹ sư RS232 | 32 | T2-T7 | 6 | 192 |
| BA | 30 | T1-T5 | 5 | 150 |
| Backend | 27 | T2-T8 | 7 | 189 |
| Frontend | 24 | T2-T7 | 6 | 144 |
| QA/QC | 20 | T3-T8 | 6 | 120 |
| Onsite | 18 | T5-T8 | 4 | 72 |
| **Tổng** | | | **50** | **1.667** |

Nguồn: tài liệu 02, mục II; kế hoạch nhân lực. Không đổi lương hoặc thu hẹp kỳ huy động chỉ vì lịch đề xuất hoàn thành sớm hơn hạn.

Chương 3 hiện ghi nhận **341,3 ngày công trên 1.053 ngày khả dụng**. Đây là nỗ lực của các hoạt động/LoE đã liệt kê, chưa phân rã đủ 50 MM huy động. Bảng tính dùng quy ước phân bổ sau để nhìn rõ hai lớp số liệu:

`Lương quy thuộc hoạt động trong kỳ = Lương tháng × Ngày công mô hình trong kỳ / Ngày làm việc khả dụng của chính kỳ đó`.

`Lương huy động chưa gán hoạt động = Lương huy động toàn kỳ - Lương quy thuộc hoạt động`.

Theo lịch hiện hành, hai phần lần lượt khoảng **509,996 triệu** và **1.157,004 triệu VNĐ**, tổng vẫn **1.667 triệu VNĐ**. Phép phân bổ này là giả định kế hoạch, không phải đơn giá trả lương theo ngày hoặc quyết định giảm ngân sách. Phần chưa gán không phải tiết kiệm, dự phòng hoặc công việc đã hoàn thành. Nhóm cần làm rõ công phối hợp/hỗ trợ, độ chi tiết hoạt động và phương thức huy động trước khi khóa ngân sách gói.

Hoạt động gắn nhiều WBS được chia đều phần công giữa các mã khi lập bảng phân bổ đề xuất, không nhân nguyên chi phí cho từng mã. Phụ lục và bảng tính giữ giả định này để nhóm có thể thay bằng tỷ lệ có căn cứ.

### 4.3.3. Giả định, biến động và hiệu lực

Đơn giá lương, thiết bị và hạn mức dịch vụ/công tác được kế thừa tài liệu 02; chưa được coi là báo giá thương mại còn hiệu lực. Mua thiết bị theo ba đợt, khách hàng cung cấp đủ tài sản/hạ tầng đã nêu và lịch nghỉ trong chương 3 đều là giả định cần xác nhận. Lương gross chưa đủ để kết luận đã bao gồm mọi khoản ngoài lương, thuế/phí hoặc chi phí chung của bên thực hiện.

Phiên bản này dùng để đối chiếu nội bộ từ **22/11/2026 đến 22/12/2026**, là thời hạn rà soát đề xuất. Phải rà soát sớm hơn nếu thay phạm vi, lịch, huy động hoặc đơn giá; xác nhận lại giá khi chốt dự toán và trước đặt mua trong năm 2027. Hiệu lực báo giá/hợp đồng tuân theo tài liệu của nhà cung cấp. Chưa có cơ sở thống kê để cam kết một khoảng sai số dự toán.

Phân tích nhạy cảm minh họa, giữ nguyên các yếu tố khác: lương tăng 5% làm tăng 83,35 triệu; tăng 10% làm tăng 166,70 triệu, lớn hơn quỹ dự phòng 143 triệu là 23,70 triệu; thiết bị tăng 10% làm tăng 13 triệu VNĐ. Đây là phép thử tác động, không phải xác suất, khoảng tin cậy hay quyền tự động dùng quỹ.

## 4.4. Tổng dự toán và phân bổ ngân sách

### 4.4.1. Cơ cấu tổng kinh phí

| Hạng mục | Triệu VNĐ | Tỷ trọng tổng ngân sách |
| --- | ---: | ---: |
| Nhân sự trực tiếp theo kỳ huy động | 1.667 | 83,35% |
| Thiết bị mua mới cho ba kho | 130 | 6,50% |
| Hạ tầng, cloud, bản quyền trong tám tháng | 25 | 1,25% |
| Công tác và triển khai hiện trường | 35 | 1,75% |
| **Cộng trước dự phòng** | **1.857** | **92,85%** |
| Contingency reserve theo bộ gốc | 143 | 7,15% |
| **Tổng kinh phí/BAC theo tài liệu 02** | **2.000** | **100,00%** |

Tài liệu gốc không lập management reserve riêng. Giữ 143 triệu contingency trong tổng 2 tỷ, không đổi tên quỹ, trừ khỏi BAC gốc hoặc cộng thêm lần thứ hai. Việc tài liệu 02 gọi tổng này là BAC không đồng nghĩa đường PV đầy đủ đã được phê duyệt.

### 4.4.2. Thiết bị và khoản ngoài lương

Kho tổng có hai cân, hai máy in, bốn máy quét và hai PC, tổng 70 triệu đồng. Mỗi chi nhánh có một cân, một máy in, hai máy quét và một PC; hai chi nhánh có thêm khoản vật tư mạng/thiết bị chuyển mạch tổng 11 triệu đồng, đưa tổng chi nhánh lên 60 triệu đồng. Toàn dự án giữ bốn cân, bốn máy in, tám máy quét và bốn PC theo tài liệu 02. Cáp/bộ chuyển RS232, tem/mực và giấy phép máy trạm cần được xác nhận về phạm vi giá, không tự coi đã bao gồm.

Đợt T2 nhận bộ mẫu 33 triệu lấy từ danh mục kho tổng; T5 nhận phần còn lại 37 triệu; T6 nhận 60 triệu thiết bị/vật tư chi nhánh. Bộ mẫu được chuyển ra kho tổng khi triển khai, không mua lần thứ hai. Các khoản này gắn WBS 1.4.1.1 và 1.5.1.1 nhưng tháng nhận hàng có thể sớm hơn tháng lắp đặt. Phải xác nhận thời gian đặt hàng và điều khoản thanh toán trong kế hoạch mua sắm.

Hạ tầng/cloud/bản quyền phân bổ 4 triệu ở T1 và 3 triệu/kỳ T2-T8. Công tác phân bổ T1-T8 lần lượt 3; 0; 0; 2; 9; 8; 9; 4 triệu. Đây là phân bổ kế hoạch theo tài liệu 02, chưa thay thế dự toán chuyến đi hay điều khoản thanh toán.

### 4.4.3. Phân bổ theo tám tháng dự án

Đơn vị: **triệu VNĐ**. T1 từ ngày 03/06/2027 đến hết 02/07/2027; các kỳ sau cùng quy ước ngày 03 đến ngày 02 tháng kế tiếp.

| Kỳ | Từ ngày - đến ngày | Lương | Thiết bị | Hạ tầng | Công tác | Cộng kỳ | Lũy kế |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| T1 | 03/06-02/07/2027 | 130 | 0 | 4 | 3 | 137 | 137 |
| T2 | 03/07-02/08/2027 | 213 | 33 | 3 | 0 | 249 | 386 |
| T3 | 03/08-02/09/2027 | 233 | 0 | 3 | 0 | 236 | 622 |
| T4 | 03/09-02/10/2027 | 233 | 0 | 3 | 2 | 238 | 860 |
| T5 | 03/10-02/11/2027 | 251 | 37 | 3 | 9 | 300 | 1.160 |
| T6 | 03/11-02/12/2027 | 221 | 60 | 3 | 8 | 292 | 1.452 |
| T7 | 03/12/2027-02/01/2028 | 221 | 0 | 3 | 9 | 233 | 1.685 |
| T8 | 03/01-02/02/2028 | 165 | 0 | 3 | 4 | 172 | 1.857 |
| **Tổng** | | **1.667** | **130** | **25** | **35** | **1.857** | |

Ngoài bảng còn **143 triệu dự phòng chưa gán kỳ**. Bảng này bao gồm lương huy động chưa gán hoạt động, nên là bảng phân bổ ngân sách/nhu cầu nguồn tiền sơ bộ; **không dùng nguyên lũy kế này làm PV công việc đã lập lịch hoặc đường PV đầy đủ cho BAC 2 tỷ**. Ngày đến hạn thanh toán còn phụ thuộc hợp đồng. Chưa có thỏa thuận cấp vốn để khẳng định nguồn tiền từng kỳ đã được bảo đảm.

### 4.4.4. Tổng hợp theo tài khoản kiểm soát

| Tài khoản | Nhóm WBS | Nội dung |
| --- | --- | --- |
| CA-11 | 1.1 | Lập kế hoạch, điều phối, kiểm soát, thay đổi và chất lượng quy trình. |
| CA-12 | 1.2 | Khảo sát, yêu cầu, kiến trúc và thiết kế. |
| CA-13 | 1.3 | Phát triển, tích hợp và kiểm thử. |
| CA-14 | 1.4 | Triển khai kho tổng và hỗ trợ sau go-live. |
| CA-15 | 1.5 | Triển khai hai kho chi nhánh. |
| CA-16 | 1.6 | Nghiệm thu, tài liệu và bàn giao. |

`WBS_thang` trong bảng tính tổng hợp 45 gói từ công đã quy thuộc và khoản ngoài lương. Dòng lương chưa gán được giữ riêng để tổng cộng vẫn khớp 1.857 triệu; 143 triệu dự phòng ở bảng riêng. Đây là các cách nhìn của cùng một dự toán, không cộng tổng bảng nguồn lực với tổng bảng WBS.

## 4.5. Dự phòng và điều kiện khóa đường cơ sở

143 triệu là quỹ cố định theo bộ gốc, không phải EMV đã tính từ xác suất và thiệt hại. Hạn mức chia theo nhóm rủi ro trong `Du_phong` là đề xuất, cần đối chiếu Risk Register và giá phương án ứng phó. Khoảng trống năng lực nhân sự đã được trả lương, thời gian dự phòng R2/R3/R51/R52/R6 trong lịch và quỹ tiền 143 triệu là ba khái niệm khác nhau; không cộng chi phí cho cùng phần nhân công hai lần.

Khi có rủi ro: ghi sự kiện/bằng chứng, xác định WBS bị ảnh hưởng, kiểm phần công và tiền đã có, ước lượng chi phí **tăng thêm**, trình người có thẩm quyền và cập nhật hồ sơ. Sử dụng quỹ không tự cho phép mở rộng phạm vi. Theo dõi số đã duyệt, cam kết, phát sinh và còn khả dụng; dự phòng chưa sử dụng không tạo AC hoặc EV.

Trước khi coi đây là đường cơ sở hoàn chỉnh, cần thực hiện đồng bộ:

1. Thẩm định mức nỗ lực/năng suất của chương 3 và làm rõ phần lương huy động chưa gán hoạt động. Quyết định giữ nguyên huy động, bổ sung chi tiết công việc hoặc điều chỉnh huy động phải có hồ sơ tương ứng.
2. Thống nhất tỷ lệ chia hoạt động nhiều WBS, ngân sách từng gói và quy tắc đo giá trị hoàn thành.
3. Xác nhận giá, điều kiện mua hàng, tài sản khách hàng cung cấp và các khoản ngoài lương chưa rõ.
4. Bố trí 143 triệu contingency vào tài khoản/gói kế hoạch và kỳ thích hợp; xác định nguồn cấp vốn, kỳ cần vốn và quyền sử dụng quỹ.
5. Lưu lịch, ngân sách gói theo thời gian, kế hoạch dự phòng, quy tắc đo và quyết định phê duyệt cùng một phiên bản.

Không tự sửa tài liệu 02, lương, lịch huy động hay lịch của thành viên khác để làm số liệu khớp. Các giả định mở được nêu trong hồ sơ chi phí để nhóm xử lý có căn cứ.

## 4.6. Kiểm soát chi phí và EVM

### 4.6.1. Ghi nhận và đo lường

`So_chi_phi` ghi từng sự kiện phát sinh và thanh toán với ngày, WBS, chứng từ, nội dung và số tiền. Thanh toán bổ sung cho nghĩa vụ đã ghi AC phải tham chiếu sự kiện gốc và không ghi AC lần nữa. Khoản ứng trước không tự là chi phí của công việc đã hoàn thành. Cam kết hợp đồng chưa phát sinh cần được theo dõi cùng hồ sơ mua sắm để dự báo đủ phần còn lại.

`Theo_doi` chỉ dùng khi có ngân sách cùng phạm vi đã được duyệt, ngày trạng thái, phiên bản, người xác nhận, dữ liệu đầy đủ và bằng chứng đầu ra. Trường thực hiện chưa có được để trống; số 0 chỉ dùng khi đã xác nhận thực sự bằng 0. Số minh họa ở `EVM` không được chuyển vào báo cáo thực hiện.

### 4.6.2. Công thức và ví dụ độc lập

| Chỉ tiêu | Công thức và ý nghĩa |
| --- | --- |
| PV | Giá trị ngân sách của công việc phải hoàn thành đến ngày trạng thái. |
| EV | Giá trị ngân sách của công việc thực tế đã hoàn thành có bằng chứng. |
| AC | Chi phí thực tế đã phát sinh cho cùng phạm vi và ngày trạng thái. |
| CV; CPI | `CV = EV - AC`; `CPI = EV / AC`, chỉ tính CPI khi AC >0. |
| SV; SPI | `SV = EV - PV`; `SPI = EV / PV`, chỉ tính SPI khi PV >0. SV không phải số ngày trễ. |
| EAC, hiệu suất tiếp diễn | `EAC = AC + (BAC - EV) / CPI`; tương đương `BAC / CPI` khi CPI = EV/AC và mẫu số hợp lệ. |
| EAC, sai lệch một lần | `EAC = AC + BAC - EV`, nếu phần còn lại thực hiện theo ngân sách ban đầu. |
| EAC, ước lượng lại | `EAC = AC + ETC_mới`; ETC mới phải có khối lượng và cơ sở giá. |
| ETC; VAC | `ETC = EAC - AC`; `VAC = BAC - EAC`. |
| TCPI theo BAC | `(BAC - EV) / (BAC - AC)`, khi ngân sách còn lại dương. Không suy diễn một ngưỡng TCPI chung quyết định mọi dự án khả thi hay không. |

Ví dụ **minh họa độc lập**, đơn vị triệu VNĐ: BAC =100, PV =60, EV =50, AC =65. Khi đó CV =-15; SV =-10; CPI ≈0,7692; SPI ≈0,8333. Nếu hiệu suất chi phí tiếp diễn, EAC =130; ETC =65; VAC =-30; TCPI theo BAC ≈1,4286. Dự báo khác cần giả định khác; không tự thay BAC bằng EAC. Đây không phải số thực hiện của dự án WMS và không dùng BAC 2 tỷ chưa có PV đầy đủ để suy ra hiệu quả hiện tại.

Khi tổng hợp nhiều gói, cộng PV/EV/AC cùng phạm vi rồi tính chỉ số; không lấy trung bình CPI hoặc SPI của các gói. Đánh giá ngày hoàn thành cần xem thêm lịch và đường găng, đặc biệt M2 và M5 còn ít khoảng dư.

## 4.7. Thay đổi và bàn giao hồ sơ

Áp dụng quy trình CR của chương phạm vi: **ghi nhận, phân tích ảnh hưởng, phê duyệt, cập nhật và thực hiện**. Phiếu thay đổi phải nêu WBS, khối lượng/nguồn lực, chi phí tăng giảm, nguồn tài trợ, ảnh hưởng mốc và phương án thay thế. Ước lượng lại ETC là đổi dự báo; đổi đường cơ sở cần quyết định riêng. Không điều chỉnh hồi tố để xóa chênh lệch.

Bộ hồ sơ chi phí gồm chương này, [phụ lục phân bổ](05a-thuyet-minh-chi-phi.md), [bảng tính](Bang_tinh_chi_phi_WMS.xlsx), ngân sách đã duyệt khi có, hồ sơ phát sinh, dự báo, dự phòng và CR. Các bảng trình bày trong chương được đối chiếu với bảng tính cùng phiên bản; thay đầu vào phải cập nhật các bảng chịu ảnh hưởng trước khi ghép vào quyển báo cáo.
