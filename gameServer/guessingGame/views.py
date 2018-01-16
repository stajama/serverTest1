from django.shortcuts import render
from django.http import HttpResponse
import bleach

from . import workers

# Create your views here.
def home(request):
    return HttpResponse("""Select Role:
        <form action="setter">
            <input type="submit" value="Setter" />
        </form>
        <form action="http://google.com">
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
    try:
        number = workers.cleanAndCheckNumber(request.GET['number'])
    except ValueError:
        return setter(request, "ValueError")
    return HttpResponse('landed')

def guesser(request):
    return