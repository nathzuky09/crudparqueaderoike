from django.contrib import admin
from .models import Funcionario, Vehiculo

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Vehiculo)
