from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="core/event/", blank=True)
    datetime = models.DateTimeField(blank=True)
    street = models.CharField(max_length=50, blank=True)
    area = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    desc = models.TextField(max_length=400)
    ticket = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    discord = models.URLField(blank=True)
    attendance = models.IntegerField(default=0)

    def __str__(self):
        return self.title

