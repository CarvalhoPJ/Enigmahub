from django.urls import path
from .views import home_page, create_enigma, enigmas_list,login_view,register_view,logout_view

urlpatterns = [
    path('', home_page, name='home'),
    path('criar-enigma/', create_enigma, name='create_enigma'),
    path('enigmas/', enigmas_list, name='enigmas'),

    path('login/', login_view, name='login'),

    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

]
