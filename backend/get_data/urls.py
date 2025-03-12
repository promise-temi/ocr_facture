from django.urls import path
from . import views

urlpatterns = [
    path('add-invoice-page/', views.add_invoice_page, name='add-invoice_page'),
    path('add-invoice/', views.add_invoice, name='add-invoice'),
]
