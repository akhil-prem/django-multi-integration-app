from django.urls import path
from .consumers import ChannelSyncConsumer, ChannelLayerSyncConsumer, MyAsyncConsumer

websocket_urlpatterns = [
    path('ws/sync_consumer/', ChannelSyncConsumer.as_asgi()),
    path('ws/layer_sync_consumer/', ChannelLayerSyncConsumer.as_asgi()),
    path('ws/async_consumer/', MyAsyncConsumer.as_asgi()),
]
