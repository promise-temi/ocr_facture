import pandas as pd

from get_data.models import Facture, User, Produit, FactureProduct
from django.db import connection
from django.db.models import Count, Sum
import pandas as pd
from dateutil.relativedelta import relativedelta
import datetime

def make_user_df():
    user = User.objects.filter(type="user")
    user_data = list(user.values())
    print(user_data)
    df = pd.DataFrame(user_data)
    print('____________________________')
    print(df.head())
    df.to_csv('modules/assets/dataframes/users.csv', index=False)

def make_facture_df():
    facture = Facture.objects.all()
    facture_data = list(facture.values())
    print(facture_data)
    df = pd.DataFrame(facture_data)
    print('____________________________')
    print(df.head())
    df.to_csv('modules/assets/dataframes/factures.csv', index=False)

def make_produit_df():
    produit = Produit.objects.all()
    produit_data = list(produit.values())
    print(produit_data)
    df = pd.DataFrame(produit_data)
    print('____________________________')
    print(df.head())
    df.to_csv('modules/assets/dataframes/produits.csv', index=False)


def make_produits_facture_df():
    produits_facture = FactureProduct.objects.all()
    produits_facture_data = list(produits_facture.values())
    print(produits_facture_data)
    df = pd.DataFrame(produits_facture_data)
    print('____________________________')
    print(df.head())
    df.to_csv('modules/assets/dataframes/produits_facture.csv', index=False)


def client_clust():
    make_user_df()
    make_facture_df()
    make_produit_df()
    make_produits_facture_df()


#reccupération des df
df_facture = pd.read_csv('modules/assets/dataframes/factures.csv')
df_produits = pd.read_csv('modules/assets/dataframes/produits.csv')
df_produits_facture = pd.read_csv('modules/assets/dataframes/produits_facture.csv')
df_users = pd.read_csv('modules/assets/dataframes/users.csv')

#creation d'un nouveau df
df = pd.DataFrame()

# reccuperation de l'id
df['id_utilisateur'] = df_users['id']
#reccuperation du code postal reduit
df['code_postal_short'] = df_users['postal_code'].astype(str).str[:2]
#reccuperation du code postal complet
df['code_postal_complet'] = df_users['postal_code']
#reccuperation de la ville
df['ville'] = df_users['city']
#reccuperation de létat
df['etat'] = df_users['state']
#reccuperation du genre
df['genre'] = df_users['genre']

# Recuperation de la collone date de naissance
df['date_naissance'] = pd.to_datetime(df_users['birth_day']).dt.date

# Reccuperation de lage a partir de la date de naissance
df['age'] = df['date_naissance'].apply(lambda x: relativedelta(datetime.date.today(), x).years)
# reccuperation de la moyenne des total par facture. en gereral avec nous il depense combien
df['avg_total'] = (
    df_facture
    .groupby('user_id')['total']
    .transform('mean')
)

print(df)

df.to_csv('modules/assets/dataframes/client_clust_data.csv', index=False)