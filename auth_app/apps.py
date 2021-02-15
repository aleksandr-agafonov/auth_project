from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    name = 'auth_app'

    def ready(self):
        from . import updater
        updater.check_links_scheduller()
