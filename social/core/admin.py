from django.contrib import admin
from .models import Attendee, Event, Profile, Friend_Request

# Register your models here.

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(Friend_Request)
