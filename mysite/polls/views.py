from http.client import ResponseNotReady
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.urls import reverse, reverse_lazy

class mainView(View):
    def get(self, req, guess):
        res = '''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>TESTING Class View</h1>
    <h2>''' + escape(guess) + ''' <h2>
    
</body>
</html>
        
        '''
        return HttpResponse(res)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def danger(req,guess):
    return HttpResponse(''' <!DOCTYPE html>
<html>
<body>

<h1>My First Heading ''' + escape(guess) + '''test danger</h1>

<p>My first paragraph.</p>

</body>
</html>

test danger''')

def redirect(req):
    return HttpResponseRedirect('https://www.google.com')

class GameView(View):
    def get(self, request, guess):
        indexLinke = reverse_lazy('polls:index')

        x = {'root':indexLinke}
        #x = {'guess' : int(guess)+11, 'test': '<b>bold<b>'}
        return render(request, 'polls/test.html', x)