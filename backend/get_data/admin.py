from django.contrib import admin
from .models import Produit, Facture, User, FactureProduct, LogEntry, UserClusterFeatures

# Register your models here.
admin.site.register(Produit)
admin.site.register(User)
admin.site.register(Facture)
admin.site.register(FactureProduct)
admin.site.register(UserClusterFeatures)


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('level', 'method', 'path', 'status_code', 'view_name', 'ip_address', 'duration', 'created_at')
    list_filter = ('level', 'method', 'status_code', 'view_name')
    search_fields = ('path', 'message', 'view_name')
    ordering = ('-created_at',)