from django.urls import path

from . import views

urlpatterns = [
    path("", views.programsPage, name="programs"),
    path("<slug:slug>", views.singleProgramsPage, name="single_program"),
]