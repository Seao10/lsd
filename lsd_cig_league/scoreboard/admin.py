from django.contrib import admin
from .models import Participant, Event, Score

admin.site.register(Participant)
admin.site.register(Event)
admin.site.register(Score)
