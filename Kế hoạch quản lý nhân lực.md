# KẾ HOẠCH QUẢN LÝ NGUỒN NHÂN LỰC DỰ ÁN

## 1. Mục tiêu quản lý nguồn nhân lực

Quản lý nguồn nhân lực của dự án **Hệ thống Quản lý Kho Trà và Chuỗi
cung ứng Tân Cương (WMS)** nhằm bảo đảm dự án có đúng nhân sự, đúng năng
lực, đúng thời điểm và đúng trách nhiệm để hoàn thành phạm vi công việc
trong thời gian từ **03/06/2027 đến 02/02/2028**.

Đội dự án được tổ chức theo cơ cấu 8 vị trí chuyên trách với tổng nguồn
lực **50 Man-Month (MM)** đã được sử dụng trong dự toán dự án:

    STT Vị trí                             Số lượng Thời gian tham gia     Khối lượng
  ----- -------------------------------- ---------- -------------------- ------------
      1 Project Manager (PM)                      1 T1--T8                       8 MM
      2 Solution Architect / Tech Lead            1 T1--T8                       8 MM
      3 Hardware / IoT Engineer                   1 T2--T7                       6 MM
      4 Business Analyst (BA)                     1 T1--T5                       5 MM
      5 Backend Developer                         1 T2--T8                       7 MM
      6 Frontend Developer                        1 T2--T7                       6 MM
      7 QA/QC Engineer                            1 T3--T8                       6 MM
      8 Deployment & Onsite Engineer              1 T5--T8                       4 MM
        **Tổng cộng**                         **8**                         **50 MM**

Mục tiêu quản lý nhân lực là:

-   Bảo đảm các Work Package có người chịu trách nhiệm rõ ràng.
-   Bảo đảm nguồn lực được huy động đúng theo tiến độ dự án.
-   Tránh thiếu hoặc dư thừa nhân lực ở từng giai đoạn.
-   Bảo đảm các công việc có phụ thuộc kỹ thuật và nghiệp vụ được phối
    hợp đúng đầu mối.
-   Duy trì trách nhiệm cá nhân đối với đầu ra của từng Work Package.
-   Kiểm soát việc sử dụng nguồn lực trong giới hạn ngân sách dự án.
-   Bảo đảm đội dự án có đủ năng lực để thực hiện phát triển, tích hợp,
    kiểm thử, triển khai và nghiệm thu.

Việc tổ chức nguồn lực được xây dựng trên WBS, tiến độ và các Work
Package của dự án. Kế hoạch nhân lực xác định vị trí, số lượng, thời
điểm cần nhân sự, thời gian tham gia và chi phí nguồn lực tương ứng.

------------------------------------------------------------------------

## 2. Cơ cấu tổ chức đội dự án

Dự án sử dụng cơ cấu tổ chức theo **Project Manager làm đầu mối điều
phối chung**, kết hợp với các đầu mối chuyên môn.

Project Manager không trực tiếp quản lý mọi công việc kỹ thuật ở mức chi
tiết. Các thành viên chịu trách nhiệm đối với lĩnh vực chuyên môn và
Work Package được giao, đồng thời phối hợp ngang với các thành viên khác
khi công việc có phụ thuộc.

### 2.1. Cơ cấu đội dự án

```text
                         PROJECT MANAGER
                         Bùi Hồng Phú
                               |
       +-----------------------+-----------------------+
       |                       |                       |
  TECH LEAD                   BA                    QA/QC
Nguyễn Tiến Dũng      Nguyễn Đức Công       Nguyễn Hải Hưng
       |
  +----+----------------------+----------------------+
  |                           |                      |
BACKEND                    FRONTEND             HARDWARE / IoT
Lê Minh Hoàng             Phạm Thu Trang       Trần Quốc Anh
                                                    |
                                          DEPLOYMENT / ONSITE
                                             Đặng Văn Long
```

Sơ đồ thể hiện các đầu mối điều phối và phối hợp công việc, không xác
lập quan hệ cấp trên–cấp dưới tuyệt đối giữa các vai trò.

Trong quá trình thực hiện, các thành viên có thể trao đổi trực tiếp với
nhau khi xử lý một Work Package. PM là người chịu trách nhiệm điều phối
tổng thể, phân bổ nguồn lực và xử lý các xung đột hoặc vấn đề vượt phạm
vi chuyên môn.

### 2.2. Thành phần đội dự án

| STT | Vị trí | Người được ghi tên trong hồ sơ | Thời gian tham gia | Khối lượng |
|---:|---|---|---|---:|
| 1 | Project Manager (PM) | Bùi Hồng Phú | T1–T8 | 8 MM |
| 2 | Solution Architect / Tech Lead | Nguyễn Tiến Dũng | T1–T8 | 8 MM |
| 3 | Kỹ sư Tích hợp Phần cứng (RS232/IoT) | Trần Quốc Anh | T2–T7 | 6 MM |
| 4 | Chuyên viên phân tích nghiệp vụ (BA) | Nguyễn Đức Công | T1–T5 | 5 MM |
| 5 | Backend Developer (Core WMS) | Lê Minh Hoàng | T2–T8 | 7 MM |
| 6 | Frontend Developer (Web Dashboard) | Phạm Thu Trang | T2–T7 | 6 MM |
| 7 | QA/QC Engineer | Nguyễn Hải Hưng | T3–T8 | 6 MM |
| 8 | Kỹ sư Triển khai & Hạ tầng Onsite | Đặng Văn Long | T5–T8 | 4 MM |
| | **Tổng cộng** | **8 vị trí** | | **50 MM** |

Cơ cấu chức danh, thời gian tham gia và khối lượng được phân bổ thống nhất
trong đội dự án gồm 8 vị trí chuyên trách, tổng cộng 50 MM.

### 2.3. Các bên không thuộc 8 nhân sự chuyên trách

Các cá nhân sau có tham gia hoặc có ảnh hưởng đến dự án nhưng **không
được tính vào đội 8 nhân sự chuyên trách**:

| Bên liên quan | Vai trò | Quan hệ với dự án |
|---|---|---|
| Đại diện đơn vị thi công | Đại diện Công ty CP Công nghệ Raumania | Đầu mối cấp tổ chức |
| Trần Minh Đức | Đại diện chủ đầu tư | Đại diện phía khách hàng/chủ đầu tư |
| Lê Thị Mai | Đại diện kho tổng | Đại diện địa điểm triển khai/người dùng |
| Phạm Văn Hòa | Đại diện kho chi nhánh 1 | Đại diện địa điểm triển khai/người dùng |
| Đặng Thu Hà | Đại diện kho chi nhánh 2 | Đại diện địa điểm triển khai/người dùng |
| Đỗ Quốc Bảo | Nhà cung cấp thiết bị | Đối tác bên ngoài |
| Hoàng Văn Sơn | Nhà cung cấp trà | Đối tác bên ngoài |

Đại diện đơn vị thi công phối hợp với PM ở cấp tổ chức về nguồn lực và
các cam kết của Công ty CP Công nghệ Raumania; vai trò này không thuộc
đội 8 nhân sự chuyên trách được phân bổ 50 MM.

------------------------------------------------------------------------

## 3. Vai trò, quyền hạn và trách nhiệm

### 3.1. Project Manager -- Bùi Hồng Phú

**Phạm vi trách nhiệm**

-   Quản lý tổng thể dự án trong 8 tháng.
-   Lập, duy trì và điều phối kế hoạch quản lý dự án.
-   Điều phối 8 thành viên trong đội dự án.
-   Theo dõi phạm vi, tiến độ, chi phí, chất lượng và rủi ro.
-   Điều phối việc thực hiện các mốc M1--M6.
-   Theo dõi việc sử dụng nguồn lực theo 50 MM.
-   Điều phối thay đổi và các vấn đề phát sinh.
-   Điều phối hoạt động triển khai, Go-live, nghiệm thu và đóng dự án.
-   Là đầu mối quản lý với đại diện đơn vị thi công và chủ đầu tư.

**Quyền hạn**

-   Phân công và điều phối nguồn lực trong phạm vi được phê duyệt.
-   Yêu cầu thành viên xử lý các vấn đề ảnh hưởng đến mục tiêu dự án.
-   Ưu tiên công việc khi có xung đột nguồn lực.
-   Yêu cầu báo cáo tiến độ và tình trạng Work Package.
-   Điều phối xử lý rủi ro và vấn đề.
-   Trình các thay đổi hoặc quyết định vượt thẩm quyền lên cấp tương
    ứng.

### 3.2. Solution Architect / Tech Lead -- Nguyễn Tiến Dũng

**Phạm vi trách nhiệm**

-   Xây dựng và kiểm soát kiến trúc giải pháp.
-   Xác định các tiêu chuẩn kỹ thuật của hệ thống.
-   Điều phối các quyết định kỹ thuật giữa Backend, Frontend và
    Hardware/IoT.
-   Review thiết kế và các thành phần kỹ thuật.
-   Kiểm soát tích hợp giữa phần mềm và thiết bị.
-   Hỗ trợ xử lý các vấn đề kỹ thuật có mức độ ảnh hưởng cao.
-   Phối hợp với QA/QC trong Integration Test và Go-live.

**Quyền hạn**

-   Quyết định giải pháp kỹ thuật trong phạm vi kiến trúc đã được phê
    duyệt.
-   Yêu cầu điều chỉnh các thành phần kỹ thuật không đáp ứng tiêu chuẩn.
-   Điều phối các thành viên kỹ thuật trong các Work Package có phụ
    thuộc.

### 3.3. Business Analyst -- Nguyễn Đức Công

**Phạm vi trách nhiệm**

-   Khảo sát và phân tích nghiệp vụ kho.
-   Thu thập, phân tích và quản lý yêu cầu.
-   Xây dựng SRS và các đặc tả nghiệp vụ.
-   Phân tích Use Case và luồng nghiệp vụ.
-   Làm rõ yêu cầu BOM/FEFO.
-   Phối hợp với nhóm phát triển để giải thích yêu cầu.
-   Hỗ trợ UAT và xác nhận các vấn đề nghiệp vụ.
-   Phối hợp đào tạo và bàn giao người dùng.

**Quyền hạn**

-   Yêu cầu làm rõ các yêu cầu nghiệp vụ chưa đầy đủ.
-   Xác nhận mức độ phù hợp của chức năng với yêu cầu nghiệp vụ đã thống
    nhất.
-   Đề xuất xử lý các vấn đề nghiệp vụ cho PM.

### 3.4. Backend Developer -- Lê Minh Hoàng

**Phạm vi trách nhiệm**

-   Phát triển Backend và API.
-   Xây dựng các chức năng nhập, xuất và quản lý tồn kho.
-   Xử lý Batch ID và dữ liệu lô.
-   Triển khai logic BOM/FEFO.
-   Phát triển các chức năng dữ liệu và phân quyền theo thiết kế.
-   Tích hợp Backend với Frontend và các thành phần liên quan.
-   Khắc phục defect Backend.
-   Hỗ trợ xử lý vấn đề trong Integration Test và Go-live.

**Quyền hạn**

-   Quyết định triển khai chi tiết trong phạm vi Backend.
-   Đề xuất thay đổi kỹ thuật khi yêu cầu hoặc thiết kế hiện tại không
    đáp ứng thực tế.

### 3.5. Frontend Developer -- Phạm Thu Trang

**Phạm vi trách nhiệm**

-   Phát triển giao diện Web.
-   Xây dựng màn hình nhập, xuất, kiểm kê và quản lý lô.
-   Phát triển dashboard và các giao diện nghiệp vụ.
-   Tích hợp giao diện với API Backend.
-   Sửa lỗi giao diện.
-   Hỗ trợ UAT và Go-live.

**Quyền hạn**

-   Quyết định triển khai chi tiết giao diện trong phạm vi thiết kế được
    phê duyệt.
-   Đề xuất thay đổi UI khi phát hiện vấn đề ảnh hưởng khả năng sử dụng.

### 3.6. Hardware / IoT Engineer -- Trần Quốc Anh

**Phạm vi trách nhiệm**

-   Tích hợp trạm cân qua RS232.
-   Tích hợp máy in tem/mã vạch và máy quét theo giao thức xác nhận trong SRS.
-   Kiểm tra protocol và khả năng tương thích thiết bị.
-   Cấu hình thiết bị phục vụ triển khai.
-   Hỗ trợ đo đạc sai số cân tự động qua RS232.
-   Phối hợp với Onsite trong lắp đặt và xử lý lỗi thiết bị.
-   Hỗ trợ Integration Test và Go-live.

**Quyền hạn**

-   Quyết định cấu hình kỹ thuật của thiết bị trong phạm vi được phê
    duyệt.
-   Đề xuất thay thế hoặc điều chỉnh cấu hình khi thiết bị không đáp ứng
    yêu cầu.

### 3.7. QA/QC Engineer -- Nguyễn Hải Hưng

**Phạm vi trách nhiệm**

-   Lập Test Plan và Test Case.
-   Kiểm thử chức năng.
-   Kiểm thử tích hợp.
-   Kiểm tra các chức năng BOM/FEFO.
-   Kiểm tra tích hợp RS232, in tem và thiết bị.
-   Theo dõi defect và kết quả sửa lỗi.
-   Thực hiện regression test.
-   Chuẩn bị bằng chứng phục vụ UAT và nghiệm thu.
-   Đánh giá chất lượng trước khi chuyển giao.

**Quyền hạn**

-   Yêu cầu xử lý defect.
-   Từ chối chuyển giao Work Package khi chưa đạt tiêu chí chất lượng đã
    thống nhất.
-   Yêu cầu kiểm thử lại sau khi defect được sửa.

### 3.8. Deployment & Onsite Engineer -- Đặng Văn Long

**Phạm vi trách nhiệm**

-   Chuẩn bị môi trường triển khai.
-   Cài đặt và cấu hình phần mềm tại các kho.
-   Phối hợp cấu hình PC và thiết bị.
-   Hỗ trợ kết nối các thiết bị.
-   Hỗ trợ triển khai kho tổng.
-   Hỗ trợ triển khai hai kho chi nhánh.
-   Hỗ trợ Go-live.
-   Ghi nhận và xử lý các vấn đề phát sinh tại hiện trường.
-   Hỗ trợ bàn giao và đào tạo người dùng tại hiện trường.

**Quyền hạn**

-   Điều phối các công việc kỹ thuật triển khai tại hiện trường trong
    phạm vi được giao.
-   Yêu cầu Hardware/IoT và Tech Lead hỗ trợ khi phát sinh vấn đề vượt
    phạm vi onsite.

------------------------------------------------------------------------

## 4. Phân bổ nguồn lực theo thời gian

Dự án được chia thành 8 tháng, ký hiệu T1--T8:

| Tháng | Khoảng thời gian | Trọng tâm |
|---|---|---|
| T1 | 03/06/2027–02/07/2027 | Khởi tạo, lập kế hoạch, khảo sát, SRS và kiến trúc |
| T2 | 03/07/2027–02/08/2027 | Phân tích chi tiết, phát triển và chuẩn bị tích hợp |
| T3 | 03/08/2027–02/09/2027 | Phát triển, tích hợp và bắt đầu kiểm thử |
| T4 | 03/09/2027–02/10/2027 | Hoàn thiện phần mềm lõi và tích hợp |
| T5 | 03/10/2027–02/11/2027 | Lắp đặt, kiểm thử và UAT nội bộ kho tổng |
| T6 | 03/11/2027–02/12/2027 | Go-live kho tổng chậm nhất ngày 02/12/2027 |
| T7 | 03/12/2027–02/01/2028 | Triển khai hai kho chi nhánh |
| T8 | 03/01/2028–02/02/2028 | Nghiệm thu tổng thể và đóng dự án |

------------------------------------------------------------------------

### 4.1. Ma trận tham gia theo tháng

| Vị trí | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | Tổng MM |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---:|
| PM | ● | ● | ● | ● | ● | ● | ● | ● | 8 |
| Tech Lead | ● | ● | ● | ● | ● | ● | ● | ● | 8 |
| Hardware / IoT | | ● | ● | ● | ● | ● | ● | | 6 |
| BA | ● | ● | ● | ● | ● | | | | 5 |
| Backend | | ● | ● | ● | ● | ● | ● | ● | 7 |
| Frontend | | ● | ● | ● | ● | ● | ● | | 6 |
| QA/QC | | | ● | ● | ● | ● | ● | ● | 6 |
| Deployment / Onsite | | | | | ● | ● | ● | ● | 4 |

**Tổng cộng: 50 MM.**

------------------------------------------------------------------------

## 5. Phân bổ nhân lực theo giai đoạn dự án

### 5.1. Giai đoạn khởi tạo và lập kế hoạch -- T1

**Nhân sự chính**

-   PM
-   Tech Lead
-   BA

**Công việc**

-   Lập PMP.
-   Hoàn thiện kế hoạch phạm vi và WBS Dictionary.
-   Lập tiến độ chi tiết và BAC.
-   Khảo sát và phân tích yêu cầu.
-   Xây dựng SRS.
-   Xây dựng kiến trúc hệ thống.

**Đầu ra chính**

-   PMP.
-   Kế hoạch phạm vi.
-   WBS Dictionary.
-   Tiến độ chi tiết.
-   SRS.
-   Kiến trúc hệ thống.

### 5.2. Giai đoạn phát triển và tích hợp -- T2--T4

**Nhân sự chính**

-   PM
-   Tech Lead
-   BA
-   Backend
-   Frontend
-   Hardware / IoT

QA/QC bắt đầu tham gia từ T3.

**Công việc**

-   Phát triển Backend.
-   Phát triển Frontend.
-   Phát triển các module nghiệp vụ.
-   Tích hợp thiết bị.
-   Tích hợp RS232.
-   Tích hợp máy in tem/mã vạch và máy quét theo giao thức xác nhận trong SRS.
-   Phát triển BOM/FEFO.
-   Integration Test.

**Mốc**

-   **M2 — 02/10/2027 (cuối T4):** hoàn thành phần mềm lõi, RS232, in tem/quét QR–barcode, BOM/FEFO.

### 5.3. Giai đoạn triển khai kho tổng -- T5--T6

**Nhân sự chính**

-   PM
-   Tech Lead
-   Hardware / IoT
-   Backend
-   Frontend
-   QA/QC
-   Deployment / Onsite

BA tham gia đến hết T5; hoàn tất bàn giao tài liệu vào cuối T5 và hỗ trợ nghiệp vụ/UAT trong thời gian tham gia.

**Công việc**

-   Lắp đặt PC, trạm cân RS232, máy in tem/mã vạch và máy quét tại kho tổng.
-   Kiểm thử tích hợp.
-   Đo đạc sai số cân.
-   UAT nội bộ kho tổng.
-   Đào tạo.
-   Chuẩn bị Go-live.

**Mốc**

-   **M3 — 02/11/2027 (cuối T5):** lắp đặt và UAT nội bộ kho tổng.
-   **M4 — 02/12/2027 (cuối T6):** Go-live kho tổng.

### 5.4. Giai đoạn triển khai hai kho chi nhánh -- T7

**Nhân sự chính**

-   PM
-   Tech Lead
-   Hardware / IoT
-   Backend
-   Frontend
-   QA/QC
-   Deployment / Onsite

**Công việc**

-   Lắp đặt phần cứng và thiết bị tại hai kho chi nhánh.
-   Cấu hình hệ thống.
-   Kiểm thử triển khai.
-   Hỗ trợ người dùng.
-   Xử lý các vấn đề phát sinh tại hiện trường.

**Mốc**

-   **M5 — 02/01/2028 (cuối T7):** hoàn thành triển khai hai kho chi nhánh.

### 5.5. Giai đoạn nghiệm thu và đóng dự án -- T8

**Nhân sự chính**

-   PM
-   Tech Lead
-   Backend
-   QA/QC
-   Deployment / Onsite

**Công việc**

-   Xử lý các vấn đề còn tồn tại.
-   QA/QC và Tech Lead tổng hợp hồ sơ nghiệm thu trong T8 từ kết quả kiểm thử đã ghi nhận ở các giai đoạn trước.
-   Bàn giao hệ thống.
-   Đóng gói mã nguồn.
-   Bàn giao tài liệu.
-   Đóng dự án.

**Mốc**

-   **M6 — 02/02/2028 (cuối T8):** nghiệm thu tổng thể và đóng dự án.

------------------------------------------------------------------------

## 6. Phân bổ trách nhiệm theo Work Package

Việc phân bổ nhân lực được gắn trực tiếp với các Work Package trong WBS
của dự án.

  -----------------------------------------------------------------------
  Work Package            Người chịu trách nhiệm  Thành viên phối hợp
                          chính                   
  ----------------------- ----------------------- -----------------------
  1.1.1.1 -- PMP          PM                      Toàn đội

  1.1.1.2 -- Kế hoạch     PM                      BA, Tech Lead
  phạm vi & WBS                                   
  Dictionary                                      

  1.1.1.3 -- Tiến độ chi  PM                      Tech Lead, các đầu mối
  tiết & BAC                                      

  Phân tích yêu cầu / SRS BA                      PM, Tech Lead, QA

  Kiến trúc hệ thống      Tech Lead               PM, Backend, Frontend,
                                                  Hardware

  Phát triển Backend      Backend                 Tech Lead, BA,
                                                  Frontend, QA

  Phát triển Frontend     Frontend                BA, Backend, QA

  BOM/FEFO                Backend                 BA, Tech Lead, QA

  Tích hợp RS232          Hardware / IoT          Tech Lead, Backend, QA

  Tích hợp in tem / QR /  Hardware / IoT          Backend, Frontend, QA
  Barcode                                         

  Integration Test        QA/QC                   Backend, Frontend,
                                                  Hardware, Tech Lead

  1.4.1.1 -- Lắp đặt      Onsite                  Hardware, Tech Lead, QA
  thiết bị kho tổng                               

  1.4.2.3 -- Onsite hỗ    Onsite                  Hardware, QA, PM
  trợ kỹ thuật tại Thái                           
  Nguyên                                          

  1.5.1.1 -- Lắp đặt tại  Onsite                  Hardware, Tech Lead, QA
  2 kho chi nhánh                                 

  1.6.1.1 -- Tổng hợp     QA/QC / Tech Lead       PM
  và kiểm lại hồ sơ cân

  UAT                     BA / QA                 PM, toàn đội liên quan

  Go-live                 PM                      Tech Lead, Backend,
                                                  Hardware, QA, Onsite

  Đào tạo                 BA / Onsite             QA, PM

  1.6.3.2 -- Bàn giao,   PM                      Tech Lead, QA, Backend,
  đóng gói mã nguồn và                            Onsite
  đóng dự án                                      
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 7. Ma trận trách nhiệm RACI

**Quy ước:**

- **R — Responsible:** trực tiếp thực hiện công việc.
- **A — Accountable:** chịu trách nhiệm cuối cùng về kết quả.
- **C — Consulted:** được tham vấn.
- **I — Informed:** được thông báo.

| Công việc | PM | Tech Lead | BA | Backend | Frontend | Hardware/IoT | QA/QC | Onsite |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Quản lý dự án | A/R | C | C | I | I | I | C | C |
| PMP | A/R | C | C | I | I | I | I | I |
| Phạm vi, WBS và WBS Dictionary | A | C | R | I | I | I | C | I |
| Tiến độ và BAC | A/R | C | C | I | I | I | I | I |
| SRS | A | C | R | C | C | C | C | I |
| Kiến trúc hệ thống | A | R | C | C | C | C | C | I |
| Thiết kế CSDL/API | C | A/R | C | R | C | I | C | I |
| UI/UX và Frontend | C | C | C | C | R | I | C | I |
| Core WMS | A | C | C | R | R | I | C | I |
| BOM/FEFO | A | C | R/C | R | C | I | C | I |
| RS232 | C | A | C | C | I | R | C | C |
| In tem / QR / Barcode | C | A | C | C | C | R | C | R |
| Integration Test | C | C | C | R | R | R | A/R | C |
| Lắp đặt kho tổng | A | C | I | I | I | R | C | R |
| Đo sai số cân | C | A | I | C | I | R | R | C |
| UAT | A | C | R | C | C | C | R | C |
| Go-live kho tổng | A | R | C | R | R | R | R | R |
| Triển khai hai kho chi nhánh | A | R | I | C | C | R | R | R |
| Đào tạo | A | C | R | I | I | C | C | R |
| Nghiệm thu | A/R | C | C | I | I | I | R | C |
| Bàn giao | A/R | R | C | C | C | C | R | R |
| Đóng dự án | A/R | C | C | I | I | I | C | C |

RACI được sử dụng để xác định rõ trách nhiệm của từng thành viên đối với
từng nhóm công việc, tránh tình trạng Work Package không có người chịu
trách nhiệm hoặc có quá nhiều người cùng chịu trách nhiệm cuối cùng.

**Phạm vi theo giai đoạn:** Bảng phân bổ ở mục 6 và RACI là tổng hợp trách
nhiệm trong toàn dự án; từng phân công chỉ thực hiện trong kỳ huy động ở
mục 4 và [02, mục II](02-du-toan-kinh-phi.md). BA tham gia UAT/đào tạo kho
tổng trong T5, rồi bàn giao tài liệu; đợt chi nhánh T7 do QA/Onsite và đội
còn huy động thực hiện, Onsite/PM đào tạo theo bộ tài liệu đã nhận. Việc
tham vấn BA cho nghiệm thu, bàn giao hoặc đóng dự án phải thực hiện trước
khi BA kết thúc T5; bộ tài liệu dùng ở T8 là đầu vào đã bàn giao, không phải
tham vấn trực tiếp hoặc huy động BA thêm tháng.

Hardware và QA kiểm cân/in tem trước khi sử dụng tại từng kho. Gói
`1.6.1.1` ở T8 là tổng hợp hồ sơ và kiểm lại phần thay đổi, do QA/Tech Lead
thực hiện theo [WBS Dictionary chương 2](BÁO%20CÁO%20QUẢN%20LÝ%20PHẠM%20VI%20DỰ%20ÁN.md);
Hardware/Frontend bàn giao đặc tả, cấu hình và hồ sơ trước hết T7. Các
trách nhiệm ở giai đoạn sau được thực hiện bởi người còn trong kỳ huy động,
không tự kéo dài kỳ của BA, Hardware hoặc Frontend.

------------------------------------------------------------------------

## 8. Quan hệ giữa đội dự án và các bên bên ngoài

Đội dự án phối hợp với các vai trò đại diện chủ đầu tư, đơn vị thi công,
các kho và nhà cung cấp được xác định trong hồ sơ tình huống.

### 8.1. Quan hệ với chủ đầu tư

**Trần Minh Đức -- Đại diện chủ đầu tư**

PM là đầu mối chính trong việc:

-   Báo cáo trạng thái dự án.
-   Báo cáo các milestone.
-   Trình các vấn đề cần quyết định.
-   Trình các thay đổi ảnh hưởng đến phạm vi, tiến độ hoặc chi phí.
-   Phối hợp nghiệm thu.
-   Điều phối các vấn đề liên quan đến cam kết của dự án.

BA và các thành viên chuyên môn chỉ làm việc trực tiếp với đại diện chủ
đầu tư khi nội dung thuộc phạm vi chuyên môn hoặc được PM điều phối.

### 8.2. Quan hệ với đơn vị thi công

**Đại diện Công ty CP Công nghệ Raumania**

Đại diện đơn vị thi công là đầu mối cấp tổ chức. PM phối hợp với đầu
mối này trong các vấn đề:

-   Cam kết nguồn lực.
-   Hỗ trợ cấp tổ chức.
-   Các vấn đề vượt thẩm quyền của đội dự án.
-   Cam kết bàn giao.
-   Các quyết định cần xử lý ở cấp công ty.

Đại diện đơn vị thi công không thuộc 8 nhân sự chuyên trách và không
được phân bổ trong 50 MM.

### 8.3. Quan hệ với các kho

  -----------------------------------------------------------------------
  Đối tượng               Đại diện                Nội dung phối hợp chính
  ----------------------- ----------------------- -----------------------
  Kho tổng                Lê Thị Mai              Khảo sát, lắp đặt, UAT,
                                                  Go-live, đào tạo

  Kho chi nhánh 1         Phạm Văn Hòa            Chuẩn bị triển khai,
                                                  lắp đặt, kiểm thử, bàn
                                                  giao

  Kho chi nhánh 2         Đặng Thu Hà             Chuẩn bị triển khai,
                                                  lắp đặt, kiểm thử, bàn
                                                  giao
  -----------------------------------------------------------------------

Các đại diện kho là người dùng/đầu mối địa điểm triển khai, không thuộc
8 nhân sự thực thi.

### 8.4. Quan hệ với nhà cung cấp thiết bị

**Đỗ Quốc Bảo -- Công ty TNHH Thiết bị An Việt**

Hardware/IoT Engineer là đầu mối kỹ thuật chính khi cần:

-   Xác nhận thông số thiết bị.
-   Kiểm tra khả năng tương thích.
-   Xử lý vấn đề thiết bị.
-   Hỗ trợ cấu hình và kết nối.
-   Phối hợp bảo hành hoặc thay thế thiết bị nếu cần.

PM tham gia khi vấn đề ảnh hưởng đến tiến độ, chi phí hoặc cam kết dự
án.

### 8.5. Quan hệ với nhà cung cấp trà

**Hoàng Văn Sơn -- Cơ sở cung cấp trà Minh Sơn**

BA là đầu mối chính đối với các vấn đề liên quan đến nghiệp vụ, dữ liệu
và quy trình sản phẩm trà khi cần xác nhận thông tin phục vụ hệ thống.

Các vấn đề có ảnh hưởng đến phạm vi hoặc yêu cầu dự án được đưa về PM để
điều phối.

------------------------------------------------------------------------

## 9. Cơ chế điều hành nhân lực

### 9.1. Nguyên tắc điều hành

Đội dự án được điều hành theo mô hình:

> **PM điều phối tổng thể → các đầu mối chuyên môn chịu trách nhiệm Work
> Package → các thành viên phối hợp ngang theo phụ thuộc công việc → vấn
> đề được xử lý ở cấp thấp nhất có đủ năng lực → vấn đề ảnh hưởng mục
> tiêu dự án được đưa lên PM.**

PM chịu trách nhiệm điều phối:

-   Phạm vi.
-   Tiến độ.
-   Chi phí.
-   Chất lượng.
-   Nguồn lực.
-   Rủi ro.
-   Các milestone.
-   Go-live.
-   Nghiệm thu.
-   Đóng dự án.

Các thành viên không phải báo cáo qua nhiều cấp trung gian khi xử lý vấn
đề chuyên môn. Họ được phép phối hợp trực tiếp với nhau theo Work
Package, đồng thời bảo đảm PM được cập nhật đối với các vấn đề có ảnh
hưởng đến dự án.

### 9.2. Cơ chế giao việc

Công việc được giao dựa trên WBS, tiến độ và RACI.

PM thực hiện:

1.  Xác định Work Package cần triển khai.
2.  Xác định người chịu trách nhiệm chính.
3.  Xác định thành viên phối hợp.
4.  Xác định thời hạn.
5.  Xác định đầu ra cần bàn giao.
6.  Theo dõi trạng thái.
7.  Xử lý phụ thuộc và xung đột nguồn lực.

Người chịu trách nhiệm chính có quyền tổ chức công việc trong phạm vi
chuyên môn nhưng phải bảo đảm đầu ra, chất lượng và thời hạn đã thống
nhất.

### 9.3. Cơ chế báo cáo

Báo cáo của thành viên tập trung vào:

-   Công việc đã hoàn thành.
-   Công việc đang thực hiện.
-   Công việc tiếp theo.
-   Vấn đề đang gặp phải.
-   Phụ thuộc cần hỗ trợ.
-   Nguy cơ ảnh hưởng tiến độ, chi phí hoặc chất lượng.

Các vấn đề được xử lý tại cấp thấp nhất có đủ năng lực.

Khi vấn đề có khả năng ảnh hưởng đến:

-   Phạm vi;
-   Tiến độ;
-   Chi phí;
-   Chất lượng;
-   Milestone;
-   Go-live;
-   Nghiệm thu;
-   Cam kết với chủ đầu tư;

thì người phụ trách phải báo cáo PM.

### 9.4. Cơ chế phối hợp theo Work Package

Các nhóm phối hợp chính:

  Nhóm công việc            Đầu mối     Phối hợp
  ------------------------- ----------- ------------------------------------------
  PMP, tiến độ, ngân sách   PM          Toàn đội
  SRS, yêu cầu nghiệp vụ    BA          PM, Tech Lead, QA
  Kiến trúc                 Tech Lead   Backend, Frontend, Hardware
  Backend/API               Backend     Tech Lead, BA, Frontend, QA
  Frontend                  Frontend    BA, Backend, QA
  RS232/thiết bị            Hardware    Tech Lead, Onsite, QA
  Integration Test          QA          Backend, Frontend, Hardware, Tech Lead
  Lắp đặt kho tổng          Onsite      Hardware, Tech Lead, QA
  Go-live                   PM          Tech Lead, Backend, Hardware, QA, Onsite
  Hai kho chi nhánh         Onsite      Hardware, Tech Lead, QA, PM
  Đào tạo                   BA/Onsite   QA, PM
  Nghiệm thu                PM          QA, BA, Tech Lead
  Đóng dự án                PM          Toàn đội

### 9.5. Cơ chế xử lý vấn đề

**Cấp 1 -- Xử lý tại chuyên môn**

-   Backend → Backend Developer + Tech Lead.
-   Frontend → Frontend Developer + Backend/BA khi cần.
-   RS232/thiết bị → Hardware/IoT + Tech Lead/Onsite.
-   Nghiệp vụ → BA + thành viên liên quan.
-   Chất lượng → QA/QC + người thực hiện Work Package.
-   Triển khai hiện trường → Onsite + Hardware/Tech Lead.

**Cấp 2 -- Điều phối bởi PM**

PM tham gia khi vấn đề:

-   liên quan nhiều Work Package;
-   cần điều phối lại nguồn lực;
-   có nguy cơ ảnh hưởng tiến độ;
-   có nguy cơ ảnh hưởng chất lượng hoặc Go-live;
-   cần quyết định về ưu tiên.

**Cấp 3 -- Trình cấp tổ chức/chủ đầu tư**

PM trình lên cấp tương ứng khi vấn đề:

-   vượt thẩm quyền của đội dự án;
-   ảnh hưởng cam kết với chủ đầu tư;
-   ảnh hưởng phạm vi hoặc ngân sách đã được phê duyệt;
-   yêu cầu thay đổi quyết định ở cấp tổ chức.

### 9.6. Điều hành theo từng giai đoạn

  -----------------------------------------------------------------------
  Giai đoạn                           Trọng tâm nhân lực
  ----------------------------------- -----------------------------------
  T1                                  PM, Tech Lead, BA

  T2--T4                              PM, Tech Lead, BA, Backend,
                                      Frontend, Hardware; QA từ T3

  T5                                  Toàn đội đang còn hiệu lực, tăng
                                      cường QA và Onsite

  T6                                  PM, Tech Lead, Backend, Frontend,
                                      Hardware, QA, Onsite tập trung
                                      Go-live

  T7                                  PM, Tech Lead, Hardware, Backend,
                                      Frontend, QA, Onsite tập trung hai
                                      kho chi nhánh

  T8                                  PM, Tech Lead, Backend, QA, Onsite
                                      tập trung nghiệm thu và đóng dự án
  -----------------------------------------------------------------------

Việc tăng hoặc giảm mức độ tham gia của từng vai trò theo giai đoạn nhằm
sử dụng nguồn lực phù hợp với nhu cầu thực tế của từng Work Package,
thay vì duy trì tất cả nhân sự ở cùng một mức độ trong toàn bộ dự án.

### 9.7. Nguyên tắc cuối cùng

Cơ chế quản lý nguồn nhân lực của dự án được thống nhất theo các nguyên
tắc:

1.  Mỗi Work Package phải có người chịu trách nhiệm rõ ràng.
2.  PM chịu trách nhiệm điều phối tổng thể, không thay thế vai trò
    chuyên môn.
3.  Các thành viên chuyên môn được phối hợp trực tiếp theo công việc.
4.  Mọi trách nhiệm chính được xác định trong RACI/RAM.
5.  Nguồn lực được huy động theo thời điểm cần thiết của dự án.
6.  Vấn đề được giải quyết ở cấp thấp nhất có đủ năng lực.
7.  Vấn đề ảnh hưởng mục tiêu dự án phải được báo cáo PM.
8.  Vấn đề vượt thẩm quyền phải được trình cấp quyết định tương ứng.
9.  Chủ đầu tư, đại diện kho và nhà cung cấp được quản lý như các bên
    liên quan bên ngoài đội dự án.
10. Cơ cấu 8 vị trí chuyên trách phải thống nhất với phân bổ **50 MM**, lịch huy động và WBS.

------------------------------------------------------------------------
