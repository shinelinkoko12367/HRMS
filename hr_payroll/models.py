from django.db import models

# Create your models here.
from django.utils import timezone
from hr_leave import models as leav
from hr_contracts import models as cont
class PayroolModel(models.Model):
    Contract_id = models.ForeignKey(cont.ContractModel,on_delete=models.CASCADE,default=None)
    leave_id = models.ForeignKey(leav.LeaveModel,on_delete=models.CASCADE,default=None)
    fine = models.FloatField(verbose_name='fine', default=leave_id)
    date = models.DateField(verbose_name='Date', default=timezone.now)
    salary = models.FloatField(verbose_name='salary', default= Contract_id)    
    bonus = models.FloatField(verbose_name='bonus', default=0.0)
    total = models.FloatField(verbose_name='total', default=0.0)
    
    def __str__(self):
        return self.Contract_id.name