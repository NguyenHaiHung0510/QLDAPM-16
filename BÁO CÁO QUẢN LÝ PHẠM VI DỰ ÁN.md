**BÁO CÁO QUẢN LÝ PHẠM VI DỰ ÁN (PROJECT SCOPE MANAGEMENT PLAN)**

- **Tên dự án:** Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS)
- **Mã bài tập:** Bài tập Nhóm 16 (PTIT)
- **Người quản lý dự án (PM):** Nguyễn Hải Hưng (Mã SV: B23DCCN371)
- **Nhà tài trợ (Project Sponsor):** Ban Giám đốc Doanh nghiệp / Hợp tác xã Trà Tân Cương (Thái Nguyên)
- **Tổng ngân sách phê duyệt (BAC):** 2.000.000.000 VNĐ (Hai tỷ đồng chẵn)
- **Thời gian thực hiện:** 08 tháng (50 Man-Month / 8 vị trí chuyên môn)

**1\. KẾ HOẠCH QUẢN LÝ PHẠM VI (SCOPE MANAGEMENT PLAN)**

**1.1 Phương pháp thu thập yêu cầu**

Để đảm bảo thu thập đầy đủ yêu cầu nghiệp vụ và kỹ thuật IoT cho 3 kho, nhóm dự án triển khai 3 phương pháp chính:

1. **Phỏng vấn sâu & Khảo sát nghiệp vụ (Interviews):**
   - Làm việc trực tiếp với **6 nhóm người dùng**: Ban Lãnh đạo, Quản lý kho, Thủ kho, Công nhân chế biến/đóng gói, Kế toán kho và Nhân sự logistics/Tài xế.
   - Tập trung làm rõ các quy trình cốt lõi: Nhập chè búp tươi, quy đổi định mức BOM theo độ ẩm, theo dõi tỷ lệ hao hụt chè, kiểm soát vị trí ô/kệ (Zone/Bin/Rack) và quy tắc xuất kho ưu tiên FEFO (First Expired, First Out).
2. **Khảo sát kỹ thuật & Giao thức IoT (Technical & Hardware Survey):**
   - Đội kỹ thuật (_RS232 Engineer_ và _Onsite Engineer_) khảo sát thực tế tại 01 Kho tổng Thái Nguyên và 02 Kho chi nhánh phân phối.
   - Đo đạc và chốt thông số kỹ thuật chuẩn cổng giao tiếp Serial COM/RS232 của **03 Trạm cân điện tử**, cổng điều khiển **04 Máy in tem Zebra**, **08 Máy quét QR** và kết nối **04 Máy chấm công**.
3. **Rà soát chứng từ & Dữ liệu lịch sử:**
   - Tiếp nhận các biểu mẫu sổ sách Excel hiện có, danh mục nhà vườn/đối tác (như Cơ sở cung cấp trà Minh Sơn), công thức tính hao hụt chế biến và dữ liệu tồn kho ban đầu do doanh nghiệp bàn giao.

**1.2 Quy trình kiểm soát thay đổi phạm vi (Scope Change Control Process)**

Mọi đề xuất thay đổi phạm vi (Change Request - CR) phải tuân thủ nghiêm ngặt quy trình 4 bước để bảo vệ mốc tiến độ và ngân sách:

1. **Ghi nhận phiếu CR:** Thành viên hoặc bên liên quan lập phiếu yêu cầu thay đổi (mô tả lý do, tính năng cần thêm/sửa).
2. **Phân tích tác động (Impact Analysis):** PM Nguyễn Hải Hưng phối hợp với Solution Architect đánh giá ảnh hưởng đến:
   - **Mốc găng Go-live Kho tổng Thái Nguyên ở Tháng 6** (mùa vụ chè cao điểm).
   - **Tổng ngân sách BAC 2.0 Tỷ VNĐ** và Quỹ dự phòng rủi ro 143.000.000 VNĐ (7.15%).
3. **Phê duyệt:**
   - _Thay đổi nhỏ:_ Thuộc hạn mức điều phối công việc của PM Nguyễn Hải Hưng.
   - _Thay đổi lớn (vượt ngân sách/trễ mốc Go-live):_ Bắt buộc trình **Project Sponsor (Ban Giám đốc Trà Tân Cương)** phê duyệt bằng văn bản.
4. **Cập nhật & Thực thi:** Cập nhật WBS, WBS Dictionary, Ma trận TRM và thông báo cho 8 nhân sự triển khai.

**2\. MA TRẬN TRUY XUẤT YÊU CẦU (REQUIREMENTS TRACEABILITY MATRIX - RTM)**

| **Mã YC**  | **Loại YC**  | **Nội dung chi tiết yêu cầu**                                            | **Đối tượng sử dụng chính** | **Mã WBS tương ứng** | **Người chịu trách nhiệm** |
| ---------- | ------------ | ------------------------------------------------------------------------ | --------------------------- | -------------------- | -------------------------- |
| **FR-01**  | Chức năng    | Quản lý Mã Lô, định vị ô/kệ (Zone/Bin/Rack) & Xuất kho ưu tiên **FEFO**  | Thủ kho, Quản lý kho        | 1.3.1.1, 1.3.1.2     | Devs / BA                  |
| **FR-02**  | Chức năng    | Định mức chuyển đổi **BOM** theo độ ẩm & Tính tỷ lệ hao hụt chè chế biến | Quản lý kho, Công nhân      | 1.3.2.1              | Devs / BA                  |
| **FR-03**  | Chức năng    | Cảnh báo tự động tồn kho dưới ngưỡng & Báo cáo tuổi hàng (Aging)         | Quản lý kho, Ban Lãnh đạo   | 1.3.2.2              | Devs                       |
| **FR-04**  | Tích hợp IoT | Đọc trực tiếp dữ liệu Cân điện tử qua cổng **COM/RS232** (không trễ)     | Công nhân chế biến/đóng gói | 1.3.3.1              | RS232 Engineer             |
| **FR-05**  | Tích hợp IoT | In tem QR bằng **máy in Zebra** (s/sp) & Quét mã QR kiểm kê              | Công nhân, Thủ kho          | 1.3.3.2, 1.3.3.3     | RS232 Engineer             |
| **FR-06**  | Tích hợp     | Tích hợp dữ liệu điểm danh từ máy chấm công công nhân                    | Kế toán, Quản lý kho        | 1.3.3.3              | Devs                       |
| **FR-07**  | Chức năng    | Quản lý Nhà cung cấp (Trà Minh Sơn), Đơn hàng, Kế toán kho & Tài xế      | Kế toán, Tài xế, Logistics  | 1.3.4.2              | Devs                       |
| **FR-08**  | Chức năng    | Dashboard KPI, báo cáo doanh thu, giá vốn lô trà & tài chính kho         | Ban Lãnh đạo, Kế toán       | 1.3.4.1              | Devs / Solution Architect  |
| **NFR-01** | Kỹ thuật     | Ứng dụng Web chạy ổn định trên máy trạm Windows tại 3 cơ sở              | Tất cả người dùng           | 1.2.3.1, 1.3.1.1     | Solution Architect         |
| **NFR-02** | Kỹ thuật     | Cơ chế đệm dữ liệu ngoại tuyến (Offline Mode) & Tự đồng bộ dữ liệu 3 kho | Thủ kho 3 chi nhánh         | 1.2.3.2, 1.5.2.1     | Solution Architect         |
| **NFR-03** | Chất lượng   | Sai số cân tự động qua RS232 , Thời gian in tem Zebra giây               | Công nhân, Thủ kho          | 1.3.5.1, 1.6.1.1     | QA / RS232 Engineer        |

**3\. TUYÊN BỐ PHẠM VI DỰ ÁN (PROJECT SCOPE STATEMENT)**

**3.1 Mục tiêu dự án**

Triển khai thành công Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS) thống nhất cho 01 Kho tổng chế biến/đóng gói tại Thái Nguyên và 02 Kho chi nhánh phân phối. Dự án thực hiện trong **8 tháng (50 Man-Month)** với tổng ngân sách phê duyệt **BAC = 2.000.000.000 VNĐ**.

**3.2 Phạm vi công việc BAO GỒM (In-Scope)**

- **Nghiên cứu & Thiết kế:** Khảo sát quy trình, lập tài liệu Đặc tả Yêu cầu (SRS), Thiết kế Kiến trúc (SAD), Quy trình thao tác chuẩn (SOP) và Sổ tay hướng dẫn sử dụng (User Manual).
- **Phát triển Phần mềm Web App:** Xây dựng ứng dụng Web chạy trên môi trường máy trạm Windows quản lý Nhập - Xuất - Tồn theo mã lô, sơ đồ ô/kệ Zone/Bin/Rack, thuật toán FEFO, công thức BOM quy đổi độ ẩm/hao hụt, cảnh báo tồn kho, công nợ nhà cung cấp, vận tải và Dashboard KPI.
- **Phát triển Module Service IoT:** Lập trình phần mềm dịch vụ chạy ngầm kết nối chuẩn COM/RS232 cho **03 Trạm cân điện tử**, điều khiển **04 Máy in tem Zebra**, **08 Máy quét QR** và tích hợp **04 Máy chấm công**.
- **Triển khai & Vận hành:**
  - Lắp đặt thiết bị (130 triệu VNĐ), chạy thử UAT và **Go-live Kho tổng Thái Nguyên ở Tháng 6 (MỐC CỨNG)**.
  - Nhân bản hạ tầng và đồng bộ CSDL cho 02 Kho chi nhánh phân phối ở Tháng 7.
  - Đào tạo người dùng, bàn giao dữ liệu khởi tạo từ Excel và Nghiệm thu tổng thể ở Tháng 8.

**3.3 Ngoại vi dự án KHÔNG BAO GỒM (Out-of-Scope)**

- **Không làm Mobile App Native:** Không xây dựng ứng dụng di động iOS/Android (hệ thống chỉ chạy giao diện Web trên máy trạm Windows).
- **Không thi công hạ tầng điện/mạng cơ bản:** Doanh nghiệp Trà Tân Cương tự chịu trách nhiệm chuẩn bị đường truyền Internet và nguồn điện tại 3 kho.
- **Không mua sắm phương tiện logistics:** Không mua xe tải hay máy nâng hạ cơ học (chỉ quản lý dữ liệu vận tải và biên bản giao nhận trên phần mềm).
- **Không nhập liệu lịch sử thủ công:** Doanh nghiệp tự kiểm kê và chuẩn hóa dữ liệu cũ vào mẫu file Excel; nhóm dự án chỉ cung cấp công cụ Import tự động.

**3.4 Tiêu chí thành công & Nghiệm thu**

1. **Kho tổng Thái Nguyên go-live vận hành thực tế đúng Tháng 6 (mùa vụ cao điểm).**
2. **Sai số đọc cân tự động qua RS232 .**
3. **Thời gian tạo và in tem QR Zebra giây / sản phẩm.**
4. **Tổng chi phí thực tế không vượt quá 2.000.000.000 VNĐ.**
5. **Biên bản nghiệm thu tổng thể được duyệt bởi Project Sponsor và PM Nguyễn Hải Hưng.**

**4\. CẤU TRÚC PHÂN CHIA CÔNG VIỆC (WORK BREAKDOWN STRUCTURE - WBS)**

Cây WBS được phân rã chi tiết **4 cấp**, bám sát **6 Mốc tiến độ (Milestones)** và bộ sản phẩm bàn giao của dự án:

Plaintext

1\. DỰ ÁN HỆ THỐNG WMS TRÀ TÂN CƯƠNG (BAC: 2.0 TỶ VNĐ)

│

├── 1.1 Quản lý Dự án (PMO)

│ ├── 1.1.1 Khởi tạo & Lập Kế hoạch

│ │ ├── 1.1.1.1 Xây dựng Kế hoạch Quản lý Dự án Tổng thể (PMP)

│ │ ├── 1.1.1.2 Xây dựng Kế hoạch Quản lý Phạm vi & Từ điển WBS

│ │ └── 1.1.1.3 Lập Tiến độ Chi tiết & Phân bổ Ngân sách BAC 2.0 Tỷ

│ ├── 1.1.2 Giám sát & Điều phối Thực thi

│ │ ├── 1.1.2.1 Tổ chức Họp Giao ban Định kỳ Tuần/Tháng

│ │ ├── 1.1.2.2 Theo dõi, Kiểm soát Chi phí & Quỹ Dự phòng (143 triệu)

│ │ └── 1.1.2.3 Báo cáo Tiến độ Định kỳ cho Project Sponsor

│ └── 1.1.3 Quản lý Thay đổi & Đảm bảo Chất lượng

│ ├── 1.1.3.1 Tiếp nhận & Đánh giá Yêu cầu Thay đổi (CR)

│ └── 1.1.3.2 Đảm bảo Chất lượng Quy trình (QA)

│

├── 1.2 M1: Phân tích Yêu cầu & Thiết kế Kiến trúc (Tháng 1)

│ ├── 1.2.1 Khảo sát Hiện trạng Nghiệp vụ 3 Kho & Thiết bị IoT

│ │ ├── 1.2.1.1 Khảo sát luồng nhập/chế biến/xuất tại Kho tổng Thái Nguyên

│ │ ├── 1.2.1.2 Khảo sát cổng giao tiếp RS232 trạm cân, máy in Zebra & máy chấm công

│ │ └── 1.2.1.3 Thu thập biểu mẫu Excel dữ liệu cũ & định mức BOM

│ ├── 1.2.2 Biên soạn Đặc tả Yêu cầu Phần mềm (SRS)

│ │ ├── 1.2.2.1 Lập đặc tả use-case cho 6 nhóm người dùng

│ │ └── 1.2.2.2 Thống nhất chuẩn giao tiếp RS232/COM & in tem Zebra

│ └── 1.2.3 Thiết kế Kiến trúc Hệ thống (SAD) & CSDL

│ ├── 1.2.3.1 Thiết kế kiến trúc Web App trên máy trạm Windows

│ ├── 1.2.3.2 Thiết kế CSDL đồng bộ 3 kho & cơ chế đệm dữ liệu Offline

│ └── 1.2.3.3 Thiết kế Giao diện (UI/UX) cho Thủ kho, Công nhân & Lãnh đạo

│

├── 1.3 M2: Phát triển Phần mềm Lõi & IoT RS232 (Tháng 2 - Tháng 4)

│ ├── 1.3.1 Phát triển Core WMS & Quản lý Kho

│ │ ├── 1.3.1.1 Lập trình Chức năng Nhập/Xuất/Kiểm kê & Sơ đồ Zone/Bin/Rack

│ │ └── 1.3.1.2 Lập trình Thuật toán Xuất kho Ưu tiên FEFO

│ ├── 1.3.2 Phát triển Module Định mức BOM & Cảnh báo

│ │ ├── 1.3.2.1 Lập trình công thức quy đổi BOM theo độ ẩm & hao hụt chè

│ │ └── 1.3.2.2 Lập trình Cảnh báo tồn kho dưới ngưỡng & Báo cáo tuổi hàng (Aging)

│ ├── 1.3.3 Phát triển Module Kết nối Thiết bị Phần cứng (IoT)

│ │ ├── 1.3.3.1 Lập trình Service kết nối RS232 đọc dữ liệu cân tự động

│ │ ├── 1.3.3.2 Lập trình Module tạo mã QR & điều khiển máy in tem Zebra

│ │ ├── 1.3.3.3 Lập trình tích hợp Máy quét QR & Máy chấm công

│ │ └── 1.3.3.4 Lập trình công cụ Import/Export danh mục chè từ Excel

│ ├── 1.3.4 Phát triển Dashboard & Chức năng Bổ trợ

│ │ ├── 1.3.4.1 Lập trình Dashboard KPI, báo cáo doanh thu & giá vốn cho Lãnh đạo

│ │ └── 1.3.4.2 Lập trình Module Quản lý Nhà cung cấp, Kế toán kho & Tài xế

│ └── 1.3.5 Kiểm thử Tích hợp Nội bộ (Internal Integration Testing)

│ ├── 1.3.5.1 Kiểm thử luồng dữ liệu Cân RS232 đến Web App

│ └── 1.3.5.2 Kiểm thử tốc độ in tem Zebra (<2s) & thuật toán FEFO/BOM

│

├── 1.4 M3 & M4: Triển khai, UAT & Go-Live Kho Tổng Thái Nguyên (Tháng 5 - Tháng 6)

│ ├── 1.4.1 M3: Lắp đặt Thiết bị & Chạy thử UAT Nội bộ (Tháng 5)

│ │ ├── 1.4.1.1 Lắp đặt PC, Trạm cân RS232, Máy in Zebra, Máy quét tại Kho tổng

│ │ ├── 1.4.1.2 Xây dựng kịch bản UAT & Hướng dẫn 6 nhóm người dùng thử nghiệm

│ │ └── 1.4.1.3 Khởi tạo dữ liệu danh mục trà ban đầu từ file Excel

│ └── 1.4.2 M4: GO-LIVE KHO TỔNG THÁI NGUYÊN (MỐC CỨNG - Tháng 6)

│ ├── 1.4.2.1 Chuyển đổi dữ liệu sang môi trường vận hành thực tế

│ ├── 1.4.2.2 Đưa Kho tổng vào vận hành chính thức vụ chè cao điểm

│ └── 1.4.2.3 Onsite hỗ trợ kỹ thuật trực tiếp tại Thái Nguyên

│

├── 1.5 M5: Triển khai & Nhân bản cho 02 Kho Chi nhánh (Tháng 7)

│ ├── 1.5.1 Lắp đặt Phần cứng & Thiết bị tại 02 Kho Chi nhánh Phân phối

│ │ └── 1.5.1.1 Lắp đặt PC, Trạm cân, Máy in Zebra tại 2 chi nhánh

│ ├── 1.5.2 Cấu hình Đồng bộ CSDL Liên kho & Cơ chế hoạt động Offline

│ │ └── 1.5.2.1 Thiết lập cơ chế nhân bản CSDL & Tự đồng bộ bù

│ └── 1.5.3 Đào tạo & Chuyển giao tại 02 Chi nhánh

│ └── 1.5.3.1 Đào tạo thao tác phần mềm cho Thủ kho & Nhân sự 2 chi nhánh

│

└── 1.6 M6: Đào tạo, Nghiệm thu Tổng thể & Đóng Dự án (Tháng 8)

├── 1.6.1 Kiểm định Tiêu chí Thành công

│ ├── 1.6.1.1 Đo đạc sai số cân tự động qua RS232 (< 0,1%)

│ └── 1.6.1.2 Đo thời gian in tem Zebra (< 2 giây/sản phẩm)

├── 1.6.2 Hoàn thiện Bộ Tài liệu Dự án

│ └── 1.6.2.1 Hoàn thiện bộ tài liệu SRS, SAD, SOP & User Manual

└── 1.6.3 Nghiệm thu Tổng thể & Kết thúc Dự án

├── 1.6.3.1 Ký Biên bản UAT & Nghiệm thu Tổng thể với Ban Giám đốc

└── 1.6.3.2 Bàn giao hệ thống, đóng gói mã nguồn & đóng dự án

**5\. BẢNG TỪ ĐIỂN WBS CHI TIẾT (FULL WBS DICTIONARY)**

Dưới đây là mô tả chi tiết cho **100% các gói công việc cấp thấp nhất (Work Packages)** trong cây WBS:

**GIAI ĐOẠN 1: QUẢN LÝ DỰ ÁN (PMO)**

**Gói công việc 1.1.1.1: Xây dựng Kế hoạch Quản lý Dự án Tổng thể (PMP)**

- **Mã WBS:** 1.1.1.1
- **Mô tả công việc:** Lập Kế hoạch Quản lý Dự án tổng hợp đầy đủ các kế hoạch thành phần: phạm vi, tiến độ, chi phí, chất lượng, nhân sự, rủi ro và mua sắm.
- **Người chịu trách nhiệm:** PM Nguyễn Hải Hưng
- **Sản phẩm đầu ra:** Document Kế hoạch Quản lý Dự án (PMP Document).
- **Tiêu chí chấp nhận:** Được Ban Giám đốc phê duyệt; khớp 100% mục tiêu 8 tháng và ngân sách BAC 2.0 Tỷ VNĐ.

**Gói công việc 1.1.1.2: Xây dựng Kế hoạch Quản lý Phạm vi & Từ điển WBS**

- **Mã WBS:** 1.1.1.2
- **Mô tả công việc:** Chi tiết hóa Tuyên bố Phạm vi, Ma trận TRM, phân rã Cây WBS 4 cấp và biên soạn Từ điển WBS toàn diện.
- **Người chịu trách nhiệm:** PM Nguyễn Hải Hưng
- **Sản phẩm đầu ra:** Báo cáo Scope Management Plan & Full WBS Dictionary.
- **Tiêu chí chấp nhận:** Phủ kín 100% các yêu cầu nghiệp vụ kho và tích hợp thiết bị IoT của Trà Tân Cương.

**Gói công việc 1.1.1.3: Lập Tiến độ Chi tiết & Phân bổ Ngân sách BAC 2.0 Tỷ**

- **Mã WBS:** 1.1.1.3
- **Mô tả công việc:** Lập lịch trình làm việc chi tiết cho 8 nhân sự (50 Man-Month); xác định đường găng (Critical Path) hướng tới mốc Go-live Kho tổng Tháng 6; phân bổ ngân sách BAC 2.0 Tỷ VNĐ.
- **Người chịu trách nhiệm:** PM Nguyễn Hải Hưng
- **Sản phẩm đầu ra:** Biểu đồ Gantt Chart & Bảng phân bổ chi phí chi tiết.
- **Tiêu chí chấp nhận:** Bảo đảm mốc Go-live Tháng 6 và tổng chi phí không vượt quá 2.000.000.000 VNĐ.

**Gói công việc 1.1.2.1: Tổ chức Họp Giao ban Định kỳ**

- **Mã WBS:** 1.1.2.1
- **Mô tả công việc:** Tổ chức các buổi họp giao ban tuần/tháng nội bộ nhóm 16 và họp báo cáo định kỳ với Ban Giám đốc Trà Tân Cương.
- **Người chịu trách nhiệm:** PM Nguyễn Hải Hưng
- **Sản phẩm đầu ra:** Biên bản họp (Meeting Minutes) & Danh sách việc cần làm (Action Items).
- **Tiêu chí chấp nhận:** 100% các cuộc họp có biên bản và được ghi nhận tiến độ đầy đủ.

**Gói công việc 1.1.2.2: Theo dõi, Kiểm soát Chi phí & Quỹ Dự phòng (143 triệu)**

- **Mã WBS:** 1.1.2.2
- **Mô tả công việc:** Theo dõi chi phí thực tế (AC) so với kế hoạch (PV), quản lý việc sử dụng Quỹ dự phòng rủi ro 143.000.000 VNĐ (7.15%).
- **Người chịu trách nhiệm:** PM Nguyễn Hải Hưng
- **Sản phẩm đầu ra:** Báo cáo theo dõi ngân sách hàng tháng.
- **Tiêu chí chấp nhận:** Chi phí phát sinh không vượt quá hạn mức dự phòng rủi ro 7.15%.

**Gói công việc 1.1.2.3: Báo cáo Tiến độ Định kỳ cho Project Sponsor**

- **Mã WBS:** 1.1.2.3
- **Mô tả công việc:** Tổng hợp báo cáo tiến độ (Monthly Status Report) gửi Ban Giám đốc Doanh nghiệp Trà Tân Cương.
- **Người chịu trách nhiệm:** PM Nguyễn Hải Hưng
- **Sản phẩm đầu ra:** Báo cáo tiến độ dự án.
- **Tiêu chí chấp nhận:** Báo cáo gửi đúng hạn vào ngày cuối cùng của mỗi tháng.

**Gói công việc 1.1.3.1: Tiếp nhận & Đánh giá Yêu cầu Thay đổi (CR)**

- **Mã WBS:** 1.1.3.1
- **Mô tả công việc:** Tiếp nhận, ghi nhận và phân tích tác động của các phiếu CR về chi phí, tiến độ và kỹ thuật trước khi trình duyệt.
- **Người chịu trách nhiệm:** PM Nguyễn Hải Hưng / Solution Architect
- **Sản phẩm đầu ra:** Nhật ký thay đổi (Change Log) & Báo cáo đánh giá tác động.
- **Tiêu chí chấp nhận:** 100% các CR phải có chữ ký duyệt của PM hoặc Sponsor trước khi thực thi.

**Gói công việc 1.1.3.2: Đảm bảo Chất lượng Quy trình (QA)**

- **Mã WBS:** 1.1.3.2
- **Mô tả công việc:** Kiểm tra, giám sát việc tuân thủ quy trình làm việc, chuẩn coding và quy trình đóng gói phần mềm của nhóm.
- **Người chịu trách nhiệm:** QA Engineer
- **Sản phẩm đầu ra:** Báo cáo kiểm định chất lượng (QA Report).
- **Tiêu chí chấp nhận:** Không vi phạm các quy trình quản lý chất lượng đã đề ra trong PMP.

**GIAI ĐOẠN 2: M1 - PHÂN TÍCH YÊU CẦU & THIẾT KẾ KHIẾN TRÚC (THÁNG 1)**

**Gói công việc 1.2.1.1: Khảo sát Luồng Nhập/Chế biến/Xuất tại Kho Tổng Thái Nguyên**

- **Mã WBS:** 1.2.1.1
- **Mô tả công việc:** Phỏng vấn Chị Đại diện Kho tổng và công nhân tại Kho tổng Thái Nguyên về quy trình thu mua búp tươi, chế biến, đóng gói và lưu kho.
- **Người chịu trách nhiệm:** BA / Onsite Engineer
- **Sản phẩm đầu ra:** Sơ đồ dòng quy trình nghiệp vụ (Business Process Model) Kho tổng.
- **Tiêu chí chấp nhận:** Được đại diện Kho tổng ký xác nhận phản ánh 100% thực tế.

**Gói công việc 1.2.1.2: Khảo sát Cổng Giao tiếp RS232 Trạm Cân, Máy in Zebra & Máy Chấm công**

- **Mã WBS:** 1.2.1.2
- **Mô tả công việc:** Đo đạc cổng kết nối Serial COM của 03 Trạm cân RS232, 04 Máy in Zebra, 08 Máy quét QR và 04 Máy chấm công.
- **Người chịu trách nhiệm:** RS232 Engineer / Onsite Engineer
- **Sản phẩm đầu ra:** Báo cáo khảo sát phần cứng & Bảng thông số kỹ thuật Baud Rate/COM Port.
- **Tiêu chí chấp nhận:** Xác định chính xác giao thức ASCII/Serial để lập trình driver.

**Gói công việc 1.2.1.3: Thu thập Biểu mẫu Excel Dữ liệu Cũ & Định mức BOM**

- **Mã WBS:** 1.2.1.3
- **Mô tả công việc:** Thu thập file Excel danh mục chè, nhà vườn, mẫu sổ sách kế toán và công thức tính hao hụt chè theo độ ẩm.
- **Người chịu trách nhiệm:** BA
- **Sản phẩm đầu ra:** Tập hợp file dữ liệu mẫu & Công thức chuyển đổi BOM.
- **Tiêu chí chấp nhận:** Cung cấp đầy đủ công thức quy đổi độ ẩm phục vụ lập trình module BOM.

**Gói công việc 1.2.2.1: Lập Đặc tả Use-case cho 6 Nhóm Người dùng**

- **Mã WBS:** 1.2.2.1
- **Mô tả công việc:** Biên soạn tài liệu chi tiết use-case cho 6 vai trò: Lãnh đạo, Quản lý kho, Thủ kho, Công nhân, Kế toán kho, Tài xế/Logistics.
- **Người chịu trách nhiệm:** BA / Devs
- **Sản phẩm đầu ra:** Tài liệu Đặc tả Yêu cầu Phần mềm SRS (Functional SRS).
- **Tiêu chí chấp nhận:** Mô tả đầy đủ 100% các luồng thao tác trên hệ thống.

**Gói công việc 1.2.2.2: Thống nhất Chuẩn Giao tiếp RS232/COM & In Tem Zebra**

- **Mã WBS:** 1.2.2.2
- **Mô tả công việc:** Viết tài liệu đặc tả phi chức năng: chuẩn đọc dữ liệu cân không trễ, tốc độ in tem giây/sản phẩm, cơ chế đệm dữ liệu Offline.
- **Người chịu trách nhiệm:** RS232 Engineer / Solution Architect
- **Sản phẩm đầu ra:** Tài liệu SRS phần Phi chức năng & Chuẩn phần cứng.
- **Tiêu chí chấp nhận:** Thống nhất các chỉ số sai số cân và tốc độ in tem s.

**Gói công việc 1.2.3.1: Thiết kế Kiến trúc Web App trên Máy trạm Windows**

- **Mã WBS:** 1.2.3.1
- **Mô tả công việc:** Thiết kế mô hình kiến trúc phần mềm (SAD), mô hình giao tiếp giữa Web Client, Local Service kết nối RS232 và CSDL Server.
- **Người chịu trách nhiệm:** Solution Architect
- **Sản phẩm đầu ra:** Tài liệu Thiết kế Kiến trúc Hệ thống (SAD).
- **Tiêu chí chấp nhận:** Tương thích hoàn toàn với hệ điều hành Windows trên máy trạm tại 3 kho.

**Gói công việc 1.2.3.2: Thiết kế CSDL Đồng bộ 3 Kho & Cơ chế Đệm Dữ liệu Offline**

- **Mã WBS:** 1.2.3.2
- **Mô tả công việc:** Thiết kế ERD CSDL quan hệ, thiết lập bảng lưu trữ mã lô, vị trí Zone/Bin/Rack và cơ chế đệm dữ liệu khi mất kết nối Internet.
- **Người chịu trách nhiệm:** Solution Architect / Devs
- **Sản phẩm đầu ra:** File thiết kế CSDL (Database Schema Design).
- **Tiêu chí chấp nhận:** Đảm bảo khả năng mở rộng đồng bộ cho 3 kho mà không gây xung đột mã lô.

**Gói công việc 1.2.3.3: Thiết kế Giao diện (UI/UX) cho Thủ kho, Công nhân & Lãnh đạo**

- **Mã WBS:** 1.2.3.3
- **Mô tả công việc:** Thiết kế Wireframe/Prototype giao diện Dashboard KPI, màn hình cân-in tem nút bấm to cho công nhân, màn hình quét QR cho thủ kho.
- **Người chịu trách nhiệm:** BA / UI-UX Designer
- **Sản phẩm đầu ra:** Bộ thiết kế Figma/UI Prototype.
- **Tiêu chí chấp nhận:** Giao diện đơn giản, công nhân thao tác cân/in tem không quá 2 bước.

**GIAI ĐOẠN 3: M2 - PHÁT TRIỂN PHẦN MỀM LÕI & IOT RS232 (THÁNG 2 - THÁNG 4)**

**Gói công việc 1.3.1.1: Lập trình Chức năng Nhập/Xuất/Kiểm kê & Sơ đồ Zone/Bin/Rack**

- **Mã WBS:** 1.3.1.1
- **Mô tả công việc:** Viết mã nguồn module Nhập kho, Xuất kho, Điều chuyển và sơ đồ định vị vị trí lưu trữ theo ô/kệ (Zone/Bin/Rack).
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module Quản lý Kho Lõi (Core WMS).
- **Tiêu chí chấp nhận:** Định vị chuẩn xác vị trí lô trà trên sơ đồ kho.

**Gói công việc 1.3.1.2: Lập trình Thuật toán Xuất kho Ưu tiên FEFO**

- **Mã WBS:** 1.3.1.2
- **Mô tả công việc:** Viết thuật toán gợi ý xuất kho tự động ưu tiên các lô trà có hạn sử dụng gần nhất (First Expired, First Out).
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module xử lý FEFO Logic.
- **Tiêu chí chấp nhận:** Gợi ý xuất kho chính xác 100% theo ngày hết hạn của mã lô.

**Gói công việc 1.3.2.1: Lập trình Công thức Quy đổi BOM theo Độ ẩm & Hao hụt Chè**

- **Mã WBS:** 1.3.2.1
- **Mô tả công việc:** Lập trình công thức quy đổi khối lượng trà búp tươi sang thành phẩm dựa trên chỉ số độ ẩm đo được và tính toán tỷ lệ hao hụt.
- **Người chịu trách nhiệm:** Devs / BA
- **Sản phẩm đầu ra:** Module BOM & Processing Loss.
- **Tiêu chí chấp nhận:** Tính toán chính xác định mức chế biến trà theo công thức đã phê duyệt.

**Gói công việc 1.3.2.2: Lập trình Cảnh báo Tồn kho Dưới ngưỡng & Báo cáo Tuổi hàng (Aging)**

- **Mã WBS:** 1.3.2.2
- **Mô tả công việc:** Viết module gửi thông báo cảnh báo tự động khi số lượng trà trong kho rơi xuống dưới ngưỡng an toàn và lập báo cáo thời gian lưu kho của từng lô chè.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module Cảnh báo & Aging Report.
- **Tiêu chí chấp nhận:** Cảnh báo hiển thị thời gian thực trên màn hình Quản lý kho.

**Gói công việc 1.3.3.1: Lập trình Service Kết nối RS232 Đọc Dữ liệu Cân Tự động**

- **Mã WBS:** 1.3.3.1
- **Mô tả công việc:** Lập trình Windows Service chạy ẩn nhận dữ liệu chuỗi từ 03 trạm cân RS232, tự động điền chỉ số trọng lượng vào ứng dụng Web mà không cần gõ tay.
- **Người chịu trách nhiệm:** RS232 Engineer
- **Sản phẩm đầu ra:** Windows Service IoT RS232 Connector.
- **Tiêu chí chấp nhận:** Đọc dữ liệu liên tục không gián đoạn, sai số truyền nhận .

**Gói công việc 1.3.3.2: Lập trình Module Tạo Mã QR & Điều khiển Máy in Tem Zebra**

- **Mã WBS:** 1.3.3.2
- **Mô tả công việc:** Lập trình thuật toán sinh mã QR chứa thông tin mã lô, ngày đóng gói, trọng lượng; truyền lệnh in đến 04 máy in tem Zebra.
- **Người chịu trách nhiệm:** RS232 Engineer
- **Sản phẩm đầu ra:** Module QRCode & Zebra Printer Driver Integration.
- **Tiêu chí chấp nhận:** Tem QR in ra sắc nét, tốc độ xử lý và in giây/sản phẩm.

**Gói công việc 1.3.3.3: Lập trình Tích hợp Máy quét QR & Máy chấm công**

- **Mã WBS:** 1.3.3.3
- **Mô tả công việc:** Viết module nhận diện dữ liệu từ 08 Máy quét QR kiểm kê và kết nối dữ liệu điểm danh công nhân từ 04 Máy chấm công.
- **Người chịu trách nhiệm:** Devs / RS232 Engineer
- **Sản phẩm đầu ra:** Sub-module Barcode Scanner & Timekeeper Sync.
- **Tiêu chí chấp nhận:** Quét mã QR chính xác 100%; dữ liệu chấm công đồng bộ theo ca làm việc.

**Gói công việc 1.3.3.4: Lập trình Công cụ Import/Export Danh mục Chè từ Excel**

- **Mã WBS:** 1.3.3.4
- **Mô tả công việc:** Viết công cụ cho phép tải file Excel danh mục trà tươi, nhà vườn, giá vốn nhập thẳng vào CSDL.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Tool Import/Export Excel.
- **Tiêu chí chấp nhận:** Báo lỗi chi tiết dòng/cột nếu file Excel sai định dạng.

**Gói công việc 1.3.4.1: Lập trình Dashboard KPI, Báo cáo Doanh thu & Giá vốn cho Lãnh đạo**

- **Mã WBS:** 1.3.4.1
- **Mô tả công việc:** Lập trình giao diện Dashboard báo cáo KPI xuất nhập kho, tỷ lệ hao hụt chè, doanh thu xuất kho và biểu đồ giá vốn cho Ban Lãnh đạo.
- **Người chịu trách nhiệm:** Devs / Solution Architect
- **Sản phẩm đầu ra:** Module Executive Dashboard.
- **Tiêu chí chấp nhận:** Biểu đồ trực quan, số liệu cập nhật tự động theo thời gian thực.

**Gói công việc 1.3.4.2: Lập trình Module Quản lý Nhà cung cấp, Kế toán Kho & Tài xế**

- **Mã WBS:** 1.3.4.2
- **Mô tả công việc:** Xây dựng module quản lý công nợ nhà cung cấp trà búp tươi, chi phí vật tư bao bì cho Kế toán kho và xác nhận biên bản giao nhận hàng cho Tài xế.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module Partner, Accounting & Transport Management.
- **Tiêu chí chấp nhận:** Quản lý chính xác công nợ và trạng thái các chuyến xe điều chuyển giữa 3 kho.

**Gói công việc 1.3.5.1: Kiểm thử Luồng Dữ liệu Cân RS232 đến Web App**

- **Mã WBS:** 1.3.5.1
- **Mô tả công việc:** Tiến hành Test giả lập dữ liệu cân truyền từ trạm cân RS232 về giao diện Web App.
- **Người chịu trách nhiệm:** QA / RS232 Engineer
- **Sản phẩm đầu ra:** Báo cáo Integration Test - RS232 Data Flow.
- **Tiêu chí chấp nhận:** Sai số cân ; không bị đứt kết nối khi cân liên tục 100 lần.

**Gói công việc 1.3.5.2: Kiểm thử Tốc độ In Tem Zebra & Thuật toán FEFO/BOM**

- **Mã WBS:** 1.3.5.2
- **Mô tả công việc:** Kiểm thử hiệu năng in tem QR Zebra và tính chính xác của công thức quy đổi BOM, quy tắc FEFO.
- **Người chịu trách nhiệm:** QA / Devs
- **Sản phẩm đầu ra:** Báo cáo Integration Test - Performance & Business Logic.
- **Tiêu chí chấp nhận:** Thời gian in tem s; tính toán BOM và FEFO đạt chính xác 100%.

**GIAI ĐOẠN 4: M3 & M4 - TRIỂN KHAI & GO-LIVE KHO TỔNG THÁI NGUYÊN (THÁNG 5 - THÁNG 6)**

**Gói công việc 1.4.1.1: Lắp đặt PC, Trạm Cân RS232, Máy in Zebra, Máy quét tại Kho Tổng**

- **Mã WBS:** 1.4.1.1
- **Mô tả công việc:** Vận chuyển, lắp đặt phần cứng (01 PC Windows, 01 Trạm cân RS232, 02 Máy in Zebra, 04 Máy quét QR, 02 Máy chấm công) tại Kho tổng Thái Nguyên.
- **Người chịu trách nhiệm:** Onsite Engineer / RS232 Engineer
- **Sản phẩm đầu ra:** Hạ tầng phần cứng hoàn chỉnh tại Kho tổng Thái Nguyên.
- **Tiêu chí chấp nhận:** Tất cả thiết bị lên nguồn, kết nối thông suốt với mạng và phần mềm.

**Gói công việc 1.4.1.2: Xây dựng Kịch bản UAT & Hướng dẫn 6 Nhóm Người dùng Thử nghiệm**

- **Mã WBS:** 1.4.1.2
- **Mô tả công việc:** Lập tài liệu Test Case UAT và hướng dẫn trực tiếp Chị Đại diện Kho tổng, thủ kho, công nhân Thái Nguyên thao tác thử nghiệm.
- **Người chịu trách nhiệm:** PM Nguyễn Hải Hưng / BA / Onsite Engineer
- **Sản phẩm đầu ra:** Kịch bản UAT & Biên bản UAT Nội bộ Kho tổng.
- **Tiêu chí chấp nhận:** Được đại diện người dùng Kho tổng ký nghiệm thu UAT.

**Gói công việc 1.4.1.3: Khởi tạo Dữ liệu Danh mục Trà Ban đầu từ File Excel**

- **Mã WBS:** 1.4.1.3
- **Mô tả công việc:** Sử dụng công cụ Import để đưa danh mục trà tươi, nhà vườn, danh mục bao bì ban đầu vào CSDL Kho tổng.
- **Người chịu trách nhiệm:** Onsite Engineer / BA
- **Sản phẩm đầu ra:** CSDL Kho tổng được khởi tạo đầy đủ dữ liệu ban đầu.
- **Tiêu chí chấp nhận:** Dữ liệu khởi tạo khớp 100% với bảng đối soát của Doanh nghiệp.

**Gói công việc 1.4.2.1: Chuyển đổi Dữ liệu Sang Môi trường Vận hành Thực tế**

- **Mã WBS:** 1.4.2.1
- **Mô tả công việc:** Khóa dữ liệu kiểm thử, thực hiện chốt sổ tồn kho thực tế và chuyển sang môi trường Production tại Kho tổng.
- **Người chịu trách nhiệm:** Solution Architect / Devs
- **Sản phẩm đầu ra:** Hệ thống WMS Production sẵn sàng vận hành.
- **Tiêu chí chấp nhận:** Dữ liệu tồn kho ban đầu chính xác, không còn dữ liệu rác từ quá trình UAT.

**Gói công việc 1.4.2.2: Đưa Kho Tổng vào Vận hành Chính thức Vụ Chè Cao điểm**

- **Mã WBS:** 1.4.2.2
- **Mô tả công việc:** Kích hoạt hệ thống chính thức (Go-live) tại Kho tổng Thái Nguyên phục vụ nhập chè tươi, đóng gói, lưu kho trong mùa vụ cao điểm.
- **Người chịu trách nhiệm:** PM Nguyễn Hải Hưng & Onsite Engineer
- **Sản phẩm đầu ra:** Biên bản Xác nhận Go-live Kho Tổng Thái Nguyên.
- **Tiêu chí chấp nhận:** **MỐC CỨNG - Phải hoàn thành đúng Tháng 6**; hệ thống vận hành thực tế không trễ, nghẽn.

**Gói công việc 1.4.2.3: Onsite Hỗ trợ Kỹ thuật Trực tiếp tại Thái Nguyên**

- **Mã WBS:** 1.4.2.3
- **Mô tả công việc:** Túc trực trực tiếp tại Kho tổng Thái Nguyên trong 2 tuần đầu Go-live để xử lý sự cố phát sinh.
- **Người chịu trách nhiệm:** Onsite Engineer / RS232 Engineer
- **Sản phẩm đầu ra:** Báo cáo nhật ký hỗ trợ Go-live (Onsite Support Log).
- **Tiêu chí chấp nhận:** Xử lý 100% sự cố kỹ thuật trong vòng 15 phút từ khi phát sinh.

**GIAI ĐOẠN 5: M5 - TRIỂN KHAI 02 KHO CHI NHÁNH (THÁNG 7)**

**Gói công việc 1.5.1.1: Lắp đặt Phần cứng & Thiết bị tại 02 Kho Chi nhánh Phân phối**

- **Mã WBS:** 1.5.1.1
- **Mô tả công việc:** Vận chuyển, cài đặt 03 PC Windows, 02 Trạm cân RS232, 02 Máy in Zebra, 04 Máy quét QR, 02 Máy chấm công tại 02 Kho chi nhánh phân phối.
- **Người chịu trách nhiệm:** Onsite Engineer
- **Sản phẩm đầu ra:** Bàn giao hạ tầng phần cứng hoàn chỉnh tại 02 Kho chi nhánh.
- **Tiêu chí chấp nhận:** Toàn bộ thiết bị kết nối thành công với máy trạm và mạng.

**Gói công việc 1.5.2.1: Cấu hình Đồng bộ CSDL Liên kho & Cơ chế Hoạt động Offline**

- **Mã WBS:** 1.5.2.1
- **Mô tả công việc:** Cấu hình đường truyền đồng bộ CSDL giữa 02 Chi nhánh với Kho tổng trung tâm; bật tính năng lưu dữ liệu Offline khi mất mạng.
- **Người chịu trách nhiệm:** Solution Architect / Devs
- **Sản phẩm đầu ra:** Hệ thống CSDL Đồng bộ 3 Kho (Multi-site Database Sync).
- **Tiêu chí chấp nhận:** Dữ liệu tự động đồng bộ bù ngay khi có kết nối Internet trở lại.

**Gói công việc 1.5.3.1: Đào tạo Thao tác Phần mềm cho Thủ kho & Nhân sự 2 Chi nhánh**

- **Mã WBS:** 1.5.3.1
- **Mô tả công việc:** Tổ chức các lớp hướng dẫn sử dụng phần mềm, quét mã QR kiểm kê, nhận hàng điều chuyển cho nhân sự tại 02 chi nhánh.
- **Người chịu trách nhiệm:** Onsite Engineer / BA
- **Sản phẩm đầu ra:** Báo cáo kết quả đào tạo & Danh sách điểm danh.
- **Tiêu chí chấp nhận:** 100% thủ kho và nhân sự 2 chi nhánh đạt bài kiểm tra thao tác thực hành.

**GIAI ĐOẠN 6: M6 - NGHIỆM THU TỔNG THỂ & ĐÓNG DỰ ÁN (THÁNG 8)**

**Gói công việc 1.6.1.1: Đo đạc Sai số Cân Tự động qua RS232**

- **Mã WBS:** 1.6.1.1
- **Mô tả công việc:** Tiến hành nghiệm thu kỹ thuật, đo đạc sai số thực tế khi cân trà tự động qua cổng RS232 tại 3 kho.
- **Người chịu trách nhiệm:** RS232 Engineer / QA
- **Sản phẩm đầu ra:** Biên bản kiểm định Tiêu chí Cân tự động.
- **Tiêu chí chấp nhận:** **Sai số cân tự động** .

**Gói công việc 1.6.1.2: Đo Thời gian Tạo & In Tem Zebra**

- **Mã WBS:** 1.6.1.2
- **Mô tả công việc:** Đo đạc tốc độ xử lý tạo mã QR và in tem nhãn Zebra thực tế trên dây chuyền.
- **Người chịu trách nhiệm:** RS232 Engineer / QA
- **Sản phẩm đầu ra:** Biên bản kiểm định Tiêu chí In tem Zebra.
- **Tiêu chí chấp nhận:** **Thời gian in tem giây/sản phẩm**.

**Gói công việc 1.6.2.1: Hoàn thiện Bộ Tài liệu Dự án**

- **Mã WBS:** 1.6.2.1
- **Mô tả công việc:** Đóng gói toàn bộ bộ tài liệu: Đặc tả SRS, Thiết kế SAD, Quy trình thao tác chuẩn SOP và Sổ tay hướng dẫn sử dụng User Manual.
- **Người chịu trách nhiệm:** BA / PM Nguyễn Hải Hưng
- **Sản phẩm đầu ra:** Bộ hồ sơ tài liệu dự án hoàn chỉnh (Project Documentation Package).
- **Tiêu chí chấp nhận:** Đầy đủ 4 bộ tài liệu chuẩn format, dễ đọc, dễ chuyển giao.

**Gói công việc 1.6.3.1: Ký Biên bản UAT & Nghiệm thu Tổng thể với Project Sponsor**

- **Mã WBS:** 1.6.3.1
- **Mô tả công việc:** Tổ chức họp tổng kết với Ban Giám đốc Doanh nghiệp Trà Tân Cương, trình bày kết quả vận hành 3 kho và tiến hành ký Biên bản Nghiệm thu Tổng thể.
- **Người chịu trách nhiệm:** PM Nguyễn Hải Hưng
- **Sản phẩm đầu ra:** Biên bản Nghiệm thu Tổng thể Dự án (Final Acceptance Sign-off).
- **Tiêu chí chấp nhận:** Đủ chữ ký của Project Sponsor (Ban Giám đốc) và PM Nguyễn Hải Hưng.

**Gói công việc 1.6.3.2: Bàn giao Hệ thống, Đóng gói Mã nguồn & Đóng Dự án**

- **Mã WBS:** 1.6.3.2
- **Mô tả công việc:** Bàn giao bản quyền phần mềm, tài khoản quản trị CSDL, mã nguồn (Source code), giải ngân thanh toán tài chính và giải thể nhóm dự án.
- **Người chịu trách nhiệm:** PM Nguyễn Hải Hưng
- **Sản phẩm đầu ra:** Báo cáo Tổng kết Đóng Dự án (Project Closure Report).
- **Tiêu chí chấp nhận:** Hoàn tất bàn giao tài sản, thanh toán hợp đồng, không còn khiếu nại hay tồn đọng rủi ro.

6. XÁC NHẬN & KIỂM SOÁT PHẠM VI (SCOPE VALIDATION & CONTROL)

6.1 Quy trình Nghiệm thu & Xác nhận Phạm vi (Scope Validation Process)
Xác nhận phạm vi là quá trình nghiệm thu chính thức các sản phẩm bàn giao (Deliverables) từng phần và toàn phần giữa Đơn vị thi công, Người quản lý dự án (PM) với Đại diện Chủ đầu tư và Đại diện các kho sử dụng.

6.1.1 Quy trình 4 bước nghiệm thu sản phẩm bàn giao
1. Bước 1: Kiểm định Chất lượng Nội bộ (Internal QA/QC Check)
   * Trước mỗi mốc bàn giao 05 ngày, Bộ phận QA và PM tiến hành kiểm tra nội bộ toàn bộ tính năng phần mềm, kịch bản đệm dữ liệu Offline và đo đạc các tiêu chí kỹ thuật (sai số cân tự động qua RS232 < 0,1%, thời gian tạo và in tem Zebra < 2 giây/sản phẩm).
2. Bước 2: Gửi Hồ sơ & Sản phẩm Bàn giao (Deliverable Submission)
   * PM gửi Hồ sơ bàn giao (Mã nguồn, Tài liệu SRS, SAD, SOP, Sổ tay hướng dẫn sử dụng, Báo cáo kết quả kiểm thử nội bộ) cho Đại diện Chủ đầu tư và Đại diện các kho liên quan (Đại diện Kho tổng, Đại diện Kho chi nhánh 1 & 2).
3. Bước 3: Đánh giá & Kiểm thử Chấp nhận Người dùng (UAT)
   * Các nhóm người dùng trực tiếp (Lãnh đạo, Quản lý kho, Thủ kho, Công nhân chế biến/đóng gói, Kế toán kho, Nhân sự logistics/Tài xế) thực hiện thao tác kiểm thử thực tế trên giao diện máy trạm Windows và thiết bị IoT dưới sự hướng dẫn của Đội Kỹ thuật Onsite.
4. Bước 4: Ký Biên bản Nghiệm thu Chính thức (Official Sign-off)
   * Nếu sản phẩm đạt 100% tiêu chí chấp nhận đã quy định trong WBS Dictionary, Đại diện Chủ đầu tư, PM và Đại diện các kho tiến hành ký Biên bản Nghiệm thu Chuyển giao từng phần hoặc Biên bản Nghiệm thu Tổng thể.

6.1.2 Bảng Danh mục Nghiệm thu Chi tiết theo 6 Mốc Tiến độ (Milestones)

| Mốc | Hạn hoàn thành | Sản phẩm bàn giao chính | Tiêu chí Nghiệm thu Chấp nhận (Acceptance Criteria) | Đầu mối Ký Phê duyệt |
| :--- | :--- | :--- | :--- | :--- |
| **M1** | **02/07/2027** (Cuối tháng 1) | Bộ tài liệu Đặc tả Yêu cầu Phần mềm (SRS) & Thiết kế Kiến trúc (SAD) | Phủ kín 100% use-case cho 6 nhóm người dùng; thiết kế CSDL đồng bộ 3 kho; khung bộ tài liệu SOP & User Manual. | Đại diện Chủ đầu tư & Người quản lý dự án (PM) |
| **M2** | **02/10/2027** (Cuối tháng 4) | Phiên bản Phần mềm WMS Lõi, Service IoT RS232 & Driver In Zebra | Hoàn thành module Nhập/Xuất/Tồn, FEFO, BOM (độ ẩm/hao hụt); Service đọc cân RS232 mượt mà; module in tem Zebra đạt < 2s/sp. | PM & Đầu mối Đội kỹ thuật |
| **M3** | **02/11/2027** (Cuối tháng 5) | Hạ tầng phần cứng & Kết quả UAT Nội bộ tại Kho tổng Thái Nguyên | Lắp đặt 01 máy trạm, 01 trạm cân RS232, 02 máy in Zebra, 04 máy quét QR, 02 máy chấm công; 100% UAT Test Cases PASSED. | Đại diện Kho tổng & PM |
| **M4** | **02/12/2027** (**MỐC CỨNG** - Cuối tháng 6) | **Chính thức Go-live & Đưa Kho tổng Thái Nguyên vào vận hành thực tế** | Phần mềm chuyển sang môi trường Production; phục vụ trực tiếp vụ chè cao điểm; đọc cân/in tem trơn tru; import 100% CSDL từ Excel. | Đại diện Chủ đầu tư & Đại diện Kho tổng |
| **M5** | **02/01/2028** (Cuối tháng 7) | Triển khai Phần cứng & Đồng bộ CSDL tại 02 Kho chi nhánh | Lắp đặt xong thiết bị tại 2 chi nhánh; cơ chế đệm dữ liệu Offline Mode & Tự động đồng bộ bù (Auto-resync) hoạt động chính xác. | Đại diện Kho chi nhánh 1, Đại diện Kho chi nhánh 2 & PM |
| **M6** | **02/02/2028** (Cuối tháng 8) | Bàn giao Phần mềm Hoàn chỉnh, CSDL Đồng bộ 03 kho & Nghiệm thu Tổng thể | Sai số cân < 0,1%; thời gian in tem < 2s; bàn giao 100% tài liệu (SRS, SAD, SOP, User Manual); ký Biên bản Nghiệm thu Tổng thể & Đóng dự án. | Đại diện Chủ đầu tư, Đại diện Đơn vị thi công & PM |

---

6.2 Cơ chế Kiểm soát & Chống Phình đại Phạm vi (Scope Creep Control)

Phình đại phạm vi (Scope Creep) là rủi ro lớn nhất làm trễ mốc Go-live Kho tổng (02/12/2027) và vượt Ngân sách phê duyệt (BAC = 2.000.000.000 VNĐ). Dự án áp dụng các nguyên tắc kiểm soát nghiêm ngặt:

6.2.1 Nguyên tắc Kiểm soát Yêu cầu Phát sinh
1. Nguyên tắc "Zero Unauthorized Changes" (Không tự ý thay đổi):
   * Các lập trình viên và kỹ sư IoT tuyệt đối không tự ý tiếp nhận hoặc phát triển các tính năng theo yêu cầu truyền miệng từ nhân sự tại các nhà kho.
   * Mọi yêu cầu thay đổi phải được cụ thể hóa bằng văn bản thông qua Phiếu Yêu cầu Thay đổi (Change Request - CR Form).
2. Tuyên bố Rào cản Phạm vi (Out-of-Scope Enforcement):
   * Kiên quyết từ chối thực hiện trong giai đoạn này các hạng mục ngoài phạm vi đã cam kết:
     * *Không phát triển Ứng dụng Di động Native (iOS/Android).*
     * *Không thi công kéo cáp mạng, sửa chữa hạ tầng điện/Internet tại các kho.*
     * *Không tích hợp thiết bị định vị GPS cơ học cho xe tải logistics.*
     * *Không thực hiện nhập liệu thủ công sổ sách lịch sử từ quá khứ.*
3. Quản lý Danh sách Chờ Giai đoạn 2 (Backlog Management):
   * Các đề xuất phát sinh hợp lý nhưng ngoài Tuyên bố Phạm vi ban đầu sẽ được PM ghi nhận vào **Danh sách Chờ (Product Backlog)** để xem xét xây dựng hợp đồng nâng cấp riêng sau khi dự án hoàn thành nghiệm thu tổng thể vào ngày 02/02/2028.

6.2.2 Quy trình Xử lý Phiếu Yêu cầu Thay đổi (Change Request - CR)

              [Đề xuất thay đổi mới từ Người dùng / Chủ đầu tư]
                                     │
                                     ▼
                          [Lập Phiếu CR Form chuẩn]
                                     │
                                     ▼
                   [PM & Đầu mối Kỹ thuật Đánh giá Tác động]
                      ├── 1. Có trễ mốc Go-live 02/12/2027?
                      ├── 2. Có vượt Ngân sách BAC 2.0 Tỷ VNĐ?
                      └── 3. Có vượt Quỹ Dự phòng Rủi ro (143 triệu)?
                                     │
             ┌───────────────────────┴───────────────────────┐
      (Có ảnh hưởng)                                  (Không ảnh hưởng)
             │                                               │
             ▼                                               ▼
[Trình Đại diện Chủ đầu tư                     [PM Phê duyệt Thực thi]
  Phê duyệt Bằng Văn bản]                                    │
             │                                               │
             └───────────────────────┬───────────────────────┘
                                     │
                                     ▼
               [Cập nhật WBS, WBS Dictionary & Tiến độ Baseline]

6.2.3 Bảng Chỉ số Đo lường Hiệu quả Kiểm soát Phạm vi (Scope KPIs)

| Chỉ số KPI | Ngưỡng Mục tiêu | Phương pháp Đo lường & Công cụ |
| :--- | :--- | :--- |
| **Tỷ lệ biến động Phạm vi (Scope Variance)** | $0\%$ (Không phình đại) | So sánh số lượng Work Packages hoàn thành thực tế với WBS Baseline ban đầu. |
| **Số lượng CR được phê duyệt** | $\le 3$ phiếu trong suốt dự án | Đánh giá qua Nhật ký Thay đổi (Change Log). |
| **Tác động Chi phí từ CR** | $\le 143.000.000$ VNĐ | Nằm gọn trong Quỹ dự phòng rủi ro Contingency Reserve ($7,15\%$). |
| **Tác động Tiến độ từ CR** | $0$ ngày | Không làm dời mốc Go-live Kho tổng (02/12/2027) và mốc Nghiệm thu (02/02/2028). |