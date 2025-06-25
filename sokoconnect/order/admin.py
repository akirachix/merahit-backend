from django.contrib import admin


from .models import Order
admin.site.register(Order)


from .models import OrderItem
admin.site.register(OrderItem)


from .models import Payment
admin.site.register(Payment)


from .models import Cart
admin.site.register(Cart)

# Register your models here.
