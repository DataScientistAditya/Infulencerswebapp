from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


User = get_user_model()


class MessageData(models.Model):
    Author = models.ForeignKey(
        User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    roomname = models.CharField(max_length=1000, default="N/A")
    User = models.CharField(max_length=200, default="N/A")

    def __str__(self):
        return self.Author.user.username
    
    def last_20_messages(room_name):
        return MessageData.objects.all().filter(roomname =room_name).values("Author","content","User")