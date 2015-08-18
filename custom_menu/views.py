from django.shortcuts import render
from django.http import HttpResponse


def all_menu(request):
    return render(request, "custom_menu/base.html")
