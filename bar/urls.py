from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('/menu', views.menu, name='menu'),
    path('/menu/<item_id>', views.menu_dodajdokoszyka, name='menu_formularz'),
   path('/koszyk', views.wyswietl_koszyk, name='koszyk'),
path('/koszyk/usun_z_koszyka/<item_id>', views.usun_z_koszyka, name='usun_z_koszyka'),
path('/rejestracja', views.register, name='rejestracja'),
path('/logowanie', views.logowanie, name='logowanie'),
path('/onas', views.onas, name='onas'),
path('/kontakt', views.kontakt, name='kontakt'),


path('/wyloguj', views.wyloguj, name='wyloguj'),
path('/koszyk/dodajdozamowien', views.dodaj_do_zamowien, name='dodaj_do_zamowien'),
path('/zamowienia', views.zamowienia, name='zamowienia'),
path('/zamowienia/usun_z_zamowien/<item_id>', views.usun_z_zamowien, name='usun_z_zamowien'),

]