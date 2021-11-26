"""
Django settings for Infulencers project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_c-_9^5^a1+1(u0r78^oxtm*zl*%kd%ove2f)quxf#&)l3@w+g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['159.89.247.164','adsbyinfluence.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App',
    'social_django',
    'phonenumber_field',
    'formtools',
    'crispy_forms',
    'Checkout',
    'Notification',
    'notifications',
    'Offers',
    'Advertiser',
    'Chat',
    'channels',
    'ReleaseRequest',
    'AmountChangeRequest',
    
    
]

AUTH_USER_MODEL = 'App.Account'
CRISPY_TEMPLATE_PACK = 'bootstrap4' 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'Infulencers.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

            ],
        },
    },
]

WSGI_APPLICATION = 'Infulencers.wsgi.application'
ASGI_APPLICATION = 'Infulencers.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('159.89.247.164', 6379)],
        },
    },
}
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Influencer',
        'USER': 'doadmin',
        'PASSWORD': 'ESnOgu95cMF5Ubqk',
        'HOST': 'db-mysql-nyc3-03598-do-user-10313622-0.b.db.ondigitalocean.com',
        'PORT': '25060',
        'OPTIONS':{'charset':'utf8mb4'}
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'App.backends.AccountAuth'
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)



SOCIAL_AUTH_RAISE_EXCEPTIONS = True
RAISE_EXCEPTIONS = True
DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mightyneurons.tech@gmail.com'
EMAIL_HOST_PASSWORD = 'fdikcalznlmfcvsk'
##EMAIL_USE_SSL = True
EMAIL_USE_TLS = True

SOCIAL_AUTH_GOOGLE_OAUTH2_USER_FIELDS = ['email','username']

LOGIN_REDIRECT_URL = '/Is_Influencer'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = 'Login'
LOGOUT_URL = 'Logout'

SOCIAL_AUTH_FACEBOOK_KEY = '397156215115010'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '4f16e5c0bfc4af9e91990506ac99dcb0'  # App Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY  = "513624232070-jpdmnqmkc8ufp3k1gvhrdplai2pm4gvi.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "qQHI6RtQRiyFl6Ia0Jgo3uUo"




CONTENT_TYPES = ['image', 'video']
MAX_UPLOAD_THUMB_SIZE = "2621440"
MAX_UPLOAD_IMAGE_SIZE = "20971520"


SESSION_EXPIRE_SECONDS = 180
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_COOKIE_AGE = 180
