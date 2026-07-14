"""
WSGI config for the BrightSmile Dental Care project.

Exposes the WSGI callable as a module-level variable named ``application``.
This file is also used as the entry point reference when configuring the
WSGI file on PythonAnywhere.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brightsmile.settings')

application = get_wsgi_application()