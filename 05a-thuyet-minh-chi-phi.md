# PHỤ LỤC A. THUYẾT MINH PHÂN BỔ CHI PHÍ

**Dự án:** Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS).  
**Nhóm 16. Người phụ trách:** Nguyễn Tuấn Dũng.  
**Phiên bản:** 22/11/2026; đi kèm [Chương 4](05-quan-ly-chi-phi.md) và [bảng tính chi phí](Bang_tinh_chi_phi_WMS.xlsx).

Phụ lục trình bày cách nối lịch, nguồn lực và các khoản chi với 45 gói WBS hiện hành. Bảng theo gói chỉ gồm **chi phí đã truy vết** theo giả định phân bổ bên dưới, chưa phải BAC hoàn chỉnh của từng gói. Phần lương huy động chưa gán hoạt động và quỹ dự phòng được giữ rõ để tổng ngân sách vẫn là 2 tỷ VNĐ.

## A.1. Quy ước tính theo kỳ

Tháng dự án tính từ ngày 03 đến hết ngày 02 tháng sau. Lịch làm việc và ngày nghỉ là giả định của chương 3. Không thay bằng số ngày cố định 22 ngày cho mọi tháng khi quy đổi công. Trong bảng này, mỗi vai trò được huy động trọn các tháng đã ghi trong tài liệu 02.

| Kỳ | Từ ngày | Đến ngày | Ngày làm việc khả dụng |
| --- | --- | --- | ---: |
| T1 | 03/06/2027 | 02/07/2027 | 22 |
| T2 | 03/07/2027 | 02/08/2027 | 21 |
| T3 | 03/08/2027 | 02/09/2027 | 22 |
| T4 | 03/09/2027 | 02/10/2027 | 20 |
| T5 | 03/10/2027 | 02/11/2027 | 22 |
| T6 | 03/11/2027 | 02/12/2027 | 22 |
| T7 | 03/12/2027 | 02/01/2028 | 21 |
| T8 | 03/01/2028 | 02/02/2028 | 18 |

Với một vai trò trong một kỳ đang huy động:

- `Ngày công mô hình = tổng (số ngày hoạt động trong kỳ × tỷ lệ phân công) + công LoE trong kỳ`.
- `MM quy đổi của kỳ = ngày công mô hình / số ngày làm việc khả dụng trong chính kỳ`.
- `Lương quy thuộc hoạt động = MM quy đổi × lương tháng của vai trò`.
- `Lương huy động chưa gán hoạt động = lương huy động kỳ - lương quy thuộc hoạt động`.

LoE là công quản lý xuyên kỳ đã nêu trong chương 3. Phần LoE kết thúc cùng mốc M6 đề xuất ngày 17/01/2028; ngân sách lương vẫn giữ hết kỳ huy động theo tài liệu 02. Nguồn lực đã đặt trong các khối dự phòng thời gian được tính trong lương huy động, không cộng lại phần lương ấy vào quỹ tiền 143 triệu.

Tổng công hoạt động/LoE hiện tại là **341,3 ngày công**, quy đổi **16,14765 MM** theo từng kỳ. Tổng **50 MM** của bảng lương là kỳ huy động nhân sự. Hai đại lượng có cơ sở khác nhau; phần chênh khoảng **33,85235 MM** chưa được gán vào các hoạt động hiện hành. Không tự coi phần này là công đã thực hiện, tiết kiệm hay dự phòng; cũng không tạo thêm WBS để hấp thụ số dư.

### A.1.1. Ví dụ kiểm tra

**Kỹ sư RS232 ở T2:** lịch ghi 14,6 ngày công trong 21 ngày khả dụng. Công quy đổi là `14,6 / 21 = 0,6952381 MM`; lương quy thuộc hoạt động là `32 × 14,6 / 21 = 22,247619 triệu VNĐ`. Phần huy động chưa gán là `32 - 22,247619 = 9,752381 triệu VNĐ`. Tổng vẫn là 32 triệu của kỳ, không thay điều khoản trả lương bằng công thức quy thuộc chi phí.

**Frontend ở T6:** lịch hiện hành ghi 0 ngày công cho vai trò này nhưng tài liệu 02 vẫn huy động trong T2-T7. Lương T6 do đó vẫn là 24 triệu; phần quy thuộc hoạt động bằng 0, phần chưa gán bằng 24 triệu. Đây là điểm cần làm rõ độ chi tiết lịch hoặc cách huy động, không phải căn cứ tự giảm ngân sách hay ghi nhận hoàn thành công việc.

### A.1.2. Hoạt động gắn nhiều WBS

Mỗi dòng hoạt động-vai trò-kỳ chỉ được tính chi phí một lần. Khi hoạt động gắn `n` mã WBS, phương án hiện tại chia đều MM và chi phí cho `n` mã. Đây là **giả định phân bổ mới cần nhóm thẩm định**, không phải tỷ lệ nghiệm thu hay tỷ lệ hoàn thành đầu ra. Ví dụ A01 gắn ba mã 1.1.1.1, 1.1.1.2 và 1.1.1.3; phần công mỗi vai trò của A01 được chia ba, không cộng nguyên giá trị A01 vào từng mã.

Nếu thay bằng tỷ lệ có căn cứ, tổng các tỷ lệ của cùng hoạt động-vai trò-kỳ phải bằng 100%; cập nhật đồng thời các bảng theo WBS, kỳ và tài khoản kiểm soát. Giữ đủ 45 mã nguồn hiện hành.

## A.2. Đối chiếu lương qua tám kỳ

Đơn vị: **triệu VNĐ**, trình bày ba chữ số thập phân. Cột “chưa gán” là một phần của lương huy động, không phải khoản chi cộng thêm.

| Kỳ | Lương quy thuộc hoạt động/LoE | Lương huy động chưa gán hoạt động | Tổng lương huy động |
| --- | ---: | ---: | ---: |
| T1 | 68,864 | 61,136 | 130,000 |
| T2 | 95,319 | 117,681 | 213,000 |
| T3 | 91,514 | 141,486 | 233,000 |
| T4 | 59,835 | 173,165 | 233,000 |
| T5 | 53,932 | 197,068 | 251,000 |
| T6 | 46,950 | 174,050 | 221,000 |
| T7 | 50,967 | 170,033 | 221,000 |
| T8 | 42,617 | 122,383 | 165,000 |
| **Tổng** | **509,996** | **1.157,004** | **1.667,000** |

Các tổng được tính từ số chưa làm tròn. Ba chữ số thập phân của đơn vị triệu tương đương 1.000 VNĐ; tổng các số đã làm tròn trên từng dòng có thể lệch một vài đơn vị hiển thị. Bảng tính giữ đầy đủ độ chính xác của phép phân bổ và trình bày tiền theo VNĐ. Độ chính xác số học không chứng minh độ chắc chắn của ước lượng.

## A.3. Chi phí đã truy vết tới 45 gói WBS

Đơn vị: **triệu VNĐ**, ba chữ số thập phân. “Ngoài lương” gồm thiết bị, hạ tầng và công tác đã quy thuộc theo mục đích sử dụng, tổng 190 triệu. Gán khoản mua sắm cho gói không làm thay đổi thời điểm nhận hàng: thiết bị có thể được nhận trước khi gói lắp đặt bắt đầu. Các khoản dịch vụ/công tác giữ kỳ và hạn mức của tài liệu 02.

Ngân sách trong từng dòng dưới đây chỉ phản ánh phần **đã truy vết theo mô hình đề xuất**, chưa bao gồm phần lương chưa gán hoạt động hoặc dự phòng và chưa dùng làm BAC gói để đo EVM. Cần hoàn thiện ngân sách gói và quy tắc đo trước phê duyệt.

| WBS | Gói công việc | Lương quy thuộc | Ngoài lương | Cộng đã truy vết |
| --- | --- | ---: | ---: | ---: |
| 1.1.1.1 | Xây dựng Kế hoạch Quản lý Dự án Tổng thể (PMP) | 2,652 | 0,000 | 2,652 |
| 1.1.1.2 | Xây dựng Kế hoạch Quản lý Phạm vi & Từ điển WBS | 2,652 | 0,000 | 2,652 |
| 1.1.1.3 | Lập Tiến độ Chi tiết & Phân bổ Ngân sách BAC 2.0 Tỷ | 3,591 | 0,000 | 3,591 |
| 1.1.2.1 | Tổ chức Họp Giao ban Định kỳ | 38,056 | 0,000 | 38,056 |
| 1.1.2.2 | Theo dõi, Kiểm soát Chi phí & Quỹ Dự phòng (143 triệu) | 19,028 | 0,000 | 19,028 |
| 1.1.2.3 | Báo cáo Tiến độ Định kỳ cho Project Sponsor | 19,028 | 0,000 | 19,028 |
| 1.1.3.1 | Tiếp nhận & Đánh giá Yêu cầu Thay đổi (CR) | 57,083 | 0,000 | 57,083 |
| 1.1.3.2 | Đảm bảo Chất lượng Quy trình (QA) | 11,222 | 0,000 | 11,222 |
| 1.2.1.1 | Khảo sát Luồng Nhập/Chế biến/Xuất tại Kho Tổng Thái Nguyên | 4,091 | 3,000 | 7,091 |
| 1.2.1.2 | Khảo sát Cổng Giao tiếp RS232 Trạm Cân, Máy in & Máy Chấm công | 4,091 | 0,000 | 4,091 |
| 1.2.1.3 | Thu thập Biểu mẫu Excel Dữ liệu Cũ & Định mức BOM | 3,545 | 0,000 | 3,545 |
| 1.2.2.1 | Lập Đặc tả Use-case cho 6 Nhóm Người dùng | 6,848 | 0,000 | 6,848 |
| 1.2.2.2 | Thống nhất Chuẩn Giao tiếp RS232/COM & In Tem | 5,591 | 0,000 | 5,591 |
| 1.2.3.1 | Thiết kế Kiến trúc Web App trên Máy trạm Windows | 13,591 | 13,000 | 26,591 |
| 1.2.3.2 | Thiết kế CSDL Đồng bộ 3 Kho & Cơ chế Đệm Dữ liệu Offline | 6,909 | 0,000 | 6,909 |
| 1.2.3.3 | Thiết kế Giao diện (UI/UX) cho Thủ kho, Công nhân & Lãnh đạo | 3,545 | 0,000 | 3,545 |
| 1.3.1.1 | Lập trình Chức năng Nhập/Xuất/Kiểm kê & Sơ đồ Zone/Bin/Rack | 27,029 | 0,000 | 27,029 |
| 1.3.1.2 | Lập trình Thuật toán Xuất kho Ưu tiên FEFO | 9,010 | 0,000 | 9,010 |
| 1.3.2.1 | Lập trình Công thức Quy đổi BOM theo Độ ẩm & Hao hụt Chè | 13,310 | 0,000 | 13,310 |
| 1.3.2.2 | Lập trình Cảnh báo Tồn kho Dưới ngưỡng, Cận hạn/Hết hạn & Báo cáo Tuổi hàng (Aging) | 8,600 | 0,000 | 8,600 |
| 1.3.2.3 | Phát triển nhật ký nhiệt độ và độ ẩm môi trường | 6,450 | 0,000 | 6,450 |
| 1.3.3.1 | Lập trình Service Kết nối RS232 Đọc Dữ liệu Cân Tự động | 13,295 | 0,000 | 13,295 |
| 1.3.3.2 | Lập trình Module Tạo Mã QR & Điều khiển Máy in Tem | 10,381 | 0,000 | 10,381 |
| 1.3.3.3 | Lập trình Tích hợp Máy quét QR & Máy chấm công | 9,407 | 0,000 | 9,407 |
| 1.3.3.4 | Lập trình Công cụ Import/Export Danh mục và Tồn đầu kỳ từ Excel | 8,600 | 0,000 | 8,600 |
| 1.3.4.1 | Lập trình Dashboard KPI, Báo cáo Doanh thu & Giá vốn cho Lãnh đạo | 9,460 | 0,000 | 9,460 |
| 1.3.4.2 | Lập trình Module Quản lý Nhà cung cấp, Kế toán Kho & Tài xế | 15,050 | 0,000 | 15,050 |
| 1.3.4.3 | Phát triển lịch ca và phân quyền vai trò | 9,030 | 0,000 | 9,030 |
| 1.3.4.4 | Phát triển danh mục tài sản dụng cụ và vật tư | 7,095 | 0,000 | 7,095 |
| 1.3.5.1 | Kiểm thử Luồng Dữ liệu Cân RS232 đến Web App | 16,508 | 0,000 | 16,508 |
| 1.3.5.2 | Kiểm thử Tốc độ In Tem & Thuật toán FEFO/BOM | 26,134 | 0,000 | 26,134 |
| 1.4.1.1 | Lắp đặt PC, Trạm Cân RS232, Máy in, Máy quét tại Kho Tổng | 7,321 | 81,000 | 88,321 |
| 1.4.1.2 | Xây dựng Kịch bản UAT & Hướng dẫn 6 Nhóm Người dùng | 17,333 | 0,000 | 17,333 |
| 1.4.1.3 | Khởi tạo Dữ liệu Danh mục Trà Ban đầu từ File Excel | 4,844 | 0,000 | 4,844 |
| 1.4.2.1 | Chuyển đổi Dữ liệu Sang Môi trường Vận hành Thực tế | 8,177 | 6,000 | 14,177 |
| 1.4.2.2 | Đưa Kho Tổng vào Vận hành Chính thức | 3,100 | 0,000 | 3,100 |
| 1.4.2.3 | Onsite Hỗ trợ Kỹ thuật Trực tiếp tại Thái Nguyên | 12,136 | 8,000 | 20,136 |
| 1.5.1.1 | Lắp đặt Phần cứng & Thiết bị tại 02 Kho Chi nhánh Phân phối | 16,346 | 69,000 | 85,346 |
| 1.5.2.1 | Cấu hình Đồng bộ CSDL Liên kho & Cơ chế Hoạt động Offline | 12,824 | 3,000 | 15,824 |
| 1.5.3.1 | Đào tạo Thao tác Phần mềm cho Thủ kho & Nhân sự 2 Chi nhánh | 4,210 | 0,000 | 4,210 |
| 1.6.1.1 | Đo đạc Sai số Cân Tự động qua RS232 | 5,491 | 0,000 | 5,491 |
| 1.6.1.2 | Đo Thời gian Tạo & In Tem | 3,897 | 0,000 | 3,897 |
| 1.6.2.1 | Hoàn thiện Bộ Tài liệu Dự án | 10,013 | 0,000 | 10,013 |
| 1.6.3.1 | Ký Biên bản UAT & Nghiệm thu Tổng thể với Project Sponsor | 8,189 | 4,000 | 12,189 |
| 1.6.3.2 | Bàn giao Hệ thống, Đóng gói Mã nguồn & Đóng Dự án | 5,233 | 3,000 | 8,233 |
| **Cộng 45 gói** | **Phần đã truy vết** | **509,996** | **190,000** | **699,996** |
| Không tạo mã WBS | Lương huy động chưa gán hoạt động, đối chiếu riêng | 1.157,004 | 0,000 | 1.157,004 |
| **Cộng trước dự phòng** | **Lương toàn kỳ và các khoản ngoài lương** | **1.667,000** | **190,000** | **1.857,000** |
| Theo dõi riêng | Contingency reserve trong ngân sách gốc, chưa gán kỳ/gói | | | 143,000 |
| **Tổng kinh phí/BAC theo tài liệu 02** | | | | **2.000,000** |

Không cộng tổng bảng nhân lực với tổng bảng WBS: chúng là hai cách tổng hợp cùng các khoản lương. Không cộng 143 triệu dự phòng vào chi phí quản lý của WBS 1.1.2.2; tiền lương quản lý quỹ đã nằm trong nguồn lực PM, còn quỹ là hạn mức chi rủi ro riêng trong tổng 2 tỷ.

## A.4. Đọc và cập nhật bảng tính

| Trang tính | Nội dung và cách dùng |
| --- | --- |
| `Tong_hop` | Xem cơ cấu ngân sách, phân bổ tám kỳ và phần lương chưa gán hoạt động. Đây chưa phải đường PV đầy đủ. |
| `Nhan_luc` | Đối chiếu lương/kỳ huy động với công quy đổi từ lịch; kiểm phần đã quy thuộc và phần chưa gán. Tỷ lệ chia WBS là giả định cần được rà soát. |
| `Ngoai_luong` | Kiểm số lượng, đơn giá, tháng và WBS của thiết bị, hạ tầng, công tác. Bộ mẫu T2 thuộc thiết bị kho tổng, không mua trùng. |
| `WBS_thang` | Xem phần chi phí đã truy vết của 45 gói theo kỳ và dòng đối chiếu lương chưa gán; chưa dùng làm BAC/PV từng gói đã duyệt. |
| `Du_phong` | Xem sáu hạn mức rủi ro đề xuất, tổng 143 triệu; đối chiếu Risk Register và chi phí tăng thêm trước khi trình sử dụng. |
| `So_chi_phi` | Ghi phát sinh thực tế và thanh toán từ chứng từ. Thanh toán khoản đã ghi AC không tạo AC lần thứ hai. |
| `Theo_doi` | Nhập dữ liệu chỉ khi có ngân sách gói cùng phạm vi đã duyệt, ngày trạng thái và bằng chứng. Trường chưa có dữ liệu giữ trống. |
| `EVM` | Ví dụ công thức độc lập để kiểm tra cách tính; không phải số liệu thực hiện của dự án WMS. |
| `Nguon_gia_dinh` | Tra phiên bản nguồn, phương pháp quy thuộc, giả định chia WBS và những đầu vào cần xác nhận. |

Bản dữ liệu [cơ sở phân bổ](chuong-4/co-so-phan-bo.json) lưu 254 dòng hoạt động-vai trò-kỳ, danh sách WBS liên quan và 173 dòng phân bổ vai trò-WBS để kiểm lại cách tính. Tiền trong bản dữ liệu dùng VNĐ; bảng tính dùng triệu VNĐ. Đây là bản chụp cùng phiên bản, không tự cập nhật khi lịch đổi.

Khi thay lịch hoặc huy động, tính lại nỗ lực từng vai trò trong từng kỳ rồi cập nhật bản dữ liệu, phần quy thuộc và phần chưa gán trong bảng tính. Khi chỉ thay tỷ lệ chia giữa WBS, tổng chi phí hoạt động-vai trò-kỳ phải giữ nguyên. Thay lương, số lượng thiết bị, tổng kinh phí hoặc đường cơ sở cần hồ sơ thay đổi theo chương 4; không sửa số nguồn để bù chênh lệch.

Trước ghép báo cáo, đối chiếu đủ 45 mã, tổng 50 MM huy động, lương 1.667 triệu, ngoài lương 190 triệu và dự phòng 143 triệu. Kiểm cả số theo kỳ, gói và nguồn; khớp tổng số học chưa chứng minh ngân sách từng gói, lịch mua sắm hoặc mức công đã được phê duyệt.

## A.5. Nguồn dữ liệu

- [Dự toán kinh phí](https://github.com/NguyenHaiHung0510/QLDAPM-16/blob/bc0593ccee1778c269bc924496b839e8bf28a74c/02-du-toan-kinh-phi.md): mục II-V: lương, kỳ huy động, số lượng/giá thiết bị, hạ tầng, công tác và quỹ dự phòng.
- [Báo cáo quản lý phạm vi](https://github.com/NguyenHaiHung0510/QLDAPM-16/blob/bc0593ccee1778c269bc924496b839e8bf28a74c/B%C3%81O%20C%C3%81O%20QU%E1%BA%A2N%20L%C3%9D%20PH%E1%BA%A0M%20VI%20D%E1%BB%B0%20%C3%81N.md): mục 4-5: 45 mã, tên gói và từ điển WBS; mục 6: xác nhận/kiểm soát thay đổi.
- [Chương 3. Quản lý thời gian](https://github.com/NguyenHaiHung0510/QLDAPM-16/blob/bc0593ccee1778c269bc924496b839e8bf28a74c/CHUONG-3-QUAN-LY-THOI-GIAN.md): mục 3.4.4: nỗ lực mô hình khác kỳ lương huy động; mục 3.5.3: điều kiện sử dụng EVM.
- [Dữ liệu lịch](https://github.com/NguyenHaiHung0510/QLDAPM-16/blob/bc0593ccee1778c269bc924496b839e8bf28a74c/chuong-3/du-lieu-lich.json): hoạt động, tỷ lệ nguồn lực và sáu phân bổ LoE.
- [Kết quả lịch](https://github.com/NguyenHaiHung0510/QLDAPM-16/blob/bc0593ccee1778c269bc924496b839e8bf28a74c/chuong-3/ket-qua-lich.json): ngày bắt đầu/kết thúc và ngày công của lịch đề xuất.
- [Tải nguồn lực theo ngày](https://github.com/NguyenHaiHung0510/QLDAPM-16/blob/bc0593ccee1778c269bc924496b839e8bf28a74c/chuong-3/tai-nguon-luc.csv): đối chiếu nỗ lực từng vai trò-tháng với tổng các hoạt động/LoE.
- [Kế hoạch quản lý nhân lực](https://github.com/NguyenHaiHung0510/QLDAPM-16/blob/bc0593ccee1778c269bc924496b839e8bf28a74c/K%E1%BA%BF%20ho%E1%BA%A1ch%20qu%E1%BA%A3n%20l%C3%BD%20nh%C3%A2n%20l%E1%BB%B1c.md): cơ cấu tám vị trí, 50 MM và ma trận tham gia T1-T8.

Các liên kết trên cố định tại commit `bc0593ccee1778c269bc924496b839e8bf28a74c`, là phiên bản dùng trong lượt đối chiếu này. Bài giảng [6-cost.pdf](tai-lieu/6-cost.pdf), trang 9, 11, 20 và 31, cung cấp căn cứ về kế hoạch, ước lượng và yêu cầu bài tập; cách áp dụng được trình bày ở chương 4. Tệp đính kèm *\_Quản lý Chi phí Dự án Phần mềm - Nhóm 3.pdf* chỉ là tài liệu tham khảo phương pháp/trình bày. Các dòng ngoài lương và hạn mức dự phòng được kế thừa bộ bài cũ *quản lý chi phí.rar*, sau đó đối chiếu lại với tài liệu 02; không coi các hạn mức chi tiết là báo giá hoặc phê duyệt mới.
