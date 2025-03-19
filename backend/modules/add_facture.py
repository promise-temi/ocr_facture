from modules.add_facture_pipeline import ajouterFacture, ajouterProduit, ajouterUser, definirFactureProduits
from datetime import datetime

def main():
    add_facture_full_pipeline()
    try_affp()

def try_affp(data_):
    image_text = data_['image_text']
    qr_code_data = data_['qrcode_text']
    print('debut de l\'ajout a la bdd')
    return qr_code_data, image_text

#ajout d'une facture et de ses données dans l'ordre
def add_facture_full_pipeline(data_):
    image_text = data_['image_text']
    qr_code_data = data_['qrcode_text']
    print('debut de l\'ajout a la bdd')

    #reccuperation des produits
    products = image_text['products']
    print(products)
    for product in products:
        product_name = product['product']
        product_price = product['price']
        print(product_name)
        print(product_price)
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
    ajouterUser(name, email, address, city, state, postal_code, "user", genre, birthday)

    #recuperation de la facture
    facture_id = user_info['id']
    creation_date = user_info['date'] +" "+ qr_code_data['invoice_time']
    creation_date_formated = datetime.strptime(creation_date, '%Y-%m-%d %H:%M:%S')
    print("_________________________________________________")
    print(creation_date_formated)
    print("_________________________________________________")
    user_email = user_info['email']

    resultLog = ajouterFacture(facture_id, creation_date_formated, user_email)
    if not resultLog:
        print('la facture existe deja')
        return 'la facture existe deja'

    #reccuperation des produits dans la facture
    produits = user_info['products']
    for produit in produits:
        produit_nom = produit['product']
        produit_quantity = produit['quantity']
        facture_id_ = user_info['id']
        print("__________________________________\n\n")
        print(produit_nom)
        print(produit_quantity)
        print(facture_id_)
        print("__________________________________\n\n")
        definirFactureProduits(facture_id_, produit_nom, produit_quantity)
        
if __name__ == "__main__":
    main()