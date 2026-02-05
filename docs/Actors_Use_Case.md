# XÁC ĐỊNH ACTOR & USE CASE DIAGRAM

## 1. Mục đích tài liệu

Tài liệu này xác định các **Actor** và **Use Case** của hệ thống Website bán Laptop và Linh kiện Laptop, làm cơ sở để thiết kế Authorization và Business Flow.

---

## 2. Xác định Actor

| Actor    | Mô tả                                                |
| -------- | ------------------------------------------------------ |
| Guest    | Người truy cập hệ thống nhưng chưa đăng nhập |
| Customer | Người dùng đã đăng ký tài khoản              |
| Staff    | Nhân viên quản lý vận hành hệ thống            |
| Admin    | Quản trị viên toàn hệ thống                      |

---

## 3. Danh sách Use Case theo Actor

### 3.1 Guest

* Xem trang chủ
* Xem danh sách sản phẩm
* Xem chi tiết sản phẩm
* Đăng ký tài khoản
* Đăng nhập

### 3.2 Customer

* Đăng nhập / đăng xuất
* Cập nhật thông tin cá nhân
* Thêm sản phẩm vào giỏ hàng
* Đặt hàng / thanh toán
* Xem lịch sử đơn hàng cá nhân

### 3.3 Staff

* Đăng nhập hệ thống
* Thêm và cập nhật sản phẩm
* Xem danh sách đơn hàng
* Cập nhật trạng thái đơn hàng

### 3.4 Admin

* Đăng nhập hệ thống
* Quản lý người dùng
* Quản lý sản phẩm (thêm / sửa / xóa)
* Quản lý đơn hàng
* Truy cập trang quản trị (Django Admin)

---

## 4. Quan hệ giữa các Actor

* Customer kế thừa toàn bộ quyền của Guest
* Admin kế thừa toàn bộ quyền của Staff
* Staff và Admin là actor nội bộ, không tham gia mua hàng

---

## 5. Mô tả Use Case Diagram (logic)

* Guest có thể chuyển thành Customer thông qua use case Đăng ký
* Customer thực hiện các use case mua hàng độc lập
* Staff và Admin xử lý nghiệp vụ quản trị hệ thống

---

## 6. Kết luận

Việc xác định đúng Actor và Use Case giúp hệ thống được thiết kế đúng nghiệp vụ, tránh chồng chéo chức năng và hỗ trợ tốt cho các bước thiết kế tiếp theo.

---

**Tài liệu:** Actors_Use_Case.md
**Thuộc repository:** `laptopqtk-proj`
