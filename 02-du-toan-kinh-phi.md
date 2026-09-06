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

### 1. Căn cứ và giới hạn của bảng phân bổ

Giữ nguyên bảng định mức lương, lịch tham gia và tổng công tại mục II; giữ nguyên toàn bộ cơ cấu ngân sách tại mục III. Chi phí nhân sự mỗi tháng bằng tổng lương tháng của các vị trí có tham gia trong tháng đó, không điều chỉnh nhân sự để bù chênh lệch ở khoản khác.

Bảng dưới là **phân bổ ngân sách công việc dự kiến theo tháng**, phục vụ hoàn thiện kế hoạch chi phí; chưa phải lịch thanh toán theo hợp đồng hoặc chi phí thực tế (AC). Tên mục giữ liên hệ với nội dung PV, nhưng **chưa dùng bảng này như một đường cơ sở PV hoàn chỉnh để tính EVM**: cần liên kết ngân sách với WBS, lịch công việc được duyệt và phân bổ dự phòng theo rủi ro trước. Lịch thanh toán và PV không mặc nhiên trùng nhau.

Các giá trị phân bổ ngoài nhân sự là **giả định lập kế hoạch**, không phải báo giá mới hay cam kết của nhà cung cấp. Không thay đổi số lượng hoặc đơn giá thiết bị tại mục IV. Nếu bước lập kế hoạch chi tiết chứng minh một giả định không phù hợp, phải trình phương án điều chỉnh trong tổng ngân sách đã chốt.

### 2. Phân bổ các khoản công việc đã có căn cứ

**Đơn vị: triệu VNĐ.** Mỗi hàng là tổng của bốn cột nhân sự, thiết bị, hạ tầng và công tác. Lũy kế trong bảng chưa bao gồm khoản dự phòng chưa phân bổ tại mục V.4.

| Tháng | Hoạt động làm căn cứ | Nhân sự | Thiết bị | Hạ tầng, cloud và bản quyền | Công tác, triển khai | Tổng công việc tháng | Lũy kế công việc |
| :---: | :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Khởi tạo, khảo sát, SRS, kiến trúc; chuẩn bị môi trường làm việc | 130 | 0 | 4 | 3 | 137 | 137 |
| 2 | Phát triển và thử tích hợp RS232, in tem, quét mã trên bộ thiết bị mẫu | 213 | 33 | 3 | 0 | 249 | 386 |
| 3 | Phát triển giao diện, nghiệp vụ; QA thử tích hợp trên bộ mẫu | 233 | 0 | 3 | 0 | 236 | 622 |
| 4 | Tích hợp BOM/FEFO; kiểm tra điều kiện lắp đặt kho tổng | 233 | 0 | 3 | 2 | 238 | 860 |
| 5 | Bổ sung thiết bị còn lại, lắp đặt và chạy thử tại kho tổng | 251 | 37 | 3 | 9 | 300 | 1.160 |
| 6 | Go-live kho tổng; tiếp nhận trước thiết bị cho hai chi nhánh | 221 | 60 | 3 | 8 | 292 | 1.452 |
| 7 | Lắp đặt, triển khai và hỗ trợ hai kho chi nhánh | 221 | 0 | 3 | 9 | 233 | 1.685 |
| 8 | Đào tạo bổ sung, nghiệm thu tổng thể và bàn giao | 165 | 0 | 3 | 4 | 172 | 1.857 |
| **TỔNG** | **Công việc dự kiến trong 8 tháng** | **1.667** | **130** | **25** | **35** | **1.857** | **1.857** |

### 3. Logic phân bổ và điều kiện cần xác nhận

**Nhân sự: 1.667 triệu, 50 MM.** Theo đúng các tháng tham gia tại mục II: tháng 2 có PM, Tech Lead, kỹ sư tích hợp, BA, Backend và Frontend, nên tổng là `50 + 50 + 32 + 30 + 27 + 24 = 213`. Tháng 7 có PM, Tech Lead, kỹ sư tích hợp, Backend, Frontend, QA và Onsite, nên tổng là `50 + 50 + 32 + 27 + 24 + 20 + 18 = 221`. Không đổi mức lương, thời điểm tham gia hay tổng chi phí nhân sự đã được duyệt.

**Thiết bị: 130 triệu, mua theo nhu cầu sử dụng.**

- Tháng 2: một bộ lấy từ danh mục kho tổng gồm 01 cân RS232 (15), 01 máy in (8), 01 máy quét (2), 01 PC (8), tổng **33 triệu**. Bộ này phục vụ kỹ sư tích hợp từ tháng 2 và QA từ tháng 3; sau đó chuyển vào kho tổng khi triển khai, không mua trùng lần nữa.
- Tháng 5: phần còn lại của kho tổng gồm 01 cân (15), 01 máy in (8), 03 máy quét (6), 01 PC (8), tổng **37 triệu**. Kết hợp bộ đã mua, tổng kho tổng vẫn là **70 triệu** theo mục IV.
- Tháng 6: tiếp nhận thiết bị và vật tư của hai chi nhánh, tổng **60 triệu** theo mục IV, để kiểm tra và cấu hình trước đợt lắp đặt tháng 7. Nhóm cần xác định thời gian đặt hàng đủ sớm để đạt mốc tiếp nhận; tháng ghi trong bảng không thay thế kế hoạch đặt hàng.
- Điều kiện: nhà cung cấp cho phép mua thành các đợt với đơn giá tại mục IV; có nơi giữ và kiểm tra thiết bị trước khi lắp đặt. Đây là giả định cần kiểm tra trong chương mua sắm. Nếu điều kiện không đạt, điều chỉnh lịch hoặc trình lại phương án, không tự tăng tổng thiết bị.

**Hạ tầng, cloud và bản quyền: 25 triệu.** Phân bổ 4 triệu tháng 1 để chuẩn bị môi trường, tên miền và các thiết lập ban đầu; 3 triệu/tháng cho tháng 2–8 để duy trì môi trường phát triển, kiểm thử và vận hành. Đây là phân bổ tổng gói ngân sách tại mục III, không phải báo giá cho một loại máy chủ hay khẳng định mọi dịch vụ được trả hàng tháng. Chương mua sắm/chi phí phải xác định khoản nào trả trước, khoản nào trả định kỳ và tránh cộng trùng khi lập lịch thanh toán.

**Công tác, triển khai: 35 triệu.** Phân bổ 3 triệu cho khảo sát tháng 1; 2 triệu cho kiểm tra hiện trường tháng 4; 9 triệu cho lắp đặt kho tổng tháng 5; 8 triệu cho go-live và chuẩn bị triển khai tháng 6; 9 triệu cho hai chi nhánh tháng 7; 4 triệu cho đào tạo bổ sung/nghiệm thu tháng 8. Khảo sát trước tháng 5 do các vai trò đang tham gia như PM/BA/kỹ sư tích hợp thực hiện theo nhiệm vụ phù hợp; không giả định kỹ sư Onsite được huy động trước lịch tại mục II. Đây là chi phí đi lại, lưu trú và triển khai ngoài lương, không cộng lại tiền lương. Địa điểm hai chi nhánh, số chuyến, số người và số ngày chưa xác định; cần bóc tách để kiểm tra tính đủ của 35 triệu trước khi chốt lịch chi tiết.

### 4. Dự phòng và đối chiếu tổng ngân sách

| Khoản | Triệu VNĐ | Trạng thái |
| :--- | ---: | :--- |
| Nhân sự + thiết bị + hạ tầng + công tác đã phân bổ tại V.2 | 1.857 | Phân bổ kế hoạch công việc |
| Dự phòng rủi ro theo mục III | 143 | Giữ trong tổng ngân sách, chưa gán tháng hoặc rủi ro cụ thể |
| **Tổng ngân sách theo mục III (BAC đã chốt)** | **2.000** | **Không thay đổi** |

Không dồn dự phòng còn lại vào tháng 8 để làm khớp tổng. Khoản 143 triệu chưa phải một hoạt động đã có lịch, chưa phải AC và không có nghĩa phải chi hết. Khi xây dựng danh mục rủi ro và phương án ứng phó, người phụ trách chi phí phối hợp với rủi ro để xác định căn cứ, thời điểm và người duyệt sử dụng dự phòng. Tổng các khoản dự phòng đã gán cộng phần chưa gán luôn bằng 143 triệu; không cộng thêm lần nữa vào 2.000 triệu.

Trước khi dùng EVM, phải hoàn thiện ngân sách công việc theo thời gian và cách xử lý dự phòng theo hướng dẫn môn học; không tự đổi nhãn dự phòng sang management reserve hoặc đổi BAC tại mục III. Việc chưa phân bổ 143 triệu làm cho bảng V.2 **chưa phải toàn bộ PV của BAC 2 tỷ**, không phải lý do giảm ngân sách xuống 1.857 triệu.

> Cập nhật ngày 06/09/2026 theo yêu cầu của người quản lý tài liệu: thay cách bù phần còn lại vào tháng 8 bằng phân bổ có căn cứ hoạt động và tách rõ dự phòng chưa phân bổ. Các mục I–IV và VI được giữ nguyên. Bảng này đã được tính lại về mặt số học; tính khả thi chi tiết còn phụ thuộc WBS, lịch mua sắm và các giả định nêu trên.

---

## VI. PHÂN CÔNG QUẢN LÝ HỒ SƠ TÀI LIỆU DỰ ÁN (RACI MATRIX)

Không bổ sung nhân sự Technical Writer riêng lẻ; tài liệu được phân bổ đúng chuyên môn của 8 nhân sự hiện có:

*   **Người quản lý dự án (PM):** Chủ trì lập và kiểm soát phiên bản toàn bộ Hồ sơ Quản lý dự án (*Project Charter, WBS Dictionary, Schedule Baseline, Cost Baseline EVM, Risk Register, Biên bản họp*).
*   **Chuyên viên phân tích nghiệp vụ (BA):** Chủ trì biên soạn *Tài liệu Đặc tả Yêu cầu (SRS/Use Cases)* và chắp bút *Tài liệu Hướng dẫn sử dụng (User Manual) / Quy trình thao tác chuẩn (SOP)* cho thủ kho và công nhân.
*   **Solution Architect / Tech Lead & Dev:** Chủ trì *Tài liệu Thiết kế Kiến trúc (SAD), Thiết kế CSDL (DB Schema)* và *Đặc tả Giao thức Tích hợp Phần cứng RS232 / Mã vạch Zebra*.
*   **QA/QC Engineer:** Chủ trì *Kế hoạch Kiểm thử (Test Plan), Kịch bản Test (Test Cases)* và *Biên bản Nghiệm thu UAT*.
*   **Kỹ sư Triển khai Onsite:** Phối hợp với BA hoàn thiện phụ lục thực địa hướng dẫn thao tác thiết bị vật lý (Cân, máy in, máy quét QR) tại kho.
