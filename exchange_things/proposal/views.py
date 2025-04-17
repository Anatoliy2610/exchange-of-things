from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django_filters.views import FilterView

from .filter import FilterProposal
from .forms import CreateProposalForm, UpdateProposalForm
from .models import ExchangeProposal


class ProposalHome(LoginRequiredMixin, FilterView, ListView):
    template_name = "proposal/proposals.html"
    context_object_name = "proposals"
    filterset_class = FilterProposal
    model = ExchangeProposal
    paginate_by = 7
    extra_context = {
        "title": "Предложения",
        "button_text": "Посмотреть",
    }

    def get_queryset(self):
        return ExchangeProposal.objects.all()


class ProposalCreate(LoginRequiredMixin, CreateView):
    form_class = CreateProposalForm
    model = ExchangeProposal
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("proposal")
    extra_context = {
        "title": "Создать предложение",
        "button_text": "Создать",
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class ProposalUpdate(LoginRequiredMixin, UpdateView):
    form_class = UpdateProposalForm
    model = ExchangeProposal
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("proposal")
    pk_url_kwarg = "proposal_id"
    extra_context = {
        "title": "Обновить предложение",
        "button_text": "Обновить",
    }


class ProposalDelete(LoginRequiredMixin, DeleteView):
    model = ExchangeProposal
    template_name = "actions/delete.html"
    success_url = reverse_lazy("proposal")
    pk_url_kwarg = "proposal_id"
    extra_context = {"title": "Удалить предложение"}


class ProposalShow(DetailView):
    model = ExchangeProposal
    template_name = "proposal/proposal.html"
    fields = ["ad_sender", "ad_receiver", "comment", "status", "created_at"]
    context_object_name = "proposal"
    pk_url_kwarg = "proposal_id"
    extra_context = {
        "title": "Просмотр предложения",
    }
