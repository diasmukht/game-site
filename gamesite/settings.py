import os
from pathlib import Path
import dj_database_url  # Для работы с PostgreSQL на Railway
from django.contrib import staticfiles
from whitenoise.storage import CompressedStaticFilesStorage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pqpawx9sh$=*1nh^2th2&)_y#u8n8+#p%oy)=qn2(g_&k-bcm-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.railway.app'] # Разрешить все домены Railway

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'main',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise для статики (сразу после SecurityMiddleware)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gamesite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gamesite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Database: Используем DATABASE_URL от Railway для PostgreSQL
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Папка, куда будет собираться статика
STATICFILES_DIRS = [BASE_DIR / "static"]  # Ваша папка 'static' в корне проекта

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEMPLATES[0]['DIRS'] = [BASE_DIR / "templates"]

# WhiteNoise для продакшн статики
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

CSRF_TRUSTED_ORIGINS = [
    'https://web-production-2f2a.up.railway.app',
    'https://*.up.railway.app', # Это позволит все поддомены на railway.app
    # Если у вас есть свой домен, например 'https://www.your-domain.com', добавьте его так:
    # 'https://www.your-domain.com',
]

# Настройка перенаправлений для аутентификации
LOGIN_REDIRECT_URL = 'index' # Перенаправлять на главную страницу после успешного входа (имя URL 'home')
LOGOUT_REDIRECT_URL = 'index' # Перенаправлять на главную страницу после выхода
LOGIN_URL = 'login' # URL для перенаправления, если требуется авторизация (имя URL 'login')