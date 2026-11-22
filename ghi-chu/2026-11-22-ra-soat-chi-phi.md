# Rà soát và cập nhật hồ sơ chi phí ngày 22/11/2026

Ghi chú đối chiếu để nhóm tích hợp tài liệu, không ghép nguyên ghi chú này thành nội dung chương 4.

## 1. Phạm vi và phiên bản đã kiểm

- Repo: [NguyenHaiHung0510/QLDAPM-16](https://github.com/NguyenHaiHung0510/QLDAPM-16), nhánh `main`, commit [`bc0593ccee1778c269bc924496b839e8bf28a74c`](https://github.com/NguyenHaiHung0510/QLDAPM-16/tree/bc0593ccee1778c269bc924496b839e8bf28a74c).
- Bài chi phí cũ trong `quản lý chi phí.rar`: hai Markdown và `Bang_tinh_chi_phi_WMS.xlsx`.
- Bài giảng `6-cost.pdf` của ThS. Ngô Tiến Đức, 31 trang; slide `_Quản lý Chi phí Dự án Phần mềm - Nhóm 3.pdf`, 89 trang; tài liệu môn học và các chương hiện có trong repo.

Tên học phần trong `tai-lieu/0-intro.pdf`, trang 3 là **Quản lý dự án phần mềm**. Đây là tên được xác định bởi bộ nguồn đang đối chiếu; không suy ra hai học phần Quản lý dự án phần mềm và Phân tích, thiết kế hệ thống thông tin là một. Bốn nội dung phân công ở trang 14 là phạm vi, thời gian, chi phí và nhân lực, không phải bốn pha của dự án.

Tài liệu đính kèm/repo được dùng làm chứng cứ về nội dung và yêu cầu. Những câu hướng dẫn làm việc, sử dụng công cụ hoặc đề xuất trong tài liệu không được tự coi là yêu cầu mới của người dùng hay quyết định đã được phê duyệt.

## 2. Kết luận về bản cũ

**Bản cũ đúng về tổng dự toán và nhiều nguyên tắc kiểm soát, nhưng không còn phù hợp để dùng nguyên trạng cùng lịch hiện hành.**

| Nội dung | Kết quả đối chiếu | Xử lý ở bản mới |
| --- | --- | --- |
| Lương, kỳ huy động | 8 vị trí, 50 MM, 1.667 triệu, khớp tài liệu 02 và kế hoạch nhân lực. | Giữ nguyên. Không thay bằng đội bốn sinh viên. |
| Tổng kinh phí | 1.667 +130 +25 +35 +143 =2.000 triệu VNĐ. | Giữ nguyên, không tăng/giảm ngân sách gốc. |
| Mã WBS | 45/45 mã lá của bảng cũ trùng WBS hiện hành. | Giữ mã và truy vết; không tạo gói công việc giả để hấp thụ lương. |
| Nguồn/phiên bản | Sổ nguồn cũ còn ghi mốc 09/10/2026 và chưa có chương nhân lực/tiến độ độc lập. | Cập nhật commit, chương 3 và nhân lực hiện hành, bài giảng chi phí được cung cấp. |
| Phân bổ nhân công | Có 31 ô vai trò-WBS-tháng ghi công ở kỳ WBS không có hoạt động trong lịch mới: tổng 4,10 MM, tương đương 131,45 triệu. Đây là kiểm cửa sổ WBS, chưa phải toàn bộ sai lệch về vai trò/khối lượng. | Thay phân bổ chủ quan cũ bằng truy vết theo hoạt động, vai trò và ngày của lịch hiện hành; nêu rõ quy ước chia. |
| Khả năng phân rã 50 MM | Lịch hiện có 341,3 ngày công trên 1.053 ngày khả dụng; không thể kết luận 50 MM đã được phân rã đầy đủ. | Giữ nguyên lương huy động; thể hiện riêng phần đã quy thuộc và chưa gán hoạt động. |
| Kế hoạch chi phí | Đã có ngưỡng, EV, trách nhiệm, nhưng chưa chốt rõ đủ sáu nội dung bài giảng trang 9. | Thêm bảng sáu quy định, CA-WBS, làm tròn, thời hạn rà soát và phân tích nhạy cảm. |
| Bản để ghép PDF | Chương cũ chủ yếu là quy trình; yêu cầu mở Excel mới xem được ngân sách/công thức. | Đưa bảng lương, cơ cấu 2 tỷ, tám kỳ và ví dụ EVM độc lập vào chương chính; phụ lục có bảng 45 gói. |
| Mẫu theo dõi | Bản cũ không bắt đủ metadata/bằng chứng trước khi thể hiện mọi chỉ tiêu; có validation trùng. | Tạo lại mẫu theo dõi; để trống actuals; phân biệt mẫu và ví dụ. |
| EVM và dự phòng | Các nguyên tắc AC khác thanh toán, EV theo đầu ra, dự phòng không tự tạo EV/AC là phù hợp. | Giữ và làm rõ điều kiện áp dụng. Không tính CPI toàn dự án từ ngân sách chưa có PV đầy đủ. |

Ví dụ về lệch kỳ: bảng cũ gán Backend/Frontend của WBS 1.3.4.3 vào T2, trong khi hoạt động A18 của lịch hiện hành chạy 31/08-07/09/2027. Công RS232 ở WBS 1.3.3.1 còn được gán sang T3/T4, trong khi các hoạt động G1/A21 thuộc T2. Lệch này không chứng minh tổng lương sai, nhưng làm phân bổ gói-tháng cũ không còn dùng được nguyên trạng.

Không coi việc mua thiết bị trước tháng lắp đặt là lỗi: bộ mẫu 33 triệu ở T2, phần còn lại kho tổng 37 triệu ở T5 và chi nhánh 60 triệu ở T6 là chủ ý của tài liệu 02 và lịch hiện hành.

## 3. Thay đổi về cách phân bổ và giới hạn

Bản mới quy thuộc chi phí mô hình theo `lương tháng × ngày công mô hình / ngày khả dụng trong chính kỳ`. Hoạt động gắn nhiều WBS được chia đều giữa các mã như một giả định phân bổ minh bạch. Tổng hợp kết quả chưa làm tròn trung gian:

| Khoản đối chiếu | VNĐ, làm tròn đến đồng |
| --- | ---: |
| Lương quy thuộc hoạt động/LoE | 509.996.472 |
| Lương huy động chưa gán hoạt động | 1.157.003.528 |
| **Lương huy động giữ nguyên** | **1.667.000.000** |
| Thiết bị, hạ tầng và công tác | 190.000.000 |
| **Cộng trước dự phòng** | **1.857.000.000** |
| Contingency reserve giữ trong ngân sách | 143.000.000 |
| **Tổng kinh phí theo bộ gốc** | **2.000.000.000** |

Đây là cách đối chiếu ngân sách với độ chi tiết hiện có của lịch, không phải kết luận chi phí thực sự chỉ khoảng 510 triệu. Không coi phần chưa gán là tiết kiệm, lợi nhuận hoặc dự phòng mới. Tỷ lệ chia nhiều WBS và phương thức quy thuộc lương là giả định mới cần nhóm thẩm định. Khi nhóm chọn cách khác, phải cập nhật đồng bộ chương 3, nhân lực và chi phí chịu ảnh hưởng.

## 4. Đối chiếu yêu cầu của giảng viên

| Yêu cầu/căn cứ | Vị trí trong hồ sơ mới |
| --- | --- |
| Trang 31 `6-cost.pdf`: tìm hiểu phương pháp; lập kế hoạch, ước lượng và phân bổ ngân sách cho bài nhóm. | Chương 4, mục 4.2-4.4; bảng tính nguồn lực, ngoài lương và WBS-tháng. |
| Trang 9: đơn vị, độ chính xác, tài khoản kiểm soát, ngưỡng, quy tắc đo, báo cáo. | Bảng sáu quy định tại 4.2.1. |
| Trang 11, 19-21: giả định, biến động, hiệu lực, effort và giá nguồn lực. | Mục 4.3; bảng lương; phụ lục phương pháp và đối chiếu nguồn lực. |
| Trang 13-14, 22-24: dự phòng, thời gian, tổng hợp ngân sách, nhu cầu vốn. | Mục 4.4-4.5; 143 triệu còn tách rõ khỏi lịch phân bổ trước dự phòng. |
| Trang 25-30: theo dõi, PV/EV/AC, CPI, EAC, ETC, TCPI, thay đổi. | Mục 4.6-4.7; các mẫu `So_chi_phi`, `Theo_doi` và ví dụ `EVM`. |
| `0-intro.pdf`, trang 12-14: quyển PDF chín chương, ghi đóng góp, đồng bộ các phần. | Chương chính có số liệu đọc độc lập; ghi người phụ trách; không thay thế toàn bộ quyển chín chương. |

Bài giảng trang 31 không bắt buộc NPV/ROI/Payback. Slide Nhóm 3 trình bày các chỉ số đó trong phần lựa chọn đầu tư, nhưng chưa có dòng lợi ích của WMS; bản sửa không tạo thêm lợi ích tài chính giả định để tính chúng.

Slide Nhóm 3 cần đọc có kiểm tra: trang PDF 52 đặt tiêu đề EV nhưng đoạn định nghĩa lại là PV; trang 59 gọi cập nhật ETC bottom-up là “Re-base”, dễ nhầm với thay đường cơ sở; trang 83 có PV lũy kế tháng 5 cao hơn vốn cấp lũy kế 70 triệu. Bản mới dùng định nghĩa/công thức bài giảng và phân biệt dự báo, baseline, PV, nhu cầu vốn và thanh toán.

Slide giới thiệu trang 14 có quy định về sao chép/AI; N-01/N-02 ghi nhận thêm lời xác nhận của Hưng về việc dùng AI phản biện bản nháp. Đây là bối cảnh yêu cầu học phần, không phải bằng chứng rằng bản sửa đã được giảng viên chấp nhận. Thành viên phụ trách cần kiểm tra, tự chịu trách nhiệm nội dung và trình bày phần mình.

## 5. Điểm nhóm cần thống nhất trước khi khóa baseline

1. **50 MM so với nỗ lực lịch:** làm rõ công phối hợp/hỗ trợ và mức chi tiết của lịch, hoặc đánh giá điều chỉnh huy động bằng quyết định riêng. Không sửa lương để làm khớp một mô hình chưa đủ chi tiết.
2. **Ngân sách gói và đo hoàn thành:** thẩm định tỷ lệ chia nhiều WBS, phần lương chưa gán và trọng số mốc. Chưa có căn cứ để đưa toàn bộ 2 tỷ vào bảng EVM thực hiện.
3. **143 triệu contingency:** xác nhận Risk Register, chi phí ứng phó tăng thêm, kỳ bố trí và quyền phê duyệt. Không đổi sang management reserve.
4. **Giá và vốn:** xác nhận giá/hạng mục đi kèm, khoản ngoài lương, tài sản khách hàng, điều khoản thanh toán và nguồn cấp vốn. Tổng chi phí đúng không chứng minh tiền luôn sẵn tại từng kỳ.

Các điểm trên thuộc quyết định chung hoặc dữ liệu còn thiếu, không được đánh dấu “đã duyệt” trong bản sửa. Hồ sơ hiện phù hợp để đưa lên repo cho nhóm rà soát và tích hợp; trước khi nộp cần giải quyết hoặc công khai đúng trạng thái các giả định có ảnh hưởng.

## 6. Tệp đưa vào repo

| Đường dẫn | Mục đích |
| --- | --- |
| `05-quan-ly-chi-phi.md` | Chương 4 có phương pháp, bảng số liệu, kiểm soát và nguồn. |
| `05a-thuyet-minh-chi-phi.md` | Cách phân bổ, đối chiếu tám kỳ, ngân sách truy vết của 45 gói và hướng dẫn đọc bảng tính. |
| `Bang_tinh_chi_phi_WMS.xlsx` | Dữ liệu/công thức, phần lương chưa gán, dự phòng và mẫu theo dõi. |
| `chuong-4/co-so-phan-bo.json` | Bản dữ liệu cùng phiên bản để truy từ hoạt động-vai trò-kỳ tới phân bổ WBS; tiền dùng VNĐ. |
| `tai-lieu/6-cost.pdf` | Bản bài giảng được cung cấp, giữ nguyên nội dung để truy nguồn. |
| `ghi-chu/2026-11-22-ra-soat-chi-phi.md` | Ghi chú kiểm tra và vấn đề cần phối hợp; không ghép vào chương nộp. |

Không sửa nội dung phạm vi, lịch hoặc nhân lực của ba thành viên khác. Trạng thái phát hành được theo dõi bằng lịch sử Git và PR tương ứng. Kiểm tra số học và định dạng chỉ xác nhận tính nhất quán của hồ sơ; không thay phê duyệt của chủ đầu tư giả định hoặc đánh giá của giảng viên.
