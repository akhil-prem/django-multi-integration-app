from asgiref.sync import async_to_sync
from channels.generic.websocket import SyncConsumer, AsyncConsumer
import asyncio


class ChannelSyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connected", event)
        self.send({
            "type": "websocket.accept"
        })

    def websocket_receive(self, event):
        print("msg received", event)
        self.send({
            "type": "websocket.send",
            "text": event["text"]
        })

    def websocket_disconnect(self, event):
        print("disconnected", event)


class ChannelLayerSyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print(self.channel_name)
        self.room_name = 'group_name'
        # Add this channel to a group
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )
        self.send({"type": "websocket.accept"})

    def websocket_receive(self, event):
        print("msg received", event)
        # Broadcast the message to the group
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                "type": "chat.message",
                "text": event['text']
            }
        )

    def chat_message(self, event):
        print("msg sent", event)
        # Send message to WebSocket
        self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    def websocket_disconnect(self, event):
        # Remove this channel from the group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("WebSocket connected:", event)
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        print("Message received:", event['text'])
        await asyncio.sleep(1)  # Simulate long-running task
        await self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    async def websocket_disconnect(self, event):
        print("WebSocket disconnected:", event)
