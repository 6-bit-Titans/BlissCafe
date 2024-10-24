from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("team/", views.team, name="team"),
    path("menu/", views.menu, name="menu"),
    path("about/", views.about, name="about"),
]
