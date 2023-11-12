from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Product, Category
from .forms import ClientForm

# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html', {'products': products, 'categories': categories})

@require_POST
def change_language(request):
    response_data = {'message': 'Language changed successfully'}
    return JsonResponse(response_data)

def payment(request):
    if request.method == 'GET':
        form = ClientForm()
        return render(request, 'payment.html', {'form': form})
    elif request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'payment.html', {'form': form})

# def payment_view(request):
#     productId = request.GET.get('productId')
#     productName = request.GET.get('productName')
#     licenseTerm = request.GET.get('licenseTerm')
#     categoryName = request.GET.get('categoryName')
#     productPrice = request.GET.get('productPrice')
#     currencyType = request.GET.get('currencyType')

#     # Передаем эти значения в контекст формы
#     context = {
#         'productId': productId,
#         'productName': productName,
#         'licenseTerm': licenseTerm,
#         'categoryName': categoryName,
#         'productPrice': productPrice,
#         'currencyType': currencyType,
#     }

#     return render(request, 'payment.html', context)
