from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from hr_jobs import models
from hr_jobs import forms
from django.db.models import Q

class JobListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.JobModel
    context_object_name = 'jobs_list'
    template_name = 'job_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        sq = self.request.GET.get("search_query")
        obn = self.request.GET.get("name")
        obee = self.request.GET.get("expected_employees")
        search_type = self.request.GET.get("search_type")

        if sq is not None:
            if search_type == "name":
                qs = qs.filter(Q(name__icontains=sq))
            elif search_type == "expected_employees":
                qs = qs.filter(Q(expected_employees__icontains=sq))
                
        if obn is not None:
            qs = qs.order_by('-name')

        if obee is not None:
            qs = qs.order_by('-expected_employees')

        return qs

class JobCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("job_list")
    model = models.JobModel
    form_class = forms.JobCreateForm
    template_name = 'job_create.html'
    success_message = "Job %(name)s created successfully"

class JobUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("job_list")
    model = models.JobModel
    form_class = forms.JobUpdateForm
    context_object_name = "job"
    template_name = 'job_update.html'
    success_message = "Job %(name)s updated successfully"

class JobDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("job_list")
    model = models.JobModel
    context_object_name = "job"
    template_name = 'job_delete.html'

class JobDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.JobModel
    context_object_name = "job"
    template_name = 'job_detail.html'