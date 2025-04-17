from django.urls import path

from exchange_things.proposal import views

urlpatterns = [
    path("", views.ProposalHome.as_view(), name="proposal"),
    path("create/", views.ProposalCreate.as_view(), name="proposal_create"),
    path(
        "<int:proposal_id>/update/",
        views.ProposalUpdate.as_view(),
        name="proposal_update",
    ),
    path(
        "<int:proposal_id>/delete/",
        views.ProposalDelete.as_view(),
        name="proposal_delete",
    ),
    path(
        "<int:proposal_id>/",
        views.ProposalShow.as_view(),
        name="proposal_show",
    ),
]
