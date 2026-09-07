# N-02 · Cách làm việc

**Ae tự làm phần mình bằng Markdown, gửi lên GitHub để đọc chéo; Hưng duyệt và ghép bản cuối (tạm quyết định thế).** Không cần cùng online hay ngồi viết chung một file.

## 1. Khi nhận việc

Thống nhất ba điều: **làm ra gì, dùng đầu vào nào, dự kiến khi nào bàn giao**. Người nhận tự cân đối lịch của mình rồi xác nhận với nhóm.

Giao một bảng hoặc một phần đủ dùng trước cũng được. Ví dụ, ae làm thời gian cần danh sách công việc để lập lịch, không cần đợi chương phạm vi viết xong toàn bộ.

## 2. Khi làm và gửi bài

1. Lấy bản mới nhất từ `main`, tạo nhánh riêng cho phần việc.
2. Viết file Markdown; bảng tính và hình có file nguồn đi kèm.
3. Commit, push nhánh rồi mở **pull request (PR)** — đề nghị đưa phần sửa vào bản chung.
4. Một người đọc chéo, người viết xử lý góp ý; Ae có thể yêu cầu Hưng hoặc các thành viên khác duyệt hoặc tự merge vào `main` rồi báo nhóm.

Trong PR, ghi ngắn: **đã làm gì, cần ae xem gì, còn vướng gì**. Chưa hoàn thiện thì ghi rõ là bản nháp. Phần Hưng viết cũng cần ae đọc chéo.

Repo là nơi giữ bản chính. Ba tài liệu [Mô tả](01-mo-ta-de-tai.md), [Dự toán](02-du-toan-kinh-phi.md), [Tôn chỉ](03-ton-chi-du-an.md) đã được thống nhất; nếu thấy cần đổi, nêu vấn đề trước khi sửa dữ liệu gốc.

## 3. Deadline và việc bị chậm

**Ae tự chọn lúc làm, nhưng cần thống nhất lúc bàn giao.** Mốc dự kiến phải sớm hơn lúc phần sau cần dùng, để còn thời gian đọc, sửa và xử lý trục trặc. Khoảng chừa đó là buffer.

Nếu thấy có thể trễ, báo sớm: đã có gì, còn thiếu gì, đang chờ ai và đề xuất mốc mới. Không cần chờ đến deadline mới báo. Nhóm sẽ điều chỉnh phần bàn giao hoặc người hỗ trợ theo ảnh hưởng thực tế.

Không bắt buộc họp sau mỗi buổi học. Ae phụ trách phần nào thì cập nhật yêu cầu mới liên quan phần đó; có ảnh hưởng phần khác thì trao đổi với người phụ trách. Chỉ họp khi trao đổi viết chưa giải quyết được.

## 4. Khi ghép báo cáo

**Ghép thử sớm, chỉnh trình bày ở cuối.** Nhóm sẽ thử xuất một phần nhỏ có chữ, bảng, hình và công thức để biết cách xuất có dùng được không. Công cụ và template cụ thể chưa chọn.

Khi nội dung đã ổn, Hưng thống nhất format và ghép PDF. Ae vẫn sửa và chịu trách nhiệm phần mình, đồng thời chuẩn bị slide và tập trình bày. Bản PDF phải ghi rõ đóng góp của từng người và được gửi trước ngày báo cáo **23/11**.

Xem [phân công và việc tiếp theo](N-03-phan-cong-va-quyet-dinh.md). Nếu chưa rõ một phần cần làm ra gì, quay lại [Khung BTL](N-01-khung-btl.md).

---

## Phụ lục · Quy cách chi tiết để kiểm tra

<details>
<summary>Ae không cần đọc hết phần này để bắt đầu. Hưng, người review hoặc AI có thể dùng để kiểm tra phần việc.</summary>

### File và Markdown

- Nội dung BTL dùng các file gốc `01–03`; hướng dẫn nhóm dùng `N-01` đến `N-03`. Khi viết chương, tổ chức theo chương/sản phẩm thay vì chỉ chia thư mục theo tên người.
- Các thư mục dự kiến: `bao-cao/` cho chương Markdown; `du-lieu/` cho bảng nguồn; `hinh/` cho hình và file chỉnh sửa; `xuat-ban/` cho cấu hình/thứ tự ghép và bản xuất. Chưa có nghĩa các thư mục hoặc pipeline này đã tồn tại.
- File UTF-8, tên không dấu có nghĩa; một tiêu đề `#`, các mục `##`/`###` theo thứ bậc. Đầu file ghi người làm, người đọc chéo đã nhận việc, trạng thái và đầu vào đang dùng.
- Liên kết tương đối; không dùng đường dẫn máy cá nhân. Khi đổi tên/di chuyển file phải tìm và sửa mọi tham chiếu.
- Bảng có đơn vị và cách tính. Phần viết mới dùng dấu chấm phân tách hàng nghìn, dấu phẩy phân tách thập phân; nếu theo quy ước khác của nguồn thì chú thích. Trong bảng “triệu VNĐ”, `1.667` nghĩa là một nghìn sáu trăm sáu mươi bảy triệu.
- Hình có chú thích, nguồn và bản sửa được; bảng tính có dữ liệu/công thức để tính lại, không chỉ có ảnh chụp. Kiểm cả cách hiển thị trong bản xuất thử.
- Thuật ngữ viết tắt được giải thích khi dùng. Dùng “Tôn chỉ dự án”, “Người quản lý dự án (PM)”. Chưa thống nhất thì không tự áp một hệ mã công việc mới.
- Mã công việc giữ ổn định. Nếu đổi cấu trúc, có ánh xạ mã cũ/mới và chỉ rõ phần chịu ảnh hưởng. Bảng lặp lại số liệu phải dẫn nguồn và được đối chiếu khi nguồn đổi.

### Mẫu thông tin của một việc

| Cần ghi | Nội dung |
| --- | --- |
| Đầu ra | File/bảng/sơ đồ cần bàn giao; thế nào là đủ dùng |
| Đầu vào | Tài liệu, mục và phiên bản; câu hỏi còn mở |
| Người làm / đọc chéo | Người đã xác nhận nhận vai |
| Phạm vi | Điều được sửa và điều cần xin quyết định trước |
| Mốc dự kiến | Người làm dự kiến bàn giao lúc nào |
| Mốc báo nguy cơ | Muộn nhất lúc nào cần báo khả năng trễ; phát hiện sớm thì báo ngay |
| Ngày cần đầu vào | Khi nào người phụ thuộc cần bản đã đủ dùng |

Giờ công khác thời gian lịch. Buffer phải chừa đủ đọc và sửa giữa các lần bàn giao; ngoài ra có khoảng riêng cho ghép bài, sửa lỗi, PDF, slide và tập trình bày. Các mốc và độ dài buffer chưa được nhóm xác nhận thì không ghi thành deadline đã chốt.

Việc được theo dõi bằng issue hoặc PR sau khi tạo; bảng phân công dẫn tới nơi đang dùng. Không để hai bảng deadline khác nhau cùng có hiệu lực hoặc tạo link đến issue chưa tồn tại.

### Thay đổi, Git và review

- Mỗi PR tập trung một đầu ra/nhóm thay đổi liên quan. Không ghi đè bản mới bằng bản cũ; không tự sửa phần người khác đang làm. Không force-push `main`, xóa lịch sử hoặc nhánh của người khác.
- Quy trình PR ở trên là quy ước nhóm, chưa phải xác nhận branch protection đã bật. Các lượt thiết lập và chỉnh tài liệu theo duyệt trực tiếp của Hưng có thể theo phạm vi commit/push Hưng giao; không thay quy trình thường lệ của ae.
- Người viết sửa sau review; Hưng duyệt tích hợp. Trạng thái: đang làm → chờ review → cần sửa (nếu có) → đã duyệt. Bị chặn thì ghi điều kiện cần giải quyết.
- Kiểm: đúng yêu cầu/phạm vi, nguồn rõ, phép tính đúng, link mở được, nội dung dễ hiểu, không mâu thuẫn phần khác, không thiếu đầu vào/bàn giao. Có đủ tiêu đề hoặc số trang chưa có nghĩa đã xong.
- Sửa sai phép tính theo dữ liệu gốc được giữ cố định. Đổi lương, lịch tham gia, ngân sách hoặc phạm vi đã chốt phải đưa ra quyết định trước. Khi hai nguồn khác nhau, ghi vấn đề và dừng phần phụ thuộc, không tự chọn số tiện dùng.
- Yêu cầu mới của thầy phải ghi nguồn và ảnh hưởng; việc chưa có người phụ trách do Hưng ghi nhận để phân tiếp. Quyết định nhóm không đổi được yêu cầu của thầy. Thay quyết định phải giữ dấu vết: ai chốt, vì sao, thay điều nào, ảnh hưởng đâu.
- T3/AI chỉ có kết luận trong phạm vi đã kiểm, theo phiên bản cụ thể; không thay người viết chịu trách nhiệm, nhóm chốt việc hay thầy chấp nhận bài. Quy định AI của thầy vẫn áp dụng; xem phụ lục Khung BTL.

### Trước khi xuất và nộp

- Chín chương đúng thứ tự, đóng góp từng người rõ; số liệu và nguồn khớp; PDF/slide nhất quán; bảng/hình/mục lục đọc được; ae đã chuẩn bị trình bày.
- Ghi commit nguồn và danh sách file được ghép. Không tự ghép file `N-` hoặc ghi chú review vào bài nộp. Bản đã xuất/nộp là snapshot, không đồng bộ ngược thành bản gốc để sửa song song.
- Đối chiếu người gửi, email/cú pháp và mốc nội bộ từ hướng dẫn môn trước khi gửi. Agent chưa được giao gửi email hay thông báo cho nhóm.
- Chưa xuất thử thì không nói pipeline đã chạy được. Không có CI hoặc chưa chạy thì ghi đúng; kiểm tài liệu không chứng minh dự án phần mềm đã thực thi.

### Nguồn

[Khung BTL](N-01-khung-btl.md) dẫn tên slide/trang. Quy cách GitHub, Markdown, đọc chéo, buffer và ghép thử là các quyết định tổ chức đã được Hưng đồng ý ngày 06/09/2026. Hướng dẫn thao tác tham khảo: [GitHub — PR review](https://docs.github.com/en/pull-requests/reference/pull-request-reviews).

</details>
