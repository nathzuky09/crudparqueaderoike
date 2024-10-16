# Generated by Django 4.2 on 2024-10-17 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funveh', '0014_remove_funcionario_aprobacion_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aprobacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprobacion_id', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_aprobacion', models.DateField(blank=True, null=True)),
                ('funcionario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='funveh.funcionario')),
            ],
        ),
    ]
