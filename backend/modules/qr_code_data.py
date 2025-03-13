import re
import cv2
import numpy as np

def main():
    qr_code_data()


    
def get_genre(datas):
    print(datas)
    for data in datas:
        re_genre = re.search(r"cust:(\w+)",data)
        if re_genre:
            genre = re_genre.group(1)
            return genre
    
def get_time(datas):
    print(datas)
    for data in datas:
        re_time = re.search(r"\d{2}:\d{2}:\d{2}",data)
        if re_time:
            genre = re_time.group()
            return genre
        

def get_birth(datas):
    print(datas)
    for data in datas:
        re_birth = re.search(r"birth\s+(\d{4}-\d{2}-\d{2})",data)
        if re_birth:
            genre = re_birth.group(1)
            return genre



def qr_code_data(image):

    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Initialiser le détecteur de QR codes
    detector = cv2.QRCodeDetector()

    # Détecter et décoder le QR code
    data, bbox, _ = detector.detectAndDecode(image)
    if data:
        print("Données du QR code :", data)
        datas = data.lower().split('\n')
        arranged_datas = {
            'invoice_time': get_time(datas),
            'genre' : get_genre(datas),
            'birth' : get_birth(datas)
}
        return arranged_datas
    else:
        print("Aucun QR code détecté.")

if __name__ == "__main__" : 
    main()