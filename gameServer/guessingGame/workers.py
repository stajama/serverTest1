import bleach
from .models import *

def cleanAndCheckNumber(numberString):
    x = bleach.clean(str(numberString))
    try:
        x = int(x)
        if x > 100 or x < 1:
            raise ValueError
    except ValueError:
        raise ValueError("Input must be a valid number from 1 to 100.")
    return x


def clearDatabase():
    x = GuessThis.objects.all()
    x.delete()
    x = Guesses.objects.all()
    x.delete()
    if len(GuessThis.objects.all()) != 0 or len(Guesses.objects.all()) != 0:
        raise ResourceWarning("clearDatabase() reads that database has not \
            been fully cleared")
    return

def setNumber(number):
    x = GuessThis(number=number)
    x.save()
    return

def getNumber():
    if len(GuessThis.objects.all()):
        return GuessThis.objects.all()[0].number
    return

def setAndCheckGuess(number):
    check = GuessThis.objects.all()[0].number
    current = Guesses(guesses=number)
    current.save()
    if number == check:
        return "Win"
    elif number < check:
        return "Higher"
    else:
        return "Lower"

def getGuessList():
    return [x.guesses for x in Guesses.objects.all()]

def isGameOver():
    return len(Guesses.objects.all()) >= 10
