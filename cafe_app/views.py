from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def menu(request):
    return render(request, "menu.html")


def about(request):
    return render(request, "about.html")


def team(request):
    return render(request, "team.html")
