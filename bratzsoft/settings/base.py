"""
Django settings for bratzsoft project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import re
from decouple import config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# https://docs.djangoproject.com/en/1.11/ref/settings/#session-expire-at-browser-close
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/




# Ignore 404 errors if from the Regular Expressions Below

IGNORABLE_404_URLS = [
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
]

# Admin Configs
ADMIN_SITE_HEADER = "BratzSoft"

# Auth
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'core:home'
LOGOUT_URL = 'accounts:logout'
AUTH_USER_MODEL = 'accounts.User'


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='PleaseChangeThisKey')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'bratzsoft.com', 'www.bratzsoft.com', 'localhost', 'bratzsoft.herokuapp.com']


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    #'tenant_schemas',
    'rest_framework',
    'rest_framework.authtoken',
    
]

OWN_APPS = [
    'bratzsoft.core',
    'bratzsoft.sap',
    'bratzsoft.api',

    'bratzsoft.accounts',
    'bratzsoft.courses',
]


INSTALLED_APPS = CUSTOM_APPS + DJANGO_APPS + OWN_APPS




#SHARED_APPS = CUSTOM_APPS + DJANGO_APPS + OWN_APPS

#TENANT_APPS = CUSTOM_APPS + DJANGO_APPS + OWN_APPS


#TENANT_MODEL = "accounts.Customer" # app.Model
#DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'



MIDDLEWARE_CLASSES = [
    # Enable only after Tenant Schemas is working
    #'tenant_schemas.middleware.DefaultTenantMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bratzsoft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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




WSGI_APPLICATION = 'bratzsoft.wsgi.application'





# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticsfiles')


# Django Rest Framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',

    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    #    'DEFAULT_RENDERER_CLASSES':[
    #        'rest_framework.renderers.JSONRenderer',

    #    ],
    #    'DEFAULT_PARSER_CLASSES':[
    #        'rest_framework.parsers.JSONParser',
    #    ]
}


# ENSURE HTTPS Communications for Production (DEBUG = False)
# https://docs.djangoproject.com/en/1.11/ref/settings/#secure-proxy-ssl-header
# https://docs.djangoproject.com/en/1.11/ref/settings/#secure-ssl-redirect
# https://docs.djangoproject.com/en/1.11/ref/settings/#session-cookie-secure
# https://docs.djangoproject.com/en/1.11/ref/settings/#csrf-cookie-secure

if DEBUG == False:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
else:
    pass
