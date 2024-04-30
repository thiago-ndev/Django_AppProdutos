from django.contrib import admin
# Register your models here.
from .models import Fornecedor, Produto, Estoque, Categoria, OperacaoEstoque

admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(OperacaoEstoque)
admin.site.register(Estoque)
admin.site.register(Categoria)


