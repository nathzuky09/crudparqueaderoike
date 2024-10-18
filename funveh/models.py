from django.db import models
from django.utils import timezone


class Cargo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Area(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Funcionario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    numeroTelefono = models.CharField(max_length=15)
    email = models.EmailField()
    cargo = models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.SET_NULL)
    area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.SET_NULL)
    fecha_aprobacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Aprobacion(models.Model):
    funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)  # Relación uno a uno
    aprobacion_id = models.CharField(max_length=50, blank=True, null=True)
    fecha_aprobacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Aprobación de {self.funcionario.nombre} {self.funcionario.apellido}"

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    tipo_vehiculo = models.ForeignKey('TipoVehiculo', null=True, blank=True, on_delete=models.SET_NULL)  # Relación con TipoVehiculo
    funcionario = models.ForeignKey('Funcionario', null=True, blank=True, on_delete=models.SET_NULL)
    fecha_entrada = models.DateField(default=timezone.now)
    hora_entrada = models.TimeField(default='00:00:00')
    fecha_salida = models.DateField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.placa

class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class MovimientoVehiculo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_entrada = models.DateTimeField(default=timezone.now)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    tipo_movimiento = models.CharField(max_length=50, choices=[('entrada', 'Entrada'), ('salida', 'Salida')])
    descripcion = models.TextField(blank=True, null=True)  # Añadir este campo

    def __str__(self):
        return f"{self.vehiculo} - {self.tipo_movimiento} ({self.fecha_entrada})"


