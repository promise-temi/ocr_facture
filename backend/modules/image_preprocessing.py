from PIL import Image, ImageOps, ImageEnhance
import cv2
import numpy as np
def main():
    image_preprocessing() 
    mask_qrcode()

def image_preprocessing(image):
    # Convertir en niveaux de gris
    image = ImageOps.grayscale(image)

    # Augmenter la netteté
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(4.0)

    # Convertir PIL -> OpenCV pour traitements avancés
    image_cv = np.array(image)
    image_cv = cv2.cvtColor(image_cv, cv2.COLOR_GRAY2BGR)  # Reconversion pour OpenCV

    #Appliquer un seuillage adaptatif pour améliorer le contraste
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

    # Dessiner un rectangle blanc pour cacher le QR code et l'image à côté
    cv2.rectangle(image_cv, top_left, bottom_right, (255, 255, 255), -1)
    
    # Reconvertir en PIL
    masked_pil = Image.fromarray(image_cv)
    # cv2.imshow(masked_pil)
    return masked_pil

if __name__ == "__main__":
    main()