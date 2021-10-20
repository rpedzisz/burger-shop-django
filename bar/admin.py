from django.contrib import admin
from bar.models import Burger
from bar.models import CartItem
from bar.models import Cart
from bar.models import Skladnik
from bar.models import Mieso
from bar.models import Rozmiar
from bar.models import UserExtended
from bar.models import Order

from . import models
from django.forms import Textarea
from django.db.models.fields import TextField


admin.site.register(Cart)
admin.site.register(Burger)
admin.site.register(Skladnik)
admin.site.register(CartItem)
admin.site.register(Mieso)
admin.site.register(Rozmiar)
admin.site.register(UserExtended)
admin.site.register(Order)
""" 
class SkladnikInline(admin.TabularInline):
    model = models.Skladnik
    fields = ['nazwa']
    extra = 4
    max_num = 10
@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    inlines = [SkladnikInline]
    search_fields = ['nazwa']
    list_per_page = 10
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
    }

    def save_model(self, request, obj, form, change):
        obj.save()

"""