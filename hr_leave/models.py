from django.db import models

# Create your models here.

from django.utils import timezone
from hr_employees import models as em

class LeaveModel(models.Model):
    leave = models.CharField(max_length=20, verbose_name='Leave')
    start_date = models.DateField(verbose_name='Start Date', default=timezone.now)
    end_date = models.DateField(verbose_name='End Date', default=timezone.now)
    fine = models.FloatField(verbose_name='Fine', default=0.0)
    employee_id = models.ForeignKey(em.EmployeeModel, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.leave
