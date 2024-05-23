"""
ASGI config for backendmmp project.

It exposes the ASGI callable as a module-level variable named `application`.
"""

import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import backendmpp.myapp.routing
import backendmpp.myapp
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backendmmp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Django's ASGI application to handle traditional HTTP requests
    "websocket": AuthMiddlewareStack(  # WebSocket handler
        URLRouter(
            backendmpp.myapp.routing.websocket_urlpatterns  # The routing defined in myapp.routing
        )
    ),
})
