from get_data.models import Facture, User, Produit, FactureProduct
from django.db import connection
from django.db.models import Count, Sum



def get_client():
    data = User.objects.filter(type="user").annotate(
        nb_factures=Count('facture'),
        total_depense=Sum('facture__total')
    ).all()
    print(data)
    if data:
        return data