# Generated by Django 3.2.18 on 2023-05-10 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appClientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='Cliente_id',
            new_name='Cliente',
        ),
    ]
