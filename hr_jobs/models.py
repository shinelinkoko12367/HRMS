from django.db import models
from hr_departments import models as dpm

# Create your models here.
class JobModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    expected_employees = models.IntegerField(verbose_name='Expected Employees', default=0)
    department_id = models.ForeignKey(dpm.DepartmentModel, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.name