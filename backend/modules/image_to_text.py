import pytesseract
import cv2
import requests
import numpy as np

def main():
    image_to_text()
    url_image_to_text()

def image_to_text(image):
#réccupération de l'image
    try:
        image = cv2.imread(image)  
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
        response = requests.get(url).content
        img_numpy_array = np.frombuffer(response, np.uint8)
        image = cv2.imdecode(img_numpy_array, cv2.IMREAD_COLOR)
    except:
        print('une erreur s\'est produite')

    #image to text grace à pytesseract
    text = pytesseract.image_to_string(image)
    if text:
        print(text)
        data = {'text': text}
        return data
            

if __name__ == "__main__":
    main()