from django.db import models


class Status(models.Model):
    name = models.CharField(
        max_length=255, unique=True, verbose_name="Статус объявления"
    )

    def __str__(self):
        return self.name
