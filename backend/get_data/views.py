from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from PIL import Image
#mes modules
from modules.image_to_text import url_image_to_text
from modules.get_facture_data import get_facture_data_pipeline


def add_invoice_page(request):
    template = loader.get_template('create-invoice.html')
    context = {}  # Vous pouvez ajouter des variables si nécessaire
    return HttpResponse(template.render(context, request))

def add_invoice(request):
    if request.method == "POST":
        data = request.POST.get('link', '')
        print(data)
        image_text = url_image_to_text(data)
        arranged_data = get_facture_data_pipeline(image_text)
        print(image_text)
        # Retourner une réponse avec un statut 200
        return HttpResponse(f"votre fature a été ajouté \n \n {arranged_data}", status=200)
    # Par exemple, si la méthode n'est pas POST, retourner une erreur 405 (Method Not Allowed)
    return HttpResponse("Method not allowed", status=405)


def add_invoice2(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('img-file', None)
        if uploaded_file:
            try:
                # Ouvre l'image directement avec PIL
                image = Image.open(uploaded_file)
                # (Optionnel) Convertir l'image au format RGB
                image = image.convert('RGB')
                # Tu peux maintenant traiter l'image avec PIL, par exemple afficher sa taille
                print("Taille de l'image :", image.size)

                return HttpResponse("Image traitée avec succès.", status=200)
            except Exception as e:
                return HttpResponse(f"Erreur lors de l'ouverture de l'image: {e}", status=400)
        else:
            return HttpResponse("Aucun fichier reçu.", status=400)
    
    return HttpResponse("Method not allowed", status=405)