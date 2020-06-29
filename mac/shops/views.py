from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index(request):
    products = Product.objects.all()
    n = len(products)
    nslide = n // 4 + ceil((n / 4) - (n // 4))
    params = {"no_of_slides": nslide, "range": range(1, nslide), "product": products}
    return render(request, "shops/index.html", params)

