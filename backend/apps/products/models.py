from django.db import models
from django.utils.text import slugify
from django.conf import settings



class Laptop(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    cpu = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=100)
    gpu = models.CharField(max_length=100, blank=True)
    screen = models.CharField(max_length=100)

    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='laptops/', blank=True, null=True)

    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Accessory(models.Model):
    CATEGORY_CHOICES = (
        ('RAM', 'RAM'),
        ('SSD', 'SSD'),
        ('HDD', 'HDD'),
        ('PERIPHERAL', 'Peripheral'),
    )

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='accessories/', blank=True, null=True)

    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('SHIPPED', 'Shipped'),
        ('CANCELLED', 'Cancelled'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"

class OrderItem(models.Model):
    PRODUCT_TYPE_CHOICES = (
        ('LAPTOP', 'Laptop'),
        ('ACCESSORY', 'Accessory'),
    )

    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
    product_id = models.PositiveIntegerField()
    product_name = models.CharField(max_length=255)

    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_subtotal(self):
        return self.price * self.quantity
