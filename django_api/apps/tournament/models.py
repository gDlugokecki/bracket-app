from django.db import models
from apps.player.models import Player


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name
