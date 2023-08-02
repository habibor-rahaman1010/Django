from django.urls import path;
from .import views

urlpatterns = [
    path('', views.showProducts, name='product')
]
