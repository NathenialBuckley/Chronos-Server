import os
"""
Django settings router for chronosserver project.
Loads appropriate settings based on DJANGO_ENV environment variable.

Set DJANGO_ENV to:
- 'production' for production settings
- 'development' (or unset) for development settings
"""

# Determine which settings to use
DJANGO_ENV = os.environ.get('DJANGO_ENV', 'development')

if DJANGO_ENV == 'production':
    from .settings_prod import *
else:
    from .settings_dev import *
