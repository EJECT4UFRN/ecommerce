from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, TemplateView
from .models import CartItem
from catalogo.models import Product
from django.contrib import messages

class CreateCartItemView(RedirectView):

	#Função de redirecionamento de url
	#args e kwargs são parâmetros passados pela url
	def get_redirect_url(self, *args, **kwargs):
		product = get_object_or_404(Product, slug=self.kwargs['slug'])
		if self.request.session.session_key is None: #Forçando a geração de uma sessão
			self.request.session.save()
		cart_item, created = CartItem.objects.add_item(self.request.session.session_key, product)
		if created:
			messages.success(self.request, 'Produto adicionado com sucesso')
		else:
			messages.success(self.request, 'Produto atualizado com sucesso')

		return product.get_absolute_url()


class CartDetailItemView(TemplateView):
	template_name = 'checkout/cart.html'
	def get_context_data(self, **kwargs):
		context = super(CartItemView, self).get_context_data(**kwargs)
		return context
create_cartitem = CreateCartItemView.as_view()