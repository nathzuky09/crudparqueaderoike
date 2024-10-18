from django.urls import path
from .views_api import FuncionarioListCreate, FuncionarioDetail, VehiculoListCreate, VehiculoDetail, RegistroAPI, LoginAPI, ListaMovimientosAPI, CargoListCreate, CargoDetail, AreaListCreate, AreaDetail, AprobacionListCreate, AprobacionDetail, TipoVehiculoListCreate, TipoVehiculoDetail  

urlpatterns = [
    path('funcionarios/', FuncionarioListCreate.as_view(), name='funcionario-list-create'),
    path('funcionarios/<int:pk>/', FuncionarioDetail.as_view(), name='funcionario-detail'),
    path('cargos/', CargoListCreate.as_view(), name='cargo-list-create'),
    path('cargos/<int:pk>/', CargoDetail.as_view(), name='cargo-detail'),
    path('areas/', AreaListCreate.as_view(), name='area-list-create'),
    path('areas/<int:pk>/', AreaDetail.as_view(), name='area-detail'),
    path('aprobaciones/', AprobacionListCreate.as_view(), name='aprobacion-list-create'),
    path('aprobaciones/<int:pk>/', AprobacionDetail.as_view(), name='aprobacion-detail'),
    path('vehiculos/', VehiculoListCreate.as_view(), name='vehiculo-list-create'),
    path('vehiculos/<int:pk>/', VehiculoDetail.as_view(), name='vehiculo-detail'),

    # Endpoint para Tipo de Vehículo
    path('tipos_vehiculo/', TipoVehiculoListCreate.as_view(), name='tipo-vehiculo-list-create'),
    path('tipos_vehiculo/<int:pk>/', TipoVehiculoDetail.as_view(), name='tipo-vehiculo-detail'),

    path('registro/', RegistroAPI.as_view(), name='registro'),  
    path('registro/<int:id>/', RegistroAPI.as_view(), name='registro'),
    path('login/', LoginAPI.as_view(), name='login'), 
    path('vehiculo/<int:vehiculo_id>/movimientos/', ListaMovimientosAPI.as_view(), name='lista_movimientos_api'),
    path('vehiculo/<int:vehiculo_id>/movimientos/', ListaMovimientosAPI.as_view(), name='crear-movimiento-api'),
    path('vehiculo/<int:vehiculo_id>/movimientos/<int:movimiento_id>/', ListaMovimientosAPI.as_view(), name='actualizar-movimiento-api'),
    path('vehiculo/<int:vehiculo_id>/movimientos/<int:movimiento_id>/', ListaMovimientosAPI.as_view(), name='eliminar-movimiento-api'),
]