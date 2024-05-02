from django import forms
from .models import ChatRoom

class RoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name']