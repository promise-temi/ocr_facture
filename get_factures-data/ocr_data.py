import requests
import xml.etree.ElementTree as ET
import easyocr
import cv2
import numpy as np

#requete http grace a request et stoquage de la reponse.
response = requests.get("https://projetocrstorageacc.blob.core.windows.net/invoices-2018?restype=container&comp=list&sv=2019-12-12&ss=b&srt=sco&sp=rl&se=2026-01-01T00:00:00Z&st=2025-01-01T00:00:00Z&spr=https&sig=%2BjCi7n8g%2F3849Rprey27XzHMoZN9zdVfDw6CifS6Y1U%3D")
print(response.text)

#sauvegarde du xml pour que ET puisse lexploiter
with open('ocr_facture/get_factures-data/factures.xml', 'w') as file:
    file.write(response.text)

#reccuperation des id dans le xml et reformation de l'url pour chaques images. et stockage de chaques lien dans une liste
factures_links = []
tree = ET.parse('ocr_facture/get_factures-data/factures.xml')
root = tree.getroot()
for facture_link_id in root.findall('.//Name'):
    facture_image_link = f'https://projetocrstorageacc.blob.core.windows.net/invoices-2018/{facture_link_id.text}?sv=2019-12-12&ss=b&srt=sco&sp=rl&se=2026-01-01T00:00:00Z&st=2025-01-01T00:00:00Z&spr=https&sig=%2BjCi7n8g%2F3849Rprey27XzHMoZN9zdVfDw6CifS6Y1U%3D'
    factures_links.append(facture_image_link)
    print(facture_image_link, '\n')

images_text = []


reader = easyocr.Reader(['en']) 
for facture_link in factures_links:
    response = requests.get(facture_link).content
    # Convertir les données d'image en tableau NumPy
    nparr = np.frombuffer(response, np.uint8)
    # Décode l'image à partir du tableau NumPy
    image_cv2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Vérification pour s'assurer que l'image a été correctement décodée
    if image_cv2 is None:
        print("Erreur de décodage de l'image pour le lien :", facture_link)
        continue

    # Prétraitement de l'image
    gray = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2GRAY)
    # Application d'un filtre pour réduire le bruit
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    # Seuillage pour binariser l'image
    ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Lecture du texte avec EasyOCR
    text = reader.readtext(
        thresh, 
        detail=0,                # Retourne uniquement le texte
        contrast_ths=0.05,       # Ajuste le seuil de contraste
        adjust_contrast=0.7,     # Ajuste automatiquement le contraste
        text_threshold=0.4,      # Filtre les détections à faible confiance
        low_text=0.3             # Seuil pour le texte peu contrasté
    )

    print(text)
    images_text.append(text)








































#sauvegarde en csv des données reccupérée
with open('ocr_facture/get_factures-data/factures_data.csv', 'w') as file:
    file.write(str(images_text))

