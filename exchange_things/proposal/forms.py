from django import forms

from exchange_things.ads.models import Ads
from exchange_things.users.models import User

from .models import ExchangeProposal


class CreateProposalForm(forms.ModelForm):
    class Meta:
        model = ExchangeProposal
        fields = ["ad_sender", "ad_receiver", "comment", "recipient"]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["ad_sender"].queryset = Ads.objects.filter(author=user)
        self.fields["ad_receiver"].queryset = Ads.objects.exclude(author=user)
        self.fields["recipient"].queryset = User.objects.exclude(username=user)


class UpdateProposalForm(forms.ModelForm):
    class Meta:
        model = ExchangeProposal
        fields = ["status"]
