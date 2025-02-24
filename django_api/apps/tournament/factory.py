import factory
from factory.django import DjangoModelFactory
import factory.fuzzy
from .models import Tournament
from apps.player.factory import PlayerFactory

categories = ["Amateur", "Professional", "Junior"]


class TournamentFactory(DjangoModelFactory):
    class Meta:
        model = Tournament

    name = factory.Faker("name")
    start_date = factory.Faker("date_time")
    end_date = factory.Faker("future_date")
    location = factory.Faker("city")
    category = factory.fuzzy.FuzzyChoice(categories)

    @factory.post_generation
    def players(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for player in extracted:
                self.players.add(player)
        else:
            num_players = factory.random.randint(4, 8)
            players = PlayerFactory.create_batch(num_players)
            for player in players:
                self.players.add(player)
