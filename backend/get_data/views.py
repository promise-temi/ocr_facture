from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from PIL import Image
#mes modules
from modules.image_to_text import image_to_text
from modules.get_facture_data import get_facture_data_pipeline


def add_invoice_page(request):
    template = loader.get_template('create-invoice.html')
    context = {}  # Vous pouvez ajouter des variables si nécessaire
    return HttpResponse(template.render(context, request))

def add_invoice(request):
    if request.method == "POST":
        uploaded_link = request.POST.get('link', '')
        if uploaded_link :
            try:
                image_text, qr_code_data = image_to_text(uploaded_link, 'url')
                arranged_data = get_facture_data_pipeline(image_text)
                data_ = {"image_text": arranged_data, "qrcode_text": qr_code_data}
                
            except Exception as e:
                return HttpResponse(f"Erreur lors de l'ouverture de l'image: {e}", status=400)
            # Retourner une réponse avec un statut 200
            return HttpResponse(f"votre fature a été ajouté \n \n {data_}", status=200)
        else:
            return HttpResponse("Aucun fichier reçu.", status=400)
    
    return HttpResponse("Method not allowed", status=405)


def add_invoice2(request):
    if request.method == "POST":
        uploaded_files = request.FILES.getlist('img-file', None)
        if uploaded_files:
            datas_ = []
            for uploaded_file in uploaded_files:
                try:
                    # Ouvre l'image directement avec PIL
                    image = Image.open(uploaded_file)
                    image_text, qr_code_data = image_to_text(image, 'file')
                    arranged_data = get_facture_data_pipeline(image_text)
                    data_ = {"image_text": arranged_data, "qrcode_text": qr_code_data}
                    datas_.append(data_)
                except Exception as e:
                    return HttpResponse(f"Erreur lors de l'ouverture de l'image: {e}", status=400)
            return HttpResponse(f"votre fature a été ajouté \n \n {datas_}", status=200)
        else:
            return HttpResponse("Aucun fichier reçu.", status=400)
    
    return HttpResponse("Method not allowed", status=405)