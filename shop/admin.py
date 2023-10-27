from django.contrib import admin
from django.contrib.admin import AdminSite

# Register your models here.
from . import models

admin.site.register(models.Category)
admin.site.register(models.Product)

class CustomAdminSite(AdminSite):
    site_header = 'Admin Panel Onicorp Official site'
    site_title = 'Admin Panel Onicorp'
