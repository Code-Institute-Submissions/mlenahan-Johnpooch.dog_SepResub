import os
import dj_database_url
import django_heroku
import logging
from .base import *


DATABASES = {
    'default': dj_database_url.parse(os.environ['DATABASE_URL'])
}

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ['SECRET_KEY']

django_heroku.settings(locals())

# DEBUG = os.environ.get('DEBUG', False)
DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
