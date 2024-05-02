import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_app.settings")

# Initialize Django ASGI application early
django_asgi_app = get_asgi_application()

# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, ChatRoom
from django.contrib.auth.models import User

from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        room_name = self.scope['url_route']['kwargs']['room_name']
        print("connected to socket")
        await self.channel_layer.group_add(room_name, self.channel_name)
        await self.accept()


    async def disconnect(self, close_code):
        room_name = self.scope['url_route']['kwargs']['room_name']  # Access room name
        await self.channel_layer.group_discard(room_name, self.channel_name)
        

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        room_name = self.scope['url_route']['kwargs']['room_name']
        # print(room_name, "hello ")

        # saving message to database 
        # print("saving message to database should be executed")
        await self.save_message(username, room_name, message)

        # Broadcast message to all clients in the specific room group
        await self.channel_layer.group_send(
            room_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

        


    async def chat_message(self, event):
        # Send message to WebSocket
        message = event['message']
        username = event['username']
        # print("chat message function called")
        await self.send(text_data=json.dumps({'message': message, 'username': username}))

    @sync_to_async
    def save_message(self, username, room_name, message):
        # after broadcasting message, i am saving it in my database
        room = ChatRoom.objects.filter(slug=room_name).first()
        user = User.objects.filter(username=username).first()
        print(ChatRoom.objects.all())
        print("message is saving..")
        print(room.name)
        print(user.username)
        new_message = Message.objects.create(room=room, user=user, content=message)

    # async def save_message(self, username, room_name, message):
    #     try:
    #         # Get room and user instances
    #         room = ChatRoom.objects.filter(slug=room_name).first()
    #         user = User.objects.filter(username=username).first()

    #         # Create new message
    #         new_message = Message.objects.create(room=room, user=user, content=message)
    #         print("Message saved successfully")
    #     except Exception as e:
    #         print("Error saving message:", str(e))
