Tốt. Bây giờ chúng ta bước vào **thiết kế dữ liệu cốt lõi** – nếu bước này sai thì  **ERD + DB + code sẽ sai dây chuyền** .

---

# **BƯỚC 15 / 100 – Xác định các Entity chính (Domain Model)**

## Mục tiêu

* Trả lời câu hỏi:
  **“Hệ thống cần lưu những dữ liệu gì?”**
* Xác định **các bảng chính trong CSDL**
* Là nền cho:
  * ERD
  * PostgreSQL schema
  * Django Models

---

## Nguyên tắc xác định Entity

Một Entity phải:

* Có dữ liệu cần lưu lâu dài
* Có vòng đời rõ ràng
* Xuất hiện trong luồng nghiệp vụ

Không phải màn hình nào cũng là entity
Không tạo entity dư thừa

---

## DANH SÁCH ENTITY CHÍNH

### 1. User

**Vai trò:** Người dùng hệ thống

Thuộc tính chính:

* id
* username
* email
* password
* role (customer / staff / admin)
* created_at

Dùng **Custom User** (Django)

---

### 2. Brand

**Vai trò:** Hãng laptop / linh kiện

Thuộc tính:

* id
* name

Ví dụ: Dell, ASUS, HP

---

### 3. Category

**Vai trò:** Phân loại sản phẩm

Thuộc tính:

* id
* name
  Laptop, RAM, SSD, VGA…

---

### 4. Product 

**Vai trò:** Khái niệm sản phẩm chung

Thuộc tính:

* id
* name
* price
* stock
* description
* image
* brand_id
* category_id

Laptop & Linh kiện đều là Product (triển khai bằng Django model hoặc kế thừa logic)

---

### 5. Order

**Vai trò:** Đơn hàng

Thuộc tính:

* id
* user_id
* total_price
* status
* created_at

status: Pending / Shipping / Completed

---

### 6. OrderItem

**Vai trò:** Chi tiết sản phẩm trong đơn

Thuộc tính:

* id
* order_id
* product_id
* quantity
* price

---

## Quan hệ giữa các Entity

* User **1–N** Order
* Order **1–N** OrderItem
* Product **1–N** OrderItem
* Brand **1–N** Product
* Category **1–N** Product
