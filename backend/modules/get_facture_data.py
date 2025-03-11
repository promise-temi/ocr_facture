import pandas as pd
import re

# réccupération de l'id dans la facture
def get_invoice_id(data):
    id_find = re.search(r"fac/\d{4}/\d+", data)
    if id_find:
        id = id_find.group()
        return id
    else:
        print('no match')

# réccupération de la date dans la facture
def get_invoice_date(data):
    date_find = re.search(r"issue\s+date\s+(\d{4}-\d{2}-\d{2})", data)
    if date_find:
        date = date_find.group(1)
        return date
    else:
        print('no match') 

#réccupération du nom du client dans la facture
def get_invoice_name(data):
    name_find = re.search(r"bill\s+to\s+(.*)", data)
    if name_find:
        name = name_find.group(1)
        return name
    else:
        print('no match')

#réccupération de l'email du client dans la facture
def get_invoice_email(data):
    email_find = re.search(r"email\s+(.+@.+\..+)", data)
    if email_find:
        email = email_find.group(1)
        return email
    else:
        print('no match')

#réccupération de l'adresse du client dans la facture
def get_invoice_home_adress(data):
    adress_find = re.search(r'address\s+(.*)', data)
    if adress_find:
        adress = adress_find.group(1)
        return adress
       
    else:
        print('no match')

#réccupération de la ville, de l'etat et du code postal du client dans la facture
def get_invoice_city(data):
    city_find = re.search(r'(\w+),\s+(\w+)\s+(\d+)', data)
    if city_find:
        city_data = {
            'city' : city_find.group(1),
            'state' : city_find.group(2),
            'postal_code' : city_find.group(3)
        }
        return city_data
    else:
        print('no match')

#réccupération des produits, de leurs quantités et prix dans la facture
def get_invoice_products(data):
    find_products = re.search(r'(.*)\.\s+(\d+).+\s+(\d+\.\d+)\s+euro', data)
    if find_products:
        products_data = {
            'product' : find_products.group(1),
            'quantity' : find_products.group(2),
            'price' : find_products.group(3)
        }
        return products_data
    else:
        print('no match')