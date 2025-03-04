from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
