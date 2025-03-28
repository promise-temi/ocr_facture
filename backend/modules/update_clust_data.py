from django.db.models import Avg, Count, F, Func, Value, CharField
from get_data.models import User, UserClusterFeatures


# Remplace LEFT par SUBSTR, compatible SQLite
class Substr(Func):
    function = 'SUBSTR'
    arity = 3  # SUBSTR(field, start_pos, length)


def update_all_user_features():
    users = User.objects.annotate(
        moyenne_total_factures=Avg('facture__total'),
        moyenne_prix_produits=Avg('facture__factureproduct__product__prix'),
        nombre_factures=Count('facture'),
        code_postal_short=Substr(
            F('postal_code'),
            Value(1),  # Commencer au premier caractère
            Value(2),  # Prendre les deux premiers caractères
            output_field=CharField()
        )
    )

    for user in users:
        UserClusterFeatures.objects.update_or_create(
            user=user,
            defaults={
                'moyenne_total_factures': user.moyenne_total_factures,
                'moyenne_prix_produits': user.moyenne_prix_produits,
                'nombre_factures': user.nombre_factures,
                'code_postal_short': user.code_postal_short
            }
        )
