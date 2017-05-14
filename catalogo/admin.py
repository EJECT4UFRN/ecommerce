from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin): #deixar pagina admin mais amigavel
	list_display = ['name', 'slug'] 
	search_display = ['name', 'slug']

admin.site.register(Category)
admin.site.register(Product)
# Register your models here.
