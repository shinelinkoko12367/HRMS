from django.urls import path

from hr_leave import views

urlpatterns = [
	path('show_leave/', views.LeaveListView.as_view(), name='leave_list'),
  	path('new_leave/', views.LeaveCreateView.as_view(), name='leave_create'),
   	path('<int:pk>/edit/', views.LeaveUpdateView.as_view(), name='leave_update'),
    path('<int:pk>', views.LeaveDetailView.as_view(), name='leave_detail'),
    path('<int:pk>/delete/', views.LeaveDeleteView.as_view(), name='leave_delete'),
]