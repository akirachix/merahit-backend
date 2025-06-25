from django.test import TestCase
from django.utils import timezone
from order.models import Order, OrderItem, Payment, Cart
from users.models import Users, Customer, MamaMboga
from inventory.models import Product
from decimal import Decimal

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = Users.objects.create(
            full_name='Jane',
            phone_number='1234567890',
            password='test1234',
            latitude=1.234,
            longitude=5.678,
            profile_picture='https://example.com/profile.jpg'
        )
        self.customer = Customer.objects.create(
            full_name='Jane',
            phone_number='0987654321',
            password='test1234',
            latitude=1.234,
            longitude=5.678,
            profile_picture='https://example.com/customer.jpg',
            is_loyal=False
        )
        self.vendor = MamaMboga.objects.create(
            full_name='Mamamax',
            phone_number='1122334455',
            password='test1234',
            latitude=2.345,
            longitude=6.789,
            profile_picture='https://example.com/vendor.jpg',
            working_days='Monday-Friday',
            working_hours='9AM-5PM'
        )
        self.product = Product.objects.create(
            vendor=self.vendor,
            product_name='Tomato',
            price=10.00,
            stock_quantity=100
        )

    def test_order_creation(self):
        order = Order.objects.create(
            customer=self.customer,
            vendor=self.vendor,
            status='PENDING',
            total_amount=Decimal('50.00')
        )
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.vendor, self.vendor)
        self.assertEqual(order.status, 'PENDING')
        self.assertEqual(order.total_amount, Decimal('50.00'))
        self.assertTrue(isinstance(order.order_date, timezone.datetime))
        self.assertTrue(isinstance(order.created_at, timezone.datetime))
        self.assertEqual(str(order), 'Order PENDING')

    def test_order_default_timestamp(self):
        order = Order.objects.create(
            customer=self.customer,
            vendor=self.vendor,
            status='PENDING',
            total_amount=Decimal('50.00')
        )
        self.assertIsNotNone(order.created_at)
        self.assertIsNotNone(order.updated_at)
        self.assertTrue(order.created_at <= order.updated_at)

class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = Users.objects.create(
            full_name='Test User',
            phone_number='1234567891',  
            password='test1234',
            latitude=1.234,
            longitude=5.678,
            profile_picture='https://example.com/profile.jpg'
        )
        self.customer = Customer.objects.create(
            full_name='Test Customer',
            phone_number='0987654322',  
            password='test1234',
            latitude=1.234,
            longitude=5.678,
            profile_picture='https://example.com/customer.jpg',
            is_loyal=False
        )
        self.vendor = MamaMboga.objects.create(
            full_name='Test Vendor',
            phone_number='1122334456', 
            password='test1234',
            latitude=2.345,
            longitude=6.789,
            profile_picture='https://example.com/vendor.jpg',
            working_days='Monday-Friday',
            working_hours='9AM-5PM'
        )
        self.product = Product.objects.create(
            vendor=self.vendor,
            product_name='Test Product',
            price=10.00,
            stock_quantity=100
        )
        self.order = Order.objects.create(
            customer=self.customer,
            vendor=self.vendor,
            status='PENDING',
            total_amount=Decimal('50.00')
        )

    def test_order_item_creation(self):
        order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=Decimal('2.00'),
            price_at_order=Decimal('10.00'),
            total_price=Decimal('20.00')
        )
        self.assertEqual(order_item.order, self.order)
        self.assertEqual(order_item.product, self.product)
        self.assertEqual(order_item.quantity, Decimal('2.00'))
        self.assertEqual(order_item.price_at_order, Decimal('10.00'))
        self.assertEqual(order_item.total_price, Decimal('20.00'))
        self.assertEqual(str(order_item), f'Item {self.product.product_name} in Order {self.order.id}')

class PaymentModelTest(TestCase):
    def setUp(self):
        self.user = Users.objects.create(
            full_name='Test User',
            phone_number='1234567893',  
            password='test1234',
            latitude=1.234,
            longitude=5.678,
            profile_picture='https://example.com/profile.jpg'
        )
        self.customer = Customer.objects.create(
            full_name='Test Customer',
            phone_number='0987654324',  
            password='test1234',
            latitude=1.234,
            longitude=5.678,
            profile_picture='https://example.com/customer.jpg',
            is_loyal=False
        )
        self.vendor = MamaMboga.objects.create(
            full_name='Test Vendor',
            phone_number='1122334457',  
            password='test1234',
            latitude=2.345,
            longitude=6.789,
            profile_picture='https://example.com/vendor.jpg',
            working_days='Monday-Friday',
            working_hours='9AM-5PM'
        )
        self.order = Order.objects.create(
            customer=self.customer,
            vendor=self.vendor,
            status='PENDING',
            total_amount=Decimal('50.00')
        )

    def test_payment_creation(self):
        payment = Payment.objects.create(
            order=self.order,
            amount=Decimal('50.00'),
            payment_status='PAID'
        )
        self.assertEqual(payment.order, self.order)
        self.assertEqual(payment.amount, Decimal('50.00'))
        self.assertEqual(payment.payment_status, 'PAID')
        self.assertTrue(isinstance(payment.payment_date, timezone.datetime))
        self.assertEqual(str(payment), 'Payment PAID')

class CartModelTest(TestCase):
    def setUp(self):
        self.user = Users.objects.create(
            full_name='Mamamax',
            phone_number='1234567895',
            password='test1234',
            latitude=1.234,
            longitude=5.678,
            profile_picture='https://example.com/profile.jpg'
        )
        self.customer = Customer.objects.create(
            full_name='Jane',
            phone_number='0987654326', 
            password='test1234',
            latitude=1.234,
            longitude=5.678,
            profile_picture='https://example.com/customer.jpg',
            is_loyal=False
        )
        self.vendor = MamaMboga.objects.create(
            full_name='Mamamax',
            phone_number='1122334458', 
            password='test1234',
            latitude=2.345,
            longitude=6.789,
            profile_picture='https://example.com/vendor.jpg',
            working_days='Monday-Friday',
            working_hours='9AM-5PM'
        )
        self.product = Product.objects.create(
            vendor=self.vendor,
            product_name='Tomato',
            price=10.00,
            stock_quantity=100
        )

    def test_cart_creation(self):
        cart = Cart.objects.create(
            customer=self.customer,
            price=Decimal('20.00'),
            number_of_items=2,
            quantity_of_items='2 items'
        )
        cart.products.add(self.product)
        self.assertEqual(cart.customer, self.customer)
        self.assertEqual(cart.price, Decimal('20.00'))
        self.assertEqual(cart.number_of_items, 2)
        self.assertEqual(cart.quantity_of_items, '2 items')
        self.assertIn(self.product, cart.products.all())
        self.assertEqual(str(cart), f"Cart with {self.product.product_name} for {self.customer.full_name}")


        