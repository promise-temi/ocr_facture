from get_data.models import Produit, User, Facture, FactureProduct 

def main():
    ajouterProduit()
    ajouterUser
    ajouterFacture()
    definirFactureProduits()

def ajouterProduit(name, prix):
    data = {
        "name" : name,
        "prix" : prix
    }
    #si le produit n'existe pas alors le créer
    if not Produit.objects.filter(name=name).exists():
        produit = Produit.objects.create(**data)

def ajouterUser(name, email, adress, city, state, postal_code, type, genre, birthday):
    data = {
        "name": name,
        "email": email,
        "adress": adress,
        "city": city,
        "state": state,
        "postal_code": postal_code,
        "type": type,
        "genre": genre,
        "birth_day": birthday
    }
    if not User.objects.filter(email=email).exists():
        user = User.objects.create(**data)


def ajouterFacture(facture_id, creation_date, email, total,total_produits, total_quantites):
    user_instance = User.objects.get(email=email)
    data = {
        "facture_id" : facture_id,
        "creation_date" : creation_date,
        "user" : user_instance,
        "total": total,
        "total_product": total_produits,
        "total_quantities": total_quantites,
    }
    if not Facture.objects.filter(facture_id=facture_id).exists():
        facture = Facture.objects.create(**data)
        return True
    else:
        return False
    


def definirFactureProduits(facture, product, quantity):
    facture_instance = Facture.objects.get(facture_id=facture)
    product_instance = Produit.objects.get(name=product)
    data = {
        "facture" : facture_instance,
        "product" : product_instance,
        "quantity" : quantity
    }
    factureProduits = FactureProduct.objects.create(**data)


#ajout d'une facture et de ses données dans l'ordre

if __name__ == "__main__":
    main()