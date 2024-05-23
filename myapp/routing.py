# myapp/routing.py

from django.urls import path
from .consumers import MovieConsumer

websocket_urlpatterns = [
    path('ws/movies/', MovieConsumer.as_asgi()),
]
