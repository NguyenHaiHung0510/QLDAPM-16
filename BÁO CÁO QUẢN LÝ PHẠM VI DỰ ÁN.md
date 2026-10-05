# BÁO CÁO QUẢN LÝ PHẠM VI DỰ ÁN (PROJECT SCOPE MANAGEMENT PLAN)

- **Tên dự án:** Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS)
- **Mã bài tập:** Bài tập Nhóm 16 (PTIT)
- **Người quản lý dự án (PM):** Bùi Hồng Phú
- **Nhà tài trợ (Project Sponsor):** Ban Giám đốc Doanh nghiệp / Hợp tác xã Trà Tân Cương (Thái Nguyên)
- **Tổng ngân sách phê duyệt (BAC):** 2.000.000.000 VNĐ (Hai tỷ đồng chẵn)
- **Thời gian thực hiện:** 08 tháng (50 Man-Month / 8 vị trí chuyên môn)
- **Tác giả bản phạm vi/WBS ban đầu:** Nguyễn Đức Công. WBS là tài sản chung của nhóm; phân công làm BTL theo N-03 khác với vai trò dự án giả định.
- **Căn cứ:** 01–04; cập nhật hồi quy ngày 05/10/2026 theo các quyết định đã thống nhất. Các giả định triển khai phải được kiểm khi khảo sát/SRS.

**1\. KẾ HOẠCH QUẢN LÝ PHẠM VI (SCOPE MANAGEMENT PLAN)**

**1.1 Phương pháp thu thập yêu cầu**

Để đảm bảo thu thập đầy đủ yêu cầu nghiệp vụ và kỹ thuật IoT cho 3 kho, nhóm dự án triển khai 3 phương pháp chính:

1. **Phỏng vấn sâu & Khảo sát nghiệp vụ (Interviews):**
   - Làm việc trực tiếp với **6 nhóm người dùng**: Ban Lãnh đạo, Quản lý kho, Thủ kho, Công nhân chế biến/đóng gói, Kế toán kho và Nhân sự logistics/Tài xế.
   - Tập trung làm rõ các quy trình cốt lõi: Nhập chè búp tươi, quy đổi định mức BOM theo độ ẩm, theo dõi tỷ lệ hao hụt chè, kiểm soát vị trí ô/kệ (Zone/Bin/Rack) và quy tắc xuất kho ưu tiên FEFO (First Expired, First Out).
2. **Khảo sát kỹ thuật & Giao thức IoT (Technical & Hardware Survey):**
   - Tháng 1, BA/Tech Lead khảo sát quy trình, tài sản sẵn có và đặc tả nhà cung cấp tại ba kho. RS232 Engineer kiểm trên bộ mẫu từ tháng 2; Onsite khảo sát/lắp đặt từ tháng 5 theo lịch huy động 02.
   - Xác nhận yêu cầu sử dụng/giao thức của **04 cân RS232, 04 máy in, 08 máy quét, 04 PC mua mới** và **03 máy chấm công sẵn có** theo 01/02. Dải cân và độ chia xác nhận trong SRS; máy in/scanner/chấm công theo đặc tả tương thích, không mặc định đều dùng Serial/ASCII.
3. **Rà soát chứng từ & Dữ liệu lịch sử:**
   - Tiếp nhận các biểu mẫu sổ sách Excel hiện có, danh mục nhà vườn/nhà cung cấp, công thức tính hao hụt chế biến và dữ liệu tồn kho ban đầu do doanh nghiệp bàn giao.

**1.2 Quy trình kiểm soát thay đổi phạm vi (Scope Change Control Process)**

Các bước dưới đây là quy trình của dự án, không phải số bước bắt buộc của giáo trình:

1. Ghi phiếu CR, nêu thay đổi và lý do.
2. PM Bùi Hồng Phú/Tech Lead đánh giá tác động đến yêu cầu, WBS, tiêu chí nghiệm thu, nguồn lực, chi phí và hạn vận hành kho tổng/thời hạn bàn giao.
3. Chủ đầu tư phê duyệt mọi thay đổi phạm vi, tiêu chí chấp nhận hoặc đường cơ sở. PM điều phối sửa lỗi/cách thực hiện trong nội dung đã duyệt; không tự đổi ngưỡng hay bỏ chức năng dưới nhãn “thay đổi nhỏ”. Phương án phải đáp ứng ràng buộc hai tỷ, kho tổng chậm nhất tháng 6 và toàn dự án tám tháng. Chưa được duyệt thì chưa thực hiện.
4. Cập nhật yêu cầu/RTM, WBS Dictionary và các kế hoạch chịu ảnh hưởng; thông báo đội dự án. Không mặc định mọi CR được chi từ dự phòng 143 triệu; chương chi phí/rủi ro phải xác định căn cứ sử dụng.

**2\. MA TRẬN TRUY XUẤT YÊU CẦU (REQUIREMENTS TRACEABILITY MATRIX - RTM)**

Ma trận nối yêu cầu trong 01–04 với sản phẩm/gói công việc và điều kiện chấp nhận. Căn cứ: slide quản lý phạm vi trang 17; PMBOK 6 §5.2.3.2 (trang in 148–149) và quy tắc 100% của WBS (trang in 161). Không yêu cầu mỗi yêu cầu phải có một gói WBS riêng.

| Mã YC | Loại | Yêu cầu và nguồn | Đối tượng | WBS | Trách nhiệm | Điều kiện chấp nhận |
| --- | --- | --- | --- | --- | --- | --- |
| FR-01 | Chức năng | Nhập/xuất/kiểm kê/điều chuyển giữa ba kho, tự sinh Batch ID, ghi chất lượng lô, vị trí và FEFO; 01 mục nhập–xuất, 04 mục 2 | Thủ kho/quản lý | 1.3.1.1, 1.3.1.2 | Devs/BA | AC-03; xuất ưu tiên lô còn hạn được phép xuất; mã lô không trùng |
| FR-02 | Chức năng | BOM, độ ẩm trà và hao hụt theo công thức đã xác nhận; 01 mục thông tin trà/BOM, 04 mục 2 | Kho/công nhân | 1.3.2.1 | Devs/BA | AC-03; nguồn độ ẩm trà riêng với %RH môi trường |
| FR-03 | Chức năng | Cảnh báo cận hạn/hết hạn, tồn tối thiểu và Aging; 01 mục tồn/bảo quản, 04 mục 2 | Quản lý/lãnh đạo | 1.3.2.2 | Devs | AC-03; kiểm trước/đúng/sau ngưỡng và ngày hết hạn |
| FR-04 | Tích hợp | Đọc cân RS232 theo dải sử dụng được chấp nhận; 01 mục ngoại vi, 02 mục IV, 04 mục 4 | Công nhân/thủ kho | 1.3.3.1, 1.3.5.1 | RS232/QA | AC-01 |
| FR-05 | Tích hợp | In tem/phiếu và quét barcode/QR; 01 mục ngoại vi, 02 mục IV | Công nhân/thủ kho | 1.3.3.2, 1.3.3.3, 1.3.5.2 | RS232/QA | AC-02 và AC-03; không khóa hãng |
| FR-06 | Tích hợp | Chấm công từ máy sẵn có; 01 mục nhân sự/giả định, 04 mục 2 | Kho/kế toán | 1.3.3.3 | Devs/RS232 | AC-03; đối soát dữ liệu máy, không nhập trùng |
| FR-07 | Chức năng | Nhà cung cấp, lịch sử nhập, đơn hàng xuất và trạng thái vận chuyển; 01 mục nhà cung cấp/đơn hàng | Kho/kế toán/logistics | 1.3.4.2 | Devs | AC-03; nhân sự logistics hoặc đầu mối kho cập nhật trên máy Windows |
| FR-08 | Chức năng | Chi phí nguyên liệu, giá thành lô, doanh thu, công nợ, phí vận hành; 01 mục tài chính | Kế toán/lãnh đạo | 1.3.4.2, 1.3.4.1 | Devs/BA | AC-03; số nhập bổ sung và số tổng đối soát |
| FR-09 | Chức năng | Nhật ký nhiệt độ/%RH môi trường, nguồn đo sẵn có và nhập thủ công; 01 mục tồn/giả định, 04 mục 2 | Thủ kho | 1.3.2.3 | Devs/BA | AC-03; có kho/khu vực, thời điểm, số đo và người ghi |
| FR-10 | Chức năng | Lịch ca và phân quyền theo vai trò; 01 mục nhân sự | Kho/kế toán/người dùng | 1.3.4.3 | Devs/BA | AC-03; kiểm cho phép/từ chối của cả sáu vai trò |
| FR-11 | Chức năng | Danh mục cơ sở vật chất, dụng cụ, máy móc, bao bì/tem; 01 mục tài sản/vật tư | Kho/kế toán | 1.3.4.4 | Devs/BA | AC-03; lưu/tra cứu/cập nhật theo quyền |
| FR-12 | Chức năng | Danh mục trà, loại, nguồn gốc, ngày sản xuất/hạn, quy cách; 01 mục thông tin trà | Kho/kế toán | 1.3.1.1, 1.3.3.4 | Devs/BA | AC-03; trường bắt buộc và dữ liệu nhập được kiểm |
| FR-13 | Chức năng | Báo cáo nhập–xuất–tồn, hao hụt, bán chạy/tồn lâu; 01 mục thống kê | Kho/lãnh đạo | 1.3.4.1, 1.3.2.2 | Devs | AC-03; số liệu và bộ lọc khớp tập đối soát |
| NFR-01 | Kỹ thuật | Web trên máy Windows, môi trường ứng dụng/CSDL; 01 mục triển khai, 02 khoản cloud | Các vai trò | 1.2.3.1, 1.2.3.4, 1.4.2.1 | Tech Lead/Backend | AC-04; cấu hình kỹ thuật trong SAD |
| NFR-02 | Kỹ thuật | Đồng bộ ba kho, đệm dữ liệu khi mất mạng; 02 vai Tech Lead, 03 giả định | Ba kho | 1.2.3.2, 1.5.2.1 | Tech Lead/Devs | AC-03; ngắt/khôi phục và đối soát, không trùng/mất giao dịch trong phạm vi offline SRS |
| NFR-03 | Chất lượng | Cân <0,1%, in tem <2 giây/sản phẩm; 04 mục 4 | Người vận hành | 1.3.5.1, 1.3.5.2, 1.6.1.1, 1.6.1.2 | QA/RS232 | AC-01/AC-02, đạt ở từng mẫu theo điều kiện xác định |
| TR-01 | Chuyển đổi | Danh mục, lô và tồn đầu kỳ từ Excel; 03 giả định/04 mục 6 | Kho/kế toán | 1.3.3.4, 1.4.1.3, 1.4.2.1 | BA/Onsite/Backend | AC-03/AC-04; doanh nghiệp chuẩn hóa, đội dự án kiểm/import/đối soát |
| TR-02 | Chuyển đổi | SRS/SAD/SOP/User Manual, đào tạo trước sử dụng và bổ sung cuối kỳ; 02 mục VI, 04 mục 3 | Người dùng kho | 1.4.1.4, 1.5.3.1, 1.6.2.1 | BA bàn giao; Onsite/PM tiếp nhận | AC-04; danh sách người học và thao tác theo vai trò |
| TR-03 | Bàn giao | Gói phần mềm/hồ sơ triển khai, tài khoản, CSDL, sao lưu/khôi phục, hướng dẫn vận hành; 04 mục 3 và giả định vận hành | Doanh nghiệp | 1.4.2.1, 1.6.3.2 | Tech Lead/Backend/PM | AC-04; đầu mối nhận và trách nhiệm phí sau dự án rõ |
| PR-01 | Ràng buộc | Hai tỷ/50 MM, kho tổng chậm nhất tháng 6, toàn dự án tám tháng; 01/02/04 | Chủ đầu tư/PM | 1.1.1.1, 1.1.1.3, 1.1.2.2, 1.6.3.1 | PM | Kế hoạch và biên bản đáp ứng mốc/ngân sách gốc |

**3\. TUYÊN BỐ PHẠM VI DỰ ÁN (PROJECT SCOPE STATEMENT)**

**3.1 Mục tiêu dự án**

Triển khai thành công Hệ thống Quản lý Kho Trà và Chuỗi cung ứng Tân Cương (WMS) thống nhất cho 01 Kho tổng chế biến/đóng gói tại Thái Nguyên và 02 Kho chi nhánh phân phối. Dự án thực hiện trong **8 tháng (50 Man-Month)** với tổng ngân sách phê duyệt **BAC = 2.000.000.000 VNĐ**.

**3.2 Phạm vi công việc BAO GỒM (In-Scope)**

- **Nghiên cứu/thiết kế:** Khảo sát và xác nhận SRS, SAD, giao thức ngoại vi, dải cân sử dụng; chuẩn bị SOP/User Manual và phương pháp nghiệm thu theo RTM.
- **Phần mềm:** Các yêu cầu FR-01–FR-13 và NFR trong RTM, đều truy về 01–04; không thêm nghiệp vụ kho trà ngoài bộ gốc trong lượt cập nhật này.
- **Ngoại vi:** Kết nối bốn cân RS232, bốn máy in, tám máy quét và ba máy chấm công sẵn có theo giả định. Cổng/giao thức của từng loại thiết bị theo đặc tả tương thích; RS232 của cân không buộc mọi ngoại vi dùng RS232. Hãng thiết bị chưa khóa ở chương 2.
- **Triển khai/vận hành:** Chuẩn bị môi trường dev/test và production, cấu hình ứng dụng/CSDL, sao lưu/khôi phục; lắp thiết bị mua mới 130 triệu theo 02. Kho tổng đào tạo trước go-live, vận hành chậm nhất cuối tháng 6; hai chi nhánh triển khai/đào tạo tháng 7; bổ sung đào tạo và bàn giao tháng 8.
- **Nguồn số đo:** Thiết bị đo môi trường và khâu kiểm chất lượng trà của khách hàng; nhập thủ công là đường cơ sở. Kết nối đo không dây chỉ là tùy chọn được khảo sát và phê duyệt nếu bổ sung, không chặn nghiệm thu phương án thủ công.

**3.3 Ranh giới trách nhiệm và phần không bao gồm**

- Không làm ứng dụng native iOS/Android; đầu cuối WMS của tình huống là máy Windows. Logistics/đầu mối kho nhập xác nhận trên đầu cuối được phân quyền, không hứa ứng dụng tài xế ngoài kho.
- Khách hàng cung cấp điện, đường Internet và tài sản sẵn có theo 01/02. Đội dự án kết nối/cấu hình LAN, PC, ngoại vi và WMS; vật tư mạng chi nhánh theo 02. Thi công điện/đường ISP ngoài điểm đấu nối không thuộc dự án; thiếu vật tư/LAN cần đánh giá và phê duyệt trước lắp.
- Doanh nghiệp chuẩn hóa Excel danh mục/lô/tồn đầu kỳ. Đội dự án cung cấp công cụ, kiểm/import/đối soát; không nhập tay toàn bộ sổ lịch sử, không cam kết chuyển mọi giao dịch quá khứ.
- Phí hạ tầng trong ngân sách bao phủ tám tháng dự án. Sau bàn giao, doanh nghiệp quản trị và chi trả duy trì; bảo trì dài hạn là thỏa thuận riêng.

**3.4 Tiêu chí thành công và điều kiện nghiệm thu**

Kho tổng vận hành chậm nhất 02/12/2027, toàn dự án bàn giao chậm nhất 02/02/2028; chi phí không vượt hai tỷ. Phần bàn giao được kiểm theo AC-01–AC-04 dưới đây, đối chiếu RTM. Chủ đầu tư, đại diện các kho liên quan và PM xác nhận theo từng mốc. Đây là điều kiện lập kế hoạch, chưa phải kết quả QA đã chạy.

### AC-01 Độ chính xác cân và dữ liệu RS232

- SRS chốt trước mua/nhận thiết bị: dải khối lượng nghiệp vụ `[m_min, m_max]` với `0 < m_min < m_max`, đơn vị kg, độ chia và trạng thái cân hợp lệ cho từng loại trạm. Không tự giả định kho cần cân gói nhỏ; không nghiệm thu dải chưa được xác nhận. Thiết bị phải đáp ứng cả dải và ngưỡng tại đó.
- Mỗi cân được kiểm **50 phép cân hợp lệ**: năm mức tải `m_min`, `m_min + 0,25 × (m_max − m_min)`, `m_min + 0,50 × (m_max − m_min)`, `m_min + 0,75 × (m_max − m_min)` và `m_max`; mỗi mức lặp mười lần. Vật đối chuẩn/thiết bị tham chiếu có khối lượng `m_ref > 0` đã xác nhận, điều kiện đặt cân và tare theo hướng dẫn thiết bị. Bốn cân có tổng 200 phép cân hợp lệ trong kế hoạch.
- Mỗi phép cân phải thỏa `abs(m_WMS - m_ref) / m_ref × 100% < 0,1%`; không dùng sai số trung bình để che mẫu không đạt. Đồng thời giá trị, đơn vị và trạng thái WMS phải khớp dữ liệu hợp lệ từ cân sau quy đổi đơn vị/độ chia đã chấp nhận; tiêu chí truyền nhận này tách với sai số phép cân vật lý.
- Kiểm riêng sáu nhóm tình huống, ít nhất một ca cho mỗi tình huống nêu trong nhóm trên từng cân: zero và tare; cân chưa ổn định; dưới và trên dải được phép; chuỗi số sai và đơn vị sai; mất cổng và mất kết nối khi đang đọc; khôi phục kết nối và gửi lại dữ liệu. Không áp phần trăm cho mẫu zero. WMS không chấp nhận bản ghi lỗi như số cân hợp lệ, không phát sinh giao dịch trùng khi khôi phục. Test Plan ghi ca cụ thể, không chọn một ca rồi coi đã phủ mọi nhánh của cả nhóm.
- Biên lai ghi ID cân, tải tham chiếu, số cân/WMS, đơn vị, trạng thái, thời điểm và kết quả từng ca. Nghiệm thu tại từng kho trước vận hành; tháng 8 tổng hợp biên lai và kiểm lại phần thay đổi, không đợi tháng 8 mới kiểm độ chính xác lần đầu.

### AC-02 Thời gian và nội dung in tem

- Kiểm **30 tem/máy** trên cả bốn máy (120 tem): ba bộ dữ liệu tem hợp lệ gồm tối thiểu trường bắt buộc, dữ liệu điển hình và độ dài tối đa trong định dạng SRS; mỗi bộ mười tem. Máy có giấy/mực, đã sẵn sàng và dùng cấu hình triển khai; tính cả tem đầu của mỗi bộ và việc tạo QR/truyền lệnh/hàng đợi/in.
- Thời gian tính từ người dùng xác nhận yêu cầu in hợp lệ trên WMS đến khi tem in xong có thể lấy, không tính thao tác dán. **Từng tem <2 giây**, không chỉ trung bình. Nội dung khớp lô/trọng lượng/ngày theo mẫu; QR quét lại đúng dữ liệu. Cả bốn máy phải đạt trước sử dụng tại kho tương ứng.
- Kiểm riêng bốn nhóm, ít nhất một ca/nhóm/máy: dữ liệu yêu cầu không hợp lệ; hết giấy/mực hoặc máy chưa sẵn sàng; mất/khôi phục kết nối; thao tác in lại. Không báo in thành công khi chưa hoàn thành; in lại là thao tác rõ ràng của người có quyền và không tạo giao dịch kho mới. Nhóm lỗi không áp <2 giây nhưng phải có xử lý/hiển thị đúng.
- Bộ kiểm trên là mẫu nghiệm thu do nhóm xác định cho tình huống, không phải cỡ mẫu bắt buộc của PMBOK hoặc chứng minh độ tin cậy suốt vòng đời. Chương 9 cụ thể hóa bộ dữ liệu, thao tác và cách ghi thời gian, giữ điều kiện đạt.

### AC-03 Độ phủ chức năng và dữ liệu

Tập QA có ba kho, đủ sáu vai trò và dữ liệu đối soát thống nhất. Mỗi FR trong RTM có ít nhất một trường hợp hợp lệ và một trường hợp không hợp lệ/không được phép; yêu cầu có ngưỡng/ngày có thêm ca ngay trước, đúng và ngay sau biên. Các nhóm bắt buộc trong Test Plan: mã lô/danh mục; nhập–xuất–tồn/đối soát; điều chuyển giữa kho (giao dịch hợp lệ, ca sai/không được phép và đối soát số lượng/trạng thái tại kho gửi–kho nhận); FEFO lô còn hạn và không xuất lô hết hạn; BOM với độ ẩm trà; cận hạn/hết hạn/tồn tối thiểu; nhật ký môi trường nhập thủ công; lịch ca/chấm công/phân quyền; tài sản/vật tư; nhà cung cấp/đơn hàng/trạng thái; tài chính/báo cáo; Excel sai trường và đối soát tồn đầu kỳ; mất/khôi phục mạng trong nghiệp vụ offline SRS. Mỗi ca có đầu vào, kết quả mong đợi và kết quả thực tế; không dùng câu “100% chức năng đạt” khi chưa có danh sách ca phủ yêu cầu.

### AC-04 Triển khai đào tạo và bàn giao

Môi trường phục vụ từng kho được xác nhận sẵn sàng trước go-live; dữ liệu danh mục/lô/tồn đầu kỳ đối soát và loại dữ liệu thử. Người dùng được đào tạo theo vai trò trước sử dụng, có danh sách và ca thao tác thực hành. Có bộ tài liệu, tài khoản quản trị, bản sao lưu và biên lai thử khôi phục, đầu mối doanh nghiệp tiếp nhận cùng trách nhiệm phí sau tháng 8. QA/PM đối chiếu hồ sơ với RTM và ký nhận từng mốc; chi tiết lịch, công, chi phí và biểu mẫu hoàn thiện ở chương 3–9.

**4\. CẤU TRÚC PHÂN CHIA CÔNG VIỆC (WORK BREAKDOWN STRUCTURE - WBS)**

Cây WBS được phân rã chi tiết **4 cấp**, bám sát **6 Mốc tiến độ (Milestones)** và bộ sản phẩm bàn giao của dự án:

```text
1. DỰ ÁN WMS TRÀ TÂN CƯƠNG
├── 1.1 Quản lý Dự án (PMO)
│   ├── 1.1.1 Khởi tạo & Lập Kế hoạch
│   │   ├── 1.1.1.1 Xây dựng Kế hoạch Quản lý Dự án Tổng thể (PMP)
│   │   ├── 1.1.1.2 Xây dựng Kế hoạch Quản lý Phạm vi & Từ điển WBS
│   │   └── 1.1.1.3 Lập Tiến độ Chi tiết & Phân bổ Ngân sách BAC 2.0 Tỷ
│   ├── 1.1.2 Giám sát & Điều phối Thực thi
│   │   ├── 1.1.2.1 Tổ chức Họp Giao ban Định kỳ Tuần/Tháng
│   │   ├── 1.1.2.2 Theo dõi, Kiểm soát Chi phí & Quỹ Dự phòng (143 triệu)
│   │   └── 1.1.2.3 Báo cáo Tiến độ Định kỳ cho Project Sponsor
│   └── 1.1.3 Quản lý Thay đổi & Đảm bảo Chất lượng
│       ├── 1.1.3.1 Tiếp nhận & Đánh giá Yêu cầu Thay đổi (CR)
│       └── 1.1.3.2 Đảm bảo Chất lượng Quy trình (QA)
├── 1.2 M1: Phân tích Yêu cầu & Thiết kế Kiến trúc (Tháng 1)
│   ├── 1.2.1 Khảo sát Hiện trạng Nghiệp vụ 3 Kho & Thiết bị IoT
│   │   ├── 1.2.1.1 Khảo sát luồng nhập/chế biến/xuất tại Kho tổng Thái Nguyên
│   │   ├── 1.2.1.2 Khảo sát yêu cầu và đặc tả kết nối thiết bị
│   │   └── 1.2.1.3 Thu thập biểu mẫu Excel dữ liệu cũ & định mức BOM
│   ├── 1.2.2 Biên soạn Đặc tả Yêu cầu Phần mềm (SRS)
│   │   ├── 1.2.2.1 Lập đặc tả use-case cho 6 nhóm người dùng
│   │   └── 1.2.2.2 Xác nhận yêu cầu phi chức năng và bộ nghiệm thu ngoại vi
│   └── 1.2.3 Thiết kế Kiến trúc Hệ thống (SAD) & CSDL
│       ├── 1.2.3.1 Thiết kế kiến trúc Web App trên máy trạm Windows
│       ├── 1.2.3.2 Thiết kế dữ liệu chung ba kho và cơ chế đệm ngoại tuyến
│       ├── 1.2.3.3 Thiết kế Giao diện (UI/UX) cho Thủ kho, Công nhân & Lãnh đạo
│       └── 1.2.3.4 Chuẩn bị môi trường phát triển và kiểm thử
├── 1.3 M2: Phát triển Phần mềm Lõi & IoT RS232 (Tháng 2 - Tháng 4)
│   ├── 1.3.1 Phát triển Core WMS & Quản lý Kho
│   │   ├── 1.3.1.1 Lập trình Chức năng Nhập/Xuất/Kiểm kê & Sơ đồ Zone/Bin/Rack
│   │   └── 1.3.1.2 Lập trình Thuật toán Xuất kho Ưu tiên FEFO
│   ├── 1.3.2 Phát triển Module Định mức BOM & Cảnh báo
│   │   ├── 1.3.2.1 Lập trình công thức quy đổi BOM theo độ ẩm & hao hụt chè
│   │   ├── 1.3.2.2 Phát triển cảnh báo tồn tối thiểu cận hạn hết hạn và Aging
│   │   └── 1.3.2.3 Phát triển nhật ký nhiệt độ và độ ẩm môi trường
│   ├── 1.3.3 Phát triển Module Kết nối Thiết bị Phần cứng (IoT)
│   │   ├── 1.3.3.1 Lập trình Service kết nối RS232 đọc dữ liệu cân tự động
│   │   ├── 1.3.3.2 Phát triển tạo QR và kết nối máy in tem phiếu
│   │   ├── 1.3.3.3 Lập trình tích hợp Máy quét QR & Máy chấm công
│   │   └── 1.3.3.4 Phát triển công cụ Excel danh mục lô và tồn đầu kỳ
│   ├── 1.3.4 Phát triển Dashboard & Chức năng Bổ trợ
│   │   ├── 1.3.4.1 Lập trình Dashboard KPI, báo cáo doanh thu & giá vốn cho Lãnh đạo
│   │   ├── 1.3.4.2 Lập trình Module Quản lý Nhà cung cấp, Kế toán kho & Tài xế
│   │   ├── 1.3.4.3 Phát triển lịch ca và phân quyền vai trò
│   │   └── 1.3.4.4 Phát triển danh mục tài sản dụng cụ và vật tư
│   └── 1.3.5 Kiểm thử Tích hợp Nội bộ (Internal Integration Testing)
│       ├── 1.3.5.1 Kiểm thử luồng dữ liệu Cân RS232 đến Web App
│       └── 1.3.5.2 Kiểm thử in tem và chức năng theo RTM
├── 1.4 M3 & M4: Triển khai, UAT & Go-Live Kho Tổng Thái Nguyên (Tháng 5 - Tháng 6)
│   ├── 1.4.1 M3: Lắp đặt, UAT và đào tạo trước vận hành (Tháng 5)
│   │   ├── 1.4.1.1 Lắp đặt PC, Trạm cân RS232, Máy in theo chuẩn tương thích, Máy quét tại Kho tổng
│   │   ├── 1.4.1.2 Xây dựng kịch bản UAT & Hướng dẫn 6 nhóm người dùng thử nghiệm
│   │   ├── 1.4.1.3 Khởi tạo dữ liệu danh mục trà ban đầu từ file Excel
│   │   └── 1.4.1.4 Đào tạo vận hành kho tổng trước go-live
│   └── 1.4.2 M4: Go-live kho tổng chậm nhất cuối tháng 6
│       ├── 1.4.2.1 Triển khai production và chuyển dữ liệu mở kho
│       ├── 1.4.2.2 Đưa kho tổng vào vận hành chậm nhất cuối tháng 6
│       └── 1.4.2.3 Thực hiện hỗ trợ kỹ thuật trực tiếp tại Thái Nguyên
├── 1.5 M5: Triển khai & Triển khai đồng bộ cho 02 Kho Chi nhánh (Tháng 7)
│   ├── 1.5.1 Lắp đặt Phần cứng & Thiết bị tại 02 Kho Chi nhánh Phân phối
│   │   └── 1.5.1.1 Lắp đặt PC, Trạm cân, Máy in theo chuẩn tương thích tại 2 chi nhánh
│   ├── 1.5.2 Cấu hình đồng bộ dữ liệu và cơ chế đệm ngoại tuyến
│   │   └── 1.5.2.1 Thiết lập đồng bộ dữ liệu ba kho và đệm ngoại tuyến
│   └── 1.5.3 Đào tạo & Chuyển giao tại 02 Chi nhánh
│       └── 1.5.3.1 Đào tạo thao tác phần mềm cho Thủ kho & Nhân sự 2 chi nhánh
└── 1.6 M6: Đào tạo, Nghiệm thu Tổng thể & Đóng Dự án (Tháng 8)
    ├── 1.6.1 Tổng hợp và kiểm lại tiêu chí thành công
    │   ├── 1.6.1.1 Đo đạc sai số cân tự động qua RS232 (< 0,1%)
    │   └── 1.6.1.2 Tổng hợp nghiệm thu tạo và in tem
    ├── 1.6.2 Hoàn thiện Bộ Tài liệu Dự án
    │   └── 1.6.2.1 Hoàn thiện bộ tài liệu SRS, SAD, SOP & User Manual
    └── 1.6.3 Nghiệm thu Tổng thể & Kết thúc Dự án
        ├── 1.6.3.1 Ký Biên bản UAT & Nghiệm thu Tổng thể với Ban Giám đốc
        └── 1.6.3.2 Bàn giao hệ thống và đóng dự án
```

**5. TỪ ĐIỂN WBS**

Từ điển bao phủ 47 gói cấp thấp nhất. Giữ mã gói gốc; năm gói bổ sung làm rõ yêu cầu/đầu ra đã có trong 01–04. Chi tiết thời lượng, công và chi phí được hoàn thiện khi lập các kế hoạch liên quan.

### Quản lý dự án

**Gói công việc 1.1.1.1: Xây dựng Kế hoạch Quản lý Dự án Tổng thể (PMP)**

- **Mã WBS:** 1.1.1.1
- **Mô tả công việc:** Lập Kế hoạch Quản lý Dự án tổng hợp đầy đủ các kế hoạch thành phần: phạm vi, tiến độ, chi phí, chất lượng, nhân sự, rủi ro và mua sắm.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Document Kế hoạch Quản lý Dự án (PMP Document).
- **Tiêu chí chấp nhận:** Được Ban Giám đốc phê duyệt; khớp 100% mục tiêu 8 tháng và ngân sách BAC 2.0 Tỷ VNĐ.

**Gói công việc 1.1.1.2: Xây dựng Kế hoạch Quản lý Phạm vi & Từ điển WBS**

- **Mã WBS:** 1.1.1.2
- **Mô tả công việc:** Chi tiết hóa Tuyên bố Phạm vi, Ma trận RTM, phân rã Cây WBS 4 cấp và biên soạn Từ điển WBS toàn diện.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Báo cáo Scope Management Plan & Full WBS Dictionary.
- **Tiêu chí chấp nhận:** Phủ kín 100% các yêu cầu nghiệp vụ kho và tích hợp thiết bị IoT của Trà Tân Cương.

**Gói công việc 1.1.1.3: Lập Tiến độ Chi tiết & Phân bổ Ngân sách BAC 2.0 Tỷ**

- **Mã WBS:** 1.1.1.3
- **Mô tả công việc:** Lập lịch trình làm việc chi tiết cho 8 nhân sự (50 Man-Month); xác định đường găng (Critical Path) hướng tới mốc Go-live Kho tổng Tháng 6; phân bổ ngân sách BAC 2.0 Tỷ VNĐ.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Biểu đồ Gantt Chart & Bảng phân bổ chi phí chi tiết.
- **Tiêu chí chấp nhận:** Bảo đảm mốc Go-live Tháng 6 và tổng chi phí không vượt quá 2.000.000.000 VNĐ.

**Gói công việc 1.1.2.1: Tổ chức Họp Giao ban Định kỳ**

- **Mã WBS:** 1.1.2.1
- **Mô tả công việc:** Tổ chức họp giao ban của đội dự án tám vị trí và báo cáo với chủ đầu tư; không phải lịch họp/điều phối BTL của nhóm sinh viên.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Biên bản họp (Meeting Minutes) & Danh sách việc cần làm (Action Items).
- **Tiêu chí chấp nhận:** 100% các cuộc họp có biên bản và được ghi nhận tiến độ đầy đủ.

**Gói công việc 1.1.2.2: Theo dõi, Kiểm soát Chi phí & Quỹ Dự phòng (143 triệu)**

- **Mã WBS:** 1.1.2.2
- **Mô tả công việc:** Theo dõi chi phí thực tế (AC) so với kế hoạch (PV), quản lý việc sử dụng Quỹ dự phòng rủi ro 143.000.000 VNĐ (7.15%).
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Báo cáo theo dõi ngân sách hàng tháng.
- **Tiêu chí chấp nhận:** Đối chiếu ngân sách công việc và căn cứ sử dụng dự phòng theo kế hoạch chi phí/rủi ro; không mặc định mọi phát sinh là khoản được chi từ 143 triệu.

**Gói công việc 1.1.2.3: Báo cáo Tiến độ Định kỳ cho Project Sponsor**

- **Mã WBS:** 1.1.2.3
- **Mô tả công việc:** Tổng hợp báo cáo tiến độ (Monthly Status Report) gửi Ban Giám đốc Doanh nghiệp Trà Tân Cương.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Báo cáo tiến độ dự án.
- **Tiêu chí chấp nhận:** Báo cáo gửi đúng hạn vào ngày cuối cùng của mỗi tháng.

**Gói công việc 1.1.3.1: Tiếp nhận & Đánh giá Yêu cầu Thay đổi (CR)**

- **Mã WBS:** 1.1.3.1
- **Mô tả công việc:** Tiếp nhận, ghi nhận và phân tích tác động của các phiếu CR về chi phí, tiến độ và kỹ thuật trước khi trình duyệt.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú / Solution Architect
- **Sản phẩm đầu ra:** Nhật ký thay đổi (Change Log) & Báo cáo đánh giá tác động.
- **Tiêu chí chấp nhận:** Thay đổi phạm vi/tiêu chí/đường cơ sở có phê duyệt của chủ đầu tư; sửa lỗi trong nội dung đã duyệt do PM điều phối, theo mục 1.2.

**Gói công việc 1.1.3.2: Đảm bảo Chất lượng Quy trình (QA)**

- **Mã WBS:** 1.1.3.2
- **Mô tả công việc:** Kiểm tra, giám sát việc tuân thủ quy trình làm việc, chuẩn coding và quy trình đóng gói phần mềm của nhóm.
- **Người chịu trách nhiệm:** QA Engineer
- **Sản phẩm đầu ra:** Báo cáo kiểm định chất lượng (QA Report).
- **Tiêu chí chấp nhận:** Không vi phạm các quy trình quản lý chất lượng đã đề ra trong PMP.

### M1 Phân tích và thiết kế (tháng 1)

**Gói công việc 1.2.1.1: Khảo sát Luồng Nhập/Chế biến/Xuất tại Kho Tổng Thái Nguyên**

- **Mã WBS:** 1.2.1.1
- **Mô tả công việc:** Phỏng vấn Chị Đại diện Kho tổng và công nhân tại Kho tổng Thái Nguyên về quy trình thu mua búp tươi, chế biến, đóng gói và lưu kho.
- **Người chịu trách nhiệm:** BA / Solution Architect
- **Sản phẩm đầu ra:** Sơ đồ dòng quy trình nghiệp vụ (Business Process Model) Kho tổng.
- **Tiêu chí chấp nhận:** Đầu mối kho xác nhận quy trình và nguồn dữ liệu theo các nhóm yêu cầu 01; điểm chưa xác nhận được ghi thành giả định, không gán là kết quả khảo sát thật.

**Gói công việc 1.2.1.2: Khảo sát yêu cầu và đặc tả kết nối thiết bị**

- **Mã WBS:** 1.2.1.2
- **Mô tả công việc:** BA/Tech Lead thu thập yêu cầu dải cân/độ chia, đặc tả RS232 của bốn cân mua mới, bốn máy in/tám scanner và ba máy chấm công sẵn có; nguồn đo môi trường/độ ẩm trà theo 01. Đặc tả nhà cung cấp dùng ở tháng 1; kiểm trên bộ mẫu khi nhận từ tháng 2.
- **Người chịu trách nhiệm:** Solution Architect / BA
- **Sản phẩm đầu ra:** Danh mục trạm/thiết bị, yêu cầu sử dụng, đặc tả giao thức và danh sách giả định cần xác nhận.
- **Tiêu chí chấp nhận:** Không tự suy mọi thiết bị dùng ASCII/Serial; dải sử dụng và điều kiện AC-01/AC-02 được xác nhận trong SRS trước nhận/mua thiết bị; giả định tài sản sẵn có được kiểm.

**Gói công việc 1.2.1.3: Thu thập Biểu mẫu Excel Dữ liệu Cũ & Định mức BOM**

- **Mã WBS:** 1.2.1.3
- **Mô tả công việc:** Thu thập file Excel danh mục chè, nhà vườn, mẫu sổ sách kế toán và công thức tính hao hụt chè theo độ ẩm.
- **Người chịu trách nhiệm:** BA
- **Sản phẩm đầu ra:** Tập hợp file dữ liệu mẫu & Công thức chuyển đổi BOM.
- **Tiêu chí chấp nhận:** Cung cấp đầy đủ công thức quy đổi độ ẩm phục vụ lập trình module BOM.

**Gói công việc 1.2.2.1: Lập Đặc tả Use-case cho 6 Nhóm Người dùng**

- **Mã WBS:** 1.2.2.1
- **Mô tả công việc:** Biên soạn tài liệu chi tiết use-case cho 6 vai trò: Lãnh đạo, Quản lý kho, Thủ kho, Công nhân, Kế toán kho, Tài xế/Logistics.
- **Người chịu trách nhiệm:** BA / Solution Architect
- **Sản phẩm đầu ra:** Tài liệu Đặc tả Yêu cầu Phần mềm SRS (Functional SRS).
- **Tiêu chí chấp nhận:** SRS truy vết toàn bộ nhóm yêu cầu 01–04 trong RTM; các tham số/dải nghiệp vụ và giới hạn offline được chủ đầu tư xác nhận.

**Gói công việc 1.2.2.2: Xác nhận yêu cầu phi chức năng và bộ nghiệm thu ngoại vi**

- **Mã WBS:** 1.2.2.2
- **Mô tả công việc:** Xác nhận dải cân/độ chia/đơn vị, định dạng tem, AC-01/AC-02 và giới hạn công việc được đệm khi mất mạng. Chuẩn của máy in/scanner/chấm công theo thiết bị tương thích; RS232 Engineer phản biện và kiểm mẫu từ tháng 2.
- **Người chịu trách nhiệm:** Solution Architect / BA
- **Sản phẩm đầu ra:** Phần phi chức năng SRS và bộ điều kiện nghiệm thu ngoại vi.
- **Tiêu chí chấp nhận:** Ngưỡng <0,1% và <2 giây có đại lượng, tập mẫu và quy tắc đạt theo AC-01/AC-02; không để trống ngưỡng hoặc hứa độ trễ bằng không.

**Gói công việc 1.2.3.1: Thiết kế Kiến trúc Web App trên Máy trạm Windows**

- **Mã WBS:** 1.2.3.1
- **Mô tả công việc:** Thiết kế mô hình kiến trúc phần mềm (SAD), mô hình giao tiếp giữa Web Client, Local Service kết nối RS232 và CSDL Server.
- **Người chịu trách nhiệm:** Solution Architect
- **Sản phẩm đầu ra:** Tài liệu Thiết kế Kiến trúc Hệ thống (SAD).
- **Tiêu chí chấp nhận:** Tương thích hoàn toàn với hệ điều hành Windows trên máy trạm tại 3 kho.

**Gói công việc 1.2.3.2: Thiết kế dữ liệu chung ba kho và cơ chế đệm ngoại tuyến**

- **Mã WBS:** 1.2.3.2
- **Mô tả công việc:** Thiết kế dữ liệu lô/vị trí/nghiệp vụ ba kho và phương án đệm khi mất mạng theo phạm vi offline SRS; SAD xác định kiến trúc lưu trữ, đồng bộ và xử lý trùng/xung đột, không mặc định phải nhân bản ba CSDL.
- **Người chịu trách nhiệm:** Solution Architect
- **Sản phẩm đầu ra:** File thiết kế CSDL (Database Schema Design).
- **Tiêu chí chấp nhận:** Kiến trúc đáp ứng đồng bộ và giới hạn offline SRS; có phương án đối soát, không tự thu hẹp khả năng ngoại tuyến đã nhận từ 02/03.

**Gói công việc 1.2.3.3: Thiết kế Giao diện (UI/UX) cho Thủ kho, Công nhân & Lãnh đạo**

- **Mã WBS:** 1.2.3.3
- **Mô tả công việc:** Thiết kế Wireframe/Prototype giao diện Dashboard KPI, màn hình cân-in tem nút bấm to cho công nhân, màn hình quét QR cho thủ kho.
- **Người chịu trách nhiệm:** BA / Solution Architect
- **Sản phẩm đầu ra:** Bộ thiết kế Figma/UI Prototype.
- **Tiêu chí chấp nhận:** Bản thiết kế thể hiện các thao tác theo vai trò và được đầu mối nghiệp vụ xác nhận; Frontend tiếp nhận từ tháng 2, không bổ sung nhân sự UI/UX riêng.

**Gói công việc 1.2.3.4: Chuẩn bị môi trường phát triển và kiểm thử**

- **Mã WBS:** 1.2.3.4
- **Mô tả công việc:** Tech Lead thiết lập môi trường ban đầu trong tháng 1 từ gói cloud/VPS 02; Backend tiếp nhận và hoàn thiện khi tham gia từ tháng 2. Chưa cần chốt CPU/RAM hoặc nhà cung cấp trong chương phạm vi.
- **Người chịu trách nhiệm:** Solution Architect
- **Sản phẩm đầu ra:** Môi trường dev/test và thông tin vận hành cấu hình ban đầu.
- **Tiêu chí chấp nhận:** Môi trường sẵn sàng theo nhu cầu giai đoạn, có đầu mối quản trị; không cộng trùng khoản 25 triệu.

### M2 Phát triển và kiểm thử (tháng 2–4)

**Gói công việc 1.3.1.1: Lập trình Chức năng Nhập/Xuất/Kiểm kê & Sơ đồ Zone/Bin/Rack**

- **Mã WBS:** 1.3.1.1
- **Mô tả công việc:** Phát triển danh mục trà/nguồn gốc/ngày/hạn/quy cách, tự sinh Batch ID, ghi kết quả chất lượng lô, nhập–xuất–tồn/kiểm kê/điều chuyển và vị trí lưu trữ theo 01.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module Quản lý Kho Lõi (Core WMS).
- **Tiêu chí chấp nhận:** FR-01/FR-12 đạt AC-03, mã lô không trùng, số lượng/đơn vị/vị trí khớp tập đối soát.

**Gói công việc 1.3.1.2: Lập trình Thuật toán Xuất kho Ưu tiên FEFO**

- **Mã WBS:** 1.3.1.2
- **Mô tả công việc:** Gợi ý xuất ưu tiên lô còn hạn, được phép xuất có ngày hết hạn gần nhất theo 04.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module xử lý FEFO Logic.
- **Tiêu chí chấp nhận:** Đạt AC-03: đúng thứ tự lô còn hạn và không gợi ý xuất lô hết hạn trong tập kiểm.

**Gói công việc 1.3.2.1: Lập trình Công thức Quy đổi BOM theo Độ ẩm & Hao hụt Chè**

- **Mã WBS:** 1.3.2.1
- **Mô tả công việc:** Phát triển BOM/hao hụt theo công thức và kết quả độ ẩm trà do doanh nghiệp xác nhận; dữ liệu này nhập thủ công từ kiểm chất lượng, không lấy %RH môi trường thay thế.
- **Người chịu trách nhiệm:** Devs / BA
- **Sản phẩm đầu ra:** Module BOM & Processing Loss.
- **Tiêu chí chấp nhận:** Tính toán chính xác định mức chế biến trà theo công thức đã phê duyệt.

**Gói công việc 1.3.2.2: Phát triển cảnh báo tồn tối thiểu cận hạn hết hạn và Aging**

- **Mã WBS:** 1.3.2.2
- **Mô tả công việc:** Phát triển cảnh báo tồn dưới ngưỡng, cận hạn/hết hạn và báo cáo tuổi hàng theo ngưỡng/ngày được xác nhận trong SRS.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module Cảnh báo & Aging Report.
- **Tiêu chí chấp nhận:** FR-03 đạt AC-03 với ca trước/đúng/sau ngưỡng và hạn; cảnh báo hiển thị đúng trên màn hình.

**Gói công việc 1.3.2.3: Phát triển nhật ký nhiệt độ và độ ẩm môi trường**

- **Mã WBS:** 1.3.2.3
- **Mô tả công việc:** Nhập/lưu/tra cứu thủ công số đo môi trường từ thiết bị khách hàng sẵn có, gắn kho/khu vực/thời điểm/người ghi; lưu riêng số đo độ ẩm trà. Kênh đo không dây chỉ khảo sát như tùy chọn, không thuộc cam kết tích hợp hiện tại.
- **Người chịu trách nhiệm:** Devs / BA
- **Sản phẩm đầu ra:** Module nhật ký môi trường kho.
- **Tiêu chí chấp nhận:** FR-09 đạt AC-03; đủ trường và quyền nhập/tra cứu; không dùng %RH môi trường tính BOM.

**Gói công việc 1.3.3.1: Lập trình Service Kết nối RS232 Đọc Dữ liệu Cân Tự động**

- **Mã WBS:** 1.3.3.1
- **Mô tả công việc:** Phát triển dịch vụ cục bộ nhận dữ liệu từ bốn cân RS232 theo trạm của 02, chuyển số/đơn vị/trạng thái hợp lệ vào WMS.
- **Người chịu trách nhiệm:** RS232 Engineer
- **Sản phẩm đầu ra:** Windows Service IoT RS232 Connector.
- **Tiêu chí chấp nhận:** Đạt AC-01: dữ liệu hợp lệ khớp nguồn và từng mẫu cân <0,1%; xử lý lỗi/khôi phục theo bộ tình huống.

**Gói công việc 1.3.3.2: Phát triển tạo QR và kết nối máy in tem phiếu**

- **Mã WBS:** 1.3.3.2
- **Mô tả công việc:** Tạo QR/tem theo dữ liệu lô/ngày/trọng lượng đã xác nhận, kết nối bốn máy in theo giao thức tương thích; chứng từ văn phòng dùng máy in sẵn có hoặc đầu ra PDF theo SRS.
- **Người chịu trách nhiệm:** RS232 Engineer
- **Sản phẩm đầu ra:** Module tạo QR, in tem và xuất/in chứng từ.
- **Tiêu chí chấp nhận:** Đạt AC-02: từng tem <2 giây và nội dung/QR đúng; nhóm lỗi có xử lý đúng, không khóa hãng ở chương 2.

**Gói công việc 1.3.3.3: Lập trình Tích hợp Máy quét QR & Máy chấm công**

- **Mã WBS:** 1.3.3.3
- **Mô tả công việc:** Tích hợp tám scanner và ba máy chấm công do doanh nghiệp cung cấp theo đặc tả; đối soát dữ liệu chấm công với ca làm việc.
- **Người chịu trách nhiệm:** Devs / RS232 Engineer
- **Sản phẩm đầu ra:** Sub-module Barcode Scanner & Timekeeper Sync.
- **Tiêu chí chấp nhận:** FR-05/FR-06 đạt AC-03; không lẫn dữ liệu nhân viên, không nhập trùng sau đồng bộ.

**Gói công việc 1.3.3.4: Phát triển công cụ Excel danh mục lô và tồn đầu kỳ**

- **Mã WBS:** 1.3.3.4
- **Mô tả công việc:** Cung cấp công cụ nhập/xuất danh mục trà/nhà cung cấp/bao bì, lô và tồn đầu kỳ theo mẫu được xác nhận; không mặc nhiên chuyển toàn bộ lịch sử giao dịch.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Tool Import/Export Excel.
- **Tiêu chí chấp nhận:** TR-01 đạt AC-03: kiểm trường/đơn vị/mã lô, báo lỗi dòng/cột, đối soát số lượng và không nhập trùng.

**Gói công việc 1.3.4.1: Lập trình Dashboard KPI, Báo cáo Doanh thu & Giá vốn cho Lãnh đạo**

- **Mã WBS:** 1.3.4.1
- **Mô tả công việc:** Phát triển Dashboard và các báo cáo nhập–xuất–tồn, Aging, hao hụt, doanh thu/giá vốn, bán chạy/tồn lâu theo RTM.
- **Người chịu trách nhiệm:** Devs / Solution Architect
- **Sản phẩm đầu ra:** Module Executive Dashboard.
- **Tiêu chí chấp nhận:** FR-08/FR-13 đạt AC-03, bộ lọc và số tổng khớp tập đối soát.

**Gói công việc 1.3.4.2: Lập trình Module Quản lý Nhà cung cấp, Kế toán Kho & Tài xế**

- **Mã WBS:** 1.3.4.2
- **Mô tả công việc:** Phát triển nhà cung cấp/lịch sử nhập, đơn hàng xuất/trạng thái vận chuyển; chi phí nguyên liệu/đóng gói, công nợ và phí vận hành do người có quyền nhập hoặc lấy từ giao dịch. Logistics/đầu mối kho cập nhật biên bản giao nhận trên máy Windows.
- **Người chịu trách nhiệm:** Devs
- **Sản phẩm đầu ra:** Module Partner, Accounting & Transport Management.
- **Tiêu chí chấp nhận:** FR-07/FR-08 đạt AC-03 theo ca hợp lệ/không hợp lệ và đối soát tài chính/trạng thái.

**Gói công việc 1.3.4.3: Phát triển lịch ca và phân quyền vai trò**

- **Mã WBS:** 1.3.4.3
- **Mô tả công việc:** Quản lý ca làm việc và quyền thao tác/tra cứu theo sáu nhóm người dùng; liên kết dữ liệu chấm công từ module đã có.
- **Người chịu trách nhiệm:** Devs / BA
- **Sản phẩm đầu ra:** Module lịch ca và phân quyền.
- **Tiêu chí chấp nhận:** FR-10 đạt AC-03, có ca cho phép và từ chối của mỗi vai trò; chấm công đối soát.

**Gói công việc 1.3.4.4: Phát triển danh mục tài sản dụng cụ và vật tư**

- **Mã WBS:** 1.3.4.4
- **Mô tả công việc:** Quản lý danh mục kệ/khu vực, máy móc/dụng cụ và vật tư bao bì/tem theo 01; không mua thêm tài sản vật lý ngoài danh mục 02.
- **Người chịu trách nhiệm:** Devs / BA
- **Sản phẩm đầu ra:** Module danh mục tài sản/dụng cụ/vật tư.
- **Tiêu chí chấp nhận:** FR-11 đạt AC-03: nhập/tra cứu/cập nhật theo quyền và dữ liệu đối soát.

**Gói công việc 1.3.5.1: Kiểm thử Luồng Dữ liệu Cân RS232 đến Web App**

- **Mã WBS:** 1.3.5.1
- **Mô tả công việc:** Từ tháng 3, QA/RS232 kiểm bộ mẫu và dữ liệu thực trên cân đã nhận; kiểm từng cân tại kho trước sử dụng. Mô phỏng bổ trợ nhóm lỗi, không thay phép cân đối chuẩn.
- **Người chịu trách nhiệm:** QA / RS232 Engineer
- **Sản phẩm đầu ra:** Báo cáo Integration Test - RS232 Data Flow.
- **Tiêu chí chấp nhận:** AC-01 có kết quả từng ca; mọi mẫu hợp lệ <0,1%, nguồn/WMS khớp, nhóm lỗi được xử lý đúng.

**Gói công việc 1.3.5.2: Kiểm thử in tem và chức năng theo RTM**

- **Mã WBS:** 1.3.5.2
- **Mô tả công việc:** Kiểm AC-02 và AC-03, gồm FEFO/BOM, nhật ký môi trường, ca/quyền, tài sản và báo cáo; kiểm từng máy in trước sử dụng tại kho.
- **Người chịu trách nhiệm:** QA / Devs
- **Sản phẩm đầu ra:** Báo cáo Integration Test - Performance & Business Logic.
- **Tiêu chí chấp nhận:** Từng tem thuộc tập AC-02 <2 giây và đúng nội dung; các ca chức năng/phân quyền/biên theo AC-03 đạt, lưu lỗi và kết quả kiểm lại.

### M3–M4 Triển khai và vận hành kho tổng (tháng 5–6)

**Gói công việc 1.4.1.1: Lắp đặt PC, Trạm Cân RS232, Máy in theo chuẩn tương thích, Máy quét tại Kho Tổng**

- **Mã WBS:** 1.4.1.1
- **Mô tả công việc:** Lắp hai PC, hai cân RS232, hai máy in và bốn scanner mua mới tại kho tổng; kết nối một máy chấm công sẵn có và các đầu cuối văn phòng do doanh nghiệp cung cấp.
- **Người chịu trách nhiệm:** Onsite Engineer / RS232 Engineer
- **Sản phẩm đầu ra:** Hạ tầng phần cứng hoàn chỉnh tại Kho tổng Thái Nguyên.
- **Tiêu chí chấp nhận:** Danh mục/vị trí khớp 02, phụ kiện và nguồn tài sản sẵn có được xác nhận; kết nối/cấu hình LAN–ngoại vi–WMS thông suốt, đạt bộ kiểm trước vận hành.

**Gói công việc 1.4.1.2: Xây dựng Kịch bản UAT & Hướng dẫn 6 Nhóm Người dùng Thử nghiệm**

- **Mã WBS:** 1.4.1.2
- **Mô tả công việc:** Lập tài liệu Test Case UAT và hướng dẫn trực tiếp Chị Đại diện Kho tổng, thủ kho, công nhân Thái Nguyên thao tác thử nghiệm.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú / BA / Onsite Engineer
- **Sản phẩm đầu ra:** Kịch bản UAT & Biên bản UAT Nội bộ Kho tổng.
- **Tiêu chí chấp nhận:** Được đại diện người dùng Kho tổng ký nghiệm thu UAT.

**Gói công việc 1.4.1.3: Khởi tạo Dữ liệu Danh mục Trà Ban đầu từ File Excel**

- **Mã WBS:** 1.4.1.3
- **Mô tả công việc:** Kiểm/import danh mục trà/nhà cung cấp/bao bì, lô và tồn đầu kỳ từ Excel chuẩn hóa của doanh nghiệp vào môi trường chạy thử; đối soát trước chuyển production.
- **Người chịu trách nhiệm:** Onsite Engineer / BA
- **Sản phẩm đầu ra:** CSDL Kho tổng được khởi tạo đầy đủ dữ liệu ban đầu.
- **Tiêu chí chấp nhận:** TR-01 đạt AC-03; dữ liệu mở kho/lô/vị trí/đơn vị và số lượng khớp bảng doanh nghiệp xác nhận.

**Gói công việc 1.4.1.4: Đào tạo vận hành kho tổng trước go-live**

- **Mã WBS:** 1.4.1.4
- **Mô tả công việc:** Onsite/BA hướng dẫn người dùng kho tổng theo vai trò trên SOP/User Manual trước vận hành; BA bàn giao tài liệu và đầu mối cập nhật cho Onsite/PM trước cuối tháng 5. Hướng dẫn tham gia UAT không tự thay hồ sơ đào tạo vận hành.
- **Người chịu trách nhiệm:** Onsite Engineer / BA / PM
- **Sản phẩm đầu ra:** Tài liệu đào tạo đủ dùng, danh sách người học và kết quả thực hành theo vai trò.
- **Tiêu chí chấp nhận:** TR-02 đạt AC-04 trước go-live kho tổng; tháng 8 chỉ đào tạo bổ sung/hoàn thiện bàn giao.

**Gói công việc 1.4.2.1: Triển khai production và chuyển dữ liệu mở kho**

- **Mã WBS:** 1.4.2.1
- **Mô tả công việc:** Tech Lead/Backend triển khai ứng dụng/CSDL, cấu hình kết nối với dịch vụ ngoại vi, kiểm sao lưu/khôi phục và chuyển danh mục/lô/tồn đầu kỳ đã đối soát; loại dữ liệu thử. Gói cloud theo tám tháng 02.
- **Người chịu trách nhiệm:** Solution Architect / Backend Developer
- **Sản phẩm đầu ra:** Môi trường production, dữ liệu mở kho, bản sao lưu và hướng dẫn vận hành đủ dùng.
- **Tiêu chí chấp nhận:** NFR-01/TR-01 đạt AC-04; khôi phục thử có biên lai và dữ liệu đối soát; môi trường/thiết bị đã đạt trước xác nhận go-live.

**Gói công việc 1.4.2.2: Đưa kho tổng vào vận hành chậm nhất cuối tháng 6**

- **Mã WBS:** 1.4.2.2
- **Mô tả công việc:** Kích hoạt sử dụng chính thức sau khi dữ liệu, ngoại vi và người dùng đạt AC-01–AC-04; không gắn mốc với một mùa vụ chưa có căn cứ.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú & Onsite Engineer
- **Sản phẩm đầu ra:** Biên bản Xác nhận Go-live Kho Tổng Thái Nguyên.
- **Tiêu chí chấp nhận:** Kho tổng vận hành thực tế chậm nhất 02/12/2027; có hồ sơ đạt, người dùng được đào tạo trước sử dụng và xác nhận của chủ đầu tư/đại diện kho.

**Gói công việc 1.4.2.3: Thực hiện hỗ trợ kỹ thuật trực tiếp tại Thái Nguyên**

- **Mã WBS:** 1.4.2.3
- **Mô tả công việc:** Túc trực trực tiếp tại Kho tổng Thái Nguyên trong 2 tuần đầu Go-live để xử lý sự cố phát sinh.
- **Người chịu trách nhiệm:** Onsite Engineer / RS232 Engineer
- **Sản phẩm đầu ra:** Báo cáo nhật ký hỗ trợ Go-live (Onsite Support Log).
- **Tiêu chí chấp nhận:** Có đầu mối tiếp nhận, phân loại và nhật ký xử lý sự cố theo mức ảnh hưởng; không cam kết mọi sự cố được giải quyết trong 15 phút. Điều kiện hỗ trợ cụ thể trong kế hoạch chất lượng/giao tiếp.

### M5 Triển khai hai chi nhánh (tháng 7)

**Gói công việc 1.5.1.1: Lắp đặt Phần cứng & Thiết bị tại 02 Kho Chi nhánh Phân phối**

- **Mã WBS:** 1.5.1.1
- **Mô tả công việc:** Mỗi chi nhánh lắp một PC, một cân, một máy in và hai scanner mua mới; kết nối một máy chấm công sẵn có/kho. Tổng hai chi nhánh: hai PC, hai cân, hai máy in, bốn scanner, hai máy chấm công khách hàng cung cấp.
- **Người chịu trách nhiệm:** Onsite Engineer
- **Sản phẩm đầu ra:** Bàn giao hạ tầng phần cứng hoàn chỉnh tại 02 Kho chi nhánh.
- **Tiêu chí chấp nhận:** Danh mục khớp 02 và giả định 01; tại mỗi kho, AC-01/AC-02 và kết nối đầu cuối đạt trước sử dụng.

**Gói công việc 1.5.2.1: Thiết lập đồng bộ dữ liệu ba kho và đệm ngoại tuyến**

- **Mã WBS:** 1.5.2.1
- **Mô tả công việc:** Triển khai đồng bộ/đệm theo SAD và phạm vi nghiệp vụ offline trong SRS; không khóa mô hình ba CSDL nhân bản chỉ vì có ba kho.
- **Người chịu trách nhiệm:** Solution Architect / Devs
- **Sản phẩm đầu ra:** Hệ thống CSDL Đồng bộ 3 Kho (Multi-site Database Sync).
- **Tiêu chí chấp nhận:** NFR-02 đạt AC-03: ngắt/khôi phục mạng, đối soát dữ liệu và xử lý trùng/xung đột theo SRS; không tự giảm yêu cầu ngoại tuyến.

**Gói công việc 1.5.3.1: Đào tạo Thao tác Phần mềm cho Thủ kho & Nhân sự 2 Chi nhánh**

- **Mã WBS:** 1.5.3.1
- **Mô tả công việc:** Tổ chức các lớp hướng dẫn sử dụng phần mềm, quét mã QR kiểm kê, nhận hàng điều chuyển cho nhân sự tại 02 chi nhánh.
- **Người chịu trách nhiệm:** Onsite Engineer / PM (tiếp nhận tài liệu BA trước cuối tháng 5)
- **Sản phẩm đầu ra:** Báo cáo kết quả đào tạo & Danh sách điểm danh.
- **Tiêu chí chấp nhận:** Người sử dụng chi nhánh được hướng dẫn trước vận hành và thực hành ca theo vai trò, lưu danh sách/kết quả theo AC-04.

### M6 Tổng hợp nghiệm thu và bàn giao (tháng 8)

**Gói công việc 1.6.1.1: Đo đạc Sai số Cân Tự động qua RS232**

- **Mã WBS:** 1.6.1.1
- **Mô tả công việc:** QA/Tech Lead tổng hợp biên lai từng cân đã nghiệm thu trước vận hành; kiểm lại delta thiết bị/phần mềm nếu thay đổi. RS232 bàn giao đặc tả/hồ sơ trước kết thúc tháng 7.
- **Người chịu trách nhiệm:** QA / Solution Architect
- **Sản phẩm đầu ra:** Biên bản kiểm định Tiêu chí Cân tự động.
- **Tiêu chí chấp nhận:** Đủ hồ sơ AC-01 cho bốn cân; mỗi phép cân hợp lệ trong tập <0,1% và nhóm tình huống đạt; không dùng số trung bình thay điều kiện từng mẫu.

**Gói công việc 1.6.1.2: Tổng hợp nghiệm thu tạo và in tem**

- **Mã WBS:** 1.6.1.2
- **Mô tả công việc:** QA/Tech Lead tổng hợp biên lai bốn máy in trước sử dụng, kiểm lại phần thay đổi nếu có; RS232 bàn giao hồ sơ trước cuối tháng 7.
- **Người chịu trách nhiệm:** QA / Solution Architect
- **Sản phẩm đầu ra:** Biên bản kiểm định Tiêu chí In tem theo chuẩn tương thích.
- **Tiêu chí chấp nhận:** Đủ hồ sơ AC-02: 30 tem/máy, từng tem <2 giây, QR/nội dung đúng và nhóm lỗi đạt.

**Gói công việc 1.6.2.1: Hoàn thiện Bộ Tài liệu Dự án**

- **Mã WBS:** 1.6.2.1
- **Mô tả công việc:** PM/Onsite đóng gói SRS, SAD, SOP, User Manual và hướng dẫn vận hành/sao lưu; dùng bản BA bàn giao tháng 5, cập nhật thay đổi bởi vai trò còn tham gia. Tech Lead/Backend phụ trách phần kỹ thuật.
- **Người chịu trách nhiệm:** PM / Onsite Engineer / Solution Architect
- **Sản phẩm đầu ra:** Bộ hồ sơ tài liệu dự án hoàn chỉnh (Project Documentation Package).
- **Tiêu chí chấp nhận:** TR-02/TR-03 đạt AC-04; bộ tài liệu đúng phiên bản, phản ánh thực tế bàn giao, không mặc định BA làm thêm tháng 8.

**Gói công việc 1.6.3.1: Ký Biên bản UAT & Nghiệm thu Tổng thể với Project Sponsor**

- **Mã WBS:** 1.6.3.1
- **Mô tả công việc:** Tổ chức họp tổng kết với Ban Giám đốc Doanh nghiệp Trà Tân Cương, trình bày kết quả vận hành 3 kho và tiến hành ký Biên bản Nghiệm thu Tổng thể.
- **Người chịu trách nhiệm:** PM Bùi Hồng Phú
- **Sản phẩm đầu ra:** Biên bản Nghiệm thu Tổng thể Dự án (Final Acceptance Sign-off).
- **Tiêu chí chấp nhận:** Chủ đầu tư, đại diện các kho và PM xác nhận sản phẩm/bộ điều kiện AC-01–AC-04, theo trách nhiệm ở 04.

**Gói công việc 1.6.3.2: Bàn giao Hệ thống và Đóng Dự án**

- **Mã WBS:** 1.6.3.2
- **Mô tả công việc:** Bàn giao gói phần mềm/hồ sơ triển khai, CSDL, tài khoản quản trị, sao lưu/biên lai khôi phục và hướng dẫn vận hành cho đầu mối doanh nghiệp; xác nhận trách nhiệm chi phí sau tháng 8, hoàn tất thanh toán/đóng dự án. Bảo trì dài hạn là thỏa thuận riêng.
- **Người chịu trách nhiệm:** PM / Solution Architect / Backend Developer
- **Sản phẩm đầu ra:** Hồ sơ bàn giao vận hành và báo cáo đóng dự án.
- **Tiêu chí chấp nhận:** TR-03 đạt AC-04, đầu mối doanh nghiệp ký nhận và trách nhiệm phí duy trì được ghi rõ, bàn giao toàn bộ chậm nhất 02/02/2028.

## 6. Xác nhận và kiểm soát phạm vi

### 6.1 Nghiệm thu theo đầu ra và mốc

1. QA/PM kiểm nội bộ phần bàn giao theo RTM và AC-01–AC-04, lưu kết quả từng ca/lỗi/kiểm lại; lịch kiểm xác định ở chương 3, không tự áp năm ngày cố định cho mọi mốc.
2. Đội dự án gửi sản phẩm và hồ sơ cho chủ đầu tư/đại diện kho liên quan, gồm kết quả kiểm, tài liệu và điểm chưa đạt nếu có.
3. Người dùng thực hiện UAT theo vai trò, đối soát dữ liệu/thiết bị. Phương án nhập môi trường thủ công được kiểm; khả năng nhận đo không dây không phải điều kiện đạt của đường cơ sở hiện tại.
4. Chủ đầu tư, PM và đại diện kho liên quan xác nhận bàn giao từng phần/tổng thể theo 04; phần chưa đạt được sửa và kiểm lại, không ký đạt chỉ vì đủ biểu mẫu.

| Mốc | Hạn hoàn thành | Đầu ra | Điều kiện chấp nhận | Đầu mối xác nhận |
| --- | --- | --- | --- | --- |
| M1 | 02/07/2027, cuối tháng 1 | SRS/SAD, yêu cầu dải cân/tem, danh mục tài sản và phương án triển khai | RTM phủ 01–04; các tham số dùng để kiểm AC được xác nhận; giới hạn offline rõ; không khóa hãng/nhân bản CSDL khi chưa có căn cứ | Chủ đầu tư/PM, đầu mối kho xác nhận nghiệp vụ |
| M2 | 02/10/2027, cuối tháng 4 | Core WMS, kết nối ngoại vi và các chức năng bổ trợ trong RTM | AC-01/AC-02 trên bộ mẫu đã nhận; AC-03 trên tập dữ liệu; chưa dùng mẫu để kết luận thiết bị chưa nhận đã đạt | PM/đầu mối kỹ thuật |
| M3 | 02/11/2027, cuối tháng 5 | Kho tổng: 2 PC, 2 cân, 2 máy in, 4 scanner và 1 máy chấm công sẵn có; UAT/đào tạo | AC-01/AC-02 cho thiết bị kho tổng, AC-03 và đào tạo AC-04; dữ liệu mở kho đối soát | Đại diện kho tổng/PM |
| M4 | 02/12/2027, chậm nhất cuối tháng 6 | Production và vận hành kho tổng | Môi trường, dữ liệu danh mục/lô/tồn, ngoại vi và người dùng sẵn sàng theo AC-04; kiểm lại delta nếu khác cấu hình đã đạt | Chủ đầu tư/đại diện kho tổng/PM |
| M5 | 02/01/2028, cuối tháng 7 | Mỗi chi nhánh: 1 PC, 1 cân, 1 máy in, 2 scanner, 1 máy chấm công sẵn có; dữ liệu/đào tạo | AC-01/AC-02 từng thiết bị chi nhánh; AC-03 đồng bộ/ngoại tuyến; AC-04 đào tạo trước sử dụng | Hai đại diện chi nhánh/PM |
| M6 | 02/02/2028, cuối tháng 8 | Toàn bộ phần mềm, dữ liệu, tài liệu và hồ sơ vận hành/bàn giao | Tổng hợp AC-01–AC-04, kiểm lại phần thay đổi; đầu mối nhận quản trị/phí duy trì được xác nhận | Chủ đầu tư/đại diện các kho/PM; đơn vị thi công bàn giao |

### 6.2 Kiểm soát thay đổi

Áp dụng quy trình mục 1.2; ghi CR, tác động, người duyệt và phiên bản yêu cầu/WBS/tiêu chí/kế hoạch được cập nhật. PM không tự duyệt bỏ chức năng hoặc thay tiêu chí dưới hạn mức ngân sách. Thay đổi chưa được duyệt không được thực hiện. Đề xuất ngoài phạm vi có thể được ghi nhận cho thỏa thuận sau dự án, không tự thành cam kết của giai đoạn hiện tại.

Theo dõi độ phủ yêu cầu và các thay đổi được duyệt bằng RTM/change log. Không dùng số gói hoàn thành để đo biến động phạm vi, không giới hạn số CR tùy ý hoặc coi mọi CR được trả từ 143 triệu. Sửa thiếu sót của yêu cầu đã có phải ước lượng và đối chiếu ngân sách/nguồn lực; chương chi phí/rủi ro xác định căn cứ dự phòng.

### Nguồn đối chiếu

- [01 Mô tả](01-mo-ta-de-tai.md), [02 Dự toán](02-du-toan-kinh-phi.md), [03 Tôn chỉ cơ sở](03-ton-chi-du-an.md), [04 Tôn chỉ đầy đủ](04-ton-chi-du-an-day-du.md).
- Slide `4-scope.pdf`: trang 14 kế hoạch phạm vi, 16–19 yêu cầu/RTM/tuyên bố, 28–32 phân rã, 38 WBS theo pha, 39–41 nghiệm thu/kiểm soát/bài tập. Nguồn này do nhóm chia sẻ cùng tài liệu học, không giả lập link khi chưa có trong repo.
- PMBOK 6: §5.2.3.2 RTM (trang in 148–149), §5.3.3.1 phạm vi/tiêu chí (154–155), §5.4.3.1 WBS/Dictionary và quy tắc 100% (161–162). Bộ mẫu AC là lựa chọn lập kế hoạch cho tình huống, không phải con số được giáo trình ấn định.
