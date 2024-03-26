from django.apps import AppConfig


class DiplomAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diplom_app'


class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'

    def ready(self):
        """
        импортируем сигналы
        """