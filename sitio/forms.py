from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
	name = forms.CharField(label='Nome')
	email = forms.EmailField(label='E-mail') #require=False diria que o campo nao é obrigatorio!
	message = forms.CharField(label='Mensagem', widget=forms.Textarea)

	#Função para enviar um e-mail simples (EU -> EU)
	def send_mail(self):
			name = self.cleaned_data['name']
			email = self.cleaned_data['email']
			message = self.cleaned_data['message']
			message = 'Nome: {0}\nE-mail:{1}\n{2}'.format(name, email, message) #Formatando a mensagem para melhor exibicao
			#ENVIANDO E-MAIL DE MIM PARA EU MESMO.
			send_mail('Contato do seu site', message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
