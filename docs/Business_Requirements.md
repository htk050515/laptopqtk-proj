# PHÂN TÍCH YÊU CẦU NGHIỆP VỤ (BUSINESS REQUIREMENTS)

## 1. Mục tiêu hệ thống

Hệ thống Website bán Laptop và Linh kiện Laptop được xây dựng nhằm:

* Cung cấp nền tảng bán laptop và linh kiện trực tuyến cho khách hàng
* Hỗ trợ người dùng tìm kiếm, lựa chọn và mua sản phẩm thuận tiện
* Hỗ trợ quản trị viên và nhân viên quản lý sản phẩm, đơn hàng hiệu quả
* Đảm bảo phân quyền rõ ràng, bảo mật dữ liệu và khả năng mở rộng

---

## 2. Phạm vi hệ thống

### 2.1 Phạm vi bao gồm

* Website thương mại điện tử bán laptop và linh kiện
* Hệ thống quản lý người dùng và phân quyền
* Hệ thống quản lý sản phẩm và đơn hàng

### 2.2 Phạm vi không bao gồm

* Thanh toán trực tuyến qua cổng ngân hàng (chỉ mô phỏng hoặc COD)
* Quản lý kho nâng cao theo thời gian thực
* Tích hợp vận chuyển bên thứ ba

---

## 3. Các yêu cầu nghiệp vụ chính

### 3.1 Quản lý người dùng

* Cho phép khách truy cập đăng ký tài khoản
* Cho phép người dùng đăng nhập và đăng xuất
* Phân quyền người dùng theo vai trò: Guest, Customer, Staff, Admin
* Cho phép Admin quản lý tài khoản người dùng

### 3.2 Quản lý sản phẩm

* Hiển thị danh sách laptop và linh kiện
* Phân loại sản phẩm theo danh mục
* Xem chi tiết sản phẩm (giá, mô tả, hình ảnh, thông số kỹ thuật)
* Cho phép Staff và Admin thêm, chỉnh sửa sản phẩm
* Chỉ Admin được phép xóa sản phẩm

### 3.3 Quản lý giỏ hàng và đơn hàng

* Customer có thể thêm sản phẩm vào giỏ hàng
* Customer có thể đặt hàng và thanh toán
* Customer có thể xem lịch sử đơn hàng cá nhân
* Staff và Admin có thể xem danh sách đơn hàng
* Staff và Admin cập nhật trạng thái đơn hàng

---

## 4. Yêu cầu phi chức năng

* Hệ thống hoạt động ổn định và phản hồi nhanh
* Giao diện thân thiện, hỗ trợ đa thiết bị (Responsive)
* Bảo mật thông tin người dùng và dữ liệu hệ thống
* Phân quyền và kiểm soát truy cập ở Backend
* Dễ bảo trì và mở rộng trong tương lai

---

## 5. Đối tượng sử dụng hệ thống

* Guest – Khách truy cập chưa đăng nhập
* Customer – Khách hàng đã đăng ký
* Staff – Nhân viên quản lý
* Admin – Quản trị viên hệ thống

---

**Tài liệu:** Business_Requirements.md
**Thuộc repository:** `laptopqtk-proj`
