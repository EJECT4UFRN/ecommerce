from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',  views.product_list, name='product_list'),
	url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'), #[\w_-] qualquer caractere com _ ou -
	url(r'^produto/(?P<slug>[\w_-]+)/$', views.product, name='product'),
]