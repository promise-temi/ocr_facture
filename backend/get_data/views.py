from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#mes modules
from modules.image_to_text import url_image_to_text

def add_invoice_page(request):
    template = loader.get_template('create-invoice.html')
    context = {}  # Vous pouvez ajouter des variables si nécessaire
    return HttpResponse(template.render(context, request))

def add_invoice(request):
    if request.method == "POST":
        data = request.POST.get('link', '')
        print(data)
        image_text = url_image_to_text(data)
        print(image_text)
        # Retourner une réponse avec un statut 200
        return HttpResponse(f"votre fature a été ajouté \n \n {image_text}", status=200)
    # Par exemple, si la méthode n'est pas POST, retourner une erreur 405 (Method Not Allowed)
    return HttpResponse("Method not allowed", status=405)