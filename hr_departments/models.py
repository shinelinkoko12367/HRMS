from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')

    def __str__(self):
        return self.name