from django import forms
from django.forms import modelformset_factory
from .models import Vehiculo, Funcionario, MovimientoVehiculo

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nombre', 'apellido', 'documento', 'numeroTelefono', 'email', 'cargo']

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['placa', 'color', 'modelo', 'tipoVehiculo', 'funcionario', 'fecha_entrada', 'hora_entrada', 'fecha_salida', 'hora_salida']
        widgets = {
            'fecha_entrada': forms.DateInput(attrs={'type': 'date'}),
            'hora_entrada': forms.TimeInput(attrs={'type': 'time'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time'}),
        }

# Define el formset para Vehiculo
VehiculoFormSet = modelformset_factory(
    Vehiculo,
    form=VehiculoForm,
    extra=1,  # Número de formularios adicionales para agregar nuevos vehículos
    can_delete=True  # Permite eliminar formularios
)

# Formulario para registrar movimientos de vehículo
class MovimientoVehiculoForm(forms.ModelForm):
    class Meta:
        model = MovimientoVehiculo
        fields = ['vehiculo', 'fecha_entrada', 'fecha_salida', 'tipo_movimiento', 'descripcion']
        widgets = {
            'fecha_entrada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_salida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }







        