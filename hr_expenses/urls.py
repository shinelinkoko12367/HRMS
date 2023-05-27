from django.urls import path

from hr_expenses import views

urlpatterns = [
	path('show_expenses/', views.ExpensesListView.as_view(), name='expenses_list'),
  	path('new_expenses/', views.ExpensesCreateView.as_view(), name='expenses_create'),
   	path('<int:pk>/edit/', views.ExpensesUpdateView.as_view(), name='expenses_update'),
    path('<int:pk>', views.ExpensesDetailView.as_view(), name='expenses_detail'),
    path('<int:pk>/delete/', views.ExpensesDeleteView.as_view(), name='expenses_delete'),

]