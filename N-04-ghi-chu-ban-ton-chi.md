# Ghi chú bản tôn chỉ đầy đủ — 07/09/2026

Ghi chú làm việc, không ghép vào bài nộp.

- Theo chỉ dẫn trực tiếp của người quản lý tài liệu trong phiên ngày 07/09/2026: giữ 03 làm cơ sở, tạo [04-ton-chi-du-an-day-du.md](04-ton-chi-du-an-day-du.md) theo 7 mục của mẫu giảng viên. Ba ảnh viết tay đã nộp là căn cứ ưu tiên; tài liệu dự án có thể điều chỉnh khi cần, tránh chốt chi tiết quá sớm.
- Bản 04 dùng PM Bùi Hồng Phú; công ty thực hiện là Công ty Cổ phần Công nghệ Raumania, đại diện Nguyễn Đức Công. Chủ đầu tư có đại diện giả định Trần Minh Đức để tách hai bên; người quản lý tài liệu đã giao quyền lựa chọn này. Vai trò trong tình huống dự án không thay đổi phân công làm bài thực tế của nhóm.
- Ngày bắt đầu 03/06/2027; quy ước tháng dự án từ ngày 03 đến hết ngày 02 tháng sau. Hoàn thành kho tổng chậm nhất 02/12/2027; toàn dự án hết 02/02/2028. Đã kiểm phép cộng tháng bằng DateTime.AddMonths; không suy ra lịch ngày làm việc hoặc đường găng từ các mốc này.
- Giữ 2 tỷ đồng, ba kho, các chức năng và ngưỡng sai số cân < 0,1%, in tem < 2 giây/sản phẩm theo bản đã nộp. Diễn đạt yêu cầu RS232 theo khả năng đáp ứng thao tác nghiệp vụ; không hứa độ trễ bằng không.
- Bản 04 không khóa số lượng thiết bị, hãng thiết bị, kiến trúc ngoại tuyến, lịch nhân sự hoặc phân bổ dự phòng. Các điểm lệch số lượng trong 02/03 và nguồn máy chấm công vẫn cần giải quyết khi lập kế hoạch chi tiết; không tự coi đã đóng các vấn đề O01/O02 trong N-03.
- Thông tin liên hệ được điền theo yêu cầu bài tập; số điện thoại tự đặt có thể trùng số thật, không dùng để liên hệ. Email dùng miền .example. Địa chỉ số 128 là giả định; tên đường/phường tham khảo [cổng thông tin phường Hà Đông](https://hadong.hanoi.gov.vn/van-hoa-xa-hoi/thong-bao-dieu-chinh-to-chuc-giao-thong-duong-tran-phu-duong-phung-hung-phuong-ha-dong-2809250907095757588.htm). Không xác nhận trụ sở doanh nghiệp thực tế.

## Kiểm tra tài liệu

- Hai subagent T3 đọc độc lập bản 04 có SHA256 `8005958D46B3308C3D5B13288A7E2117363AF24F61427F312FBC3DFFB4774241`: một lượt kiểm tính đúng đắn/ảnh nguồn; một lượt kiểm logic, ngày tháng, annotation và mức độ chi tiết.
- T3 logic: PASS. T3 tính đúng đắn: một P2 về câu FEFO có thể bị hiểu là xuất hàng đã hết hạn. Đã sửa thành ưu tiên lô còn hạn sử dụng có ngày hết hạn gần nhất; không đổi yêu cầu.
- T3 đã kiểm lại đúng delta và đóng P2: PASS. SHA256 bản 04 cuối: `05C3293D4D67AA591691BC0F00B773933C8DDA39EF9696859798FAE316567669`.
- Đã kiểm đủ 7 mục; lịch tháng khớp; 01/02/03 không có diff so với HEAD. Các sửa đổi sẵn có của người dùng ở N-01/N-02 được giữ nguyên.
- Chỉ kiểm tài liệu Markdown; chưa xuất Word/PDF, chưa kiểm bố cục bản in, chưa có xác nhận của nhóm hoặc giảng viên. Không có kiểm thử phần mềm hay thiết bị thực tế trong công việc này.

## Lưu lên GitHub

Người quản lý tài liệu yêu cầu push kết quả cùng các file vừa copy: 7 PDF trong tai-lieu và các chỉnh sửa đang có ở N-01/N-02. Kết quả commit/push được ghi bằng mã commit trong phản hồi kết thúc phiên; không gửi thông báo cho người khác.
