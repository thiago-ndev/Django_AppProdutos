from django.db import models
from django.db.models.signals import post_save

# Create your models here.

class Fornecedor(models.Model):
    class Meta:
        db_table = 'fornecedor'
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, null=False)
    telefone = models.CharField(max_length=12, null=False)


    def __str__(self):
        return f'{self.id}, {self.nome}, {self.telefone}'

    def __repr__(self):
        return f'{self.id}, {self.nome}, {self.telefone}'

class Categoria(models.Model):
    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=True)
    sigla = models.CharField(max_length=10, null=True, unique=True)


    def __str__(self):
        return f'{self.id}, {self.nome}, {self.sigla}'

    def __repr__(self):
        return f'{self.id}, {self.nome}, {self.sigla}'



class Produto(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,null=False)
    preco = models.FloatField(null=False)


    class Meta:
        db_table = 'produto'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    #TODO : Relacionamento entre produto e forncedor

    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.id}, {self.nome}, {self.preco}'


    def __repr__(self):
        return f'{self.id}, {self.nome}, {self.preco}'


class Estoque(models.Model):
    class Meta:
        db_table = 'estoque'
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'

    id = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    quantidade = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f'{self.id}, {self.produto}, {self.quantidade}'

    def __repr__(self):
        return f'{self.id}, {self.produto}, {self.quantidade}'


class OperacaoEstoque(models.Model):

    class Meta:
        db_table = 'operacao_estoque'
        verbose_name = 'Operação de Estoque'
        verbose_name_plural = 'Operações de Estoque'

    cadastrar = "ADD"
    remover = "DELETE"

    operacoes = (
        ('ADD', 'Cadastrar'),
        ('DELETE', 'Remover')
    )

    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True, null=False)
    type = models.CharField(max_length=20, choices=operacoes)
    quantidade = models.IntegerField( null=False)
    
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    funcionario = models.ForeignKey('appClientes.Funcionario', on_delete=models.CASCADE, null=True)
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.id},{self.date}, {self.type} ,{self.produto}, {self.funcionario},{self.quantidade}, {self.date}'

    def __repr__(self):
        return f'{self.id},{self.date}, {self.type}, {self.produto},{self.funcionario} ,{self.quantidade}, {self.date}'
