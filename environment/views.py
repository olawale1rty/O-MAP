from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from django.views import generic
from environment.models import Incidence, Country
#from django.views.decorators.cache import cache_page


# Create your views here.
class Home(generic.TemplateView):
	template_name = 'incidence_list.html'


def Country_data(request):
    countries = serialize('geojson', Country.objects.all())
    return HttpResponse(countries, content_type='json')



def Incidence_data(request):
	incidence = serialize('geojson', Incidence.objects.all())
	return HttpResponse(incidence,content_type='json')