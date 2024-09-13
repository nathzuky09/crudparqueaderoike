# miapp/urls_api.py

from django.urls import path
from .views_api import FuncionarioListCreate, FuncionarioDetail, VehiculoListCreate, VehiculoDetail


urlpatterns = [
    path('funcionarios/', FuncionarioListCreate.as_view(), name='funcionario-list-create'),
    path('funcionarios/<int:pk>/', FuncionarioDetail.as_view(), name='funcionario-detail'),
    path('vehiculos/', VehiculoListCreate.as_view(), name='vehiculo-list-create'),
    path('vehiculos/<int:pk>/', VehiculoDetail.as_view(), name='vehiculo-detail'),
    
]
