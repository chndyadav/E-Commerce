from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "shops/index.html")

