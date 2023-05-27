from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from hr_departments import models
from hr_departments import forms
from django.db.models import Q

class DepartmentListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.DepartmentModel
    context_object_name = 'departments_list'
    template_name = 'department_list.html'
    
class DepartmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("department_list")
    model = models.DepartmentModel
    form_class = forms.DepartmentCreateForm
    template_name = 'department_create.html'
    success_message = "departments %(name)s created successfully"

class DepartmentUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("department_list")
    model = models.DepartmentModel
    form_class = forms.DepartmentUpdateForm
    context_object_name = "department"
    template_name = 'department_update.html'
    success_message = "Department %(name)s updated successfully"

class DepartmentDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("department_list")
    model = models.DepartmentModel
    context_object_name = "department"
    template_name = 'department_delete.html'
    
class DepartmentDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.DepartmentModel
    context_object_name = "department"
    template_name = 'department_detail.html'