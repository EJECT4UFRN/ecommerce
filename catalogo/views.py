from django.shortcuts import render, get_object_or_404	
from .models import Category, Product
from django.views import generic
from django.views.generic import View, ListView

#Classe based on view. o ListView já é oferecido pelo django !!
class ProductListView(generic.ListView):
	model = Product
	template_name = 'catalogo/product_list.html'
	paginate_by = 3 #sistema de paginação do django (caso você queira ter mais páginas para listagem de algo)
					#Nesse caso, existiriam apenas 3 produtos por página!
product_list = ProductListView.as_view()

#Função para impressão de produtos
#def product_list(request):
#	context = {
#		'products': Product.objects.all()
#	}
#	return render(request, 'catalogo/product_list.html', context)

#def category(request,slug):
#	category = Category.objects.get(slug=slug)
#	context = {
#		'current_category': category,
#		'product_list': Product.objects.filter(category=category),
#	}
#	return render(request, 'catalogo/category.html', context)

class CategoryListView(generic.ListView):
	def get_queryset(self):
		#Maneira de puxar o modelo com o slug pela url
		return Product.objects.filter(category__slug=self.kwargs['slug'])

	#Função para carregar a variável current_category (nome da categoria para template)
	def get_context_data(self, **kwargs):
		context = super(CategoryListView, self).get_context_data(**kwargs)
		context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
		return context

	template_name = 'catalogo/category.html'
	paginate_by = 3

category = CategoryListView.as_view()

def product(request,slug):
	product = Product.objects.get(slug=slug)
	context = {
		'product': product
	}
	return render(request, 'catalogo/product.html', context)