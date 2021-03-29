from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 'u5h4i@k8zl$24!dhx)=22c)ue@5y%$pg)hpr&@#*wt6rcjx0)f'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'juan',
        'PASSWORD': '6val123,B',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR.child('media')
