**Bài tập tại lớp**

**Mô tả sơ bộ dự án phần mềm: Phần mềm quản lý kho trà Tân Cương**

Doanh nghiệp Trà Tân Cương sở hữu 3 cơ sở kho (01 kho tổng chế biến/đóng gói và 02 kho chi nhánh phân phối), đơn vị đặt hàng triển khai một phần mềm quản lý thống nhất hoạt động kho và điều phối chuỗi cung ứng.

Yêu cầu: Hoàn thành việc bàn giao toàn bộ phần mềm trong thời gian 8 tháng, trong đó phần mềm sẽ được đưa vào vận hành thực tế tại 01 kho tổng trong thời gian muộn nhất là 6 tháng.

---

Các chức năng mà phía quản lý kho yêu cầu phải có:

* **Quản lý quy trình nhập - xuất kho:** tiếp nhận trà nguyên liệu/thành phẩm, kiểm tra chỉ số chất lượng (độ ẩm, cảm quan), lập phiếu nhập/xuất kho, tự động sinh mã lô (Batch ID), kiểm soát xuất kho ưu tiên hàng cận date theo thuật toán FEFO (First Expired, First Out),...


* **Quản lý thông tin trà và định mức (BOM):** mã trà, tên trà, dòng trà (trà xanh, Oolong, Phổ Nhĩ,...), nguồn gốc, ngày sản xuất, hạn sử dụng, quy cách đóng gói, định mức chuyển đổi vật tư (trà thô kg $\rightarrow$ túi/hộp thành phẩm),...


* **Quản lý tồn kho và bảo quản:** theo dõi tồn kho chi tiết theo vị trí (zone, kệ, máng), ghi nhận nhật ký nhiệt độ/độ ẩm môi trường lưu kho, cảnh báo trà cận date/hết hạn, cảnh báo dưới ngưỡng tồn kho tối thiểu,...


* **Quản lý nhà cung cấp và đơn hàng xuất:** thông tin nông trường/nhà cung cấp, lịch sử nhập hàng, tiếp nhận đơn hàng xuất cho chi nhánh/đại lý, theo dõi trạng thái vận chuyển,...


* **Quản lý nhân sự:** lịch làm việc theo ca, phân quyền truy cập hệ thống theo vai trò, chấm công nhân viên kho,...


* **Quản lý tài chính:** tiền nhập nguyên liệu, giá thành đóng gói theo lô, doanh thu xuất kho, quản lý công nợ, chi phí vận hành kho,...


* **Quản lý cơ sở vật chất, dụng cụ, vật tư kho:** danh mục kệ, khu vực lưu trữ, máy móc đóng gói/chế biến nhỏ, bao bì, tem nhãn,...


* **Báo cáo thống kê:** nhập – xuất – tồn, báo cáo tuổi hàng (Aging report), báo cáo tỷ lệ hao hụt nguyên liệu trong chế biến, thống kê sản phẩm bán chạy/tồn lâu,...



Phần mềm được triển khai dưới dạng website chạy trên hệ điều hành Windows, có khả năng kết nối trực tiếp với các thiết bị ngoại vi như đầu đọc mã vạch/QR code, máy in tem mã lô/hóa đơn, cân điện tử kết nối chuẩn RS232, máy chấm công,...

Tất cả các bộ phận, nhân viên có liên quan thuộc các chi nhánh kho đều tham gia sử dụng phần mềm theo vai trò và quyền hạn được phân công.