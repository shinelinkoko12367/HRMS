from django.urls import path

from hr_contracts import views

urlpatterns = [
	path('show_contract/', views.ContractListView.as_view(), name='contract_list'),
    path('new_contract/', views.ContractCreateView.as_view(), name='contract_create'),
    path('<int:pk>', views.ContractDetailView.as_view(), name='contract_detail'),
    path('<int:pk>/delete/', views.ContractDeleteView.as_view(), name='contract_delete'),
    path('<int:pk>/edit/', views.ContractUpdateView.as_view(), name='contract_update'),
]