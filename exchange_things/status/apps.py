from django.apps import AppConfig


class StatusConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "exchange_things.status"

    def ready(self):
        import exchange_things.status.signals
