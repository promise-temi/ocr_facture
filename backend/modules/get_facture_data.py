import re

def main():
    get_invoice_id()
    get_invoice_date()
    get_invoice_name()
    get_invoice_email()
    get_invoice_home_adress()
    get_invoice_city()
    get_invoice_products()
    get_invoice_total()



# réccupération de l'id dans la facture
def get_invoice_id(datas):
    for data in datas:
        id_find = re.search(r"fac/\d{4}/\d+", data)
        if id_find:
            id = id_find.group()
            return id
        else:
            print('no match')


# réccupération de la date dans la facture
def get_invoice_date(datas):
    for data in datas:
        date_find = re.search(r"issue\s+date\s+(\d{4}-\d{2}-\d{2})", data)
        if date_find:
            date = date_find.group(1)
            return date
        else:
            print('no match') 


#réccupération du nom du client dans la facture
def get_invoice_name(datas):
    for data in datas:
        name_find = re.search(r"bill\s+to\s+(.*)", data)
        if name_find:
            name = name_find.group(1)
            return name
        else:
            print('no match')


#réccupération de l'email du client dans la facture
def get_invoice_email(datas):
    emails = []
    for data in datas:
        email_find = re.search(r"email\s+(.+@.+\..+)", data)
        if email_find:
            email = email_find.group(1)
            emails.append(email)
        else:
            print('no match')
    return emails


#réccupération de l'adresse du client dans la facture
def get_invoice_home_adress(datas):
    for data in datas:
        adress_find = re.search(r'address\s+(.*)', data)
        if adress_find:
            adress = adress_find.group(1)
            return adress
        else:
            print('no match')


#réccupération de la ville, de l'etat et du code postal du client dans la facture
def get_invoice_city(datas):
    for data in datas:
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
def get_invoice_products(datas):
    products_datas = []
    for data in datas:
        find_products = re.search(r'(.*)\.\s+(\d+).+\s+(\d+\.\d+)\s+euro', data)
        if find_products:
            products_data = {
                'product' : find_products.group(1),
                'quantity' : find_products.group(2),
                'price' : find_products.group(3)
            }
            products_datas.append(products_data)
        else:
            print('no match')
    return products_datas


#réccupération du prix total dans la facture 
def get_invoice_total(datas):
    for data in datas:
        find_total = re.search(r'total\s+(\d+\.\d+)\s+euro', data)
        if find_total:
            total = find_total.group(1)
            return total
        else:
            print('no match')

def get_facture_data_pipeline(data_):
    facture_text = data_['text']
    facture_text_list = data_['text'].lower().replace("]", "l").split('\n')
    print("________________________________")
    print(facture_text_list)
    print("________________________________")
    facture_datas =  {
        "id": get_invoice_id(facture_text_list),
        "date" : get_invoice_date(facture_text_list),
        "name": get_invoice_name(facture_text_list),
        "email": get_invoice_email(facture_text_list),
        "home_adress": get_invoice_home_adress(facture_text_list),
        "city": get_invoice_city(facture_text_list),
        "products": get_invoice_products(facture_text_list),
        "total": get_invoice_total(facture_text_list),
    }
    return facture_datas




if __name__ == "__main__":
    main()