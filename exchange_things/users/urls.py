from django.urls import path

from exchange_things.users import views

urlpatterns = [
    path("", views.UsersHome.as_view(), name="users"),
    path("create/", views.UsersCreate.as_view(), name="user_create"),
    path(
        "<int:user_id>/update/",
        views.UsersUpdate.as_view(),
        name="user_update",
    ),
    path("<int:user_id>/delete/", views.UserDelete.as_view(), name="user_delete"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.LogoutUser.as_view(), name="logout"),
]
