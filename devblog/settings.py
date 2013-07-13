###############################################################################
# Custom Project Setup.

import os
import sys
ROOT_PATH = os.path.dirname(__file__)
PROJECT_ROOT_PATH = os.path.abspath(os.path.join(ROOT_PATH, '..'))
GLOBAL_ROOT_PATH = '/Users/Samir/Documents/Development/django_sites/'
sys.path.insert(0, os.path.join(GLOBAL_ROOT_PATH, "packages"))

# Title of Blog
CK_SITE_TITLE = 'Coder Ex Gamer'

# Use JS libraries hosted locally
CK_LOCAL_JS_LIBRARIES = True

# Number of posts to display per page.
CK_METABLOG_PER_PAGE_COUNT = 5

# Ping google on publishing a post
CK_METABLOG_PING_GOOGLE = False


###############################################################################
# Django settings for devblog project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Operations', 'operations@cinekine.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ckblog',                # Or path to database file if using sqlite3.
        'USER': 'cinekine',              # Not used with sqlite3.
        'PASSWORD': 'cinekine',          # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT_PATH, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(GLOBAL_ROOT_PATH, 'static'),
    os.path.join(ROOT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y3#76c-vo!h8+f5!k$fdf5!527bx%(d^*aalfs+h$!9ifwq=bp'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django_mobile.loader.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    # Django mobile
    "django_mobile.context_processors.flavour",
    # custom context processors
    "cinekine.context_processors.config",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

ROOT_URLCONF = 'devblog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'devblog.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    # Sitemap
    'django.contrib.sitemaps',

    # database
    'south',
    # tracking
    # 'tracking',
    # text editor
    'wysihtml5',
    # Disqus commenting (django-disqus)
    'disqus',
    # Mobile detection and template processor
    'django_mobile',
    # blog app
    'cinekine.metablog',
    # local apps
    'devblog'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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


###############################################################################
# WYSIHTML5 SETTINGS

WYSIHTML5_ALLOWED_TAGS = ('h1 h2 h3 h4 h5 h6 div p b i u'
                          ' ul ol li span img a blockquote pre code samp')


###############################################################################
# DISQUS SETTINGS

DISQUS_API_KEY = 'QUfzIeg85vnglA9TBjIdLqN5RlWUTA0XeFiD0i8st3Tuk1xOL3flvMQRVIKpPlLJ'
DISQUS_WEBSITE_SHORTNAME = 'coderxgamer'

###############################################################################
# MOBILE SETTINGS

FLAVOURS = ('full', 'mobile')
FLAVOURS_TEMPLATE_PREFIX = 'variants/'
FLAVOURS_GET_PARAMETER = 'variant'
FLAVOURS_SESSION_KEY = 'variant'