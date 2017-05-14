from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
	#code = models.IntegerField(primary_key=True) #Caso eu queira que o admin digite o id da categoria
	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('ID', max_length=100) #CharField para passagem na url (url amigavel)

	#Pegar a data em que o modelo é criado !!
	created = models.DateTimeField('Criado em', auto_now_add=True)
	#Pegar a data em que o modelo é salvo (ultima modificacao)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'
		ordering = ['name'] #ordenando em ordem crescente pelos nomes

	def __str__(self):
		return self.name #apenas para aparecer o nome da classe na pagina admin

	def get_absolute_url(self):
		return reverse('catalogo:category', kwargs={'slug': self.slug})

class Product(models.Model):
	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('ID', max_length=100) #CharField
	category = models.ForeignKey('catalogo.Category', verbose_name='Categoria') #Chave estrangeira
	description = models.TextField('Descrição', blank=True) #blank true, ou seja, campo nao obrigatorio
	price = models.DecimalField('Preço', decimal_places=2, max_digits=8) #preços com no maximo 2 casas decimais

	#Pegar a data em que o modelo é criado !!
	created = models.DateTimeField('Criado em', auto_now_add=True)
	#Pegar a data em que o modelo é salvo (ultima modificacao)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'
		ordering = ['name'] #ordenando em ordem crescente pelos nomes

	def get_absolute_url(self):
		return reverse('catalogo:product', kwargs={'slug': self.slug})