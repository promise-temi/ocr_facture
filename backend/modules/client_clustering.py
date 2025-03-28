import pandas as pd
from get_data.models import User, UserClusterFeatures


def main():

    def get_user_features():
        """
        Récupère les caractéristiques des utilisateurs à partir de la base de données.
        """
        user_features = UserClusterFeatures.objects.values(
            'user__state',
            'user__postal_code',
            'user__genre',
            'user__birth_day',
            'moyenne_total_factures',
            'moyenne_prix_produits',
            'nombre_factures',
            'code_postal_short'
        )
        return pd.DataFrame(list(user_features))

    df = get_user_features()

    df['age'] = pd.to_datetime('today').year - pd.to_datetime(df['user__birth_day']).dt.year
    df.drop(columns=['user__birth_day'], inplace=True)
    df.dropna(inplace=True)

    

    df.to_csv('modules/assets/user_features.csv', index=False)
