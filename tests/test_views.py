import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client
from django.utils import timezone
from funveh.models import Funcionario, Vehiculo, MovimientoVehiculo
from django.contrib.auth.forms import AuthenticationForm
from django.forms import modelformset_factory

@pytest.mark.django_db
@pytest.fixture
def test_user():
    # Crea un usuario de prueba para las pruebas de inicio de sesión
    return get_user_model().objects.create_user(username='testuser', password='password123')

@pytest.mark.django_db
@pytest.fixture
def test_funcionario():
    # Crea un funcionario para pruebas
    return Funcionario.objects.create(nombre="Funcionario 1", aprobacion_id=1, fecha_aprobacion=timezone.now())

@pytest.mark.django_db
@pytest.fixture
def test_vehiculo(test_funcionario):
    # Crea un vehículo para pruebas
    return Vehiculo.objects.create(placa="ABC123", funcionario=test_funcionario)

@pytest.fixture
def client():
    return Client()

# Test Home view
@pytest.mark.django_db
def test_home(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert 'index.html' in [template.name for template in response.templates]

# Test Signup view
@pytest.mark.django_db
def test_signup(client):
    response = client.get(reverse('signup'))
    assert response.status_code == 200
    assert 'signup.html' in [template.name for template in response.templates]

    # Probar con datos correctos
    data = {'username': 'newuser', 'password1': 'password123', 'password2': 'password123'}
    response = client.post(reverse('signup'), data)
    assert response.status_code == 302  # Redirige a login

# Test Tasks view
@pytest.mark.django_db
def test_tasks(client, test_user, test_funcionario, test_vehiculo):
    client.login(username='testuser', password='password123')

    response = client.get(reverse('tasks'))
    assert response.status_code == 200
    assert 'tasks.html' in [template.name for template in response.templates]
    assert test_funcionario in response.content.decode()
    assert test_vehiculo in response.content.decode()

# Test Task Detail view
@pytest.mark.django_db
def test_task_detail(client, test_user, test_vehiculo):
    client.login(username='testuser', password='password123')

    response = client.get(reverse('task_detail', args=[test_vehiculo.id]))
    assert response.status_code == 200
    assert 'task_detail.html' in [template.name for template in response.templates]
    assert test_vehiculo.placa in response.content.decode()

# Test Create Task view
@pytest.mark.django_db
def test_create_task(client, test_user):
    client.login(username='testuser', password='password123')

    response = client.get(reverse('create_task'))
    assert response.status_code == 200
    assert 'create_task.html' in [template.name for template in response.templates]

    # Prueba con datos correctos
    data = {
        'funcionario_form-0-nombre': 'Funcionario Test',
        'vehiculo_form-0-placa': 'XYZ456',
    }
    response = client.post(reverse('create_task'), data)
    assert response.status_code == 302  # Redirige a tasks

# Test Update Funcionario view
@pytest.mark.django_db
def test_update_funcionario(client, test_user, test_funcionario):
    client.login(username='testuser', password='password123')

    response = client.get(reverse('update_funcionario', args=[test_funcionario.id]))
    assert response.status_code == 200
    assert 'update_funcionario.html' in [template.name for template in response.templates]

    # Prueba de actualización
    data = {'funcionario_form-nombre': 'Funcionario Modificado'}
    response = client.post(reverse('update_funcionario', args=[test_funcionario.id]), data)
    assert response.status_code == 302  # Redirige a tasks

# Test Registrar Movimiento view
@pytest.mark.django_db
def test_registrar_movimiento(client, test_user, test_vehiculo):
    client.login(username='testuser', password='password123')

    response = client.get(reverse('registrar_movimiento', args=[test_vehiculo.id]))
    assert response.status_code == 200
    assert 'registrar_movimiento.html' in [template.name for template in response.templates]

    # Prueba con datos correctos
    data = {'fecha_entrada': '2024-10-01T10:00', 'fecha_salida': '2024-10-01T12:00'}
    response = client.post(reverse('registrar_movimiento', args=[test_vehiculo.id]), data)
    assert response.status_code == 302  # Redirige a tasks

# Test Lista Movimientos view
@pytest.mark.django_db
def test_lista_movimientos(client, test_user, test_vehiculo):
    client.login(username='testuser', password='password123')

    response = client.get(reverse('lista_movimientos', args=[test_vehiculo.id]))
    assert response.status_code == 200
    assert 'movimientos.html' in [template.name for template in response.templates]
    assert test_vehiculo.placa in response.content.decode()

# Test cerrar_sesion view
@pytest.mark.django_db
def test_cerrar_sesion(client, test_user):
    client.login(username='testuser', password='password123')

    response = client.get(reverse('cerrar_sesion'))
    assert response.status_code == 302  # Redirige a home
    assert not client.session.get('_auth_user_id')  # Verifica que no hay sesión activa

# Test Inicio Sesion view
@pytest.mark.django_db
def test_inicio_sesion(client, test_user):
    response = client.get(reverse('inicio_sesion'))
    assert response.status_code == 200
    assert 'inicio_sesion.html' in [template.name for template in response.templates]

    # Probar con credenciales correctas
    data = {'username': 'testuser', 'password': 'password123'}
    response = client.post(reverse('inicio_sesion'), data)
    assert response.status_code == 302  # Redirige a tasks
