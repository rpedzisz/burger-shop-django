from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Burger
from .models import Skladnik
from .models import CartItem
from .models import Cart
from .models import Mieso
from .models import Rozmiar
from .models import UserExtended
from .models import Order

from .forms import DodajDoKoszykaForm, LoginForm
from .forms import RegisterForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
def main(request):
    uzytkownik = request.user
    kontekst = {'komunikat': 'Strona główna',
                'uzytkownik': uzytkownik,    }
    return render(request, 'main.html', kontekst)

def onas(request):
    uzytkownik = request.user
    kontekst = {'komunikat': 'Strona główna',
                'uzytkownik': uzytkownik, }
    return render(request, 'about.html', kontekst)
def kontakt(request):
    uzytkownik = request.user
    kontekst = {'komunikat': 'Strona główna',
                'uzytkownik': uzytkownik, }
    return render(request, 'contact.html', kontekst)


def menu(request):

    if (request.user.is_authenticated):

        burgery = Burger.objects.all()
        nazwa_uzytkownika = request.user.username
        uzytkownik = request.user
        form = DodajDoKoszykaForm(request.POST)
        kontekst = {
            'uzytkownik': uzytkownik,
            'komunikat': 'Witaj w menu',
            'burgery': burgery,
            'form': form,
        }
        return render(request, 'menu.html', kontekst)
    else:
        messages.warning(request, "Aby przeglądać menu należy się zalogować")
        return redirect('/bar/logowanie')


def menu_dodajdokoszyka(request, item_id):
    kontekst = {'komunikat': 'Witaj w menu'}
    burgery = Burger.objects.all()

    if request.method == 'POST':
        form = DodajDoKoszykaForm(request.POST)
        kontekst = {
            'burgery': burgery,
            'form': form,
        }
        if form.is_valid():
            cleandata=form.cleaned_data
            mieso = get_object_or_404(Mieso, nazwa = cleandata.get('mieso'))
            rozmiar = get_object_or_404(Rozmiar, nazwa = cleandata.get('rozmiar'))


            item = get_object_or_404(Burger, id=item_id)
            cartitem, created = CartItem.objects.get_or_create(item=item, user=request.user, mieso = mieso, rozmiar = rozmiar, cena_total=item.cena+mieso.cena+rozmiar.cena, ukonczone=False)


            cart = Cart.objects.filter(user=request.user, ukonczone=False)

            if cart.exists():
                cart = cart[0]
                if cart.items.filter(item_id=item_id, mieso=mieso, rozmiar=rozmiar).exists():
                    cartitem.ilosc += 1
                    cartitem.save()
                    cart.cena_total_cart = cart.get_items_price()
                    cart.save()
                else:
                    cart.items.add(cartitem)
                    cart.cena_total_cart = cart.get_items_price()
                    cart.save()
            else:
                cart = Cart.objects.create(user=request.user, cena_total_cart=0)
                cart.items.add(cartitem)
                cart.cena_total_cart = cart.get_items_price()
                cart.save()
                form = DodajDoKoszykaForm()
                ##messages.success(request, "Dodano pomyslnie")



        else:

                messages.warning(request, "Blad dodawania")

    else:
        form = DodajDoKoszykaForm()
    return redirect('/bar/menu')
   # return render(request, 'menu.html', kontekst)

def wyswietl_koszyk(request):
    if request.user.is_authenticated:


        uzytkownik = request.user
        cart = Cart.objects.filter(user=request.user, ukonczone=False)
        uzytkownik_extended = UserExtended.objects.get(user=uzytkownik.id)

        if cart.exists():
            cart = cart[0]

            kontekst = {

                'uzytkownik' : uzytkownik,
                'uzytkownik_extended' : uzytkownik_extended,
                'cart': cart
            }


            return render(request, 'koszyk.html', kontekst)
        else:
            kontekst1 = {

                'uzytkownik': uzytkownik,
                'uzytkownik_extended': uzytkownik_extended,

            }

            return render(request, 'koszyk.html', kontekst1)
    else:
        messages.warning(request, "Aby przeglądać koszyk należy się zalogować")

        return redirect('/bar/logowanie')


def usun_z_koszyka(request, item_id):
    cart = Cart.objects.filter(user=request.user, ukonczone=False)



    if cart.exists():
        cart = cart[0]
        cart.items.filter(id=item_id).delete()
        cart.cena_total_cart = cart.get_items_price()
        cart.save()

    uzytkownik = request.user
    uzytkownik_extended = UserExtended.objects.get(user=uzytkownik.id)
    kontekst = {

        'uzytkownik': uzytkownik,
        'uzytkownik_extended': uzytkownik_extended,
        'cart': cart
    }

    return render(request, 'koszyk.html', kontekst)








def register(request):

 if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
        login = request.POST["login"]
        password = request.POST["password"]
        imie = request.POST["imie"]
        nazwisko = request.POST["nazwisko"]
        adres = request.POST["adres"]
        miasto = request.POST["miasto"]
        telefon = request.POST["telefon"]
        user, created = User.objects.get_or_create(username=login)
        if (created):
            user.set_password(password)
            user.save()
            user_extended, created_extended = UserExtended.objects.get_or_create(user=user, imie=imie,
                                                                                 nazwisko=nazwisko, adres=adres,
                                                                                 miasto=miasto, telefon=telefon)
            user_extended.save()
            messages.success(request, "Pomyślnie zarejestrowano")
            return redirect('/bar/rejestracja')
        else:
            messages.warning(request, "Użytkownik już istnieje")

    else:
        return redirect('/bar/rejestracja')

    if (not request.user.is_authenticated):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    else:
        return redirect('/bar/rejestracja')

 else:
     uzytkownik = request.user
     form = RegisterForm()
     context = {'form': form,
                'uzytkownik' : uzytkownik}
     return render(request, 'register.html', context)



def logowanie(request):
    uzytkownik = request.user
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["login"]
            password = request.POST["password"]
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)

                messages.success(request, "Pomyślnie zalogowano")
                return redirect('/bar/logowanie')
            else:
                messages.warning(request, "Nieprawidłowe dane")
                return redirect('/bar/logowanie')
        else:
            return redirect('/bar/logowanie')

        if (request.user.is_authenticated):
            messages.warning(request, "Już jesteś zalogowany")
            return render(request, 'login.html')
        else:
            kontekst = {'form': form,
                       'uzytkownik': uzytkownik}
            return render(request, 'login.html', kontekst)

    else:
        form = LoginForm()
        kontekst = {'form': form,
                    'uzytkownik': uzytkownik}

        return render(request, 'login.html', kontekst)


def wyloguj(request):
    if (request.user.is_authenticated):
        logout(request)
        messages.success(request, "Wylogowano pomyślnie")
        return redirect('/bar')


def dodaj_do_zamowien(request):
    cart = Cart.objects.get(user=request.user, ukonczone=False)

    if cart is not None:
        for cartitem in cart.items.all():
            cartitem.ukonczone = True
            cartitem.save()

        cart.ukonczone = True
        cart.save()
        user_extended = UserExtended.objects.get(user = request.user)
        order, created = Order.objects.get_or_create(user=request.user, user_extended=user_extended, cart=cart)

        order.save()
        messages.success(request, "Dodano zamówienie do listy zamówień")
    else:
        messages.warning(request, "Koszyk jest pusty")

    return redirect('/bar/koszyk')

def zamowienia(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            orders = Order.objects.filter(ukonczone=False).order_by('order_time')

            uzytkownik = request.user
            kontekst = {
                'uzytkownik' : uzytkownik,
                'orders' : orders,
            }
            return render(request, 'zamowienia.html', kontekst)
        else:
            HttpResponse("Strona dostępna tylko dla adminów")
    else:
        HttpResponse("Zaloguj sie")

def usun_z_zamowien(request, item_id):
    order = Order.objects.get(id = item_id, user=request.user, ukonczone=False)
    if order is not None:

        order.ukonczone = True
        order.save()
    return redirect('/bar/zamowienia')












