# Ghi chú điều chỉnh báo cáo quản lý phạm vi

Đối chiếu [bản trước PR](https://github.com/NguyenHaiHung0510/QLDAPM-16/blob/ff5528889b6ef1c99a6802949228914328cc72a4/B%C3%81O%20C%C3%81O%20QU%E1%BA%A2N%20L%C3%9D%20PH%E1%BA%A0M%20VI%20D%E1%BB%B0%20%C3%81N.md) của Nguyễn Đức Công với [bộ gốc 01](../01-mo-ta-de-tai.md), [02](../02-du-toan-kinh-phi.md), [03](../03-ton-chi-du-an.md), [04](../04-ton-chi-du-an-day-du.md). Đây là ghi chú thay đổi của nhóm, tách khỏi nội dung chương 2.

## Phần giữ lại

Giữ sáu phần báo cáo, ba phương pháp thu thập yêu cầu, cách tổ chức WBS theo pha/bốn cấp, 42 mã gói gốc và các tên/mô tả còn phù hợp. Báo cáo gốc đã có RTM gồm 11 yêu cầu; bản sửa bổ sung vào ma trận này. Ngân sách hai tỷ, tám vị trí/50 MM, tám tháng và hạn kho tổng vận hành chậm nhất tháng 6 được giữ theo bộ gốc.

## Thay đổi và căn cứ

| Vị trí | Điều chỉnh | Lý do và căn cứ |
| --- | --- | --- |
| Thông tin đầu báo cáo; các dòng PM | Dùng PM Bùi Hồng Phú, đơn vị thi công Raumania; ghi công tác giả WBS ban đầu. | Thống nhất với 04, mục 1/5. Phân công viết BTL nằm ở N-03. |
| 1.1; 1.2.1.2; các gói tích hợp/lắp đặt | Kho tổng 2 cân/2 PC; mỗi chi nhánh 1 cân/1 PC; tổng 4 máy in/8 máy quét. Giả định 3 máy chấm công và thiết bị đo do doanh nghiệp cung cấp. | Số mua mới theo 02, mục IV. Tài sản sẵn có là giả định tại 01, được xác nhận khi khảo sát. |
| 1.2 và 6.2 | Giữ quy trình CR bốn bước; làm rõ người phê duyệt đường cơ sở và ghi tác động trong Change Log. Bỏ giới hạn ≤3 CR và cách đo phạm vi bằng số gói hoàn thành. | Bài giảng Quản lý phạm vi, trang 40: kiểm thay đổi so với baseline. Số gói hoàn thành phản ánh tiến độ; bộ gốc không đặt hạn mức số CR. |
| 2, RTM | Giữ mã FR-01–FR-08/NFR-01–NFR-03, bổ sung nguồn và điều kiện chấp nhận; thêm FR-09–FR-13, TR-01–TR-03 và PR-01. Tổng 20 yêu cầu. | 01 đã nêu nhật ký môi trường, ca/quyền, tài sản, danh mục trà và báo cáo; 02/04 có triển khai, đào tạo và bàn giao. RTM: bài giảng trang 17; PMBOK 6 §5.2.3.2, tr. 148–149. |
| 3.4; các ô nghiệm thu để trống | Điền <0,1% và <2 giây; định nghĩa sai số tương đối, khối lượng tham chiếu, dải sử dụng và điểm bắt đầu/kết thúc đo in. | Ngưỡng từ 04, mục 4. Công thức và điểm đo làm rõ ý nghĩa chỉ số; PMBOK 6 §5.3.3.1, tr. 154 yêu cầu điều kiện chấp nhận. |
| 3.4, bản chỉnh trước | Rút cỡ mẫu tự đặt 200 phép cân/120 tem và danh sách thao tác kiểm chi tiết; giao Test Plan cho chương 9, thống nhất trước nghiệm thu. | Lựa chọn mức chi tiết cho BTL: chương 2 xác định điều kiện đạt. PMBOK 6 §8.3.2.1 và §8.3.2.4, tr. 303 đặt cỡ mẫu, loại/quy mô kiểm trong kế hoạch chất lượng. |
| WBS 1.3.2.3, 1.3.4.3, 1.3.4.4 | Thêm ba gói: nhật ký môi trường; ca/phân quyền; tài sản/dụng cụ/vật tư. Tổng 45 gói và 45 mục Dictionary. | Ba nhóm chức năng đã có ở 01 nhưng chưa có đầu ra rõ trong WBS gốc. Cách tách ba gói phục vụ giao việc/ước lượng; bài giảng trang 32, PMBOK 6 tr. 161 về độ phủ toàn bộ công việc. |
| 1.2.3.1; 1.4.1.2 | Bổ sung môi trường dev/test vào gói kiến trúc; đào tạo kho tổng vào gói UAT/hướng dẫn đã có. Hai gói thêm ở bản chỉnh trước được gộp lại. | 02 có ngân sách môi trường; 04 yêu cầu đào tạo trước sử dụng. Giữ cấu trúc gốc và bổ sung đầu ra cần thiết; Dictionary được chi tiết hóa dần theo PMBOK 6 tr. 162. |
| Trách nhiệm ở các gói tháng 1, 7–8 | Dùng BA/Tech Lead khảo sát tháng 1; RS232 từ tháng 2, Onsite từ tháng 5. BA bàn giao tài liệu cuối tháng 5; vai trò còn tham gia tiếp nhận. | Lịch huy động/lương tại 02, mục II. Giữ tám vai trò hiện có; thay người phụ trách và bổ sung bàn giao thay cho tăng nhân sự. |
| 1.3.3.4; 1.4.1.3; 1.4.2.1 | Xác định dữ liệu mở kho gồm danh mục, lô và tồn đầu kỳ; kiểm/import/đối soát trước vận hành. | 01 yêu cầu nhập–xuất–tồn theo lô; số tồn ban đầu là đầu vào vận hành. 03/04 đã có chuyển dữ liệu Excel; làm rõ bộ dữ liệu để giới hạn công việc. |
| 1.4.2.1; 1.6.2.1–1.6.3.2 | Bổ sung triển khai ứng dụng/CSDL, sao lưu/khôi phục, tài khoản và hướng dẫn vận hành; doanh nghiệp tiếp nhận phí duy trì sau tháng 8. | 02, mục III/V/VI và 04, mục 3/6. Khoản 25 triệu có thời hạn tám tháng dự án; phạm vi cần có đầu ra bàn giao vận hành. |
| Mốc go-live; hãng/giao thức; 1.4.2.3 | Giữ hạn “chậm nhất tháng 6”; bỏ lý do mùa cao điểm. Ghi thiết bị/giao thức theo yêu cầu tương thích; thay cam kết xử lý mọi sự cố/15 phút bằng hồ sơ hỗ trợ. | Hạn từ 01/04; số lượng từ 02. Mùa vụ, hãng cho cả bốn máy, ASCII cho mọi thiết bị và SLA 15 phút thiếu căn cứ trong bộ gốc. |
| Văn phong và nguồn | Bỏ lời giải thích theo hội thoại; giữ câu mô tả công việc/đầu ra. Nêu tên bài giảng, file và trang; khôi phục tên/mô tả gốc còn đúng. | Tài liệu chung phải đọc được từ nguồn trong repo. Bài giảng trang 14/19 và PMBOK 6 §5.3.3.1 hướng dẫn nội dung phạm vi; cách diễn đạt được chỉnh để rõ và gọn. |

## Nguồn tham khảo

- **Bài giảng Quản lý dự án phần mềm — Quản lý phạm vi dự án**, ThS. Ngô Tiến Đức: [tai-lieu/4-scope.pdf](../tai-lieu/4-scope.pdf), trang 14, 17, 19, 28–32, 38–41.
- **Project Management Institute (2017), A Guide to the Project Management Body of Knowledge (PMBOK® Guide), Sixth Edition**: các mục/trang dẫn trong bảng là số trang bản in. Sách được dùng làm nguồn tham khảo; các số thiết bị, ngân sách và ngưỡng của dự án lấy từ 01–04.

Giả định tài sản sẵn có và thông số SRS cần được xác nhận trong dự án giả định. Ghi chú này phản ánh sửa tài liệu; kết quả chạy phần mềm/thiết bị và bản xuất PDF được ghi nhận riêng.

