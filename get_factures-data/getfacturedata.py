import requests
import xml.etree.ElementTree as ET
import pytesseract

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
reader = easyocr.Reader(['fr','en'])
for facture_link in factures_links:
    response = requests.get(facture_link).content
    image = response
    
    text = reader.readtext(image, detail = 0) #si detail etait a 0 alors j'aurai juste le texte sans les coordonnées
    print(text)

    images_text.append(text)



#sauvegarde en csv des données reccupérée
with open('ocr_facture/get_factures-data/factures_data.csv', 'w') as file:
    file.write(str(images_text))

