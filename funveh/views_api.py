# miapp/views_api.py

from rest_framework import generics
from .models import Funcionario, Vehiculo, MovimientoVehiculo
from .serializers import FuncionarioSerializer, VehiculoSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout
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
    


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer

class RegistroAPI(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"msg": "Usuario creado correctamente."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        # Si se proporciona un ID, se busca ese usuario específico
        if id:
            try:
                user = User.objects.get(id=id)
                serializer = UserRegisterSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        # Si no se proporciona un ID, se devuelven todos los usuarios
        else:
            users = User.objects.all()
            serializer = UserRegisterSerializer(users, many=True)  # many=True para listas
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id=None):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserRegisterSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Usuario actualizado correctamente."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response({"msg": "Usuario eliminado correctamente."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)



class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"msg": "Inicio de sesión exitoso."}, status=status.HTTP_200_OK)
        return Response({"error": "Credenciales inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        if request.user.is_authenticated:
            return Response({"msg": f"Usuario autenticado: {request.user.username}"}, status=status.HTTP_200_OK)
        return Response({"error": "Usuario no autenticado."}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        # Logout
        if request.user.is_authenticated:
            logout(request)
            return Response({"msg": "Sesión cerrada correctamente."}, status=status.HTTP_200_OK)
        return Response({"error": "No hay sesión iniciada."}, status=status.HTTP_400_BAD_REQUEST)

    
class ListaMovimientosAPI(APIView):
    # Método GET: obtiene los movimientos de un vehículo específico
    def get(self, request, vehiculo_id):
        # Obtiene el vehículo o devuelve 404 si no existe
        vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)

        # Filtra los movimientos del vehículo
        movimientos = MovimientoVehiculo.objects.filter(vehiculo=vehiculo)

        # Si no hay movimientos, responde con un mensaje adecuado
        if not movimientos.exists():  # Cambié de 'if not movimientos' a 'if not movimientos.exists()'
            return Response(
                {"message": "No se encontraron movimientos para este vehículo."},
                status=status.HTTP_204_NO_CONTENT
            )

        # Serializa los movimientos y devuelve la respuesta
        serializer = MovimientoVehiculoSerializer(movimientos, many=True)
        return Response(serializer.data)

    # Método POST: crea un nuevo movimiento
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

    # Método PUT: actualiza un movimiento existente
    def put(self, request, vehiculo_id, movimiento_id):
        # Obtiene el vehículo o devuelve 404 si no existe
        vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)

        # Obtiene el movimiento por su ID
        movimiento = get_object_or_404(MovimientoVehiculo, pk=movimiento_id, vehiculo=vehiculo)

        # Serializa y actualiza los datos
        # Asegurándote de no modificar el campo 'vehiculo' al actualizar
        serializer = MovimientoVehiculoSerializer(movimiento, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()  # Actualiza el movimiento con los nuevos datos
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método DELETE: elimina un movimiento
    def delete(self, request, vehiculo_id, movimiento_id):
        # Obtiene el vehículo o devuelve 404 si no existe
        vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)

        # Obtiene el movimiento por su ID
        movimiento = get_object_or_404(MovimientoVehiculo, pk=movimiento_id, vehiculo=vehiculo)

        # Elimina el movimiento
        movimiento.delete()
        return Response({"message": "Movimiento eliminado con éxito."}, status=status.HTTP_204_NO_CONTENT)

