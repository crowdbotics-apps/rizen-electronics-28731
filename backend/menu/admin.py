from django.contrib import admin
from .models import Review, Category, Item, Country, ItemVariant

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(ItemVariant)
admin.site.register(Review)

# Register your models here.
