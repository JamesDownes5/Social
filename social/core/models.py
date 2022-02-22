from django.db import models
from django.test import tag

class Event(models.Model):
    title = models.CharField(max_length=50)
#    image = models.ImageField(upload_to="static/core/event/")
    location = models.CharField(max_length=50)
    date =  models.DateField()
    desc = models.CharField(max_length=400)
    ticket = models.URLField()
    # social = 
    # tag = 

