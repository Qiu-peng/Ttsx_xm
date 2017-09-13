from django.shortcuts import render


def cart(request):
    return render(request, 'Cart/cart.html')

