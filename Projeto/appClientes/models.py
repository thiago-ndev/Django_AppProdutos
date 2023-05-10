from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    senha = models.CharField(max_length=60, null=False)
    data_Nasc = models.DateField(null=False)
    
    
    def __str__(self):
        return '{}, {}, {}, {}, {},'.format(self.id, self.nome, self.email,
                                            self.senha, self.data_Nasc)
    
    def __repr__(self):
        return '{}, {}, {}, {}, {},'.format(self.id, self.nome, self.email,
                                            self.senha, self.data_Nasc)
        
class Endereco(models.Model):
    cidade = models.CharField(max_length=60, null=False)
    bairro = models.CharField(max_length=60, null=False)
    rua = models.CharField(max_length=60, null=False)
    numero = models.IntegerField(null=False) 
    
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    
    
    def __str__(self):
        return '{}, {}, {}, {}, {},'.format(self.id, self.cidade, self.bairro,
                                            self.rua, self.numero)
    
    def __repr__(self):
        return '{}, {}, {}, {}, {},'.format(self.id, self.cidade, self.bairro,
                                            self.rua, self.numero)
    
    
    