from .base import *

env = environ.Env()
environ.Env.read_env()  # the .env file should be in the settings path, not the manage.py path

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG', default=True)

DATABASES = {
    'default': env.db(),  # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}
