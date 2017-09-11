from django.shortcuts import render


# Create your views here.
# 首页视图
def index(request):
    return render(request, 'Goods/index.html')


