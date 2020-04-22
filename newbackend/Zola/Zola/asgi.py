"""
ASGI config for Zola project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import django
import channels
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Zola.settings')
#from channels.asgi import get_channel_layer

#django.setup()
application = channels.asgi.get_channel_layer()
