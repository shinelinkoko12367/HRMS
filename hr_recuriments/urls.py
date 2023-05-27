from django.urls import path

from hr_recuriments import views

urlpatterns = [
	path('show_recuriments/', views.RecurimentsListView.as_view(), name='recuriments_list'),
  	path('new_recuriments/', views.RecurimentsCreateView.as_view(), name='recuriments_create'),
   	path('<int:pk>/edit/', views.RecurimentsUpdateView.as_view(), name='recuriments_update'),
    path('<int:pk>', views.RecurimentsDetailView.as_view(), name='recuriments_detail'),
    path('<int:pk>/delete/', views.RecurimentsDeleteView.as_view(), name='recuriments_delete'),
]