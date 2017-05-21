from django.shortcuts import get_object_or_404, redirect
from django.views.generic import RedirectView, TemplateView
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from catalogo.models import Product

from .models import CartItem, Order

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


class CheckoutView(LoginRequiredMixin, TemplateView):

    template_name = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
    	session_key = request.session.session_key
    	if session_key and CartItem.objects.filter(cart_key=session_key).exists():
    		cart_items = CartItem.objects.filter(cart_key=session_key)
    		order = Order.objects.create_order(user=request.user, cart_items=cart_items)
    	else:
    		messages.info(request, 'Não há intens no carrinho')
    		return redirect('checkout:cart_item')
    	return super(CheckoutView, self).get(request, *args, **kwargs)

create_cartitem = CreateCartItemView.as_view()
cart_item = CartItemView.as_view()
checkout = CheckoutView.as_view()