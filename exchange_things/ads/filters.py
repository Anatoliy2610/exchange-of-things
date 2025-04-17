from django_filters import FilterSet, ModelChoiceFilter

from exchange_things.category.models import Category
from exchange_things.condition.models import Condition

from .models import Ads


class FilterAds(FilterSet):
    category = ModelChoiceFilter(
        queryset=Category.objects.all(), label="Категория товара"
    )
    condition = ModelChoiceFilter(
        queryset=Condition.objects.all(), label="Состояние товара"
    )

    class Meta:
        model = Ads
        fields = ["category", "condition"]
