# CHIẾN LƯỢC CẤU TRÚC: TÔN CHỈ DỰ ÁN (PROJECT CHARTER)
**Đề tài:** Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS)  
**Tài liệu tham khảo cấu trúc:** Bài giảng Khởi tạo dự án, [tai-lieu/3-initial.pdf](tai-lieu/3-initial.pdf#page=36), trang 36; PMBOK 6 §4.1.3.1, trang 81. Bản tôn chỉ đầy đủ xem [04](04-ton-chi-du-an-day-du.md).

```
                                      CẤU TRÚC 5 PHẦN CỐT LÕI
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. THÔNG TIN CHUNG & QUYỀN HẠN PM  │ Dự án, Nhà tài trợ, PM, Quyền điều phối ngân sách 2 tỷ & 8 NS     │
├────────────────────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 2. TỔNG QUAN & ĐỐI TƯỢNG SỬ DỤNG   │ Mô hình 3 kho + Bảng 6 nhóm người dùng (từ Thủ kho đến Giám đốc)  │
├────────────────────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 3. SẢN PHẨM BÀN GIAO & BÊN LIÊN QUAN│ 4 nhóm bàn giao (App, IoT RS232, Docs, UAT) + Ma trận Stakeholder│
├────────────────────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 4. MỐC TIẾN ĐỘ & NGÂN SÁCH (BAC)   │ Bảng 6 Milestones (Mốc cứng Tháng 6) + Bảng bóc tách BAC 2.0 Tỷ   │
├────────────────────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 5. RÀNG BUỘC, GIẢ ĐỊNH & PHÊ DUYỆT │ Bảng Constraints (Tháng 6, RS232) + Assumption Log + Tiêu chí     │
└────────────────────────────────────┴───────────────────────────────────────────────────────────────────┘
```

---

## 1. Thông tin chung & Trao quyền cho Người quản lý dự án (PM)
*   **Tên dự án:** Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS).
*   **Mục tiêu cốt lõi:** Số hóa toàn diện quy trình nhập – chế biến/đóng gói – bảo quản – xuất kho cho 3 cơ sở kho của Doanh nghiệp Trà Tân Cương.
*   **Đơn vị thực hiện:** Công ty Cổ phần Công nghệ Raumania (tình huống dự án giả định; nhóm 16 thực hiện BTL).
*   **Người quản lý dự án (PM):** Bùi Hồng Phú — Điều phối 8 vị trí chuyên môn (50 Man-Month) trong phạm vi và ngân sách 2.000.000.000 VNĐ đã được chủ đầu tư phê duyệt; thay đổi đường cơ sở phải trình chủ đầu tư.
*   **Nhà tài trợ (Project Sponsor):** Ban Giám đốc Doanh nghiệp / Hợp tác xã Trà Tân Cương (Thái Nguyên).

---

## 2. Tổng quan hệ thống & Đối tượng sử dụng
*   **Tổng quan:** Website chạy trên máy trạm Windows tại 3 cơ sở (01 Kho tổng chế biến/đóng gói tại Thái Nguyên + 02 Kho chi nhánh phân phối), tích hợp trực tiếp Cân điện tử RS232, máy in tem theo chuẩn tương thích, máy quét QR và máy chấm công. Xử lý nghiệp vụ nông sản: Định mức chuyển đổi BOM theo độ ẩm, thuật toán xuất kho FEFO.
*   **Bảng phân vai 6 nhóm người dùng:**
    1.  *Ban Lãnh đạo:* Xem Dashboard KPI, doanh thu xuất kho, tỷ lệ hao hụt chè, báo cáo tuổi hàng (Aging).
    2.  *Quản lý kho tổng/chi nhánh:* Duyệt lệnh nhập/xuất/chuyển kho, thiết lập ngưỡng tồn kho tối thiểu.
    3.  *Thủ kho:* Quét mã QR kiểm kê, định vị ô/kệ (Zone/Bin/Rack), ghi nhận nhật ký nhiệt độ/độ ẩm.
    4.  *Công nhân chế biến/đóng gói:* Thao tác cân trọng lượng tự động qua RS232, in tem QR dán gói trà.
    5.  *Kế toán kho:* Theo dõi giá vốn lô trà, công nợ nhà cung cấp nông trường, chi phí vật tư bao bì.
    6.  *Nhân sự logistics/Tài xế:* Xác nhận biên bản giao nhận hàng điều phối giữa 3 kho.

---

## 3. Sản phẩm bàn giao & Các bên liên quan
*   **4 Nhóm sản phẩm bàn giao (Key Deliverables):**
    1.  *Gói phần mềm WMS:* Web App quản lý kho hoàn chỉnh + Service kết nối phần cứng COM/RS232 + CSDL đồng bộ 3 kho.
    2.  *Hạ tầng & Thiết bị (130 triệu):* 04 Cân RS232, 04 Máy in tem, 08 Máy quét QR, 04 PC Windows (kho tổng: 2/2/4/2; mỗi chi nhánh: 1/1/2/1 theo 02) đã lắp đặt và cấu hình sẵn sàng tại 3 kho.
    3.  *Bộ tài liệu kỹ thuật & quy trình:* Đặc tả yêu cầu (SRS), Thiết kế kiến trúc (SAD), Quy trình thao tác chuẩn (SOP), Sổ tay hướng dẫn sử dụng (User Manual).
    4.  *Nghiệm thu & Vận hành:* Dữ liệu danh mục trà khởi tạo thành công, Biên bản kiểm thử UAT có chữ ký xác nhận của đại diện 3 kho.
*   **Ma trận các bên liên quan (Stakeholder Matrix):**
    *   *Nội bộ:* PM, Solution Architect, RS232 Engineer, BA, Devs, QA, Onsite Engineer (khớp bảng 8 nhân sự).
    *   *Bên ngoài:* Ban Giám đốc Trà Tân Cương (Chủ đầu tư), Thủ kho & Công nhân tại 3 kho (Người dùng cuối), Nhà cung cấp trà búp tươi, Đối tác thiết bị phần cứng.

---

## 4. Mốc thời gian then chốt & Dự toán ngân sách
*   **Bảng 6 Mốc tiến độ (Milestones khớp 8 tháng):**
    *   `M1 (Tháng 1)`: Hoàn tất Khảo sát, Đặc tả SRS & Thiết kế Kiến trúc hệ thống.
    *   `M2 (Tháng 2 – 4)`: Hoàn thành Lập trình Core WMS, Module RS232 đọc cân, Module in tem QR & Logic BOM/FEFO.
    *   `M3 (Tháng 5)`: Lắp đặt thiết bị phần cứng tại Kho tổng Thái Nguyên & Chạy thử nghiệm UAT nội bộ.
    *   `M4 (Tháng 6 - MỐC CỨNG)`: **Kho tổng được đào tạo trước khi sử dụng và chính thức vận hành chậm nhất cuối tháng thứ 6.**
    *   `M5 (Tháng 7)`: Lắp đặt phần cứng, đồng bộ dữ liệu và đào tạo trước sử dụng cho 02 Kho chi nhánh phân phối.
    *   `M6 (Tháng 8)`: Đào tạo bổ sung, Nghiệm thu tổng thể 3 kho và Đóng gói kết thúc dự án.
*   **Bảng tóm tắt ngân sách (Khớp 100% với BAC = 2.0 Tỷ VNĐ):**
    *   Chi phí nhân sự trực tiếp (50 Man-Month / 8 nhân sự): **1.667.000.000 VNĐ** (83.35%)
    *   Thiết bị phần cứng 3 kho: **130.000.000 VNĐ** (6.50%)
    *   Hạ tầng Cloud, Server & Bản quyền (8 tháng): **25.000.000 VNĐ** (1.25%)
    *   Chi phí công tác & Onsite Hà Nội – Thái Nguyên – Chi nhánh: **35.000.000 VNĐ** (1.75%)
    *   Quỹ dự phòng rủi ro (Contingency Reserve 7.15%): **143.000.000 VNĐ** (7.15%)
    *   👉 **Tổng ngân sách phê duyệt (BAC):** **2.000.000.000 VNĐ** (100%)

---

## 5. Danh mục Ràng buộc, Giả định & Tiêu chí thành công
*   **Ràng buộc cốt lõi (Constraints):**
    *   *Tiến độ:* Kho tổng vận hành chậm nhất cuối tháng thứ 6; đóng gói toàn bộ ở tháng thứ 8.
    *   *Chi phí:* Ngân sách trần không vượt quá 2.000.000.000 VNĐ.
    *   *Kỹ thuật:* Web chạy trên máy trạm Windows, nhận dữ liệu cân qua RS232; sai số cân và thời gian in tem theo tiêu chí nghiệm thu tại chương 2.
    *   *Nghiệp vụ:* Bắt buộc áp dụng đúng thuật toán xuất kho FEFO và công thức hao hụt BOM.
*   **Nhật ký giả định (Assumption Log):**
    *   Doanh nghiệp Trà Tân Cương bố trí công nhân và thủ kho tham gia UAT đúng tiến độ.
    *   Nguồn điện và đường truyền Internet tại 3 kho ổn định (hệ thống có cơ chế đệm dữ liệu ngoại tuyến).
    *   Cân mua mới có RS232; máy in, máy quét và máy chấm công có giao thức kết nối được xác nhận theo đặc tả thiết bị.
    *   Dữ liệu cũ (danh mục chè, nhà vườn) được cung cấp dưới dạng bảng tính Excel chuẩn hóa trước Tháng 5.
*   **Tiêu chí thành công & Ký duyệt (Sign-off):**
    *   Vận hành thực tế tại 3 kho, sai số cân tự động < 0,1%, thời gian in tem < 2 giây/sản phẩm; các chức năng và điều kiện nghiệm thu theo chương 2.
    *   Chữ ký phê duyệt của Project Sponsor (Đại diện Trà Tân Cương) và PM (Bùi Hồng Phú), với xác nhận của đại diện các kho cho phần sử dụng tại kho.

### Làm rõ giả định triển khai và bàn giao

Nguồn số đo môi trường/chất lượng trà và tài sản doanh nghiệp cung cấp theo giả định tại 01/02. Số đo được nhập thủ công; tích hợp đo không dây được đánh giá khi khảo sát và xử lý theo quy trình thay đổi phạm vi. Dải khối lượng sử dụng và độ chia của cân được xác nhận trong SRS.

Gói 25 triệu bao phủ môi trường phát triển, kiểm thử và production trong tám tháng dự án. Tech Lead/Backend triển khai ứng dụng/CSDL, chuẩn bị sao lưu và hướng dẫn vận hành; Onsite kết nối thiết bị và đào tạo tại kho. Sau tháng 8, doanh nghiệp nhận quản trị và chịu phí duy trì; bảo trì dài hạn là thỏa thuận riêng. SAD xác định kiến trúc dữ liệu chung ba kho và cơ chế đệm/đồng bộ ngoại tuyến.

Tài liệu này là cơ sở cấu trúc của bản tôn chỉ đầy đủ 04. Phân công làm BTL và quy trình cộng tác nằm ở N-01–N-04.
