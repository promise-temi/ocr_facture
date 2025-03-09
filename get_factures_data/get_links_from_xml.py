import requests
import xml.etree.ElementTree as ET

#requete http grace a request et stoquage de la reponse.
response = requests.get("https://projetocrstorageacc.blob.core.windows.net/invoices-2018?restype=container&comp=list&sv=2019-12-12&ss=b&srt=sco&sp=rl&se=2026-01-01T00:00:00Z&st=2025-01-01T00:00:00Z&spr=https&sig=%2BjCi7n8g%2F3849Rprey27XzHMoZN9zdVfDw6CifS6Y1U%3D")
print(response.text)

#sauvegarde du xml pour que ET puisse lexploiter
with open('ocr_facture/get_factures_data/data/factures.xml', 'w') as file:
    file.write(response.text)

#reccuperation des id dans le xml et reformation de l'url pour chaques images. et stockage de chaques lien dans une liste
factures_links = []
tree = ET.parse('ocr_facture/get_factures_data/data/factures.xml')
root = tree.getroot()
for facture_link_id in root.findall('.//Name'):
    facture_image_link = f"https://projetocrstorageacc.blob.core.windows.net/invoices-2018/{facture_link_id.text}?sv=2019-12-12&ss=b&srt=sco&sp=rl&se=2026-01-01T00:00:00Z&st=2025-01-01T00:00:00Z&spr=https&sig=%2BjCi7n8g%2F3849Rprey27XzHMoZN9zdVfDw6CifS6Y1U%3D"
    factures_links.append(facture_image_link)

with open('ocr_facture/get_factures_data/data/factures_links.txt','w') as file:
    file.write(str(factures_links))

