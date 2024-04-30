from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import OperacaoEstoque


def adicionar_quantidade_no_estoque(sender, instance, created, **kwargs):

    # TODO: adicionar validador de valroes negativos e validacoes de dados


    if created:
        if instance.type == "ADD":
            if instance.estoque:
                instance.produto = instance.produto
                instance.estoque.quantidade += instance.quantidade
                instance.estoque.save()

        elif instance.type == "DELETE":
            if instance.estoque:
                instance.estoque.quantidade -= instance.quantidade
                instance.estoque.save()


post_save.connect(adicionar_quantidade_no_estoque, sender=OperacaoEstoque)
