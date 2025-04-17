from django import forms

from .models import Condition


class CreateUpdateConditionForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Состояние товара", "class": "form-control"}
            ),
        }
