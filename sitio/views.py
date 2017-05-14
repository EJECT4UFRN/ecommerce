from django.shortcuts import render
#from catalogo.models import Category, Product
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View, TemplateView

#Poderíamos criar uma função para cada página, ou utilizarmos classes based on views!
#def index(request):
#	return render(request, 'index.html')

#Class based views (para maior reutilização de códigos, transformamos uma função em uma classe)
#TemplateView já é oferecido pelo django!!!
class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()


def contact(request):
	success = False
	if request.method == 'POST':
		form = ContactForm(request.POST or None) #Se não for POST, passa None, ou seja, o mesmo que nada!
		if form.is_valid():
			form.send_mail()
			success = True
	else:
		form = ContactForm()

	context = {
		'form': form,
		'success': success
	}
	return render(request, 'contact.html', context)