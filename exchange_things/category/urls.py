from django.urls import path

from exchange_things.category import views

urlpatterns = [
    path("", views.CategoryHome.as_view(), name="category"),
    path("create/", views.CategoryCreate.as_view(), name="category_create"),
    path(
        "<int:category_id>/update/",
        views.CategoryUpdate.as_view(),
        name="category_update",
    ),
    path(
        "<int:category_id>/delete/",
        views.CategoryDelete.as_view(),
        name="category_delete",
    ),
]
