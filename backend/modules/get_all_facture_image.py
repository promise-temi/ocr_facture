import os
import requests
import xml.etree.ElementTree as ET
import json
from io import BytesIO
from PIL import Image

def main():
    get_all_facture_image()



def get_all_facture_image(annees=[2018]):
    """
    Cette fonction permet de récupérer toutes les factures stockées dans une base de données tierce à nimporte quelles années voulues a condition quelles y sont.
    Il récupère tout d'abord un fichier XML contenant les identifiants des images des factures pour réccupérer tous les liens d'images.
    Il sauvegarde ensuite les liens dans un fichier JSON.
    A l'aide des liens du fichier JSON il télécharge ensuite les images et les sauvegarde dans un dossier.
    """

    # Parcours de chaque année
    for annee in annees:
        # Construit l'URL en fonction de l'année
        url = f"https://projetocrstorageacc.blob.core.windows.net/invoices-{annee}?restype=container&comp=list&sv=2019-12-12&ss=b&srt=sco&sp=rl&se=2026-01-01T00:00:00Z&st=2025-01-01T00:00:00Z&spr=https&sig=%2BjCi7n8g%2F3849Rprey27XzHMoZN9zdVfDw6CifS6Y1U%3D"
        print(f"Traitement de l'année {annee} : {url}")
        
        # Récupération du XML
        response = requests.get(url)
        print(response.text)
        
        # Sauvegarde du XML
        xml_filename = f'assets/factures_{annee}.xml'
        os.makedirs('assets', exist_ok=True)
        with open(xml_filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        # Extraction des liens d'images à partir du XML
        factures_links = []
        tree = ET.parse(xml_filename)
        root = tree.getroot()
        for facture_link_id in root.findall('.//Name'):
            facture_image_link = f"https://projetocrstorageacc.blob.core.windows.net/invoices-{annee}/{facture_link_id.text}?sv=2019-12-12&ss=b&srt=sco&sp=rl&se=2026-01-01T00:00:00Z&st=2025-01-01T00:00:00Z&spr=https&sig=%2BjCi7n8g%2F3849Rprey27XzHMoZN9zdVfDw6CifS6Y1U%3D"
            factures_links.append(facture_image_link)
        
        # Optionnel meis pertinant selon moi: sauvegarde des liens en JSON
        with open(f'assets/factures_links_{annee}.json','w', encoding='utf-8') as file:
            factures_links_dict = {"factures_links": factures_links}
            file.write(json.dumps(factures_links_dict, indent=4))
        
        # Téléchargement et sauvegarde des images pour l'année courante
        images_dir = 'assets/images'
        os.makedirs(images_dir, exist_ok=True)
        loc = 0
        for link in factures_links:
            response = requests.get(link)
            image = Image.open(BytesIO(response.content))
            loc += 1
            image.save(f'assets/images/{annee}_image{loc}.png')
            print(f"Image {annee} - {loc} traitée et sauvegardée !")

if __name__ == '__main__':
    main()