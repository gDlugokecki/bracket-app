from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True)


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    players = models.ManyToManyField(Player)


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
