# miapp/serializers.py

from rest_framework import serializers
from .models import Funcionario, Vehiculo, MovimientoVehiculo, Cargo, Area, Aprobacion, TipoVehiculo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class AprobacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aprobacion
        fields = ['id', 'funcionario', 'aprobacion_id', 'fecha_aprobacion']

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
class TipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = ['id', 'nombre']       


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Eliminar confirm_password antes de guardar
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Encriptar la contraseña
        user.save()
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs.get('confirm_password'):
            raise serializers.ValidationError("Las contraseñas no coinciden.")
        return attrs


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError('Credenciales inválidas')
        else:
            raise serializers.ValidationError('Ambos campos son obligatorios')
        
        return attrs


class MovimientoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoVehiculo
        fields = ['fecha_entrada', 'fecha_salida', 'vehiculo']
            