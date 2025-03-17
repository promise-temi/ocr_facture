from get_data.models import Produit, User, Facture, FactureProduct

def ajouterProduit(name, prix):
    data = {
        "name" : name,
        "prix" : prix

    }
    produit = Produit.objects.create(**data)

def ajouterUser(name, email, adress, type, genre, birthday):
    data = {
        "name": name,
        "email": email,
        "adress": adress,
        "type": type,
        "genre": genre,
        "birthday": birthday
    }
    user = User.objects.create(**data)


def ajouterFacture(creation_date, user, total_price):
    data = {
        "creation_date" : creation_date,
        "user" : user
    }
    facture = Facture.objects.create(**data)


def definirFactureProduits(facture, product, quantity):
    data = {
        "facture" : facture,
        "product" : product,
        "quantity" : quantity
    }
    factureProduits = FactureProduct.objects.create(**data)


    #ajout d'une facture et de ses données dans l'ordre
    def add_facture_full_pipeline(ajouter_produit_data, ajouter_user_data, ajouter_facture_data, definir_facture_produits_data):
        # reccupération des produits dans la facture (sans relation juste un nom de produit et son prix)
        ajouterProduit(ajouter_produit_data)
        # reccuperation des données de l'utilisateur dans la facture (juste ses données a lui, sans relation)
        ajouterUser(ajouter_user_data)
        # ajout de la facture en question
        ajouterFacture(ajouter_facture_data)
        # ajout des produit contenu dans la facture ainsi que leurs quantité
        definirFactureProduits(definir_facture_produits_data)