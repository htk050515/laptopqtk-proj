# THIẾT KẾ ERD (ENTITY RELATIONSHIP DIAGRAM)

## 1. Mục tiêu của ERD trong dự án này

ERD dùng để:

* Xác định **các bảng (Entity)** trong database
* Xác định **thuộc tính (Attribute)** của mỗi bảng
* Xác định **mối quan hệ (Relationship)** giữa các bảng
* Làm nền cho:
  * Django Models
  * Migration
  * API
  * Frontend hiển thị dữ liệu

---

## 2, Xác định các Entity chính

Dựa trên nghiệp vụ bán laptop & linh kiện, hệ thống **bắt buộc** có các entity sau:

### Nhóm Người dùng

1. **User**
2. **Role**

### Nhóm Sản phẩm

3. **Category**
4. **Brand**
5. **Product**
6. **ProductImage**

### Nhóm Bán hàng

7. **Cart**
8. **CartItem**
9. **Order**
10. **OrderItem**
11. **Payment**

### Nhóm mở rộng (khuyến nghị)

12. **Review**
13. **Inventory**

Tổng cộng: **13 entity**

---

## Chi tiết từng Entity (chuẩn ERD)

---

### 1. USER

| Field      | Kiểu    | Ghi chú        |
| ---------- | -------- | --------------- |
| id         | PK       | Khóa chính    |
| username   | varchar  | Đăng nhập    |
| email      | varchar  | Unique          |
| password   | varchar  | Hash            |
| full_name  | varchar  |                 |
| phone      | varchar  |                 |
| address    | text     |                 |
| role_id    | FK       | Liên kết Role |
| created_at | datetime |                 |
| is_active  | boolean  |                 |

---

### 2. ROLE

| Field | Kiểu   |
| ----- | ------- |
| id    | PK      |
| name  | varchar |

 Quan hệ:

* **Role 1 – N User**

---

### 3. CATEGORY

| Field       | Kiểu   |
| ----------- | ------- |
| id          | PK      |
| name        | varchar |
| description | text    |

 Quan hệ:

* **Category 1 – N Product**

---

### 4. BRAND

| Field | Kiểu   |
| ----- | ------- |
| id    | PK      |
| name  | varchar |

 Quan hệ:

* **Brand 1 – N Product**

---

### 5. PRODUCT

| Field       | Kiểu    |
| ----------- | -------- |
| id          | PK       |
| name        | varchar  |
| description | text     |
| price       | decimal  |
| category_id | FK       |
| brand_id    | FK       |
| type        | varchar  |
| created_at  | datetime |
| is_active   | boolean  |

Quan hệ:

* Category 1 – N Product
* Brand 1 – N Product
* Product 1 – N ProductImage
* Product 1 – N Review
* Product 1 – 1 Inventory

---

### 6. PRODUCT_IMAGE

| Field      | Kiểu   |
| ---------- | ------- |
| id         | PK      |
| product_id | FK      |
| image_url  | varchar |

---

### 7. INVENTORY

| Field      | Kiểu |
| ---------- | ----- |
| id         | PK    |
| product_id | FK    |
| quantity   | int   |

 Quan hệ:

* Product 1 – 1 Inventory

---

### 8. CART

| Field      | Kiểu    |
| ---------- | -------- |
| id         | PK       |
| user_id    | FK       |
| created_at | datetime |

 Quan hệ:

* User 1 – 1 Cart

---

### 9. CART_ITEM

| Field      | Kiểu |
| ---------- | ----- |
| id         | PK    |
| cart_id    | FK    |
| product_id | FK    |
| quantity   | int   |

 Quan hệ:

* Cart 1 – N CartItem
* Product 1 – N CartItem

---

### 10. ORDER

| Field       | Kiểu    |
| ----------- | -------- |
| id          | PK       |
| user_id     | FK       |
| total_price | decimal  |
| status      | varchar  |
| created_at  | datetime |

---

### 11. ORDER_ITEM

| Field      | Kiểu   |
| ---------- | ------- |
| id         | PK      |
| order_id   | FK      |
| product_id | FK      |
| quantity   | int     |
| price      | decimal |

 Quan hệ:

* Order 1 – N OrderItem
* Product 1 – N OrderItem

---

### 12. PAYMENT

| Field          | Kiểu    |
| -------------- | -------- |
| id             | PK       |
| order_id       | FK       |
| payment_method | varchar  |
| payment_status | varchar  |
| paid_at        | datetime |

Quan hệ:

* Order 1 – 1 Payment

---

### 13. REVIEW

| Field      | Kiểu    |
| ---------- | -------- |
| id         | PK       |
| user_id    | FK       |
| product_id | FK       |
| rating     | int      |
| comment    | text     |
| created_at | datetime |

---

## Tóm tắt quan hệ ERD (để vẽ)

* Role 1 — N User
* User 1 — 1 Cart
* Cart 1 — N CartItem
* Product 1 — N CartItem
* User 1 — N Order
* Order 1 — N OrderItem
* Product 1 — N OrderItem
* Order 1 — 1 Payment
* Category 1 — N Product
* Brand 1 — N Product
* Product 1 — N ProductImage
* Product 1 — N Review
* Product 1 — 1 Inventory

---

## Công cụ vẽ ERD 

Eraser


// --- NHÓM NGƯỜI DÙNG & PHÂN QUYỀN ---

User[icon:user,color:blue]{

  idint[pk, increment]

  usernamevarchar[unique]

  emailvarchar[unique]

  passwordvarchar

  full_namevarchar

  phonevarchar

  addresstext

  role_idint[ref: > Role.id]

  created_atdatetime

  is_activeboolean

}

Role[icon:shield,color:blue]{

  idint[pk, increment]

  namevarchar

}

// --- NHÓM SẢN PHẨM ---

Category[icon:grid,color:green]{

  idint[pk, increment]

  namevarchar

  descriptiontext

}

Brand[icon:award,,color:green]{

  idint[pk, increment]

  namevarchar

}

Product[icon:package,color:green]{

  idint[pk, increment]

  category_idint[ref: > Category.id]

  brand_idint[ref: > Brand.id]

  namevarchar

  descriptiontext

  pricedecimal

  typevarchar

  created_atdatetime

  is_activeboolean

}

ProductImage[icon:image,color:green]{

  idint[pk, increment]

  product_idint[ref: > Product.id]

  image_urlvarchar

}

Inventory[icon:database,color:green]{

  idint[pk, increment]

  product_idint[ref: - Product.id] // Quan hệ 1-1

  quantityint

}

// --- NHÓM GIỎ HÀNG & ĐƠN HÀNG ---

Cart[icon:shopping-cart,color:orange]{

  idint[pk, increment]

  user_idint[ref: - User.id] // Quan hệ 1-1

  created_atdatetime

}

CartItem[color:orange]{

  idint[pk, increment]

  cart_idint[ref: > Cart.id]

  product_idint[ref: > Product.id]

  quantityint

}

Order[icon:file-text,color:orange]{

  idint[pk, increment]

  user_idint[ref: > User.id]

  total_pricedecimal

  statusvarchar

  created_atdatetime

}

OrderItem[color:orange]{

  idint[pk, increment]

  order_idint[ref: > Order.id]

  product_idint[ref: > Product.id]

  quantityint

  pricedecimal

}

// --- THANH TOÁN & ĐÁNH GIÁ ---

Payment[icon:credit-card,color:purple]{

  idint[pk, increment]

  order_idint[ref: - Order.id] // Quan hệ 1-1

  payment_methodvarchar

  payment_statusvarchar

  paid_atdatetime

}

Review[icon:star,color:purple]{

  idint[pk, increment]

  user_idint[ref: > User.id]

  product_idint[ref: > Product.id]

  ratingint

  commenttext

  created_atdatetime

}
