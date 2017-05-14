from django.shortcuts import render
#from catalogo.models import Category, Product

def index(request):
	return render(request, 'index.html')