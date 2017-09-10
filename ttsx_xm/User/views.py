from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'User/login.html')

def register(request):
    return render(request, 'User/register.html')


