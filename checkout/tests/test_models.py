from django.test import TestCase
from model_mommy import mommy
from django.conf import settings
from checkout.models import CartItem, Order


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


class OrderTestCase(TestCase):

    def setUp(self):
        self.cart_item = mommy.make(CartItem)
        self.user = mommy.make(settings.AUTH_USER_MODEL)

    def test_create_order(self):
        Order.objects.create_order(self.user, [self.cart_item])
        self.assertEquals(Order.objects.count(), 1)
        order = Order.objects.get()
        self.assertEquals(order.user, self.user)
        order_item = order.items.get()
		self.assertEquals(order_item.product, self.cart_item.product)