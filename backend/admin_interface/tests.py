from django.test import TestCase
from modules.get_factures import getfacture
# Create your tests here.
class Test_facture(TestCase):
    def test_facture(self):
        getfacture()
