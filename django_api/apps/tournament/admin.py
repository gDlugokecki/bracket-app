from django.contrib import admin
from apps.match.models import Match
from .models import Tournament


class MatchInline(admin.TabularInline):
    model = Match

    extra = 1


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    # pass
    filter_horizontal = ["players"]
    inlines = [MatchInline]

    def get_players(self, obj):
        return ", ".join([str(player) for player in obj.players.all()])

    get_players.short_description = "Players132"
