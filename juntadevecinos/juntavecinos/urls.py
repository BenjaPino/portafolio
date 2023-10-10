from django.urls import include, path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('nosotros', views.nosotros, name='nosotros'),
    path('juntas/crear', views.crear, name='crear'),
    path('index', views.index, name='index'),
    path('form', views.form, name='form'),
    path('juntas/noticias', views.form, name='noticias'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)                 