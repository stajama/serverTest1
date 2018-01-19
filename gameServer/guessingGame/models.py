from django.db import models

# Create your models here.

class GuessThis(models.Model):
    """GuessThis holds the current number to be guessed at by player 2."""
    number = models.IntegerField(default=0)
    hasBeenGuessed = models.BooleanField(default=False)

class Guesses(models.Model):
    guesses = models.IntegerField(default=0)