from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.


def home_page(request):
    return HttpResponse('<html><title>Listy rzeczy do zrobienia</title></html>')
