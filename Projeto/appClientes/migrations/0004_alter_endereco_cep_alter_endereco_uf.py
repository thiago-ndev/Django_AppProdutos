# Generated by Django 4.1.5 on 2024-04-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appClientes', '0003_endereco_fornecedor_endereco_uf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='uf',
            field=models.CharField(max_length=100),
        ),
    ]
