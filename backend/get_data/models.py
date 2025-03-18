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


#Table des produits dans la facture 
class FactureProduct(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
