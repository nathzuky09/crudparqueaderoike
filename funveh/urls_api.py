from django.urls import path
from .views_api import FuncionarioListCreate, FuncionarioDetail, VehiculoListCreate, VehiculoDetail, RegistroAPI, LoginAPI, ListaMovimientosAPI

urlpatterns = [
    path('funcionarios/', FuncionarioListCreate.as_view(), name='funcionario-list-create'),
    path('funcionarios/<int:pk>/', FuncionarioDetail.as_view(), name='funcionario-detail'),
    path('vehiculos/', VehiculoListCreate.as_view(), name='vehiculo-list-create'),
    path('vehiculos/<int:pk>/', VehiculoDetail.as_view(), name='vehiculo-detail'),
    path('registro/', RegistroAPI.as_view(), name='registro'),  
    path('login/', LoginAPI.as_view(), name='login'), 
    path('vehiculo/<int:vehiculo_id>/movimientos/', ListaMovimientosAPI.as_view(), name='lista_movimientos_api'),
    path('vehiculo/<int:vehiculo_id>/movimientos/', ListaMovimientosAPI.as_view(), name='crear-movimiento-api'),
    path('vehiculo/<int:vehiculo_id>/movimientos/<int:movimiento_id>/', ListaMovimientosAPI.as_view(), name='actualizar-movimiento-api'),
    path('vehiculo/<int:vehiculo_id>/movimientos/<int:movimiento_id>/', ListaMovimientosAPI.as_view(), name='eliminar-movimiento-api'),
]
