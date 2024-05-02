from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RoomForm
from .models import ChatRoom, Message
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def rooms(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'room/chat_rooms.html', {'rooms': rooms})

@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('room:rooms'))
    else:
        form = RoomForm()

    context = {'form': form}
    return render(request, 'room/create_room.html', context)

@login_required
def chat_room(request, slug):
    room = ChatRoom.objects.filter(slug=slug).first()
    # print("printing roomname: ", slug)
    # print(room.slug)
    logged_in_user = request.user
    username = logged_in_user.username

    # now also retrieving all stored messages of that room 
    messages = Message.objects.filter(room=room)

    # retrieving recent 30 messages only 

    messages = messages.order_by('-timestamp')[:30][::-1]


    context = {
        'username': username,
        'room': room,
        'messages': messages,
    }

    return render(request, "room/chat_room.html", context)
