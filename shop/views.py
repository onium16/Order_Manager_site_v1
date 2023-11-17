from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Product, Category
from .forms import ClientForm

from django.http import FileResponse
from django.views.generic import View
import os
from django.conf import settings


# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html', {'products': products, 'categories': categories})

class LogoView(View):
    def get(self, request):
        # Путь к вашему изображению
        image_path = os.path.join(settings.BASE_DIR, 'shop/templates/email/logo.png')

        return FileResponse(open(image_path, 'rb'), content_type='image/png')

@require_POST
def change_language(request):
    response_data = {'message': 'Language changed successfully'}
    return JsonResponse(response_data)

def payment(request):
    if request.method == 'GET':
        form = ClientForm()
        return render(request, 'payment.html', {'form': form})
    elif request.method == 'POST':
        stripe_api_value = request.COOKIES.get('stripeApi', None) # get stripe_api from cookies
        print(stripe_api_value,  '- stripeApi')

        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()

            if stripe_api_value == None:
            # Добавляем параметр success=1 к URL перед редиректом
                redirect_url = reverse('index') + '?success=1'
            # Redirect to Stripe payment service
            else: 
                redirect_url = stripe_api_value

            return redirect(redirect_url)
        else:
            return render(request, 'payment.html', {'form': form})