from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# mes modules
from modules.get_factures import getfacture, get_facture_related_user, get_single_facture
from modules.get_clients import get_client

# Create your views here.
def factures(request):
    data = getfacture()
    template = loader.get_template('factures.html')
    context = {
        'mes_factures': data,
    }  # Vous pouvez ajouter des variables si nécessaire
    return HttpResponse(template.render(context, request)) 


def info_facture(request, facture_id):
    id = facture_id
    template = loader.get_template('info_facture.html')
    facture, user, produits = get_single_facture(id)
    print(produits)
    context = {
        "facture": facture,
        "user" : user,
        "produits" : produits
    }
    return HttpResponse(template.render(context, request)) 

def clients(requests):
    data = get_client()
    template = loader.get_template('clients.html')
    context = {
        'clients': data
        }
    
    return HttpResponse(template.render(context, requests))