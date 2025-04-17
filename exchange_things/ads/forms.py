from django import forms

from .models import Ads


class CreateAdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ["title", "description", "image_url", "category", "condition"]


class UpdateAdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ["title", "description", "image_url", "category", "condition"]


class AdsSearchForm(forms.Form):
    q = forms.CharField(
        label="Поиск",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Поиск по ключевым словам...",
                "class": "container wrapper flex-grow-1",
            }
        ),
    )
