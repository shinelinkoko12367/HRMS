from django import forms
from  hr_recuriments import models
from flatpickr import DatePickerInput

class RecruitmentCreateForm(forms.ModelForm):
    class Meta:
        model = models.RecruitmentModel
        fields = '__all__'
        widgets = {
        'birthday': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }

class RecruitmentUpdateForm(forms.ModelForm):
    class Meta:
        model = models.RecruitmentModel
        fields = '__all__'
        widgets = {
        'birthday': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }