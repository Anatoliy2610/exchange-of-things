from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CreateUpdateStatusForm
from .models import Status


class StatusHome(ListView):
    model = Status
    template_name = "status/status.html"
    context_object_name = "statuses"
    extra_context = {"title": "Статусы"}

    def get_queryset(self):
        return Status.objects.all()


class StatusCreate(CreateView):
    form_class = CreateUpdateStatusForm
    model = Status
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("statuses")
    extra_context = {
        "title": "Создать статус",
        "button_text": "Создать",
    }


class StatusUpdate(UpdateView):
    form_class = CreateUpdateStatusForm
    model = Status
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("statuses")
    pk_url_kwarg = "status_id"
    extra_context = {
        "title": "Изменить статус",
        "button_text": "Изменить",
    }


class StatusDelete(DeleteView):
    model = Status
    template_name = "actions/delete.html"
    success_url = reverse_lazy("statuses")
    pk_url_kwarg = "status_id"
    extra_context = {"title": "Удаление статуса"}
