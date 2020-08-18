from django.urls import path
from . import views

urlpatterns = [
    path('base', views.Base, name='base'),
    path('form', views.form, name='form'),
    path('multisel', views.multiselect, name='multisel'),
    path('media_up', views.mediaUpload, name='media_up'),
    path('django_form', views.djangoform, name='django_form'),
]