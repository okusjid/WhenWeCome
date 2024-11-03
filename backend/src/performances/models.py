from django.db import models
from users.models import User
from tenants.models import Tenant


class PerformanceReview(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.PositiveIntegerField()
    feedback = models.TextField()
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_given")

    def __str__(self):
        return f"{self.user.username} - Performance Review"
