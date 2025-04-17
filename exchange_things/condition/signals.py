from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Condition


@receiver(post_migrate)
def create_statuses(sender, **kwargs):
    if sender.name == "exchange_things.category":
        Condition.objects.get_or_create(name="Новое")
        Condition.objects.get_or_create(name="Поврежденное")
        Condition.objects.get_or_create(name="Б/У")
        Condition.objects.get_or_create(name="Идеально")
