from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # Включаем URL-адреса из вашего приложения 'main'
    path('accounts/', include('django.contrib.auth.urls')), # Встроенные URL-адреса Django для аутентификации
]