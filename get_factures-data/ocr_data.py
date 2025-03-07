import easyocr
import requests

#reccuperation de mes liens
links = open('ocr_facture/get_factures-data/factures_links.txt').read()
print(links)

#transformation de mon str en list
links = list(links)

# Parcourir chaque lien et extraire le texte
for link in links:
    try:
        response = requests.get(link)  # Télécharger l'image
        response.raise_for_status()  # Vérifie si l'image a bien été récupérée
        
        image_bytes = response.content  # Extraire les données binaires de l'image
        result = reader.readtext(image_bytes, detail=0)  # OCR sur l'image

        print(f"Texte extrait de {link} :")
        print("\n".join(result))  # Afficher le texte extrait
        print("-" * 50)  # Séparateur

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement de {link} : {e}")