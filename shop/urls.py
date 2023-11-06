from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('change-language', views.change_language, name='change_language'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])