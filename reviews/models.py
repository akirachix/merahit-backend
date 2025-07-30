from django.db import models
from django.utils import timezone
from users.models import Users
class Review(models.Model):
    vendor = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        limit_choices_to={'usertype': 'mamamboga'},
        related_name='mamamboga_review'
    )
    customer = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        limit_choices_to={'usertype': 'customer'},
        related_name='customer_review'
    )
    rating = models.SmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Review for {self.vendor.full_name}"
