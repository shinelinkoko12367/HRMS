from django.db import models

# Create your models here.
from django.utils import timezone
from hr_employees import models as em

class ExpensesModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    employee_id = models.ForeignKey(em.EmployeeModel, on_delete=models.CASCADE, default=None)
    date = models.DateField(verbose_name='Date', default=timezone.now)
    Price = models.FloatField(verbose_name='Price', default=0.0)
    def __str__(self):
        return self.name