# import os
# from pathlib import Path
# from decouple import config

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Load sensitive settings from .env
# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=False, cast=bool)
# ALLOWED_HOSTS = []  # Update this for production

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'main',  # Ensure your app is correctly listed
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'EvalZen.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR,"templates")],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'EvalZen.wsgi.application'
# APPEND_SLASH=False 

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': config('DB_NAME'),  
#         'CLIENT': {
#             'host': config('MONGO_URI'),  # Use your MongoDB URI here
#             'username': config('DB_USER'), 
#             'password': config('DB_PASSWORD'), 
#             'authSource': config('DB_AUTH_SOURCE', default='admin'), 
#         }
#     }
# }



# # Static files (CSS, JavaScript, Images)
# STATIC_URL = 'static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'main', 'static'),  # Path to the 'static' folder inside 'main' app
# ]

# # Default primary key field type    
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # OpenAI API Key
# OPENAI_API_KEY = config('OPENAI_API_KEY')

# # Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# # settings.py

import os
from pathlib import Path
from decouple import config

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY SETTINGS
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]


# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'EvalZen.urls'


# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'EvalZen.wsgi.application'


APPEND_SLASH = False


# DATABASE (MongoDB using Djongo)
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': config('DB_NAME'),
        'CLIENT': {
            'host': config('MONGO_URI'),
            'username': config('DB_USER'),
            'password': config('DB_PASSWORD'),
            'authSource': config('DB_AUTH_SOURCE', default='admin'),
        }
    }
}


# IMPORTANT FIX FOR DJONGO SESSION ERROR
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# SESSION_ENGINE = "django.contrib.sessions.backends.db"

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
# PASSWORD VALIDATION (Optional but recommended)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]


# LANGUAGE AND TIMEZONE
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# STATIC FILES
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main', 'static'),
]


# DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# OPENAI API
OPENAI_API_KEY = config('OPENAI_API_KEY')


# EMAIL SETTINGS (GMAIL SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = 'praveenmurugan060@gmail.com'
EMAIL_HOST_PASSWORD = 'gtqwwffjomcmbmwy' 


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = 'evalzen24@gmail.com'
# EMAIL_HOST_PASSWORD = 'fxuw jnor jrvj hgnw'