from django.db import models

## Create your models here.



#Table Produits
class Produits(models.Model):
    name = models.CharField(max_length=250)
    prix = models.FloatField()


#Table Users

class Users(models.Model):
    name = models.CharField(max_length=250)
    adress = models.CharField(max_length=500)
    type = models.CharField(max_length=10)


#Table Factures
class Factures(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    products = models.ManyToManyField(Produits)
    products_quantity = models.CharField(max_length=250)
    total_price = models.FloatField()


