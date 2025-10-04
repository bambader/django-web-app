from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render

from listings.models import Band


def band_list(request):

    bands = Band.objects.all()
    return render(request,
                    'listings/band_list.html',
                    {'bands': bands})


def band_detail(request, id):  # notez le paramètre id supplémentaire
   band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
   return render(request,
                    'listings/band_detail.html',
                    {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit
         

def about(request):

    return HttpResponse('<h1>À propos de nous</h1> <p>Nous adorons merch !</p>')

def contact(request):

    return HttpResponse('<h1>Nous contacter</h1> <p>Contact: 0033 05 45 78 59 65</p>')

