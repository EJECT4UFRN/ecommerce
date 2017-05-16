from django.db import models

class CartItem(models.Model):

	cart_key = models.CharField('Chave do Carrinho', max_length=40, db_index=True)  #id do carrinho
	product = models.ForeignKey('catalogo.Product', verbose_name='Produto')
	quantity = models.PositiveIntegerField('Quantidade', default=1)
	price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

	class Meta:
		verbose_name = 'Item do carrinho'
		verbose_name_plural = 'Itens dos carrinhos'

	def __str__(self):
		return '{} [{}]'.format(self.product, self.quantity)


