from django.shortcuts import render

def index(request):
	context = {
		'title': 'Django E-Commerce'
	}
	return render(request, 'index.html', context)

def product_list(request):
    return render(request, 'product_list.html')


def product(request):
		return render(request, 'product.html')