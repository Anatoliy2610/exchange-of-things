from django import forms

from .models import Status


class CreateUpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Статус объявления", "class": "form-control"}
            ),
        }
