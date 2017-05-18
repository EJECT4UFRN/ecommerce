from django.test import TestCase
from model_mommy import mommy
from checkout.models import CartItem


# Teste de modelo, pois utilizamos o sinal para determinar a remoção com quantidade=0
class CartItemTestCase(TestCase):

	def setUp(self):
		#Gerando 3 modelos com o mommy maker
		mommy.make(CartItem, _quantity=3)

	#Haviam 3, caso um seja 0, então, retornará apenas 2 (test de remoção para quantidade=0)
	def test_post_save_cart_item(self):
		cart_item = CartItem.objects.all()[0]
		cart_item.quantity = 0
		cart_item.save()	
		self.assertEquals(CartItem.objects.count(), 2)
