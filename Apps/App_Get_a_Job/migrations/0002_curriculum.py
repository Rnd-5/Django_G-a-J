# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Get_a_Job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('Cod_Curriculum', models.AutoField(primary_key=True, serialize=False)),
                ('Telefono', models.IntegerField()),
                ('Celular', models.IntegerField()),
                ('Direccion', models.CharField(max_length=70)),
                ('Fecha_InicioC', models.DateField()),
                ('Fecha_FinC', models.DateField()),
                ('Fecha_IniEstd', models.DateField()),
                ('Fecha_FinEstd', models.DateField()),
                ('Trabajo_Rect', models.CharField(max_length=50)),
                ('InstTrbj', models.CharField(max_length=50)),
                ('PeriodoTrbj', models.IntegerField()),
                ('DescripTrbj', models.CharField(max_length=2500)),
                ('OtroTrbj', models.CharField(max_length=50)),
                ('InstOtrTrbj', models.CharField(max_length=50)),
                ('PeriodoOtrTrbj', models.IntegerField()),
                ('DescripOtrTrbj', models.CharField(max_length=2500)),
                ('ObjetivoProf', models.TextField(max_length=400)),
                ('Cedula_Solct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.Solicitante')),
                ('HabLab1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.HabilidadesCarr')),
                ('HabLab2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.HabilidadesEstd')),
                ('InstOtrEsd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.InstEstd')),
                ('Institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.Universidades')),
                ('Otro_Estd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.OtrosEstd')),
                ('Pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.Paises')),
                ('Provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.Provincias')),
                ('Titulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.Carreras')),
            ],
        ),
    ]
