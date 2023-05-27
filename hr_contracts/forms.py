from django import forms
from hr_contracts import models
from flatpickr import DatePickerInput

class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = models.ContractModel
        fields = '__all__'
        widgets = {
            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }

class ContractUpdateForm(forms.ModelForm):
    class Meta:
        model = models.ContractModel
        fields = '__all__'
        widgets = {
            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }