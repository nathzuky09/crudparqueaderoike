# Generated by Django 4.2 on 2024-10-11 23:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('funveh', '0007_remove_movimientovehiculo_hora_entrada_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimientovehiculo',
            name='funcionario',
        ),
        migrations.AddField(
            model_name='movimientovehiculo',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movimientovehiculo',
            name='fecha_entrada',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='movimientovehiculo',
            name='tipo_movimiento',
            field=models.CharField(choices=[('entrada', 'Entrada'), ('salida', 'Salida')], max_length=50),
        ),
    ]
