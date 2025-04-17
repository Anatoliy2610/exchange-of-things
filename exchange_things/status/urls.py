from django.urls import path

from exchange_things.status import views

urlpatterns = [
    path("", views.StatusHome.as_view(), name="statuses"),
    path("create/", views.StatusCreate.as_view(), name="status_create"),
    path(
        "<int:status_id>/update/",
        views.StatusUpdate.as_view(),
        name="status_update",
    ),
    path(
        "<int:status_id>/delete/",
        views.StatusDelete.as_view(),
        name="status_delete",
    ),
]
