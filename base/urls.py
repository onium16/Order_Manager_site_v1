from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.i18n import set_language
from django.conf.urls.i18n import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')), 
    path("i18n/", include("django.conf.urls.i18n")),
 
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
