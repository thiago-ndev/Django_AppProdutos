# Generated by Django 3.2.18 on 2023-05-10 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('senha', models.CharField(max_length=60)),
                ('data_Nasc', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=60)),
                ('bairro', models.CharField(max_length=60)),
                ('rua', models.CharField(max_length=60)),
                ('numero', models.IntegerField()),
                ('Cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appClientes.cliente')),
            ],
        ),
    ]
