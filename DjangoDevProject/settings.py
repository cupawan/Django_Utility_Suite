from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv
print("Environment Loaded:")
print(load_dotenv("./django_utility_suite/.env"))
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', get_random_secret_key())

DEBUG = True

ALLOWED_HOSTS = ["cupawan.pythonanywhere.com", "127.0.0.1"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "GoogleTranslationApp",
    "RedditPostsApp",
    "YouTubeToolsApp",
    "DailyActivityLoggerApp",
    "MaintainaceApp",
    "BudgetManagerApp",
    "StravaRunWidgetApp"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "DjangoDevProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "Templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "DjangoDevProject.wsgi.application"



MONGO_DB_NAME = os.environ['MongodbDatabase']
MONGO_CONNECTION_STRING = os.environ['MongodbConnectionString']

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.mysql",
        'NAME': 'cupawan$garmindb',
        'USER': 'cupawan',
        'PASSWORD': os.environ['PawMySqlPassword'],
        'HOST': 'cupawan.mysql.pythonanywhere-services.com',
        'PORT': '3306',              
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
