from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Status


@receiver(post_migrate)
def create_statuses(sender, **kwargs):
    if sender.name == "exchange_things.status":
        Status.objects.get_or_create(name="Принято")
        Status.objects.get_or_create(name="Отклонена")
        Status.objects.get_or_create(name="Ожидает")
