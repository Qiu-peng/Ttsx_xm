from django.shortcuts import render
from django.http import HttpResponseRedirect


def cart(request):
    return render(request, 'Cart/cart.html')

