from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CreateUpdateConditionForm
from .models import Condition


class ConditionHome(ListView):
    model = Condition
    template_name = "condition/condition.html"
    context_object_name = "condition"
    extra_context = {"title": "Состояние товара"}

    def get_queryset(self):
        return Condition.objects.all()


class ConditionCreate(CreateView):
    form_class = CreateUpdateConditionForm
    model = Condition
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("condition")
    extra_context = {
        "title": "Создать состояние товара",
        "button_text": "Создать",
    }


class ConditionUpdate(UpdateView):
    form_class = CreateUpdateConditionForm
    model = Condition
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("condition")
    pk_url_kwarg = "condition_id"
    extra_context = {
        "title": "Изменить состояние товара",
        "button_text": "Изменить",
    }


class ConditionDelete(DeleteView):
    model = Condition
    template_name = "actions/delete.html"
    success_url = reverse_lazy("condition")
    pk_url_kwarg = "condition_id"
    extra_context = {"title": "Удаление состояние товара"}
