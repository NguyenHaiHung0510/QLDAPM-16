# Bảng hoạt động và lịch đề xuất

Ngày dùng là ngày làm việc. MO/ML/MP là ba điểm ước lượng; ô trống dùng căn cứ trực tiếp. ES/EF/LS/LF/TF là chỉ số ngày của mạng logic có release và hạn mốc, **chưa xét cạnh tranh nguồn lực**; cột ngày bắt đầu/kết thúc là lịch sau phân bổ nguồn lực. Biên thời gian là khoảng [ES, EF), ngày đầu dự án có chỉ số 0. TF toàn mạng không thay biên dự phòng riêng của từng mốc.

| Mã | WBS | Hoạt động | MO | ML | MP | PERT | Ngày dùng | Tiền nhiệm | Nguồn lực | Bắt đầu | Kết thúc | ES | EF | LS | LF | TF | Dịch do nguồn lực |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 1.1.1.1, 1.1.1.2, 1.1.1.3 | Lập PMP, kế hoạch phạm vi/WBS và lịch/ngân sách đề xuất | 3 | 4 | 9 | 4.67 | 5 | — | PM 60%; TL 10% | 2027-06-03 | 2027-06-09 | 0 | 5 | 15 | 20 | 15 | 0 |
| A02 | 1.2.1.1, 1.2.1.2 | Khảo sát luồng kho tổng và danh mục/giao thức tài sản ba kho | 3 | 4 | 9 | 4.67 | 5 | — | BA 70%; TL 20%; PM 10% | 2027-06-03 | 2027-06-09 | 0 | 5 | 4 | 9 | 4 | 0 |
| A03 | 1.2.1.3 | Khảo sát Excel, BOM và dữ liệu mở kho | 1 | 2 | 7 | 2.67 | 3 | A02 FS | BA 70%; TL 10% | 2027-06-10 | 2027-06-14 | 5 | 8 | 9 | 12 | 4 | 0 |
| A04 | 1.2.2.2 | Chốt giao thức, dải cân, tem và yêu cầu phi chức năng | 1 | 2 | 7 | 2.67 | 3 | A02 FS | TL 70%; BA 20% | 2027-06-10 | 2027-06-14 | 5 | 8 | 9 | 12 | 4 | 0 |
| A05 | 1.2.2.1 | Lập SRS/use case và ma trận yêu cầu cho sáu nhóm người dùng | 3 | 4 | 9 | 4.67 | 5 | A03 FS, A04 FS | BA 70%; TL 10% | 2027-06-15 | 2027-06-21 | 8 | 13 | 12 | 17 | 4 | 0 |
| A06 | 1.2.3.1 | Thiết kế kiến trúc và kế hoạch môi trường dev/test | 2 | 3 | 8 | 3.67 | 4 | A04 FS | TL 70%; BA 10% | 2027-06-15 | 2027-06-18 | 8 | 12 | 12 | 16 | 4 | 0 |
| A07 | 1.2.3.2 | Thiết kế dữ liệu, điều chuyển và đệm ngoại tuyến | 2 | 3 | 8 | 3.67 | 4 | A06 FS | TL 70%; BA 10% | 2027-06-21 | 2027-06-24 | 12 | 16 | 16 | 20 | 4 | 0 |
| A08 | 1.2.3.3 | Thiết kế giao diện các luồng theo vai trò | 1 | 2 | 7 | 2.67 | 3 | A05 FS | BA 70%; TL 10% | 2027-06-22 | 2027-06-24 | 13 | 16 | 17 | 20 | 4 | 0 |
| A09 | 1.2.2.1, 1.2.3.1, 1.1.1.3 | Thẩm định và xác nhận SRS/SAD, RTM và lịch đề xuất |  |  |  |  | 2 | A01 FS, A05 FS, A07 FS, A08 FS | PM 30%; TL 20%; BA 20% | 2027-06-25 | 2027-06-28 | 16 | 18 | 20 | 22 | 4 | 0 |
| M1 | 1.2.2.1, 1.2.3.1 | M1 – SRS/SAD được xác nhận |  |  |  |  | 0 | A09 FS | — | 2027-06-28 | 2027-06-28 | 18 | 18 | 22 | 22 | 4 | 0 |
| A10 | 1.2.3.1 | Dựng môi trường dev/test và bàn giao thiết kế cho Dev | 1 | 2 | 7 | 2.67 | 3 | M1 FS | TL 60%; BE 20%; FE 20% | 2027-07-05 | 2027-07-07 | 22 | 25 | 23 | 26 | 1 | 0 |
| G1 | 1.3.3.1, 1.3.3.2, 1.3.3.3 | Tiếp nhận bộ mẫu kho tổng: 1 cân, 1 máy in, 1 scanner, 1 PC |  |  |  |  | 1 | M1 FS | PM 10%; HW 20% | 2027-07-05 | 2027-07-05 | 22 | 23 | 52 | 53 | 30 | 0 |
| A24 | 1.3.5.1, 1.3.5.2 | Lập Test Plan và dữ liệu đối soát RTM/AC | 3 | 4 | 9 | 4.67 | 5 | M1 FS | QA 80%; BA 10%; TL 10% | 2027-08-03 | 2027-08-09 | 43 | 48 | 59 | 64 | 16 | 0 |
| A11 | 1.3.1.1 | Phát triển danh mục/lô, nhập–xuất–tồn, điều chuyển, Zone/Bin/Rack | 10 | 11 | 16 | 11.67 | 12 | A10 SS+1d | BE 80%; FE 80%; TL 10%; BA 5% | 2027-07-06 | 2027-07-21 | 23 | 35 | 24 | 36 | 1 | 0 |
| A21 | 1.3.3.1 | Phát triển service cân RS232 và xử lý mất kết nối | 7 | 8 | 13 | 8.67 | 9 | A10 FS, G1 FS | HW 80%; TL 10% | 2027-07-08 | 2027-07-20 | 25 | 34 | 53 | 62 | 28 | 0 |
| A12 | 1.3.1.2 | Phát triển FEFO và chặn lô hết hạn | 2 | 3 | 8 | 3.67 | 4 | A11 FS | BE 80%; FE 80%; TL 10%; BA 5% | 2027-07-22 | 2027-07-27 | 35 | 39 | 36 | 40 | 1 | 0 |
| A22 | 1.3.3.2 | Phát triển QR và điều khiển in tem theo giao thức phù hợp | 5 | 6 | 11 | 6.67 | 7 | A21 FS | HW 80%; TL 10% | 2027-07-21 | 2027-07-29 | 34 | 41 | 62 | 69 | 28 | 0 |
| A25 | 1.3.5.1 | Kiểm luồng cân tới web và phục hồi trên bộ mẫu | 3 | 4 | 9 | 4.67 | 5 | A21 FS, A11 FS, A24 FS | QA 80%; HW 20%; BE 10% | 2027-08-10 | 2027-08-16 | 48 | 53 | 64 | 69 | 16 | 0 |
| A13 | 1.3.2.1 | Phát triển BOM, độ ẩm và hao hụt | 4 | 5 | 10 | 5.67 | 6 | A12 FS | BE 80%; FE 80%; TL 10%; BA 5% | 2027-07-28 | 2027-08-04 | 39 | 45 | 40 | 46 | 1 | 0 |
| A23 | 1.3.3.3 | Tích hợp scanner và ba máy chấm công sẵn có | 4 | 5 | 10 | 5.67 | 6 | A22 FS | HW 80%; BE 10%; TL 10% | 2027-07-30 | 2027-08-06 | 41 | 47 | 69 | 75 | 28 | 0 |
| A14 | 1.3.2.2 | Phát triển cảnh báo và tuổi hàng | 2 | 3 | 8 | 3.67 | 4 | A13 FS | BE 80%; FE 80%; TL 10%; BA 5% | 2027-08-05 | 2027-08-10 | 45 | 49 | 46 | 50 | 1 | 0 |
| A26 | 1.3.5.2 | Kiểm tem, FEFO/BOM và đối soát các module đã sẵn sàng | 4 | 5 | 10 | 5.67 | 6 | A22 FS, A13 FS, A25 FS | QA 80%; HW 20%; BE 10%; FE 10% | 2027-08-17 | 2027-08-24 | 53 | 59 | 69 | 75 | 16 | 0 |
| A15 | 1.3.2.3 | Phát triển nhật ký môi trường nhập thủ công | 1 | 2 | 7 | 2.67 | 3 | A14 FS | BE 80%; FE 80%; TL 10%; BA 5% | 2027-08-11 | 2027-08-13 | 49 | 52 | 50 | 53 | 1 | 0 |
| A16 | 1.3.3.4 | Phát triển import/export danh mục, lô và tồn đầu kỳ | 2 | 3 | 8 | 3.67 | 4 | A15 FS | BE 80%; FE 80%; TL 10%; BA 5% | 2027-08-16 | 2027-08-19 | 52 | 56 | 53 | 57 | 1 | 0 |
| A17 | 1.3.4.2 | Phát triển nhà cung cấp, công nợ, đơn hàng và vận chuyển | 5 | 6 | 11 | 6.67 | 7 | A16 FS | BE 80%; FE 80%; TL 10%; BA 5% | 2027-08-20 | 2027-08-30 | 56 | 63 | 57 | 64 | 1 | 0 |
| A18 | 1.3.4.3 | Phát triển lịch ca và phân quyền sáu vai trò | 2 | 3 | 8 | 3.67 | 4 | A17 FS | BE 80%; FE 80%; TL 10%; BA 5% | 2027-08-31 | 2027-09-07 | 63 | 67 | 64 | 68 | 1 | 0 |
| A19 | 1.3.4.4 | Phát triển danh mục tài sản, dụng cụ và vật tư | 1 | 2 | 7 | 2.67 | 3 | A18 FS | BE 80%; FE 80%; TL 10%; BA 5% | 2027-09-08 | 2027-09-10 | 67 | 70 | 68 | 71 | 1 | 0 |
| A20 | 1.3.4.1 | Phát triển dashboard và toàn bộ báo cáo RTM | 2 | 3 | 8 | 3.67 | 4 | A19 FS | BE 80%; FE 80%; TL 10%; BA 5% | 2027-09-13 | 2027-09-16 | 70 | 74 | 71 | 75 | 1 | 0 |
| A27 | 1.3.5.2 | Kiểm tích hợp đầy đủ 20 dòng RTM, quyền, offline và điều chuyển | 4 | 5 | 10 | 5.67 | 6 | A20 FS, A23 FS, A26 FS | QA 80%; BE 10%; FE 10%; TL 10% | 2027-09-17 | 2027-09-24 | 74 | 80 | 75 | 81 | 1 | 0 |
| R2 | 1.3.5.1, 1.3.5.2 | Dự phòng xử lý/kiểm lại lỗi tích hợp trước M2 |  |  |  |  | 4 | A27 FS | BE 50%; FE 50%; HW 30%; QA 80%; TL 10% | 2027-09-27 | 2027-09-30 | 80 | 84 | 81 | 85 | 1 | 0 |
| M2 | 1.3.5.1, 1.3.5.2 | M2 – Chức năng và bộ mẫu đạt kiểm tích hợp |  |  |  |  | 0 | R2 FS | — | 2027-09-30 | 2027-09-30 | 84 | 84 | 85 | 85 | 1 | 0 |
| G2 | 1.4.1.1, 1.4.1.3, 1.4.1.2 | Nhận phần thiết bị còn lại kho tổng, xác nhận điện/LAN/Excel/người học |  |  |  |  | 1 | M2 FS | PM 20%; OS 20%; HW 20% | 2027-10-04 | 2027-10-04 | 85 | 86 | 90 | 91 | 5 | 0 |
| A30 | 1.4.1.2 | Hoàn thiện kịch bản UAT và SOP/User Manual sáu vai trò | 3 | 4 | 9 | 4.67 | 5 | M2 FS | BA 70%; QA 20%; OS 10% | 2027-10-04 | 2027-10-08 | 85 | 90 | 93 | 98 | 8 | 0 |
| A28 | 1.4.1.1 | Lắp đặt kho tổng và cấu hình toàn bộ đầu cuối/ngoại vi | 2 | 3 | 8 | 3.67 | 4 | G2 FS | OS 80%; HW 60%; TL 10% | 2027-10-05 | 2027-10-08 | 86 | 90 | 91 | 95 | 5 | 0 |
| A29 | 1.4.1.3 | Import và đối soát dữ liệu kho tổng trong môi trường chạy thử | 1 | 2 | 7 | 2.67 | 3 | A28 FS, A16 FS | OS 40%; BA 60%; BE 30% | 2027-10-11 | 2027-10-13 | 90 | 93 | 95 | 98 | 5 | 0 |
| A31 | 1.4.1.2, 1.3.5.1, 1.3.5.2 | UAT kho tổng, đo từng cân/in tem và kiểm toàn bộ luồng | 2 | 3 | 8 | 3.67 | 4 | A29 FS, A30 FS | QA 80%; BA 20%; OS 40%; HW 20%; BE 10%; FE 10% | 2027-10-14 | 2027-10-19 | 93 | 97 | 98 | 102 | 5 | 0 |
| R3 | 1.4.1.2 | Dự phòng sửa và kiểm lại phát hiện UAT kho tổng |  |  |  |  | 2 | A31 FS | QA 80%; BE 50%; FE 50%; HW 20%; OS 30% | 2027-10-20 | 2027-10-21 | 97 | 99 | 102 | 104 | 5 | 0 |
| A32 | 1.4.1.2 | Đào tạo thực hành kho tổng và BA bàn giao hướng dẫn cho PM/Onsite |  |  |  |  | 3 | R3 FS | OS 70%; BA 30%; PM 10% | 2027-10-22 | 2027-10-26 | 99 | 102 | 104 | 107 | 5 | 0 |
| M3 | 1.4.1.1, 1.4.1.2, 1.4.1.3 | M3 – Kho tổng chạy thử/UAT/đào tạo đạt, BA đã bàn giao |  |  |  |  | 0 | A32 FS | — | 2027-10-26 | 2027-10-26 | 102 | 102 | 107 | 107 | 5 | 0 |
| A33 | 1.4.2.1 | Cấu hình production, chuyển dữ liệu và thử backup/restore | 1 | 2 | 7 | 2.67 | 3 | M3 FS | TL 50%; BE 70%; OS 20% | 2027-11-03 | 2027-11-05 | 107 | 110 | 110 | 113 | 3 | 0 |
| A34 | 1.4.2.1, 1.4.2.2 | Kiểm điều kiện go-live và delta cấu hình/dữ liệu production |  |  |  |  | 2 | A33 FS | QA 60%; TL 20%; OS 30%; PM 20% | 2027-11-08 | 2027-11-09 | 110 | 112 | 113 | 115 | 3 | 0 |
| A35 | 1.4.2.2 | Kích hoạt vận hành chính thức kho tổng |  |  |  |  | 1 | A34 FS | PM 20%; OS 50%; BE 20%; HW 20% | 2027-11-10 | 2027-11-10 | 112 | 113 | 115 | 116 | 3 | 0 |
| M4 | 1.4.2.2 | M4 – Kho tổng vận hành chính thức |  |  |  |  | 0 | A35 FS | — | 2027-11-10 | 2027-11-10 | 113 | 113 | 116 | 116 | 3 | 0 |
| A36 | 1.4.2.3 | Hỗ trợ onsite trong hai tuần đầu vận hành kho tổng |  |  |  |  | 10 | M4 FS | OS 80%; HW 30%; BE 10% | 2027-11-11 | 2027-11-24 | 113 | 123 | 116 | 126 | 3 | 0 |
| G3 | 1.5.1.1 | Nhận và tiền cấu hình thiết bị hai chi nhánh, chốt tuyến công tác |  |  |  |  | 3 | A36 FS | OS 30%; HW 60%; PM 10% | 2027-11-25 | 2027-11-29 | 123 | 126 | 126 | 129 | 3 | 0 |
| A37 | 1.5.1.1 | Di chuyển và lắp thiết bị tại chi nhánh 1 |  |  |  |  | 3 | G3 FS | OS 80%; HW 30% | 2027-12-03 | 2027-12-07 | 129 | 132 | 129 | 132 | 0 | 0 |
| A38 | 1.5.2.1 | Cấu hình đồng bộ/ngoại tuyến và dữ liệu chi nhánh 1 |  |  |  |  | 2 | A37 FS | TL 30%; BE 50%; FE 20%; OS 30% | 2027-12-08 | 2027-12-09 | 132 | 134 | 132 | 134 | 0 | 0 |
| A39 | 1.5.1.1, 1.5.2.1 | Nghiệm thu cân/tem, UAT và đối soát chi nhánh 1 |  |  |  |  | 2 | A38 FS | QA 80%; OS 40%; HW 20%; TL 10% | 2027-12-10 | 2027-12-13 | 134 | 136 | 134 | 136 | 0 | 0 |
| R51 | 1.5.1.1, 1.5.2.1 | Dự phòng sửa/kiểm lại trước vận hành chi nhánh 1 |  |  |  |  | 1 | A39 FS | OS 60%; QA 60%; HW 30%; BE 30%; FE 20% | 2027-12-14 | 2027-12-14 | 136 | 137 | 136 | 137 | 0 | 0 |
| A40 | 1.5.3.1 | Đào tạo, xác nhận vận hành và hỗ trợ ban đầu chi nhánh 1 |  |  |  |  | 2 | R51 FS | OS 80%; PM 10%; BE 10% | 2027-12-15 | 2027-12-16 | 137 | 139 | 137 | 139 | 0 | 0 |
| A41 | 1.5.1.1 | Di chuyển và lắp thiết bị tại chi nhánh 2 |  |  |  |  | 3 | A40 FS | OS 80%; HW 30% | 2027-12-17 | 2027-12-21 | 139 | 142 | 139 | 142 | 0 | 0 |
| A42 | 1.5.2.1 | Cấu hình đồng bộ/ngoại tuyến và dữ liệu chi nhánh 2 |  |  |  |  | 2 | A41 FS | TL 30%; BE 50%; FE 20%; OS 30% | 2027-12-22 | 2027-12-23 | 142 | 144 | 142 | 144 | 0 | 0 |
| A43 | 1.5.1.1, 1.5.2.1 | Nghiệm thu cân/tem, UAT và đối soát chi nhánh 2 |  |  |  |  | 2 | A42 FS | QA 80%; OS 40%; HW 20%; TL 10% | 2027-12-24 | 2027-12-27 | 144 | 146 | 144 | 146 | 0 | 0 |
| R52 | 1.5.1.1, 1.5.2.1 | Dự phòng sửa/kiểm lại trước vận hành chi nhánh 2 |  |  |  |  | 1 | A43 FS | OS 60%; QA 60%; HW 30%; BE 30%; FE 20% | 2027-12-28 | 2027-12-28 | 146 | 147 | 146 | 147 | 0 | 0 |
| A44 | 1.5.3.1 | Đào tạo, xác nhận vận hành và hỗ trợ ban đầu chi nhánh 2 |  |  |  |  | 2 | R52 FS | OS 80%; PM 10%; BE 10% | 2027-12-29 | 2027-12-30 | 147 | 149 | 147 | 149 | 0 | 0 |
| A45 | 1.6.1.1, 1.6.1.2, 1.6.2.1 | Kỹ sư RS232/Frontend bàn giao đặc tả và hồ sơ trước khi rời dự án |  |  |  |  | 1 | A44 FS | HW 50%; FE 40%; TL 20%; QA 20%; PM 10% | 2027-12-31 | 2027-12-31 | 149 | 150 | 149 | 150 | 0 | 0 |
| M5 | 1.5.1.1, 1.5.2.1, 1.5.3.1 | M5 – Hai chi nhánh đạt, được đào tạo; hồ sơ kỹ thuật đã bàn giao |  |  |  |  | 0 | A45 FS | — | 2027-12-31 | 2027-12-31 | 150 | 150 | 150 | 150 | 0 | 0 |
| A46 | 1.6.1.1 | Tổng hợp hồ sơ bốn cân và kiểm lại phần thay đổi |  |  |  |  | 3 | M5 FS | QA 80%; TL 20%; BE 10% | 2028-01-03 | 2028-01-05 | 150 | 153 | 150 | 153 | 0 | 0 |
| A48 | 1.6.2.1 | Hoàn thiện SRS/SAD/SOP/User Manual và đào tạo bổ sung |  |  |  |  | 5 | M5 FS | PM 20%; OS 60%; TL 20%; BE 10% | 2028-01-03 | 2028-01-07 | 150 | 155 | 150 | 155 | 0 | 0 |
| A47 | 1.6.1.2 | Tổng hợp hồ sơ bốn máy in và kiểm lại phần thay đổi |  |  |  |  | 2 | A46 FS | QA 80%; TL 20%; BE 10% | 2028-01-06 | 2028-01-07 | 153 | 155 | 153 | 155 | 0 | 0 |
| R6 | 1.6.3.1 | Dự phòng đóng phát hiện nghiệm thu tổng thể |  |  |  |  | 2 | A47 FS, A48 FS | QA 60%; TL 20%; BE 50%; OS 20% | 2028-01-10 | 2028-01-11 | 155 | 157 | 155 | 157 | 0 | 0 |
| A49 | 1.6.3.1 | Nghiệm thu tổng thể với chủ đầu tư và các kho |  |  |  |  | 2 | R6 FS | PM 30%; QA 30%; TL 20%; OS 20% | 2028-01-12 | 2028-01-13 | 157 | 159 | 157 | 159 | 0 | 0 |
| A50 | 1.6.3.2 | Bàn giao phần mềm/mã nguồn, CSDL, tài khoản, backup và trách nhiệm phí |  |  |  |  | 2 | A49 FS | PM 30%; TL 30%; BE 50%; OS 20% | 2028-01-14 | 2028-01-17 | 159 | 161 | 159 | 161 | 0 | 0 |
| M6 | 1.6.3.2 | M6 – Nghiệm thu, bàn giao và đóng dự án |  |  |  |  | 0 | A50 FS | — | 2028-01-17 | 2028-01-17 | 161 | 161 | 161 | 161 | 0 | 0 |

## Căn cứ từng hoạt động

| Mã | Căn cứ/điều kiện |
| --- | --- |
| A01 | Ba hồ sơ kế hoạch được lập từ tôn chỉ và WBS, có vòng thẩm định; ngân sách chi tiết phối hợp chương 4, chưa tạo PV hoàn chỉnh. |
| A02 | Khảo sát chính tại kho tổng, hai chi nhánh cung cấp thông tin/ảnh/đặc tả từ xa; có một vòng xác minh, không huy động HW hoặc Onsite tháng 1. |
| A03 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A04 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A05 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A06 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A07 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A08 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A09 | Hai ngày làm việc đặt trước để rà soát và lấy xác nhận đầu mối doanh nghiệp; thời gian phản hồi là điều kiện lịch. |
| M1 | Mốc không thời lượng; đạt khi các công việc tiền nhiệm đáp ứng tiêu chí. |
| A10 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| G1 | Giả định nhà cung cấp giao bộ 33 triệu ngay đầu tháng 2; PM đặt hàng từ tháng 1. Đây là điểm giao diện mua sắm theo 02 mục V, không thêm số lượng/ngân sách. |
| A24 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A11 | Một cặp Backend/Frontend làm lần lượt từng module, API/UI được phối hợp cùng hoạt động. Ba điểm phản ánh phạm vi module và lỗi thường gặp; không phải dữ liệu năng suất đã đo. Bắt đầu sau một ngày dựng môi trường (repo/API khung đã sẵn sàng), song song hai ngày hoàn thiện dev/test; A10 dùng 20% và A11 dùng 80% năng lực mỗi Dev, không vượt 100%. |
| A21 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A12 | Một cặp Backend/Frontend làm lần lượt từng module, API/UI được phối hợp cùng hoạt động. Ba điểm phản ánh phạm vi module và lỗi thường gặp; không phải dữ liệu năng suất đã đo. |
| A22 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A25 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A13 | Một cặp Backend/Frontend làm lần lượt từng module, API/UI được phối hợp cùng hoạt động. Ba điểm phản ánh phạm vi module và lỗi thường gặp; không phải dữ liệu năng suất đã đo. |
| A23 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A14 | Một cặp Backend/Frontend làm lần lượt từng module, API/UI được phối hợp cùng hoạt động. Ba điểm phản ánh phạm vi module và lỗi thường gặp; không phải dữ liệu năng suất đã đo. |
| A26 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A15 | Một cặp Backend/Frontend làm lần lượt từng module, API/UI được phối hợp cùng hoạt động. Ba điểm phản ánh phạm vi module và lỗi thường gặp; không phải dữ liệu năng suất đã đo. |
| A16 | Một cặp Backend/Frontend làm lần lượt từng module, API/UI được phối hợp cùng hoạt động. Ba điểm phản ánh phạm vi module và lỗi thường gặp; không phải dữ liệu năng suất đã đo. |
| A17 | Một cặp Backend/Frontend làm lần lượt từng module, API/UI được phối hợp cùng hoạt động. Ba điểm phản ánh phạm vi module và lỗi thường gặp; không phải dữ liệu năng suất đã đo. |
| A18 | Một cặp Backend/Frontend làm lần lượt từng module, API/UI được phối hợp cùng hoạt động. Ba điểm phản ánh phạm vi module và lỗi thường gặp; không phải dữ liệu năng suất đã đo. |
| A19 | Một cặp Backend/Frontend làm lần lượt từng module, API/UI được phối hợp cùng hoạt động. Ba điểm phản ánh phạm vi module và lỗi thường gặp; không phải dữ liệu năng suất đã đo. |
| A20 | Một cặp Backend/Frontend làm lần lượt từng module, API/UI được phối hợp cùng hoạt động. Ba điểm phản ánh phạm vi module và lỗi thường gặp; không phải dữ liệu năng suất đã đo. |
| A27 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| R2 | Khối dự phòng thời gian công khai cho lỗi liên module/phần cứng; 4 ngày tương đương khoảng 7% chuỗi phát triển 54 ngày, không cộng thêm 10% từng dòng. |
| M2 | Mốc không thời lượng; đạt khi các công việc tiền nhiệm đáp ứng tiêu chí. |
| G2 | 37 triệu còn lại theo 02 mục V: 1 cân, 1 máy in, 3 scanner, 1 PC. PM đặt trước tháng 5; khách hàng bố trí điện/LAN, dữ liệu chuẩn và người học trước lắp đặt. |
| A30 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A28 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A29 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A31 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| R3 | Dự phòng riêng cho cấu hình/dữ liệu thực địa chưa có trên bộ mẫu; không dùng thay tiêu chí đạt. |
| A32 | Giả định sáu nhóm người dùng học theo các ca trong ba ngày, khách hàng cung cấp người học; mỗi vai trò có kết quả thực hành trước sử dụng. |
| M3 | Mốc không thời lượng; đạt khi các công việc tiền nhiệm đáp ứng tiêu chí. |
| A33 | Ước lượng giả định BTL: phạm vi đã chốt, một người/vai trò, dành thời gian thực hiện và xử lý lỗi thông thường; cần hiệu chỉnh sau khảo sát. |
| A34 | Kiểm lại điều kiện AC-01–AC-04 khác môi trường UAT; đại diện kho/chủ đầu tư ký quyết định mở kho. |
| A35 | Một ngày chuyển trạng thái sử dụng sau xác nhận sẵn sàng; có phương án quay lại và đầu mối xử lý. |
| M4 | Mốc không thời lượng; đạt khi các công việc tiền nhiệm đáp ứng tiêu chí. |
| A36 | Hai tuần lịch liên tiếp sau go-live tương ứng 10 ngày làm việc trong lịch giả định. Ngoài giờ/cuối tuần kho không giao dịch theo giả định; phải xác nhận nếu kho hoạt động khác. |
| G3 | Bộ chi nhánh 60 triệu nhận tháng 6 theo 02, kiểm/cấu hình trước tháng 7; địa điểm và thời gian đi lại được giả định trong các hoạt động từng kho. |
| A37 | Một ngày đi lại và hai ngày lắp: 1 PC, 1 cân, 1 máy in, 2 scanner và máy chấm công khách hàng; giả định tuyến đi mỗi kho tối đa một ngày. |
| A38 | Cấu hình từ thiết kế đã kiểm, nạp dữ liệu khách hàng và đối soát kho gửi–nhận. |
| A39 | AC-01/AC-02 từng thiết bị, AC-03 quyền/offline/điều chuyển; chưa đưa vào sử dụng khi chưa đạt. |
| R51 | Dự phòng tại gate từng kho, xử lý và kiểm lại lỗi trước đào tạo/kích hoạt; lỗi chưa đạt không được bỏ qua để giữ mốc. |
| A40 | Ngày đầu đào tạo/thực hành, xác nhận đạt trước kích hoạt; ngày thứ hai hỗ trợ vận hành ban đầu. |
| A41 | Một kỹ sư Onsite nên hai chi nhánh triển khai lần lượt, cùng cấu hình/số lượng với chi nhánh 1. |
| A42 | Cấu hình, nạp/đối soát dữ liệu, kiểm liên kho theo bộ kịch bản đã đạt. |
| A43 | AC-01/AC-02 từng thiết bị và AC-03 trước sử dụng, có hồ sơ nghiệm thu. |
| R52 | Dự phòng một ngày tại gate chi nhánh 2; không kích hoạt khi chưa đạt. |
| A44 | Đào tạo/thực hành trước kích hoạt, sau đó hỗ trợ ban đầu như chi nhánh 1. |
| A45 | Bàn giao hồ sơ bốn cân/bốn máy in, cấu hình và lỗi còn mở cho QA/Tech Lead; không bố trí HW/FE ở tháng 8. |
| M5 | Mốc không thời lượng; đạt khi các công việc tiền nhiệm đáp ứng tiêu chí. |
| A46 | QA/Tech Lead tổng hợp kiểm tại từng kho và kiểm delta; không lần đầu nghiệm thu thiết bị trong tháng 8. |
| A48 | PM/Onsite cập nhật từ bản BA đã bàn giao; Tech Lead/Backend cập nhật tài liệu kỹ thuật và vận hành; đào tạo bổ sung theo nhật ký phát sinh. |
| A47 | Tổng hợp điều kiện đo <2 giây và dữ liệu tem/QR của từng máy; kiểm lại delta nếu cần. |
| R6 | Hai ngày dự phòng kiểm/cập nhật hồ sơ trước ký; không thay trách nhiệm xử lý lỗi ngăn bàn giao. |
| A49 | Lịch họp và hai ngày phản hồi/chốt biên bản giả định đã đặt trước; không coi im lặng là ký nhận. |
| A50 | Thực hành khôi phục và ký nhận đầu mối quản trị/phí sau tháng 8; tài khoản thực tế không đưa vào báo cáo nhóm. |
| M6 | Mốc không thời lượng; đạt khi các công việc tiền nhiệm đáp ứng tiêu chí. |

## Công việc quản lý xuyên kỳ

Đây là phân bổ Level of Effort (LoE) – nỗ lực xuyên kỳ; không kéo dài đường găng mạng bàn giao. Dành tỷ lệ năng lực trung bình cố định mỗi ngày trong kỳ huy động, bao gồm trong bảng nguồn lực. Họp thực tế được bố trí vào khoảng năng lực này.

| Mã | WBS | Công việc | Nguồn lực | Phân bổ |
| --- | --- | --- | --- | --- |
| L01 | 1.1.2.1 | Giao ban tuần/tháng | PM | 10% |
| L02 | 1.1.2.2 | Kiểm soát chi phí/dự phòng | PM | 5% |
| L03 | 1.1.2.3 | Báo cáo chủ đầu tư | PM | 5% |
| L04 | 1.1.3.1 | Tiếp nhận và đánh giá thay đổi | PM | 5% |
| L05 | 1.1.3.1 | Thẩm định kỹ thuật thay đổi | TL | 10% |
| L06 | 1.1.3.2 | Đảm bảo chất lượng quy trình | QA | 10% |
