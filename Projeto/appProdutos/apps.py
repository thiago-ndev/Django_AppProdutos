from django.apps import AppConfig


class AppprodutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appProdutos'

    def ready(self):
        import appProdutos.signals
