import re
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-q9$hxov6f!+nxuyz3fs#g1!dpshmyr94+o59)_7igc-h_#5r+c"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
APP_NAME = "Inertia + Django + Vite + React"
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Inertia apps
    "django_vite",
    "inertia",
    # Custom apps
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Inertia middleware
    "inertia.middleware.InertiaMiddleware",
    "config.middleware.InertiaShareMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "config.context_processors.debug_mode",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# django-vite settings
# https://github.com/MrBin99/django-vite
DJANGO_VITE_DEV_MODE = DEBUG  # DEBUG - follow Django's dev mode

# Where ViteJS assets are built.
DJANGO_VITE_ASSETS_PATH = BASE_DIR / "static" / "dist"

# Vite 3 defaults to 5173. Default for django-vite is 3000, which is the default for Vite 2.
DJANGO_VITE_DEV_SERVER_PORT = 5173

# Output directory for collectstatic to put all your static files into.
STATIC_ROOT = BASE_DIR / "staticfiles"

DJANGO_VITE_MANIFEST_PATH = os.path.join(STATIC_ROOT, "manifest.json")

# Include DJANGO_VITE_ASSETS_PATH into STATICFILES_DIRS to be copied inside
# when run command python manage.py collectstatic
STATICFILES_DIRS = [DJANGO_VITE_ASSETS_PATH]

# Inertia settings
INERTIA_LAYOUT = BASE_DIR / "templates" / "index.html"


# Vite generates files with 8 hash digits
# http://whitenoise.evans.io/en/stable/django.html#WHITENOISE_IMMUTABLE_FILE_TEST
def immutable_file_test(path, url):
    # Match filename with 12 hex digits before the extension
    # e.g. app.db8f2edc0c8a.js
    return re.match(r"^.+\.[0-9a-f]{8,12}\..+$", url)


WHITENOISE_IMMUTABLE_FILE_TEST = immutable_file_test
