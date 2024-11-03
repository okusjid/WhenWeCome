from django.db import models
from tenants.models import Tenant
from users.models import Department

class JobPosting(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    posted_date = models.DateField()
    closing_date = models.DateField()

    def __str__(self):
        return self.title
