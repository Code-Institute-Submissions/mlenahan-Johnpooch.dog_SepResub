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

DEBUG = os.environ['DEBUG_VALUE']
