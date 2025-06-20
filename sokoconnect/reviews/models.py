from django.db import models
from django.utils import timezone
from users.models import Customer, MamaMboga

class VendorReview(models.Model):
    vendor = models.ForeignKey(MamaMboga, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reviews')
    rating = models.SmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review for {self.vendor.full_name}"
