import os
import json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
# REFRESH_TOKEN_SECRET = os.environ.get("REFRESH_TOKEN_SECRET")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS = []

ROOT_URLCONF = 'JWT_Wala_Service.urls'

WSGI_APPLICATION = 'JWT_Wala_Service.wsgi.application'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

urls_data = open('urls_config.json')
URLS = json.load(urls_data)
