
# -*- encoding: utf-8 -*-
import os
from .settingswrap.base import *
import dj_database_url


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django_postgrespool'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '/staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)



STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEBUG = True

ALLOWED_HOSTS = []