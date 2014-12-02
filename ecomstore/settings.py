"""
Django settings for ecomstore project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=!pnqpdeuxdl5c7akng%h_2v7y)3fjb2^0-2$z7hg=3r=w_swf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

SITE_NAME = 'ecomstore'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'preview',
    'catalog',
    'utils',
    'cart',
    # 'django_pdb',
    # 'bootstrap3',
    'registration', 

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_pdb.middleware.PdbMiddleware',

)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'utils.context_processors.ecomstore',
)


ROOT_URLCONF = 'ecomstore.urls'

WSGI_APPLICATION = 'ecomstore.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecomstore',
        'USER': 'root',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
# import dj_database_url

# DATABASES['default'] =  dj_database_url.config()

# TEMPLATE_DIRS = {os.path.join(os.path.dirname(__file__), 'templates'),}
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REGISTRATION_OPEN = True                # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'  # The page users are directed to if they are not logged in,
                                                                # and are trying to access pages requiring authentication

# # Cookie name. This can be whatever you want.
# SESSION_COOKIE_NAME = 'sessionid'
# # The module to store sessions data.
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# # Age of cookie, in seconds (default: 2 weeks).
# SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2
# # Whether a user's session cookie expires when the Web browser is closed
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# # Whether the session cookie should be secure (https:// only).
# SESSION_COOKIE_SECURE = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles/')

# STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     ('assets', '/home/yuva/Desktop/django-python/ecomstore/static'),
# )

STATIC_PATH = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/' # You may find this is already defined as such.

STATICFILES_DIRS = (
    STATIC_PATH,
)

