# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-31 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Get_a_Job', '0004_auto_20180731_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('Cod_Carr', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('Cod_Curriculum', models.AutoField(primary_key=True, serialize=False)),
                ('Telefono', models.IntegerField()),
                ('Fecha_Carr', models.DateField()),
                ('Fecha_Estd', models.DateField()),
                ('Trabajo_Rect', models.CharField(max_length=50)),
                ('InstTrbj', models.CharField(max_length=50)),
                ('PeriodoTrbj', models.IntegerField()),
                ('DescripTrbj', models.CharField(max_length=2500)),
                ('OtroTrbj', models.CharField(max_length=50)),
                ('InstOtrTrbj', models.CharField(max_length=50)),
                ('PeriodoOtrTrbj', models.IntegerField()),
                ('DescripOtrTrbj', models.CharField(max_length=2500)),
                ('ObjetivoProf', models.CharField(max_length=200)),
                ('Carrera_P', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.Carreras')),
                ('Cedula_Solct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.Solicitante')),
            ],
        ),
        migrations.CreateModel(
            name='HabilidadesCarr',
            fields=[
                ('Cod_Habld', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=50)),
                ('Cod_Carr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.Carreras')),
            ],
        ),
        migrations.CreateModel(
            name='HabilidadesEstd',
            fields=[
                ('Cod_Habld', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InstEstd',
            fields=[
                ('Cod_InstEstd', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OtrosEstd',
            fields=[
                ('Cod_Estd', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Cod_InstEstd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.InstEstd')),
            ],
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('Cod_Provincia', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='habilidadesestd',
            name='Cod_Estd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.OtrosEstd'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='Direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.Provincias'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='Otro_Estd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.OtrosEstd'),
        ),
        migrations.AddField(
            model_name='carreras',
            name='InstEstd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Get_a_Job.InstEstd'),
        ),
    ]
