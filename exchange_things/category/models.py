from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=255, unique=True, verbose_name="Категория товара"
    )

    def __str__(self):
        return self.name
