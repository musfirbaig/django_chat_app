from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RoomForm
from .models import ChatRoom

# Create your views here.

def rooms(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'room/chat_rooms.html', {'rooms': rooms})


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

def chat_room(request, slug):
    room = ChatRoom.objects.filter(slug=slug).first()
    # print("printing roomname: ", slug)
    # print(room.slug)
    logged_in_user = request.user
    username = logged_in_user.username
    context = {
        'username': username,
        'room': room,
    }

    return render(request, "room/chat_room.html", context)
