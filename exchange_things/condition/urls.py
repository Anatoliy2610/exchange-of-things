from django.urls import path

from exchange_things.condition import views

urlpatterns = [
    path("", views.ConditionHome.as_view(), name="condition"),
    path("create/", views.ConditionCreate.as_view(), name="condition_create"),
    path(
        "<int:condition_id>/update/",
        views.ConditionUpdate.as_view(),
        name="condition_update",
    ),
    path(
        "<int:condition_id>/delete/",
        views.ConditionDelete.as_view(),
        name="condition_delete",
    ),
]
