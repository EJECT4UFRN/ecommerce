from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, TemplateView
from .models import CartItem
from catalogo.models import Product
from django.contrib import messages
from django.forms import modelformset_factory
from django.core.urlresolvers import reverse_lazy

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

		return reverse_lazy('checkout:cart_item')


#Classe de exibição do formulário do carrinho
class CartItemView(TemplateView):

	template_name = 'checkout/cart.html'

	def get_form_set(self, clear=False):

		CartItemFormSet = modelformset_factory(
			CartItem, fields=('quantity',), can_delete=True, extra=0
		)
		session_key = self.request.session.session_key
		#Se houver sessão, então há mudanças no cart
		if session_key:
			if clear:
				formset = CartItemFormSet(
					queryset=CartItem.objects.filter(cart_key=session_key)
                )
			else:
			    formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key),
                    data=self.request.POST or None
                )
		else:
			formset = CartItemFormSet(queryset=CartItem.objects.none())
		return formset

	def get_context_data(self, **kwargs): 
		context = super(CartItemView, self).get_context_data(**kwargs)
		context['formset'] = self.get_form_set()
		return context

	def post(self, request, *args, **kwargs):
		formset = self.get_form_set()
		context = self.get_context_data(**kwargs)
		if formset.is_valid():
			formset.save()
			messages.success(request, 'Carrinho atualizado com sucesso')
			context['formset'] = self.get_form_set(clear=True)
		return self.render_to_response(context)


create_cartitem = CreateCartItemView.as_view()
cart_item = CartItemView.as_view()