
# Chuẩn hóa Database & Ánh xạ ERD → PostgreSQL + Django Models

## 1. Mục tiêu

Bước này nhằm chuẩn hóa thiết kế cơ sở dữ liệu cho hệ thống website bán laptop, đảm bảo dữ liệu đạt chuẩn  **Third Normal Form (3NF)** , lựa chọn kiểu dữ liệu phù hợp trong  **PostgreSQL** , đồng thời ánh xạ rõ ràng sang **Django Models** để sẵn sàng cho giai đoạn migration và triển khai backend.

Các mục tiêu cụ thể bao gồm:

* Chuẩn hóa dữ liệu, tránh dư thừa và phụ thuộc không cần thiết.
* Xác định cấu trúc bảng vật lý trong PostgreSQL.
* Thiết lập quy ước đặt tên thống nhất.
* Chuẩn bị nền tảng logic cho Django ORM.

---

## 2. Chuẩn hóa dữ liệu (Normalization – 3NF)

### 2.1. Chuẩn 1NF – Atomic

Mỗi trường dữ liệu chỉ chứa một giá trị duy nhất, không lưu danh sách hay tập giá trị trong cùng một field.

Ví dụ:

* Không lưu danh sách ảnh sản phẩm trong một cột duy nhất.
* Tách bảng `product_image` để lưu nhiều ảnh cho một sản phẩm.

### 2.2. Chuẩn 2NF – Không phụ thuộc từng phần

Các thuộc tính không khóa phải phụ thuộc đầy đủ vào khóa chính.

* Bảng `order_item` được tách riêng khỏi `order`.
* Giá sản phẩm được lưu tại `order_item.price` nhằm đảm bảo tính lịch sử (snapshot) khi giá thay đổi theo thời gian.

### 2.3. Chuẩn 3NF – Không phụ thuộc bắc cầu

Không tồn tại sự phụ thuộc gián tiếp giữa các thuộc tính không khóa.

* Bảng `product` không lưu trực tiếp tên thương hiệu.
* Chỉ lưu `brand_id` và tham chiếu sang bảng `brand`.

**Kết luận:** ERD thiết kế ở Bước 16 đã đạt chuẩn 3NF và đáp ứng yêu cầu cho đồ án.

---

## 3. Quy ước thiết kế Database (PostgreSQL)

### 3.1. Quy ước đặt tên

| Thành phần      | Quy ước              |
| ----------------- | ---------------------- |
| Tên bảng        | snake_case, số ít    |
| Khóa chính (PK) | id                     |
| Khóa ngoại (FK) | _id                    |
| Thời gian        | created_at, updated_at |

Quy ước này giúp đảm bảo tính nhất quán, dễ bảo trì và tương thích tốt với Django ORM.

---

## 4. Thiết kế các bảng dữ liệu (Mapping ERD → PostgreSQL)

### 4.1. Bảng role

id SERIAL PRIMARY KEY
name VARCHAR(30) UNIQUE NOT NULL

### 4.2. Bảng user

id SERIAL PRIMARY KEY
username VARCHAR(50) UNIQUE
email VARCHAR(100) UNIQUE
password VARCHAR(255)
full_name VARCHAR(100)
phone VARCHAR(20)
address TEXT
role_id INT REFERENCES role(id)
is_active BOOLEAN DEFAULT TRUE
created_at TIMESTAMP

Lưu ý: Trong triển khai thực tế, Django sẽ sử dụng `AbstractUser` để mở rộng.

### 4.3. Bảng category

**id SERIAL PRIMARY KEY
name VARCHAR(100)
description TEXT**

### 4.4. Bảng brand

* id SERIAL PRIMARY KEY
  name VARCHAR(100)

### 4.5. Bảng product

id SERIAL PRIMARY KEY
name VARCHAR(200)
description TEXT
price NUMERIC(12,2)
type VARCHAR(20)
category_id INT REFERENCES category(id)
brand_id INT REFERENCES brand(id)
is_active BOOLEAN DEFAULT TRUE
created_at TIMESTAMP

### 4.6. Bảng product_image

id SERIAL PRIMARY KEY
product_id INT REFERENCES product(id)
image_url VARCHAR(255)

### 4.7. Bảng inventory

id SERIAL PRIMARY KEY
product_id INT UNIQUE REFERENCES product(id)
quantity INT DEFAULT 0

### 4.8. Bảng cart

id SERIAL PRIMARY KEY
user_id INT UNIQUE REFERENCES "user"(id)
created_at TIMESTAMP

### 4.9. Bảng cart_item

id SERIAL PRIMARY KEY
cart_id INT REFERENCES cart(id)
product_id INT REFERENCES product(id)
quantity INT

### 4.10. Bảng order

id SERIAL PRIMARY KEY
user_id INT REFERENCES "user"(id)
total_price NUMERIC(12,2)
status VARCHAR(30)
created_at TIMESTAMP

### 4.11. Bảng order_item

id SERIAL PRIMARY KEY
order_id INT REFERENCES "order"(id)
product_id INT REFERENCES product(id)
quantity INT
price NUMERIC(12,2)

### 4.12. Bảng payment

id SERIAL PRIMARY KEY
order_id INT UNIQUE REFERENCES "order"(id)
payment_method VARCHAR(50)
payment_status VARCHAR(50)
paid_at TIMESTAMP

### 4.13. Bảng review

id SERIAL PRIMARY KEY
user_id INT REFERENCES "user"(id)
product_id INT REFERENCES product(id)
rating INT
comment TEXT
created_at TIMESTAMP

---

## 5. Ánh xạ PostgreSQL sang Django Models

|  |  |
| - | - |



| PostgreSQL | Django               |
| ---------- | -------------------- |
| SERIAL     | models.AutoField     |
| VARCHAR    | models.CharField     |
| TEXT       | models.TextField     |
| NUMERIC    | models.DecimalField  |
| TIMESTAMP  | models.DateTimeField |
| FK         | models.ForeignKey    |
| UNIQUE     | unique=True          |

Mỗi bảng tương ứng với một Model trong Django. Các khóa ngoại cần khai báo `related_name` để thuận tiện trong truy vấn ORM.
