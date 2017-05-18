from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin): #deixar pagina admin mais amigavel
	list_display = ['name', 'slug'] 
	search_display = ['name', 'slug']
	list_filter = ['created', 'modified']

class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
