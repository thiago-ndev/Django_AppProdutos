from django.contrib import admin
from .models import Gerente, Endereco, Funcionario
# Register your models here.

admin.site.register(Gerente)
admin.site.register(Funcionario)
admin.site.register(Endereco)
