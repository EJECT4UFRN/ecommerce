from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages


#Poderíamos criar uma função para cada página, ou utilizarmos classes based on views!
#def index(request):
#	return render(request, 'index.html')

#Class based views (para maior reutilização de códigos, transformamos uma função em uma classe)
#TemplateView já é oferecido pelo django!!!

User = get_user_model()

class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()


def contact(request):
	success = False
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.send_mail()
		success = True
	elif request.method == 'POST':
		messages.error(request, 'Formulário inválido')
	context = {
        'form': form,
        'success': success
    }
	return render(request, 'contact.html', context)

#Classe view para criação de usuário
#class RegisterView(CreateView):
#	form_class = UserCreationForm
#	template_name = 'register.html'
#	model = User
#	success_url = reverse_lazy('index') #o reverse_lazy evitaria um erro do reverse !

#register = RegisterView.as_view()