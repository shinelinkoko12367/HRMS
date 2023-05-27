from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from hr_payroll import models
from hr_payroll import forms
from django.db.models import Q

class PayrollListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.PayroolModel
    context_object_name = 'payroll_list'
    template_name = 'payroll_list.html'
    
    
class PayrollCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("payroll_list")
    model = models.PayroolModel
    form_class = forms.PayrollCreateForm
    template_name = 'payroll_create.html'
    success_message = "Payroll %(Contract_id)s created successfully"
    
class PayrollUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("payroll_list")
    model = models.PayroolModel
    form_class = forms.PayrollUpdateForm
    context_object_name = "payroll"
    template_name = 'payroll_update.html'
    success_message = "Payroll %(Contract_id)s updated successfully"
    
class PayrollDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.PayroolModel
    context_object_name = "payroll"
    template_name = 'payroll_detail.html'
    
class PayrollDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("payroll_list")
    model = models.PayroolModel
    context_object_name = "payroll"
    template_name = 'payroll_delete.html'

from hr_contracts.models import ContractModel
from django.http import JsonResponse

def get_salary(request):
    contract_id = request.GET.get('contract_id', None)
    data = {'salary': ContractModel.objects.get(id=contract_id).salary}
    return JsonResponse(data)

from hr_leave.models import LeaveModel

def get_fine(request):
    leave_id = request.GET.get('leave_id',None)
    data= {'fine': LeaveModel.objects.get(id=leave_id).fine}
    return JsonResponse(data)