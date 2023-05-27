from django import forms
from hr_payroll import models
from flatpickr import DatePickerInput

class PayrollCreateForm(forms.ModelForm):
    class Meta:
        model = models.PayroolModel
        fields = '__all__'
        widgets = {
            'date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }
        
class PayrollUpdateForm(forms.ModelForm):
    class Meta:
        model = models.PayroolModel
        fields = '__all__'
        widgets = {
            'date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }