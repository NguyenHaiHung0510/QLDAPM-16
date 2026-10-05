# N-04 · Bối cảnh tài liệu gốc và bản tôn chỉ đầy đủ

Cập nhật ngày 05/10/2026. Ghi chú làm việc, không ghép vào bài nộp; không dùng để quản lý deadline hoặc việc tiếp theo của nhóm.

## 1. Cách sử dụng 01–04

01–04 cùng tạo thành bộ gốc của dự án. 03 là cơ sở tôn chỉ trước khi tạo [04](04-ton-chi-du-an-day-du.md) theo mẫu bảy mục của giảng viên. Người làm các chương sau phải đối chiếu cả bộ; không bỏ qua điểm khác nhau giữa các bản.

Ngày 05/10/2026, Hưng đồng ý phương án sửa hồi quy và giao cập nhật 01–04/chương 2, tạo PR, ad-review bằng Luna MAX và Gemini Flash HIGH; Hưng sẽ tự merge. Các quyết định/giả định dùng trong bản cập nhật:

| Điểm | Cách xử lý |
| --- | --- |
| PM và đơn vị thực hiện | Bùi Hồng Phú / công ty Raumania theo 04; 03 và chương 2 đã đồng bộ. Phân công sinh viên giữ riêng ở N-03. |
| O01 · Cân/PC | Theo 02: kho tổng 2 cân, 2 PC; mỗi chi nhánh 1 cân, 1 PC; tổng 4 cân/4 PC. Các bảng/WBS/đầu ra được đối chiếu cùng cấu hình. |
| O02 · Máy chấm công | Giả định doanh nghiệp cung cấp 1 máy/kho (3 máy), kiểm giao thức khi khảo sát; không mua thêm trong 130 triệu. Đây là giả định, chưa xác nhận hiện trường. |
| Nguồn số đo | Thiết bị môi trường và khâu kiểm độ ẩm trà của doanh nghiệp, nhập thủ công. Kết nối đo không dây chỉ là tùy chọn phải thẩm định/phê duyệt; không thêm nghiệp vụ kho ngoài tài liệu gốc. |
| Server/vận hành | Gói 25 triệu dùng trong 8 tháng dự án; Tech Lead/Backend triển khai/sao lưu/hướng dẫn, Onsite kết nối và đào tạo. Doanh nghiệp nhận quản trị và phí sau bàn giao; bảo trì dài hạn là thỏa thuận riêng. |
| Lịch huy động | Khảo sát tháng 1 BA/Tech Lead; RS232 từ tháng 2, Onsite từ tháng 5. BA bàn giao tài liệu cuối tháng 5; người còn tham gia cập nhật/đóng gói. QA/Tech Lead tổng hợp nghiệm thu tháng 8 từ biên lai trước vận hành. |
| Nghiệm thu | AC-01/AC-02 chương 2 xác định ý nghĩa ngưỡng, cỡ mẫu, nhóm lỗi và điều kiện đạt; các tham số nghiệp vụ chốt trong SRS, Test Plan hoàn thiện ở chương 9. Không chỉ điền hai con số vào chỗ trống. |

Không kế thừa dấu PASS cũ cho bản mới. PR và lượt review sau sửa là căn cứ đánh giá phiên bản hiện hành; kiểm tài liệu không chứng minh thiết bị/QA thực tế đã chạy. Nếu một giả định tài sản không đạt, cần đánh giá công/chi phí và xử lý thay đổi trước triển khai.

## 2. Bối cảnh tạo bản 04 ngày 07/09/2026

- Theo chỉ dẫn trực tiếp trong phiên đó, giữ 03 làm cơ sở và tạo 04 theo bảy mục của mẫu giảng viên. Ba ảnh viết tay đã nộp được dùng làm căn cứ ưu tiên khi tạo bản này.
- Bản 04 dùng PM Bùi Hồng Phú; đơn vị thực hiện là Công ty Cổ phần Công nghệ Raumania, đại diện Nguyễn Đức Công. Chủ đầu tư có đại diện giả định Trần Minh Đức. Đây là vai trò của tình huống, không phải phân công sinh viên làm BTL.
- Ngày bắt đầu dự án giả định là 03/06/2027; tháng dự án từ ngày 03 đến hết ngày 02 tháng sau. Kho tổng hoạt động chậm nhất 02/12/2027; toàn dự án kết thúc 02/02/2028. Đây không phải deadline làm BTL; các mốc này chưa xác định lịch ngày làm việc hoặc đường găng.
- Giữ ngân sách hai tỷ, ba kho và ngưỡng cân `<0,1%`, in tem `<2 giây/sản phẩm>` theo bản đã nộp lúc đó. 04 ghi cách đo được thống nhất trong kế hoạch kiểm thử. Nếu điều chỉnh tiêu chí, cần sửa thống nhất bộ gốc và các phần liên quan.
- 04 không khóa số lượng/hãng thiết bị, kiến trúc ngoại tuyến, lịch nhân sự hoặc cách phân bổ dự phòng. Những điểm này cần có căn cứ khi chi tiết hóa.
- Tên tổ chức, bên liên quan và thông tin liên hệ trong tình huống có yếu tố giả định; ghi chú cũ không chứng minh chúng là dữ liệu doanh nghiệp thực tế. Không dùng thông tin tự đặt để liên hệ.

## 3. Biên lai kiểm tra cũ và giới hạn

Hai subagent đã đọc độc lập bản 04 ngày 07/09/2026, SHA256 `8005958D46B3308C3D5B13288A7E2117363AF24F61427F312FBC3DFFB4774241`. Một góp ý P2 về FEFO đã được sửa: ưu tiên lô **còn hạn** có ngày hết hạn gần nhất. Lượt kiểm lại delta ghi PASS; SHA256 bản cuối khi đó là `05C3293D4D67AA591691BC0F00B773933C8DDA39EF9696859798FAE316567669`.

Biên lai này chỉ áp dụng cho các phiên bản đó, không chứng minh bản 04 hiện tại hoặc toàn bộ BTL đã đạt. Đã kiểm Markdown; chưa kiểm bản in Word/PDF, thiết bị hoặc phần mềm thực tế, chưa có xác nhận chấp nhận bài của giảng viên.

Việc commit/push ngày 07/09/2026 được giao trong phiên đó; không tạo quyền duyệt hoặc tích hợp thường trực cho Hưng. Cơ chế làm việc và phân công hiện hành nằm ở [N-02](N-02-cach-lam-viec.md) và [N-03](N-03-phan-cong-va-quyet-dinh.md).
