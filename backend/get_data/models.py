from django.db import models

## Create your models here.



#Table Produits
class Produit(models.Model):
    name = models.CharField(max_length=250, unique=True)
    prix = models.FloatField()


#Table Users

class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=300, null=True, blank=False, unique=True)
    adress = models.CharField(max_length=500)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=10, default="user")
    genre = models.CharField(max_length=10, null=True)
    birth_day = models.DateField(null=True)


#Table Factures
class Facture(models.Model):
    facture_id = models.CharField(max_length=100, null=True)
    creation_date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField(null=True)
    total_product = models.IntegerField(null=True)
    total_quantities = models.IntegerField(null=True)


#Table des produits dans la facture 
class FactureProduct(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class UserClusterFeatures(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    moyenne_prix_produits = models.FloatField(null=True, blank=True)
    moyenne_total_factures = models.FloatField(null=True, blank=True)
    nombre_factures = models.IntegerField(null=True, blank=True)
    code_postal_short = models.CharField(max_length=10, null=True, blank=True)
    

# Table des logs
class LogEntry(models.Model):
    level = models.CharField(max_length=20)
    message = models.TextField()
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    status_code = models.PositiveSmallIntegerField()
    view_name = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    extra_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

