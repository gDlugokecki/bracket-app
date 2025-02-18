import factory
from factory.django import DjangoModelFactory
import factory.fuzzy
from .models import Player


class PlayerFactory(DjangoModelFactory):
    class Meta:
        model = Player

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Sequence(lambda n: f"user_{n}@example.com")
