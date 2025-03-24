from django.urls import path
from . import views

urlpatterns = [
    path('factures/', views.factures, name='factures'),
    path('info_facture/<path:facture_id>/', views.info_facture, name='info_facture'),
    path('clients/', views.clients, name='clients'),
    path('info_client/<path:client_id>/', views.info_client, name='info_client'),
]
