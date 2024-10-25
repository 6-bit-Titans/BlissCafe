from django.shortcuts import render

from .data.home_data import coffee_data, dessert_data

# Create your views here.


def home(request):
    return render(
        request, "home.html", {"coffee_data": coffee_data, "dessert_data": dessert_data}
    )


def contacts(request):
    return render(request, "contacts.html")


def menu(request):
    return render(request, "menu.html")


def about(request):
    return render(request, "about.html")


def team(request):
    return render(request, "team.html")
