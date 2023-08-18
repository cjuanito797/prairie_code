"""
Django settings for prairie_code project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join (BASE_DIR, 'media')
MEDIA_URL = '/media/'



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5p4)@haavsi-c3p2*cy07e)a=k3*07$p+8e^qg932g&1lo$7l+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['18.117.26.68', 'prairiecode.net', 'www.prairiecode.net', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home.apps.HomeConfig",
    "django_celery_beat",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django_permissions_policy.PermissionsPolicyMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

PERMISSIONS_POLICY = {
    "accelerometer": [],
}

ROOT_URLCONF = "prairie_code.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join (BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = "prairie_code.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Chicago"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# SMTP Configutation
# SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'prairiecodellc@gmail.com'
EMAIL_HOST_PASSWORD = 'hexeyvmtspkiflzv'
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = 'prairiecodellc@gmail.com'
SERVER_EMAIL = 'prairiecodellc@gmail.com'

# Add to project/settings.py
SECURE_HSTS_SECONDS = 2592000  # Unit is seconds; *USE A SMALL VALUE FOR TESTING!*
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

MIDDLEWARE += ["csp.middleware.CSPMiddleware"]

CSP_SCRIPT_SRC = [
    "'unsafe-inline'",
    "'self'",
    "https://stackpath.bootstrapcdn.com",
    "https://cdn.jsdelivr.net",
    "https://code.jquery.com",
    "https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"
]

CSP_STYLE_SRC = [
    "https://fonts.googleapis.com/",
    "https://cdn.jsdelivr.net/",
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js",
    "'unsafe-inline'",
    "'self'",
]

CSP_FONT_SRC = [
    "https://fonts.gstatic.com/",
]

CSP_IMG_SRC = [
    "'self'",
    "https://cdnassets.hw.net/",
    "http://www.w3.org/2000/svg",
    "data:",
    "https://bulma.io/images/bulma-logo.png",
    "https://www.freepnglogos.com/uploads/javascript/logo-html-5-css-javascript-source-code-for-the-taking-23.png",
    "https://static.vecteezy.com/system/resources/previews/011/354/484/original/young-man-in-hat-holding-laptop-3d-character-illustration-png.png",
    "https://t4.ftcdn.net/jpg/02/84/69/23/360_F_284692342_FkKunloWDjhyfVsmUxxnGJQjR3fiOZ4U.jpg",
    "https://static.vecteezy.com/system/resources/previews/011/383/944/non_2x/young-girl-holding-a-trophy-3d-character-illustration-free-png.png",

]

CSP_FRAME_SRC = [
    "https://maps.google.com/maps",
    "https://www.google.com/maps/",
]

CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
