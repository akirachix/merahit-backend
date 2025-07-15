from django.db import models
from django.utils import timezone
from users.models import MamaMboga, Customer

class Product(models.Model):
    vendor = models.ForeignKey(MamaMboga, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(
    max_length=50,
    choices=[
        ('tomatoes', 'Tomatoes'),
        ('cucumber', 'Cucumber'),
        ('onion', 'Onion'),
        ('carrot', 'Carrot'),
        ('sukuma', 'Sukuma'),
        ('potato', 'Potato'),
        ('cabbage', 'Cabbage'),
        ('okra', 'Okra'),
        ('kale', 'Kale'),
        ('pumpkin_leaves', 'Pumpkin Leaves'),
        ('bell_pepper', 'Bell Pepper'),
        ('omena', 'Omena'),
        ('tilapia', 'Tilapia'),
        ('fish_ball', 'Fish Ball'),
        ('fulu_fish', 'Fulu Fish'),
        ('fish_skew', 'Fish Skew'),
        ('fish_stick', 'Fish Stick'),
        ('black_beans', 'Black Beans'),
        ('yellow_beans', 'Yellow Beans'),
        ('githeri', 'Githeri'),
        ('red_beans', 'Red Beans'),
        ('lentils', 'Lentils'),
        ('green_peas', 'Green Peas'),
        ('chick_peas', 'Chick Peas'),
        ('green_grams', 'Green Grams'),
        ('garlic', 'Garlic'),
        ('chilli', 'Chilli'),
        ('ginger', 'Ginger'),
        ('matoke', 'Matoke'),
    ]
    )

    category = models.CharField(
        max_length=20,
        choices=[
            ('vegetable', 'Vegetable'),
            ('fish', 'Fish'),
            ('cereal', 'Cereal'),
            ('others', 'Others'),
        ]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    stock_unit = models.CharField(max_length=50,
    choices=[
        ('bunch','Bunch'),
        ('kilogram','Kilogram'),
        ('cup','Cup'),
        ('piece','Piece')
    ])
    product_image =  models.URLField(max_length=800)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class Discount(models.Model):
    vendor = models.ForeignKey(MamaMboga, on_delete=models.CASCADE, related_name='discounts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discounts')
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Discount on {self.product.product_name}"

class LoyalCustomerDiscount(models.Model):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='loyal_discounts')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loyal_discounts')
    received = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Loyal Discount for {self.customer.full_name}"

