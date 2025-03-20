from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# mes modules
from modules.get_factures import getfacture, get_facture_related_user

# Create your views here.
def factures(request):
    data = getfacture()
    template = loader.get_template('factures.html')
    context = {
        'mes_factures': data,
    }  # Vous pouvez ajouter des variables si nécessaire
    return HttpResponse(template.render(context, request)) 