import os
import dj_database_url
import django_heroku
import logging
from .base import *

debug = os.environ.get('DEVELOPMENT', False)

DATABASES = {
    'default': dj_database_url.parse(os.environ['DATABASE_URL'])
}

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('SECRET_KEY')

django_heroku.settings(locals())

DEBUG = debug
