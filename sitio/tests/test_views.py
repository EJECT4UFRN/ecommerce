
from django.test import TestCase, Client
from django.sitio.urlresolvers import reverse

class IndexViewTestCase(TestCase): #Classe de teste para views

	
    def setUp(self):
        self.client = Client()
		self.url = reverse('index')

	def tearDown(self):
		pass

	def test_status_code(self): #testar retorno da pagina html
		response = self.client.get(self.url) #pegar o resultado, em número, da resposta do browser
		self.assertEquals(response.status_code, 200) #testar se a resposta for 200 (se sim, está tudo ok)

	def test_template_used(self): #testar se um template esta sendo usado
		response = self.client.get(self.url) #pegar o resultado, em número, da resposta do browser	
		self.assertTemplateUsed(response, 'index.html') #teste para verificar se o usuario esta usando o template index.html


