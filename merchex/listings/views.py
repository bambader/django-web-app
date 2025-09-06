from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render

from listings.models import Band


def hello(request):

    bands = Band.objects.all()

    return HttpResponse(f"""

        <h1>Hello Django !</h1>

        <p>Mes groupes préférés sont :<p>

        <ul>

            <li>{bands[0].name}</li>

            <li>{bands[1].name}</li>

            <li>{bands[2].name}</li>

        </ul>

""")

def about(request):

    return HttpResponse('<h1>À propos de nous</h1> <p>Nous adorons merch !</p>')

def contact(request):

    return HttpResponse('<h1>Nous contacter</h1> <p>Contact: 0033 05 45 78 59 65</p>')

