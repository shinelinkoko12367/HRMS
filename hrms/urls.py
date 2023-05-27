from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings  
from django.conf.urls.static import static  

from hr_employees import views as em
from account import views 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', em.EmployeeListView.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/profile/', em.EmployeeListView.as_view()),

    path('account/', views.account_view, name="account"),
    path('hr_employees/', include('hr_employees.urls')), 
    path('hr_contracts/', include('hr_contracts.urls')), 
    path('hr_jobs/', include('hr_jobs.urls')), 
    path('hr_departments/', include('hr_departments.urls')),
    
    path('hr_expenses/', include('hr_expenses.urls')),
    
    path('hr_leave/', include('hr_leave.urls')),
    
    path('hr_recuriments/', include('hr_recuriments.urls')),
    
    path('hr_payroll/', include('hr_payroll.urls')),
]
