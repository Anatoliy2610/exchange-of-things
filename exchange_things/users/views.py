from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from exchange_things.mixin import MixinDeleteUser, MixinLoginRequired, MixinUpdateUser
from exchange_things.users.forms import RegisterUserForm, UsersChangeForm
from exchange_things.users.models import User


class UsersHome(ListView):
    model = User
    template_name = "users/users.html"
    context_object_name = "user"
    extra_context = {"title": "Пользователи"}


class UsersCreate(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    model = User
    template_name = "actions/create_or_update.html"
    success_message = "Пользователь успешно зарегистрирован"
    success_url = reverse_lazy("login")
    extra_context = {
        "title": "Регистрация",
        "button_text": "Зарегистрировать",
    }


class UsersUpdate(MixinLoginRequired, MixinUpdateUser, SuccessMessageMixin, UpdateView):
    form_class = UsersChangeForm
    model = User
    template_name = "actions/create_or_update.html"
    pk_url_kwarg = "user_id"
    success_message = "Пользователь успешно изменен"
    extra_context = {
        "title": "Изменить пользователя",
        "button_text": "Изменить",
    }
    messages_for_error = "У вас нет прав на смену другого пользователя"
    redirect_for_error = reverse_lazy("users")
    success_url = reverse_lazy("users")


class UserDelete(MixinLoginRequired, MixinDeleteUser, SuccessMessageMixin, DeleteView):
    model = User
    template_name = "actions/delete.html"
    success_url = reverse_lazy("users")
    pk_url_kwarg = "user_id"
    success_message = "Пользователь был успешно удален"
    extra_context = {
        "title": "Удалить пользователя",
        "button_text": "Удалить",
    }
    flash_get = "Вы не можете удалить другого пользователя"
    redirect_for_error = "users"


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    success_message = "Вы залогинены"
    extra_context = {
        "title": "Авторизоваться",
        "button_text": "Вход",
    }

    def get_success_url(self):
        return reverse_lazy("users")


class LogoutUser(LogoutView):
    next_page = reverse_lazy("users")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы вышли из системы")
        return super().dispatch(request, *args, **kwargs)
