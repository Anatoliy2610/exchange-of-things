from django.contrib import admin
from django.urls import include, path

# from exchange_things import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("category/", include("exchange_things.category.urls")),
    path("status/", include("exchange_things.status.urls")),
    path("", include("exchange_things.ads.urls")),
    path("users/", include("exchange_things.users.urls")),
    path("condition/", include("exchange_things.condition.urls")),
    path("proposal/", include("exchange_things.proposal.urls")),
]

handler404 = "exchange_things.ads.views.page_not_found_view"
