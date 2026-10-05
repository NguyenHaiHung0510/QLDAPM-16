# BÁO CÁO QUẢN LÝ PHẠM VI DỰ ÁN (PROJECT SCOPE MANAGEMENT PLAN)

- **Tên dự án:** Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS)
- **Mã bài tập:** Bài tập Nhóm 16 (PTIT)
- **Người quản lý dự án (PM):** Bùi Hồng Phú
- **Nhà tài trợ (Project Sponsor):** Ban Giám đốc Doanh nghiệp / Hợp tác xã Trà Tân Cương (Thái Nguyên)
- **Tổng ngân sách phê duyệt (BAC):** 2.000.000.000 VNĐ (Hai tỷ đồng chẵn)
- **Thời gian thực hiện:** 08 tháng (50 Man-Month / 8 vị trí chuyên môn)
- **Tác giả bản phạm vi/WBS ban đầu:** Nguyễn Đức Công.
- **Căn cứ:** Bộ tài liệu gốc 01–04 và tài liệu tham khảo tại mục Nguồn đối chiếu.

**1\. KẾ HOẠCH QUẢN LÝ PHẠM VI (SCOPE MANAGEMENT PLAN)**

**1.1 Phương pháp thu thập yêu cầu**

Để đảm bảo thu thập đầy đủ yêu cầu nghiệp vụ và kỹ thuật IoT cho 3 kho, nhóm dự án triển khai 3 phương pháp chính:

1. **Phỏng vấn sâu & Khảo sát nghiệp vụ (Interviews):**
   - Làm việc trực tiếp với **6 nhóm người dùng**: Ban Lãnh đạo, Quản lý kho, Thủ kho, Công nhân chế biến/đóng gói, Kế toán kho và Nhân sự logistics/Tài xế.
   - Tập trung làm rõ các quy trình cốt lõi: Nhập chè búp tươi, quy đổi định mức BOM theo độ ẩm, theo dõi tỷ lệ hao hụt chè, kiểm soát vị trí ô/kệ (Zone/Bin/Rack) và quy tắc xuất kho ưu tiên FEFO (First Expired, First Out).
2. **Khảo sát kỹ thuật & Giao thức IoT (Technical & Hardware Survey):**
   - Tháng 1, BA/Tech Lead khảo sát quy trình, tài sản sẵn có và đặc tả nhà cung cấp tại ba kho. RS232 Engineer kiểm trên bộ mẫu từ tháng 2; Onsite khảo sát/lắp đặt từ tháng 5 theo lịch huy động 02.
   - Xác nhận yêu cầu sử dụng/giao thức của **04 cân RS232, 04 máy in, 08 máy quét, 04 PC mua mới** và **03 máy chấm công sẵn có** theo 01/02. Dải cân, độ chia và giao thức của từng loại thiết bị được xác nhận trong SRS theo đặc tả nhà cung cấp.
3. **Rà soát chứng từ & Dữ liệu lịch sử:**
   - Tiếp nhận các biểu mẫu sổ sách Excel hiện có, danh mục nhà vườn/nhà cung cấp, công thức tính hao hụt chế biến và dữ liệu tồn kho ban đầu do doanh nghiệp bàn giao.

**1.2 Quy trình kiểm soát thay đổi phạm vi (Scope Change Control Process)**

Mọi đề xuất thay đổi phạm vi được ghi nhận và xử lý theo bốn bước:

1. **Ghi nhận phiếu CR:** Thành viên hoặc bên liên quan nêu nội dung thay đổi và lý do.
2. **Phân tích tác động:** PM Bùi Hồng Phú phối hợp với Solution Architect đánh giá ảnh hưởng đến yêu cầu, WBS, tiêu chí nghiệm thu, nguồn lực, tiến độ và ngân sách.
3. **Phê duyệt:** Chủ đầu tư phê duyệt thay đổi phạm vi, tiêu chí chấp nhận và đường cơ sở; PM điều phối sửa lỗi và công việc trong phạm vi đã duyệt. Các phương án được đánh giá theo hạn kho tổng vận hành chậm nhất tháng 6, toàn dự án tám tháng và ngân sách hai tỷ.
4. **Cập nhật và thực thi:** Cập nhật RTM, WBS, WBS Dictionary và kế hoạch liên quan; thông báo cho đội dự án. Nguồn chi cho thay đổi được xác định trong kế hoạch chi phí/rủi ro.

**2\. MA TRẬN TRUY XUẤT YÊU CẦU (REQUIREMENTS TRACEABILITY MATRIX - RTM)**

Ma trận truy vết yêu cầu nối yêu cầu trong 01–04 với gói công việc và điều kiện chấp nhận. Tham khảo: Bài giảng Quản lý dự án phần mềm — Quản lý phạm vi dự án, [4-scope.pdf](tai-lieu/4-scope.pdf#page=17), trang 17; PMBOK 6 §5.2.3.2, trang 148–149.

| Mã YC | Loại | Yêu cầu và nguồn | Đối tượng | WBS | Trách nhiệm | Điều kiện chấp nhận |
| --- | --- | --- | --- | --- | --- | --- |
| FR-01 | Chức năng | Nhập/xuất/kiểm kê/điều chuyển giữa ba kho, tự sinh Batch ID, ghi chất lượng lô, vị trí và FEFO; 01 mục nhập–xuất, 04 mục 2 | Thủ kho/quản lý | 1.3.1.1, 1.3.1.2 | Devs/BA | AC-03; xuất ưu tiên lô còn hạn được phép xuất; mã lô không trùng |
| FR-02 | Chức năng | BOM, độ ẩm trà và hao hụt theo công thức đã xác nhận; 01 mục thông tin trà/BOM, 04 mục 2 | Kho/công nhân | 1.3.2.1 | Devs/BA | AC-03; nguồn độ ẩm trà riêng với %RH môi trường |
| FR-03 | Chức năng | Cảnh báo cận hạn/hết hạn, tồn tối thiểu và Aging; 01 mục tồn/bảo quản, 04 mục 2 | Quản lý/lãnh đạo | 1.3.2.2 | Devs | AC-03; kiểm trước/đúng/sau ngưỡng và ngày hết hạn |
| FR-04 | Tích hợp | Đọc cân RS232 theo dải sử dụng được chấp nhận; 01 mục ngoại vi, 02 mục IV, 04 mục 4 | Công nhân/thủ kho | 1.3.3.1, 1.3.5.1 | RS232/QA | AC-01 |
| FR-05 | Tích hợp | In tem/phiếu và quét barcode/QR; 01 mục ngoại vi, 02 mục IV | Công nhân/thủ kho | 1.3.3.2, 1.3.3.3, 1.3.5.2 | RS232/QA | AC-02 và AC-03 |
| FR-06 | Tích hợp | Chấm công từ máy sẵn có; 01 mục nhân sự/giả định, 04 mục 2 | Kho/kế toán | 1.3.3.3 | Devs/RS232 | AC-03; đối soát dữ liệu máy, không nhập trùng |
| FR-07 | Chức năng | Nhà cung cấp, lịch sử nhập, đơn hàng xuất và trạng thái vận chuyển; 01 mục nhà cung cấp/đơn hàng | Kho/kế toán/logistics | 1.3.4.2 | Devs | AC-03; nhân sự logistics hoặc đầu mối kho cập nhật trên máy Windows |
| FR-08 | Chức năng | Chi phí nguyên liệu, giá thành lô, doanh thu, công nợ, phí vận hành; 01 mục tài chính | Kế toán/lãnh đạo | 1.3.4.2, 1.3.4.1 | Devs/BA | AC-03; số nhập bổ sung và số tổng đối soát |
| FR-09 | Chức năng | Nhật ký nhiệt độ/%RH môi trường, nguồn đo sẵn có và nhập thủ công; 01 mục tồn/giả định, 04 mục 2 | Thủ kho | 1.3.2.3 | Devs/BA | AC-03; có kho/khu vực, thời điểm, số đo và người ghi |
| FR-10 | Chức năng | Lịch ca và phân quyền theo vai trò; 01 mục nhân sự | Kho/kế toán/người dùng | 1.3.4.3 | Devs/BA | AC-03; kiểm cho phép/từ chối của cả sáu vai trò |
| FR-11 | Chức năng | Danh mục cơ sở vật chất, dụng cụ, máy móc, bao bì/tem; 01 mục tài sản/vật tư | Kho/kế toán | 1.3.4.4 | Devs/BA | AC-03; lưu/tra cứu/cập nhật theo quyền |
| FR-12 | Chức năng | Danh mục trà, loại, nguồn gốc, ngày sản xuất/hạn, quy cách; 01 mục thông tin trà | Kho/kế toán | 1.3.1.1, 1.3.3.4 | Devs/BA | AC-03; trường bắt buộc và dữ liệu nhập được kiểm |
| FR-13 | Chức năng | Báo cáo nhập–xuất–tồn, hao hụt, bán chạy/tồn lâu; 01 mục thống kê | Kho/lãnh đạo | 1.3.4.1, 1.3.2.2 | Devs | AC-03; số liệu và bộ lọc khớp tập đối soát |
| NFR-01 | Kỹ thuật | Web trên máy Windows, môi trường ứng dụng/CSDL; 01 mục triển khai, 02 khoản cloud | Các vai trò | 1.2.3.1, 1.4.2.1 | Tech Lead/Backend | AC-04; cấu hình kỹ thuật trong SAD |
| NFR-02 | Kỹ thuật | Đồng bộ ba kho, đệm dữ liệu khi mất mạng; 02 vai Tech Lead, 03 giả định | Ba kho | 1.2.3.2, 1.5.2.1 | Tech Lead/Devs | AC-03; ngắt/khôi phục và đối soát, không trùng/mất giao dịch trong phạm vi offline SRS |
| NFR-03 | Chất lượng | Cân <0,1%, in tem <2 giây/sản phẩm; 04 mục 4 | Người vận hành | 1.3.5.1, 1.3.5.2, 1.6.1.1, 1.6.1.2 | QA/RS232 | AC-01/AC-02, đạt ở từng mẫu theo điều kiện xác định |
| TR-01 | Chuyển đổi | Danh mục, lô và tồn đầu kỳ từ Excel; 03 giả định/04 mục 6 | Kho/kế toán | 1.3.3.4, 1.4.1.3, 1.4.2.1 | BA/Onsite/Backend | AC-03/AC-04; doanh nghiệp chuẩn hóa, đội dự án kiểm/import/đối soát |
| TR-02 | Chuyển đổi | SRS/SAD/SOP/User Manual, đào tạo trước sử dụng và bổ sung cuối kỳ; 02 mục VI, 04 mục 3 | Người dùng kho | 1.4.1.2, 1.5.3.1, 1.6.2.1 | BA bàn giao; Onsite/PM tiếp nhận | AC-04; danh sách người học và thao tác theo vai trò |
| TR-03 | Bàn giao | Gói phần mềm/hồ sơ triển khai, tài khoản, CSDL, sao lưu/khôi phục, hướng dẫn vận hành; 04 mục 3 và giả định vận hành | Doanh nghiệp | 1.4.2.1, 1.6.3.2 | Tech Lead/Backend/PM | AC-04; đầu mối nhận và trách nhiệm phí sau dự án rõ |
| PR-01 | Ràng buộc | Hai tỷ/50 MM, kho tổng chậm nhất tháng 6, toàn dự án tám tháng; 01/02/04 | Chủ đầu tư/PM | 1.1.1.1, 1.1.1.3, 1.1.2.2, 1.6.3.1 | PM | Kế hoạch và biên bản đáp ứng mốc/ngân sách gốc |

**3\. TUYÊN BỐ PHẠM VI DỰ ÁN (PROJECT SCOPE STATEMENT)**

**3.1 Mục tiêu dự án**

Triển khai thành công Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS) thống nhất cho 01 Kho tổng chế biến/đóng gói tại Thái Nguyên và 02 Kho chi nhánh phân phối. Dự án thực hiện trong **8 tháng (50 Man-Month)** với tổng ngân sách phê duyệt **BAC = 2.000.000.000 VNĐ**.

**3.2 Phạm vi công việc BAO GỒM (In-Scope)**

- **Nghiên cứu & Thiết kế:** Khảo sát quy trình, lập tài liệu Đặc tả Yêu cầu (SRS), Thiết kế Kiến trúc (SAD), Quy trình thao tác chuẩn (SOP) và Sổ tay hướng dẫn sử dụng (User Manual).
- **Phát triển Phần mềm Web App:** Quản lý nhập–xuất–tồn/điều chuyển theo mã lô và vị trí, FEFO, BOM/hao hụt, cảnh báo, nhật ký môi trường, nhà cung cấp/đơn hàng, ca làm/phân quyền, tài chính kho, tài sản/vật tư và báo cáo theo FR-01–FR-13 trong RTM.
- **Tích hợp ngoại vi:** Dịch vụ kết nối bốn cân RS232, bốn máy in, tám máy quét và ba máy chấm công theo cấu hình của 01/02.
- **Triển khai & Vận hành:** Chuẩn bị môi trường phát triển, kiểm thử và production; cấu hình ứng dụng/CSDL, sao lưu/khôi phục; lắp đặt thiết bị 130 triệu theo 02. Kho tổng được đào tạo trước sử dụng, go-live chậm nhất cuối tháng 6; hai chi nhánh triển khai/đào tạo tháng 7; đào tạo bổ sung và bàn giao tháng 8.

**3.3 Phần không bao gồm và điều kiện triển khai**

- **Ứng dụng di động:** Không phát triển ứng dụng native iOS/Android. WMS sử dụng đầu cuối Windows; logistics/đầu mối kho xác nhận giao nhận trên đầu cuối được phân quyền.
- **Hạ tầng:** Doanh nghiệp cung cấp điện, đường Internet và LAN kho tổng. Đội dự án kết nối/cấu hình LAN, PC, ngoại vi và WMS; vật tư mạng hai chi nhánh theo 02. Thi công điện và đường ISP ngoài điểm đấu nối thuộc doanh nghiệp.
- **Dữ liệu chuyển đổi:** Doanh nghiệp chuẩn hóa Excel danh mục/lô/tồn đầu kỳ; đội dự án kiểm, import và đối soát. Phạm vi chuyển đổi gồm dữ liệu mở kho, không bao gồm nhập tay toàn bộ sổ lịch sử.
- **Tài sản và số đo:** Theo giả định 01, doanh nghiệp cung cấp thiết bị đo môi trường/chất lượng trà, ba máy chấm công và đầu cuối văn phòng. Số đo được nhập thủ công; tính tương thích thiết bị được xác nhận khi khảo sát. Tích hợp đo không dây được đánh giá và phê duyệt qua CR khi bổ sung.
- **Vận hành sau dự án:** Chi phí hạ tầng bao phủ tám tháng dự án. Doanh nghiệp tiếp nhận quản trị và phí duy trì sau bàn giao; dịch vụ bảo trì tiếp theo được thỏa thuận riêng.

**3.4 Tiêu chí thành công & Nghiệm thu**

Kho tổng vận hành chậm nhất 02/12/2027; toàn dự án bàn giao chậm nhất 02/02/2028; tổng chi phí không vượt hai tỷ. Chủ đầu tư, PM và đại diện các kho xác nhận phần bàn giao theo các tiêu chí sau:

| Mã | Tiêu chí chấp nhận |
| --- | --- |
| AC-01 | **Cân và dữ liệu RS232:** Sai số tương đối `abs(m_WMS - m_ref) / m_ref × 100% < 0,1%`, với `m_ref > 0` là khối lượng tham chiếu đã xác nhận, cùng đơn vị kg và trong dải sử dụng/độ chia ghi ở SRS. Giá trị, đơn vị và trạng thái nhận trên WMS khớp dữ liệu hợp lệ từ cân. Mỗi cân tại cả ba kho được nghiệm thu theo tiêu chí này trước sử dụng. |
| AC-02 | **Tạo và in tem:** Thời gian từ người dùng xác nhận yêu cầu in hợp lệ trên WMS đến khi tem in xong có thể lấy **<2 giây/sản phẩm**; máy sẵn sàng, có giấy/mực và dùng định dạng/cấu hình triển khai đã xác nhận. Tem đúng dữ liệu lô, ngày và trọng lượng; QR quét lại đúng nội dung. Tiêu chí áp dụng cho từng máy in tại ba kho. |
| AC-03 | **Chức năng:** Các yêu cầu RTM được kiểm trên dữ liệu đối soát ở ba kho và theo quyền của sáu nhóm người dùng. Số liệu nhập–xuất–tồn/điều chuyển ở kho gửi–kho nhận khớp; FEFO, BOM, cảnh báo, nhật ký môi trường, chấm công/ca/quyền, tài sản, tài chính và báo cáo đúng yêu cầu. |
| AC-04 | **Triển khai và bàn giao:** Môi trường, dữ liệu mở kho và thiết bị sẵn sàng trước go-live; người dùng được đào tạo trước sử dụng. Bộ tài liệu, tài khoản quản trị, sao lưu/khôi phục và hướng dẫn vận hành được bàn giao cho đầu mối doanh nghiệp, kèm trách nhiệm duy trì sau tháng 8. |

Dải cân/độ chia, định dạng tem và tham số nghiệp vụ được xác nhận trong SRS. Chương 9 lập Test Plan: dữ liệu, số mẫu, số lượt lặp, tình huống hợp lệ/lỗi/biên, cách đo và ghi kết quả. QA, PM và đại diện kho thống nhất kế hoạch này trước nghiệm thu; kết quả từng ca được đối chiếu với các tiêu chí trên. Căn cứ phân định: PMBOK 6 §5.3.3.1 (trang 154), §8.1.3.1–8.1.3.2 (trang 286–287), §8.3.2.1/8.3.2.4 (trang 303).

**4\. CẤU TRÚC PHÂN CHIA CÔNG VIỆC (WORK BREAKDOWN STRUCTURE - WBS)**

Cây WBS được phân rã chi tiết **4 cấp**, bám sát **6 Mốc tiến độ (Milestones)** và bộ sản phẩm bàn giao của dự án:

WBS được tổ chức theo hoạt động quản lý và các pha M1–M6; mỗi pha được phân rã thành sản phẩm và gói công việc có đầu ra, trách nhiệm và điều kiện chấp nhận. Mức phân rã phục vụ lập lịch, ước lượng nguồn lực/chi phí theo hướng dẫn ở bài giảng Quản lý phạm vi dự án, trang 28–32 và 38.

```text
1. DỰ ÁN WMS TRÀ TÂN CƯƠNG
├── 1.1 Quản lý Dự án (PMO)
│   ├── 1.1.1 Khởi tạo & Lập Kế hoạch
│   │   ├── 1.1.1.1 Xây dựng Kế hoạch Quản lý Dự án Tổng thể (PMP)
│   │   ├── 1.1.1.2 Xây dựng Kế hoạch Quản lý Phạm vi & Từ điển WBS
│   │   └── 1.1.1.3 Lập Tiến độ Chi tiết & Phân bổ Ngân sách BAC 2.0 Tỷ
│   ├── 1.1.2 Giám sát & Điều phối Thực thi
│   │   ├── 1.1.2.1 Tổ chức Họp Giao ban Định kỳ Tuần/Tháng
│   │   ├── 1.1.2.2 Theo dõi, Kiểm soát Chi phí & Quỹ Dự phòng (143 triệu)
│   │   └── 1.1.2.3 Báo cáo Tiến độ Định kỳ cho Project Sponsor
│   └── 1.1.3 Quản lý Thay đổi & Đảm bảo Chất lượng
│       ├── 1.1.3.1 Tiếp nhận & Đánh giá Yêu cầu Thay đổi (CR)
│       └── 1.1.3.2 Đảm bảo Chất lượng Quy trình (QA)
├── 1.2 M1: Phân tích Yêu cầu & Thiết kế Kiến trúc (Tháng 1)
│   ├── 1.2.1 Khảo sát Hiện trạng Nghiệp vụ 3 Kho & Thiết bị IoT
│   │   ├── 1.2.1.1 Khảo sát luồng nhập/chế biến/xuất tại Kho tổng Thái Nguyên
│   │   ├── 1.2.1.2 Khảo sát Cổng Giao tiếp RS232 Trạm Cân, Máy in & Máy Chấm công
│   │   └── 1.2.1.3 Thu thập biểu mẫu Excel dữ liệu cũ & định mức BOM
│   ├── 1.2.2 Biên soạn Đặc tả Yêu cầu Phần mềm (SRS)
│   │   ├── 1.2.2.1 Lập đặc tả use-case cho 6 nhóm người dùng
│   │   └── 1.2.2.2 Thống nhất Chuẩn Giao tiếp RS232/COM & In Tem
│   └── 1.2.3 Thiết kế Kiến trúc Hệ thống (SAD) & CSDL
│       ├── 1.2.3.1 Thiết kế kiến trúc Web App trên máy trạm Windows
│       ├── 1.2.3.2 Thiết kế CSDL Đồng bộ 3 Kho & Cơ chế Đệm Dữ liệu Offline
│       └── 1.2.3.3 Thiết kế Giao diện (UI/UX) cho Thủ kho, Công nhân & Lãnh đạo
├── 1.3 M2: Phát triển Phần mềm Lõi & IoT RS232 (Tháng 2 - Tháng 4)
│   ├── 1.3.1 Phát triển Core WMS & Quản lý Kho
│   │   ├── 1.3.1.1 Lập trình Chức năng Nhập/Xuất/Kiểm kê & Sơ đồ Zone/Bin/Rack
│   │   └── 1.3.1.2 Lập trình Thuật toán Xuất kho Ưu tiên FEFO
│   ├── 1.3.2 Phát triển Module Định mức BOM & Cảnh báo
│   │   ├── 1.3.2.1 Lập trình công thức quy đổi BOM theo độ ẩm & hao hụt chè
│   │   ├── 1.3.2.2 Lập trình Cảnh báo Tồn kho Dưới ngưỡng, Cận hạn/Hết hạn & Báo cáo Tuổi hàng (Aging)
│   │   └── 1.3.2.3 Phát triển nhật ký nhiệt độ và độ ẩm môi trường
│   ├── 1.3.3 Phát triển Module Kết nối Thiết bị Phần cứng (IoT)
│   │   ├── 1.3.3.1 Lập trình Service kết nối RS232 đọc dữ liệu cân tự động
│   │   ├── 1.3.3.2 Lập trình Module Tạo Mã QR & Điều khiển Máy in Tem
│   │   ├── 1.3.3.3 Lập trình tích hợp Máy quét QR & Máy chấm công
│   │   └── 1.3.3.4 Lập trình Công cụ Import/Export Danh mục và Tồn đầu kỳ từ Excel
│   ├── 1.3.4 Phát triển Dashboard & Chức năng Bổ trợ
│   │   ├── 1.3.4.1 Lập trình Dashboard KPI, báo cáo doanh thu & giá vốn cho Lãnh đạo
│   │   ├── 1.3.4.2 Lập trình Module Quản lý Nhà cung cấp, Kế toán kho & Tài xế
│   │   ├── 1.3.4.3 Phát triển lịch ca và phân quyền vai trò
│   │   └── 1.3.4.4 Phát triển danh mục tài sản dụng cụ và vật tư
│   └── 1.3.5 Kiểm thử Tích hợp Nội bộ (Internal Integration Testing)
│       ├── 1.3.5.1 Kiểm thử luồng dữ liệu Cân RS232 đến Web App
│       └── 1.3.5.2 Kiểm thử Tốc độ In Tem & Thuật toán FEFO/BOM
├── 1.4 M3 & M4: Triển khai, UAT & Go-Live Kho Tổng Thái Nguyên (Tháng 5 - Tháng 6)
│   ├── 1.4.1 M3: Lắp đặt, UAT và đào tạo trước vận hành (Tháng 5)
│   │   ├── 1.4.1.1 Lắp đặt PC, Trạm Cân RS232, Máy in, Máy quét tại Kho Tổng
│   │   ├── 1.4.1.2 Xây dựng Kịch bản UAT & Hướng dẫn 6 Nhóm Người dùng
│   │   └── 1.4.1.3 Khởi tạo dữ liệu danh mục trà ban đầu từ file Excel
│   └── 1.4.2 M4: Go-live kho tổng chậm nhất cuối tháng 6
│       ├── 1.4.2.1 Chuyển đổi Dữ liệu Sang Môi trường Vận hành Thực tế
│       ├── 1.4.2.2 Đưa Kho Tổng vào Vận hành Chính thức
│       └── 1.4.2.3 Onsite Hỗ trợ Kỹ thuật Trực tiếp tại Thái Nguyên
├── 1.5 M5: Triển khai & Triển khai đồng bộ cho 02 Kho Chi nhánh (Tháng 7)
│   ├── 1.5.1 Lắp đặt Phần cứng & Thiết bị tại 02 Kho Chi nhánh Phân phối
│   │   └── 1.5.1.1 Lắp đặt PC, Trạm cân, Máy in theo chuẩn tương thích tại 2 chi nhánh
│   ├── 1.5.2 Cấu hình đồng bộ dữ liệu và cơ chế đệm ngoại tuyến
│   │   └── 1.5.2.1 Cấu hình Đồng bộ CSDL Liên kho & Cơ chế Hoạt động Offline
│   └── 1.5.3 Đào tạo & Chuyển giao tại 02 Chi nhánh
│       └── 1.5.3.1 Đào tạo thao tác phần mềm cho Thủ kho & Nhân sự 2 chi nhánh
└── 1.6 M6: Đào tạo, Nghiệm thu Tổng thể & Đóng Dự án (Tháng 8)
    ├── 1.6.1 Tổng hợp và kiểm lại tiêu chí thành công
    │   ├── 1.6.1.1 Đo đạc sai số cân tự động qua RS232 (< 0,1%)
    │   └── 1.6.1.2 Đo Thời gian Tạo & In Tem
    ├── 1.6.2 Hoàn thiện Bộ Tài liệu Dự án
    │   └── 1.6.2.1 Hoàn thiện bộ tài liệu SRS, SAD, SOP & User Manual
    └── 1.6.3 Nghiệm thu Tổng thể & Kết thúc Dự án
        ├── 1.6.3.1 Ký Biên bản UAT & Nghiệm thu Tổng thể với Ban Giám đốc
        └── 1.6.3.2 Bàn giao hệ thống và đóng dự án
```

**5. TỪ ĐIỂN WBS**

Từ điển mô tả 45 gói công việc cấp thấp nhất. Thời lượng, nguồn lực và chi phí từng gói được bổ sung khi lập các kế hoạch liên quan, theo PMBOK 6 §5.4.3.1 (trang 161–162).

### Quản lý dự án

**Gói công việc 1.1.1.1: Xây dựng Kế hoạch Quản lý Dự án Tổng thể (PMP)**

- **Mã WBS:** 1.1.1.1
- **Mô tả công việc:** Lập Kế hoạch Quản lý Dự án tổng hợp đầy đủ các kế hoạch thành phần: phạm vi, tiến độ, chi phí, chất lượng, nhân sự, rủi ro và mua sắm.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Document Kế hoạch Quản lý Dự án (PMP Document).
- **Tiêu chí chấp nhận:** Được Ban Giám đốc phê duyệt; khớp 100% mục tiêu 8 tháng và ngân sách BAC 2.0 Tỷ VNĐ.

**Gói công việc 1.1.1.2: Xây dựng Kế hoạch Quản lý Phạm vi & Từ điển WBS**

- **Mã WBS:** 1.1.1.2
- **Mô tả công việc:** Chi tiết hóa Tuyên bố Phạm vi, Ma trận RTM, phân rã Cây WBS 4 cấp và biên soạn Từ điển WBS toàn diện.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Báo cáo Scope Management Plan & Full WBS Dictionary.
- **Tiêu chí chấp nhận:** Phủ kín 100% các yêu cầu nghiệp vụ kho và tích hợp thiết bị IoT của Trà Tân Cương.

**Gói công việc 1.1.1.3: Lập Tiến độ Chi tiết & Phân bổ Ngân sách BAC 2.0 Tỷ**

- **Mã WBS:** 1.1.1.3
- **Mô tả công việc:** Lập lịch trình làm việc chi tiết cho 8 nhân sự (50 Man-Month); xác định đường găng (Critical Path) hướng tới mốc Go-live Kho tổng Tháng 6; phân bổ ngân sách BAC 2.0 Tỷ VNĐ.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Biểu đồ Gantt Chart & Bảng phân bổ chi phí chi tiết.
- **Tiêu chí chấp nhận:** Bảo đảm mốc Go-live Tháng 6 và tổng chi phí không vượt quá 2.000.000.000 VNĐ.

**Gói công việc 1.1.2.1: Tổ chức Họp Giao ban Định kỳ**

- **Mã WBS:** 1.1.2.1
- **Mô tả công việc:** Tổ chức các buổi họp giao ban tuần/tháng của đội dự án và họp báo cáo định kỳ với Ban Giám đốc Trà Tân Cương.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Biên bản họp (Meeting Minutes) & Danh sách việc cần làm (Action Items).
- **Tiêu chí chấp nhận:** 100% các cuộc họp có biên bản và được ghi nhận tiến độ đầy đủ.

**Gói công việc 1.1.2.2: Theo dõi, Kiểm soát Chi phí & Quỹ Dự phòng (143 triệu)**

- **Mã WBS:** 1.1.2.2
- **Mô tả công việc:** Theo dõi chi phí thực tế (AC) so với kế hoạch (PV), quản lý việc sử dụng Quỹ dự phòng rủi ro 143.000.000 VNĐ (7.15%).
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Báo cáo theo dõi ngân sách hàng tháng.
- **Tiêu chí chấp nhận:** Việc sử dụng dự phòng có căn cứ và phê duyệt theo kế hoạch chi phí/rủi ro; tổng chi phí trong ngân sách hai tỷ.

**Gói công việc 1.1.2.3: Báo cáo Tiến độ Định kỳ cho Project Sponsor**

- **Mã WBS:** 1.1.2.3
- **Mô tả công việc:** Tổng hợp báo cáo tiến độ (Monthly Status Report) gửi Ban Giám đốc Doanh nghiệp Trà Tân Cương.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Báo cáo tiến độ dự án.
- **Tiêu chí chấp nhận:** Báo cáo gửi đúng hạn vào ngày cuối cùng của mỗi tháng.

**Gói công việc 1.1.3.1: Tiếp nhận & Đánh giá Yêu cầu Thay đổi (CR)**

- **Mã WBS:** 1.1.3.1
- **Mô tả công việc:** Tiếp nhận, ghi nhận và phân tích tác động của các phiếu CR về chi phí, tiến độ và kỹ thuật trước khi trình duyệt.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú / Solution Architect
- **Sản phẩm đầu ra:** Nhật ký thay đổi (Change Log) & Báo cáo đánh giá tác động.
- **Tiêu chí chấp nhận:** Thay đổi phạm vi/tiêu chí/đường cơ sở có phê duyệt của chủ đầu tư; sửa lỗi trong nội dung đã duyệt do PM điều phối, theo mục 1.2.

**Gói công việc 1.1.3.2: Đảm bảo Chất lượng Quy trình (QA)**

- **Mã WBS:** 1.1.3.2
- **Mô tả công việc:** Kiểm tra, giám sát việc tuân thủ quy trình làm việc, chuẩn coding và quy trình đóng gói phần mềm của nhóm.
- **Người chịu trách nhiệm:** QA Engineer
- **Sản phẩm đầu ra:** Báo cáo kiểm định chất lượng (QA Report).
- **Tiêu chí chấp nhận:** Không vi phạm các quy trình quản lý chất lượng đã đề ra trong PMP.

### M1 Phân tích và thiết kế (tháng 1)

**Gói công việc 1.2.1.1: Khảo sát Luồng Nhập/Chế biến/Xuất tại Kho Tổng Thái Nguyên**

- **Mã WBS:** 1.2.1.1
- **Mô tả công việc:** Phỏng vấn Chị Đại diện Kho tổng và công nhân tại Kho tổng Thái Nguyên về quy trình thu mua búp tươi, chế biến, đóng gói và lưu kho.
- **Người chịu trách nhiệm:** BA / Solution Architect
- **Sản phẩm đầu ra:** Sơ đồ dòng quy trình nghiệp vụ (Business Process Model) Kho tổng.
- **Tiêu chí chấp nhận:** Được đại diện Kho tổng ký xác nhận quy trình và nguồn dữ liệu khảo sát.

**Gói công việc 1.2.1.2: Khảo sát Cổng Giao tiếp RS232 Trạm Cân, Máy in & Máy Chấm công**

- **Mã WBS:** 1.2.1.2
- **Mô tả công việc:** Thu thập đặc tả kết nối của bốn cân RS232, bốn máy in, tám máy quét và ba máy chấm công theo 01/02; xác nhận dải cân, độ chia và nguồn số đo. BA/Tech Lead khảo sát tháng 1; kỹ sư RS232 kiểm bộ mẫu từ tháng 2.
- **Người chịu trách nhiệm:** Solution Architect / BA
- **Sản phẩm đầu ra:** Báo cáo khảo sát phần cứng & Bảng thông số giao thức thiết bị.
- **Tiêu chí chấp nhận:** Danh mục, dải sử dụng và giao thức thiết bị được xác nhận trong SRS; tài sản doanh nghiệp cung cấp được đối chiếu khi khảo sát.

**Gói công việc 1.2.1.3: Thu thập Biểu mẫu Excel Dữ liệu Cũ & Định mức BOM**

- **Mã WBS:** 1.2.1.3
- **Mô tả công việc:** Thu thập file Excel danh mục chè, nhà vườn, mẫu sổ sách kế toán và công thức tính hao hụt chè theo độ ẩm.
- **Người chịu trách nhiệm:** BA
- **Sản phẩm đầu ra:** Tập hợp file dữ liệu mẫu & Công thức chuyển đổi BOM.
- **Tiêu chí chấp nhận:** Cung cấp đầy đủ công thức quy đổi độ ẩm phục vụ lập trình module BOM.

**Gói công việc 1.2.2.1: Lập Đặc tả Use-case cho 6 Nhóm Người dùng**

- **Mã WBS:** 1.2.2.1
- **Mô tả công việc:** Biên soạn tài liệu chi tiết use-case cho 6 vai trò: Lãnh đạo, Quản lý kho, Thủ kho, Công nhân, Kế toán kho, Tài xế/Logistics.
- **Người chịu trách nhiệm:** BA / Solution Architect
- **Sản phẩm đầu ra:** Tài liệu Đặc tả Yêu cầu Phần mềm SRS (Functional SRS).
- **Tiêu chí chấp nhận:** SRS mô tả các nhóm yêu cầu 01–04 và luồng thao tác của sáu vai trò, được chủ đầu tư xác nhận.

**Gói công việc 1.2.2.2: Thống nhất Chuẩn Giao tiếp RS232/COM & In Tem**

- **Mã WBS:** 1.2.2.2
- **Mô tả công việc:** Đặc tả yêu cầu phi chức năng: dải cân/độ chia, sai số cân <0,1%, thời gian tạo và in tem <2 giây/sản phẩm, định dạng tem và cơ chế đệm dữ liệu ngoại tuyến. Kỹ sư RS232 tiếp nhận, kiểm mẫu từ tháng 2.
- **Người chịu trách nhiệm:** Solution Architect / BA
- **Sản phẩm đầu ra:** Tài liệu SRS phần Phi chức năng & Chuẩn phần cứng.
- **Tiêu chí chấp nhận:** Thông số phần cứng và tiêu chí AC-01/AC-02 được xác nhận trong SRS.

**Gói công việc 1.2.3.1: Thiết kế Kiến trúc Web App trên Máy trạm Windows**

- **Mã WBS:** 1.2.3.1
- **Mô tả công việc:** Thiết kế mô hình kiến trúc phần mềm (SAD), giao tiếp Web Client, Local Service RS232 và CSDL Server; chuẩn bị môi trường phát triển/kiểm thử từ gói cloud 02. Tech Lead phụ trách tháng 1, Backend tiếp nhận từ tháng 2.
- **Người chịu trách nhiệm:** Solution Architect
- **Sản phẩm đầu ra:** Tài liệu Thiết kế Kiến trúc Hệ thống (SAD) và môi trường phát triển/kiểm thử.
- **Tiêu chí chấp nhận:** Kiến trúc tương thích Windows tại ba kho; môi trường phát triển/kiểm thử sẵn sàng cho giai đoạn phát triển.

**Gói công việc 1.2.3.2: Thiết kế CSDL Đồng bộ 3 Kho & Cơ chế Đệm Dữ liệu Offline**

- **Mã WBS:** 1.2.3.2
- **Mô tả công việc:** Thiết kế ERD CSDL quan hệ, bảng mã lô/vị trí/nghiệp vụ và cơ chế đệm dữ liệu khi mất Internet; kiến trúc lưu trữ và đồng bộ được xác định trong SAD theo yêu cầu offline của SRS.
- **Người chịu trách nhiệm:** Solution Architect
- **Sản phẩm đầu ra:** File thiết kế CSDL (Database Schema Design).
- **Tiêu chí chấp nhận:** CSDL phục vụ đồng bộ ba kho, xử lý trùng/xung đột mã lô và đáp ứng phạm vi hoạt động ngoại tuyến đã xác nhận.

**Gói công việc 1.2.3.3: Thiết kế Giao diện (UI/UX) cho Thủ kho, Công nhân & Lãnh đạo**

- **Mã WBS:** 1.2.3.3
- **Mô tả công việc:** Thiết kế Wireframe/Prototype giao diện Dashboard KPI, màn hình cân-in tem nút bấm to cho công nhân, màn hình quét QR cho thủ kho.
- **Người chịu trách nhiệm:** BA / Solution Architect
- **Sản phẩm đầu ra:** Bộ thiết kế Figma/UI Prototype.
- **Tiêu chí chấp nhận:** Giao diện đơn giản, công nhân thao tác cân/in tem không quá hai bước; bản thiết kế được đầu mối nghiệp vụ xác nhận.

### M2 Phát triển và kiểm thử (tháng 2–4)

**Gói công việc 1.3.1.1: Lập trình Chức năng Nhập/Xuất/Kiểm kê & Sơ đồ Zone/Bin/Rack**

- **Mã WBS:** 1.3.1.1
- **Mô tả công việc:** Phát triển danh mục trà/nguồn gốc/ngày/hạn/quy cách, tự sinh Batch ID, ghi kết quả chất lượng lô, nhập–xuất–tồn/kiểm kê/điều chuyển và vị trí lưu trữ theo 01.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module Quản lý Kho Lõi (Core WMS).
- **Tiêu chí chấp nhận:** FR-01/FR-12 đạt AC-03, mã lô không trùng, số lượng/đơn vị/vị trí khớp tập đối soát.

**Gói công việc 1.3.1.2: Lập trình Thuật toán Xuất kho Ưu tiên FEFO**

- **Mã WBS:** 1.3.1.2
- **Mô tả công việc:** Gợi ý xuất ưu tiên lô còn hạn, được phép xuất có ngày hết hạn gần nhất theo 04.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module xử lý FEFO Logic.
- **Tiêu chí chấp nhận:** Đạt AC-03: đúng thứ tự lô còn hạn và không gợi ý xuất lô hết hạn trong tập kiểm.

**Gói công việc 1.3.2.1: Lập trình Công thức Quy đổi BOM theo Độ ẩm & Hao hụt Chè**

- **Mã WBS:** 1.3.2.1
- **Mô tả công việc:** Lập trình công thức quy đổi khối lượng trà búp tươi sang thành phẩm và tỷ lệ hao hụt theo độ ẩm trà, dùng công thức/số đo do doanh nghiệp xác nhận.
- **Người chịu trách nhiệm:** Devs / BA
- **Sản phẩm đầu ra:** Module BOM & Processing Loss.
- **Tiêu chí chấp nhận:** Tính toán chính xác định mức chế biến trà theo công thức đã phê duyệt.

**Gói công việc 1.3.2.2: Lập trình Cảnh báo Tồn kho Dưới ngưỡng, Cận hạn/Hết hạn & Báo cáo Tuổi hàng (Aging)**

- **Mã WBS:** 1.3.2.2
- **Mô tả công việc:** Phát triển cảnh báo tồn dưới ngưỡng, cận hạn/hết hạn và báo cáo tuổi hàng theo ngưỡng/ngày được xác nhận trong SRS.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module Cảnh báo & Aging Report.
- **Tiêu chí chấp nhận:** Cảnh báo tồn dưới ngưỡng, cận hạn/hết hạn và báo cáo tuổi hàng đúng tham số SRS theo AC-03.

**Gói công việc 1.3.2.3: Phát triển nhật ký nhiệt độ và độ ẩm môi trường**

- **Mã WBS:** 1.3.2.3
- **Mô tả công việc:** Nhập, lưu và tra cứu thủ công nhiệt độ/độ ẩm môi trường từ thiết bị doanh nghiệp; ghi kho, khu vực, thời điểm và người nhập.
- **Người chịu trách nhiệm:** Devs / BA
- **Sản phẩm đầu ra:** Module nhật ký môi trường kho.
- **Tiêu chí chấp nhận:** Nhật ký môi trường đủ trường dữ liệu, tra cứu theo kho/thời điểm và thực hiện theo quyền người dùng.

**Gói công việc 1.3.3.1: Lập trình Service Kết nối RS232 Đọc Dữ liệu Cân Tự động**

- **Mã WBS:** 1.3.3.1
- **Mô tả công việc:** Phát triển dịch vụ cục bộ nhận dữ liệu từ bốn cân RS232 theo trạm của 02, chuyển số/đơn vị/trạng thái hợp lệ vào WMS.
- **Người chịu trách nhiệm:** RS232 Engineer
- **Sản phẩm đầu ra:** Windows Service IoT RS232 Connector.
- **Tiêu chí chấp nhận:** Giá trị, đơn vị và trạng thái WMS khớp dữ liệu hợp lệ từ cân; kết quả nghiệm thu đáp ứng AC-01.

**Gói công việc 1.3.3.2: Lập trình Module Tạo Mã QR & Điều khiển Máy in Tem**

- **Mã WBS:** 1.3.3.2
- **Mô tả công việc:** Tạo QR/tem theo dữ liệu lô/ngày/trọng lượng đã xác nhận, kết nối bốn máy in theo giao thức tương thích; chứng từ văn phòng dùng máy in sẵn có hoặc đầu ra PDF theo SRS.
- **Người chịu trách nhiệm:** RS232 Engineer
- **Sản phẩm đầu ra:** Module QRCode & Printer Driver Integration.
- **Tiêu chí chấp nhận:** Tem QR đúng nội dung, quét lại được; thời gian tạo và in <2 giây/sản phẩm theo AC-02.

**Gói công việc 1.3.3.3: Lập trình Tích hợp Máy quét QR & Máy chấm công**

- **Mã WBS:** 1.3.3.3
- **Mô tả công việc:** Tích hợp tám scanner và ba máy chấm công do doanh nghiệp cung cấp theo đặc tả; đối soát dữ liệu chấm công với ca làm việc.
- **Người chịu trách nhiệm:** Devs / RS232 Engineer
- **Sản phẩm đầu ra:** Sub-module Barcode Scanner & Timekeeper Sync.
- **Tiêu chí chấp nhận:** FR-05/FR-06 đạt AC-03; không lẫn dữ liệu nhân viên, không nhập trùng sau đồng bộ.

**Gói công việc 1.3.3.4: Lập trình Công cụ Import/Export Danh mục và Tồn đầu kỳ từ Excel**

- **Mã WBS:** 1.3.3.4
- **Mô tả công việc:** Cung cấp công cụ nhập/xuất danh mục trà/nhà cung cấp/bao bì, lô và tồn đầu kỳ theo mẫu Excel đã xác nhận.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Tool Import/Export Excel.
- **Tiêu chí chấp nhận:** Báo lỗi dòng/cột sai định dạng; mã lô, đơn vị và số lượng nhập khớp dữ liệu đối soát, dữ liệu nhập lại được kiểm tra trùng.

**Gói công việc 1.3.4.1: Lập trình Dashboard KPI, Báo cáo Doanh thu & Giá vốn cho Lãnh đạo**

- **Mã WBS:** 1.3.4.1
- **Mô tả công việc:** Phát triển Dashboard và các báo cáo nhập–xuất–tồn, Aging, hao hụt, doanh thu/giá vốn, bán chạy/tồn lâu theo RTM.
- **Người chịu trách nhiệm:** Devs / Solution Architect
- **Sản phẩm đầu ra:** Module Executive Dashboard.
- **Tiêu chí chấp nhận:** FR-08/FR-13 đạt AC-03, bộ lọc và số tổng khớp tập đối soát.

**Gói công việc 1.3.4.2: Lập trình Module Quản lý Nhà cung cấp, Kế toán Kho & Tài xế**

- **Mã WBS:** 1.3.4.2
- **Mô tả công việc:** Phát triển nhà cung cấp/lịch sử nhập, đơn hàng xuất/trạng thái vận chuyển; chi phí nguyên liệu/đóng gói, công nợ và phí vận hành do người có quyền nhập hoặc lấy từ giao dịch. Logistics/đầu mối kho cập nhật biên bản giao nhận trên máy Windows.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module Partner, Accounting & Transport Management.
- **Tiêu chí chấp nhận:** Quản lý chính xác công nợ và trạng thái giao nhận/điều chuyển; dữ liệu tài chính khớp tập đối soát theo AC-03.

**Gói công việc 1.3.4.3: Phát triển lịch ca và phân quyền vai trò**

- **Mã WBS:** 1.3.4.3
- **Mô tả công việc:** Quản lý ca làm việc và quyền thao tác/tra cứu theo sáu nhóm người dùng; liên kết dữ liệu chấm công từ module đã có.
- **Người chịu trách nhiệm:** Devs / BA
- **Sản phẩm đầu ra:** Module lịch ca và phân quyền.
- **Tiêu chí chấp nhận:** Lịch ca và dữ liệu chấm công khớp đối soát; mỗi vai trò thực hiện đúng quyền thao tác/tra cứu.

**Gói công việc 1.3.4.4: Phát triển danh mục tài sản dụng cụ và vật tư**

- **Mã WBS:** 1.3.4.4
- **Mô tả công việc:** Quản lý danh mục kệ/khu vực, máy móc, dụng cụ và vật tư bao bì/tem theo yêu cầu 01.
- **Người chịu trách nhiệm:** Devs / BA
- **Sản phẩm đầu ra:** Module danh mục tài sản/dụng cụ/vật tư.
- **Tiêu chí chấp nhận:** FR-11 đạt AC-03: nhập/tra cứu/cập nhật theo quyền và dữ liệu đối soát.

**Gói công việc 1.3.5.1: Kiểm thử Luồng Dữ liệu Cân RS232 đến Web App**

- **Mã WBS:** 1.3.5.1
- **Mô tả công việc:** Kiểm thử luồng dữ liệu RS232 trên bộ mẫu từ tháng 3; nghiệm thu từng cân tại kho trước sử dụng, kết hợp kiểm lỗi kết nối và khôi phục.
- **Người chịu trách nhiệm:** QA / RS232 Engineer
- **Sản phẩm đầu ra:** Báo cáo Integration Test - RS232 Data Flow.
- **Tiêu chí chấp nhận:** Sai số cân <0,1% theo AC-01; dữ liệu cân/WMS khớp; có hồ sơ kết quả và kiểm lại lỗi.

**Gói công việc 1.3.5.2: Kiểm thử Tốc độ In Tem & Thuật toán FEFO/BOM**

- **Mã WBS:** 1.3.5.2
- **Mô tả công việc:** Kiểm thử hiệu năng in tem, FEFO/BOM và các chức năng RTM; nghiệm thu từng máy in trước sử dụng tại kho.
- **Người chịu trách nhiệm:** QA / Devs
- **Sản phẩm đầu ra:** Báo cáo Integration Test - Performance & Business Logic.
- **Tiêu chí chấp nhận:** Thời gian tạo và in tem <2 giây/sản phẩm theo AC-02; chức năng và dữ liệu đối soát đáp ứng AC-03.

### M3–M4 Triển khai và vận hành kho tổng (tháng 5–6)

**Gói công việc 1.4.1.1: Lắp đặt PC, Trạm Cân RS232, Máy in, Máy quét tại Kho Tổng**

- **Mã WBS:** 1.4.1.1
- **Mô tả công việc:** Lắp hai PC, hai cân RS232, hai máy in và bốn scanner mua mới tại kho tổng; kết nối một máy chấm công sẵn có và các đầu cuối văn phòng do doanh nghiệp cung cấp.
- **Người chịu trách nhiệm:** Onsite Engineer / RS232 Engineer
- **Sản phẩm đầu ra:** Hạ tầng phần cứng hoàn chỉnh tại Kho tổng Thái Nguyên.
- **Tiêu chí chấp nhận:** Danh mục/vị trí khớp 02, phụ kiện và nguồn tài sản sẵn có được xác nhận; kết nối/cấu hình LAN–ngoại vi–WMS thông suốt, đạt bộ kiểm trước vận hành.

**Gói công việc 1.4.1.2: Xây dựng Kịch bản UAT & Hướng dẫn 6 Nhóm Người dùng**

- **Mã WBS:** 1.4.1.2
- **Mô tả công việc:** Lập kịch bản UAT, hướng dẫn người dùng thử nghiệm và đào tạo thao tác vận hành tại kho tổng trước go-live. BA bàn giao SOP/User Manual cho Onsite/PM trước cuối tháng 5.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú / BA / Onsite Engineer
- **Sản phẩm đầu ra:** Kịch bản/biên bản UAT Kho tổng, tài liệu hướng dẫn, danh sách và kết quả thực hành của người học.
- **Tiêu chí chấp nhận:** Đại diện Kho tổng xác nhận UAT; người dùng được đào tạo trước vận hành, có hồ sơ thực hành theo AC-04.

**Gói công việc 1.4.1.3: Khởi tạo Dữ liệu Danh mục Trà Ban đầu từ File Excel**

- **Mã WBS:** 1.4.1.3
- **Mô tả công việc:** Kiểm/import danh mục trà/nhà cung cấp/bao bì, lô và tồn đầu kỳ từ Excel chuẩn hóa của doanh nghiệp vào môi trường chạy thử; đối soát trước chuyển production.
- **Người chịu trách nhiệm:** Onsite Engineer / BA
- **Sản phẩm đầu ra:** CSDL Kho tổng được khởi tạo đầy đủ dữ liệu ban đầu.
- **Tiêu chí chấp nhận:** TR-01 đạt AC-03; dữ liệu mở kho/lô/vị trí/đơn vị và số lượng khớp bảng doanh nghiệp xác nhận.

**Gói công việc 1.4.2.1: Chuyển đổi Dữ liệu Sang Môi trường Vận hành Thực tế**

- **Mã WBS:** 1.4.2.1
- **Mô tả công việc:** Triển khai môi trường ứng dụng/CSDL production, cấu hình kết nối ngoại vi, kiểm sao lưu/khôi phục và chuyển danh mục/lô/tồn đầu kỳ đã đối soát; loại dữ liệu thử.
- **Người chịu trách nhiệm:** Solution Architect / Backend Developer
- **Sản phẩm đầu ra:** Môi trường production, dữ liệu mở kho, bản sao lưu và hướng dẫn vận hành đủ dùng.
- **Tiêu chí chấp nhận:** Môi trường production và dữ liệu mở kho sẵn sàng theo AC-04; có hồ sơ thử khôi phục và đối soát.

**Gói công việc 1.4.2.2: Đưa Kho Tổng vào Vận hành Chính thức**

- **Mã WBS:** 1.4.2.2
- **Mô tả công việc:** Kích hoạt sử dụng chính thức sau khi dữ liệu, ngoại vi và người dùng đáp ứng AC-01–AC-04.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú & Onsite Engineer
- **Sản phẩm đầu ra:** Biên bản Xác nhận Go-live Kho Tổng Thái Nguyên.
- **Tiêu chí chấp nhận:** Kho tổng vận hành thực tế chậm nhất 02/12/2027; có hồ sơ đạt, người dùng được đào tạo trước sử dụng và xác nhận của chủ đầu tư/đại diện kho.

**Gói công việc 1.4.2.3: Onsite Hỗ trợ Kỹ thuật Trực tiếp tại Thái Nguyên**

- **Mã WBS:** 1.4.2.3
- **Mô tả công việc:** Túc trực trực tiếp tại Kho tổng Thái Nguyên trong 2 tuần đầu Go-live để xử lý sự cố phát sinh.
- **Người chịu trách nhiệm:** Onsite Engineer / RS232 Engineer
- **Sản phẩm đầu ra:** Báo cáo nhật ký hỗ trợ Go-live (Onsite Support Log).
- **Tiêu chí chấp nhận:** Có đầu mối tiếp nhận, nhật ký sự cố, trạng thái xử lý và kết quả hỗ trợ.

### M5 Triển khai hai chi nhánh (tháng 7)

**Gói công việc 1.5.1.1: Lắp đặt Phần cứng & Thiết bị tại 02 Kho Chi nhánh Phân phối**

- **Mã WBS:** 1.5.1.1
- **Mô tả công việc:** Mỗi chi nhánh lắp một PC, một cân, một máy in và hai scanner mua mới; kết nối một máy chấm công sẵn có/kho. Tổng hai chi nhánh: hai PC, hai cân, hai máy in, bốn scanner, hai máy chấm công khách hàng cung cấp.
- **Người chịu trách nhiệm:** Onsite Engineer
- **Sản phẩm đầu ra:** Bàn giao hạ tầng phần cứng hoàn chỉnh tại 02 Kho chi nhánh.
- **Tiêu chí chấp nhận:** Danh mục khớp 02 và giả định 01; tại mỗi kho, AC-01/AC-02 và kết nối đầu cuối đạt trước sử dụng.

**Gói công việc 1.5.2.1: Cấu hình Đồng bộ CSDL Liên kho & Cơ chế Hoạt động Offline**

- **Mã WBS:** 1.5.2.1
- **Mô tả công việc:** Cấu hình đồng bộ dữ liệu giữa hai chi nhánh và kho tổng theo SAD; bật đệm ngoại tuyến cho các nghiệp vụ được xác nhận trong SRS.
- **Người chịu trách nhiệm:** Solution Architect / Devs
- **Sản phẩm đầu ra:** Hệ thống CSDL Đồng bộ 3 Kho (Multi-site Database Sync).
- **Tiêu chí chấp nhận:** Dữ liệu được đồng bộ khi Internet khôi phục; số liệu khớp đối soát, xử lý trùng/xung đột theo AC-03.

**Gói công việc 1.5.3.1: Đào tạo Thao tác Phần mềm cho Thủ kho & Nhân sự 2 Chi nhánh**

- **Mã WBS:** 1.5.3.1
- **Mô tả công việc:** Tổ chức các lớp hướng dẫn sử dụng phần mềm, quét mã QR kiểm kê, nhận hàng điều chuyển cho nhân sự tại 02 chi nhánh.
- **Người chịu trách nhiệm:** Onsite Engineer / PM
- **Sản phẩm đầu ra:** Báo cáo kết quả đào tạo & Danh sách điểm danh.
- **Tiêu chí chấp nhận:** Người dùng hai chi nhánh được đào tạo trước vận hành và đạt bài thực hành theo vai trò.

### M6 Tổng hợp nghiệm thu và bàn giao (tháng 8)

**Gói công việc 1.6.1.1: Đo đạc Sai số Cân Tự động qua RS232**

- **Mã WBS:** 1.6.1.1
- **Mô tả công việc:** Tổng hợp hồ sơ nghiệm thu độ chính xác bốn cân tại ba kho; đo lại phần thiết bị/phần mềm thay đổi nếu có. Kỹ sư RS232 bàn giao đặc tả/hồ sơ trước cuối tháng 7.
- **Người chịu trách nhiệm:** QA / Solution Architect
- **Sản phẩm đầu ra:** Biên bản kiểm định Tiêu chí Cân tự động.
- **Tiêu chí chấp nhận:** Đủ hồ sơ nghiệm thu bốn cân theo AC-01; sai số cân <0,1% trong điều kiện đã xác nhận.

**Gói công việc 1.6.1.2: Đo Thời gian Tạo & In Tem**

- **Mã WBS:** 1.6.1.2
- **Mô tả công việc:** Tổng hợp hồ sơ đo thời gian tạo/in tem của bốn máy; đo lại phần thay đổi nếu có. Kỹ sư RS232 bàn giao hồ sơ trước cuối tháng 7.
- **Người chịu trách nhiệm:** QA / Solution Architect
- **Sản phẩm đầu ra:** Biên bản kiểm định Tiêu chí In tem.
- **Tiêu chí chấp nhận:** Đủ hồ sơ nghiệm thu bốn máy in theo AC-02; thời gian tạo và in <2 giây/sản phẩm.

**Gói công việc 1.6.2.1: Hoàn thiện Bộ Tài liệu Dự án**

- **Mã WBS:** 1.6.2.1
- **Mô tả công việc:** Đóng gói SRS, SAD, SOP, User Manual và hướng dẫn vận hành/sao lưu. BA bàn giao tài liệu nghiệp vụ trước cuối tháng 5; PM/Onsite và Tech Lead/Backend cập nhật phần thuộc trách nhiệm của mình.
- **Người chịu trách nhiệm:** PM / Onsite Engineer / Solution Architect
- **Sản phẩm đầu ra:** Bộ hồ sơ tài liệu dự án hoàn chỉnh (Project Documentation Package).
- **Tiêu chí chấp nhận:** Đủ bộ tài liệu đúng phiên bản, dễ đọc và chuyển giao theo AC-04.

**Gói công việc 1.6.3.1: Ký Biên bản UAT & Nghiệm thu Tổng thể với Project Sponsor**

- **Mã WBS:** 1.6.3.1
- **Mô tả công việc:** Tổ chức họp tổng kết với Ban Giám đốc Doanh nghiệp Trà Tân Cương, trình bày kết quả vận hành 3 kho và tiến hành ký Biên bản Nghiệm thu Tổng thể.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Biên bản Nghiệm thu Tổng thể Dự án (Final Acceptance Sign-off).
- **Tiêu chí chấp nhận:** Chủ đầu tư, đại diện các kho và PM xác nhận sản phẩm/bộ điều kiện AC-01–AC-04, theo trách nhiệm ở 04.

**Gói công việc 1.6.3.2: Bàn giao Hệ thống và Đóng Dự án**

- **Mã WBS:** 1.6.3.2
- **Mô tả công việc:** Bàn giao gói phần mềm/hồ sơ triển khai, CSDL, tài khoản quản trị, sao lưu/biên lai khôi phục và hướng dẫn vận hành cho đầu mối doanh nghiệp; xác nhận trách nhiệm chi phí sau tháng 8, hoàn tất thanh toán/đóng dự án. Bảo trì dài hạn là thỏa thuận riêng.
- **Người chịu trách nhiệm:** PM / Solution Architect / Backend Developer
- **Sản phẩm đầu ra:** Hồ sơ bàn giao vận hành và báo cáo đóng dự án.
- **Tiêu chí chấp nhận:** TR-03 đạt AC-04, đầu mối doanh nghiệp ký nhận và trách nhiệm phí duy trì được ghi rõ, bàn giao toàn bộ chậm nhất 02/02/2028.

## 6. Xác nhận và kiểm soát phạm vi

### 6.1 Nghiệm thu theo đầu ra và mốc

1. QA/PM kiểm nội bộ phần bàn giao theo RTM và AC-01–AC-04; lưu kết quả, lỗi và kiểm lại theo Test Plan.
2. Đội dự án gửi sản phẩm và hồ sơ cho chủ đầu tư/đại diện kho liên quan, gồm kết quả kiểm, tài liệu và điểm chưa đạt nếu có.
3. Người dùng thực hiện UAT theo vai trò và đối soát dữ liệu/thiết bị, gồm nhật ký môi trường nhập thủ công.
4. Chủ đầu tư, PM và đại diện kho liên quan xác nhận bàn giao từng phần/tổng thể theo 04 sau khi các tiêu chí đạt; phần chưa đạt được sửa và kiểm lại.

| Mốc | Hạn hoàn thành | Đầu ra | Điều kiện chấp nhận | Đầu mối xác nhận |
| --- | --- | --- | --- | --- |
| M1 | 02/07/2027, cuối tháng 1 | SRS/SAD, yêu cầu dải cân/tem, danh mục tài sản và phương án triển khai | RTM phủ 01–04; dải cân/độ chia, định dạng tem, tài sản sẵn có và phạm vi offline được xác nhận trong SRS/SAD | Chủ đầu tư/PM, đầu mối kho xác nhận nghiệp vụ |
| M2 | 02/10/2027, cuối tháng 4 | Core WMS, kết nối ngoại vi và các chức năng bổ trợ trong RTM | AC-01/AC-02 trên bộ thiết bị mẫu; AC-03 trên dữ liệu đối soát theo Test Plan | PM/đầu mối kỹ thuật |
| M3 | 02/11/2027, cuối tháng 5 | Kho tổng: 2 PC, 2 cân, 2 máy in, 4 scanner và 1 máy chấm công sẵn có; UAT/đào tạo | AC-01/AC-02 cho thiết bị kho tổng, AC-03 và đào tạo AC-04; dữ liệu mở kho đối soát | Đại diện kho tổng/PM |
| M4 | 02/12/2027, chậm nhất cuối tháng 6 | Production và vận hành kho tổng | Môi trường, dữ liệu danh mục/lô/tồn, ngoại vi và người dùng sẵn sàng theo AC-04; kiểm lại delta nếu khác cấu hình đã đạt | Chủ đầu tư/đại diện kho tổng/PM |
| M5 | 02/01/2028, cuối tháng 7 | Mỗi chi nhánh: 1 PC, 1 cân, 1 máy in, 2 scanner, 1 máy chấm công sẵn có; dữ liệu/đào tạo | AC-01/AC-02 từng thiết bị chi nhánh; AC-03 đồng bộ/ngoại tuyến; AC-04 đào tạo trước sử dụng | Hai đại diện chi nhánh/PM |
| M6 | 02/02/2028, cuối tháng 8 | Toàn bộ phần mềm, dữ liệu, tài liệu và hồ sơ vận hành/bàn giao | Tổng hợp AC-01–AC-04, kiểm lại phần thay đổi; đầu mối nhận quản trị/phí duy trì được xác nhận | Chủ đầu tư/đại diện các kho/PM; đơn vị thi công bàn giao |

### 6.2 Kiểm soát thay đổi

Áp dụng quy trình mục 1.2; Change Log ghi yêu cầu, tác động, người duyệt và phiên bản RTM/WBS/tiêu chí/kế hoạch đã cập nhật. Các đề xuất ngoài phạm vi được ghi nhận để xem xét thỏa thuận tiếp theo.

Theo dõi biến động phạm vi bằng cách đối chiếu nội dung yêu cầu/sản phẩm bàn giao với đường cơ sở và các CR đã duyệt. Chi phí, tiến độ và nguồn lực chịu ảnh hưởng được cập nhật trong các kế hoạch tương ứng.

### Nguồn đối chiếu

- [01 Mô tả](01-mo-ta-de-tai.md), [02 Dự toán](02-du-toan-kinh-phi.md), [03 Tôn chỉ cơ sở](03-ton-chi-du-an.md), [04 Tôn chỉ đầy đủ](04-ton-chi-du-an-day-du.md).
- **Bài giảng Quản lý dự án phần mềm — Quản lý phạm vi dự án**, ThS. Ngô Tiến Đức, [tai-lieu/4-scope.pdf](tai-lieu/4-scope.pdf): trang 14 kế hoạch phạm vi; 16–19 yêu cầu/RTM/tuyên bố; 28–32 phân rã; 38 trình bày WBS theo pha; 39–41 nghiệm thu/kiểm soát/bài tập.
- **Project Management Institute (2017), A Guide to the Project Management Body of Knowledge (PMBOK® Guide), Sixth Edition**: §5.2.3.2 RTM (trang 148–149); §5.3.3.1 tuyên bố phạm vi/tiêu chí chấp nhận (154–155); §5.4.3.1 WBS/Dictionary và quy tắc 100% (161–162); §8.1.3.1–8.1.3.2 kế hoạch/chỉ số chất lượng (286–287); §8.3.2.1/8.3.2.4 cỡ mẫu và kiểm thử (303). Số trang theo bản in.
