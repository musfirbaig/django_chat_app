from django.urls import path
from .views import rooms, create_room, chat_room



app_name = 'room'

urlpatterns = [
    path('', rooms, name='rooms'),
    path('create-room/', create_room, name='create-room'),
    path('<str:slug>/', chat_room, name='chat-room'),
]