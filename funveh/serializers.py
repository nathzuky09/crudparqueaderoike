# miapp/serializers.py

from rest_framework import serializers
from .models import Funcionario, Vehiculo
from django.contrib.auth.models import User


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


