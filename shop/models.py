from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.category_name 
    
# Абстрактный базовый класс, который содержит общие поля для моделей Person и Employee
class Product_def(models.Model):
    product_name = models.CharField(max_length=255)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency_type = models.CharField(max_length=255)
    license_term = models.CharField(max_length=255)

    class Meta:
        abstract = True # Это указывает Django, что этот класс не должен иметь своей таблицы в базе данных

class Product(Product_def):
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_api = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self, field='default'):
        return f'{self.product_name}, {self.product_price}, {self.currency_type}, {self.license_term}'

class Client(Product_def):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=False)
    request_date = models.DateField(null=True, blank=True, default=timezone.now)  
    subscription_end_date = models.DateField(null=True, blank=True, default=timezone.now)
    license_key = models.CharField(max_length=100, null=True)
    processed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.product_name} | {self.request_date} | {self.subscription_end_date} | {self.email} | {self.processed} |'


