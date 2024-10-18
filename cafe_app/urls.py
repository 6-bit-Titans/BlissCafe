from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="about"),
    path("contacts/", views.contacts, name="about"),
    path("team/", views.team, name="about"),
    path("menu/", views.menu, name="about"),
    path("about/", views.about, name="about"),
]
