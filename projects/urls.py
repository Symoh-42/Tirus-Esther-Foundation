from django.urls import path

from . import views

urlpatterns = [
    path("", views.projectsPage, name="projects"),
    path("<slug:slug>", views.singleProjectPage, name="single_project"),
]