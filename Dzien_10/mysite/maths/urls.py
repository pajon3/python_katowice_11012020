
from django.urls import path
from maths.views import add, sub, div, mul, sqrt, pow_view, lista_elementow

urlpatterns = [
    path('add/<int:a>/<int:b>', add),
    path('sub/<int:a>/<int:b>', sub),
    path('div/<int:a>/<int:b>', div),
    path('mul/<int:a>/<int:b>', mul),
    path('pow/<int:a>/<int:b>', pow_view),
    path('sqrt/<int:a>', sqrt),
    path('lista/',lista_elementow)
]