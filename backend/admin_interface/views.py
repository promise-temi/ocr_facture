
from django.http import HttpResponse
from django.template import loader
# mes modules
from modules.get_factures import getfacture, get_single_facture
from modules.get_clients import get_client, get_single_client
from django.contrib.auth.decorators import login_required
from modules.update_clust_data import update_all_user_features
from modules.client_clustering import main as clustering

# Create your views here.
@login_required
def factures(request):
    data = getfacture()
    template = loader.get_template('factures.html')
    context = {
        'mes_factures': data,
    }  
    return HttpResponse(template.render(context, request)) 

@login_required
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

@login_required
def clients(requests):
    data = get_client()
    template = loader.get_template('clients.html')
    context = {
        'clients': data
        }
    update_all_user_features()
    clustering()
    return HttpResponse(template.render(context, requests))

@login_required
def info_client(requests, client_id):
    client, factures = get_single_client(client_id)
    template = loader.get_template('info_client.html')
    print(client_id)
    context = {
        "client" : client,
        "factures" : factures,
    }
    
    return HttpResponse(template.render(context, requests))