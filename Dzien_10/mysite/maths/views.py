from django.shortcuts import render
from django.http import HttpResponse
from maths.models import Math



# Create your views here.


def add(request, a, b):
    Math.objects.create(operation = "add", a = a, b = b)
    result = a + b
    return render(request, 'maths/result.html', {'result': (result), 'operacja': 'dodawanie'})


def sub(request, a, b):
    Math.objects.create(operation="sub", a=a, b=b)
    result = (a - b)
    return render(request, 'maths/result.html', {'result': (result), 'operacja': 'odejmowanie'})


def div(request, a, b):
    Math.objects.create(operation="div", a=a, b=b)
    a = int(a)
    b = int(b)
    if b == 0:
        result = "nie dzielic przez 0"
    else:
        result = a / b
    return render(request, 'maths/result.html', {'result': (result), 'operacja': 'dzielenie'})


def mul(request, a, b):
    Math.objects.create(operation="mul", a=a, b=b)
    result = a * b
    return render(request, 'maths/result.html', {'result': (result), 'operacja': 'mnożenie'})


def pow_view(request, a, b):
    Math.objects.create(operation="pow", a=a, b=b)
    result = a ** b
    return render(request, 'maths/result.html', {'result': (result), 'operacja': 'potęga'})


def sqrt(request, a):
    Math.objects.create(operation="sqr", a=a)
    result = a ** 2
    return render(request, 'maths/result.html', {'result': (result), 'operacja': 'potęga'})



def lista_elementow(request):
    elementy = [1, 2, 3, 4, 5, 6, 'a']
    return render(
        request,
        'maths/lista.html',
        {"elements": elementy}
    )

