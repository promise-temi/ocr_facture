from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from PIL import Image
#mes modules
from modules.image_to_text import image_to_text
from modules.get_facture_data import get_facture_data_pipeline
from modules.add_facture import add_facture_full_pipeline
from django.contrib.auth.decorators import login_required



@login_required
def add_invoice_page(request):
    template = loader.get_template('create-invoice.html')
    context = {}  # Vous pouvez ajouter des variables si nécessaire
    return HttpResponse(template.render(context, request))

@login_required
def add_invoice(request):
    if request.method == "POST":
        uploaded_link = request.POST.get('link', '')
        if uploaded_link :
            print(uploaded_link)
            try:
                image_text, qr_code_data = image_to_text(uploaded_link, 'url')
                arranged_data = get_facture_data_pipeline(image_text)
                data_ = {"image_text": arranged_data, "qrcode_text": qr_code_data}
                try:
                    add_facture_full_pipeline(data_)
                except Exception as e:
                    print('impossible d\'ajouter le facture a la base de donnée')
                    print(e)
                
            except Exception as e:
                return HttpResponse(f"Erreur lors de l'ouverture de l'image: {e}", status=400)
            # Retourner une réponse avec un statut 200
            return HttpResponse(f"votre fature a été ajouté", status=200)
        else:
            return HttpResponse("Aucun fichier reçu.", status=400)
    
    return HttpResponse("Method not allowed", status=405)

@login_required
def add_invoice2(request):
    if request.method == "POST":
        uploaded_files = request.FILES.getlist('img-file', None)
        if uploaded_files:
            datas_ = []
            for uploaded_file in uploaded_files:
                print(uploaded_file)
                try:
                    # Ouvre l'image directement avec PIL
                    image = Image.open(uploaded_file)
                    image_text, qr_code_data = image_to_text(image, 'file')
                    arranged_data = get_facture_data_pipeline(image_text)
                    data_ = {"image_text": arranged_data, "qrcode_text": qr_code_data}
                    try:
                        add_facture_full_pipeline(data_)
                    except Exception as e:
                        print('impossible d\'ajouter le facture a la base de donnée')
                        print(e)
                    datas_.append(data_)
                except Exception as e:
                    return HttpResponse(f"Erreur lors de l'ouverture de l'image: {e}", status=400)
            return HttpResponse(f"votre fature a été ajouté", status=200)
        else:
            return HttpResponse("Aucun fichier reçu.", status=400)
    
    return HttpResponse("Method not allowed", status=405)


