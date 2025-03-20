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


if __name__ == "__main__":
    main()