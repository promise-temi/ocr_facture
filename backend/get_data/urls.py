from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('xml-to-text/', views.factures_xml_to_text, name='xml-to-text')
]
