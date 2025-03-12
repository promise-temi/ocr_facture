import pytesseract
import cv2
import requests
import numpy as np
from PIL import Image, ImageOps, ImageEnhance
from io import BytesIO

def main():
    image_to_text()
    url_image_to_text()

def image_to_text(image):
#réccupération de l'image
    try:
        image = cv2.imread(image)  
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    except:
        print('une erreur s\'est produite')

    #image to text grace à pytesseract
    text = pytesseract.image_to_string(image)
    if text:
        print(text)
        data = {'text': text}
        return data
    
def url_image_to_text(url):
#réccupération de l'image
    try:
        # response = requests.get(url).content
        # img_numpy_array = np.frombuffer(response, np.uint8)
        # image = cv2.imdecode(img_numpy_array, cv2.IMREAD_COLOR)
        response = requests.get(url)         # Télécharge l'image
        # 📌 1) Charger l’image avec PIL
        image = Image.open(BytesIO(response.content))
        # 2) Masquer la zone du QR code
        image = mask_qrcode(image)

        image_final = image_preprocessing(image)
        image_final = cv2.imread(image_final)  
    except:
        print('une erreur s\'est produite')

    #image to text grace à pytesseract
    text = pytesseract.image_to_string(image_final, lang='eng', config="--psm 6")
    if text:
        print(text)
        data = {'text': text}
        return data
            
def image_preprocessing(image):

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
    image_final.save(f'image_pretraitee.png')

    return 'image_pretraitee.png'



def mask_qrcode(pil_image):
    """
    Masque la zone du QR code (et éventuellement l'image à côté)
    en dessinant un rectangle blanc sur l'image.
    Ajuste les coordonnées selon la position exacte du QR code.
    """
    # Convertir l'image PIL en array OpenCV (numpy)
    image_cv = np.array(pil_image)

    # Récupérer les dimensions
    height, width = image_cv.shape[:2]

    # Par exemple, on suppose que le QR code et l'image font ~300x300 px en haut à droite.
    # Ajuste selon tes besoins :
    top_left = (width - 300, 0)    # coin supérieur gauche du rectangle
    bottom_right = (width, 150)    # coin inférieur droit du rectangle

    # Dessiner un rectangle blanc (-1 = rempli)
    cv2.rectangle(image_cv, top_left, bottom_right, (255, 255, 255), -1)
    
    # Reconvertir en PIL
    masked_pil = Image.fromarray(image_cv)
    # cv2.imshow(masked_pil)
    return masked_pil

if __name__ == "__main__":
    main()