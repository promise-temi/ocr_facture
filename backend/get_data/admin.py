from django.contrib import admin
from .models import Produit, Facture, User, FactureProduct

# Register your models here.
admin.site.register(Produit)
admin.site.register(User)
admin.site.register(Facture)
admin.site.register(FactureProduct)