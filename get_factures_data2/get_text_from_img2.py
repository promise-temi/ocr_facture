import os
import pytesseract
import cv2

mes_images = os.listdir('ocr_facture/get_factures_data2/data/images/')

print(mes_images)





img = cv2.imread(f'ocr_facture/get_factures_data2/data/images/{mes_images[0]}')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Appliquer seuil pour convertir en image binaire
threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# Passe l'image par pytesseract
text = pytesseract.image_to_string(threshold_img)
# Imprime le texte extrait
print(text)