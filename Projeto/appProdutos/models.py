from django.db import models

# Create your models here.

class Produto(models.Model):

    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,null=False)
    preco = models.FloatField(null=False)
    quantidade = models.IntegerField(null=False)

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.codigo, self.nome,
                                       self.preco, self.quantidade)

    def __repr__(self):
        return '{}, {}, {}, {}'.format(self.codigo, self.nome,
                                       self.preco, self.quantidade)