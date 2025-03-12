import pytesseract
import cv2

def main():
    image_to_text()

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
            

if __name__ == "__main__":
    main()