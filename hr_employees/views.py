from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from hr_employees import models
from hr_employees import forms
from django.db.models import Q

from django.contrib.auth import logout
from django.shortcuts import redirect

class EmployeeListView(LoginRequiredMixin, ListView):
    paginate_by = 2
    login_url = reverse_lazy('login')
    model = models.EmployeeModel
    context_object_name = 'employees_list'
    template_name = 'employee_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        sq = self.request.GET.get("search_query")
        obn = self.request.GET.get("name")
        obz = self.request.GET.get("zip_code")
        search_type = self.request.GET.get("search_type")

        if sq is not None:
            if search_type == "name":
                qs = qs.filter(Q(name__icontains=sq))
            elif search_type == "street":
                qs = qs.filter(Q(street__icontains=sq))

        if obn is not None:
            qs = qs.order_by('-name')

        if obz is not None:
            qs = qs.order_by('-zip_code')

        return qs

class EmployeeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
   
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("employee_list")
    model = models.EmployeeModel
    form_class = forms.EmployeeCreateForm
    template_name = 'employee_create.html'
    success_message = "Employee %(name)s created successfully"


class EmployeeUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("employee_list")
    model = models.EmployeeModel
    form_class = forms.EmployeeUpdateForm
    context_object_name = "employee"
    template_name = 'employee_update.html'
    success_message = "Employee %(name)s updated successfully"

class EmployeeDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("employee_list")
    model = models.EmployeeModel
    context_object_name = "employee"
    template_name = 'employee_delete.html'

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.EmployeeModel
    context_object_name = "employee"
    template_name = 'employee_detail.html'
