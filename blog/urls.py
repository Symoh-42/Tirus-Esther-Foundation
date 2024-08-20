from django.urls import path

from . import views

urlpatterns = [
    path("", views.blogsPage, name="blogs"),
    path("<slug:slug>", views.singleBlogsPage, name="single_blogs"),
]