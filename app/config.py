import os
from dotenv import dotenv_values

environ = dotenv_values()

PRODUCTION = bool(int(environ.get('PRODUCTION', os.environ.get('PRODUCTION'))))

if PRODUCTION:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = bool(int(os.environ.get('DEBUG')))
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DB_ENGINE'),
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }

else:
    SECRET_KEY = environ.get('SECRET_KEY')
    DEBUG = not PRODUCTION
    ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS').split(',')
    DATABASES = {
        'default': {
            'ENGINE': environ.get('DB_ENGINE'),
            'NAME': environ.get('DB_NAME'),
            'USER': environ.get('DB_USER'),
            'PASSWORD': environ.get('DB_PASSWORD'),
            'HOST': environ.get('DB_HOST'),
            'PORT': environ.get('DB_PORT'),
        }
    }
