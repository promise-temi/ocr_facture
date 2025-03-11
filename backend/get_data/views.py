from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#mes modules



def hello(request, name="promise"):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


