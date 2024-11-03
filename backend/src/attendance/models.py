from django.db import models
from users.models import User
from tenants.models import Tenant

class AttendanceRecord(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    status = models.CharField(max_length=50, choices=[('present', 'Present'), ('absent', 'Absent')])

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class LeaveRequest(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=[('approved', 'Approved'), ('pending', 'Pending'), ('rejected', 'Rejected')])

    def __str__(self):
        return f"{self.user.username} - {self.leave_type}"


class Holiday(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Shift(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    break_duration = models.DurationField()

    def __str__(self):
        return self.name

