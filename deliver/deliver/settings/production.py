from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ['to-do-app-one-khaki.vercel.app']

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Static & Media
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

#Security Settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

# SQLite Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 5,
            'transaction_mode': 'IMMEDIATE',
            'init_command': """
                PRAGMA journal_mode=WAL;
                PRAGMA synchronous=NORMAL;
                PRAGMA mmap_size=134217728;
                PRAGMA journal_size_limit=67108864;
                PRAGMA cache_size=2000;
            """,
        },
    }
}
