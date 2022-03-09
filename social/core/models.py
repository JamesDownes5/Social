from django.db import models
from django.contrib.auth.models import User

# Create your models here.

##TODO Remove blank verbose field and work out how to remove from creation form
class Event(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="event", blank=True)
    datetime = models.DateTimeField(blank=True)
    street = models.CharField(max_length=50, blank=True)
    area = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    desc = models.TextField(max_length=400)
    ticket = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    discord = models.URLField(blank=True)
    attendance = models.IntegerField(default=0) # editable=False

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default= "default.png", upload_to='profile')

    def __str__(self):
        return f'{self.user.username} Profile'
