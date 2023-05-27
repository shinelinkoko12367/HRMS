from django.contrib import admin

# Register your models here.
from .models import LeaveModel

admin.site.register(LeaveModel)