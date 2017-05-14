

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail

class IndexViewTestCase(TestCase): #Classe de teste para views
	
    #def setUp(self):
     #   self.client = Client()
	#	self.url = reverse('index')

	#def tearDown(self):
	#	pass

	def test_status_code(self): #testar retorno da pagina html
		client = Client()
		response = client.get('/') 
		self.assertEqual(response.status_code, 200) #testar se a resposta for 200 (se sim, está tudo ok)

	def test_template_used(self): #testar se um template esta sendo usado
		client = Client()
		response = client.get('/') 
		self.assertTemplateUsed(response, 'index.html') #teste para verificar se o usuario esta usando o template index.html

#Testes do formulario de contato
class ContactViewTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		self.url = reverse('contact')

	#Teste do template e do cliente(navegador)
	def test_view_ok(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'contact.html')

	#Teste de páginas (paginação)
#	def test_context(self):
#		response = self.client.get(self.url)
#		self.assertTrue('products' in response.context)
#		product_list = response.context['products']
#		self.assertEquals(product_list.count(), 3)
#		paginator = response.context['paginator']
#		self.assertEquals(paginator.num_pages, 4)

	#Teste de página nao existir, devido a paginação
#	def test_page_not_found(self):
#		response = self.client.get('{}?page=5'.format(self.url))
#		self.assertEquals(response.status_code, 404)

	#Teste do formulario (se houve erro ou nao)
	def test_form(self):
		data = {'name': '', 'email': '', 'message': ''}
		response = self.client.post(self.url, data)
		self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
		self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
		self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')

	#teste de envio de e-mail
	def test_form_ok(self):
		data = {'name': 'test', 'email': 'test@test.com', 'message': 'test'}
		response = self.client.post(self.url, data)
		self.assertTrue(response.context['success'])
		self.assertEquals(len(mail.outbox), 1) #se o email foi enviado é testado aqui
		#self.assertEquals(len(mail.outbox[0].subject, 'Contato do seu site')) #teste para ver se o assunto do email é o mesmo
