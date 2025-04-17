from django.contrib.auth import get_user_model
from django.db import models

from exchange_things.ads.models import Ads
from exchange_things.status.models import Status
from exchange_things.users.models import User


class ExchangeProposal(models.Model):
    ad_sender = models.ForeignKey(
        Ads, on_delete=models.PROTECT, verbose_name="Объявление отправителя"
    )
    ad_receiver = models.ForeignKey(
        Ads,
        on_delete=models.PROTECT,
        verbose_name="Объявление получателя",
        related_name="receiver",
    )
    comment = models.CharField(max_length=1000, verbose_name="Комментарий")
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name="Статус предложения",
        default=3,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания предложения"
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        verbose_name="Отправитель",
        related_name="author",
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Получатель",
        related_name="recipient",
    )

    def __str__(self):
        return str(self.status)
