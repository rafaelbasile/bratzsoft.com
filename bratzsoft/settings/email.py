"""
Django settings for bratzsoft project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from decouple import config

# Admin Email Notifications
SERVER_EMAIL = config('ERROR_SERVER_EMAIL', default='errors@bratzsoft.com')
ADMINS = config('ADMINS', default=[('Eduardo Bratz', 'ebratz@gmail.com')])
EMAIL_HOST = config('SMTP_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('SMTP_PORT', default='587')
EMAIL_HOST_USER = config('SMTP_USER', default='')
EMAIL_HOST_PASSWORD = config('SMTP_PASSWORD', default='')
EMAIL_USE_TLS = config('SMTP_TLS', default=True)
EMAIL_USE_SSL = config('SMTP_SSL', default=False)
CONTACT_EMAIL = config('CONTACT_MAIL', default=[('Contact', 'contact@bratzsoft.com')])
