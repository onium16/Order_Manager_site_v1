from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Client

from . import models

admin.site.register(models.Category, verbose_name='Categories')
admin.site.register(models.Product)
# admin.site.register(models.Client)

class CustomAdminSite(AdminSite):

    AdminSite.site_header = "Admin Panel Onicorp Official site"
    AdminSite.site_title = 'Admin Panel Onicorp'
    AdminSite.index_title = ''
    AdminSite.verbose_name_plural = "Categories"

class ClientAdmin(admin.ModelAdmin):
    list_display = ('processed', 'first_name', 'last_name', 'phone_number', 'email',  'product_name', 'category_name', 'product_price', 'currency_type',  'license_key', 'license_term', 'request_date', 'subscription_end_date',)

admin.site.register(Client, ClientAdmin)
