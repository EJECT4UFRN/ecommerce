from django.test import Client, TestCase
from model_mommy import mommy 
from checkout.models import CartItem
from django.core.urlresolvers import reverse

#Classe para teste de adição de produto ao carrinho
class CreateCartItemTestCase(TestCase):

	def setUp(self):
		self.product = mommy.make('catalogo.Product')
		self.client = Client()
		self.url = reverse(
			'checkout:create_cartitem', kwargs={'slug': self.product.slug}
		)

	def tearDown(self):
		self.product.delete()
		CartItem.objects.all().delete()

	#Teste simples de adição de produto
	def test_add_cart_item_simple(self):
		response = self.client.get(self.url)
		redirect_url = reverse('checkout:cart_item')

		#Verificação de url e de criação do produto no carrinho
		self.assertRedirects(response, redirect_url)
		self.assertEquals(CartItem.objects.count(), 1)


	#Se adicionarmos 2 vezes o mesmo produto, então ele deverá ter duas quantidades
	def test_add_cart_item_complex(self):
		response = self.client.get(self.url)
		response = self.client.get(self.url)
		cart_item = CartItem.objects.get()
		self.assertEquals(cart_item.quantity, 2)