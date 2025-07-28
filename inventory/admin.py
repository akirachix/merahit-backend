from django.contrib import admin

from .models import Product
admin.site.register(Product)
from .models import Discount
admin.site.register(Discount)
from .models import LoyalCustomerDiscount
admin.site.register(LoyalCustomerDiscount)


