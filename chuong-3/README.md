# Hồ sơ tiến độ WMS Tân Cương

Thư mục này kèm [chương 3 — Quản lý thời gian](../CHUONG-3-QUAN-LY-THOI-GIAN.md) của bài tập lớn Nhóm 16. Hồ sơ lập lịch cho kho tổng và hai chi nhánh trong **03/06/2027–02/02/2028**, dựa trên WBS chương 2 và nhân sự ở tài liệu 02. Lịch hiện là phương án đề xuất, dùng các giả định nêu tại §3.1.2 của chương.

Để đọc nhanh, xem chương 3 và [Gantt](gantt.svg). Để xem từng hoạt động, mở [bảng đầy đủ](bang-hoat-dong.md). Để chỉnh trong ProjectLibre, làm theo [hướng dẫn công cụ](HUONG-DAN.md); bản 1.9.8 cần mở bằng chế độ UTC để giữ đúng ngày nghỉ.

## Các tệp dùng để làm gì?

| Tệp | Vai trò |
| --- | --- |
| [du-lieu-lich.json](du-lieu-lich.json) | Đầu vào dùng chung: hoạt động, ba điểm, quan hệ, lịch làm việc và phân công |
| [lap-lich.py](lap-lich.py) | Tính lịch và tải nguồn lực từ JSON bằng Python 3, chỉ dùng thư viện chuẩn |
| [bang-hoat-dong.md](bang-hoat-dong.md), [CSV](bang-hoat-dong.csv) | Kết quả chi tiết theo hoạt động: WBS, thời lượng, ngày, quan hệ và phân công |
| [truy-vet-wbs.md](truy-vet-wbs.md) | Tra 45 gói WBS tới hoạt động lịch tương ứng |
| [ket-qua-lich.json](ket-qua-lich.json), [tai-nguon-luc.csv](tai-nguon-luc.csv) | Kết quả mạng, ngày mốc và tải từng vai trò theo ngày |
| [gantt.svg](gantt.svg) | Hình lịch tạo từ kết quả tính, xem trực tiếp trong repo |
| [lich-wms.xml](lich-wms.xml) | Lịch trao đổi tạo từ JSON để nhập vào ProjectLibre |
| [lich-wms.pod](lich-wms.pod) | Bản lịch mở và chỉnh bằng ProjectLibre Desktop |
| [mo-projectlibre.ps1](mo-projectlibre.ps1), [HUONG-DAN.md](HUONG-DAN.md) | Cách mở lịch trên Windows, chỉnh thử và đồng bộ các tệp |

## Khi thay đổi lịch

1. Chỉnh đầu vào trong `du-lieu-lich.json`; giữ truy vết WBS và các kỳ huy động theo tài liệu 02.
2. Từ thư mục gốc repo, chạy:

   ```powershell
   python -B chuong-3/lap-lich.py
   ```

3. Xem lại ngày của sáu mốc, tải từng người và các giả định đã thay đổi. Nhập XML mới vào ProjectLibre theo hướng dẫn, lưu bản `.pod` tương ứng và cập nhật bảng tóm tắt trong chương 3. Chương trình tạo lại các bảng/JSON/CSV/SVG/XML; `.pod` được lưu bằng ProjectLibre.

Nếu chỉnh thử trực tiếp trong ProjectLibre, dùng bản sao; thay đổi được chọn cho hồ sơ chung cần cập nhật lại vào JSON và tính lại. Nhóm thống nhất phiên bản lịch trước khi dùng số liệu giữa các chương.

Hai mốc cần theo dõi sát trong phương án hiện tại: **M2 dư một ngày làm việc; M5 dư 0 ngày** tới hạn gốc, sau các khối dự phòng đã lập lịch.
