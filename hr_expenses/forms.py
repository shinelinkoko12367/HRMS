from django import forms
from hr_expenses import models
from flatpickr import DatePickerInput

class ExpensesCreateForm(forms.ModelForm):
    class Meta:
        model = models.ExpensesModel
        fields = '__all__'
        widgets = {
            'date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }
        
class ExpensesUpdateForm(forms.ModelForm):
    class Meta:
        model = models.ExpensesModel
        fields = '__all__'
        widgets = {
            'date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }