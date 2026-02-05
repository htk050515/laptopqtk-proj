**BƯỚC 15 / 100 – THIẾT KẾ KIẾN TRÚC TỔNG THỂ HỆ THỐNG (SYSTEM ARCHITECTURE)**

## 1. Mục đích 

* Xác định **toàn bộ kiến trúc kỹ thuật** của hệ thống
* Trả lời rõ:
  * Frontend nói chuyện với Backend thế nào?
  * Backend xử lý ra sao?
  * Database nằm ở đâu?
* Là cơ sở để:
  * Vẽ **Architecture Diagram**
  * Thiết kế API (bước sau)
  * Chia việc cho nhóm 3 người

---

## 2. Mô hình kiến trúc được chọn

Hệ thống sử dụng **mô hình 3-Tier Architecture + RESTful API**

```
[ Client (Browser) ]
        |
        |  HTTP/HTTPS
        v
[ Frontend – Next.js ]
        |
        |  REST API (JSON)
        v
[ Backend – Django REST ]
        |
        |  ORM
        v
[ PostgreSQL Database ]
```

---

## 3. Phân tích từng tầng 

### 3.1 Presentation Layer – Frontend

**Công nghệ:**

* Next.js
* TailwindCSS

**Chức năng:**

* Hiển thị giao diện người dùng
* Gửi request tới Backend API
* Nhận JSON và render UI
* Không xử lý logic nghiệp vụ

**Lưu ý báo cáo:**

> Frontend chỉ đảm nhiệm hiển thị và tương tác, không trực tiếp truy cập database.

---

### 3.2 Application Layer – Backend

**Công nghệ:**

* Django
* Django REST Framework
* JWT Authentication

**Chức năng:**

* Xử lý nghiệp vụ
* Kiểm tra phân quyền (RBAC)
* Xác thực người dùng
* Cung cấp RESTful API

**Module chính:**

* User Management
* Product Management
* Order Management
* Authorization

---

### 3.3 Data Layer – Database

**Công nghệ:**

* PostgreSQL

**Chức năng:**

* Lưu trữ dữ liệu người dùng
* Lưu trữ sản phẩm, đơn hàng
* Đảm bảo toàn vẹn dữ liệu

---

## 4. Luồng dữ liệu tổng quát (Data Flow)

Ví dụ: Customer đặt hàng

1. Người dùng thao tác trên giao diện
2. Frontend gửi request `POST /api/orders`
3. Backend:
   * Xác thực JWT
   * Kiểm tra quyền Customer
   * Xử lý nghiệp vụ
4. Backend ghi dữ liệu vào PostgreSQL
5. Trả response JSON
6. Frontend hiển thị kết quả

---

## 5. Bảo mật trong kiến trúc

* JWT cho xác thực
* RBAC cho phân quyền
* Không expose database
* Validate dữ liệu ở Backend

---

## 6. Phân chia trách nhiệm theo kiến trúc

| Thành viên  | Phụ trách                 |
| ------------- | --------------------------- |
| Backend Lead  | Django, API, DB             |
| Frontend Lead | Next.js, UI                 |
| Fullstack     | Git, tích hợp, tài liệu |

---

## 7. Kết luận (chuẩn báo cáo)

Kiến trúc 3-tier giúp hệ thống:

* Dễ mở rộng
* Dễ bảo trì
* Phù hợp phát triển nhiều client (web, mobile)
