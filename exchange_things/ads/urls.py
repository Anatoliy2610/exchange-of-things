from django.urls import path

from exchange_things.ads import views

urlpatterns = [
    path("", views.AdsHome.as_view(), name="ads"),
    path("create/", views.AdsCreate.as_view(), name="ads_create"),
    path(
        "<int:ads_id>/update/",
        views.AdsUpdate.as_view(),
        name="ads_update",
    ),
    path(
        "<int:ads_id>/delete/",
        views.AdsDelete.as_view(),
        name="ads_delete",
    ),
    path(
        "ad/<int:ad_id>/",
        views.AdShow.as_view(),
        name="ad_show",
    ),
]
