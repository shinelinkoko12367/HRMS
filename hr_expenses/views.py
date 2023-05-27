from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from hr_expenses import models
from hr_expenses import forms
from django.db.models import Q

class ExpensesListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.ExpensesModel
    context_object_name = 'expenses_list'
    template_name = 'expenses_list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        sq = self.request.GET.get("search_query")
        obn = self.request.GET.get("name")
        obs = self.request.GET.get("Price")
        search_type = self.request.GET.get("search_type")

        if sq is not None:
            if search_type == "name":
                qs = qs.filter(Q(name__icontains=sq))
            elif search_type == "Price":
                qs = qs.filter(Q(salary__icontains=sq))

        if obn is not None:
            qs = qs.order_by('-name')

        if obs is not None:
            qs = qs.order_by('-Price')

        return qs
    
    
    
    
    
class ExpensesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("expenses_list")
    model = models.ExpensesModel
    form_class = forms.ExpensesCreateForm
    template_name = 'expenses_create.html'
    success_message = "Expenses %(name)s created successfully"
    
class ExpensesUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("expenses_list")
    model = models.ExpensesModel
    form_class = forms.ExpensesUpdateForm
    context_object_name = "expenses"
    template_name = 'expenses_update.html'
    success_message = "Expenses %(name)s updated successfully"
    
class ExpensesDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.ExpensesModel
    context_object_name = "expenses"
    template_name = 'expenses_detail.html'
    
class ExpensesDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("expenses_list")
    model = models.ExpensesModel
    context_object_name = "expenses"
    template_name = 'expenses_delete.html'