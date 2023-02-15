from django.contrib import admin
from.models import Article,Panier,Achat
from .models import Category

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Panier)
admin.site.register(Achat)