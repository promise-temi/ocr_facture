from django.urls import path
from . import views

urlpatterns = [
    path('factures/', views.factures, name='factures'),
]
