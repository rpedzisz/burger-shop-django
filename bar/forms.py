from django import forms
from .models import Mieso
from .models import Rozmiar

class DodajDoKoszykaForm (forms.Form):

    mieso = forms.ModelChoiceField(queryset=Mieso.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    rozmiar = forms.ModelChoiceField(queryset=Rozmiar.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))




class RegisterForm(forms.Form):
   login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}) ,required=True)
   imie = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
   nazwisko = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
   adres = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
   miasto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
   telefon = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)

class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}) ,required=True)