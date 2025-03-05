from django.db import models

## Create your models here.



#Table Produits
class Produit(models.Model):
    name = models.CharField(max_length=250)
    prix = models.FloatField()


#Table Users

class User(models.Model):
    name = models.CharField(max_length=250)
    adress = models.CharField(max_length=500)
    type = models.CharField(max_length=10)


#Table Factures
class Facture(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Produit)
    products_quantity = models.CharField(max_length=250)
    total_price = models.FloatField()


