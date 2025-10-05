from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render

from listings.models import Band

# Importer le formulaire créé
from listings.forms import ContactUsForm

from django.core.mail import send_mail


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

def email_sent (request):

    return HttpResponse('<h1>Email bien envoyé</h1> <p>Merci !</p>')

def contact(request):
  
 if request.method == 'POST':

        # créer une instance de notre formulaire et le remplir avec les données POST

        form = ContactUsForm(request.POST)


        if form.is_valid():

            send_mail(

            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',

            message=form.cleaned_data['message'],

            from_email=form.cleaned_data['email'],

            recipient_list=['admin@merchex.xyz'],

        )
        return redirect("email_sent")
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return

    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
 else:

    # ceci doit être une requête GET, donc créer un formulaire vide

         form = ContactUsForm()

 return render(request,

          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit


