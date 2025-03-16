from django.test import TestCase
import cv2
from PIL import Image 
import os

# Mes modules
from modules.image_to_text import image_to_text





class Test_IMG_To_TXT(TestCase):

    

    def test_image_to_text(self):
        #SETUP
        current_dir = os.path.dirname(__file__)
        # Construit le chemin absolu vers l'image
        image_path = os.path.join(current_dir, 'test_assets', 'FAC_2018_0002-114.png')
        image = Image.open(image_path)
        #TEST
        text_data, qr_code_data = image_to_text(image, "file")
        #doit me retourner un dictionnaire
        self.assertIsInstance(text_data, dict) 
        #ce dictionnaire doit contenir la clé text
        self.assertIn('text', text_data)
        #les données de clé text du dict retourné doit contenir du text
        self.assertIsInstance(text_data['text'], str)

        # dans ce texte je doit retrouver obligatoirement ces strings

        #id doit etre present
        self.assertRegex(text_data['text'], r"invoice\s+fac/\d{4}/\d+")
        #date doit etre presente
        self.assertRegex(text_data['text'], r'issue\s+date\s+\d{4}-\d{2}-\d{2}')
        #name doit etre présente 
        self.assertRegex(text_data['text'], r'bill\s+to\s+.*')
        #email doit etre presente
        self.assertRegex(text_data['text'], r'email\s+.+@.+\..+')
        #adresse doit etre presente
        self.assertRegex(text_data['text'], r'address\s+.*')
        #ville doit etre presente
        self.assertRegex(text_data['text'], r'\w*,\s+\w+\s+\d+')
        #doit contenir produit et quantité et total
        self.assertRegex(text_data['text'], r'.+\s+\d+\s+.+\s+\d+\.\d+')
        #doit contenir prix total
        self.assertRegex(text_data['text'], r'total\s+\d+\.\d+\s+euro')

    
