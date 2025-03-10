import json
import requests
import cv2
import numpy as np
from PIL import Image, ImageOps, ImageEnhance
from io import BytesIO
import pytesseract

# Charger les liens des images depuis JSON
with open('data/factures_links.json') as file:
    file_data = json.load(file)

links = file_data['factures_links']
print(links)

loc = 0
for link in links:
    response = requests.get(link)
    
    # 📌 1) Charger l’image avec PIL
    image = Image.open(BytesIO(response.content))

    # 📌 2) Convertir en niveaux de gris
    image = ImageOps.grayscale(image)

    # 📌 3) Augmenter la netteté
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(4.0)

    # Convertir PIL -> OpenCV pour traitements avancés
    image_cv = np.array(image)
    image_cv = cv2.cvtColor(image_cv, cv2.COLOR_GRAY2BGR)  # Reconversion pour OpenCV

    # 📌 4) Appliquer un seuillage adaptatif pour améliorer le contraste
    image_cv = cv2.adaptiveThreshold(cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY),
                                     255,
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY,
                                     11, 2)

    
    # 📌 6) Amélioration de la résolution si nécessaire
    height, width = image_cv.shape[:2]
    if width < 1000:  # Augmenter la résolution si l'image est trop petite
        image_cv = cv2.resize(image_cv, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)

    # Convertir OpenCV -> PIL pour sauvegarde
    image_final = Image.fromarray(image_cv)

    # 📌 Sauvegarde de l’image améliorée
    loc += 1
    image_final.save(f'data/images/image_pretraitee{loc}.png')

    print(f"Image {loc} traitée et sauvegardée !")
