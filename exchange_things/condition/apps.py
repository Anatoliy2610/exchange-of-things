from django.apps import AppConfig


class ConditionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "exchange_things.condition"

    def ready(self):
        import exchange_things.condition.signals
