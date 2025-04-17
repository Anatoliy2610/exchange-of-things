from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CreateUpdateCategoryForm
from .models import Category


class CategoryHome(ListView):
    model = Category
    template_name = "category/category.html"
    context_object_name = "category"
    extra_context = {"title": "Категории товара"}

    def get_queryset(self):
        return Category.objects.all()


class CategoryCreate(CreateView):
    form_class = CreateUpdateCategoryForm
    model = Category
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("category")
    extra_context = {
        "title": "Создать категорию товара",
        "button_text": "Создать",
    }


class CategoryUpdate(UpdateView):
    form_class = CreateUpdateCategoryForm
    model = Category
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("category")
    pk_url_kwarg = "category_id"
    extra_context = {
        "title": "Изменить категорию товара",
        "button_text": "Изменить",
    }


class CategoryDelete(DeleteView):
    model = Category
    template_name = "actions/delete.html"
    success_url = reverse_lazy("category")
    pk_url_kwarg = "category_id"
    extra_context = {"title": "Удаление категорию товара"}
