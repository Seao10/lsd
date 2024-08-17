from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

class Score(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.participant.name} - {self.event.name} - {self.score}"
