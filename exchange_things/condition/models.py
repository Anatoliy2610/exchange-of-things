from django.db import models


class Condition(models.Model):
    name = models.CharField(
        max_length=255, unique=True, verbose_name="Состояние товара"
    )

    def __str__(self):
        return self.name
