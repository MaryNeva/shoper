from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:slug_product>/', views.show_product, name='product-detail'),
    path('', views.show_section, name='section-detail'),


]