
# **Chuẩn hóa Response JSON & Review thiết kế tổng thể**

## 🎯 Mục tiêu

* Chuẩn hóa **format response JSON** cho toàn hệ thống
* Frontend chỉ cần **1 kiểu xử lý**
* Backend code nhất quán
* Dễ debug, dễ bảo trì, dễ bảo vệ

---

## 1️⃣ Nguyên tắc chuẩn Response (CHỐT)

### ✅ Mọi API đều trả về **JSON object**

Không trả raw list, không trả text.

---

### ✅ Cấu trúc response thống nhất

```json
{
  "success": true,
  "message": "Mô tả ngắn gọn",
  "data": { }
}
```

---

### ❌ KHÔNG LÀM

* Không trả nhiều format khác nhau
* Không trả string thuần
* Không trả HTTP 200 cho lỗi logic

---

## 2️⃣ Chuẩn Response cho từng trường hợp

---

### 🔹 2.1. Response thành công – GET (List)

```json
{
  "success": true,
  "message": "Get products successfully",
  "data": {
    "items": [
      {
        "id": 1,
        "name": "Laptop Dell XPS 13",
        "price": 25000000
      }
    ],
    "total": 10
  }
}
```

---

### 🔹 2.2. Response thành công – GET (Detail)

```json
{
  "success": true,
  "message": "Get product detail successfully",
  "data": {
    "id": 1,
    "name": "Laptop Dell XPS 13",
    "price": 25000000
  }
}
```

---

### 🔹 2.3. POST thành công

```json
{
  "success": true,
  "message": "Create product successfully",
  "data": {
    "id": 5
  }
}
```

---

### 🔹 2.4. Lỗi validation (400)

```json
{
  "success": false,
  "message": "Validation error",
  "errors": {
    "email": ["Email already exists"]
  }
}
```

---

### 🔹 2.5. Unauthorized (401)

```json
{
  "success": false,
  "message": "Authentication required"
}
```

---

### 🔹 2.6. Forbidden (403)

```json
{
  "success": false,
  "message": "Permission denied"
}
```

---

### 🔹 2.7. Not Found (404)

```json
{
  "success": false,
  "message": "Resource not found"
}
```

---

### 🔹 2.8. Server Error (500)

```json
{
  "success": false,
  "message": "Internal server error"
}
```

---

## 3️⃣ Chuẩn HTTP Status Code (bắt buộc)

| Tình huống    | Status |
| --------------- | ------ |
| GET OK          | 200    |
| POST tạo       | 201    |
| Validation lỗi | 400    |
| Unauthorized    | 401    |
| Forbidden       | 403    |
| Not found       | 404    |
| Server error    | 500    |

---

## 4️⃣ Chuẩn Response cho AUTH (JWT)

### Login thành công

```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "access": "jwt_access_token",
    "refresh": "jwt_refresh_token",
    "user": {
      "id": 1,
      "username": "khoi",
      "role": "CUSTOMER"
    }
  }
}
```

---

## 5️⃣ Chuẩn pagination

```json
{
  "success": true,
  "message": "Get products successfully",
  "data": {
    "items": [...],
    "pagination": {
      "page": 1,
      "page_size": 10,
      "total_pages": 5,
      "total_items": 42
    }
  }
}
```

---

## 6️⃣ Review tổng thể thiết kế (Checklist)

### ✔ Database

* ERD rõ
* 3NF
* Product dùng chung cho laptop & linh kiện

### ✔ API

* RESTful
* Versioned `/api/v1`
* Phân quyền rõ

### ✔ Frontend

* Chỉ consume API
* Không xử lý business logic

### ✔ Teamwork

* Monorepo
* Branch rõ
* Dễ chia task cho 3 người

---

## 7️⃣ Việc bạn PHẢI làm

1. Tạo file:

```
docs/api_response_standard.md
```

2. Ghi:

* Cấu trúc JSON
* Ví dụ thành công / lỗi
* HTTP status code

📌 File này cực kỳ quan trọng khi:

* FE code
* Test API
* Viết báo cáo
