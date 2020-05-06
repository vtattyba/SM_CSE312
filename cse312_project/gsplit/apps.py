from django.apps import AppConfig


class GsplitConfig(AppConfig):
    name = 'gsplit'

    def ready(self):
        import gsplit.signals
