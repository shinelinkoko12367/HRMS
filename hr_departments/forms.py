from django import forms
from hr_departments import models
from flatpickr import DatePickerInput

class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = models.DepartmentModel
        fields = '__all__'

class DepartmentUpdateForm(forms.ModelForm):
    class Meta:
        model = models.DepartmentModel
        fields = '__all__'