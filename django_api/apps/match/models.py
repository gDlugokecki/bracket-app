from django.utils import timezone
from django.db import models

from apps.player.models import Player
from apps.tournament.models import Tournament


class Match(models.Model):
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, related_name="matches"
    )
    # For singles matches
    player1 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="matches_as_player1"
    )
    player2 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="matches_as_player2"
    )

    MATCH_STATUS_CHOICES = [
        ("SCHEDULED", "Scheduled"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]
    status = models.CharField(
        max_length=20, choices=MATCH_STATUS_CHOICES, default="SCHEDULED"
    )

    scheduled_time = models.DateTimeField()
    court_number = models.CharField(max_length=10, blank=True)
    round_number = models.IntegerField(null=True)

    winner = models.ForeignKey(
        Player,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="matches_won",
    )

    score = models.CharField(max_length=100, blank=True)
    duration = models.DurationField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "matches"

    def __str__(self):
        return f"{self.player1} vs {self.player2} - {self.tournament.name}"


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
