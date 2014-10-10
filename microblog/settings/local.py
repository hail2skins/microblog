DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'microblog',
        'USER': 'vagrant',
        'PASSWORD': 'password',
    }
}
