from django.test import TestCase
from modules.database.add_facture_pipeline import add_facture_full_pipeline

class Test_Add_To_Db(TestCase):

    def test_add_facture_full_pipeline(self):
        #SETUP
        data = [{'image_text': {'id': 'fac/2018/0005', 'date': '2018-11-17', 'name': 'rachel ramirez', 'email': ['patriciakelley@example.org'], 'home_adress': '7896 jones underpass', 'city': {'city': 'kennethborough', 'state': 'ct', 'postal_code': '89365'}, 'products': [{'product': 'visit money record ability', 'quantity': '1', 'price': '74.84'}], 'total': '74.84'}, 'qrcode_text': {'invoice_time': '18:13:00', 'genre': 'm', 'birth': '1989-05-20'}}]
        #TEST
        add_facture_full_pipeline(data)