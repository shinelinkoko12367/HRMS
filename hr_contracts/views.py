from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from hr_contracts import models
from hr_contracts import forms
from django.db.models import Q

class ContractListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.ContractModel
    context_object_name = 'contracts_list'
    template_name = 'contract_list.html'
    

    def get_queryset(self):
        qs = super().get_queryset()
        sq = self.request.GET.get("search_query")
        obn = self.request.GET.get("name")
        obs = self.request.GET.get("salary")
        search_type = self.request.GET.get("search_type")

        if sq is not None:
            if search_type == "name":
                qs = qs.filter(Q(name__icontains=sq))
            elif search_type == "salary":
                qs = qs.filter(Q(salary__icontains=sq))

        if obn is not None:
            qs = qs.order_by('-name')

        if obs is not None:
            qs = qs.order_by('-salary')

        return qs

class ContractCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("contract_list")
    model = models.ContractModel
    form_class = forms.ContractCreateForm
    template_name = 'contract_create.html'
    success_message = "Contract %(name)s created successfully"

class ContractUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("contract_list")
    model = models.ContractModel
    form_class = forms.ContractUpdateForm
    context_object_name = "contract"
    template_name = 'contract_update.html'
    success_message = "Contract %(name)s updated successfully"

class ContractDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("contract_list")
    model = models.ContractModel
    context_object_name = "contract"
    template_name = 'contract_delete.html'

class ContractDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.ContractModel
    context_object_name = "contract"
    template_name = 'contract_detail.html'