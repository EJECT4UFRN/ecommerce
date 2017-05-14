from django.template import Library

register = Library()

@register.inclusion_tag('pagination.html')
def pagination(request, paginator, page_obj):
	context = {}
	context['paginator'] = paginator
	context['request'] = request
	context['page_obj'] = page_obj
	getvars = request.GET.copy()
	if 'page' in getvars:
		del getvars['page']
	if len(getvars) > 0:
		#Se a URL já existir algo com ?search=2, não retirar isso da URL !!!
		context['getvars'] = '&{0}'.format(getvars.urlencode())
	else:
		context['getvars'] = ''
	return context