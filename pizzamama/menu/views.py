from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

# Acces par : /menu
def index(request):
    """
    pizzaNameAndPrice = [pizza.nom + " : " + str(pizza.prix) + "€" for pizza in pizzas]
    pizzaNameAndPriceStr = ", ".join(pizzaNameAndPrice)
    return HttpResponse("Les pizzas : " + pizzaNameAndPriceStr )"""
    pizzas = Pizza.objects.all()
    return render(request, 'menu/index.html', {'pizzas' : pizzas})