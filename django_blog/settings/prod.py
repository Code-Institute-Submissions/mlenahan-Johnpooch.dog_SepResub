import os
import dj_database_url
import django_heroku
from .base import *


DATABASES = {
    'default': dj_database_url.parse(os.environ['DATABASE_URL'])
}

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ['SECRET_KEY']

django_heroku.settings(locals())

# DEBUG = 'DEBUG' in os.environ

# DEBUG = os.environ['DEBUG_VALUE'] == 'TRUE'

DEBUG = False


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
