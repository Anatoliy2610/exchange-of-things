from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect


class MixinLoginRequired(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                self.request,
                "Вы не авторизованы! Пожалуйста, авторизуйтесь",
            )
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)


class MixinChangeAd:
    messages_for_error = None
    redirect_for_error = None

    def get(self, request, *args, **kwargs):
        if self.get_object().author != self.request.user:
            messages.error(
                self.request, "Вносить изменения в объявление может только его автор."
            )
            return redirect(self.redirect_for_error)
        if not self.get_object():
            messages.error(self.request, "Объявления не существует")
            return redirect(self.redirect_for_error)
        return super().get(request, *args, **kwargs)


class MixinUpdateUser(UserPassesTestMixin):
    messages_for_error = None
    redirect_for_error = None

    def test_func(self):
        if self.get_object() != self.request.user:
            messages.error(self.request, (self.messages_for_error))
            return redirect(self.redirect_for_error)
        return self.get_object() == self.request.user


class MixinDeleteUser:
    flash_get = None
    flash_post = None
    redirect_for_error = None

    def get(self, request, *args, **kwargs):
        if self.get_object().username != self.request.user:
            messages.error(self.request, (self.flash_get))
            return redirect(self.redirect_for_error)
        return super().get(request, *args, **kwargs)
