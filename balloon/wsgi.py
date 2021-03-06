"""
WSGI config for balloon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import time
import traceback
import signal
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/var/www/html/game/balloon/balloon')
sys.path.append('/var/www/html/venv/lib/python3.7/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'balloon.settings')

try:
	application = get_wsgi_application()
except Exception:
	if 'mod_wsgi' in sys.modules:
		traceback.print_exc()
		os.kill(os.getpid(), signal.SIGINT)
		TIME.SLEEP(2.5)