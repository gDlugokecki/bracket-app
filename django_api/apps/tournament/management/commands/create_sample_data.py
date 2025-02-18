# myapp/management/commands/create_sample_data.py
from django.core.management.base import BaseCommand
from apps.tournament.factory import TournamentFactory
from apps.player.factory import PlayerFactory
from apps.match.factory import MatchFactory, StatisticsFactory, SetFactory
import random


class Command(BaseCommand):

    help = "Creates sample data using factories"

    def create_match_with_details(self, tournament, player1, player2, round_number):
        match = MatchFactory(
            tournament=tournament,
            player1=player1,
            player2=player2,
            round_number=round_number,
            status="COMPLETED",
        )
        match.winner = random.choice([player1, player2])
        match.save()

        # Create sets and statistics
        for set_num in range(3):
            SetFactory(match=match)

        StatisticsFactory(match=match, player=player1)
        StatisticsFactory(match=match, player=player2)

        return match

    def create_round_matches(self, tournament, players, round_number):
        winners = []
        for i in range(0, len(players), 2):
            match = self.create_match_with_details(
                tournament, players[i], players[i + 1], round_number
            )
            winners.append(match.winner)
        return winners

    # def handle(self, *args, **kwargs):
    #     players = PlayerFactory.create_batch(10)
    #     self.stdout.write(f"Created {len(players)} players")

    #     tournament = TournamentFactory(players=players[:5])
    #     self.stdout.write(f"Created tournament: {tournament.name}")
    def handle(self, *args, **kwargs):
        # Create players and tournament
        players = PlayerFactory.create_batch(32)
        tournament = TournamentFactory(players=players)

        self.stdout.write(
            f"Created tournament: {tournament.name} with {len(players)} players"
        )

        # Round of 32
        round_32_winners = self.create_round_matches(tournament, players, 1)
        self.stdout.write("Created Round of 32 matches")

        # Round of 16
        round_16_winners = self.create_round_matches(tournament, round_32_winners, 2)
        self.stdout.write("Created Round of 16 matches")

        # Quarter-finals
        quarter_winners = self.create_round_matches(tournament, round_16_winners, 3)
        self.stdout.write("Created Quarter-final matches")

        # Semi-finals
        semi_winners = self.create_round_matches(tournament, quarter_winners, 4)
        self.stdout.write("Created Semi-final matches")

        # Final
        final = self.create_match_with_details(
            tournament, semi_winners[0], semi_winners[1], 5
        )
        self.stdout.write(f"Created Final match: {final.player1} vs {final.player2}")
        self.stdout.write(f"Tournament winner: {final.winner}")
