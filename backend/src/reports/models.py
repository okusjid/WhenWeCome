from django.db import models
from tenants.models import Tenant
from users.models import User

class Report(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    report_data = models.JSONField()

    def __str__(self):
        return self.name
