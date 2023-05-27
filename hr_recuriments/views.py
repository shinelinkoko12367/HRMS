from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from hr_recuriments import models
from hr_recuriments import forms
from django.db.models import Q

class RecurimentsListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.RecruitmentModel
    context_object_name = 'recuriments_list'
    template_name = 'recuriments_list.html'
    
    
class RecurimentsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("recuriments_list")
    model = models.RecruitmentModel
    form_class = forms.RecruitmentCreateForm
    template_name = 'recuriments_create.html'
    success_message = "Recuriments %(name)s created successfully"
    
class RecurimentsUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("recuriments_list")
    model = models.RecruitmentModel
    form_class = forms.RecruitmentUpdateForm
    context_object_name = "recuriments"
    template_name = 'recuriments_update.html'
    success_message = "Recuriments %(name)s updated successfully"
    
class RecurimentsDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.RecruitmentModel
    context_object_name = "recuriments"
    template_name = 'Recuriments_detail.html'
    
class RecurimentsDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("recuriments_list")
    model = models.RecruitmentModel
    context_object_name = "recuriments"
    template_name = 'recuriments_delete.html'