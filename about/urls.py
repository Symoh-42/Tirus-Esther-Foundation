from django.urls import path

from . import views

urlpatterns = [
    path("", views.aboutPage, name="about"),
    path("leadership", views.leadershipPage, name="leadership"),
    path("partnership", views.partnershipPage, name="partnership"),
    path("<str:id>", views.singleTeamPage, name="single_team"),
]