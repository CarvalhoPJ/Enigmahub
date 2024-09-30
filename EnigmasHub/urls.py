from django.urls import path
from .views import home_page, create_enigma, enigmas_list

urlpatterns = [
    path('', home_page, name='home'),
    path('criar-enigma/', create_enigma, name='create_enigma'),
    path('enigmas/', enigmas_list, name='enigmas'),
]
