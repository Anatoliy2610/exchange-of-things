from django.contrib.auth import get_user_model
from django.db import models

from exchange_things.category.models import Category
from exchange_things.condition.models import Condition


class Ads(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок объявления")
    description = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Описание"
    )
    image_url = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Ссылка на картинку"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="Категория товара"
    )
    condition = models.ForeignKey(
        Condition, on_delete=models.PROTECT, verbose_name="Состояние товара"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания объявления"
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        null=True
    )

    def __str__(self):
        return str(self.title)
