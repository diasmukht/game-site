from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Главная страница

def shop(request):
    return render(request, 'shop.html')  # Магазин

def contact(request):
    return render(request, 'contact.html')  # Контакты

def product(request):
    return render(request, 'product-details.html')