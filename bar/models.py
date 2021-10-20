from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings


class UserExtended(models.Model):
    class Meta: verbose_name_plural = 'Users Extended'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imie = models.CharField(verbose_name=u"imie", max_length=50)
    nazwisko = models.CharField(verbose_name=u"nazwisko", max_length=50)
    adres = models.CharField(verbose_name=u"adres", max_length=150)
    miasto = models.CharField(verbose_name=u"miasto", max_length=150)
    telefon = models.IntegerField(verbose_name=u"telefon")

    def __str__(self):
        return self.user.username



class Skladnik(models.Model):
    class Meta: verbose_name_plural = 'Skladniki'
    nazwa = models.CharField(verbose_name=u"składnik", max_length=50)
    cena = models.DecimalField(max_digits=5, decimal_places=2, default=51
                               )
    def __str__(self):
        return self.nazwa


class Burger(models.Model):
    class Meta: verbose_name_plural = 'Burgery'
    obraz = models.CharField(verbose_name='obraz', max_length=100)
    nazwa = models.CharField(verbose_name='Burger', max_length=100)
    opis = models.CharField(verbose_name='Opis', max_length=255)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    skladniki = models.ManyToManyField(Skladnik)

    def get_skladniki(self):
        return self.skladniki.all()

    def __str__(self):
        return self.nazwa

class Mieso(models.Model):
    class Meta: verbose_name_plural = 'Mieso'
    nazwa = models.CharField(verbose_name='mieso', max_length=100)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nazwa


class Rozmiar(models.Model):
    class Meta: verbose_name_plural = 'Rozmiary'

    nazwa = models.CharField(verbose_name='rozmiar', max_length=100)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nazwa


class CartItem(models.Model):

    item = models.ForeignKey(Burger, on_delete=models.CASCADE)
    mieso = models.ForeignKey(Mieso, on_delete=models.CASCADE)
    rozmiar = models.ForeignKey(Rozmiar, on_delete=models.CASCADE)
    cena_total =  models.DecimalField(max_digits=5, decimal_places=2)
    ilosc = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    ukonczone = models.BooleanField(default=False)

    def get_object_price(self):
        return self.cena_total*self.ilosc

    def calculate_price(self):
        return (self.item.cena + self.mieso.cena + self.rozmiar.cena)*self.ilosc

    def __str__(self):
        return self.item.nazwa


class Cart(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    ukonczone = models.BooleanField(default=False)
    cena_total_cart = models.DecimalField(max_digits=5, decimal_places=2)


    def get_items(self):
        return self.items.all()

    def get_items_price(self):
        return sum([item.cena_total*item.ilosc for item in self.items.all()])

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_extended = models.ForeignKey(UserExtended, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    ukonczone = models.BooleanField(default=False)















