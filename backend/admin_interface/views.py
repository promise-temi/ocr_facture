from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def factures(request):
    template = loader.get_template('factures.html')
    context = {}  # Vous pouvez ajouter des variables si nécessaire
    return HttpResponse(template.render(context, request)) 