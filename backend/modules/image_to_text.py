import pytesseract
import cv2
import requests
import numpy as np
from PIL import Image
from io import BytesIO
# mon module
from modules.image_preprocessing import image_preprocessing, mask_qrcode
from modules.qr_code_data import qr_code_data

def main():
    image_to_text()

    
def image_to_text(data_, type):
#réccupération de l'image
    try:
        if type == 'url':
            url = data_
            response = requests.get(url)         # Télécharge l'image
            # Charger l’image avec PIL
            image = Image.open(BytesIO(response.content))

        if type == 'file':
            image = data_
        
        try:
            # reccuperer les données du qr code
            qr_code_data_ = qr_code_data(image)
        except:
            print("une erreur s'est produite avec la reception du qr code")

        # 2) Masquer la zone du QR code
        image = mask_qrcode(image)

        image_final = image_preprocessing(image)
        image_final = cv2.imread(image_final)  
    except:
        print('une erreur s\'est produite')

    #image to text grace à pytesseract
    text = pytesseract.image_to_string(image_final, lang='eng', config="--psm 6")
    #petit nettoyage du texte
    text = text.lower().replace("]", "l")
    if text:
        print(text)
        data = {'text': text}
        return data, qr_code_data_
            


if __name__ == "__main__":
    main()