"""
Django settings for MediaKaan project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directorios adicionales
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR = os.path.join(BASE_DIR,'static')
MEDIA_DIR = os.path.join(BASE_DIR,'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'httvtdt!@ts&p9^oes6atfxi$!fm4vrj0ny3$9li!#i(d_iotn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'mathfilters',
    'gestionUsuarios',
    'gestionArticulos',
    'gestionMensajeria'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MediaKaan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MediaKaan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# Configuración de la base de datos que utilizaremos, en nuestro caso una con MongoDB con el motor djongo para Django
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'mediakaanadb',
		'CLIENT': {
			'host': 'mongodb+srv://root:toor@mediakaanadb-mevxh.gcp.mongodb.net/test?retryWrites=true&w=majority',
			'port': 27017,
			'username': 'root',
			'password': 'toor',
		}
	}
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

LOGIN_URL = '/gestionUsuarios/iniciosesion/'

# Para informar a través de los email
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hads202018@gmail.com'
EMAIL_HOST_PASSWORD = ''
# with open('etc/credential_email.txt') as f:
#    EMAIL_HOST_PASSWORD = f.read().strip()
EMAIL_PORT = 587