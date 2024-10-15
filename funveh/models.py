from django.db import models
from django.utils import timezone

class Funcionario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    numeroTelefono = models.CharField(max_length=15)
    email = models.EmailField()
    cargo = models.CharField(max_length=100, default='Sin especificar')
    aprobacion_id = models.CharField(max_length=50, blank=True, null=True)
    fecha_aprobacion = models.DateField(blank=True, null=True)
    area = models.CharField(max_length=100, default='Sin especificar')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    tipoVehiculo = models.CharField(max_length=30)
    funcionario = models.ForeignKey('Funcionario', null=True, blank=True, on_delete=models.SET_NULL)
    fecha_entrada = models.DateField(default=timezone.now)
    hora_entrada = models.TimeField(default='00:00:00')
    fecha_salida = models.DateField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.placa


class MovimientoVehiculo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_entrada = models.DateTimeField(default=timezone.now)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    tipo_movimiento = models.CharField(max_length=50, choices=[('entrada', 'Entrada'), ('salida', 'Salida')])
    descripcion = models.TextField(blank=True, null=True)  # Añadir este campo

    def __str__(self):
        return f"{self.vehiculo} - {self.tipo_movimiento} ({self.fecha_entrada})"


