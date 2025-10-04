from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render

from listings.models import Band

# Importer le formulaire créé
from listings.forms import ContactUsForm


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
  
  if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST

     form = ContactUsForm(request.POST)
  else:

 # ceci doit être une requête GET, donc créer un formulaire vide
   form = ContactUsForm()  # ajout d’un nouveau formulaire ici

  return render(request,

          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit


