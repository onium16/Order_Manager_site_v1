from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

@require_POST
def change_language(request):
    # Ваш код для изменения языка
    # Этот код должен обработать POST-запрос и установить новый язык
    
    # Возвращаем JSON-ответ
    response_data = {'message': 'Language changed successfully'}
    return JsonResponse(response_data)