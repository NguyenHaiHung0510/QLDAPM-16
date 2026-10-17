# Sử dụng lịch trong ProjectLibre Desktop

Đầu vào dùng chung là `du-lieu-lich.json`; các bảng, `gantt.svg` và `lich-wms.xml` được tạo bằng `lap-lich.py`. Tệp `lich-wms.pod` là bản lịch chỉnh trong ProjectLibre. Xem [README](README.md) để biết vai trò từng tệp và [chương 3](../CHUONG-3-QUAN-LY-THOI-GIAN.md) để đọc căn cứ của phương án.

## 1. Mở lịch

Hồ sơ dùng [ProjectLibre Desktop](https://projectlibre.com/projectlibre-desktop/) miễn phí, phiên bản 1.9.8. Cần Java có lệnh `javaw.exe` và tệp `projectlibre.jar` trong bộ công cụ. Từ thư mục gốc repo, chạy PowerShell với đường dẫn bộ công cụ trên máy:

```powershell
.\chuong-3\mo-projectlibre.ps1 -ProjectLibreJar 'D:\Cong-cu\projectlibre-1.9.8\projectlibre.jar'
```

Thay đường dẫn ví dụ bằng đường dẫn thật. Script mở `lich-wms.pod` trong một tiến trình Java dùng `-Duser.timezone=UTC`.

**Chế độ UTC cần cho lịch này trên bản 1.9.8.** Khi mở ở UTC+7, ứng dụng có thể dịch ngày ngoại lệ và cho mốc sớm hơn lịch đã tính. UTC chỉ áp dụng cho tiến trình Java; Windows giữ nguyên múi giờ. Khi dùng bản khác, đối chiếu ngày nghỉ và sáu mốc trước khi chỉnh lịch.

## 2. Đọc và chỉnh lịch

- **Gantt:** ngày bắt đầu/kết thúc, mốc và quan hệ phụ thuộc.
- **Network:** mạng hoạt động và các nhánh trước–sau.
- **Resource Sheet / Resource Usage:** tám vai trò, tỷ lệ phân công và tải theo thời gian.
- **Task Information:** thời lượng, quan hệ, ràng buộc và Notes. Mã A/G/R/M/L ở tên hoạt động; mã WBS gốc nằm trong Notes vì một hoạt động có thể phục vụ nhiều gói.

Lịch có 64 hoạt động/mốc và sáu dòng quản lý xuyên kỳ (LoE — Level of Effort). L01–L06 kết thúc cùng M6 trong phương án hiện tại. Khi M6 đổi ngày, cập nhật thời lượng/kết thúc LoE và kiểm lại tải: các dòng này có thời lượng cố định, được quản lý riêng với chuỗi bàn giao sản phẩm.

### Các thuộc tính cần giữ khi chỉnh

| Thuộc tính | Cách dùng trong hồ sơ |
| --- | --- |
| Fixed Duration — thời lượng cố định | Giữ thời lượng đã ước lượng; tỷ lệ hỗ trợ được phân công riêng |
| Effort Driven — tính theo nỗ lực | ProjectLibre 1.9.8 có thể bật lại cờ này khi nhập XML. Kiểm Task Information → Advanced trước khi đổi phân công, rồi tính lại thời lượng/nỗ lực |
| As Soon As Possible (ASAP) — sớm nhất có thể | Dùng cho công việc theo quan hệ để lịch dịch khi đầu vào thay đổi |
| Start No Earlier Than (SNET) — bắt đầu từ ngày sàn | Dùng ở đầu kỳ huy động, ngày nhận hàng hoặc đợt triển khai đã ghi trong dữ liệu |
| Finish-to-Start (FS), Start-to-Start (SS) | FS là việc trước kết thúc rồi việc sau bắt đầu; A10→A11 dùng SS + một ngày làm việc |

Sau khi đổi thời lượng hoặc phân công, kiểm ngày mốc và tải từng vai trò trong kỳ huy động. Ngày Start/Finish trao đổi trong XML là kết quả của phương án; ứng dụng tính lại theo quan hệ, ràng buộc và lịch làm việc.

## 3. Thử tác động của một thay đổi

1. Dùng **bản sao** của lịch. Mở Task Information của **A11 — phát triển core kho**.
2. Tăng Duration từ **12 lên 15 ngày làm việc**, giữ quan hệ và các khối dự phòng.
3. Tính lại: M2 từ 30/09 sang **05/10/2027**, vượt hạn 02/10; M3 sang **28/10**. M4–M6 giữ ngày do ngày sàn và khoảng trống giữa các giai đoạn.
4. Xem các phương án phản ứng có điều kiện ở §3.4.5 của chương 3. Giữ phép thử ở bản sao; mở lại lịch gốc sau khi hoàn thành.

## 4. Đồng bộ với hồ sơ chung

Khi chọn một thay đổi để dùng chung, cập nhật thời lượng, quan hệ, ngày sàn hoặc tỷ lệ nguồn lực vào JSON rồi chạy `python -B chuong-3/lap-lich.py`. Nhập `lich-wms.xml` mới bằng phiên ProjectLibre UTC, đối chiếu sáu mốc và tải nguồn lực, lưu `.pod` tương ứng rồi cập nhật chương 3.

JSON và XML sinh từ chương trình là nguồn tái lập của phương án. XML do ProjectLibre 1.9.8 xuất có thể chứa `CalendarUID` của nguồn lực thiếu lịch tham chiếu; dùng bản xuất đó để đối chiếu, giữ XML sinh từ JSON làm tệp trao đổi chung.

Trong `ket-qua-lich.json`, `phase_cpm` dùng ngày hoàn thành sớm nhất của từng mốc. `logical.total_float` dùng mạng có hạn mốc trung gian và ngày hoàn thành sớm nhất toàn dự án. Khoảng dư đến hạn gốc được trình riêng trong chương 3.

## 5. Đường cơ sở và theo dõi thực tế

Tệp hiện là lịch đề xuất. Khi phương án được phê duyệt, lưu phiên bản và quyết định rồi dùng **Save Baseline** để theo dõi chênh lệch. Cập nhật ngày thực tế/thời lượng còn lại theo §3.5 của chương 3.

ProjectLibre có các chức năng chi phí và Earned Value Management (EVM) — quản lý giá trị thu được. Hồ sơ hiện chứa lịch và phân công; sử dụng EVM cần đường cơ sở chi phí, quy tắc đo và dữ liệu thực tế theo chương 4.

Tài liệu thao tác của nhà phát triển: [Overview](https://projectlibre.com/projectlibre-documentation/overview/).
