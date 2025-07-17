from django.db import models
from django.utils import timezone
from users.models import Users
from inventory.models import Product

class Order(models.Model):
    customer = models.ForeignKey(Users, on_delete=models.CASCADE,limit_choices_to={'usertype': 'customer'},related_name='customer_orders',)
    vendor = models.ForeignKey(Users, on_delete=models.CASCADE, limit_choices_to={'usertype': 'mamamboga'},related_name='vendor_orders',)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_at_order = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Item {self.product.product_name} in Order {self.order.id}"

class Payment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="Payment status"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Payment amount"
    )
    merchant_request_id = models.CharField(max_length=100, unique=True, default='test123')
    checkout_request_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        help_text="Unique Checkout Request ID from M-Pesa"
    )
    result_code = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="M-Pesa Result Code"
    )
    result_desc = models.TextField(
        blank=True,
        null=True,
        help_text="M-Pesa Result Description"
    )
    mpesa_receipt_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="M-Pesa Transaction Receipt Number"
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        help_text="Phone number used for payment"
    )
    transaction_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Date and time of the transaction"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the payment record was last updated"
    )
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        indexes = [
            models.Index(fields=['merchant_request_id']),
            models.Index(fields=['checkout_request_id']),
            models.Index(fields=['status']),
            models.Index(fields=['order']),
        ]
    def __str__(self):
        return f"Payment {self.id} for Order {self.order.id} ({self.status})"

class Cart(models.Model):
    customer = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='carts', limit_choices_to={'usertype': 'customer'})
    products = models.ManyToManyField(Product, related_name='carts')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_items = models.PositiveIntegerField()
    quantity_of_items = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        product_names = ", ".join([product.product_name for product in self.products.all()]) or "no products"
        return f"Cart with {product_names} for {self.customer.full_name}"