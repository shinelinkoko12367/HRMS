from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from hr_leave import models
from hr_leave import forms
from django.db.models import Q

class LeaveListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.LeaveModel
    context_object_name = 'leave_list'
    template_name = 'leave_list.html'
    
    
class LeaveCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("leave_list")
    model = models.LeaveModel
    form_class = forms.LeaveCreateForm
    template_name = 'leave_create.html'
    success_message = "Leave %(leave)s created successfully"
    
class LeaveUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("leave_list")
    model = models.LeaveModel
    form_class = forms.LeaveUpdateForm
    context_object_name = "leave"
    template_name = 'leave_update.html'
    success_message = "Leave %(leave)s updated successfully"
    
class LeaveDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.LeaveModel
    context_object_name = "leave"
    template_name = 'leave_detail.html'
    
class LeaveDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("leave_list")
    model = models.LeaveModel
    context_object_name = "leave"
    template_name = 'leave_delete.html'