from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_view(request, name=""):
    return HttpResponse(f"Hello World {name}")
