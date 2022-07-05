from .base import *
if os.path.isfile('env.py'):
    import env

SECRET_KEY = 'ifoehwfgqingqojg5348423589hfbjnsd'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
