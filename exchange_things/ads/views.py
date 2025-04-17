from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django_filters.views import FilterView

from exchange_things.mixin import MixinChangeAd, MixinLoginRequired

from .filters import FilterAds
from .forms import AdsSearchForm, CreateAdsForm, UpdateAdsForm
from .models import Ads


class AdsHome(FilterView, ListView):
    template_name = "ads/ads.html"
    context_object_name = "ads"
    filterset_class = FilterAds
    model = Ads
    paginate_by = 5
    extra_context = {
        "title": "Заказы",
        "button_text": "Посмотреть",
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = AdsSearchForm(self.request.GET)
        if self.form.is_valid():
            query = self.form.cleaned_data.get("q")
            if query:
                queryset = queryset.filter(
                    Q(title__icontains=query) | Q(description__icontains=query)
                )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = getattr(self, "form", AdsSearchForm())
        context["request"] = self.request
        return context


class AdsCreate(MixinLoginRequired, SuccessMessageMixin, CreateView):
    form_class = CreateAdsForm
    model = Ads
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("ads")
    extra_context = {
        "title": "Создать объявление",
        "button_text": "Создать",
    }
    success_message = "Вы создали объявление"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdsUpdate(MixinLoginRequired, MixinChangeAd, SuccessMessageMixin, UpdateView):
    form_class = UpdateAdsForm
    model = Ads
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("ads")
    pk_url_kwarg = "ads_id"
    extra_context = {
        "title": "Обновить объявление",
        "button_text": "Обновить",
    }
    success_message = "Вы изменили объявление"
    messages_for_error = "Вы не являетесь автором"
    redirect_for_error = "ads"


class AdsDelete(MixinLoginRequired, MixinChangeAd, SuccessMessageMixin, DeleteView):
    model = Ads
    template_name = "actions/delete.html"
    success_url = reverse_lazy("ads")
    pk_url_kwarg = "ads_id"
    extra_context = {"title": "Удалить объявление"}
    success_message = "Вы удалили объявление"
    messages_for_error = "Вы не являетесь автором"
    redirect_for_error = "ads"


class AdShow(DetailView):
    model = Ads
    template_name = "ads/ad.html"
    fields = [
        "title",
        "description",
        "image_url",
        "category",
        "condition",
        "created_at",
        "author",
    ]
    context_object_name = "ad"
    pk_url_kwarg = "ad_id"
    extra_context = {
        "title": "Просмотр объявления",
    }


def page_not_found_view(request, exception):
    return render(request, "404.html", status=404)
