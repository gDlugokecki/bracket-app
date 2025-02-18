import factory
from factory.django import DjangoModelFactory
import factory.fuzzy
from .models import Match
from datetime import timedelta
from django.utils import timezone
from apps.player.factory import PlayerFactory
from apps.tournament.factory import TournamentFactory
import random


class MatchFactory(DjangoModelFactory):
    class Meta:
        model = "match.Match"

    tournament = factory.SubFactory(TournamentFactory)
    player1 = factory.SubFactory(PlayerFactory)
    player2 = factory.SubFactory(PlayerFactory)
    status = factory.Faker(
        "random_element", elements=[s[0] for s in Match.MATCH_STATUS_CHOICES]
    )
    scheduled_time = factory.Faker("future_datetime")
    court_number = factory.Sequence(lambda n: f"Court {n+1}")
    round_number = factory.Faker("random_int", min=1, max=7)
    winner = factory.LazyAttribute(
        lambda o: (
            random.choice([o.player1, o.player2]) if o.status == "COMPLETED" else None
        )
    )
    score = factory.LazyAttribute(
        lambda o: "6-4, 6-3" if o.status == "COMPLETED" else ""
    )
    duration = factory.LazyAttribute(
        lambda o: (
            timedelta(minutes=random.randint(60, 180))
            if o.status == "COMPLETED"
            else None
        )
    )
    created_at = factory.LazyFunction(timezone.now)
    updated_at = factory.LazyFunction(timezone.now)


class SetFactory(DjangoModelFactory):
    class Meta:
        model = "match.Set"

    match = factory.SubFactory(MatchFactory)
    set_number = factory.Sequence(lambda n: n + 1)
    player1_score = factory.Faker("random_int", min=0, max=7)
    player2_score = factory.Faker("random_int", min=0, max=7)


class StatisticsFactory(DjangoModelFactory):
    class Meta:
        model = "match.Statistics"

    match = factory.SubFactory(MatchFactory)
    player = factory.SelfAttribute("match.player1")  # Default to player1's stats
    aces = factory.Faker("random_int", min=0, max=20)
    double_faults = factory.Faker("random_int", min=0, max=10)
    first_serve_percentage = factory.Faker(
        "pydecimal", left_digits=2, right_digits=2, positive=True, max_value=100
    )
    winners = factory.Faker("random_int", min=10, max=50)
    unforced_errors = factory.Faker("random_int", min=5, max=40)
