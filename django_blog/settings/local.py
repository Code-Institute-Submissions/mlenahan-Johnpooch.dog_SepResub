from .base import *
if os.path.isfile('env.py'):
    import env

SECRET_KEY = 'ifoehwfgqingqojg5348423589hfbjnsd'

DEBUG = False

ALLOWED_HOSTS = ['django-blog-ml.herokuapp.com', 'johnpooch.dog']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
