# AUTHORIZATION & ACCESS CONTROL DESIGN

## 1. Mục đích tài liệu

Tài liệu này mô tả **cơ chế phân quyền và kiểm soát truy cập (Authorization)** trong dự án  **Website bán Laptop và Linh kiện Laptop** . Nội dung nhằm làm rõ cách hệ thống xác định  **ai được phép truy cập chức năng nào** , đảm bảo tính **bảo mật, toàn vẹn dữ liệu** và  **đúng nghiệp vụ thương mại điện tử** .

Tài liệu được sử dụng cho:

* Tham khảo khi phát triển Backend (Django + DRF)
* Thống nhất giữa Backend và Frontend
* Đưa vào báo cáo đồ án và repository GitHub

---

## 2. Tổng quan mô hình phân quyền

Hệ thống áp dụng mô hình  **Role-Based Access Control (RBAC)** , trong đó quyền truy cập được gán dựa trên  **vai trò người dùng (Role)** .

### Các nguyên tắc chính:

* Mỗi người dùng chỉ có **một vai trò chính** tại một thời điểm
* API Backend kiểm soát quyền truy cập ở mức **endpoint**
* Frontend chỉ hiển thị chức năng tương ứng với quyền đã được cấp
* Mọi truy cập trái phép đều bị từ chối ở Backend

---

## 3. Các vai trò trong hệ thống

### 3.1 Admin (Quản trị viên)

**Mô tả:**
Người có toàn quyền quản trị hệ thống.

**Quyền hạn:**

* Quản lý người dùng (tạo, sửa, khóa tài khoản)
* Quản lý danh mục sản phẩm
* Thêm, sửa, xóa sản phẩm laptop và linh kiện
* Xem và xử lý toàn bộ đơn hàng
* Truy cập Django Admin
* Xem báo cáo tổng hợp

---

### 3.2 Staff (Nhân viên quản lý)

**Mô tả:**
Nhân viên hỗ trợ vận hành hệ thống bán hàng.

**Quyền hạn:**

* Thêm và cập nhật thông tin sản phẩm
* Xem danh sách đơn hàng
* Cập nhật trạng thái đơn hàng
* Không có quyền quản lý người dùng
* Không có quyền xóa dữ liệu quan trọng

---

### 3.3 Customer (Khách hàng)

**Mô tả:**
Người sử dụng hệ thống để mua laptop và linh kiện.

**Quyền hạn:**

* Đăng ký tài khoản
* Đăng nhập / đăng xuất
* Xem danh sách và chi tiết sản phẩm
* Thêm sản phẩm vào giỏ hàng
* Đặt hàng và thanh toán
* Xem lịch sử đơn hàng cá nhân
* Cập nhật thông tin cá nhân

---

### 3.4 Guest (Khách chưa đăng nhập)

**Mô tả:**
Người truy cập hệ thống nhưng chưa đăng nhập.

**Quyền hạn:**

* Xem trang chủ
* Xem danh sách sản phẩm
* Xem chi tiết sản phẩm
* Không được đặt hàng
* Không truy cập chức năng cá nhân

---

## 4. Ma trận phân quyền chức năng

| Chức năng                         | Guest | Customer | Staff | Admin |
| ----------------------------------- | ----- | -------- | ----- | ----- |
| Xem trang chủ                      | ✓    | ✓       | ✓    | ✓    |
| Xem danh sách sản phẩm           | ✓    | ✓       | ✓    | ✓    |
| Xem chi tiết sản phẩm            | ✓    | ✓       | ✓    | ✓    |
| Đăng ký tài khoản              | ✓    | ✗       | ✗    | ✗    |
| Đăng nhập / Đăng xuất         | ✓    | ✓       | ✓    | ✓    |
| Thêm vào giỏ hàng               | ✗    | ✓       | ✗    | ✗    |
| Đặt hàng / Thanh toán           | ✗    | ✓       | ✗    | ✗    |
| Xem lịch sử đơn hàng cá nhân | ✗    | ✓       | ✗    | ✗    |
| Cập nhật thông tin cá nhân     | ✗    | ✓       | ✗    | ✗    |
| Quản lý sản phẩm (Thêm/Sửa)   | ✗    | ✗       | ✓    | ✓    |
| Xóa sản phẩm                     | ✗    | ✗       | ✗    | ✓    |
| Xem danh sách đơn hàng          | ✗    | ✗       | ✓    | ✓    |
| Cập nhật trạng thái đơn hàng | ✗    | ✗       | ✓    | ✓    |
| Quản lý người dùng             | ✗    | ✗       | ✗    | ✓    |
| Truy cập Django Admin              | ✗    | ✗       | ✗    | ✓    |

---

## 5. Thiết kế Authorization ở Backend

### 5.1 Cơ chế xác thực

* Sử dụng **JWT (JSON Web Token)**
* Token được cấp khi đăng nhập thành công
* Token gửi kèm trong header `Authorization: Bearer <token>`

### 5.2 Kiểm soát quyền truy cập

* Sử dụng **permission classes** của Django REST Framework
* Kiểm tra role trước khi xử lý request
* Tách rõ `IsAuthenticated`, `IsAdmin`, `IsStaff`

### 5.3 Nguyên tắc bảo mật

* Không tin dữ liệu từ Frontend
* Mọi kiểm tra quyền phải thực hiện ở Backend
* Trả về HTTP Status phù hợp (`401`, `403`)

---

## 6. Thiết kế Authorization ở Frontend

* Lưu JWT trong localStorage hoặc cookie (HttpOnly nếu có)
* Ẩn/hiện menu theo role
* Bảo vệ route (Route Guard)
* Tự động redirect khi không đủ quyền

---

## 7. Kết luận

Tài liệu Authorization này đóng vai trò nền tảng cho việc thiết kế **luồng nghiệp vụ (Business Flow)** ở bước tiếp theo. Việc xác định rõ vai trò và quyền hạn giúp hệ thống:

* Hoạt động đúng nghiệp vụ
* Dễ mở rộng
* Đảm bảo an toàn và bảo mật dữ liệu

---

**Tài liệu:** authorization.md
**Thuộc repository:** `laptopqtk-proj`
