# TÀI LIỆU DỰ TOÁN KINH PHÍ & CƠ CẤU NGUỒN LỰC DỰ ÁN
**Đề tài:** Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS)  
**Môn học:** Quản lý dự án phần mềm (PTIT)  
**Giảng viên phụ trách:** ThS. Ngô Tiến Đức  
**Thuật ngữ quản lý chuẩn:** Người quản lý dự án (Project Manager - PM) *(Tuyệt đối không dùng 'giám đốc dự án')*  
**Đặc thù bài tập lớn:** Tập trung 100% vào quy trình quản trị, lập kế hoạch, biểu mẫu chuẩn PMBOK 6th; không viết code hay prototype.

---

## I. TỔNG QUAN RÀNG BUỘC TIẾN ĐỘ & NGÂN SÁCH

*   **Thời gian thực hiện toàn dự án:** **08 tháng** (35 tuần làm việc).
*   **Mốc then chốt (Hard Milestone):** **Tháng thứ 6** — Bắt buộc phải hoàn thành Go-live và đưa vào vận hành thực tế tại **Kho tổng chế biến/đóng gói** (Thái Nguyên).
*   **Tháng 7 – 8:** Triển khai tiếp nối cho **2 Kho chi nhánh**, đào tạo người dùng, nghiệm thu và đóng gói dự án.
*   **Tổng ngân sách phê duyệt (BAC - Budget at Completion):** **2.000.000.000 VNĐ** *(Hai tỷ đồng chẵn)*.

---

## II. CƠ CẤU ĐỘI DỰ ÁN VÀ ĐỊNH MỨC LƯƠNG (50 MAN-MONTH)

Đội dự án gồm **08 nhân sự chuyên trách**, mức lương đã được chuẩn hóa theo độ phức tạp kỹ thuật và nghiệp vụ nông sản:

### 1. Bảng định mức lương và căn cứ chuyên môn
| STT | Vị trí / Chức danh | Lương Gross/tháng (VNĐ) | Thời gian tham gia | Tổng công (MM) | Căn cứ chuyên môn & Trách nhiệm chính |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | **Người quản lý dự án (PM)** | **50.000.000** | Tháng 1 – 8 (8 tháng) | 8.0 | Chịu trách nhiệm toàn diện về tiến độ, chất lượng, chi phí, mốc Go-live tháng 6 và kiểm soát cấu hình tài liệu. |
| **2** | **Solution Architect / Tech Lead** | **50.000.000** | Tháng 1 – 8 (8 tháng) | 8.0 | Thiết kế kiến trúc phân tán 3 kho, xử lý luồng đồng bộ trực tuyến/ngoại tuyến, bảo mật và thẩm định kỹ thuật. |
| **3** | **Kỹ sư Tích hợp Phần cứng (RS232/IoT)** | **32.000.000** | Tháng 2 – 7 (6 tháng) | 6.0 | Lập trình giao tiếp cổng COM/RS232 đọc dữ liệu Cân điện tử thời gian thực, điều khiển máy in mã vạch Zebra và máy quét QR. |
| **4** | **Chuyên viên phân tích nghiệp vụ (BA)** | **30.000.000** | Tháng 1 – 5 (5 tháng) | 5.0 | Phân tích nghiệp vụ đặc thù: Định mức chuyển đổi BOM chè búp tươi $\rightarrow$ chè khô $\rightarrow$ thành phẩm, quy tắc xuất kho FEFO và viết User Manual. |
| **5** | **Backend Developer (Core WMS)** | **27.000.000** | Tháng 2 – 8 (7 tháng) | 7.0 | Lập trình module nghiệp vụ kho, vị trí ô kệ (Bin/Rack), xử lý Transaction luân chuyển hàng giữa các kho. |
| **6** | **Frontend Developer (Web Dashboard)** | **24.000.000** | Tháng 2 – 7 (6 tháng) | 6.0 | Xây dựng giao diện Web chạy mượt trên máy trạm Windows, tối ưu hóa thao tác chạm/quét mã nhanh cho công nhân. |
| **7** | **QA/QC Engineer (Kiểm thử hệ thống)** | **20.000.000** | Tháng 3 – 8 (6 tháng) | 6.0 | Thiết kế Test Cases nghiệp vụ kho, kiểm thử tích hợp phần cứng và thực hiện kiểm thử nghiệm thu người dùng (UAT). |
| **8** | **Kỹ sư Triển khai & Hạ tầng Onsite** | **18.000.000** | Tháng 5 – 8 (4 tháng) | 4.0 | Lắp đặt thiết bị ngoại vi, mạng nội bộ, cài driver cổng COM, trực tiếp đào tạo công nhân tại Thái Nguyên và 2 kho chi nhánh. |
| **TỔNG** | **Đội dự án 08 người** | | | **50.0 MM** | **1.667.000.000 VNĐ** |

---

## III. BẢNG TỔNG DỰ TOÁN NGÂN SÁCH DỰ ÁN (BAC = 2,0 TỶ VNĐ)

| Hạng mục chi phí | Chi tiết bóc tách | Thành tiền (VNĐ) | Tỷ trọng (%) |
| :--- | :--- | :---: | :---: |
| **1. Chi phí Nhân sự trực tiếp** | 50 Man-Month cho 08 nhân sự theo bảng lương trên | **1.667.000.000** | **83.35%** |
| **2. Mua sắm Thiết bị Phần cứng (3 kho)** | Trang bị đầy đủ cho 1 Kho tổng chế biến và 2 Kho chi nhánh *(chi tiết mục IV)* | **130.000.000** | **6.50%** |
| **3. Hạ tầng Mạng, Cloud & Bản quyền** | Thuê Cloud Server VPS (8 tháng), Domain, Chứng chỉ SSL, dịch vụ SMS/Email Brandname | **25.000.000** | **1.25%** |
| **4. Chi phí Công tác & Triển khai thực địa** | Chi phí đi lại, lưu trú của đội kỹ thuật khảo sát & Onsite giữa Hà Nội – Thái Nguyên – Chi nhánh | **35.000.000** | **1.75%** |
| **5. Dự phòng rủi ro (Contingency Reserve)** | Quỹ dự phòng rủi ro kỹ thuật, thay đổi yêu cầu và biến động thực tế | **143.000.000** | **7.15%** |
| **TỔNG KINH PHÍ (BAC)** | **Tổng ngân sách toàn diện dự án (8 tháng)** | **2.000.000.000 VNĐ** | **100.00%** |

---

## IV. BÓC TÁCH CHI PHÍ THIẾT BỊ PHẦN CỨNG CHO 3 KHO (130 TRIỆU VNĐ)

Hệ thống triển khai trên nền tảng Web chạy trong môi trường Windows, kết nối thiết bị ngoại vi tại 3 địa điểm:

### 1. Kho tổng chế biến / đóng gói (Thái Nguyên) — 70.000.000 VNĐ
*   **02 Cân điện tử công nghiệp chuẩn RS232** (tải trọng 30kg - 100kg, cổng COM truyền data): $2 \times 15.000.000 = \mathbf{30.000.000\text{ VNĐ}}$
*   **02 Máy in mã vạch/tem nhãn công nghiệp Zebra** (in tem thùng, tem hộp trà): $2 \times 8.000.000 = \mathbf{16.000.000\text{ VNĐ}}$
*   **04 Máy quét mã vạch/QR 2D không dây** (quét mã lô, quét vị trí kệ): $4 \times 2.000.000 = \mathbf{8.000.000\text{ VNĐ}}$
*   **02 Máy trạm PC Windows đặt tại bàn cân & đóng gói:** $2 \times 8.000.000 = \mathbf{16.000.000\text{ VNĐ}}$

### 2. 02 Kho chi nhánh phân phối — 60.000.000 VNĐ *(30.000.000 VNĐ / kho)*
*   **02 Cân điện tử bàn kiểm tra RS232:** $2 \times 7.500.000 = \mathbf{15.000.000\text{ VNĐ}}$
*   **02 Máy in mã vạch/phiếu xuất:** $2 \times 5.000.000 = \mathbf{10.000.000\text{ VNĐ}}$
*   **04 Máy quét mã QR cầm tay:** $4 \times 2.000.000 = \mathbf{8.000.000\text{ VNĐ}}$
*   **02 Máy trạm PC Windows kiểm kê kho:** $2 \times 8.000.000 = \mathbf{16.000.000\text{ VNĐ}}$
*   **Vật tư mạng & Thiết bị chuyển mạch phụ trợ 2 kho:** $\mathbf{11.000.000\text{ VNĐ}}$

---

## V. KẾ HOẠCH PHÂN BỔ DÒNG TIỀN THEO 8 THÁNG (PLANNED VALUE - PV)

Bảng phân bổ chi phí theo từng tháng đóng vai trò là **Đường cơ sở chi phí (Cost Baseline)** để nhóm sinh viên tính toán Quản lý giá trị thu được (EVM - Earned Value Management) trong **Chương 4**:

| Tháng | Giai đoạn & Hoạt động trọng tâm | Chi phí nhân sự | Chi phí thiết bị & khác | Dự phòng giải ngân | Tổng chi phí tháng (PV) | Chi phí tích lũy (Cumulative PV) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **Tháng 1** | Khởi tạo, Khảo sát, Đặc tả SRS & Kiến trúc hệ thống | 130.000.000 | 0 | 0 | **130.000.000** | 130.000.000 (6.5%) |
| **Tháng 2** | Thiết kế DB, Phát triển Core WMS & Module RS232 | 213.000.000 | 10.000.000 *(Setup Cloud)* | 0 | **223.000.000** | 353.000.000 (17.65%) |
| **Tháng 3** | Lập trình giao diện, Module Cân, In tem QR, Test logic | 233.000.000 | 2.000.000 *(Cloud)* | 0 | **235.000.000** | 588.000.000 (29.4%) |
| **Tháng 4** | Tích hợp BOM chế biến, xuất kho FEFO, Test hệ thống | 233.000.000 | 7.000.000 *(Cloud + Khảo sát)* | 0 | **240.000.000** | 828.000.000 (41.4%) |
| **Tháng 5** | Chuẩn bị vận hành Kho tổng, Lắp đặt phần cứng Kho tổng | 251.000.000 | 82.000.000 *(70M HW + Onsite)* | 0 | **333.000.000** | 1.161.000.000 (58.05%) |
| **Tháng 6** | **GOLIVE KHO TỔNG (MỐC CỨNG)**, Hiệu chỉnh vận hành | 221.000.000 | 13.000.000 *(Cloud + Onsite)* | 30.000.000 | **264.000.000** | 1.425.000.000 (71.25%) |
| **Tháng 7** | Nhân bản & Triển khai phần cứng tại 02 Kho chi nhánh | 221.000.000 | 73.000.000 *(60M HW + Onsite)* | 30.000.000 | **324.000.000** | 1.749.000.000 (87.45%) |
| **Tháng 8** | Nghiệm thu tổng thể, Đào tạo nhân sự, Đóng gói dự án | 165.000.000 | 3.000.000 *(Cloud + Nghiệm thu)* | 83.000.000 | **251.000.000** | **2.000.000.000 (100%)** |
| **TỔNG** | **Toàn bộ 8 tháng** | **1.667.000.000** | **190.000.000** | **143.000.000** | **2.000.000.000 VNĐ** | |

> Ghi chú đối chiếu ngày 06/09/2026: Giữ nguyên ngân sách và cơ cấu chi phí tại mục III. Chi phí nhân sự từng tháng được tính theo lịch tham gia tại mục II (tháng 2: 213 triệu; tháng 7: 221 triệu). Phân bổ thiết bị và chi phí khác giữ nguyên tháng 1–7; tháng 8 là phần còn lại 3 triệu để tổng cột bằng 190 triệu. Đây là phân bổ kế hoạch để đối chiếu ngân sách, chưa phải số thực chi hoặc bằng chứng về lịch thanh toán; cần rà soát lại thời điểm phân bổ khi hoàn thiện WBS và tiến độ chi tiết. Dự phòng 143 triệu giữ nguyên theo mục III; phân bổ dự phòng trong bảng không có nghĩa khoản này đã phát sinh hoặc bắt buộc phải chi hết.

---

## VI. PHÂN CÔNG QUẢN LÝ HỒ SƠ TÀI LIỆU DỰ ÁN (RACI MATRIX)

Không bổ sung nhân sự Technical Writer riêng lẻ; tài liệu được phân bổ đúng chuyên môn của 8 nhân sự hiện có:

*   **Người quản lý dự án (PM):** Chủ trì lập và kiểm soát phiên bản toàn bộ Hồ sơ Quản lý dự án (*Project Charter, WBS Dictionary, Schedule Baseline, Cost Baseline EVM, Risk Register, Biên bản họp*).
*   **Chuyên viên phân tích nghiệp vụ (BA):** Chủ trì biên soạn *Tài liệu Đặc tả Yêu cầu (SRS/Use Cases)* và chắp bút *Tài liệu Hướng dẫn sử dụng (User Manual) / Quy trình thao tác chuẩn (SOP)* cho thủ kho và công nhân.
*   **Solution Architect / Tech Lead & Dev:** Chủ trì *Tài liệu Thiết kế Kiến trúc (SAD), Thiết kế CSDL (DB Schema)* và *Đặc tả Giao thức Tích hợp Phần cứng RS232 / Mã vạch Zebra*.
*   **QA/QC Engineer:** Chủ trì *Kế hoạch Kiểm thử (Test Plan), Kịch bản Test (Test Cases)* và *Biên bản Nghiệm thu UAT*.
*   **Kỹ sư Triển khai Onsite:** Phối hợp với BA hoàn thiện phụ lục thực địa hướng dẫn thao tác thiết bị vật lý (Cân, máy in, máy quét QR) tại kho.
