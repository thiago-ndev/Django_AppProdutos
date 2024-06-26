# Generated by Django 4.1.5 on 2024-04-30 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('appProdutos', '0002_categoria_estoque_fornecedor_alter_produto_options_and_more'),
        ('appClientes', '0002_funcionario_gerente_remove_endereco_cliente_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='fornecedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appProdutos.fornecedor'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='uf',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='rua',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AddField(
            model_name='gerente',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='gerente_groups', related_query_name='gerente', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='gerente',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='gerente_user_permissions', related_query_name='gerente', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appClientes.funcionario'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='gerente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appClientes.gerente'),
        ),
    ]
