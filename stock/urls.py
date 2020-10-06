from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('nature',views.nature,name='nature'),
    path('architecture',views.architecture,name='architecture'),
    path('contact',views.contact,name='contact')


]
