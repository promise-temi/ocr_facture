from get_data.models import Produit, User, Facture, FactureProduct

def ajouterProduit(name, prix):
    data = {
        "name" : name,
        "prix" : prix
    }
    #si le produit n'existe pas alors le créer
    if not Produit.objects.filter(name=name).exists():
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
    if not User.objects.filter(email=email).exists():
        user = User.objects.create(**data)


def ajouterFacture(facture_id, creation_date, user, total_price):
    data = {
        "facture_id" : facture_id,
        "creation_date" : creation_date,
        "user" : user
    }
    if not Facture.objects.filter(facture_id=facture_id).exists():
        facture = Facture.objects.create(**data)


def definirFactureProduits(facture, product, quantity):
    data = {
        "facture" : facture,
        "product" : product,
        "quantity" : quantity
    }
    factureProduits = FactureProduct.objects.create(**data)


#ajout d'une facture et de ses données dans l'ordre
def add_facture_full_pipeline(data_):
    image_text = data_[0]['image_text']
    qr_code_data = data_[0]['qrcode_text']

    #reccuperation des produits
    products = image_text['products']
    print(products)
    for product in products:
        product_name = product['product']
        product_price = product['price']
        ajouterProduit(product_name, product_price)

    #reccuperation des données utilisateur
    user_info = image_text
    print(user_info)
    name = user_info['name']
    email = user_info['email']
    address = user_info['home_adress']
    city = user_info['city']['city']
    state = user_info['city']['state']
    postal_code = user_info['city']['postal_code']
    genre = qr_code_data['genre']
    birthday = qr_code_data["birth"]
    ajouterUser(name, email, address, "user", genre, birthday)
        
        