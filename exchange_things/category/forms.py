from django import forms

from .models import Category


class CreateUpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Категория товара", "class": "form-control"}
            ),
        }
