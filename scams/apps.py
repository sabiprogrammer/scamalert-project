from django.apps import AppConfig


class ScamsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scams'


def ready(self):
    import scams.signals
