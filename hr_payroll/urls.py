from django.urls import path

from hr_payroll import views

urlpatterns = [
	path('show_payroll/', views.PayrollListView.as_view(), name='payroll_list'),
  	path('new_payroll/', views.PayrollCreateView.as_view(), name='payroll_create'),
   	path('<int:pk>/edit/', views.PayrollUpdateView.as_view(), name='payroll_update'),
    path('<int:pk>', views.PayrollDetailView.as_view(), name='payroll_detail'),
    path('<int:pk>/delete/', views.PayrollDeleteView.as_view(), name='payroll_delete'),

    path('get_salary/', views.get_salary, name="get_salary"),
    path('get_fine/', views.get_fine, name="get_fine"),
]