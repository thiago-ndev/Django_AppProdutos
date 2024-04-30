from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager, Group, Permission

# Create your models here.


class Gerenciar_fornecedor:
    """
    Classe responsavel por gerenciar as fornecedor
    """

    def cadastrar_fornecedores(self, fornecedor):
        pass

    def deletar_fornecedores(self, idfornecedor, fornecedor):
        pass

    def atualizar_fornecedores(self, idfornecedor, fornecedor):
        pass

    def listar_fornecedores(self):
        pass


class Gerente(AbstractUser):

    class Meta:
        db_table = 'gerente'
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="gerente_groups",  # Novo related_name
        related_query_name="gerente",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="gerente_user_permissions",  # Novo related_name
        related_query_name="gerente",
    )

    nome = models.CharField(
        max_length=150,
        null=False)

    username = models.CharField(
        max_length=150,
        unique=True,
        error_messages={
            "unique": "O nome de usuario já existe",
            "required": "O nome de usuario é obrigatorio."
        },
        null=False)

    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": "O email informado já está em uso.",
            "required": "O email é obrigatorio."
        },
        max_length=150,
        null=False

    )

    objects = UserManager()

                                                        # manager funcionarios
    def cadastrar_funcionario(self, funcionario):
        pass

    def deletar_funcionario(self, idfuncionario, funcionario):
        pass

    def atualizar_funcionario(self, idfuncionario, funcionario):
        pass


                                                        # manager catergoria
    def cadastrar_categoria(self, categoria):
        pass

    def deletar_categoria(self, idcategoria, categoria):
        pass

    def atualizar_categoria(self, idcategoria,categoria):
        pass

                                                        # manager produtos
    def cadastrar_produto(self, produto):
        pass

    def deletar_produto(self, idproduto, produto):
        pass

    def atualizar_produto(self, idproduto,produto):
        pass


                                                        # manager fornecedores
    def cadastrar_fornecedor(self, fornecedor):
        pass

    def deletar_fornecedor(self, idfornecedor, fornecedor):
        pass

    def atualizar_fornecedor(self, idfornecedor, fornecedor):
        pass



    def Agendar_entrega_de_produtos(self):
        pass

    def gerar_relatorios(self):
        pass


    def acessar_Auditorias(self):
        pass

    def gerenciar_fornecedores(self):
        pass

    def realizar_backup(self):
        pass


    def avaliar_fornecedores(self):
        pass



    def __str__(self):
        return f'{self.nome}, {self.email}, {self.username}'

    def __repr__(self):
        return f'{self.nome}, {self.email}, {self.username}'



class Funcionario(User):

    class Meta:
        db_table = 'funcionario'
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    nome = models.CharField(max_length=150, null=False)
    data_Nasc = models.DateField(null=False)




    def Registrar_Entrada_Produto(self):
        pass

    def Registrar_Saida_Produto(self):
        pass

    def __str__(self):
        return f'{self.nome}, {self.email}'

    def __repr__(self):
        return f'{self.nome}, {self.email}'


class Endereco(models.Model):

    id = models.AutoField(primary_key=True)
    uf = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False)
    bairro = models.CharField(max_length=100, null=False)
    rua = models.CharField(max_length=100, null=False)
    cep = models.CharField(max_length=100, )

    fornecedor = models.ForeignKey('appProdutos.Fornecedor', on_delete=models.CASCADE, null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True)
    gerente = models.ForeignKey(Gerente, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.id},{self.uf}, {self.cidade}, {self.bairro}, {self.rua}, {self.cep}'

    def __repr__(self):
        return f'{self.id},{self.uf},{self.cidade}, {self.bairro}, {self.rua}, {self.cep}'

