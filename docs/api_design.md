**BƯỚC 19 / 100 – Thiết kế API Endpoints**

## Mục tiêu

* Xác định **toàn bộ API** hệ thống
* Chuẩn RESTful, dễ mở rộng
* Dùng trực tiếp cho:
  * Django REST Framework
  * Frontend Next.js gọi API
* Tránh sửa DB / logic về sau

---

## Nguyên tắc thiết kế API (bắt buộc)

### RESTful

* **Resource-based**
* Dùng danh từ, không dùng động từ

 `/getProducts`
`/api/products/`

---

### HTTP Method đúng nghĩa

| Method      | Ý nghĩa      |
| ----------- | -------------- |
| GET         | Lấy dữ liệu |
| POST        | Tạo mới      |
| PUT / PATCH | Cập nhật     |
| DELETE      | Xóa           |

### Versioning

```text
/api/v1/...
```

---

## Tổng quan nhóm API

| Nhóm    | Mô tả                  |
| -------- | ------------------------ |
| Auth     | Đăng nhập, đăng ký |
| User     | Thông tin người dùng |
| Product  | Laptop & Linh kiện      |
| Category | Danh mục                |
| Brand    | Hãng                    |
| Cart     | Giỏ hàng               |
| Order    | Đơn hàng              |
| Payment  | Thanh toán              |
| Admin    | Quản trị               |

---

## CHI TIẾT API ENDPOINTS (CHỐT)

## AUTH API

### Đăng ký

```
POST /api/v1/auth/register/
```

Body:

```json
{
  "username": "khoi",
  "email": "khoi@gmail.com",
  "password": "123456"
}
```

---

### Đăng nhập

```
POST /api/v1/auth/login/
```

Response:

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token",
  "user": {
    "id": 1,
    "role": "CUSTOMER"
  }
}
```

---

## 👤 USER API

### Lấy profile

```
GET /api/v1/users/me/
Authorization: Bearer <token>
```

---

## 📦 CATEGORY API

```
GET    /api/v1/categories/
POST   /api/v1/categories/        (ADMIN)
PUT    /api/v1/categories/{id}/   (ADMIN)
DELETE /api/v1/categories/{id}/   (ADMIN)
```

---

## 🏷 BRAND API

```
GET    /api/v1/brands/
POST   /api/v1/brands/        (ADMIN)
PUT    /api/v1/brands/{id}/   (ADMIN)
DELETE /api/v1/brands/{id}/   (ADMIN)
```

---

## 🖥️ PRODUCT API (Laptop & Linh kiện)

📌 **Dùng chung bảng `product`, phân biệt bằng `type`**

### Danh sách sản phẩm

```
GET /api/v1/products/
```

Query:

```
?type=LAPTOP
?category=ram
?brand=asus
?min_price=10000000
```

---

### Chi tiết sản phẩm

```
GET /api/v1/products/{id}/
```

---

### CRUD sản phẩm (ADMIN)

```
POST   /api/v1/products/
PUT    /api/v1/products/{id}/
DELETE /api/v1/products/{id}/
```

## 🛒 CART API

### Lấy giỏ hàng

```
GET /api/v1/cart/
```

### Thêm sản phẩm

```
POST /api/v1/cart/items/
```

```json
{
  "product_id": 5,
  "quantity": 2
}
```

### Xóa sản phẩm

```
DELETE /api/v1/cart/items/{id}/
```

## 📑 ORDER API

### Checkout

```
POST /api/v1/orders/checkout/
```

### Danh sách đơn hàng (user)

```
GET /api/v1/orders/my/
```

### Danh sách đơn hàng (ADMIN)

```
GET /api/v1/orders/
```

---

## 💳 PAYMENT API

```
POST /api/v1/payments/
```

📌 Giai đoạn đồ án: **mock payment** (COD / giả lập)

## 🛠 ADMIN API

```
GET /api/v1/admin/dashboard/
```

* Tổng số user
* Tổng đơn hàng
* Doanh thu

## 4️⃣ Mapping API → Django App

| App      | API                      |
| -------- | ------------------------ |
| users    | auth, profile            |
| products | product, category, brand |
| orders   | cart, order              |
| payments | payment                  |

## Tiêu chí bảo vệ (giảng viên hay hỏi)

✔️ Vì sao dùng `/products/` không tách laptop/linh kiện
✔️ Vì sao dùng JWT
✔️ Vì sao cart tách bảng
✔️ Vì sao order có order_item

→ Tất cả **đã trả lời bằng thiết kế này**
