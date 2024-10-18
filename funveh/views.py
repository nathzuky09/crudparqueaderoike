from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import FuncionarioForm, VehiculoForm, MovimientoVehiculoForm# Asegúrate de que MovimientoVehiculoForm esté importado
from .models import Funcionario, Vehiculo, MovimientoVehiculo, Cargo, Area
from django.contrib import messages
from django.utils import timezone

# vistas del proyecto 

def home(request):
    return render(request, 'index.html')  

# Registro
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página de inicio de sesión
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

# Control panel
def tasks(request):
    # Obtener todos los funcionarios y vehículos
    funcionarios = Funcionario.objects.all()
    vehiculos = Vehiculo.objects.all()

    # Asignar fecha y ID de aprobación si aún no existen
    for funcionario in funcionarios:
        if not funcionario.fecha_aprobacion:  # Si no tiene fecha de aprobación
            funcionario.fecha_aprobacion = timezone.now()
            funcionario.save()

    # Registrar movimiento de vehículo
    if request.method == 'POST':
        movimiento_form = MovimientoVehiculoForm(request.POST)
        if movimiento_form.is_valid():
            movimiento = movimiento_form.save(commit=False)
            movimiento.save()  # Guardamos el movimiento en la base de datos
            messages.success(request, 'Movimiento registrado exitosamente.')
            return redirect('tasks')  # Redirigimos a la vista de tareas
    else:
        movimiento_form = MovimientoVehiculoForm()  # Formulario vacío para POST

    # Obtener los cargos y áreas asociados a los funcionarios
    cargos = Cargo.objects.all()
    areas = Area.objects.all()

    return render(request, 'tasks.html', {
        'funcionarios': funcionarios,
        'vehiculos': vehiculos,
        'cargos': cargos,  # Pasar los cargos al template
        'areas': areas,    # Pasar las áreas al template
        'movimiento_form': movimiento_form,
    })



# Vista para mostrar cargos y áreas (opcional)
def list_cargos_areas(request):
    cargos = Cargo.objects.all()
    areas = Area.objects.all()
    return render(request, 'list_cargos_areas.html', {
        'cargos': cargos,
        'areas': areas
    })

# Crear registros para la base de datos
def create_task(request):
    if request.method == 'POST':
        funcionario_form = FuncionarioForm(request.POST)
        vehiculo_form = VehiculoForm(request.POST)
        
        if funcionario_form.is_valid() and vehiculo_form.is_valid():
            # Guardar el formulario de Funcionario
            funcionario = funcionario_form.save()

            # Si la fecha de aprobación está vacía, asignar la fecha actual
            if not funcionario.fecha_aprobacion:
                funcionario.fecha_aprobacion = timezone.now()
                funcionario.save()

            # Guardar el formulario de Vehículo
            vehiculo = vehiculo_form.save(commit=False)
            vehiculo.funcionario = funcionario  # Asociar el vehículo con el funcionario
            vehiculo.save()

            messages.success(request, 'Funcionario y Vehículo creados exitosamente.')
            return redirect('tasks')  # Redirigimos a la vista de tareas

        else:
            # Manejo de errores si los formularios no son válidos
            for field, errors in funcionario_form.errors.as_data().items():
                for error in errors:
                    messages.error(request, f"Error en {field}: {error.message}")

            for field, errors in vehiculo_form.errors.as_data().items():
                for error in errors:
                    messages.error(request, f"Error en {field}: {error.message}")

    else:
        funcionario_form = FuncionarioForm()
        vehiculo_form = VehiculoForm()

    return render(request, 'create_task.html', {
        'funcionario_form': funcionario_form,
        'vehiculo_form': vehiculo_form,
    })
    
# Movimientos del vehículo
def mostrar_movimientos(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    
    # Obtener todos los movimientos de entrada y salida del vehículo, ordenados por fecha_entrada
    movimientos = MovimientoVehiculo.objects.filter(vehiculo=vehiculo).order_by('-fecha_entrada')
    
    return render(request, 'movimientos_vehiculo.html', {
        'vehiculo': vehiculo,
        'movimientos': movimientos,
    })
    


# Registrar movimiento de vehículo
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovimientoVehiculoForm
from .models import Vehiculo, MovimientoVehiculo

def registrar_movimiento(request, id):
    vehiculo = get_object_or_404(Vehiculo, pk=id)

    if request.method == 'POST':
        form = MovimientoVehiculoForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.vehiculo = vehiculo  # Asocia el vehículo al movimiento
            movimiento.save()  # Guardamos el movimiento
            messages.success(request, 'Movimiento registrado exitosamente.')
            return redirect('tasks')
    else:
        form = MovimientoVehiculoForm()

    return render(request, 'registrar_movimiento.html', {
        'form': form,
        'vehiculo': vehiculo,
    })


def lista_movimientos(request, id):
    # Obtén el vehículo correspondiente con el id proporcionado
    vehiculo = get_object_or_404(Vehiculo, pk=id)
    # Obtén todos los movimientos asociados al vehículo
    movimientos = MovimientoVehiculo.objects.filter(vehiculo=vehiculo)

    return render(request, 'movimientos.html', {'vehiculo': vehiculo, 'movimientos': movimientos})



# Detalle de la tarea
def task_detail(request, task_id):
    vehiculo = get_object_or_404(Vehiculo, id=task_id)
    funcionario = vehiculo.funcionario  # Obtiene el funcionario asociado al vehículo
    return render(request, 'task_detail.html', {
        'vehiculo': vehiculo,
        'funcionario': funcionario
    })

# Actualizar datos o eliminar
def update_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    vehiculos = Vehiculo.objects.filter(funcionario=funcionario)

    # Crear el formset para los vehículos
    VehiculoFormSet = modelformset_factory(Vehiculo, form=VehiculoForm, extra=0)

    if request.method == 'POST':
        funcionario_form = FuncionarioForm(request.POST, instance=funcionario)
        formset = VehiculoFormSet(request.POST, queryset=vehiculos)

        if 'delete' in request.POST:
            # Eliminar funcionario y sus vehículos
            vehiculos.delete()
            funcionario.delete()
            messages.success(request, "Funcionario y vehículos eliminados exitosamente.")
            return redirect('tasks')

        if funcionario_form.is_valid() and formset.is_valid():
            funcionario_form.save()

            # Guardar los cambios en el formset de vehículos
            for form in formset:
                if form.cleaned_data.get('DELETE'):
                    vehiculo = form.instance
                    vehiculo.delete()
                else:
                    form.save()

            messages.success(request, "Datos actualizados exitosamente.")
            return redirect('tasks')
    else:
        funcionario_form = FuncionarioForm(instance=funcionario)
        formset = VehiculoFormSet(queryset=vehiculos)

    return render(request, 'update_funcionario.html', {
        'funcionario_form': funcionario_form,
        'formset': formset,
    })
    
    
# Cerrar sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

# Iniciar sesión
def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html', {
            'form': AuthenticationForm()
        })
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tasks')
            else:
                return render(request, 'inicio_sesion.html', {
                    'form': form,
                    'error': 'Usuario o contraseña incorrectos'
                })
        else:
            return render(request, 'inicio_sesion.html', {
                'form': form,
                'error': 'Formulario no válido'
            })
