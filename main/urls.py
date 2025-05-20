from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('shop/', views.shop, name='shop'),  # Страница магазина
    path('contact/', views.contact, name='contact'),  # Контакты
    path('product/', views.product, name='product'),
]
