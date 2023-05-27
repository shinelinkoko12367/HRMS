from django import forms
from hr_leave import models
from flatpickr import DatePickerInput

class LeaveCreateForm(forms.ModelForm):
    class Meta:
        model = models.LeaveModel
        fields = '__all__'
        widgets = {
            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }
        
class LeaveUpdateForm(forms.ModelForm):
    class Meta:
        model = models.LeaveModel
        fields = '__all__'
        widgets = {
            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }