import os
"""
Development settings for chronosserver project.
Use this for local development.
"""

from .settings_base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ypq5uwpg%qjq*nq^%o7xtd4et7g=#2nrbake@u_owep=&k=0!u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow configuring ALLOWED_HOSTS via environment variable for local/CI use.
_default_allowed = '127.0.0.1,localhost,testserver'
ALLOWED_HOSTS = [h.strip() for h in os.environ.get('ALLOWED_HOSTS', _default_allowed).split(',') if h.strip()]

# CORS settings for development
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://127.0.0.1:3000',
)

# Database - SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
