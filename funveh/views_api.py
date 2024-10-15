# miapp/views_api.py

from rest_framework import generics
from .models import Funcionario, Vehiculo, MovimientoVehiculo
from .serializers import FuncionarioSerializer, VehiculoSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, MovimientoVehiculoSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class FuncionarioListCreate(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FuncionarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class VehiculoListCreate(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class VehiculoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    

class RegistroAPI(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"msg": "Usuario creado correctamente."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"msg": "Inicio de sesión exitoso."}, status=status.HTTP_200_OK)
        return Response({"error": "Credenciales inválidas."}, status=status.HTTP_401_UNAUTHORIZED)
    
    
class ListaMovimientosAPI(APIView):
    def get(self, request, vehiculo_id):
        # Obtiene el vehículo o devuelve 404 si no existe
        vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)

        # Filtra los movimientos del vehículo
        movimientos = MovimientoVehiculo.objects.filter(vehiculo=vehiculo)

        # Si no hay movimientos, responde con un mensaje adecuado
        if not movimientos:
            return Response(
                {"message": "No se encontraron movimientos para este vehículo."},
                status=status.HTTP_204_NO_CONTENT
            )

        # Serializa los movimientos y devuelve la respuesta
        serializer = MovimientoVehiculoSerializer(movimientos, many=True)
        return Response(serializer.data)

    def post(self, request, vehiculo_id):
        # Obtiene el vehículo o devuelve 404 si no existe
        vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)

        # Crea un nuevo movimiento
        serializer = MovimientoVehiculoSerializer(data=request.data)
        if serializer.is_valid():
            # Asocia el vehículo con el movimiento
            serializer.save(vehiculo=vehiculo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, vehiculo_id, movimiento_id):
        # Obtiene el vehículo o devuelve 404 si no existe
        vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)

        # Obtiene el movimiento por su ID
        movimiento = get_object_or_404(MovimientoVehiculo, pk=movimiento_id, vehiculo=vehiculo)

        # Serializa y actualiza los datos
        serializer = MovimientoVehiculoSerializer(movimiento, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Actualiza el movimiento con los nuevos datos
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vehiculo_id, movimiento_id):
        # Obtiene el vehículo o devuelve 404 si no existe
        vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)

        # Obtiene el movimiento por su ID
        movimiento = get_object_or_404(MovimientoVehiculo, pk=movimiento_id, vehiculo=vehiculo)

        # Elimina el movimiento
        movimiento.delete()
        return Response({"message": "Movimiento eliminado con éxito."}, status=status.HTTP_204_NO_CONTENT)
