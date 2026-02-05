# **Thiết kế luồng nghiệp vụ chính (Business Flow)**

## Mục tiêu

* Mô tả **hệ thống vận hành như thế nào từ đầu đến cuối**
* Trả lời:
  * Người dùng làm gì trước?
  * Hệ thống xử lý gì tiếp theo?
* Là cơ sở để:
  * Thiết kế CSDL
  * Thiết kế API
  * Code backend/frontend không bị rối

---

## Các luồng nghiệp vụ CỐT LÕI (CHỐT)

Chúng ta **chỉ cần 4 luồng chính**

---

## 1. Luồng Đăng ký – Đăng nhập

**Actor:** Customer

**Flow:**

```
Mở website
→ Chọn Đăng ký
→ Nhập thông tin (email, mật khẩu)
→ Backend validate
→ Lưu user vào DB
→ Đăng nhập
→ Trả JWT
→ Frontend lưu token
```

 Ghi chú:

* Password **băm**
* JWT dùng cho mọi request sau

---

## 2. Luồng Xem & Chọn sản phẩm

**Actor:** Guest / Customer

**Flow:**

```
Vào trang Home
→ Xem danh sách laptop / linh kiện
→ Lọc / tìm kiếm
→ Xem chi tiết sản phẩm
```

 Không cần đăng nhập

---

## 3. Luồng Đặt hàng (Quan trọng nhất)

**Actor:** Customer

**Flow:**

```
Xem sản phẩm
→ Thêm vào giỏ hàng
→ Xem giỏ hàng
→ Nhấn Đặt hàng
→ Backend tạo Order
→ Trừ tồn kho
→ Trạng thái: Pending
```

Sau này Staff/Admin xử lý

---

## 4. Luồng Xử lý đơn hàng

**Actor:** Staff / Admin

**Flow:**

```
Đăng nhập admin
→ Xem danh sách đơn
→ Cập nhật trạng thái:
   Pending → Shipping → Completed
```

---


* Vẽ **Activity Diagram**
* Hoặc viết **flow dạng text** (được chấp nhận)
