from django_filters import FilterSet, ModelChoiceFilter

from exchange_things.status.models import Status
from exchange_things.users.models import User

from .models import ExchangeProposal


class FilterProposal(FilterSet):
    author = ModelChoiceFilter(
        queryset=User.objects.all(), label="Отправитель предложения"
    )
    recipient = ModelChoiceFilter(
        queryset=User.objects.all(), label="Получатель предложения"
    )
    status = ModelChoiceFilter(
        queryset=Status.objects.all(), label="Статус предложения"
    )

    class Meta:
        model = ExchangeProposal
        fields = ["author", "recipient", "status"]
