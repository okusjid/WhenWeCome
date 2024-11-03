from django.db import models
from tenants.models import Tenant

class Asset(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    purchase_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('assigned', 'Assigned')])

    def __str__(self):
        return self.name
