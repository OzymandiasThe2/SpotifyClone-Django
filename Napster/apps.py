from django.apps import AppConfig


class NapsterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Napster'

    def ready(self):
        import Napster.signals
