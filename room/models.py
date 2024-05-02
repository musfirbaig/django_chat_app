from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 

# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128,unique=True)

    def save(self, *args, **kwargs):
        # Generate slug automatically before saving (your custom logic)
        self.slug = slugify(self.name)

        # Call the parent class's save method to execute its core functionality
        super().save(*args, **kwargs)



class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=ChatRoom, on_delete=models.CASCADE)
    content = models.TextField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.timestamp}]'