# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p+19yorjq@c4&nool3wp*1qge)b!j^#=tc=8=*_z_3mbz_jic!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False  # Depends on DEBUG being equal to True
ALLOWED_HOSTS = ['cion.50carleton.com', 'norontcrew.cionorth.ca']

ADMINS = (
    ('Trevor', 'trevor@50carleton.com'),
)

ROOT_URLCONF = 'cion_crew.urls'
WSGI_APPLICATION = 'cion_crew.wsgi.application'

# Application definition
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'longerusernameandemail',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'skills',
    'search',
    'ckeditor',
    'cion_crew'
)


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cion_crew',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = ''
STATIC_URL = '/static/'

MEDIA_ROOT = '%s/%s/' % (PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Email Settings
EMAIL_HOST = 'mail.50carleton.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_SUBJECT_PREFIX = '[CION Crew] '

LOGIN_REDIRECT_URL = '/skills/profile/'
GRAPPELLI_ADMIN_TITLE = "CION Crew Database"
LOGIN_URL = '/'

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [      'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline',
              '-', 'SpellChecker', 'Scayt',
              '-', 'Maximize',
            ],
            [      'HorizontalRule',
              '-', 'BulletedList', 'NumberedList',
              '-', 'SpecialChar',
            ]
        ],
        'width': 940,
        'height': 100,
        'toolbarCanCollapse': False,
    }
}
