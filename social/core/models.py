from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

##TODO Remove blank verbose field and work out how to remove from creation form
class Event(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(default='fireworks2.jpg', upload_to='event')
    datetime = models.DateTimeField()
    street = models.CharField(max_length=50, blank=True)
    area = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    desc = models.TextField(max_length=400, verbose_name='Description')
    ticket = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    discord = models.URLField(blank=True)
    attendance = models.IntegerField(default=0) # editable=False
    # user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user", default='admin')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', kwargs={'pk': self.pk})

# class Attendance(models.Model):
#     event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    friends = models.ManyToManyField(User, related_name="friends",blank=True)
    img = models.ImageField(default= "core/user.jpg", upload_to='profile')


    def __str__(self):
        return f'{self.user.username}'


class Friend_Request(models.Model):
    from_user = models.ForeignKey(Profile, related_name='from_user', on_delete= models.CASCADE)
    # from_usr = models.ForeignKey(Profile, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Profile, related_name='to_user',on_delete=models.CASCADE)
    # to_usr = models.ForeignKey(Profile, related_name='to_user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'

