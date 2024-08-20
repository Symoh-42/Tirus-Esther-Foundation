from pathlib import Path
import os
import pymysql

pymysql.version_info = (1, 4, 6, "final", 0)
pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-4gjn$57!70omb*b^i)@c(sq70az1)3jkokkpia(rvdwr1=cutv'

DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Internal Apps
    'about.apps.AboutConfig',
    'accounts.apps.AccountsConfig',
    'blog.apps.BlogConfig',
    'contact.apps.ContactConfig',
    'dashboard.apps.DashboardConfig',
    'programs.apps.ProgramsConfig',
    'projects.apps.ProjectsConfig',
    'storycards.apps.StorycardsConfig',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.sites', # must
    'allauth', # must
    'allauth.account', # must
    'allauth.socialaccount', # must
    'allauth.socialaccount.providers.google', # new
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Man Made
                "dashboard.context_processors.unread_inquires",
                "dashboard.context_processors.allPrograms",
                "dashboard.context_processors.allProjects",
                "core.context_processors.all_settings",
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "v2_t&e_foundation",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "3306",
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "tirusandesther_v1",
#         "USER": "tirusandesther_v1",
#         "PASSWORD": "Cx;i04uLcKj0",
#         "HOST": "localhost",
#         "PORT": "3306",
#     }
# }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/images/'
STATIC_ROOT = BASE_DIR / "core/static"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT =  os.path.join(BASE_DIR, 'static/images')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CKEditor Settings
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "width": "auto",
        "extraPlugins": ",".join(
            [
                "codesnippet",
            ]
        ),
    },
}

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ],

        "AUTH_PARAMS": {
            "access_type": "online",
        }
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'