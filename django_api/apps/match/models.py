from django.db import models

from apps.player.models import Player
from apps.tournament.models import Tournament


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player_1 = models.ForeignKey(
        Player, related_name="matches_as_player1", on_delete=models.CASCADE
    )
    player_2 = models.ForeignKey(
        Player, related_name="matches_as_player2", on_delete=models.CASCADE
    )
    winner = models.ForeignKey(
        Player, related_name="matches_won", on_delete=models.CASCADE
    )
    score = models.ForeignKey(
        Player, related_name="match_wins", on_delete=models.CASCADE
    )
    date = models.DateTimeField()
    round = models.CharField(max_length=50)


class Set(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    set_number = models.IntegerField()
    player1_score = models.IntegerField()
    player2_score = models.IntegerField()


class Statistics(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    aces = models.IntegerField()
    double_faults = models.IntegerField()
    first_serve_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    winners = models.IntegerField()
    unforced_errors = models.IntegerField()
