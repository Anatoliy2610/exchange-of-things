from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Category


@receiver(post_migrate)
def create_statuses(sender, **kwargs):
    if sender.name == "exchange_things.category":
        Category.objects.get_or_create(name="Одежда")
        Category.objects.get_or_create(name="Еда")
        Category.objects.get_or_create(name="Телефон")
        Category.objects.get_or_create(name="Бытовая техника")
