"""Current implementation uses a HTML meta refresh command to automatically
upate each client as new information is added to the database. The next step
is to try a javascript/jQuery solution, directly altering an HTML element on
a timed update rather than force refreshing the entire page."""

"""URLs are getting added information that is screwing with django url lookup.
Must find out where these stated URI addons are coming from and stop them."""

from django.shortcuts import render
from django.http import HttpResponse
import bleach

from .models import Guesses, GuessThis
from . import workers

# Create your views here.
def home(request):
    workers.clearDatabase()
    return HttpResponse("""Select Role:
        <form action="setter">
            <input type="submit" value="Setter" />
        </form>
        <form action="guesser">
            <input type="submit" value="Guesser" />
        </form>""")

def setter(request, errorStatement=""):
    if errorStatement:
        errorStatement = "ERROR: Input must be a number between 1 and 100.\n"
    return HttpResponse(errorStatement + """Select a number between 1 and 100.
         <form action="setter2/">
            <input type="text" name="number"><br>
            <input type="submit" value="Submit">
        </form> """)

def setter2(request):
    if not workers.getNumber():
        try:
            number = workers.cleanAndCheckNumber(request.GET['number'])
        except ValueError:
            return setter(request, "ValueError")
        workers.setNumber(int(number))
    else:
        if GuessThis.objects.all()[0].hasBeenGuessed:
            return setter3(request)
        elif workers.isGameOver():
            return setter3(request, True)
    addTo = ""
    print(workers.getGuessList())
    for i in workers.getGuessList():
        addTo += "<li>" + str(i) + "</li>"
        print(addTo,)
    return HttpResponse("""<head> <meta HTTP-EQUIV="refresh" CONTENT="15"> </head>
     Number Received. Waiting for other player's guesses.<br><ol>""" + addTo + "</ol>")

def setter3(request, won=False):
    if won:
        y = "You win." 
    else:
        y = "Player 2 won. It took only " + str(len(workers.getGuessList())) + " guesses."
    return HttpResponse(y + '<br>'\
         + """Play Again?:
        <form action="">
            <input type="submit" value="Yes" />
        </form>""")

def guesser(request):
    if len(GuessThis.objects.all()) == 0:
        return HttpResponse('<head> <meta HTTP-EQUIV="refresh" CONTENT="15"> </head>Waiting for Player 1.')
    else:
        return HttpResponse("""The game is afoot. Select a number between 1 and 100.
         <form action="guesser2/">
            <input type="text" name="number"><br>
            <input type="submit" value="Submit">
        </form> """)

def guesser2(request):
    if not workers.isGameOver():
        x = int(request.GET['number'])
        x = cleanAndCheckNumber(x)
        answer = workers.setAndCheckGuess(x)
        if answer == "Win" or workers.isGameOver():
            GuessThis.objects.all()[0].hasBeenGuessed = True
            return guesser3(request, True)
        else:
            return HttpResponse(answer + '<br>' + """Select a number between 1 and 100.
         <form action="guesser2/">
            <input type="text" name="number"><br>
            <input type="submit" value="Submit">
        </form> """)
    else:
        return guesser3(request, False)

def guesser3(request, won=False):
    """As confimed, I seem to be too stupid to put simple logic together.
    The page in test keeps returning "You Win" text even upon defeat. 
    Call is made from guesser2() reliant upon workers.isGameOver() or number
    matching GuessThis.number."""

    x = "The number was: " + str(workers.getNumber())
    if won:
        y = "You Win. It took " + str(len(workers.getGuessList())) + " guesses."
    else:
        y = "Player 1 wins."
    return HttpResponse(x + '<br>' + y + '<br>'\
         + """Play Again?:
        <form action="">
            <input type="submit" value="Yes" />
        </form>""")