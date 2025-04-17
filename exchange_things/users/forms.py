from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")
    username = forms.CharField(
        label="Имя пользователя",
        # help_text=HELP_TEXT_1 + HELP_TEXT_2,
    )
    email = forms.CharField(label="Email")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повторить пароль", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем существует")
        return username


class UsersChangeForm(RegisterUserForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if get_user_model().objects.filter(username=username).exists():
            if username != self.instance.username:
                raise forms.ValidationError("Пользователь с таким именем существует")
        return username
