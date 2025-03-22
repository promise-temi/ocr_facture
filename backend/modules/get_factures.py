from get_data.models import Facture, User, Produit, FactureProduct
from django.db import connection

def main():
    getfacture()
    get_facture_related_user()

def getfacture():
    print("###################################################\n \n \n")
    data = Facture.objects.select_related('user').all()
    if data:
        print(Facture.objects.select_related('user').all())
        print(data)
        print("Base de données utilisée :", connection.settings_dict['NAME'])
        print("\n \n \n###################################################")
        return data
    else:
        print(Facture.objects.select_related('user').all())
        print("it is empty!!!")
        print("Base de données utilisée :", connection.settings_dict['NAME'])
        print("\n \n \n###################################################")

def get_facture_related_user():
    data = Facture.objects.select_related('user').all()
    if data:
        print(Facture.objects.select_related('user').all())
        print(data)
        print("Base de données utilisée :", connection.settings_dict['NAME'])
        print("\n \n \n###################################################")
        return data
    else:
        print(Facture.objects.select_related('user').all())
        print("it is empty!!!")
        print("Base de données utilisée :", connection.settings_dict['NAME'])
        print("\n \n \n###################################################")


def get_single_facture(id):
    facture = Facture.objects.get(facture_id=id)
    user = facture.user
    facture_produits = FactureProduct.objects.filter(facture=facture).select_related('product')
    print(facture_produits.values)

    return facture, user, facture_produits


if __name__ == "__main__":
    main()