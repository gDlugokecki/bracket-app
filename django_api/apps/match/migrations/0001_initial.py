# Generated by Django 5.1.5 on 2025-02-16 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("player", "0002_initial"),
        ("tournament", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("SCHEDULED", "Scheduled"),
                            ("IN_PROGRESS", "In Progress"),
                            ("COMPLETED", "Completed"),
                            ("CANCELLED", "Cancelled"),
                        ],
                        default="SCHEDULED",
                        max_length=20,
                    ),
                ),
                ("scheduled_time", models.DateTimeField()),
                ("court_number", models.CharField(blank=True, max_length=10)),
                ("round_number", models.IntegerField(null=True)),
                ("score", models.CharField(blank=True, max_length=100)),
                ("duration", models.DurationField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "player1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matches_as_player1",
                        to="player.player",
                    ),
                ),
                (
                    "player2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matches_as_player2",
                        to="player.player",
                    ),
                ),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matches",
                        to="tournament.tournament",
                    ),
                ),
                (
                    "winner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="matches_won",
                        to="player.player",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "matches",
            },
        ),
        migrations.CreateModel(
            name="Set",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("set_number", models.IntegerField()),
                ("player1_score", models.IntegerField()),
                ("player2_score", models.IntegerField()),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="match.match"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Statistics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("aces", models.IntegerField()),
                ("double_faults", models.IntegerField()),
                (
                    "first_serve_percentage",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("winners", models.IntegerField()),
                ("unforced_errors", models.IntegerField()),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="match.match"
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="player.player"
                    ),
                ),
            ],
        ),
    ]
