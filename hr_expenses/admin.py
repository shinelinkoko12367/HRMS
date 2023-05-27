from django.contrib import admin

# Register your models here.
from .models import ExpensesModel
admin.site.register(ExpensesModel)