import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

QHONUSKAN_VOTES_PATH = os.path.dirname(
    os.path.join(PROJECT_PATH, "../", "../"))

os.sys.path.insert(0, QHONUSKAN_VOTES_PATH)

ADMIN_MEDIA_PREFIX = '/admin_media/'
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'sqlite.db'
DEBUG = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'qhonuskan_votes',
    'app')

INTERNAL_IPS = ('127.0.0.1',)

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

MEDIA_URL = '/media'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware')

ROOT_URLCONF = 'project.urls'

SECRET_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcd'

SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request')

STATIC_ROOT = os.path.join(PROJECT_PATH, "sitestatic/")

STATIC_URL = "/static/"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder")

TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
