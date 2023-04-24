from config.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '65.21.113.45:1521/ORCL',  # Oracle SID or service name
        'USER': 'OWEQTOPEX',
        'PASSWORD': 'PwdDb(#)23!ora',
    }
}