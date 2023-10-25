from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()

    # return HttpResponse(''.join([str(product)+ '<br>' for product in products]) )
    return render(request, 'index.html', {'products': products})