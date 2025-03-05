from django.contrib import admin
from .models import Produit, Facture, User

# Register your models here.
admin.site.register(Produit)
admin.site.register(User)
admin.site.register(Facture)